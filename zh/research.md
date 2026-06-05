---
title: "研究"
kicker: "研究方向"
description: "研究方向、器件概念，以及可公开的专利记录。"
section: research
lang: zh
alternate_url: /research/
permalink: /zh/research/
---

{% assign profile = site.data.profile.zh %}

<section id="research" class="section-block">
  <h2>研究</h2>
  <div class="research-grid">
    {% for item in profile.research %}
      <article class="research-card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
      </article>
    {% endfor %}
  </div>
</section>

{% if profile.patents and profile.patents.size > 0 %}
<section id="patents" class="section-block">
  <h2>专利</h2>
    <div class="timeline">
      {% for item in profile.patents %}
        <article class="timeline__item">
          <div class="timeline__period">{{ item.period }}</div>
          <h3>{{ item.title }}</h3>
          <p class="timeline__meta">{{ item.status }}</p>
        </article>
      {% endfor %}
    </div>
</section>
{% endif %}
