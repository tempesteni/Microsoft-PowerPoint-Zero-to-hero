import os
#!/usr/bin/env python3
"""Generate sample-05-training-deck-notes.pptx: training deck with speaker notes on every slide.
Part of the PowerPoint Zero to Hero package. All content is fictional (YourCompany Inc)."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

TERRA = RGBColor(0xB8, 0x50, 0x42)   # dominant
SAND  = RGBColor(0xE7, 0xE8, 0xD1)   # content background
SAGE  = RGBColor(0xA7, 0xBE, 0xAE)   # accent
INK   = RGBColor(0x2B, 0x2B, 0x2B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
CREAM = RGBColor(0xFA, 0xFA, F5) if False else RGBColor(0xFA, 0xFA, 0xF5)

HDR = "Georgia"
BODY = "Calibri"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

def add_slide(bg):
    s = prs.slides.add_slide(BLANK)
    fill = s.background.fill
    fill.solid()
    fill.fore_color.rgb = bg
    return s

def txt(s, x, y, w, h, text, size, color, bold=False, font=BODY, align=PP_ALIGN.LEFT):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.name = font
    return tb

def bullets(s, x, y, w, h, items, size=16, color=INK):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = it
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.name = BODY
        p.space_after = Pt(8)
    return tb

def num_circle(s, x, y, n, d=0.55):
    """Repeated motif: terracotta circle with a step number."""
    sh = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    sh.fill.solid()
    sh.fill.fore_color.rgb = TERRA
    sh.line.fill.background()
    tf = sh.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(n)
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = WHITE
    r.font.name = BODY
    return sh

def notes(s, text):
    s.notes_slide.notes_text_frame.text = text

# ---------------- Slide 1: Title (dark) ----------------
s = add_slide(TERRA)
txt(s, 0.9, 2.3, 11.5, 1.4, "Getting Started with TaskFlow Pro", 44, WHITE, bold=True, font=HDR)
txt(s, 0.9, 3.7, 11.5, 0.7, "New User Training  |  YourCompany Inc", 20, SAND)
txt(s, 0.9, 4.5, 11.5, 0.6, "Facilitator: YourCompany Inc Training Team", 14, SAND)
notes(s, "Welcome everyone. This session gets you productive in TaskFlow Pro in under an hour. Housekeeping: cameras optional, questions in chat or unmute anytime, and there is a hands-on activity near the end. Say your name and team in chat so people can find each other later.")

# ---------------- Slide 2: Learning Objectives ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "By the end of this session you can", 36, TERRA, bold=True, font=HDR)
objs = [
    ("Navigate the dashboard", "Find projects, filters, and your personal task list in seconds."),
    ("Run the core workflow", "Capture a task, organize it on a board, and ship it to done."),
    ("Apply 5 power moves", "Shortcuts and settings that save time every single day."),
]
for i, (head, desc) in enumerate(objs):
    y = 1.9 + i * 1.55
    num_circle(s, 0.95, y, i + 1)
    txt(s, 1.8, y - 0.05, 10.4, 0.5, head, 20, INK, bold=True)
    txt(s, 1.8, y + 0.45, 10.4, 0.6, desc, 15, INK)
notes(s, "Frame the hour: three outcomes, nothing more. Ask the group which objective matters most to their role and note it mentally; if the room is heavy on one role, spend an extra minute in that section. Do not read the bullets aloud.")

# ---------------- Slide 3: Agenda ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "Agenda", 36, TERRA, bold=True, font=HDR)
rows = [
    ("1  Getting Around", "Dashboard zones, your first project"),
    ("2  Core Workflow", "Capture, organize, ship"),
    ("3  Tips & Tricks", "5 power moves + hands-on activity"),
    ("Wrap-up", "Recap, resources, Q&A"),
]
for i, (head, desc) in enumerate(rows):
    y = 1.8 + i * 1.15
    bar = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(y), Inches(0.16), Inches(0.8))
    bar.fill.solid(); bar.fill.fore_color.rgb = SAGE; bar.line.fill.background()
    txt(s, 1.3, y - 0.05, 5.2, 0.5, head, 19, INK, bold=True)
    txt(s, 6.6, y - 0.02, 5.6, 0.5, desc, 15, INK)
notes(s, "Point out the rhythm: short demo blocks with two practice pauses. Tell them timing: roughly 10 minutes per section plus 5 for the activity and 5 for Q&A. If running short, the Tips section is the one to compress, never the activity.")

# ---------------- Slide 4: Section divider 1 ----------------
s = add_slide(TERRA)
txt(s, 0.9, 2.6, 2.0, 1.2, "01", 60, SAND, bold=True, font=HDR)
txt(s, 2.8, 2.85, 9.5, 1.0, "Getting Around", 40, WHITE, bold=True, font=HDR)
notes(s, "Transition line: before we build anything, let us get you oriented so nothing feels unfamiliar. Keep this divider on screen for about ten seconds.")

# ---------------- Slide 5: Teaching (dashboard zones) ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "The dashboard has 3 zones", 36, TERRA, bold=True, font=HDR)
zones = [("Left rail", "Projects, filters, and settings. Pin your top 3."),
         ("Center board", "Where the work lives. Cards move left to right."),
         ("Right panel", "Card details: owner, due date, checklist.")]
for i, (head, desc) in enumerate(zones):
    y = 1.8 + i * 1.5
    num_circle(s, 0.95, y, i + 1)
    txt(s, 1.8, y - 0.05, 4.6, 0.5, head, 20, INK, bold=True)
    txt(s, 1.8, y + 0.45, 4.6, 0.7, desc, 15, INK)
# simple zone diagram on the right
dcolors = [SAGE, TERRA, RGBColor(0xD9, 0xC8, 0xA0)]
for i in range(3):
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                             Inches(7.6 + i * 1.75), Inches(2.0 + i * 0.6), Inches(1.5), Inches(3.0 - i * 0.5))
    box.fill.solid(); box.fill.fore_color.rgb = dcolors[i]; box.line.fill.background()
notes(s, "Live demo: point at each zone on your screen as you name it. The diagram on the right is a simplified map of the real UI. Ask them to find each zone in their own instance before moving on. This is practice pause one.")

# ---------------- Slide 6: Teaching (first project) ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "Your first project in 5 clicks", 36, TERRA, bold=True, font=HDR)
steps = [
    "Click + New Project in the left rail",
    "Name it (try: Team Onboarding)",
    "Pick the Kanban starter template",
    "Invite one teammate by email",
    "Add your first card and drag it to Doing",
]
for i, st in enumerate(steps):
    y = 1.7 + i * 0.95
    num_circle(s, 0.95, y, i + 1, d=0.5)
    txt(s, 1.7, y - 0.02, 10.6, 0.5, st, 17, INK)
notes(s, "Walk through it live, one click at a time, narrating the WHY behind each choice (template first because it teaches structure). Invite step: remind them to use work email only. If the demo fails, fall back to the screenshots workbook in the follow-up email.")

# ---------------- Slide 7: Section divider 2 ----------------
s = add_slide(TERRA)
txt(s, 0.9, 2.6, 2.0, 1.2, "02", 60, SAND, bold=True, font=HDR)
txt(s, 2.8, 2.85, 9.5, 1.0, "Core Workflow", 40, WHITE, bold=True, font=HDR)
notes(s, "Transition line: now that you can find everything, here is the rhythm of daily work. Three verbs: capture, organize, ship.")

# ---------------- Slide 8: Teaching (capture organize ship) ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "Capture, organize, ship", 36, TERRA, bold=True, font=HDR)
cols = [
    ("Capture", "Quick-add with C key. Title first, details later."),
    ("Organize", "Weekly triage: sort, assign, and date every card."),
    ("Ship", "Drag to Done and celebrate. Review stats on Friday."),
]
for i, (head, desc) in enumerate(cols):
    x = 0.9 + i * 4.1
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(2.0), Inches(3.7), Inches(3.4))
    box.fill.solid(); box.fill.fore_color.rgb = WHITE; box.line.color.rgb = SAGE
    txt(s, x + 0.3, 2.25, 3.1, 0.5, head, 20, TERRA, bold=True)
    txt(s, x + 0.3, 2.9, 3.1, 2.2, desc, 15, INK)
    num_circle(s, x + 0.3, 4.6, i + 1, d=0.5)
notes(s, "The three-column layout matches the mental model: left to right, like the board itself. Stress the weekly triage habit: the tool only works if capture stays cheap and triage stays scheduled. Ask: which of the three do you already do well, and which is missing?")

# ---------------- Slide 9: Teaching (boards lists cards) ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "Boards, lists, and cards", 36, TERRA, bold=True, font=HDR)
items = [
    "Board = one project or process (keep it focused)",
    "List = a stage in your flow (To Do, Doing, Done)",
    "Card = one task: title, owner, due date, checklist",
    "Rule of thumb: one card should take under 2 hours",
]
bullets(s, 0.9, 1.8, 6.4, 4.6, items, size=17)
# mini diagram: board with 3 lists of 2 cards
b = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.7), Inches(1.9), Inches(4.9), Inches(4.2))
b.fill.solid(); b.fill.fore_color.rgb = WHITE; b.line.color.rgb = SAGE
for i in range(3):
    lst = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.95 + i * 1.55), Inches(2.2), Inches(1.35), Inches(3.5))
    lst.fill.solid(); lst.fill.fore_color.rgb = SAND; lst.line.fill.background()
    for j in range(2):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1 + i * 1.55), Inches(2.5 + j * 0.95), Inches(1.05), Inches(0.7))
        card.fill.solid(); card.fill.fore_color.rgb = TERRA if j == 0 else SAGE; card.line.fill.background()
notes(s, "Use the diagram: a board is the whole whiteboard, lists are the columns, cards are the sticky notes. The 2-hour rule comes from the onboarding guide; bigger work should be split. Quick check for understanding: ask someone to name a real process on their team that maps to these three levels.")

# ---------------- Slide 10: Section divider 3 ----------------
s = add_slide(TERRA)
txt(s, 0.9, 2.6, 2.0, 1.2, "03", 60, SAND, bold=True, font=HDR)
txt(s, 2.8, 2.85, 9.5, 1.0, "Tips & Tricks", 40, WHITE, bold=True, font=HDR)
notes(s, "Transition line: you have the basics. Here is the layer that makes you fast.")

# ---------------- Slide 11: Teaching (5 power moves) ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "5 power moves", 36, TERRA, bold=True, font=HDR)
moves = [
    "C = quick capture from anywhere",
    "Ctrl + K = jump to any project or card",
    "Due date shortcuts: type 'next tue' instead of picking dates",
    "Saved filters: build one view per meeting you run",
    "Friday digest: turn it on in Settings > Notifications",
]
for i, mv in enumerate(moves):
    y = 1.65 + i * 0.95
    num_circle(s, 0.95, y, i + 1, d=0.5)
    txt(s, 1.7, y - 0.02, 10.6, 0.5, mv, 17, INK)
notes(s, "Fast demo per move, about 20 seconds each. The saved-filters move gets the biggest reaction: show your own 'Monday standup' filter live. Give them the shortcut card PDF from the follow-up email as the takeaway.")

# ---------------- Slide 12: Activity ----------------
s = add_slide(SAND)
txt(s, 0.9, 0.55, 11.5, 0.9, "Try it: 5 minutes", 36, TERRA, bold=True, font=HDR)
box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.8), Inches(11.5), Inches(3.6))
box.fill.solid(); box.fill.fore_color.rgb = WHITE; box.line.color.rgb = TERRA
txt(s, 1.3, 2.1, 10.7, 0.6, "Build a Team Onboarding board", 22, TERRA, bold=True)
bullets(s, 1.3, 2.8, 10.7, 2.4, [
    "1. Create one project from the Kanban template",
    "2. Add 3 cards with owners and due dates",
    "3. Move one card all the way to Done",
    "Bonus: quick-capture one task with the C key",
], size=17)
txt(s, 0.9, 5.7, 11.5, 0.6, "We will screenshare two volunteers when time is up.", 14, TERRA, bold=True)
notes(s, "This is the most important slide. Give clear boundaries: five minutes, work in your own instance, and the bonus is optional. Stay silent for the first minute so people start. At four minutes, call 'one minute left'. Then ask two volunteers to share screens and praise specifics, not generalities.")

# ---------------- Slide 13: Recap & close (dark) ----------------
s = add_slide(TERRA)
txt(s, 0.9, 0.7, 11.5, 1.0, "Recap", 36, WHITE, bold=True, font=HDR)
recap = [
    "3 dashboard zones: rail, board, panel",
    "Core workflow: capture, organize, ship",
    "5 power moves, starting with C and Ctrl + K",
    "Your next step: build one real board this week",
]
bullets(s, 0.9, 1.9, 7.0, 3.6, recap, size=18, color=WHITE)
txt(s, 8.3, 2.0, 4.2, 0.6, "Resources", 20, SAND, bold=True)
bullets(s, 8.3, 2.7, 4.2, 2.8, [
    "Help center: TaskFlow Pro guide",
    "Shortcut card (PDF in follow-up)",
    "Office hours: Thursdays, 30 min",
], size=14, color=SAND)
txt(s, 0.9, 6.4, 11.5, 0.6, "Questions?  |  YourCompany Inc Training Team", 16, SAND)
notes(s, "Recap in their words: ask the room to name one thing they will use tomorrow before you read your own list. Close with the office-hours invite and end on time. Send the follow-up email with the shortcut card and the recorded session within the hour.")

prs.save("os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample-05-training-deck-notes.pptx")")
print("saved:", len(prs.slides._sldIdLst), "slides")
