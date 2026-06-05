---
title: "学术会议"
kicker: "报告与海报展示"
description: "学术会议与报告记录。"
section: conferences
lang: zh
alternate_url: /conferences/
permalink: /zh/conferences/
---

{% assign profile = site.data.profile.zh %}

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
