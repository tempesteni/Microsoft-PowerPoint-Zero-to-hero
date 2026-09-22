import os
#!/usr/bin/env python3
"""Generate exercise-fix-this-deck.pptx: a DELIBERATELY BAD deck with 20 planted issues.
Companion answer key: ../exercises/fix-this-deck-challenge.md. Fictional content only."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.oxml.ns import qn
from lxml import etree
import copy

TERRA = RGBColor(0xB8, 0x50, 0x42)
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
TITLE_ONLY = prs.slide_layouts[5]

def txt(s, x, y, w, h, text, size, color, bold=False, font="Calibri"):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    r = tf.paragraphs[0].add_run()
    r.text = text
    r.font.size = Pt(size); r.font.bold = bold
    r.font.color.rgb = color; r.font.name = font
    return tb

def bullets(s, x, y, w, h, items, size=14, color=RGBColor(0x2B, 0x2B, 0x2B), font="Calibri"):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = it
        p.font.size = Pt(size); p.font.color.rgb = color; p.font.name = font
        p.space_after = Pt(4)
    return tb

# ================= Slide 1: Title (issues 1, 2-fonts-part, 5-start) =================
s1 = prs.slides.add_slide(BLANK)
# ISSUE 1: stretched logo (squashed wide rectangle)
logo = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(3.8), Inches(0.4), Inches(5.8), Inches(0.35))
logo.fill.solid(); logo.fill.fore_color.rgb = RGBColor(0x1F, 0x4E, 0x79); logo.line.fill.background()
logo.name = "YourCompany Inc logo"
ltf = logo.text_frame; ltf.paragraphs[0].alignment = 1
lr = ltf.paragraphs[0].add_run(); lr.text = "YourCompany Inc logo"
lr.font.size = Pt(8); lr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
# ISSUE 2 (part 1 of 3): title in Impact
txt(s1, 1.2, 2.6, 11.0, 1.2, "TASKFLOW PRO - SALES DECK 2026", 44, RGBColor(0x80, 0x00, 0x80), bold=True, font="Impact")
# jagged subtitle (issue 5 warmup, still on-topic)
txt(s1, 0.6, 4.1, 11.5, 0.6, "Prepared by the YourCompany Inc Sales Team", 18, RGBColor(0x44, 0x44, 0x44))

# ================= Slide 2: Agenda = WORD WALL (issues 4, 15) =================
s2 = prs.slides.add_slide(BLANK)  # ISSUE 15: no title placeholder
bullets(s2, 1.4, 0.7, 10.8, 6.2, [
    "Welcome everybody to the TaskFlow Pro sales presentation for YourCompany Inc which covers everything about our product.",
    "First we will talk about the history of the company and how we started building productivity software in 2019.",
    "Then we will explain the problem that teams face when they manage tasks across too many different tools and spreadsheets.",
    "After that we will show the product and all of the features that it has including boards, lists, cards, and automations.",
    "We will also cover the market opportunity and why the productivity software market is growing so fast right now.",
    "Our traction numbers will be presented including revenue growth and user growth over the last four quarters of this year.",
    "The business model slide explains how we make money through subscriptions and what our pricing tiers look like today.",
    "A competitive analysis will show how TaskFlow Pro compares against other tools that you may be using at your company.",
    "Then we will introduce the team and all of the people who are working here and their experience and backgrounds.",
    "Finally we will make the ask and tell you exactly how much investment we are looking for and what we will do with it.",
    "Thank you for listening to this presentation and please hold your questions until the very end of the presentation.",
], size=13)  # ISSUE 4: exactly 11 full-sentence bullet lines (word wall)

# ================= Slide 3: Product (issues 2-part2, 5, 6) =================
s3 = prs.slides.add_slide(TITLE_ONLY)
t3 = s3.shapes.title
t3.text = "Product Overview"
t3.text_frame.paragraphs[0].runs[0].font.size = Pt(32)
# ISSUE 5: three text boxes with jagged, unaligned left edges
bullets(s3, 0.7, 1.5, 4.6, 1.6, ["Boards for every project you manage with drag and drop"], size=15, font="Comic Sans MS")
bullets(s3, 1.05, 3.1, 4.6, 1.6, ["Lists for every stage of your process like To Do and Done"], size=15, font="Comic Sans MS")
bullets(s3, 0.5, 4.7, 4.6, 1.6, ["Cards for every task with owners, dates, and checklists too"], size=15, font="Comic Sans MS")
# ISSUE 6: ugly clip-art-style robot built from shapes
rb = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.0), Inches(2.6), Inches(2.4), Inches(2.4))
rb.fill.solid(); rb.fill.fore_color.rgb = RGBColor(0xC0, 0xC0, 0xC0); rb.line.color.rgb = RGBColor(0x00, 0x00, 0x00)
head = s3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.5), Inches(1.4), Inches(1.4), Inches(1.1))
head.fill.solid(); head.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0x00); head.line.color.rgb = RGBColor(0x00, 0x00, 0x00)
eye1 = s3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.75), Inches(1.7), Inches(0.25), Inches(0.25))
eye1.fill.solid(); eye1.fill.fore_color.rgb = RGBColor(0xFF, 0x00, 0x00); eye1.line.fill.background()
eye2 = s3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.4), Inches(1.7), Inches(0.25), Inches(0.25))
eye2.fill.solid(); eye2.fill.fore_color.rgb = RGBColor(0xFF, 0x00, 0x00); eye2.line.fill.background()
arm1 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.9), Inches(2.9), Inches(1.1), Inches(0.3))
arm1.fill.solid(); arm1.fill.fore_color.rgb = RGBColor(0x80, 0x80, 0x80); arm1.line.fill.background()
arm2 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(10.4), Inches(2.9), Inches(1.1), Inches(0.3))
arm2.fill.solid(); arm2.fill.fore_color.rgb = RGBColor(0x80, 0x80, 0x80); arm2.line.fill.background()
txt(s3, 8.2, 5.15, 2.2, 0.5, "CLIP ART", 14, RGBColor(0x00, 0x00, 0x00), bold=True)

# ================= Slide 4: Revenue pie (issues 8, 9, 14) =================
s4 = prs.slides.add_slide(TITLE_ONLY)
# ISSUE 14 (reading order chaos): decorative shapes added BEFORE the headline in shape-tree order
for i, col in enumerate([RGBColor(0xFF, 0xD7, 0x00), RGBColor(0x00, 0x80, 0x80)]):
    dec = s4.shapes.add_shape(MSO_SHAPE.STAR_5_POINT, Inches(0.3 + i * 12.3), Inches(0.3), Inches(0.6), Inches(0.6))
    dec.fill.solid(); dec.fill.fore_color.rgb = col; dec.line.fill.background()
t4 = s4.shapes.title  # title added AFTER the decorative stars (bad reading order)
t4.text = "Revenue"    # ISSUE 8: topic title, not a claim
t4.text_frame.paragraphs[0].runs[0].font.size = Pt(32)
cd = CategoryChartData()
cd.categories = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26"]
cd.add_series("Revenue", (42.0, 51.0, 47.0, 63.0, 58.0, 66.0, 71.0, 84.0))
# ISSUE 9: PIE chart for 8 quarters of trend data (wrong chart type)
gf4 = s4.shapes.add_chart(XL_CHART_TYPE.PIE, Inches(2.2), Inches(1.5), Inches(8.8), Inches(5.4), cd)
ch4 = gf4.chart
ch4.has_legend = True
# charts carry meaningful content but get EMPTY alt text (issue 13: #1 and #2)

# ================= Slide 5: Revenue column (issues 10, 11, 13, 15, 18) =================
s5 = prs.slides.add_slide(BLANK)  # ISSUE 15: no title placeholder
txt(s5, 1.3, 0.4, 10.0, 0.8, "Quarterly Revenue Detail", 28, RGBColor(0x33, 0x33, 0x33), bold=True)
cd5 = CategoryChartData()
cd5.categories = ["Q1", "Q2", "Q3", "Q4"]
cd5.add_series("Revenue in thousands USD", (31.0, 44.0, 47.0, 63.0))
gf5 = s5.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.8), Inches(1.4), Inches(7.6), Inches(5.4), cd5)
ch5 = gf5.chart
ch5.value_axis.minimum_scale = 30000 * 0.001  # ISSUE 10: truncated axis (min 30 on 31-63 values)
ch5.value_axis.maximum_scale = 70.0
ch5.value_axis.has_major_gridlines = True     # ISSUE 11: chart junk: gridlines
ch5.has_legend = True                          # + legend
ch5.value_axis.has_title = True                # + axis titles
ch5.category_axis.has_title = True
ch5.value_axis.axis_title.text_frame.text = "Revenue (thousands)"
ch5.category_axis.axis_title.text_frame.text = "Fiscal Quarter"
plot = ch5.plots[0]
plot.has_data_labels = True                    # + data labels
# ISSUE 18: 4:3-residue content block (10x7.5 proportion pasted at odd position)
res = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.8), Inches(1.6), Inches(3.6), Inches(2.7))
res.fill.solid(); res.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
res.line.color.rgb = RGBColor(0x00, 0x00, 0x00)
txt(s5, 8.95, 1.8, 3.3, 2.3, "(chart pasted from old 4:3 deck, does not line up)", 12, RGBColor(0x66, 0x66, 0x66))

# ================= Slide 6: Market share (issues 3, 7, 12, 13, 15) =================
s6 = prs.slides.add_slide(BLANK)  # ISSUE 15: no title placeholder
s6.background.fill.solid()
s6.background.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xCC)  # ISSUE 7: light yellow background
txt(s6, 1.6, 0.5, 10.0, 0.8, "Market Share Position", 28, RGBColor(0xD9, 0xD9, 0xD9), bold=True)  # ISSUE 7: light gray text
txt(s6, 1.6, 1.5, 10.0, 0.8, "Our market share is 12.3847%", 24, RGBColor(0xD9, 0xD9, 0xD9))   # ISSUE 12: fake precision
# ISSUE 3: rainbow palette (5 accent colors on one slide)
cols = [(0x00, 0x80, 0x00), (0x80, 0x00, 0x80), (0xFF, 0x80, 0x00), (0xFF, 0x00, 0x00), (0x00, 0x80, 0x80)]
labels = ["SMB", "Mid-Market", "Enterprise", "Education", "Gov"]
for i, (c, lab) in enumerate(zip(cols, labels)):
    seg = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0 + i * 2.3), Inches(4.6 - i * 0.45), Inches(2.0), Inches(1.0 + i * 0.45))
    seg.fill.solid(); seg.fill.fore_color.rgb = RGBColor(*c); seg.line.fill.background()
    stf = seg.text_frame; sr = stf.paragraphs[0].add_run(); sr.text = lab
    sr.font.size = Pt(13); sr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)  # meaningful graphic, empty alt (issue 13: #3)

# ================= Slide 7: Demo (issues 16, 17, 20-target) =================
s7 = prs.slides.add_slide(BLANK)  # ISSUE 15: no title placeholder
txt(s7, 1.1, 0.3, 10.0, 0.8, "Click to add title", 28, RGBColor(0x80, 0x80, 0x80))  # ISSUE 17: literal placeholder junk
vid = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(2.4), Inches(1.4), Inches(8.4), Inches(4.3))
vid.fill.solid(); vid.fill.fore_color.rgb = RGBColor(0x00, 0x00, 0x00); vid.line.fill.background()
vid.name = "DemoVideo"  # ISSUE 16: media with no captions/transcript
vtf = vid.text_frame; vr = vtf.paragraphs[0].add_run(); vr.text = "DEMO VIDEO (no captions)"
vr.font.size = Pt(20); vr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
demo_bullets = bullets(s7, 1.1, 5.9, 11.0, 1.2, [
    "Watch the product demo video above to see all of the features of TaskFlow Pro in real action right now.",
    "Contact our sales team at sales@acme.example to schedule a longer custom demo for your organization today.",
], size=13)

# ================= Slide 8: Close (issue 19) =================
s8 = prs.slides.add_slide(BLANK)  # ISSUE 15: no title placeholder
s8.background.fill.solid()
s8.background.fill.fore_color.rgb = RGBColor(0x1F, 0x4E, 0x79)
txt(s8, 1.4, 2.3, 10.5, 1.0, "THANK YOU FOR YOUR TIME!!!", 40, RGBColor(0xFF, 0xFF, 0x00), bold=True, font="Impact")
link_tb = txt(s8, 1.4, 3.8, 10.5, 0.8, "Learn more at our website: Learn more", 18, RGBColor(0xFF, 0xFF, 0xFF))
run = link_tb.text_frame.paragraphs[0].runs[0]
run.hyperlink.address = "https://example.com/moved-page-gone"  # ISSUE 19: dead hyperlink

# ================= ISSUE 20: tacky Bounce entrance on EVERY text shape on EVERY slide ================
NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
PNS = "http://schemas.openxmlformats.org/presentationml/2006/main"

def add_bounce_animations(slide):
    """Attach a Bounce (presetID 26) entrance on click for every text-bearing shape."""
    spTree = slide.shapes._spTree
    ids = []
    for sp in spTree.findall(qn('p:sp')) + spTree.findall(qn('p:graphicFrame')):
        cNvPr = sp.find('.//' + qn('p:cNvPr'))
        if cNvPr is None:
            continue
        if sp.find('.//' + qn('a:t')) is not None:
            ids.append(cNvPr.get('id'))
    if not ids:
        return
    parts = []
    cid = [10]
    def nid():
        cid[0] += 1
        return str(cid[0])
    groups = []
    for spid in ids:
        groups.append(f'''<p:par><p:cTn id="{nid()}" fill="hold">
  <p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>
  <p:childTnLst><p:par><p:cTn id="{nid()}" fill="hold">
    <p:stCondLst><p:cond delay="0"/></p:stCondLst>
    <p:childTnLst><p:par><p:cTn id="{nid()}" presetID="26" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="clickEffect">
      <p:stCondLst><p:cond delay="0"/></p:stCondLst>
      <p:childTnLst>
        <p:set><p:cBhvr><p:cTn id="{nid()}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>
          <p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>
          <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>
          <p:to><p:strVal val="visible"/></p:to></p:set>
        <p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{nid()}" dur="600"/>
          <p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>
      </p:childTnLst></p:cTn></p:par></p:childTnLst>
  </p:cTn></p:par></p:childTnLst>
</p:cTn></p:par>''')
    xml = f'''<p:timing xmlns:p="{PNS}" xmlns:a="{NS}">
<p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>
<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>
{''.join(groups)}
</p:childTnLst></p:cTn>
<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>
<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>
</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>'''
    timing = etree.fromstring(xml)
    clrMapOvr = spTree.getparent().find(qn('p:clrMapOvr'))
    csld = spTree.getparent()
    # insert timing before extLst / at end of cSld-level (after clrMapOvr)
    ext = csld.find(qn('p:extLst'))
    if ext is not None:
        ext.addprevious(timing)
    else:
        csld.append(timing)

for slide in prs.slides:
    add_bounce_animations(slide)

prs.save("os.path.join(os.path.dirname(os.path.abspath(__file__)), "exercise-fix-this-deck.pptx")")
print("saved: 8 slides with planted issues + bounce animations")
