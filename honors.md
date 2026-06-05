---
title: "Honors"
kicker: "Recognition"
description: "Selected awards and honors."
section: honors
lang: en
alternate_url: /zh/honors/
permalink: /honors/
---

{% assign profile = site.data.profile.en %}

<section class="section-block">
  {% if profile.honors and profile.honors.size > 0 %}
    <div class="timeline">
      {% for item in profile.honors %}
        <article class="timeline__item">
          <div class="timeline__period">{{ item.period }}</div>
          <h3>{{ item.title }}</h3>
          <p class="timeline__meta">{{ item.organization }}</p>
        </article>
      {% endfor %}
    </div>
  {% else %}
    <p class="empty-state">{{ profile.empty.honors }}</p>
  {% endif %}
</section>

