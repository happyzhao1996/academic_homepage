---
title: "Education & Experience"
kicker: "Academic Path"
description: "Education and appointment history."
section: education
lang: en
alternate_url: /zh/education/
permalink: /education/
---

{% assign profile = site.data.profile.en %}

<section id="education" class="section-block">
  <h2>Education</h2>
  {% if profile.education and profile.education.size > 0 %}
    <div class="timeline">
      {% for item in profile.education %}
        <article class="timeline__item">
          <div class="timeline__period">{{ item.period }}</div>
          <h3>{{ item.title }}</h3>
          <p class="timeline__meta">{{ item.organization }}{% if item.location %}, {{ item.location }}{% endif %}</p>
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
  <h2>Experience</h2>
  <div class="timeline">
    {% for item in profile.experience %}
      <article class="timeline__item">
        <div class="timeline__period">{{ item.period }}</div>
        <h3>{{ item.title }}</h3>
        <p class="timeline__meta">{{ item.organization }}{% if item.location %}, {{ item.location }}{% endif %}</p>
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
