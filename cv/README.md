# PDF CV generator

The PDF CV ([`assets/cv/Alexander_Boll_CV.pdf`](../assets/cv/Alexander_Boll_CV.pdf))
is **auto-generated** from the same data that drives the website. There is no
hand-maintained `.tex` file to keep in sync — edit the data, rerun, commit.

## Regenerate

```sh
make cv          # → assets/cv/Alexander_Boll_CV.pdf
```

(or `python3 cv/generate_cv.py`). Then commit the updated PDF. GitHub Pages serves
it directly; the "View CV" button on the homepage links to it.

## Where the content comes from

| Section on the CV                              | Source |
| ---------------------------------------------- | ------ |
| Name, role, affiliation, location, photo       | `_data/site.yml` |
| Contact links (email, web, LinkedIn, …)        | `_data/socials.yml`, `_config.yml` |
| Profile, experience, education, awards,         | `_data/cv.yml` |
| presentations, grants, skills, languages,       | (CV-only data) |
| memberships, nationality                        | |
| Publications                                    | `_data/publications.yml` |
| Supervision / Teaching / Service / Reviewing    | `_data/{supervision,teaching,service,reviewing}.yml` |

`_data/cv.yml` is the **only** file that exists solely for the CV. Everything else
is shared with the website's main page, so updating a publication or a supervision
entry updates both the site and the PDF.

## How it works

`generate_cv.py` loads the YAML, renders the Jinja2 LaTeX template `cv.tex.j2`
(custom `((* *))` / `((( )))` delimiters so they don't clash with LaTeX braces),
and compiles it with `latexmk -xelatex` into `cv/build/`, copying the result to
`assets/cv/`.

### Requirements

- Python 3 with **PyYAML** and **Jinja2**
- A TeX distribution with **XeLaTeX** and `latexmk` (TeX Live full is fine).
  Packages used: `fontspec`, `paracol`, `eso-pic`, `tikz`, `enumitem`,
  `microtype`, `graphicx`, `hyperref`.
- **Inkscape** on PATH — the sidebar icons are the website's own SVG logos
  (`_includes/icons/*.svg`), recolored cream and exported to vector PDFs at
  build time (no invented icon set; one source of truth with the site).
- The **Inter** font installed system-wide (matches the website typography).

`cv/build/` holds LaTeX intermediates and is git-ignored.

## Style

Modern two-column layout: a full-bleed navy sidebar (photo, contact, skills,
languages, memberships) beside a white main column (experience, education,
publications, …). Palette and font match the website (`#0B1220` navy ink on
`#F4F1E8` cream, Inter).
