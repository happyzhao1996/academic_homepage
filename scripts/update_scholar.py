#!/usr/bin/env python3
"""Refresh local Google Scholar data files for the Jekyll site.

Google Scholar has no public API for this profile data, so this script performs
a conservative HTML fetch and only writes files after it has parsed all required
sections successfully. If Scholar blocks the request, existing data stays intact.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_USER_ID = "qc6CJjYAAAAJ"
BASE_URL = "https://scholar.google.com"
PROFILE_PATH = ROOT / "_data" / "profile.yml"
PUBLICATIONS_PATH = ROOT / "_data" / "publications.yml"
CITATION_HISTORY_PATH = ROOT / "_data" / "citation_history.yml"


def strip_tags(value: str) -> str:
    value = re.sub(r"<script\b.*?</script>", "", value, flags=re.S | re.I)
    value = re.sub(r"<style\b.*?</style>", "", value, flags=re.S | re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"\s+([,;:)])", r"\1", value)
    value = re.sub(r"([(])\s+", r"\1", value)
    return value


def yaml_quote(value: object) -> str:
    text = "" if value is None else str(value)
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def fetch(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def scholar_url(user_id: str, cstart: int = 0, pagesize: int = 20) -> str:
    params = {
        "user": user_id,
        "hl": "en",
        "cstart": str(cstart),
        "pagesize": str(pagesize),
    }
    return f"{BASE_URL}/citations?" + urllib.parse.urlencode(params)


def parse_metrics(page: str) -> dict[str, str]:
    keys = {
        "citations": "citations",
        "h-index": "h_index",
        "i10-index": "i10_index",
    }
    metrics: dict[str, str] = {}

    for row in re.findall(r"<tr[^>]*>.*?</tr>", page, flags=re.S | re.I):
        cells = [strip_tags(cell) for cell in re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.S | re.I)]
        if len(cells) < 2:
            continue
        key = keys.get(cells[0].lower())
        if key:
            metrics[key] = cells[1]

    if len(metrics) != 3:
        values = [
            strip_tags(item)
            for item in re.findall(r'<td class="gsc_rsb_std">\s*(.*?)\s*</td>', page, flags=re.S)
        ]
        if len(values) >= 5:
            metrics = {
                "citations": values[0],
                "h_index": values[2],
                "i10_index": values[4],
            }

    if len(metrics) != 3:
        raise ValueError("Could not parse citation metrics from Google Scholar.")
    return metrics


def parse_citation_history(page: str) -> list[dict[str, int | str]]:
    years = re.findall(r'<span class="gsc_g_t"[^>]*>\s*(\d{4})\s*</span>', page, flags=re.S)
    citations = re.findall(r'<span class="gsc_g_al">\s*([\d,]+)\s*</span>', page, flags=re.S)
    items = [
        {"year": year, "citations": int(citation.replace(",", ""))}
        for year, citation in zip(years, citations)
    ]
    if not items:
        raise ValueError("Could not parse yearly citation history from Google Scholar.")
    return items


def parse_publication_rows(page: str) -> list[dict[str, str]]:
    rows = re.findall(r'<tr class="gsc_a_tr".*?</tr>', page, flags=re.S)
    publications: list[dict[str, str]] = []
    for row in rows:
        title_anchor_match = re.search(r'(<a[^>]*class="gsc_a_at"[^>]*>.*?</a>)', row, flags=re.S)
        if not title_anchor_match:
            continue
        title_anchor = title_anchor_match.group(1)
        title_match = re.search(r">(.*?)</a>", title_anchor, flags=re.S)
        href_match = re.search(r'href="([^"]+)"', title_anchor, flags=re.S)
        grays = re.findall(r'<div class="gs_gray">(.*?)</div>', row, flags=re.S)
        citation_match = re.search(r'<td class="gsc_a_c"[^>]*>(.*?)</td>', row, flags=re.S)
        year_match = re.search(r'<td class="gsc_a_y"[^>]*>(.*?)</td>', row, flags=re.S)

        citation_text = strip_tags(citation_match.group(1)) if citation_match else ""
        citation_digits = re.search(r"\d+", citation_text.replace(",", ""))
        year_text = strip_tags(year_match.group(1)) if year_match else ""
        year_digits = re.search(r"\d{4}", year_text)

        publications.append(
            {
                "title": strip_tags(title_match.group(1)) if title_match else "",
                "authors": strip_tags(grays[0]) if len(grays) > 0 else "",
                "venue": strip_tags(grays[1]) if len(grays) > 1 else "",
                "year": year_digits.group(0) if year_digits else "",
                "citations": citation_digits.group(0) if citation_digits else "",
                "scholar_url": urllib.parse.urljoin(BASE_URL, html.unescape(href_match.group(1)))
                if href_match
                else "",
            }
        )
    return publications


def parse_original_article_link(page: str) -> str:
    match = re.search(r'<a[^>]*class="gsc_oci_title_link"[^>]*href="([^"]+)"', page, flags=re.S)
    return html.unescape(match.group(1)).strip() if match else ""


def add_original_article_links(publications: list[dict[str, str]]) -> int:
    found = 0
    for item in publications:
        detail_url = item.get("scholar_url", "")
        if not detail_url:
            continue
        try:
            time.sleep(0.5)
            original_link = parse_original_article_link(fetch(detail_url))
        except Exception as exc:
            print(f"Warning: could not fetch article link for {item['title']}: {exc}", file=sys.stderr)
            continue
        if original_link:
            item["link"] = original_link
            found += 1
    return found


def parse_publications(first_page: str, user_id: str, limit: int = 20) -> list[dict[str, str]]:
    publications: list[dict[str, str]] = []
    seen: set[str] = set()

    page = first_page
    cstart = 0
    pagesize = min(max(limit, 1), 20)
    while True:
        rows = parse_publication_rows(page)
        for row in rows:
            key = row["title"]
            if key and key not in seen:
                publications.append(row)
                seen.add(key)
                if len(publications) >= limit:
                    return publications

        if len(rows) < pagesize or cstart >= 400:
            break
        cstart += pagesize
        time.sleep(1.0)
        page = fetch(scholar_url(user_id, cstart=cstart, pagesize=pagesize))

    if not publications:
        raise ValueError("Could not parse publication rows from Google Scholar.")
    return publications


def render_publications(publications: list[dict[str, str]], captured_on: str, source_url: str) -> str:
    lines = [
        'source: "Google Scholar"',
        f"source_url: {yaml_quote(source_url)}",
        f"captured_on: {yaml_quote(captured_on)}",
        "items:",
    ]
    for item in publications:
        lines.extend(
            [
                f"  - title: {yaml_quote(item['title'])}",
                f"    authors: {yaml_quote(item['authors'])}",
                f"    venue: {yaml_quote(item['venue'])}",
                f"    year: {yaml_quote(item['year'])}",
                f"    citations: {yaml_quote(item['citations'])}",
            ]
        )
        if item.get("link"):
            lines.append(f"    link: {yaml_quote(item['link'])}")
    return "\n".join(lines) + "\n"


def render_citation_history(
    history: list[dict[str, int | str]], metrics: dict[str, str], captured_on: str, source_url: str
) -> str:
    max_yearly = max(int(item["citations"]) for item in history)
    lines = [
        'source: "Google Scholar"',
        f"source_url: {yaml_quote(source_url)}",
        f"captured_on: {yaml_quote(captured_on)}",
        f"total: {yaml_quote(metrics['citations'])}",
        f"max: {max_yearly}",
        "items:",
    ]
    for item in history:
        lines.extend(
            [
                f"  - year: {yaml_quote(item['year'])}",
                f"    citations: {int(item['citations'])}",
            ]
        )
    return "\n".join(lines) + "\n"


def update_profile_metrics(profile_text: str, metrics: dict[str, str], captured_on: str) -> str:
    lines = profile_text.splitlines()
    current_lang = ""
    in_metrics = False
    updated: list[str] = []

    for line in lines:
        if re.match(r"^[A-Za-z_-]+:\s*$", line):
            current_lang = line.split(":", 1)[0]
            in_metrics = False
        elif current_lang in {"en", "zh"} and line == "  metrics:":
            in_metrics = True
        elif in_metrics and line.startswith("  ") and not line.startswith("    "):
            in_metrics = False

        if in_metrics:
            if line.startswith("    citations:"):
                line = f"    citations: {yaml_quote(metrics['citations'])}"
            elif line.startswith("    h_index:"):
                line = f"    h_index: {yaml_quote(metrics['h_index'])}"
            elif line.startswith("    i10_index:"):
                line = f"    i10_index: {yaml_quote(metrics['i10_index'])}"
            elif line.startswith("    updated:"):
                line = f"    updated: {yaml_quote(captured_on)}"
        updated.append(line)

    return "\n".join(updated) + "\n"


def write_if_changed(path: Path, content: str, dry_run: bool) -> bool:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old == content:
        return False
    if not dry_run:
        path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh Google Scholar YAML data.")
    parser.add_argument("--user-id", default=os.environ.get("SCHOLAR_USER_ID", DEFAULT_USER_ID), help="Google Scholar user id.")
    parser.add_argument("--limit", type=int, default=20, help="Maximum publications to fetch, capped at 20.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and parse without writing files.")
    parser.add_argument("--skip-links", action="store_true", help="Skip Scholar detail-page fetches for article links.")
    args = parser.parse_args()

    user_id = args.user_id.strip()
    limit = min(max(args.limit, 1), 20)
    source_url = f"{BASE_URL}/citations?user={user_id}&hl=en"
    captured_on = _dt.date.today().isoformat()
    print(f"Fetching Google Scholar profile: {source_url}")
    first_page = fetch(scholar_url(user_id, cstart=0, pagesize=limit))

    metrics = parse_metrics(first_page)
    history = parse_citation_history(first_page)
    publications = parse_publications(first_page, user_id, limit=limit)
    linked_publications = 0 if args.skip_links else add_original_article_links(publications)

    profile_text = PROFILE_PATH.read_text(encoding="utf-8")
    outputs = {
        PUBLICATIONS_PATH: render_publications(publications, captured_on, source_url),
        CITATION_HISTORY_PATH: render_citation_history(history, metrics, captured_on, source_url),
        PROFILE_PATH: update_profile_metrics(profile_text, metrics, captured_on),
    }

    changed = [path for path, content in outputs.items() if write_if_changed(path, content, args.dry_run)]
    prefix = "Would update" if args.dry_run else "Updated"
    if changed:
        for path in changed:
            print(f"{prefix}: {path.relative_to(ROOT)}")
    else:
        print("Scholar data already up to date.")

    print(
        "Parsed "
        f"{len(publications)} publications, "
        f"{len(history)} yearly citation points, "
        f"{metrics['citations']} total citations, "
        f"{linked_publications} original article links."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Scholar update failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
