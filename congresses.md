---
title: Congresses
menu: top-nav
menu-index: 2
---


A [world map of all congresses](https://www.google.com/maps/d/edit?hl=en&authuser=0&mid=zW44vtqWxj2c.kPfPEi8R_fog) is available. A click on the markers in the map provides detailed information. The list of all ITC conferences can be found below. Please click on the link to get detailed information about the selected event.

{% assign congresses = site.congresses | reverse %}
{% for c in congresses %}
<p>
    <a href="{{ c.url }}">
      <b>ITC {{ c.path | slice: -6, 3 | abs }}:  <em> {{ c.conftitle }} </em></b><br/>
    </a>
    {{ c.confdate }}
</p>
{% endfor %}
