---
title: ITC Library
menu: top-nav
menu-index: 4
sidebar: itc-library
---

<!--- these divs are necessary otherwise the liquid code appears in plain text --->
<div>
{% assign congresses = site.itc-library | reverse %}

{% for c in congresses %}
    {% assign loopindex = forloop.index0 | modulo: 3 %}

    {% if loopindex == 0 %}
        <div class="container columns-4-4-4 typo3-neos-nodetypes-threecolumn">
    {% endif %}

    <div class="column neos-contentcollection">
        <div class="typo3-neos-nodetypes-textwithimage">
            <figure class="typo3-neos-alignment-center">
                <a href="{{ c.url | relative_url }}">
                    <img src="{{ site.baseurl }}/assets/Persistent/{{ c.sprite }}">
                </a>
            </figure>
            <div>
                <p style="text-align: center;">
                    <a href="{{ c.url | relative_url }}">ITC {{ c.path | slice: -5, 2 | abs }}</a>
                </p>
            </div>
        </div>
    </div>

    {% if loopindex == 2 or forloop.last == true %}
        </div>
        <div class=" typo3-neos-nodetypes-html">
            <br style="clear:both;">
        </div>
    {% endif %}
{% endfor %}
</div>
