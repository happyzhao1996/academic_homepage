---
title: "教育与工作经历"
kicker: "学术经历"
description: "教育经历与工作经历。"
section: education
lang: zh
alternate_url: /education/
permalink: /zh/education/
---

{% assign profile = site.data.profile.zh %}

<section id="education" class="section-block">
  <h2>教育经历</h2>
  {% if profile.education and profile.education.size > 0 %}
    <div class="timeline">
      {% for item in profile.education %}
        <article class="timeline__item">
          <div class="timeline__period">{{ item.period }}</div>
          <h3>{{ item.title }}</h3>
          <p class="timeline__meta">{{ item.organization }}{% if item.location %}，{{ item.location }}{% endif %}</p>
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
    <p class="empty-state">{{ profile.empty.education }}</p>
  {% endif %}
</section>

<section id="experience" class="section-block">
  <h2>工作经历</h2>
  <div class="timeline">
    {% for item in profile.experience %}
      <article class="timeline__item">
        <div class="timeline__period">{{ item.period }}</div>
        <h3>{{ item.title }}</h3>
        <p class="timeline__meta">{{ item.organization }}{% if item.location %}，{{ item.location }}{% endif %}</p>
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
</section>
