---
title: Congresses
menu: top-nav
menu-index: 2
---


A [world map of all congresses](https://www.google.com/maps/d/edit?hl=en&authuser=0&mid=zW44vtqWxj2c.kPfPEi8R_fog) is available. A click on the markers in the map provides detailed information. The list of all ITC conferences can be found below. Please click on the link to get detailed information about the selected event.

Some [basic statistics]({{ site.baseurl }}/congress_statistics.html) about the ITC congresses are also available. Information on ITC can also be found in Wikipedia ["International Teletraffic Congress"](https://en.wikipedia.org/wiki/International_Teletraffic_Congress).

<p>
<b><a href="https://itc34.itc-conference.org">ITC 34: Teletraffic Engineering for Smart Networking</a></b><br/>
4. - 16. September 2022, Shenzhen, China

{% assign congresses = site.congresses | reverse %}
{% for c in congresses %}
<p>
    <a href="{{ c.url | relative_url }}">
    <b>
    {% if c.conftitle %}
        ITC {{ c.path | slice: -6, 3 | abs }}: <em>{{ c.conftitle }}</em>
    {% else %}
        ITC {{ c.path | slice: -6, 3 | abs }}
    {% endif %}
    </b>
    </a><br/>
    {{ c.confdate }}
</p>
{% endfor %}
