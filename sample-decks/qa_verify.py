import os
#!/usr/bin/env python3
"""Claims-vs-reality audit of the sample decks: verify each deck contains what
the README table, walkthroughs, and module mapping promise."""
from pptx import Presentation
from pptx.util import Emu
import zipfile, re, glob, os

D = os.path.dirname(os.path.abspath(__file__))

def audit(name):
    path = os.path.join(D, name)
    p = Presentation(path)
    slides = list(p.slides)
    out = {"file": name, "slides": len(slides)}
    charts = tables = notes = 0
    fonts = set()
    links = []
    title_placeholders = 0
    for s in slides:
        if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip():
            notes += 1
        # title placeholder present?
        for ph in s.placeholders:
            if ph.placeholder_format.idx == 0:
                title_placeholders += 1
                break
        for sh in s.shapes:
            if getattr(sh, "has_chart", False):
                charts += 1
            if getattr(sh, "has_table", False):
                tables += 1
            if sh.has_text_frame:
                for para in sh.text_frame.paragraphs:
                    for r in para.runs:
                        if r.font.name:
                            fonts.add(r.font.name)
                        if r.hyperlink and r.hyperlink.address:
                            links.append(r.hyperlink.address)
    out.update(charts=charts, tables=tables, notes=notes,
               fonts=sorted(fonts), links=links, titled_slides=title_placeholders)
    # XML-level: morph, timing, click triggers, slide-number fields, shape-name pairs
    z = zipfile.ZipFile(path)
    morph = timing = clicktrig = slidenums = 0
    names_per_slide = []
    for n in sorted(z.namelist()):
        if not re.match(r"ppt/slides/slide\d+\.xml$", n):
            continue
        x = z.read(n).decode("utf8", "ignore")
        morph += ("morph" in x)
        timing += ("<p:timing>" in x)
        clicktrig += ('evt="onClick"' in x or 'delay="indefinite"' in x and "<p:cond " in x and "spTgt" in x)
        slidenums += ('type="slidenum"' in x)
        names_per_slide.append(set(re.findall(r'<p:cNvPr id="\d+" name="([^"]+)"', x)))
    out.update(morph_slides=morph, timing_slides=timing,
               trigger_slides=clicktrig, slidenumber_fields=slidenums)
    shared = 0
    for a, b in zip(names_per_slide, names_per_slide[1:]):
        shared += len((a & b) - {""})
    out["shared_shape_names_adjacent"] = shared
    return out

for f in ["sample-01-starter-deck.pptx", "sample-02-business-pitch-deck.pptx",
          "sample-03-data-report-deck.pptx", "sample-04-animated-product-demo.pptx",
          "sample-05-training-deck-notes.pptx", "sample-06-brand-template.pptx",
          "exercise-fix-this-deck.pptx"]:
    a = audit(f)
    print("=" * 60)
    for k, v in a.items():
        print(f"{k}: {v}")
