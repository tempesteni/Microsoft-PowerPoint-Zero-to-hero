import os
#!/usr/bin/env python3
"""Generate sample-06-brand-template.potx (+ .pptx preview copy) for YourCompany Inc.
Template layouts: Title, Section Header, Two Content, Closing (+ usage example)."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
import zipfile, shutil, os, re

NAVY = RGBColor(0x1E, 0x27, 0x61)
SAND = RGBColor(0xE7, 0xE8, 0xD1)
GOLD = RGBColor(0xC9, 0xA2, 0x27)
INK = RGBColor(0x2B, 0x2B, 0x2B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

def txt(s, x, y, w, h, text, size, color, bold=False, font="Calibri", align=PP_ALIGN.LEFT):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.bold = bold
    r.font.color.rgb = color; r.font.name = font
    return tb

def brand_frame(s, footer=True):
    """Repeated motif: gold tick top-left + footer bar with placeholder logo + page field."""
    tick = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(0.5), Inches(0.55), Inches(0.12))
    tick.fill.solid(); tick.fill.fore_color.rgb = GOLD; tick.line.fill.background()
    if footer:
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(6.95), Inches(13.333), Inches(0.55))
        bar.fill.solid(); bar.fill.fore_color.rgb = NAVY; bar.line.fill.background()
        logo = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(7.05), Inches(1.5), Inches(0.34))
        logo.fill.background(); logo.line.color.rgb = SAND
        logo.name = "LOGO PLACEHOLDER (replace)"
        lr = logo.text_frame.paragraphs[0].add_run(); lr.text = "YOUR LOGO"
        lr.font.size = Pt(9); lr.font.color.rgb = SAND; lr.font.name = "Calibri"
        txt(s, 10.3, 7.05, 2.5, 0.34, "YourCompany Inc | Confidential", 10, SAND, align=PP_ALIGN.RIGHT)

# ---------------- Slide 1: TITLE layout ----------------
s = prs.slides.add_slide(BLANK)
s.background.fill.solid(); s.background.fill.fore_color.rgb = NAVY
brand_frame(s, footer=False)
txt(s, 0.9, 2.4, 11.5, 1.3, "Presentation Title Goes Here", 44, WHITE, bold=True, font="Georgia")
txt(s, 0.9, 3.8, 11.5, 0.7, "Subtitle: audience, date, occasion", 20, SAND)
txt(s, 0.9, 4.7, 11.5, 0.5, "Presenter Name | Role | presenter@acme.example", 14, SAND)
gold = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(5.5), Inches(1.6), Inches(0.08))
gold.fill.solid(); gold.fill.fore_color.rgb = GOLD; gold.line.fill.background()

# ---------------- Slide 2: SECTION HEADER layout ----------------
s = prs.slides.add_slide(BLANK)
s.background.fill.solid(); s.background.fill.fore_color.rgb = NAVY
brand_frame(s, footer=False)
txt(s, 0.9, 2.5, 2.0, 1.2, "01", 60, GOLD, bold=True, font="Georgia")
txt(s, 2.9, 2.8, 9.5, 1.0, "Section Title Goes Here", 40, WHITE, bold=True, font="Georgia")
txt(s, 2.9, 3.9, 9.5, 0.6, "One-line section promise (optional)", 16, SAND)

# ---------------- Slide 3: CONTENT layout ----------------
s = prs.slides.add_slide(BLANK)
s.background.fill.solid(); s.background.fill.fore_color.rgb = SAND
brand_frame(s)
txt(s, 0.9, 0.8, 11.5, 0.9, "Assertion Title Goes Here", 36, NAVY, bold=True, font="Georgia")
tb = s.shapes.add_textbox(Inches(0.9), Inches(2.0), Inches(7.2), Inches(4.4))
tf = tb.text_frame; tf.word_wrap = True
for i, item in enumerate(["First supporting point (max 6 words)", "Second supporting point", "Third supporting point"]):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.text = item
    p.font.size = Pt(18); p.font.color.rgb = INK; p.font.name = "Calibri"
    p.space_after = Pt(12)
vis = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(2.0), Inches(3.9), Inches(4.2))
vis.fill.solid(); vis.fill.fore_color.rgb = WHITE; vis.line.color.rgb = NAVY
vt = vis.text_frame; vr = vt.paragraphs[0].add_run(); vr.text = "VISUAL AREA\n(chart, image, or diagram)"
vt.paragraphs[0].alignment = PP_ALIGN.CENTER
vr.font.size = Pt(14); vr.font.color.rgb = NAVY; vr.font.name = "Calibri"

# ---------------- Slide 4: TWO CONTENT layout ----------------
s = prs.slides.add_slide(BLANK)
s.background.fill.solid(); s.background.fill.fore_color.rgb = SAND
brand_frame(s)
txt(s, 0.9, 0.8, 11.5, 0.9, "Comparison or Two-Idea Title", 36, NAVY, bold=True, font="Georgia")
for i, head in enumerate(["Left Column Head", "Right Column Head"]):
    x = 0.9 + i * 6.1
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(2.0), Inches(5.6), Inches(4.2))
    card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = NAVY
    txt(s, x + 0.35, 2.3, 4.9, 0.6, head, 20, NAVY, bold=True)
    txt(s, x + 0.35, 3.1, 4.9, 2.8, "Supporting detail goes here. Keep it to 3 short lines per card.", 15, INK)

# ---------------- Slide 5: CLOSING layout ----------------
s = prs.slides.add_slide(BLANK)
s.background.fill.solid(); s.background.fill.fore_color.rgb = NAVY
brand_frame(s, footer=False)
txt(s, 0.9, 2.5, 11.5, 1.1, "Closing Takeaway or Call to Action", 40, WHITE, bold=True, font="Georgia", align=PP_ALIGN.CENTER)
txt(s, 0.9, 3.9, 11.5, 0.6, "Contact: presenter@acme.example | YourCompany Inc", 16, SAND, align=PP_ALIGN.CENTER)

# ---------------- Slide 6: USAGE EXAMPLE (built from the layouts above) ----------------
s = prs.slides.add_slide(BLANK)
s.background.fill.solid(); s.background.fill.fore_color.rgb = SAND
brand_frame(s)
txt(s, 0.9, 0.8, 11.5, 0.9, "How to use this template", 36, NAVY, bold=True, font="Georgia")
tb = s.shapes.add_textbox(Inches(0.9), Inches(2.0), Inches(11.5), Inches(4.4))
tf = tb.text_frame; tf.word_wrap = True
steps = [
    "1. Save your copy as .potx (this file) into your PowerPoint Templates folder so it appears in File > New > Personal",
    "2. Replace the YOUR LOGO placeholder and the footer text with your brand",
    "3. Duplicate the layout slides you need: Title, Section Header, Content, Two Content, Closing",
    "4. Keep the gold tick and footer bar on every slide: that is the brand glue",
    "5. Test: apply a theme color change and confirm every slide updates",
]
for i, st in enumerate(steps):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.text = st
    p.font.size = Pt(16); p.font.color.rgb = INK; p.font.name = "Calibri"
    p.space_after = Pt(10)

base = "os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample-06-brand-template")"
prs.save(base + ".pptx")  # preview copy

# ---- convert to .potx: rewrite presentation content type ----
shutil.copy(base + ".pptx", base + ".potx")
tmp = base + ".tmp.potx"
with zipfile.ZipFile(base + ".potx", "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.namelist():
        data = zin.read(item)
        if item == "[Content_Types].xml":
            data = data.replace(
                b"application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
                b"application/vnd.openxmlformats-officedocument.presentationml.template.main+xml")
        zout.writestr(item, data)
os.replace(tmp, base + ".potx")
print("saved:", base + ".pptx (preview) and sample-06-brand-template.potx (template)")
