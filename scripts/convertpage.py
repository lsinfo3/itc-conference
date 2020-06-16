#!/usr/bin/env python
# -*- coding: utf-8 -*-

# requires BeautifulSoup and html2text package
# usage:
#   ./convertpage.py [--anyfrontmatterkey=value]... files...

import traceback
import bs4
import html2text
import sys
import re
import os

html2text.config.BODY_WIDTH = 0

frontmatterdict = {
    # "layout": "default",
}
files = []
failed = []

for i in sys.argv[1:]:
    m = re.match(r"--(.+)=(.+)", i)
    if m:
        frontmatterdict[m.group(1)] = m.group(2)
    else:
        files.append(i)

if not files or (len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help")):
    print("No files specified")

    print("Converts ITC html pages to jekyll markdown.")
    print("Usage: convertpage.py [--anyfrontmatterkey=value]... files...")
    print("Example: convertpage.py \"--title=custom title with spaces\" --somekey=foo page.html")
    sys.exit(1)

for currentfile in files:
    try:
        print("Processing file {}...".format(currentfile))

        with open(currentfile, "r") as f:
            html = bs4.BeautifulSoup(f.read(), 'html.parser')

        content = html.select(".cont_left .neos-contentcollection")[0]  # type: bs4.element.Tag
        header = html.select(".cont_left .entry-header")
        if header:
            content.insert(0, header[0])

        for i in ( "href", "src" ):
            for tag in content.find_all(attrs={ i: True }):
                url = str(tag[i])
                print("found link: " + url)
                # transform outgoing links to the same site to absolute links
                url = re.sub(r'^.*?:.*itc-conference.org(.*)', r'\1', url)

                # skip outgoing links
                if re.match(r'^.*?:', url):
                    continue

                if not url.startswith("/"):
                    if url.startswith(".."):
                        url = url.replace("../", "")
                    url = "/" + url

                url = re.sub(r'.*_Resources/Persistent/.*/(.*)', r'/assets/Persistent/\1', url)
                url = re.sub(r'en/', "", url)

                if url.startswith("/"):
                    url = "{{ site.baseurl }}" + url

                print("fixed link: " + url)
                tag[i] = url

        for i in content.find_all("figure"):
            if i.has_attr("class") and i.img:
                i.img.insert_after('{{:class="{}"}}'.format(str(i["class"][0])))

        # print(content.prettify())

        title = html.select(".breadcrumb .current")
        title = title[0] if title else html.title
        title = title.string.strip()
        basename = title.find(" - itc-conference.org")
        if basename != -1:
            title = title[:basename]
        frontmatterdict["title"] = title

        markdown = html2text.html2text(str(content))
        markdown = "\n".join([ i.rstrip() for i in markdown.splitlines() ])
        markdown = re.subn(r'\s*(\{:class=.*\})', r'\1', markdown)[0]
        markdown = re.subn(r'(\S)\n(\w)', r'\1<br/>\n\2', markdown, flags=re.MULTILINE)[0]

        frontmatter = "\n".join([ "{}: {}".format(str(k), str(v)) for k, v in frontmatterdict.items() ])
        final = "---\n{}\n---\n\n{}".format(frontmatter, markdown)
        print(final)

        with open(os.path.splitext(currentfile)[0] + ".md", "w") as f:
            f.write(final)

    except:  # noqa pylint: disable=bare-except
        failed.append((currentfile, traceback.format_exc()))

for fname, exc in failed:
    print(fname, "failed:\n", exc)

sys.exit(min(len(failed), 255))
