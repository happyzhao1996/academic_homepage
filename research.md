---
title: "Research"
kicker: "Research Program"
description: "Research directions, device concepts, and patent records when available."
section: research
lang: en
alternate_url: /zh/research/
permalink: /research/
---

{% assign profile = site.data.profile.en %}

<section id="research" class="section-block">
  <h2>Research</h2>
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
  <h2>Patents</h2>
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
