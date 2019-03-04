---
title: News
menu: top-nav
menu-index: 1
---

{% for post in site.posts %}
<div>
  <h1><a href="{{ post.url }}"> {{ post.title }}</a></h1>
  <p>
    {% capture postdate %}
    {{ post.date }}
    {% endcapture %}
    <i> {% include insertpostdate date=postdate %}</i>, by: {{ post.author }}<br/>
    {{ post.excerpt | strip_html | strip_newlines | truncate: 100 }}
    <a href="{{ post.url }}"> Read more </a>
  </p>
  <br/><br/>
</div>
{% endfor %}
