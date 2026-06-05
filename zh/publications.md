---
title: "论文"
kicker: "研究成果"
description: "模板论文列表。"
section: publications
lang: zh
alternate_url: /publications/
permalink: /zh/publications/
---

<p class="muted">来源：<a href="{{ site.data.publications.source_url }}" target="_blank" rel="noopener">{{ site.data.publications.source }}</a>；更新日期：{{ site.data.publications.captured_on }}。</p>

{% include citation-chart.html %}

{% include publication-list.html items=site.data.publications.items sortable=true %}
