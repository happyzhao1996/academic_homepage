---
title: "Notes & Archive"
kicker: "Notes"
description: "Template notes and posts."
section: essays
lang: en
alternate_url: /zh/essays/
permalink: /essays/
---

{% assign ui = site.data.ui.en %}

<div class="tabs" data-tabs>
  <div class="tab-list" role="tablist" aria-label="Post categories">
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
