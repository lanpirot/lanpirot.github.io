#!/usr/bin/env python3
"""Generate Alexander Boll's PDF CV from the website's own data.

Reads the same _data/*.yml files that drive the website (plus _data/cv.yml for
CV-only sections), renders a LaTeX source from cv/cv.tex.j2, and compiles it with
XeLaTeX into assets/cv/Alexander_Boll_CV.pdf.

Usage:
    python3 cv/generate_cv.py          # build the PDF
    python3 cv/generate_cv.py --tex    # only render the .tex (no compile)

Single source of truth: edit the _data/*.yml files, then rerun (`make cv`).
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip install pyyaml")

try:
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError:
    sys.exit("Jinja2 is required:  pip install jinja2")

CV_DIR = Path(__file__).resolve().parent
ROOT = CV_DIR.parent
DATA = ROOT / "_data"
ICONS_SRC = ROOT / "_includes" / "icons"
BUILD = CV_DIR / "build"
ICONS_OUT = BUILD / "icons"
OUT_PDF = ROOT / "assets" / "cv" / "Alexander_Boll_CV.pdf"

# Sidebar icons are the website's own SVG logos, recolored cream for the navy panel.
ICON_COLOR = "F4F1E8"

# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

_TEX_SPECIALS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
_TEX_RE = re.compile("|".join(re.escape(k) for k in _TEX_SPECIALS))


def tex(value) -> str:
    """Escape arbitrary text for LaTeX (XeLaTeX handles UTF-8 directly)."""
    if value is None:
        return ""
    return _TEX_RE.sub(lambda m: _TEX_SPECIALS[m.group()], str(value)).strip()


def rich(value) -> str:
    r"""Escape, then turn lightweight *markdown* into LaTeX.

    Supports *italic* (single asterisks). '*' is not a TeX special, so it
    survives escaping and we convert balanced pairs afterwards.
    """
    out = tex(value)
    out = re.sub(r"\*(.+?)\*", r"\\textit{\1}", out)
    return out


def authors(value, me: str = "Alexander Boll") -> str:
    """Escape an author string and embolden my own name."""
    out = tex(value)
    return out.replace(tex(me), r"\textbf{%s}" % tex(me))


def url_escape(value) -> str:
    """Escape a URL for use inside \\href{...} (only # and % bite there)."""
    return str(value).replace("\\", r"\\").replace("%", r"\%").replace("#", r"\#")


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_config() -> dict:
    """Minimal front-matter-free read of _config.yml."""
    return load_yaml(ROOT / "_config.yml")


def convert_icons(names) -> dict:
    """Recolor the website's SVG logos to cream and export each to a vector PDF.

    Returns {icon_name: absolute_pdf_path}. Requires Inkscape on PATH.
    """
    if not shutil.which("inkscape"):
        sys.exit("Inkscape is required to embed the website's SVG logos. Install it, "
                 "or remove the icon usage from cv/cv.tex.j2.")
    ICONS_OUT.mkdir(parents=True, exist_ok=True)
    out = {}
    for name in names:
        svg = (ICONS_SRC / ("%s.svg" % name)).read_text(encoding="utf-8")
        svg = svg.replace("currentColor", "#%s" % ICON_COLOR)
        if name == "dblp":
            # The dblp logo is a filled square keyed off theme CSS variables.
            # Invert it for the dark sidebar: cream square with navy marks.
            svg = (svg.replace("var(--fg)", "#%s" % ICON_COLOR)
                      .replace("var(--muted)", "#0B1220")
                      .replace("var(--bg)", "#0B1220"))
        tmp_svg = ICONS_OUT / ("%s.svg" % name)
        tmp_svg.write_text(svg, encoding="utf-8")
        pdf = ICONS_OUT / ("%s.pdf" % name)
        subprocess.run(
            # Export the full (square) viewBox, like the website renders it, so every
            # icon is a uniform square that aligns consistently in the sidebar.
            ["inkscape", str(tmp_svg), "--export-type=pdf",
             "--export-filename=%s" % pdf, "--export-area-page"],
            check=True, capture_output=True, text=True,
        )
        out[name] = pdf.as_posix()
    return out


def build_contacts(socials: list, config: dict, icons: dict) -> list[dict]:
    """Sidebar contact rows — brand logos that exist on the website, in site order."""
    email = config.get("author", {}).get("email", "")
    by_icon = {s.get("icon"): s for s in socials}

    rows = [{"icon": "email", "text": email, "url": "mailto:%s" % email}]

    def social(icon, label):
        s = by_icon.get(icon)
        if s:
            rows.append({"icon": icon, "text": label, "url": s["url"]})

    social("linkedin", "LinkedIn")
    social("github", "GitHub")
    social("orcid", "ORCID")
    social("scholar", "Google Scholar")
    social("dblp", "DBLP")

    for r in rows:
        r["icon_pdf"] = icons[r["icon"]]
    return rows


def group_publications(pubs: list) -> dict:
    """Group publications for the CV, mirroring the website's ordering."""
    def fmt(p):
        return {
            "authors": authors(p.get("authors", "")),
            "title": tex(p.get("title", "")),
            "venue": tex(p.get("venue", "")),
            "year": p.get("year", ""),
            "doi": p.get("doi"),
            "doi_url": url_escape("https://doi.org/%s" % p["doi"]) if p.get("doi") else None,
            "award": tex(p["award"]) if p.get("award") else None,
        }

    journals = [fmt(p) for p in pubs if p.get("type") == "journal"]
    conferences = [fmt(p) for p in pubs if p.get("type") == "conference"]
    preprints = [fmt(p) for p in pubs if p.get("status") == "preprint"]
    theses = [fmt(p) for p in pubs if p.get("type") == "thesis"]
    return {
        "journals": journals,
        "conferences": conferences,
        "preprints": preprints,
        "theses": theses,
    }


def reviewing_summary(reviewing: list):
    """Flatten the year×venue reviewing table into a single deduped venue list."""
    seen = []
    years = []
    for year in reviewing:
        years.append(year["year"])
        for v in year["venues"]:
            name = v["name"].split(" (")[0].strip()  # merge tracks, e.g. "ICSE (NIER)"
            if name not in seen:
                seen.append(name)
    span = "%s–%s" % (min(years), max(years)) if years else ""
    return seen, span


def build_context() -> dict:
    site = load_yaml(DATA / "site.yml")
    socials = load_yaml(DATA / "socials.yml")
    cv = load_yaml(DATA / "cv.yml")
    config = load_config()

    photo = (ROOT / site["photo"].lstrip("/")).resolve()
    icons = convert_icons(["email", "linkedin", "github", "orcid", "scholar", "dblp"])
    website_url = config.get("url", "")

    return {
        "name": tex(site["name"]),
        "role": tex(site["role"]),
        "affiliation": tex(site["affiliation"]),
        "location": tex(site["location"]),
        "website": tex(website_url.replace("https://", "").replace("http://", "")),
        "website_url": website_url,
        "photo": photo.as_posix(),
        "contacts": build_contacts(socials, config, icons),
        "summary": tex(cv["summary"]),
        "experience": cv["experience"],
        "education": cv["education"],
        "awards": cv.get("awards", []),
        "presentations": cv.get("presentations", []),
        "grants": cv.get("grants", []),
        "skills": cv["skills"],
        "languages": cv["languages"],
        "memberships": cv.get("memberships", []),
        "publications": group_publications(load_yaml(DATA / "publications.yml")),
        "teaching": load_yaml(DATA / "teaching.yml"),
        "supervision": load_yaml(DATA / "supervision.yml"),
        "service": load_yaml(DATA / "service.yml"),
        "reviewing_venues": reviewing_summary(load_yaml(DATA / "reviewing.yml"))[0],
        "reviewing_span": reviewing_summary(load_yaml(DATA / "reviewing.yml"))[1],
        # expose helpers for in-template use
        "tex": tex,
        "rich": rich,
    }


# ---------------------------------------------------------------------------
# Rendering & compilation
# ---------------------------------------------------------------------------

def render_tex() -> str:
    env = Environment(
        loader=FileSystemLoader(str(CV_DIR)),
        block_start_string="((*",
        block_end_string="*))",
        variable_start_string="(((",
        variable_end_string=")))",
        comment_start_string="((#",
        comment_end_string="#))",
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=False,
        undefined=StrictUndefined,
    )
    env.filters["tex"] = tex
    env.filters["rich"] = rich
    env.filters["join_list"] = lambda xs, sep=", ": sep.join(tex(x) for x in xs)
    template = env.get_template("cv.tex.j2")
    return template.render(**build_context())


def compile_pdf(tex_source: str) -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    tex_path = BUILD / "cv.tex"
    tex_path.write_text(tex_source, encoding="utf-8")

    cmd = [
        "latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", "-output-directory=%s" % BUILD, str(tex_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout[-4000:])
        sys.stderr.write(proc.stderr[-2000:])
        sys.exit("\nLaTeX compilation failed (see log above and %s)." % (BUILD / "cv.log"))

    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BUILD / "cv.pdf", OUT_PDF)
    print("Wrote %s" % OUT_PDF.relative_to(ROOT))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tex", action="store_true", help="only render the .tex, do not compile")
    args = ap.parse_args()

    source = render_tex()
    if args.tex:
        BUILD.mkdir(parents=True, exist_ok=True)
        (BUILD / "cv.tex").write_text(source, encoding="utf-8")
        print("Wrote %s" % (BUILD / "cv.tex").relative_to(ROOT))
        return
    compile_pdf(source)


if __name__ == "__main__":
    main()
