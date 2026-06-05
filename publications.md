---
title: "Publications"
kicker: "Research Output"
description: "Template publication list."
section: publications
lang: en
alternate_url: /zh/publications/
permalink: /publications/
---

<p class="muted">Source: <a href="{{ site.data.publications.source_url }}" target="_blank" rel="noopener">{{ site.data.publications.source }}</a>. Updated on {{ site.data.publications.captured_on }}.</p>

{% include citation-chart.html %}

{% include publication-list.html items=site.data.publications.items sortable=true %}
