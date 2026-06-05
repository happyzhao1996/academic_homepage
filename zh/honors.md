---
title: "获奖情况"
kicker: "荣誉奖励"
description: "代表性获奖情况。"
section: honors
lang: zh
alternate_url: /honors/
permalink: /zh/honors/
---

{% assign profile = site.data.profile.zh %}

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

