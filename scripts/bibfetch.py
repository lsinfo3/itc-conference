#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Requirements: urllib, requests, pylatexenc

# See also https://bitbucket.org/bibsonomy/bibsonomy-python
# Get your API key at https://www.bibsonomy.org/settings?selTab=1
# Put username and API key in a file called APIKEY (first line username, second line key)

import bibsonomy
import sys
import os
from pylatexenc.latex2text import LatexNodes2Text
import requests

def get_api_credentials():
    username = ""
    key = ""
    missing = False

    try:
        with open(os.path.dirname(__file__) + "/APIKEY", "r") as f:
            username = f.readline().strip()
            key = f.readline().strip()
    except:
        missing = True

    if missing or not key or not username:
        print("Invalid APIKEY file.")
        print("Please put your username and API key, newline separated, in a file called 'APIKEY' in the script directory.")

    return (username, key)


def generate_bibsonomy_link(res):
    return "https://www.bibsonomy.org/bibtex/{}/itc".format(res.intra_hash)


def generate_bibtex(res):
    kvs = res.__dict__
    filter = ( "intra_hash", "entry_type", "inter_hash", "bibtex_key", "abstract", "url" )
    attribs = ",\n".join(
        [ "    {:13} = {{ {} }}".format(k, v) for k, v in kvs.items() if k not in filter ])

    return """@{entry_type}{{{bibtex_key},\n{attribs}\n}}""".format(
        **kvs, attribs=attribs)


def generate_html(postres):
    latexdecoder = LatexNodes2Text()
    res = {}

    # decode latex
    for k, v in postres.__dict__.items():
        try:
            res[k] = latexdecoder.latex_to_text(v)
        except AttributeError:
            # latex_to_text() fails if there is no latex in the string
            pass

    s = """<div class="item">
    <span class="pubauthors">{author}</span><br/>
    <span class="pubtitle">{title}</span><br/>""".format(
        author=res.get("author", res.get("editor", "No author")),
        title=res["title"]
    )

    if "booktitle" in res:
        s += "In <span class='pubbooktitle'>{booktitle}</span>.".format(**res)

    if "address" in res:
        s += "<span class='pubaddress'>{address}</span> ".format(**res)

    s += """<span class="year">{year}</span>.<br/>
    <a class="bibtexLink" href="javascript:toggleVis('{bibtex_key}')">[BibTeX]</a> """.format(**res)

    if "abstract" in res:
        s += """<a class="abstractLink" href="javascript:toggleVis('abstract_{bibtex_key}')">
        [Abstract]</a> """.format(**res)

    if "url" in res:
        s += "<a href='{url}' class='fileLink'>[Download]</a> ".format(**res)

    s += """<a href="{bibsonomy_url}" class="bibsonomyLink">[BibSonomy]</a>

    <div id="{bibtex_key}" style="display: none;" class="bibtex">{bibtex}</div>""".format(
        **res,
        bibsonomy_url=generate_bibsonomy_link(postres),
        bibtex=generate_bibtex(postres))

    if "abstract" in res:
        s += """\n<div id="abstract_{bibtex_key}" style="display: none;" class="abstract">
    <strong>Abstract:</strong> {abstract}</div>""".format(**res)

    s += "\n</div>\n"
    return s

def gen_page(tag, posts):
    html = []
    year = None

    for post in posts:
        res = post.resource

        if not year:
            year = res.year

        if "booktitle" in res.__dict__:
            booktitle = res.booktitle
            if booktitle.startswith("{") and booktitle.endswith("}"):
                res.booktitle = booktitle[1:-1].strip()

        html.append((res.title, generate_html(res)))

    html.sort(key=lambda x: x[0])

    frontmatter = {
        "title": tag.upper(),
        "year": year if year else "TODO" if posts else "Not available",
    }


    lines = [ "---" ]
    lines += [ "{}: {}".format(k, v) for k, v in frontmatter.items() ]
    lines.append("---\n")
    lines += [ i[1] for i in html ]

    if not posts:
        lines.append("No entries available.")

    with open("{}.html".format(tag), "w") as f:
        f.write("\n".join(lines))

def download_pdfs(tag, posts):
    """Download all PDFs of this conference to a corresponding local folder"""
    for post in posts:
        res = post.resource
        if "url" in res.__dict__ and res.url:
            fullpath = res.url[res.url.find("_Resources"):]
            dirname, fname = os.path.split(fullpath)

            if not dirname:
                print("Invalid URL:", res.url)
                continue

            if os.path.exists(fullpath):
                print(fname, "exists -> Skipping")
                continue
            else:
                print("Downloading", fname)

            os.makedirs(dirname, exist_ok=True)
            pdf = requests.get(res.url)
            with open(fullpath, "wb") as f:
                f.write(pdf.content)


def main():
    if len(sys.argv) < 2:
        print("No tag specified")
        return 1

    username, key = get_api_credentials()
    if not username or not key:
        return 1

    json_source = bibsonomy.REST(username, key)
    bib = bibsonomy.BibSonomy(json_source)

    posts = bib.getPostsForTag("bibtex", [ sys.argv[1] ])

    if len(sys.argv) > 2 and sys.argv[2] == "pdf":
        download_pdfs(sys.argv[1], posts)
    else:
        gen_page(sys.argv[1], posts)

    return 0


if __name__ == "__main__":
    sys.exit(main())
