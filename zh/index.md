---
layout: default
title: "主页"
description: "学术主页模板。"
section: home
lang: zh
alternate_url: /
permalink: /zh/
---

{% assign profile = site.data.profile.zh %}

<section class="section-block section-block--lead">
  <h2>关于我</h2>
  <p class="lead-copy">{{ profile.summary }}</p>
</section>

<section class="section-block">
  <h2>近期研究方向</h2>
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
  <h2>专业技能</h2>
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
  <h2>代表性论文</h2>
  {% assign selected_publications = site.data.selected_publications.items %}
  {% include publication-list.html items=selected_publications %}
  <p><a class="button-link" href="{{ '/zh/publications/' | relative_url }}">完整论文列表</a></p>
</section>
