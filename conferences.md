---
title: "Conferences"
kicker: "Talks & Posters"
description: "Conference presentations and academic meetings."
section: conferences
lang: en
alternate_url: /zh/conferences/
permalink: /conferences/
---

{% assign profile = site.data.profile.en %}

<section class="section-block">
  {% if profile.conferences and profile.conferences.size > 0 %}
    <div class="timeline">
      {% for item in profile.conferences %}
        <article class="timeline__item">
          <div class="timeline__period">{{ item.period }}</div>
          <h3>{{ item.title }}</h3>
          <p class="timeline__meta">{{ item.location }}</p>
        </article>
      {% endfor %}
    </div>
  {% else %}
    <p class="empty-state">{{ profile.empty.conferences }}</p>
  {% endif %}
</section>
