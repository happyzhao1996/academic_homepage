---
title: "学术服务"
kicker: "学术共同体"
description: "审稿、组织与专业服务。"
section: service
lang: zh
alternate_url: /service/
permalink: /zh/service/
---

{% assign profile = site.data.profile.zh %}

<section class="section-block">
  {% if profile.service and profile.service.size > 0 %}
    <div class="timeline">
      {% for item in profile.service %}
        <article class="timeline__item">
          <div class="timeline__period">{{ item.period }}</div>
          <h3>{{ item.title }}</h3>
          <p class="timeline__meta">{{ item.organization }}</p>
          {% if item.details %}
            <ul>
              {% for detail in item.details %}
                <li>{{ detail }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        </article>
      {% endfor %}
    </div>
  {% else %}
    <p class="empty-state">{{ profile.empty.service }}</p>
  {% endif %}
</section>
