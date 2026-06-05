---
layout: default
title: "Home"
description: "Academic homepage template."
section: home
lang: en
alternate_url: /zh/
---

{% assign profile = site.data.profile.en %}

<section class="section-block section-block--lead">
  <h2>About Myself</h2>
  <p class="lead-copy">{{ profile.summary }}</p>
</section>

<section class="section-block">
  <h2>Recent Research Profile</h2>
  <div class="research-grid">
    {% for item in profile.research %}
      <article class="research-card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="section-block">
  <h2>Experimental Skills</h2>
  <div class="skill-grid">
    {% for skill in profile.skills %}
      <article class="skill-card">
        <h3>{{ skill.category }}</h3>
        <p>{{ skill.items }}</p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="section-block">
  <h2>Selected Publications</h2>
  {% assign selected_publications = site.data.selected_publications.items %}
  {% include publication-list.html items=selected_publications %}
  <p><a class="button-link" href="{{ '/publications/' | relative_url }}">Full publication list</a></p>
</section>
