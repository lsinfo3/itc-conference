#!/usr/bin/env python
# -*- coding: utf-8 -*-

# See also https://bitbucket.org/bibsonomy/bibsonomy-python
# Get your API key at https://www.bibsonomy.org/settings?selTab=1
# Put username and API key in a file called APIKEY (first line username, second line key)

from typing import List, Set
import argparse
import bibsonomy
import sys
import os
from bibtexparser.customization import convert_to_unicode


def get_api_credentials():
    username = ""
    key = ""

    try:
        dirname = os.path.dirname(__file__)
    except NameError:  # Running in interactive shell
        dirname = ""

    try:
        with open(os.path.join(dirname, "APIKEY")) as f:
            username = f.readline().strip()
            key = f.readline().strip()
    finally:
        if not key or not username:
            print("Invalid APIKEY file or not found in {}.".format(dirname))
            print("Please put your username and API key, newline separated, in a file called 'APIKEY' in the script directory.")

    return (username, key)


def generate_bibsonomy_link(entry: dict):
    return "https://www.bibsonomy.org/bibtex/{}/itc".format(entry["intra_hash"])


def generate_bibtex(entry: dict):
    filterset = { "intra_hash", "entry_type", "inter_hash", "bibtex_key", "abstract", "url" }
    attribs = ",\n".join(
        [ "    {:13} = {{ {} }}".format(k, v) for k, v in entry.items() if k not in filterset ])
    return "@{entry_type}{{{bibtex_key},\n{attribs}\n}}".format(
        **entry, attribs=attribs)


def generate_entry(entry: dict):
    content = []
    content.append("{}<br/>\n**{}**<br/>\n".format(
        entry.get("author", entry.get("editor", "")), entry["title"].strip()))

    if "booktitle" in entry:
        content.append("In *{}*. ".format(entry["booktitle"].strip()))

    content.append("{} {}<br/>\n".format(entry.get("address", ""), entry["year"]))
    content.append('[\\[BibTeX\\]](javascript:toggleVis(\'{bibtex_key}\'))\n'.format(**entry))

    if "abstract" in entry:
        content.append('[\\[Abstract\\]](javascript:toggleVis(\'abstract_{bibtex_key}\'))\n'.format(**entry))

    if "url" in entry:
        content.append("[\\[Download\\]]({url})\n".format(**entry))

    content.append("[\\[BibSonomy\\]]({})\n\n".format(generate_bibsonomy_link(entry)))
    content.append('<div id="{bibtex_key}" style="display: none;" class="bibtex">{bibtex}</div>'.format(
        **entry, bibtex=generate_bibtex(entry)))

    if "abstract" in entry:
        content.append("""\n<div id="abstract_{bibtex_key}" style="display: none;" class="abstract">
    <strong>Abstract:</strong> {abstract}\n</div>""".format(**entry))

    content.append("\n")
    return "".join(content)


def gen_page(tag: str, entries: List[dict]):
    content = []  # Stores tuples (title, content) for each entry
    year = None

    for entry in entries:
        if not year:
            year = entry.get("year", None)

        content.append((entry["title"], generate_entry(entry)))

    # Sort by title
    content.sort(key=lambda x: x[0])

    # Front matter
    lines = [
        "---",
        "title: {}".format(tag.upper()),
        "year: {}".format(year if year else "TODO" if entries else "Not available"),
        "---\n",
    ]

    # Add content
    lines += [ i[1] for i in content ]

    if not entries:
        lines.append("No entries available.")

    with open("{}.md".format(tag), "w") as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""Fetches all entries with a given tag from bibsonomy and generates the library page from it.

Requires a bibsonomy API key. You can get it here: https://www.bibsonomy.org/settings?selTab=1 .
Put your username and API key in a file called APIKEY in the same directory as the script.
The first line should contain the username, the second the key.""")
    parser.add_argument("tag", type=str, help="A tag to search for")
    args = parser.parse_args()

    if not args.tag:
        print("No tag specified")
        return 1

    username, key = get_api_credentials()
    if not username or not key:
        return 1

    json_source = bibsonomy.REST(username, key)
    bib = bibsonomy.BibSonomy(json_source)

    posts = bib.getPostsForTag("bibtex", [ args.tag ])
    entries = [ convert_to_unicode(i.resource.__dict__) for i in posts ]
    gen_page(args.tag, entries)

    return 0


if __name__ == "__main__":
    sys.exit(main())
