# Academic Homepage Template

A lightweight bilingual Jekyll template for academic personal homepages. The template keeps personal content in YAML files, can refresh Google Scholar data locally, and ships with placeholder records so it is easy to adapt without exposing private information.

## Preview

![Homepage preview](screenshot/crop_1.png)

![Publications and citation history preview](screenshot/crop_2.png)

## Quick Start

Install Ruby, Bundler, and the gems first:

```powershell
bundle install
```

On Windows, double-click `run_server.bat` to refresh Scholar data and start the local Jekyll preview. `run_server.ps1` does the same from PowerShell.

The preview runs at:

```text
http://127.0.0.1:4000/
```

## Scholar Refresh

The launch scripts run this before serving the site:

```powershell
python scripts/update_scholar.py --skip-links --limit 20
```

That updates:

- `_data/publications.yml`
- `_data/citation_history.yml`
- Scholar metrics inside `_data/profile.yml`

The default Scholar profile is Albert Einstein's public profile, used only as a safe example. To use your own profile, set `SCHOLAR_USER_ID` before launching the script, or run:

```powershell
python scripts/update_scholar.py --user-id <scholar_user_id> --limit 20 --skip-links
```

Google Scholar may block frequent automated requests. If that happens, the script exits without overwriting existing YAML files.

## Editing Content

Most personal content lives in `_data/profile.yml`. Update both the `en` and `zh` sections if you want the bilingual pages to stay aligned.

- Profile name, title, affiliation, portrait, links, research interests, metrics, education, experience, honors, service, conferences, skills, and patents: `_data/profile.yml`
- Navigation labels and section links: `_data/navigation.yml`
- Full publication records: `_data/publications.yml`
- Homepage selected publications: `_data/selected_publications.yml`
- Citation chart data: `_data/citation_history.yml`
- Essays and notes: `_posts/`
- Page text: `index.md`, `zh/index.md`, and the other top-level Markdown pages
- Styles: `assets/css/main.scss`

The default language is English at `/`; Chinese pages live under `/zh/`.

## License

This template is released under the Apache License 2.0. See `LICENSE`.
