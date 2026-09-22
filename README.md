# PowerPoint Zero to Hero

**A complete, self-paced Microsoft PowerPoint curriculum from absolute beginner to advanced user.**

Learn PowerPoint through structured modules, 7 real sample decks you can open and reverse-engineer, quizzes, cheat sheets, and flashcards. Works for self-study, AI-assisted learning (NotebookLM, ChatGPT, Claude), and AI agent training pipelines. Comes with 5 study plan lengths (12 / 8 / 6 / 4 / 2 weeks): pick your pace, keep all the content.

---

## Table of Contents

1. [Start Here: How to Use This Package](#start-here-how-to-use-this-package)
2. [What's Inside: Full Content Map](#whats-inside-full-content-map)
3. [Setup Guide: NotebookLM](#setup-guide-notebooklm)
4. [Setup Guide: ChatGPT / Claude / AI Chatbots](#setup-guide-chatgpt--claude--ai-chatbots)
5. [Setup Guide: AI Agents & RAG Systems](#setup-guide-ai-agents--rag-systems)
6. [Setup Guide: Anki Flashcards](#setup-guide-anki-flashcards)
7. [The 9 Modules: What You'll Learn](#the-9-modules-what-youll-learn)
8. [Deck Basics: What a Slide Deck Is and Why It Matters](#deck-basics-what-a-slide-deck-is-and-why-it-matters)
9. [The 7 Sample Decks](#the-7-sample-decks)
10. [Study Plans: 12 / 8 / 6 / 4 / 2 Weeks](#study-plans-12--8--6--4--2-weeks)
11. [Supporting Materials](#supporting-materials)
12. [Who This Is For](#who-this-is-for)
13. [Certification Paths](#certification-paths)
14. [Sources & References](#sources--references)
15. [Contributing](#contributing)
16. [License](#license)
17. [Author & Contributors](#author--contributors)

---

## Start Here: How to Use This Package

**Pick the path that matches how you want to learn:**

### Path A: I want to learn on my own (no AI)
1. Download or clone this repo.
2. Open [11-Study-Plan/00-zero-to-hero-study-plans.md](11-Study-Plan/00-zero-to-hero-study-plans.md) and pick one of 5 tracks (12 / 8 / 6 / 4 / 2 weeks).
3. Follow the schedule: read the module, do the exercises, open the matching sample deck, take the quiz.
4. Check off skills in the [Progress Tracker](11-Study-Plan/progress-tracker.md).
5. Print the [Cheat Sheets](cheat-sheets/) and keep them next to your keyboard.

### Path B: I want AI to teach me (NotebookLM) <sup>Recommended</sup>
1. Go to [notebooklm.google.com](https://notebooklm.google.com) and create a notebook named `PowerPoint Zero to Hero`.
2. Upload the module files (upload order table in [the guide below](#setup-guide-notebooklm)).
3. Start asking questions like:
   - *"Explain slide masters from Module 2 like I'm 10 years old"*
   - *"Quiz me on Module 5 (Animations) one question at a time and grade me"*
   - *"I have 2 hours today on the 6-week track. Make me a minute-by-minute plan"*
   - *"I work in logistics. Design a monthly operations review deck using Modules 3 and 4"*
4. Use **Audio Overview** for podcast-style summaries while commuting.

### Path C: I want ChatGPT or Claude to tutor me
1. Open a new chat and paste the setup prompt from [the guide below](#setup-guide-chatgpt--claude--ai-chatbots).
2. Paste one module at a time and let the AI drill you.
3. Use the follow-up prompts for quizzes, deck reviews, and design feedback.

### Path D: I'm building an AI agent or training system
1. All content is structured Markdown with self-contained `##` sections, ready for RAG ingestion.
2. See [AI Agent Setup](#setup-guide-ai-agents--rag-systems) for chunking strategy, metadata schema, and sample code.
3. Quiz files = ready-made assessment content. Deck-build briefs = exercise generation source.

---

## What's Inside: Full Content Map

### The Folder Structure

```
POWERPOINT Learn/
│
├── 01-Fundamentals/                      # Module 1 - Beginner
│   └── 01-powerpoint-fundamentals.md     # Interface, views, slides, text, formats
│
├── 02-Design-Foundations/                # Module 2 - Beginner+
│   └── 02-design-foundations.md          # Themes, slide master, layouts, .potx templates
│
├── 03-Visual-Design/                     # Module 3 - Intermediate
│   └── 03-visual-design.md               # CRAP principles, type, color, shapes, SmartArt
│
├── 04-Tables-Charts-DataViz/             # Module 4 - Intermediate
│   └── 04-tables-charts-dataviz.md       # Tables, chart chooser, honest axes, infographics
│
├── 05-Transitions-Animations/            # Module 5 - Intermediate+
│   └── 05-transitions-animations.md      # Morph, animation pane, triggers, restraint
│
├── 06-Media-Interactivity/               # Module 6 - Advanced
│   └── 06-media-interactivity.md         # Video/audio, Zoom nav, kiosk mode, export
│
├── 07-Delivery-Workflow/                 # Module 7 - Advanced
│   └── 07-delivery-workflow.md           # Presenter View, accessibility, co-authoring
│
├── 08-VBA-Automation/                    # Module 8 - Advanced+
│   └── 08-vba-automation.md              # VBA object model, batch slides, .ppam add-ins
│
├── 09-Real-World-Projects/               # Module 9 - All levels
│   └── 09-real-world-projects.md         # 6 capstone project briefs with rubrics
│
├── 10-Sources-References/
│   └── sources-references-index.md       # 40+ verified sources, books, courses
│
├── 11-Study-Plan/
│   ├── 00-zero-to-hero-study-plans.md    # 5 tracks: 12 / 8 / 6 / 4 / 2 weeks
│   └── progress-tracker.md               # Checkbox mastery checklist + scoreboard
│
├── sample-decks/                         # 7 REAL .pptx FILES + walkthroughs
│   ├── sample-01-starter-deck.pptx       # 7 slides: fundamentals done right
│   ├── sample-02-business-pitch-deck.pptx # 12 slides: the visual-design showcase
│   ├── sample-03-data-report-deck.pptx   # 9 slides: 6 native charts, honest vs misleading
│   ├── sample-04-animated-product-demo.pptx # 8 slides: Morph + trigger animations
│   ├── sample-05-training-deck-notes.pptx # 13 slides: speaker notes on every slide
│   ├── sample-06-brand-template.potx     # Reusable template (opens in File > New > Personal)
│   ├── sample-06-brand-template.pptx     # Preview copy you can open normally
│   ├── exercise-fix-this-deck.pptx       # DELIBERATELY BAD deck: find the 20 issues
│   ├── walkthrough-01-starter.md         # What to notice in each deck
│   ├── walkthrough-02-pitch-deck.md
│   ├── walkthrough-03-data-report.md
│   ├── walkthrough-04-animated-demo.md
│   ├── walkthrough-05-training-deck.md
│   ├── walkthrough-06-fix-this-deck.md
│   ├── walkthrough-06-brand-template.md
│   ├── build_sample05.py                 # Generators (python-pptx): study these too
│   ├── build_fixme.py
│   ├── build_sample06.py
│   └── qa_verify.py                      # Claims-vs-reality QA script
│
├── cheat-sheets/                         # Printable quick references
│   ├── keyboard-shortcuts-cheat-sheet.md # 92 shortcuts in 8 categories
│   ├── slide-design-rules-cheat-sheet.md # Type sizes, 6x6, 60-30-10, CRAP checklist
│   ├── chart-chooser-cheat-sheet.md      # Story -> chart decision table + cleanup list
│   └── animation-quick-reference.md      # Start modes, Morph in 5 steps, ban list
│
├── quizzes/                              # Self-assessment with answer keys
│   ├── quiz-01-fundamentals.md           # 15 MC + 5 practical = 70 pts each
│   ├── quiz-02-design-foundations.md
│   ├── quiz-03-visual-design.md
│   ├── quiz-04-tables-charts.md
│   ├── quiz-05-transitions-animations.md
│   ├── quiz-06-media-interactivity.md
│   ├── quiz-07-delivery-workflow.md
│   ├── quiz-08-vba-automation.md
│   └── quiz-score-summary.md             # Fillable scoreboard + readiness checklist
│
├── exercises/
│   ├── deck-build-briefs.md              # 10 client-style build briefs with rubrics
│   └── fix-this-deck-challenge.md        # 20-issue challenge + answer key
│
├── anki/
│   ├── powerpoint-flashcards.csv         # 120 cards: Front,Back,Category
│   └── README.md                         # Import guide
│
├── HOW-TO-USE-WITH-AI.md                 # Detailed AI platform guides + prompts
├── path.md                               # How this package was built (process doc)
├── CONTRIBUTORS.md                       # Who did what
└── README.md                             # This file
```

### Content Summary

| Category | Files | What You Get |
|----------|-------|-------------|
| **Learning Modules** | 9 files, ~480 KB | Full curriculum: basics to VBA, plus 6 capstone projects |
| **Sample Decks** | 7 .pptx/.potx + 7 walkthroughs | Real decks with charts, animations, speaker notes, and planted bugs |
| **Quizzes** | 9 files | 120 MC + 40 practical challenges, answer keys, scoreboard |
| **Cheat Sheets** | 4 files | 92 shortcuts, design rules, chart chooser, animation reference |
| **Exercises** | 2 files | 10 build briefs + the 20-issue fix-this-deck challenge |
| **Flashcards** | 1 .csv + guide | 120 Anki-compatible cards across 9 categories |
| **Study Plans** | 2 files | 5 tracks (12/8/6/4/2 weeks) + progress tracker |
| **Sources** | 1 file | 40+ verified references: docs, books, courses, channels |
| **AI Guides** | 1 file | Platform setup + copy-paste prompts |

---

## Setup Guide: NotebookLM

**What is NotebookLM?** Google's free AI research tool. Upload documents and it answers questions using ONLY your uploaded content.

**Step 1:** Go to [notebooklm.google.com](https://notebooklm.google.com) and sign in.

**Step 2:** Click **"Create new notebook"** and name it `PowerPoint Zero to Hero`.

**Want one link instead of many uploads?** Add this single **Website** source and NotebookLM gets the entire course (every module, quiz, cheat sheet, walkthrough, and answer key):

```
https://raw.githubusercontent.com/tempesteni/Microsoft-PowerPoint-Zero-to-hero/main/curriculum-full.md
```

(Built by `make_curriculum_full.py`. If a tool truncates very large pages, fall back to the per-file list below.)

**Step 3:** Upload your sources in this order:

| Upload Order | File | Why This Order |
|-------------|------|----------------|
| 1st | `11-Study-Plan/00-zero-to-hero-study-plans.md` | Gives the AI the curriculum map |
| 2nd-10th | `01-Fundamentals/` through `09-Real-World-Projects/` | The lessons, in sequence |
| 11th | `10-Sources-References/sources-references-index.md` | Reference context |
| 12th-20th | `quizzes/*.md` (9 files) | Assessment content |
| 21st-24th | `cheat-sheets/*.md` (4 files) | Quick-reference context |
| 25th | `exercises/deck-build-briefs.md` | Practice briefs |

**Step 4:** Ask away. Copy-paste starters:

```
I'm a complete beginner. Explain slide masters from Module 2 like I'm 10 years old. Give me 3 real exercises I can try in PowerPoint right now.
```
```
Quiz me on Module 4 (Tables & Charts). Ask 5 questions one at a time, wait for my answer, then grade me and tell me what to review.
```
```
I have 2 hours today and I'm on the 6-week track. What should I study today? Create a minute-by-minute schedule.
```
```
I work in [your field]. Show me how to build a [monthly report] deck using Modules 3 and 4, step by step, with the exact slide structure.
```

---

## Setup Guide: ChatGPT / Claude / AI Chatbots

### Quick Start Prompt (copy-paste this first)

```
I'm learning Microsoft PowerPoint from a structured curriculum. I'll share modules one at a time. For each module:
1. Summarize the 5 most important concepts
2. Explain the hardest concept like I'm a beginner
3. Create 3 quiz questions and wait for my answers
4. Tell me what to focus on next

When I say "quiz me": give me 10 questions (mixed multiple-choice and hands-on) and grade me.
When I say "practice": create a hands-on PowerPoint exercise.
When I say "explain [topic]": break it down step by step.

Ready? Here's Module 1: Fundamentals.

[PASTE THE CONTENT OF 01-Fundamentals/01-powerpoint-fundamentals.md HERE]
```

### Useful Follow-Up Prompts

```
I finished Module [X]. Quiz me with 10 questions, score me out of 100, and tell me which sections to reread.
```
```
I don't understand Morph transitions. Explain 3 ways: like I'm 10, with a business example, and by comparison with ordinary transitions I already know.
```
```
Here's my slide description: [describe]. Give me the layout (positions and sizes in inches), font sizes, and a color palette with hex values.
```
```
Review this deck outline like a presentation coach: [paste outline]. Score it on story, structure, and visual design. Give me the 5 highest-impact fixes.
```
```
I have a job interview that requires presenting. Based on my materials: top 10 PowerPoint/presentation interview questions, model answers, and a 2-day crash plan.
```

---

## Setup Guide: AI Agents & RAG Systems

Every file is structured Markdown with clear `##` hierarchy: compatible with RAG systems, vector databases, and AI tutoring agents.

### Chunking Strategy
```
Source format: Markdown (.md)
Split by: ## headings (each section is self-contained)
Chunk size: ~500-1500 tokens per chunk
Overlap: include the parent heading as context in each chunk
```

### Metadata Schema
```json
{
  "module_number": "01-09",
  "difficulty": "beginner | intermediate | advanced",
  "topic": "fundamentals | design | visual-design | charts | animations | media | delivery | vba | projects",
  "content_type": "lesson | exercise | quiz | cheat_sheet | study_plan | walkthrough",
  "file_path": "relative/path/to/file.md"
}
```

### Embedding & Retrieval
```
Recommended model: text-embedding-3-small or all-MiniLM-L6-v2
Retrieval: Top-k=5 with metadata filter on module_number or difficulty
```

### Agent Modes

| Mode | What It Does | Input |
|------|-------------|-------|
| **Quiz** | Runs quiz files, grades answers | Quiz file + user answer |
| **Explain** | Breaks down concepts | Module file + topic |
| **Practice** | Generates exercises from briefs | Deck-build briefs + difficulty |
| **Progress** | Tracks completion, suggests next | progress-tracker.md + scores |
| **Reference** | Quick lookups | Cheat sheet + query |

### Sample Agent Code
```python
def answer_powerpoint_question(question, user_level="beginner"):
    chunks = vector_db.search(query=question, top_k=5,
                              filter={"difficulty": user_level})
    context = "\n\n".join(c.text for c in chunks)
    prompt = f"""You are a PowerPoint tutor. Use ONLY this context.
    Reference the module and section when possible.

    Context: {context}
    Student question: {question}
    Answer clearly, with an example, and suggest what to learn next."""
    return llm.generate(prompt)
```

---

## Setup Guide: Anki Flashcards

### How to Import

1. Open Anki (free: [apps.ankiweb.net](https://apps.ankiweb.net/)).
2. Click **File > Import** and select `anki/powerpoint-flashcards.csv`.
3. Field mapping: Field 1 > Front, Field 2 > Back, Field 3 > Tags.
4. Click **Import**.

### What's in the Deck (120 cards)

| Category | Cards | Examples |
|----------|-------|---------|
| fundamentals | 15 | Views, placeholder vs text box, file formats |
| design-foundations | 12 | Slide master hierarchy, .potx workflow |
| visual-design | 18 | 60-30-10, merge shapes, no-stretch rule |
| tables-charts | 18 | Chart chooser logic, linked vs embedded |
| animations | 16 | Morph technique, start modes, triggers |
| media-interactivity | 14 | Zoom navigation, kiosk mode, poster frames |
| delivery-accessibility | 12 | Alt text, reading order, handouts |
| vba | 10 | Object model, For Each, .ppam |
| design-principles | 5 | CRAP, assertion-evidence |

**Study tip:** 5 new cards per day. Anki's spaced repetition shows weak cards more often.

---

## The 9 Modules: What You'll Learn

### Module 1: Fundamentals (Beginner)
Interface tour, the 5 views, creating slides, layouts and placeholders vs text boxes, outline view, bullet discipline (6x6), sections, slide size, file formats (.pptx, .potx, .ppsx, .pptm, PDF), saving and autosave, essential shortcuts.

### Module 2: Design Foundations (Beginner+)
Themes and variants, slide master vs layouts, editing masters (logos, footers, slide numbers), placeholders, building and saving .potx templates, background formatting, Reset, Design Ideas, building a brand system.

### Module 3: Visual Design (Intermediate)
CRAP principles, assertion-evidence slides, typography (36-44pt titles / 14-24pt body), color theory (60-30-10, contrast, color-blind-safe palettes), shapes and Merge Shapes, icons and SVG, image cropping and compression, SmartArt, alignment tools, avoiding dated looks.

### Module 4: Tables, Charts & DataViz (Intermediate)
Table styling, every chart type, chart chooser logic (comparison / trend / composition / relationship), editing chart data, linked vs embedded Excel data, chart formatting, chart junk and the data-ink ratio, shape-built infographics and KPI callouts, honest axes and ethical display.

### Module 5: Transitions & Animations (Intermediate+)
Transitions vs animations, Morph (object matching, the duplicate-slide technique), the animation pane, entrance/emphasis/exit/motion paths, start modes, timing and delay, animating charts by category, triggers, Animation Painter, animation restraint (the 3-second rule).

### Module 6: Media & Interactivity (Advanced)
Video insert/trim/poster frame, playback options, audio and narration, compressing media, screen recording, hyperlinks and action buttons, Slide/Section/Summary Zoom menus, Custom Shows, kiosk mode, export to MP4/GIF, media accessibility.

### Module 7: Delivery & Workflow (Advanced)
Speaker notes (prompts not scripts), Presenter View, Rehearse Timings and recording, co-authoring and comments, Compare & Merge, accessibility (checker, alt text, reading order), exporting PDF/video, printing handouts, protecting decks, pre-flight checklist.

### Module 8: VBA Automation (Advanced+)
Developer tab and macro security, the macro recorder's limits, the VBA editor, the PowerPoint object model, Sub procedures, variables, loops and conditionals, bulk slide generation (including from Excel), error handling, .ppam add-ins, when NOT to use VBA.

### Module 9: Real-World Projects (All levels)
6 capstone briefs with build walkthroughs and 10-criterion rubrics: startup pitch deck, training/workshop deck, quarterly business review, conference talk, animated product demo, branded template system. Plus a final "build for a real need" capstone.

---

## Deck Basics: What a Slide Deck Is and Why It Matters

New to presentations? This 2-minute primer covers the vocabulary the rest of this package uses.

**What is a deck?**
A deck (short for "slide deck") is a sequence of slides shown on a screen while a person speaks. The name comes from a deck of cards: each slide is one card in the stack. "Deck", "presentation", and "slide show" all mean the same thing. PowerPoint saves them as `.pptx` files.

**Why decks exist**
Slides are visual backup for a speaker, not a document to read. A good deck does three jobs:
- Makes one point per slide graspable in 3 seconds
- Gives the audience something to look at while you talk
- Leaves behind a record that still works after you leave the room (the deck that gets emailed after the meeting)

**Deck vs document vs spreadsheet**

| | Deck | Document | Spreadsheet |
|---|---|---|---|
| How it's read | On a screen, paced by a speaker | At your own pace | At your own pace |
| Text density | Low: one idea per slide | High: paragraphs | High: grids of numbers |
| Best for | Decisions, pitches, teaching | Details, records | Analysis, calculations |
| The quality test | Can the back row read it? | Can I find the detail later? | Can I trust the formula? |

**Why decks matter at work**
The deck is often the deliverable that keeps working after the meeting:
- **Pitch decks** win or lose funding
- **Business reviews and updates** drive decisions
- **Training decks** let one instructor teach many people, repeatedly
- **Conference talks** build reputation and open doors

**The anatomy of a deck**
Most decks follow the same skeleton: a title slide, an agenda, content slides (the evidence), section dividers (for long decks), and a closing slide with the ask or takeaway. Underneath sits the slide master: the design spine that keeps every slide on-brand (Module 2).

**How this package uses decks**
Everything in `sample-decks/` is a real `.pptx` file, not a picture of one. Open each deck while studying its walkthrough, rebuild parts of it in the exercises, and use `exercise-fix-this-deck.pptx` to train your eye on what to avoid. Reading real decks is how design instincts are built.

---

## The 7 Sample Decks

Real `.pptx` files you open and study, each with a walkthrough explaining what to notice.

| Deck | Slides | Teaches | Highlight |
|------|--------|---------|-----------|
| `sample-01-starter-deck.pptx` | 7 | Module 1 | Fundamentals done right |
| `sample-02-business-pitch-deck.pptx` | 12 | Modules 2-3 | The visual-design showcase |
| `sample-03-data-report-deck.pptx` | 9 | Module 4 | 6 native charts, honest vs misleading axes |
| `sample-04-animated-product-demo.pptx` | 8 | Module 5 | Morph transitions + click-trigger reveal |
| `sample-05-training-deck-notes.pptx` | 13 | Module 7 | Speaker notes on all 13 slides |
| `sample-06-brand-template.potx` | 6 layouts | Module 2 | Reusable branded template |
| `exercise-fix-this-deck.pptx` | 8 | All | Deliberately bad: find the 20 planted issues |

Every deck uses fictional brands and data (YourCompany Inc / TaskFlow Pro). The generators (`build_sample*.py`) that produced the decks are included: reading them is a Module 8 lesson in itself.

---

## Study Plans: 12 / 8 / 6 / 4 / 2 Weeks

The content never changes, only the pace. Every track covers all modules, projects, and quizzes.

| Track | Weeks | Hours/week | Best for |
|------|-------|-----------|----------|
| 12-Week Mastery | 12 | 6-8 | Deep, lasting skill |
| 8-Week Standard | 8 | 8-10 | Most learners with a day job |
| 6-Week Accelerated | 6 | 10-12 | Some Office experience |
| 4-Week Sprint | 4 | 12-15 | Fast upskilling for a job or project |
| 2-Week Crash | 2 | 18-25 | Deadlines: interviews, certification, a big talk |

Full weekly schedules, daily session rhythm, and score gates: [11-Study-Plan/00-zero-to-hero-study-plans.md](11-Study-Plan/00-zero-to-hero-study-plans.md).

---

## Supporting Materials

### Quizzes (test yourself)
Each quiz: **15 multiple-choice** (3 pts each) + **5 practical challenges** (5 pts each) = **70 points**, with full answer keys and model solutions.

| Score | Meaning |
|-------|---------|
| 90%+ (63+) | Advance to the next module |
| 70-89% (49-62) | Review weak areas, then advance |
| Below 70% (<49) | Restudy the module before moving on |

### Cheat Sheets (print these)
Shortcuts (92), slide design rules, chart chooser, animation quick reference.

### Exercises
10 client-style deck-build briefs (30-120 min each, with self-grading criteria) and the Fix-This-Deck challenge (spot 20 planted issues, score yourself, then rebuild it properly).

---

## Who This Is For

- **Complete beginners** who have never opened PowerPoint
- **Career switchers** who need decks for work, pitches, or training
- **Students** preparing for MOS certification
- **Self-learners** who want structure instead of scattered videos
- **Professionals** whose decks currently look like documents and want them to look like presentations
- **AI engineers** building presentation training agents or RAG systems
- **Teachers and trainers** adapting a ready-made curriculum

---

## Certification Paths

There are real certifications worth pairing with this curriculum. Every link below was verified live.

| Certification | Provider | What It Tests | Difficulty | Link |
|--------------|----------|---------------|------------|------|
| MOS: PowerPoint Associate | Microsoft / Certiport | Core creation, delivery, and design | Beginner-Intermediate | [MOS program page](https://www.microsoft.com/en-us/learning/mos-certification.aspx) |
| MOS: PowerPoint Expert | Microsoft / Certiport | Advanced features and automation | Advanced | [Book via Certiport](https://www.certiport.com/) |
| Microsoft 365 Fundamentals (MS-900) and other M365 certifications | Microsoft Learn | Broad Microsoft 365 literacy | Beginner | [Browse certifications](https://learn.microsoft.com/en-us/credentials/certifications/) |
| Course certificates: presentation skills | Coursera | Delivery, storytelling, design | All levels | [Search courses](https://www.coursera.org/search?query=presentation%20skills) |
| Course certificates: presentation & communication | edX | Delivery and storytelling | All levels | [Search courses](https://www.edx.org/search?q=presentation) |
| Certificates of completion | LinkedIn Learning | Practical PowerPoint tracks | All levels | [LinkedIn Learning](https://www.linkedin.com/learning/) |

**Booking MOS exams:**
- Exams are delivered through Certiport authorized test centers: register at [certiport.com](https://www.certiport.com/).
- Exam codes change between generations (the PowerPoint Associate exam has carried codes like MO-300). Always confirm the current code and objectives on the official pages above before booking.
- Note: Microsoft's online credential catalog currently returns no results for "PowerPoint" (MOS is administered via Certiport), so use the MOS program page and the Certiport link rather than hunting through the Learn catalog.

**How this package prepares you:**
- Modules 1-3 cover the Associate core (creation and design), Modules 4-7 cover delivery and collaboration, Module 8 covers the Expert automation territory.
- Book a certification exam only after scoring 63+/70 (90%+) on all 8 quizzes in `quizzes/` and finishing at least 4 of the 6 projects in Module 9.
- Use `quizzes/quiz-score-summary.md` as your readiness checklist.

---

## Sources & References

This curriculum draws from **40+ verified sources**, all curl-tested live before release:

- **Official:** Microsoft Support, Microsoft Learn, Microsoft Create, Microsoft 365 Roadmap
- **Design craft:** Presentation Guru, Think Outside the Slide (Dave Paradi), Duarte
- **YouTube:** Leila Gharani, Kevin Stratvert, Simon Sez IT, PPT Guru, Microsoft
- **Books:** slide:ology (Duarte), Resonate (Duarte), Presentation Zen (Reynolds), Beyond Bullet Points (Atkinson), The Non-Designer's Design Book (Williams), Storytelling with Data (Knaflic), Speaking PowerPoint (Gabrielle)
- **Communities:** r/powerpoint, Microsoft Tech Community, Super User, Stack Overflow (powerpoint-vba)

Full bibliography with ISBNs and attribution notes: [Sources & References Index](10-Sources-References/sources-references-index.md).

---

## Contributing

Found an error? Want to add content?

1. Fork this repo.
2. Make your changes (everything is Markdown; decks regenerate via the included scripts).
3. Submit a pull request.

Contributions welcome: new modules, more sample decks, additional briefs, translations, corrections.

---

## License

This project is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

- **Share** - copy and redistribute in any format
- **Adapt** - remix, transform, and build upon the material
- **Attribution** - give credit and link to this repo

---

## Author & Contributors

Created by **[tempesteni](https://github.com/tempesteni)** with **[Hermes Agent](https://hermes-agent.nousresearch.com)** by Nous Research.

| Contributor | Roles |
|-------------|-------|
| tempesteni | Concept and curriculum direction, scope decisions, review, corrections, quality control, publishing decisions |
| Hermes Agent | Research and compilation, module authoring, quiz/flashcard/cheat sheet generation, sample deck generation, animation XML engineering, URL verification, content and security verification, documentation |

**Stats:** 56 files | ~100,000 words | 8 modules + 6 capstone projects | 7 sample decks | 9 quizzes | 120 flashcards | 5 study tracks | estimated study time 40-120 hours depending on track | prerequisites: basic computer literacy, access to PowerPoint (2019, 2021, or Microsoft 365) for practice.
