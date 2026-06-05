---
title: "Academic Service"
kicker: "Community"
description: "Reviewing, organization, and professional service."
section: service
lang: en
alternate_url: /zh/service/
permalink: /service/
---

{% assign profile = site.data.profile.en %}

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
