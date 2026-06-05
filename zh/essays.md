---
title: "生活随笔"
kicker: "笔记"
description: "模板笔记与文章。"
section: essays
lang: zh
alternate_url: /essays/
permalink: /zh/essays/
---

{% assign ui = site.data.ui.zh %}

<div class="tabs" data-tabs>
  <div class="tab-list" role="tablist" aria-label="文章分类">
    <button type="button" data-tab-target="all">{{ ui.all_posts }}</button>
    {% assign sorted_categories = site.categories | sort %}
    {% for category in sorted_categories %}
      <button type="button" data-tab-target="{{ category[0] | slugify }}">{{ category[0] }}</button>
    {% endfor %}
  </div>

  <section data-tab-panel="all">
    <div class="post-grid">
      {% for post in site.posts %}
        {% include post-card.html %}
      {% endfor %}
    </div>
  </section>

  {% for category in sorted_categories %}
    <section data-tab-panel="{{ category[0] | slugify }}" hidden>
      <div class="post-grid">
        {% for post in category[1] %}
          {% include post-card.html %}
        {% endfor %}
      </div>
    </section>
  {% endfor %}
</div>
