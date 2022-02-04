# General Information

See readme in [itc-template](https://github.com/lsinfo3/itc-template) repo.

## Collections

See also: <https://jekyllrb.com/docs/collections/>

Collection properties are set in `_config.yml`. They should have a `title` and `url`, which enables automatic breadcrumb, title, and sidebar generation.

## Sidebar

Pages can have an additional sidebar listing all pages in a collection, e.g. as in "About ITC" or "ITC Library" pages.

To enable the sidebar, set the `sidebar` attribute to a respective collection.
To enable the sidebar on whole subdirectories, use the `defaults` section in `_config.yml`

## ITC Library

ITC Library pages are usually not manually written but auto-generated using `bibfetch.py`. See The corresponding entry under [scripts](#scripts).

ITC Library pages can have a `sprite` attribute to set the icon used on the overview page.
The default sprite is defined in `_config.yml` under `defaults`.

Sprites must be set manually, as `bibfetch.py` script does not do this automatically.

## Repositories

* This repo contains <https://itc-conference.org>
* ITC template repo for new ITC sites: <https://github.com/lsinfo3/itc-template>
* Paper repos are here:
  * Public papers, bib files, and bibsonomy prepare script: <https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-publications-public>
  * Private papers (only pdfs): <https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-publications-private>
* Repo used to redirect `i-teletraffic.org` to `itc-conference.org`: <https://github.com/lsinfo3/i-teletraffic-redirect>

    It is not possible to redirect domains to other domains using Host Europe, because apparently, it is not included in the in the "Domain Basic" package.
    Github also allows only one domain per repository.

    As a workaround, we connected `i-teletraffic` to this repo and added a single `index.html` that redirects to `itc-conference.org`.
* Archive of older ITCs: <https://github.com/lsinfo3/itc-clones>

    Is connected to `archive.itc-conference.org`. Pages can be accessed using `archive.itc-conference.org/itcXY`.


# Scripts

First, install dependencies
```sh
$ pip install -r scripts/requirements.txt
```

All scripts have a `-h/--help` flag documenting their usage.

### `bibfetch.py`

Usage: `bibfetch.py <tag>`

Fetches all entries with the given tag from bibsonomy and generates the library page from it.

Requires a bibsonomy API key. See also `bibfetch.py -h`.

### `convertpage.py`

Usage: `convertpage.py <html_files>...`

Converts ITC html pages to jekyll markdown pages.<br/>
Was used to port the website over to jekyll and is probably no longer needed.

# Adding a new conference

1. Create entry in `_congresses`
2. Create entry in `_redirect`
3. Upload papers to bibsonomy

    See readme in public paper repo on how to prepare bib files: <https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-publications-public>
4. Generate entry in `_itc-library` using `bibfetch.py`

See the individual sections for further information on each step.

## Adding a congresses entry

See other conference pages for more detailed examples.

1. Create a new file in `_congresses` with the name `itcXXX.md` (filename matters!).
2. Set the `confdate` and `conftitle` attribute to enable auto-generation of the overview page (`congresses.md`).
3. Add content


## Redirects

The `_redirect` subfolder contains pages that redirect to the respective ITC site, so that each site can be accessed using `https://itc-conference.org/itcXY`.

**Note:** To assign a custom domain, see [here](https://github.com/lsinfo3/itc-template#custom-domain).

To add a new redirect, create a new file in the `_redirect`folder and set the `target` attribute to the desired URL, e.g. for ITC 31:

itc31.html:
```
---
target: https://itc31.itc-conference.org
---
```
