# PowerPoint Zero to Hero: Full Curriculum (Single-File AI Edition)

> One link, the complete course. Built so AI tools can see everything at once.
>
> **How to use:** in NotebookLM add this page as a single **Website** source. In ChatGPT/Claude, paste the link and ask your questions. In a RAG system, chunk by `## FILE:` headings.
>
> **Companion binaries:** the sample decks live as separate .pptx/.potx files in the GitHub repo (this file keeps their walkthroughs).
>
> **Regenerated from source files** by `make_curriculum_full.py`. Prefer per-file sources? Use the raw links listed in the README.

## Table of Contents

- `README.md`
- `01-Fundamentals/01-powerpoint-fundamentals.md`
- `02-Design-Foundations/02-design-foundations.md`
- `03-Visual-Design/03-visual-design.md`
- `04-Tables-Charts-DataViz/04-tables-charts-dataviz.md`
- `05-Transitions-Animations/05-transitions-animations.md`
- `06-Media-Interactivity/06-media-interactivity.md`
- `07-Delivery-Workflow/07-delivery-workflow.md`
- `08-VBA-Automation/08-vba-automation.md`
- `09-Real-World-Projects/09-real-world-projects.md`
- `10-Sources-References/sources-references-index.md`
- `11-Study-Plan/00-zero-to-hero-study-plans.md`
- `11-Study-Plan/progress-tracker.md`
- `HOW-TO-USE-WITH-AI.md`
- `cheat-sheets/animation-quick-reference.md`
- `cheat-sheets/chart-chooser-cheat-sheet.md`
- `cheat-sheets/keyboard-shortcuts-cheat-sheet.md`
- `cheat-sheets/slide-design-rules-cheat-sheet.md`
- `quizzes/quiz-01-fundamentals.md`
- `quizzes/quiz-02-design-foundations.md`
- `quizzes/quiz-03-visual-design.md`
- `quizzes/quiz-04-tables-charts.md`
- `quizzes/quiz-05-transitions-animations.md`
- `quizzes/quiz-06-media-interactivity.md`
- `quizzes/quiz-07-delivery-workflow.md`
- `quizzes/quiz-08-vba-automation.md`
- `quizzes/quiz-score-summary.md`
- `sample-decks/walkthrough-01-starter.md`
- `sample-decks/walkthrough-02-pitch-deck.md`
- `sample-decks/walkthrough-03-data-report.md`
- `sample-decks/walkthrough-04-animated-demo.md`
- `sample-decks/walkthrough-05-training-deck.md`
- `sample-decks/walkthrough-06-brand-template.md`
- `sample-decks/walkthrough-06-fix-this-deck.md`
- `exercises/deck-build-briefs.md`
- `exercises/fix-this-deck-challenge.md`
- `anki/README.md`
- `anki/powerpoint-flashcards.csv`
- `CONTRIBUTORS.md`
- `path.md`

---


## FILE: README.md

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


## FILE: 01-Fundamentals/01-powerpoint-fundamentals.md

# Module 01: PowerPoint Fundamentals

---
**Module number:** 01
**Title:** PowerPoint Fundamentals
**Level:** Beginner
**Prerequisites:** None. Basic mouse and typing skills assumed. Microsoft PowerPoint 2019, 2021, or Microsoft 365 (Windows or Mac). Steps reference the Windows ribbon; Mac locations are noted where they differ.
**Estimated study time:** 2.5 - 3 hours (plus 2-3 hours of hands-on practice)
**Next module:** 02 - Design and Visual Communication (themes, colors, fonts, and slide design basics)
---

Welcome to the first module of **PowerPoint Zero to Hero**. By the end of this module you will know the PowerPoint interface blind, understand how slides are actually built (layouts and placeholders, not just typing on white rectangles), and you will have created, saved, and exported your first real presentations. Everything here is foundation: the design, storytelling, animation, and presenting skills in later modules all sit on top of what you learn in these sections.

---

## 1. What PowerPoint Is and When to Use It

### Explanation

Microsoft PowerPoint is a **presentation graphics application**. Its job is to help you build a sequence of visual slides that support a live or recorded talk. A slide can hold text, images, shapes, charts, tables, video, and animation, but the mental model that matters is this: **the slide supports the speaker, the speaker does not read the slide**.

PowerPoint is part of the Microsoft 365 / Office family alongside Word and Excel. The difference in philosophy matters:

- **Word** is for documents people *read*. Linear, dense, complete sentences.
- **Excel** is for numbers people *analyze*. Tables, formulas, exploration.
- **PowerPoint** is for ideas people *need to be convinced of*. Short, visual, persuasive, spoken.

**When PowerPoint is the right tool:**

- Business case or project proposal to stakeholders or leadership.
- Quarterly business review, sales pitch, investor update.
- Training or teaching a class session with visual aids.
- Conference or meetup talk (20-45 minutes).
- Webinar or recorded video lesson.
- Event rundown: wedding slideshow, graduation recap, family photo story.
- Reporting results where a chart or before/after image beats a paragraph.

**When PowerPoint is the wrong tool** (and what to use instead):

- A document people will read alone: use **Word** or a PDF.
- A living dataset people filter and explore: use **Excel**.
- Heavy documentation or a wiki: use **Word**, **OneNote**, or **SharePoint**.
- A one-screen handout with no spoken talk: write a one-pager in Word and export to PDF.

A useful test: *"Will someone talk while this is on screen?"* If yes, PowerPoint. If people read it silently in an inbox, Word or PDF is usually better.

### Real-world examples

- **Business:** A project manager at YourCompany Inc presents a 12-slide status deck to the steering committee: problem, timeline, budget, risks, ask. Total on screen: 10 minutes, then discussion.
- **Education:** A teacher builds a 20-slide lesson on the water cycle with diagrams and one question per slide to prompt class discussion.
- **Personal:** A family photo story of 30 slides with captions and music for a 60th birthday dinner.

### Try it now

Open PowerPoint and look at the start screen. Answer in writing (paper or a note): for one real talk you will give in the next month, write the *single sentence* the audience should remember afterward. That sentence is the seed of your presentation. Keep it, you will use it in the practice projects.

---

## 2. Interface Tour: Ribbon, Tabs, Quick Access Toolbar, Thumbnails Pane, Status Bar

### Explanation

PowerPoint's window has five zones you must be able to name and find without thinking.

1. **Title bar** (top): file name plus AutoSave toggle and account. Double-click empty title bar space to maximize/restore.
2. **Ribbon** (below title bar): the command surface. It is organized into **tabs** (File, Home, Insert, Design, Transitions, Animations, Slide Show, Review, View, Help, plus contextual tabs that appear only when you select something, such as **Shape Format** or **Picture Format**). Each tab has **groups** (Clipboard, Slides, Font, Paragraph, Drawing on the Home tab) and inside groups are buttons, dropdowns, and small **dialog launchers** (the tiny arrow in the bottom-right corner of a group opens the full dialog box).
3. **Quick Access Toolbar (QAT)** (top-left by default, or above the ribbon when floated): Save, Undo, Redo, and the **Customize Quick Access Toolbar** dropdown. This is the one toolbar you should personalize on day one (see steps below).
4. **Thumbnails pane** (left): one small image per slide, drag to reorder, right-click to add/delete/duplicate, and (since PowerPoint 2016) collapsible **sections** shown as headers.
5. **Slide canvas** (center): the slide you are editing, with placeholders and rulers if enabled.
6. **Notes pane** (below the canvas): your speaker notes. Collapsed by default on some layouts; drag the top edge up to expand.
7. **Status bar** (bottom): slide number ("Slide 3 of 12"), language, spelling status, **Notes** button, comments, view buttons (Normal / Slide Sorter / Reading View / Slide Show) and the **zoom slider** with "Fit slide to current window" button.

**Ribbon behaviors that confuse beginners:**

- **Contextual tabs** (green or colored, e.g. *Shape Format*) only appear when you select a matching object. If a tab "disappeared", click the object again.
- **Ctrl + F1** collapses and expands the ribbon. If your ribbon is "gone", that is why.
- Right-click almost anything for a context menu with the most common commands.
- The **File** tab opens the **Backstage** view (New, Open, Save, Save As, Export, Print, Share, Account, Options). Press **Esc** to leave it.

### Step-by-step: pin the commands you always need to the Quick Access Toolbar

1. Click the small dropdown arrow on the **Quick Access Toolbar** (right of the Undo icon) at the top-left of the window.
2. In the list, click **More Commands...** (or right-click any ribbon button and choose **Add to Quick Access Toolbar**).
3. In **PowerPoint Options > Quick Access Toolbar**, set "Choose commands from" to **Popular Commands**.
4. Add **New Slide**, **Format Painter**, and **Align Objects**, then click **Add >>** for each.
5. Check **Show Quick Access Toolbar** and choose **Below the Ribbon** if you prefer it closer to the canvas.
6. Click **OK**. Your three commands now sit as small icons at the top of the window in every presentation.

### Step-by-step: turn on rulers and gridlines (View tab)

1. Open the **View** tab.
2. In the **Show** group, tick **Ruler**, **Gridlines**, and **Guides** as needed.
3. Right-click the slide and choose **Grid and Guides > Grid Settings...** to change spacing.

### Real-world examples

- **Business:** You add **Email** and **Publish Slides** to the QAT in your reporting profile so weekly decks take 3 fewer clicks per export.
- **Education:** A teacher keeps **Duplicate Slide** on the QAT because lesson decks are built by cloning the previous slide's structure.
- **Personal:** Turn off Gridlines before a photo slideshow; turn them on for a diagram-heavy workflow.

### Try it now

1. Collapse the ribbon with **Ctrl + F1**, then bring it back with the same shortcut.
2. Right-click the **Bold** button on the Home tab and choose **Add to Quick Access Toolbar**.
3. Click a shape (Insert > Shapes > Rectangle, draw one) and find the contextual **Shape Format** tab that appears, then press **Esc** twice and watch it vanish. Write down where the contextual tabs appear for pictures, tables, and charts by trying each (Insert > Picture, Insert > Table, Insert > Chart).

---

## 3. The Five Views: Normal, Slide Sorter, Notes Page, Reading View, Presenter View

### Explanation

PowerPoint has five ways of looking at the same presentation. Choosing the right one changes how fast you work.

| View | What it is for | How to open |
|---|---|---|
| **Normal** | Default. Editing slides one at a time, with thumbnails and notes. | View tab > Normal, or status bar icon |
| **Slide Sorter** | Bird's-eye reorganizing: drag slides, apply transitions to many slides, spot pacing problems. | View tab > Slide Sorter, or status bar icon |
| **Notes Page** | See and edit what prints for the speaker: slide on top, notes below. Prepare handouts here. | View tab > Notes Page |
| **Reading View** | Run the slideshow inside the window (no full screen) for quick self-checks or sending a deck to review. | View tab > Reading View, or status bar icon |
| **Slide Show** (with **Presenter View** when two displays) | Deliver the talk. Full screen for the audience; Presenter View shows you the current slide, next slide, notes, timer, and annotation tools. | Slide Show tab > From Beginning (**F5**) or From Current Slide (**Shift + F5**) |

Two other views that appear in the **View** tab and matter later: **Slide Master** (module on templates) and **Outline View** (covered in section 6 of this module).

**Presenter View essentials** (Slide Show tab > Set Up Slide Show > "Use Presenter View" must be checked, and Windows display mode should be "Extend", not "Duplicate"):

- You see: current slide, **Next Slide** preview, **Notes**, timer, black/white screen (**B** / **W**), and tools (laser pointer, pen, highlighter) via the pen icon at bottom-left.
- The audience sees only the current slide.
- With one monitor, hold **Alt + F5** to preview Presenter View in a window.

### Step-by-step: preview a deck in Reading View without leaving the window

1. Open any presentation (or the one you started in the Try it now of section 1).
2. Click the **Reading View** icon on the status bar (third from the right), or **View > Reading View**.
3. Press **Space**, **Right Arrow**, or **N** to advance; **Left Arrow** or **P** to go back.
4. Press **Esc** to return to Normal view. Nothing was lost.

### Real-world examples

- **Business:** Slide Sorter is where you discover that slides 8-14 are all "middle-of-story" and cut three of them before the review.
- **Education:** A teacher checks slide pacing with Reading View on a laptop before class instead of firing up the projector.
- **Personal:** Notes Page view is how you print cue-card style notes to read from at a wedding toast.

### Try it now

Open any deck and run this 60-second circuit: Normal > Slide Sorter (drag slide 2 to position 5) > Notes Page (type one line of speaker notes) > Reading View (step through 3 slides) > back to Normal. Then undo everything with **Ctrl + Z** until the deck is back to its original order. This circuit is your new habit whenever you finish a draft.

---

## 4. Creating Presentations and Slides

### Explanation

A **presentation** is one .pptx file containing **slides**. A slide is a canvas built from a **layout** (next section) that pulls colors, fonts, and backgrounds from the theme. New presentations can start from a blank file, a template, or an existing file you copy.

Rules of thumb for slide count and flow:

- Plan 1-2 minutes per slide for a business talk; less for data-dense slides.
- Structure: title/agenda, context or problem, your content in 2-5 chunks, summary, and a clear "ask" or next step.
- More slides is fine; dense slides are not. A 30-slide fast deck beats 10 packed ones.

### Step-by-step: create a presentation

1. Open PowerPoint. On the start screen pick **Blank Presentation**, or a template thumbnail (this opens the New screen with search).
2. For templates: **File > New**, type a keyword (e.g. "pitch", "lesson") in the search box, pick a result, then **Create**.
3. Save immediately: **Ctrl + S**, choose **OneDrive - YourCompany Inc** or **This PC**, type a name like `2026-09-QBR-YourCompany-Deck`, click **Save**. (Section 11 covers formats and AutoSave.)

### Step-by-step: add, rename, duplicate, delete, and reorder slides

1. In the **Thumbnails pane**, click the slide you want to build on.
2. **New slide with layout picker:** on the **Home** tab, click the top half of the **New Slide** button to reuse the previous slide's layout, or the bottom half (dropdown arrow) to choose a layout from the list. Shortcut: **Ctrl + M**.
3. **Duplicate:** right-click the thumbnail > **Duplicate Slide** (great for keeping identical structure across parallel slides).
4. **Reorder:** drag the thumbnail up or down in the pane, or use Slide Sorter for longer moves.
5. **Rename:** right-click the thumbnail > **Rename Slide** (the name shows in Outline View and in Zoom/Summary features later).
6. **Delete:** select and press **Delete**, or right-click > **Delete Slide**.
7. **Hide a slide** (keep it in the file but skip when presenting): right-click > **Hide Slide**; the number gets crossed out.

### Step-by-step: import slides from another deck

1. **Home > New Slide > Reuse Slides...**
2. The Reuse Slides pane opens; click **Browse > Browse File** and pick the other .pptx.
3. Tick **Keep source formatting** at the bottom if you want the donor deck's look, then click each slide in the pane to insert it.

### Real-world examples

- **Business:** Weekly status decks are built by right-clicking last week's file in File Explorer, choosing **Copy**, pasting, renaming with the date, then editing only what changed.
- **Education:** A lecture template of 12 skeleton slides (title, objectives, 6 content, quiz, summary) is cloned per lesson.
- **Personal:** Duplicate the "photo + caption" slide 15 times, then replace content slide by slide, like filling in a form.

### Try it now

Create a blank presentation titled `Try01-MyFirstDeck`. Add 5 slides with these layouts in order: Title Slide, Title and Content, Section Header, Two Content, Title Only. Then reorder so the Section Header is slide 2, duplicate slide 3, and delete the original. Save with **Ctrl + S**.

---

## 5. Slide Layouts and Placeholders vs Text Boxes

### Explanation

This is the single most important structural concept in PowerPoint, and the one beginners get wrong.

A **slide layout** is a pre-designed arrangement of **placeholders** that comes from the **Slide Master** (the theme's blueprint). A **placeholder** is a content region that knows what it is: a title placeholder, a text/body placeholder, a picture placeholder ("Click icon to add picture"), chart, table, media, etc. Placeholders are inherited from the theme, so they carry fonts, sizes, colors, and positions automatically, and they feed Outline View and section summaries.

A **text box** is a free-floating object you draw anywhere with **Insert > Text Box**. It has no theme knowledge, no outline entry, and no automatic bullet styling from the layout. Text boxes are for labels, callouts, quotes, and captions that sit outside the structure.

| | Placeholder | Text box |
|---|---|---|
| Created by | The slide layout (theme) | You, via Insert > Text Box |
| Position | Fixed by layout, consistent across slides | Anywhere |
| Shows in Outline View | Body text yes, titles yes | No |
| Updates with theme | Yes (fonts/colors follow the master) | Only manually |
| Right use | All structured content | Labels, callouts, marginalia |

The common standard layouts: **Title Slide**, **Title and Content**, **Section Header**, **Two Content**, **Comparison**, **Title Only**, **Blank**, **Content with Caption**, **Picture with Caption**. Microsoft's built-in themes ship all of these.

**The beginner mistake to avoid:** typing everything into pasted text boxes because "it looks the same". It does not look the same after a theme change, and the text will not appear in Outline View or convert to other layouts. Use **Home > Layout** to change a slide's layout at any time, and use **Home > Reset** to snap placeholders back to their theme-defined position after manual nudging.

### Step-by-step: build a slide correctly with layout and placeholders

1. Select the slide in the Thumbnails pane.
2. **Home > Layout** and choose **Two Content**.
3. Click inside the **left content placeholder** ("Click to add text" or the six icons: table, chart, SmartArt, picture, online picture, video) and pick **Picture > This Device**, choose `C:\Users\Public\Pictures\Sample Pictures\demo-product-shot.png` (any image will do).
4. Click the **right body placeholder** and type two short lines.
5. Now insert a text box on the same slide: **Insert > Text Box**, click near the bottom, type `Confidential - for internal review`. Notice this text does NOT appear in the outline (check **View > Outline View**).
6. Change the theme (**Design** tab, pick a theme) and watch placeholders restyle while the text box stubbornly keeps its old font until you fix it manually.

### Step-by-step: change a slide's layout and reset placeholders

1. Click the slide thumbnail.
2. **Home > Layout > Comparison** and observe the placeholders rearrange (content is kept where the placeholder types match).
3. If someone dragged a placeholder off-position, click **Home > Reset** to return it to the layout-defined position.

### Real-world examples

- **Business:** A 40-slide deck restyled to brand colors in 2 minutes by switching the theme because every slide used placeholders.
- **Education:** Quiz slides use the Comparison layout: question on the left placeholder, answer on the right, hidden until discussion.
- **Personal:** Photo slides use the Picture with Caption layout so every photo snaps to identical size and position.

### Try it now

On a new slide apply the **Comparison** layout. Put text in the left placeholder and a picture in the right one. Add one text box label at the top-right corner saying `DRAFT`. Switch the theme via **Design** tab and note which object changes and which does not. Then use **Home > Reset** and delete the text box. Success: you can explain out loud why the text box did not follow the theme.

---

## 6. Adding and Structuring Text, and Working in Outline View

### Explanation

Text on slides has two jobs: **headline** (the slide's claim) and **support** (bullets, labels, or captions). Good structure comes first; styling comes later.

Principles for adding and structuring text:

1. **Titles are assertions, not topics.** "Q3 revenue grew 14% in EMEA" beats "Q3 Results".
2. **One idea per slide.** If a slide needs "and", it is probably two slides.
3. **3-6 body lines per slide**, each a phrase of at most 2 lines (see the 6x6 rule in section 7).
4. **Level your text:** level 1 for main points, level 2 for supporting detail, level 3 rarely. Use **Tab** / **Shift + Tab** in a placeholder to demote/promote (or the **Home > Increase List Level** buttons).
5. **Type into placeholders, draw text boxes only for labels.** (Section 5.)

**Outline View** (**View > Outline View** or **Home > New Slide > Slides from Outline...**) is the fastest structuring tool in PowerPoint and almost nobody uses it. The left pane switches from slide thumbnails to a text outline: each slide's title at top level, body bullets indented beneath. You can write a whole deck here at typing speed, then switch back and design.

### Step-by-step: build a deck skeleton in Outline View

1. Open a blank presentation. **View > Outline View**.
2. In the outline pane, type: `Quarterly Business Review - YourCompany Inc` then press **Enter**.
3. Press **Tab** (the new line demotes and becomes body text of slide 1). Type `Presenter: jdoe@acme.com (fake example)` and `Date: 22 Sep 2026`.
4. Press **Enter**, then **Shift + Tab** to promote back to slide level. Type `Agenda`, press **Enter**.
5. Press **Tab**, then type each bullet on its own line: `Business update`, `Customer wins`, `Risks`, `Asks`.
6. Press **Enter**, **Shift + Tab**, type `Business update`, and continue. Each top-level line creates a new slide instantly.
7. To reorganize: drag slide icons in the outline pane to reorder whole slides, or select bullets and drag to move text between slides.
8. Switch back with **View > Normal**. All slides now have titles and body text in the correct placeholders.

### Step-by-step: promote, demote, and use keyboard text controls

- **Tab** at the start of a bullet: demote one level. **Shift + Tab**: promote one level.
- **Ctrl + Shift + C / Ctrl + Shift + V**: copy/paste formatting only (like Format Painter).
- **Ctrl + A** inside the outline pane selects all outline text for bulk font changes (**Home** tab).
- **Insert > Text Box**, then click once and type for a point text box; drag to draw a paragraph text box.

### Real-world examples

- **Business:** A consultant drafts a 30-slide client deck entirely in Outline View during a 20-minute train ride, then designs it on arrival.
- **Education:** A lecturer pastes an existing Word document heading structure via **Home > New Slide > Slides from Outline...** and PowerPoint turns each Heading 1 into a slide title (Word styles must be Heading 1/2, not just bold text).
- **Personal:** Outline View is the fastest way to write thank-you slide captions for a wedding photo deck.

### Try it now

In Outline View, build exactly 4 slides about your week: `Week of 22 Sep 2026`, `Wins`, `Blockers`, `Next Week`. Each with 3 bullets at level 1 and 1 bullet at level 2. Then drag "Blockers" above "Wins" in the outline pane and check in Normal view that the slides really swapped. Time yourself: aim for under 3 minutes.

---

## 7. Bullet Discipline: The 6x6 Rule and When NOT to Use Bullets

### Explanation

Bullets are the most abused feature in PowerPoint. Audiences cannot read and listen at the same time: if your slide is a wall of text, they read silently and miss your voice. Bullet discipline fixes this.

**The 6x6 rule (guideline, not law):** at most **6 bullets per slide**, at most **6 words per bullet**. It forces brevity and creates white space. Use it as a checklist, then flex: 4x4 for executive audiences, up to 8 short items only when the slide is a reference list the audience keeps.

Supporting rules:

- Bullets are **phrases**, not sentences. No periods. No "and then...". No paragraphs.
- Maximum 2 levels of nesting; level 3+ signals the slide should be split.
- Parallel structure: all bullets start the same way (all verbs, or all nouns).
- Give the slide a **claim title** so the bullets only need to prove it.
- Numbers and dates belong in charts and tables, not bullets.

**When NOT to use bullets:**

| Situation | Use instead |
|---|---|
| A powerful quote or one-sentence statement | Large centered text, no bullets (a "statement slide") |
| Numeric comparison of 3+ items | Chart or table (module 03/04) |
| A process or timeline | Shapes with arrows, SmartArt, or a diagram |
| Emotional moment, story, photo | Full-bleed image with 5-word caption |
| Detailed data people will study | Table or an appendix slide |
| Speaker's words | Speaker notes (View > Notes Page), not the slide |

If a slide is only bullets and you cannot cut it below 6, split it into two slides or move the detail to the notes. Nobody in the history of presentations complained that slides were too short.

### Step-by-step: fix a dense slide

1. Take a slide with a paragraph of text in the body placeholder. Select the paragraph text.
2. Cut it to the notes: open the **Notes pane** and paste it there (**Ctrl + X**, click notes, **Ctrl + V**).
3. Rewrite what remains as at most 6 phrase bullets. Delete every word that is not load-bearing (adverbs, "that", "in order to", hedges).
4. Convert one bullet into evidence: **Insert > Chart > Column**, use a tiny 2-series table like `Region: EMEA 114, APAC 87` to replace a bullet "EMEA 114 vs APAC 87".
5. Read the slide aloud in 10 seconds. If you cannot, cut again.

### Real-world examples

- **Business:** An executive summary slide: claim title "Pipeline coverage is 3.2x, healthy for Q4", then 4 bullets of 4-5 words each. The detail lives in the appendix.
- **Education:** Key vocabulary as 6 one-word bullets; the definitions go in speaker notes and the class handout.
- **Personal:** A trip recap slide with one photo and the caption "Kyoto, day 3: rain and ramen". Zero bullets.

### Try it now

Write the worst possible slide: 12 bullets, 15 words each, about anything. Then fix it to the 6x6 standard and move the rest into notes. Bonus: make the third bullet a chart instead. Keep both versions; the contrast is the lesson.

---

## 8. Sections for Organizing Decks

### Explanation

**Sections** are collapsible groups of slides in the Thumbnails pane, named like chapter headings. Once a deck passes ~15 slides, sections stop you from losing your place and make reordering a whole chapter one drag instead of 10.

Sections can be collapsed/expanded, renamed, moved as a block, and section names appear in **Slide Sorter**, in **Presenter View** (as the section of the current slide), and can be printed as a table of contents via **File > Print > Print All Slides > Print Sections**-style options or the **Slides from Outline** handout approaches.

### Step-by-step: create and use sections

1. In the **Thumbnails pane**, right-click above the slide where a new chapter should start (e.g. before slide 5).
2. Click **Add Section**.
3. Right-click the section header (**Untitled Section**) > **Rename Section**, type `Part 1 - Context`, click **Rename**.
4. Repeat at each chapter boundary: `Part 2 - Findings`, `Part 3 - Ask`, `Appendix`.
5. Click the small triangle beside a section name to collapse/expand it.
6. To move a chapter: drag the **section name** (not an individual slide) up or down. Every slide inside moves together.
7. To remove grouping: right-click > **Remove Section** (slides stay) or **Remove Section & Slides** (both go).

### Step-by-step: print or jump by section

1. Open **Slide Show > Custom Slide Show > Custom Shows...** and create a custom show from one section's slides for a shortened version of the talk (e.g. `Board version - 12 slides`).
2. During the show, right-click the screen > **Custom Show** to switch versions live.

### Real-world examples

- **Business:** `Agenda`, `Company`, `Market`, `Product`, `Traction`, `Financials`, `Team`, `Appendix`. The appendix section is hidden from the main show and used only for Q&A.
- **Education:** One section per lecture week inside a single course master deck; export each week as its own file via **File > Save As**.
- **Personal:** `Ceremony`, `Speeches`, `Dinner`, `Dancing` for an event slideshow, so the AV volunteer can jump to the right chapter.

### Try it now

Open your `Try01-MyFirstDeck` and add 3 sections: `Opening`, `Body`, `Closing`. Collapse `Body`, drag `Closing` above `Body`, expand all. Then create a Custom Show called `Short` containing only `Opening` and `Closing`, and run it with **F5** (advance with **Space**, quit with **Esc**).

---

## 9. Slide Size: 16:9 vs 4:3

### Explanation

**Slide size** is the canvas dimension. Get this right before you design slide 2.

- **Widescreen 16:9** (13.333 x 7.5 in / 33.867 x 19.05 cm; default since PowerPoint 2013): for modern projectors, monitors, TVs, webinars, video export. Use this unless you know otherwise.
- **Standard 4:3** (10 x 7.5 in / 25.4 x 19.05 cm): legacy projectors and some older conference-room displays; still requested at some venues and universities.

Changing size **after** building slides forces PowerPoint to scale content (**Maximize** = fill, may crop/crowd) or **Ensure Fit** = fit everything, leaving white bands). Both produce imperfect results, so decide first. For a printed poster or a giant screen, you can also set a **Custom Slide Size** (Design > Slide Size > Custom Slide Size with exact inches and orientation).

### Step-by-step: set slide size before designing

1. Open a new presentation (do this first, before content).
2. **Design** tab > **Slide Size** (far right group).
3. Choose **Widescreen (16:9)** or **Standard (4:3)**.
4. If the deck already has slides, PowerPoint asks: **Maximize** (content fills, may clip) or **Ensure Fit** (content shrinks to fit). Choose **Ensure Fit** for text-heavy decks, **Maximize** for image-heavy ones.
5. For custom sizes: **Design > Slide Size > Custom Slide Size...**, set width/height/orientation, click **OK**.

### Step-by-step: check what the venue needs

1. Email the venue or AV contact: "What resolution does the projector run, 16:9 or 4:3?"
2. If unknown, design 16:9 and export a PDF as a safety copy (section 10) plus bring the .pptx on a USB drive.

### Real-world examples

- **Business:** A 16:9 deck for the webinar, then **Design > Slide Size > Standard (4:3) > Ensure Fit** and save a second file `...-4x3-version.pptx` for the client's ancient boardroom projector.
- **Education:** Some lecture halls still run 4:3 at 1024x768. Check once per semester and set the course template accordingly.
- **Personal:** A TV photo slideshow at home: 16:9 with images sized to the slide so no black bars appear.

### Try it now

Create 3 slides of content in 16:9, then switch to 4:3 choosing **Ensure Fit**. Undo (**Ctrl + Z**) and switch again choosing **Maximize**. Compare the two results and note which one you would keep. Then switch back to 16:9.

---

## 10. File Formats: .pptx, .ppt, .potx, .ppsx, .pptm, and PDF Export

### Explanation

Every PowerPoint format is a different promise about compatibility and behavior. The full save list lives in **File > Save As > Save as type**.

| Extension | What it is | When to use |
|---|---|---|
| **.pptx** | Standard presentation (XML, zip-based, no macros). Default since 2007. | Always, for working decks. |
| **.ppt** | Legacy binary format (PowerPoint 97-2003). | Only when someone with ancient PowerPoint must edit the file. Loses modern features. |
| **.potx** | Template: opens as a reusable starting point that creates new untitled presentations. | Company/brand/course templates so every new deck starts correct. |
| **.ppsx** | Show file: opens straight into Slide Show, not editing view. | Sending finished decks to viewers who should just watch. |
| **.pptm** | Macro-enabled presentation (can contain VBA). | Only when you actually ship macros; many corporate mail filters block it. |
| **.pdf** | Portable Document Format export (via **File > Export > Create PDF/XPS Document** or **Save As > PDF**). | Distribution to readers, printing, upload to portals where fidelity matters and editing must not. |
| **.ppsxm / .potm** | Macro-enabled show/template variants. | Rare; same caveats as .pptm. |
| **.gif/.png/.jpg/.mp4** | Image/video export (**File > Export > Create a Video / Save as Picture**). | Social posts, websites, self-running kiosks (covered in later modules). |

Key behavior notes:

- Saving as .ppt shows a **Compatibility Checker** warning you which effects will be lost (newer transitions, morph, some media).
- **File > Info > Check for Issues > Inspect Document** removes comments, hidden metadata, and personal info before you share outside the company.
- PowerPoint can **open** old .ppt and even some .pps files and convert them (**File > Info > Convert**) to .pptx.

### Step-by-step: save in each important format

1. **File > Save As > Browse**, pick a folder such as `C:\Users\jdoe\Documents\Decks\2026-09\`.
2. File name: `2026-09-22-Board-Update-YourCompany`. **Save as type:** `PowerPoint Presentation (*.pptx)` > **Save**.
3. Template: **Save as type:** `PowerPoint Template (*.potx)`. PowerPoint offers the **Custom Office Templates** folder; save there and it appears under **File > New > Personal/Custom**.
4. Show file: **Save as type:** `PowerPoint Show (*.ppsx)`. Double-clicking it starts the show immediately.
5. PDF: **File > Export > Create PDF/XPS Document > Create PDF/XPS**, name it, then in **Options...** choose **Slides** or **Notes pages** (for handouts with notes), click **Publish**.

### Real-world examples

- **Business:** Send the client a `.ppsx` for the read-only review, the final signed-off deck as `.pdf`, and keep the master as `.pptx`. Archive the `.potx` brand template for the team.
- **Education:** Publish each lecture as `.pdf` to the course portal so students on any device can read it; keep the `.pptx` for editing.
- **Personal:** A `.ppsx` photo slideshow emailed to relatives ("double-click to watch"), with a `.pdf` fallback for the ones whose ancient PC chokes.

### Try it now

Take `Try01-MyFirstDeck` and save it 4 times: as `.pptx`, as `.potx` (Custom Office Templates), as `.ppsx`, and export a `.pdf`. Close everything, then double-click the `.ppsx` from File Explorer and confirm it launches straight into the slide show (**Esc** to exit). Open the PDF and confirm the slides render as expected.

---

## 11. Saving, AutoSave, OneDrive, and Undo/Redo

### Explanation

**Saving** protects work; **AutoSave** in Microsoft 365 protects it continuously, but only for files stored in **OneDrive**, **OneDrive for Business**, or **SharePoint**. The AutoSave toggle sits at the top-left of the title bar. When it says **On**, changes are saved every few seconds and version history is recorded; when **Off**, you are back to manual **Ctrl + S** discipline.

**Undo/Redo:** **Ctrl + Z** undoes the last action, repeatedly, up to a large but finite history (100+ actions in modern versions; do not rely on it as storage). **Ctrl + Y** (or **Ctrl + Shift + Z** in some configurations) redoes. The QAT dropdown beside Undo shows the full list of reversible steps, and clicking a step undoes everything up to it. Some actions (Save, macro actions) cannot be undone.

**Version history:** for OneDrive/SharePoint files, **File > Info > Version History** (or click the file-name link at the top of the window) restores any earlier state. This is your safety net.

Habits that prevent disaster:

1. Save the first time within 30 seconds of creating a file.
2. **Ctrl + S** becomes a tic after every meaningful change when AutoSave is off.
3. Keep masters on OneDrive/SharePoint so AutoSave and Version History work.
4. Before big edits, make a snapshot copy: **File > Save a Copy** named `...-backup-2026-09-22.pptx`.
5. 30 minutes before presenting, stop editing structure and rehearse instead.

### Step-by-step: turn on AutoSave and find version history

1. Open a presentation stored on OneDrive (check the title bar path; if it says "Saved to this PC", move it: **File > Save As > OneDrive - YourCompany Inc**).
2. Click the **AutoSave** toggle at the top-left and set it to **On**. The label changes to "Saving..." then "Saved".
3. Make an edit, wait 2 seconds, and confirm the title bar reads **Saved**.
4. To see older versions: click the **file name** in the title bar (or **File > Info > Version History**), pick a timestamp, and choose **Restore** or **Open** a copy.
5. On the web, open the file in PowerPoint for the web and use **File > Version History** there if the desktop app is unavailable.

### Step-by-step: recover after a crash

1. Reopen PowerPoint. The **Document Recovery** pane appears on the left with recovered files and timestamps.
2. Click each entry to preview, then **Save As** the good one immediately.
3. If the pane does not appear: **File > Info > Manage Presentation > Recover Unsaved Presentations** and look in the UnsavedFiles folder.

### Real-world examples

- **Business:** A colleague's laptop died mid-edit 10 minutes before the board call. Because the deck lived on SharePoint with AutoSave on, opening it on another machine showed every change up to the crash.
- **Education:** A teacher reverts a mangled lecture deck to yesterday's version via Version History after a bad bulk edit.
- **Personal:** Restore the pre-"helpful cousin edited it" version of a wedding slideshow from Version History.

### Try it now

Move `Try01-MyFirstDeck` to OneDrive (or any SharePoint folder) and switch **AutoSave** on. Type a word, watch the status change to **Saved** without pressing anything. Make 5 different edits, then open **Version History** and count the captured versions. Finally, delete a slide on purpose and undo it with **Ctrl + Z** twice (delete, then undo), then redo it with **Ctrl + Y** and undo once more to leave the deck intact.

---

## 12. Essential Keyboard Shortcuts

### Explanation

Shortcuts are how experienced PowerPoint users look fast. Learn these in three tiers; drill until tier 1 is automatic this week.

**Tier 1 - daily survival (learn today):**

| Shortcut | Action |
|---|---|
| **Ctrl + N** | New presentation |
| **Ctrl + O** | Open |
| **Ctrl + S** | Save |
| **Ctrl + Z / Ctrl + Y** | Undo / Redo |
| **Ctrl + M** | New slide |
| **Ctrl + D** | Duplicate selected slide(s) or object(s) |
| **Ctrl + C / X / V** | Copy / Cut / Paste |
| **Ctrl + K** | Insert hyperlink |
| **Ctrl + A** | Select all (slide objects or outline text) |
| **Tab / Shift + Tab** | Select next / previous object on a slide |
| **Esc** | Cancel, or exit slide show |

**Tier 2 - structuring (learn this week):**

| Shortcut | Action |
|---|---|
| **F5 / Shift + F5** | Slide show from beginning / from current slide |
| **Ctrl + Shift + C / V** | Copy / paste formatting only |
| **Tab / Shift + Tab** (in a placeholder) | Demote / promote bullet level |
| **Ctrl + L / E / R / J** | Align text left / center / right / justify |
| **Ctrl + B / I / U** | Bold / italic / underline |
| **Alt + Shift + Left/Right** (in outline) | Promote / demote outline paragraph |
| **Ctrl + Enter** | Insert a new slide (in some contexts) |
| **F2** | Edit text of selected text object |

**Tier 3 - presenting (learn before your first talk):**

| Shortcut | Action |
|---|---|
| **N, Space, Right, Down, Page Down** | Next slide or animation |
| **P, Left, Up, Page Up** | Previous |
| **B / W** | Black screen / white screen (press again to return) |
| **E** | Erase on-screen annotations |
| **Ctrl + P / Ctrl + I / Ctrl + A** | Pen / laser pointer / arrow during show |
| **Ctrl + L** (during show) | Laser pointer (older builds) |
| **Number + Enter** | Jump to slide 7: type `7`, press **Enter** |
| **S** | Stop/restart automatic show |
| **Esc** | End the show |
| **Alt + F5** | Start Presenter View preview on one monitor |
| **Ctrl + F1** | Collapse / expand the ribbon |
| **F4 / Ctrl + Shift + G** | Repeat last action / group objects (grouping is **Ctrl + G**) |

Tip: open a full printable list any time via **File > Options > Customize Ribbon > Customize... (keyboard shortcuts)** dialog, or press **F1** in PowerPoint and search "keyboard shortcuts".

### Step-by-step: build a slide using only shortcuts

1. **Ctrl + N**, then **Ctrl + S**, name it `shortcut-drill.pptx`.
2. Type a title (the title placeholder is focused by default).
3. **Ctrl + M** for a new slide, type a title, press **Tab**, type 3 bullets.
4. Press **Ctrl + F1** to hide the ribbon and keep working for 2 minutes with only shortcuts and right-click menus.
5. **F5** to present, **Space** to advance, **B** to blank the screen, **B** again, **Esc**.

### Real-world examples

- **Business:** Building a 20-slide skeleton takes 4 minutes with **Ctrl + M** + **Tab**/typing, versus 15 with mouse-only.
- **Education:** **B** during class to blank the screen and force discussion is the teacher's best trick.
- **Personal:** **Ctrl + D** to duplicate a photo slide 15 times, then only swap images.

### Try it now

The "90-second rebuild": create a slide with a title and 4 bullets using only shortcuts from tier 1 and 2 (no ribbon clicks), then run it with **F5** and blank the screen once. Repeat tomorrow without looking at the table.

---

## Hands-On Practice Projects

Complete all five. Each builds a real file you will keep in your portfolio folder.

### Project 1: About Me deck (interface + slides + save)

**Build:** A 5-slide personal introduction: Title Slide, "What I do", "What I am learning", "A picture that matters", "How to reach me" (use fake details: `jdoe@acme.com`). Use sections `Intro` and `Contact`. Save as .pptx on OneDrive with AutoSave on, and export a .pdf.

**Success criteria:**
- All 5 slides use layout placeholders (no pasted text boxes for body content).
- 2 named sections visible in the Thumbnails pane.
- Theme change via **Design** tab restyles every slide consistently.
- Both `AboutMe-jdoe.pptx` and `AboutMe-jdoe.pdf` exist and open correctly.

### Project 2: Outline-first business update (outline view + bullet discipline)

**Build:** A 6-slide "Monthly Update - YourCompany Inc" written first in Outline View only: claim-style titles, max 6 bullets per slide, max 6 words per bullet. At least one bullet must become a chart placeholder (Insert > Chart > Column with fake numbers like `EMEA 114, APAC 87, AMER 63`). Sections: `Highlights`, `Metrics`, `Next`.

**Success criteria:**
- Deck drafted in under 10 minutes in Outline View (time yourself).
- Zero slides exceed the 6x6 rule; all body text is phrase-level (no sentences, no periods).
- At least one slide replaces a would-be bullet with a chart or table.
- Speaker notes on every slide contain the "detail" that was cut.

### Project 3: Format round-trip (file formats)

**Build:** From Project 2, produce: a `.potx` brand template saved to Custom Office Templates, a `.ppsx` show version for distribution, a `.pdf`, and a copy saved as legacy `.ppt` with the Compatibility Checker reviewed (note which features warned).

**Success criteria:**
- Creating a new presentation from **File > New > Custom > [your template]** produces an untitled deck with your sections/theme.
- Double-clicking the `.ppsx` starts the slide show immediately.
- The PDF opens on another viewer (browser) and matches slide order and text.
- You can list, in writing, at least 2 features the .ppt compatibility check warned about.

### Project 4: The venue problem (slide size + layouts)

**Build:** Take Project 2 and produce two versions: 16:9 for the webinar and 4:3 (`Ensure Fit`) for "the client's old boardroom projector". Fix any layout damage in the 4:3 version (text overflow, cropped pictures). Save as `...-16x9.pptx` and `...-4x3.pptx`.

**Success criteria:**
- Both files exist with correct dimensions (**Design > Slide Size** shows 13.333 x 7.5 in and 10 x 7.5 in).
- Zero overflow warnings in 4:3 (no text spilling out of placeholders, no scroll bars in placeholders).
- **Home > Reset** used at least once to restore placeholder positions.
- A short note (3 bullet points) on what changed between versions.

### Project 5: The 3-minute talk (views + presenter view + shortcuts + recovery)

**Build:** A 5-slide, 3-minute talk on any hobby or topic. Prepare with Slide Sorter for final ordering, Notes Page for cue cards, rehearse with Reading View, deliver with **F5** and Presenter View (**Alt + F5** on one monitor). Include one black-screen moment (**B**) for a question. Save a backup copy with **File > Save a Copy** before rehearsing.

**Success criteria:**
- Talk delivered within 3:00 (timer visible in Presenter View).
- Presenter View used for notes and next-slide preview at least once.
- At least one jump-to-slide during Q&A (type a number + **Enter**).
- Deck built and edited using tier-1 shortcuts with the ribbon collapsed (**Ctrl + F1**) for at least 2 minutes.
- Crash drill performed once: kill PowerPoint from Task Manager, reopen, and recover via the **Document Recovery** pane or **Manage Presentation > Recover Unsaved Presentations**.

---

## Common Mistakes and Pitfalls

| Mistake | Why it hurts | Fix |
|---|---|---|
| Typing body content into pasted text boxes instead of placeholders | Breaks outline view, breaks theme changes, inconsistent positions | Use **Home > Layout** and type into placeholders; text boxes only for labels/callouts |
| Starting design before checking slide size | Late conversion crops images and breaks layouts (**Maximize** vs **Ensure Fit** damage) | Set **Design > Slide Size** on slide 1 |
| Wall-of-text slides ("document syndrome") | Audience reads instead of listens; speaker becomes redundant | 6x6 rule; move detail to notes; one idea per slide |
| Topic titles instead of claim titles | Audience must guess the point | Titles state the takeaway ("Churn fell to 2.1%") |
| Saving only to Desktop with AutoSave off | Crash = lost work, no version history | Store on OneDrive/SharePoint, AutoSave **On**, **Ctrl + S** tic elsewhere |
| Sending .pptx to viewers who only need to read | Formatting drift across machines, accidental edits | Distribute **.pdf** or **.ppsx** |
| Saving as legacy .ppt "just in case" | Loses modern transitions/effects silently (Compatibility Checker) | Keep .pptx masters; export .ppt only on request |
| Over-nesting bullets to level 3+ | Slide looks like an indented novel | Max 2 levels; split the slide |
| Ignoring contextual tabs ("the tab disappeared") | Beginners think the app is broken | Select the object; contextual tab returns (e.g. **Shape Format**) |
| Dragging placeholders around instead of fixing the layout | Every future slide inherits the mess | Fix via **View > Slide Master** (module 02); **Home > Reset** per slide |
| Presenting in Duplicate display mode | Presenter View never appears | Windows display mode **Extend**, then **Slide Show > Use Presenter View** |
| Editing till the last minute before a talk | Broken fonts on the presenter PC, no rehearsal | Freeze content 30 minutes prior; bring .pptx + .pdf on USB |
| Using bullets for quotes, processes, or numbers | Wasted visual potential | Statement slide, diagram/SmartArt, or chart/table instead |
| Not naming sections in long decks | Reordering and Q&A navigation become painful | **Add Section** at every chapter boundary |
| Relying on Undo as file storage | History is finite and lost on close | Save copies (**File > Save a Copy**) before risky edits |

---

## Key Takeaways

1. PowerPoint is for spoken, visual persuasion. If nobody will talk over it, use Word or PDF.
2. The interface is five zones: Ribbon (tabs and groups), Quick Access Toolbar, Thumbnails pane, slide canvas + notes, and the status bar. Learn them by name so instructions make sense.
3. Use the right view for the job: **Normal** to edit, **Slide Sorter** to reorganize, **Notes Page** for cue cards, **Reading View** for quick self-checks, **Slide Show + Presenter View** to deliver.
4. Slides come from **layouts** and **placeholders**, not from pasted text boxes. Placeholders follow the theme and feed the outline; text boxes do neither.
5. **Outline View** is the fastest way to draft a full deck structure at typing speed. Structure first, design second.
6. Bullet discipline: 6x6 as a checklist, phrases not sentences, and never bullets for quotes, processes, or numbers.
7. **Sections** turn a 40-slide deck into 5 movable chapters and make custom shows and Q&A navigation trivial.
8. Set slide size (16:9 default, 4:3 for legacy venues) before designing slide 2. Changing it later always costs quality.
9. Know your formats: `.pptx` to work, `.potx` to template, `.ppsx` to show, `.pdf` to distribute, `.ppt` only under duress, `.pptm` only with macros.
10. AutoSave works only on OneDrive/SharePoint. Keep masters there and use **Version History** as your safety net; **Ctrl + Z** is for seconds, not hours.
11. Shortcuts compound: tier 1 today, tier 2 this week, tier 3 before your first talk. Build one full slide with the ribbon collapsed to prove it.

---

## Further Learning

All links below point to official Microsoft documentation for PowerPoint and Microsoft 365.

1. PowerPoint help and learning hub (start here for any feature lookup): https://support.microsoft.com/en-us/powerpoint
2. Microsoft PowerPoint product overview and feature tour: https://www.microsoft.com/en-us/microsoft-365/powerpoint
3. Microsoft 365 Training center (free PowerPoint video courses, beginner to advanced): https://learn.microsoft.com/en-us/training/
4. Microsoft Create: free PowerPoint templates and design inspiration: https://create.microsoft.com/
5. Microsoft 365 documentation home (covers PowerPoint alongside Word/Excel, including OneDrive save behavior): https://learn.microsoft.com/en-us/microsoft-365/
6. OneDrive documentation (where AutoSave and Version History actually live): https://learn.microsoft.com/en-us/onedrive/
7. Microsoft 365 support home (troubleshooting, recovery, and subscription help): https://support.microsoft.com/en-us/microsoft-365
8. Office training and tutorials portal (guided paths for PowerPoint fundamentals): https://learn.microsoft.com/en-us/training/
9. Microsoft Create: presentation design guides and slide inspiration: https://create.microsoft.com/
10. Microsoft 365 roadmap (what is coming to PowerPoint, including AI features): https://www.microsoft.com/en-us/microsoft-365/roadmap

*Note on sources: search engines were unreachable from the authoring environment at write time, so this list is limited to stable, official Microsoft hub and documentation entry points rather than deep article links. Always navigate from these hubs to the latest article for your exact PowerPoint version, since article locations move between releases.*

---

*End of Module 01. Next: Module 02 - Design and Visual Communication.*


## FILE: 02-Design-Foundations/02-design-foundations.md

# Module 02: Design Foundations

> **Module number:** 02
> **Title:** Design Foundations
> **Level:** Beginner+
> **Prerequisites:** Module 01 (Getting Started with PowerPoint) - you should know the ribbon, the slide thumbnails pane, Normal view vs Slide Sorter view, and how to create and save a basic presentation.
> **Estimated study time:** 2.5 to 3 hours (including hands-on practice projects)
> **Next module:** Module 03 (Working with Text and Content)

---

Welcome to the module that separates amateur decks from professional ones. Everything you will learn here happens "behind the slides": the theme layer, the master layer, the layout layer, and the template file format that packages them all for reuse. A presenter who understands design foundations can make 50 slides look identical in minutes, rebuild a company's brand in PowerPoint in under an hour, and stop fighting with fonts that keep reverting to Calibri. That is exactly what you will be able to do by the end of this module.

Throughout the module we use one fictional company, **YourCompany Inc**, a small logistics software business with brand colors Navy `#1F3864`, Teal `#2E9BA6`, and Sand `#EDE6D6`, plus the fonts Georgia (headings) and Calibri (body). Swap in your own organization's details as you practice.

---

## 2.1 Why Design Foundations Matter: The Consistency Principle

**Explanation.** A presentation is read as one object, slide after slide. Audiences judge credibility partly on visual consistency: every title in the same place, the same font sizes, the same two or three colors, the same footer treatment. The single biggest reason decks look amateur is that formatting is applied slide by slide (manual formatting) instead of at the design layer (automatic formatting). PowerPoint solves this with a stack of reusable layers: theme, slide master, slide layouts, and templates. Format once at the top of the stack, and it flows to every current and future slide.

The consistency principle has four practical rules:

1. **Format at the highest layer possible.** If a font, color, logo, or footer belongs on every slide, it belongs in the master, not on the slide.
2. **Use layouts instead of manual boxes.** A Title and Content slide should come from the "Title and Content" layout, not from hand-built text boxes.
3. **Limit your palette and type scale.** Two to four theme colors, two fonts (one heading, one body), and three to four font sizes cover 95% of decks.
4. **Reset first, style second.** When a slide drifts out of shape, use Home > Reset before reformatting by hand.

Real-world examples: in business, a quarterly review deck of 60 slides from five contributors only holds together because everyone starts from the same corporate template. In education, a teacher's 40-slide course deck stays legible because every definition slide uses the same layout. In personal use, a wedding slideshow or travel recap feels intentional when the same photo-corner style and caption font repeat throughout.

**Try it now.** Open any deck you made recently and play "spot the inconsistency" for two minutes: count the distinct title positions, fonts, and accent colors. List the top three offenders. You will fix these exact problems by the end of this module.

---

## 2.2 Themes and Theme Variants

**Explanation.** A **theme** is a coordinated design package: a color set (12 colors: 4 text/background pairs, 6 accents, 2 hyperlinks), a font set (heading font + body font), and a set of shape effects (shadows, glows, bevels). Every new blank presentation already has a theme (the default "Office" theme). Themes control the *look*; masters and layouts (covered later) control the *structure*.

**Theme variants** are the lighter swatches shown to the right of each theme gallery entry on the Design tab. Each theme ships with up to four variants that keep the same layout logic but adjust the palette or font treatment. Variants are the fastest way to reskin a deck: same content, different mood.

**Applying and switching themes:**

1. Click the **Design** tab.
2. In the **Themes** gallery, hover to live-preview each theme on your slides (PowerPoint previews on the real slides as you hover).
3. Click a theme to apply it to the entire presentation.
4. To the right of the gallery, open the **Variants** group and click a variant swatch to restyle within the theme.
5. If the Themes gallery is too small, click the **More** arrow (bottom-right of the gallery) to expand the full gallery including "This Presentation", "From Office.com", and "Browse for Themes".

**Switching themes mid-work:** simply click another theme. Because colors and fonts are defined at theme level, all objects using theme colors (more in the next section) update automatically. This is the entire point: switch from "Facet" to "Integral" and your charts, shapes, and titles reskin in one click.

**Multiple themes in one presentation** are supported: select slides in the Slide Sorter or thumbnail pane, right-click a theme or variant in the Design gallery, and choose **Apply to Selected Slides**. PowerPoint adds a second slide master behind the scenes (each master carries its own theme).

Real-world examples: a business pitch team drafts in a neutral theme during writing, then switches to the brand theme at polish time. A teacher gives the "history unit" a parchment-feeling theme and the "science unit" a bright variant of the same base theme. A personal resume deck uses a dark variant for the cover section and a light variant for content sections.

**Try it now.** Make five throwaway slides, apply the "Facet" theme, then click three different variants and watch the thumbnails. Now right-click a different theme and choose **Apply to Selected Slides** on just two of them. Open View > Slide Master and notice the two masters in the left pane. Undo everything afterwards.

---

## 2.3 Fonts and Colors as Theme Components

**Explanation.** Theme colors and theme fonts are *named slots*, not fixed values. When text is formatted with "Theme Color: Text/Background 1" or "Theme Font: Heading", its actual appearance is a lookup into the current theme. This is why professional decks change appearance instantly when themes change, while amateur decks (whose colors were hard-picked from the standard colors row) do not.

**The 12 theme color slots:**

- **Text/Background 1-4**: four dark/light pairs designed to always contrast. Slide backgrounds and body text come from these.
- **Accent 1-6**: your brand and chart colors. Accent 1 is the default fill for new shapes and chart series 1.
- **Hyperlink** and **Followed Hyperlink**: link colors.

**Theme fonts:** exactly two slots, Heading and Body. Each maps to a major (heading) and minor (body) font, and Office applies Heading to titles and Body to everything else automatically.

**Using theme colors deliberately:**

1. Select a shape or text.
2. On the mini-toolbar or the **Shape Format / Home** tab, open the **Font Color** or **Shape Fill** dropdown.
3. In the top row (**Theme Colors**), hover to preview and pick a slot. The bottom row (**Standard Colors**) and "More Colors" are *fixed* colors: they will never change with the theme. Avoid them for anything that repeats.

**Customizing the theme's color set:**

1. **Design** tab > **Variants** group > **More** arrow > **Colors** > **Customize Colors**.
2. In the "Create New Theme Colors" dialog, click each color slot and set the exact brand values (for YourCompany Inc: Accent 1 = Navy `#1F3864`, Accent 2 = Teal `#2E9BA6`, Text/Background 2 = Sand `#EDE6D6`).
3. Name the set "YourCompany Brand" and click **Save**. Every theme-color object in the deck updates at once.

**Customizing theme fonts:**

1. **Design** tab > **Variants** > **More** arrow > **Fonts** > **Customize Fonts**.
2. Set Heading font = Georgia, Body font = Calibri, name it "YourCompany Fonts", click **Save**.

Real-world examples: a business rebrand from navy to teal is one Colors dialog change across every deck built on the template. A school sets one "High Contrast" color set for projector-heavy lecture halls. A personal photo book deck switches theme fonts from playful to formal for printing.

**Try it now.** Create a slide with a title, a bullet list, one rounded rectangle filled with Accent 1, and a chart. Now change the theme color set to your own three hex values as above. Every one of those objects should recolor together. If any object does not change, it was formatted with a fixed color: select it and move it to the matching theme slot.

---

## 2.4 The Hierarchy: Slide Masters vs Slide Layouts

**Explanation.** This is the mental model the whole module hangs on:

```
Presentation
└── Slide Master (1 per theme; carries the theme)
    ├── Layout: Title Slide
    ├── Layout: Title and Content
    ├── Layout: Section Header
    ├── Layout: Two Content
    ├── Layout: Comparison
    ├── Layout: Title Only
    ├── Layout: Blank
    └── ... (more layouts, up to any number)
        └── Actual Slides (each slide is an instance of ONE layout)
```

- The **slide master** is the top-level design sheet: the theme, the background treatment, the logo/watermark, the footer strip, and the master title and body text styles (which define title/body font, size, color, and bullet styles for everything beneath it).
- **Slide layouts** are children of the master. Each layout arranges placeholders differently (title plus one content area, title plus two, comparison columns, etc.) and can override master-level choices (for example a "Title Slide" layout with a full-bleed image background while the master stays white).
- **Slides** are instances of a layout. Slide-level formatting overrides layout, layout overrides master, master holds the theme.

Rule of thumb: **design choice belongs at the highest level that is still true everywhere it applies.** Logo and footer: master. "Every section divider should look like X": one layout. "This one slide needs bigger text": slide level.

Also note: each slide master represents one theme. Multiple masters (View > Slide Master > Insert Slide Master) mean multiple themes in one file.

Real-world examples: business templates ship with 8-12 custom layouts ("Agenda", "KPI Dashboard", "Team Bio", "Quote") so authors never build structure by hand. In education, a "Definition" layout and a "Worked Example" layout let a professor build a consistent lecture. A personal portfolio uses a "Photo + Caption" layout throughout.

**Try it now.** Open View > Slide Master and draw (on paper or in notes) the hierarchy of your own most-used deck type: what belongs on the master (list 3 things) and what deserves its own layout (list 3 layouts). This sketch becomes the spec for Project 1 at the end of the module.

---

## 2.5 Editing the Slide Master: Backgrounds, Logos, Footers, Slide Numbers

**Explanation.** Slide Master view is the workshop where the design layer is edited. Anything you place on the master itself (the top, largest thumbnail) appears on every slide that uses that master, and it is unselectable in Normal view - which is exactly what you want for a logo or footer.

**Entering and leaving Slide Master view:**

1. **View** tab > **Slide Master**. The ribbon switches to the **Slide Master** tab and the left pane shows the master at top with its layouts beneath.
2. Click the master thumbnail (the big one at the top) to edit master-wide elements; click a layout thumbnail to edit just that layout.
3. When done, click **Slide Master** tab > **Close Master View** (rightmost button).

**Adding a logo or watermark to every slide:**

1. In Slide Master view, select the master thumbnail.
2. **Insert** > **Pictures** > **This Device** (or **Stock Images**), pick the YourCompany Inc logo file, click **Insert**.
3. With the picture selected, use **Picture Format** > **Align** > **Align Right** and **Align Bottom** (turn on "Align to Slide"), then drag slightly up/left to leave a 0.3 inch margin.
4. Send it behind content: **Picture Format** > **Send Backward** (or place it in a spot where no placeholder overlaps).
5. For a full-size watermark effect (like "DRAFT"), stretch the image behind everything, then use **Picture Format** > **Transparency** to fade it to about 80-90%.
6. **Close Master View**. The logo now appears on every slide using that master and cannot be clicked or moved in Normal view.

**Footers and slide numbers (master-level placement):**

1. In Slide Master view, on the master thumbnail, note the three footer placeholders along the bottom: **Footer**, **Date**, **Slide Number**. If they are missing or hidden: **Slide Master** tab > **Master Layout**, then tick **Footers** and click **OK**.
2. Reposition and style these placeholders once (for example, slide number bottom-right in 10pt italic gray, footer text bottom-left with "YourCompany Inc - Confidential").
3. To actually *populate* them for the presentation, exit master view, then **Insert** > **Header & Footer** (or **Insert** > **Slide Number**).
4. In the Header and Footer dialog, tick **Slide number**, **Footer** (type the text), and optionally **Date and time**. Choose "Don't show on title slide" if desired, then click **Apply to All**.
5. Verify on a couple of slides. The text and numbering come from the dialog; the *position and style* come from the master.

**Master background styling** (solid, gradient, picture, textured) is covered in section 2.7; the key point is to set it on the master or a layout via **Slide Master** tab > **Background Styles** > **Format Background**, so every slide inherits it.

**Editing master text styles:** on the master thumbnail, click into the "Click to edit Master title style" placeholder and set the title font, size, and color (for YourCompany Inc: Georgia 40pt, Navy, left-aligned). Then set the five levels of "Master text styles" (Calibri 24/20/18/16/14 with decreasing indentation). Every title and body placeholder in the deck inherits these unless a layout or slide overrides them.

Real-world examples: a business places its logo plus "Confidential - Q3 FY Review" footer on the master so no one can forget either. A teacher puts the course code and lecture number in the footer with slide numbers so students can cite slides in questions. A personal portfolio puts a small monogram and page numbers on every slide for a printed leave-behind.

**Try it now.** On a scratch presentation, add a text-box "watermark" (the word CONFIDENTIAL at 96pt, 90% transparency) plus a slide number to the master. Close master view, add five slides, and confirm: the watermark is unselectable and the number appears and increments automatically.

---

## 2.6 Placeholders in Masters and Layouts

**Explanation.** A **placeholder** is a reserved container defined on a master or layout that authors fill with content on real slides. Placeholders are why text snaps into position, why fonts inherit from theme styles, and why "Reset" can fix a mangled slide. The placeholder types PowerPoint understands:

- **Title** and **Text** (body/outline text with multi-level bullets)
- **Content** (a 6-in-1 placeholder offering table, chart, SmartArt, picture, online picture, or video)
- **Picture**, **Chart**, **Table**, **SmartArt**, **Media**, **Online Image**
- **Vertical Title** / **Vertical Text** (for East Asian or poster-style layouts)
- **Footer**, **Date**, **Slide Number** (bottom strip placeholders)

**What belongs on the master vs a layout:** on the master, style the *title placeholder* and the *body text placeholder* (these define the styles all layouts inherit) and the footer strip. On each layout, arrange the placeholders that make that layout unique (for example, "Comparison" needs two content placeholders side by side with two subtitles).

**Editing placeholders in layouts:**

1. **View** > **Slide Master**, click the layout you want to change (say, "Title and Content").
2. To add a placeholder: **Slide Master** tab > **Insert Placeholder** > choose the type (Content, Picture, Text...) and drag out the rectangle on the layout.
3. To move or resize: drag the placeholder border; use **Align** tools on the contextual **Shape Format** tab for exact positioning (for example, all content placeholders 1.0 inch from the left edge).
4. To edit prompt text: click into the placeholder and retype. Custom prompt text like "Type your KPI headline here" guides future authors. (Note: custom prompt text shows only until the author types; it does not print.)
5. To hide a placeholder from slides of this layout: select it and press Delete, or **Slide Master** tab > **Master Layout** / **Hide Background Graphics** for master-level graphics on one layout.

**Re-applying a layout after editing it:** if slides already use the layout and you changed its placeholders, PowerPoint needs a nudge: on the affected slides use **Home** > **Reset** (or right-click the layout in **Home** > **New Slide**'s layout gallery and choose **Reset Layout**). Microsoft documents this "edit and re-apply" step explicitly.

Real-world examples: a business "KPI Dashboard" layout with one chart placeholder and three text placeholders keeps every monthly review identical. A teacher's "Warm-up Question" layout has a title and a single large text placeholder sized for big projector type. A personal "Photo of the Day" layout holds one picture placeholder with a caption text placeholder under it.

**Try it now.** Duplicate the "Title and Content" layout (right-click it in Slide Master view > **Duplicate Layout**), rename it "Big Quote", delete the body placeholder, and add one large centered Text placeholder with the prompt "Type one sentence worth remembering". Close master view, apply the layout via **Home** > **Layout**, and confirm the prompt appears.

---

## 2.7 Background Formatting: Solid, Gradient, Picture, and Pattern Fills

**Explanation.** Backgrounds set the mood and the contrast budget for everything above them. PowerPoint offers four families of background fill plus a transparency control. Format backgrounds at the master or layout level so the choice propagates.

**Opening the background tools:**

- Simple: **Design** tab > **Format Background** (opens the task pane), or right-click any empty slide area > **Format Background**.
- In Slide Master view: **Slide Master** tab > **Background Styles** > **Format Background** (or **Hide Background Graphics** to suppress master graphics on one layout).

**The four fill types (Format Background pane > Fill):**

1. **Solid fill**: pick **Color** (use a Theme Colors slot!), then adjust **Transparency**. Default professional choice: Text/Background Light 1 (white) or a very light theme tint for content slides, and Text/Background Dark 1 (near-black) for title and closing slides.
2. **Gradient fill**: choose a **Type** (Linear, Radial, Rectangular, Path) and **Direction**, then edit the **Gradient stops** (click a stop, set its color and position, drag to reorder). Keep gradients subtle: two stops, same hue, 10-20% lightness difference. Example: a linear top-to-bottom gradient from Navy `#1F3864` to a slightly lighter navy for the YourCompany cover slide.
3. **Picture or texture fill**: click **Insert** (under Picture source) to choose **From a File** (a brand photo or texture), **Stock Images**, or **Online**. Use **Transparency** to push it back (60-80%) so text stays readable, and tick **Rotate with shape** if needed. This is the standard "photo title slide" trick and also how subtle paper/canvas textures are applied.
4. **Pattern fill**: pick a pattern swatch (dots, diagonal lines, bricks) and set **Foreground** and **Background** colors. Patterns are mostly for printed handouts, posters, or deliberately retro styles; they easily look dated in business settings, so use them sparingly.

Then click **Apply to All** (whole presentation, per current master) or just close the pane to affect the selected slide/layout only. In Slide Master view, changes apply to the master or layout you are editing.

Contrast discipline: whatever fill you choose, body text must keep roughly a 4.5:1 contrast ratio. Navy text on Sand is fine; Teal text on Navy is marginal at small sizes; light gray text on white is always a mistake.

Real-world examples: a business closing slide with a subtle brand gradient and white "Thank you / questions" text. A lecture slide with a 15%-transparency campus photo behind the title so slides feel part of an institution. A personal birthday deck with a light pattern fill behind photo captions.

**Try it now.** On one layout in Slide Master view, apply a two-stop gradient; on a second layout, apply a picture fill at 70% transparency. Make two slides using each layout and compare readability with 24pt body text. Whichever loses the contrast test gets its background lightened or darkened until the text passes.

---

## 2.8 Applying Templates to Existing Decks, and Resetting Slides

**Explanation.** Two small but career-saving mechanics: applying a template/design to a deck that already has content, and resetting slides that have drifted.

**Apply a theme or template to an existing presentation:**

1. **Design** tab > expand the **Themes** gallery.
2. Either pick a built-in theme, or choose **Browse for Themes** and select a `.thmx` or `.potx` file from your brand folder.
3. To start a *new* file from a saved template: **File** > **New** > **Personal** (or **Custom** in older builds) > click your template. If the template is a file on disk, right-click the `.potx` and choose **Open** (this creates a new untitled presentation from it), or use **File** > **New from Existing** on some builds.
4. Microsoft also documents **Apply a template to an existing presentation**: in the Design tab's theme gallery use **Browse for Themes** and point at the template file; PowerPoint applies its theme and layouts.

**Reset slides (the undo-drift button):**

1. Click the offending slide (or select several in the thumbnail pane / Slide Sorter).
2. **Home** tab > **Reset** (in the **Slides** group), or right-click the slide thumbnail > **Reset Slide**.
3. What it does: returns all placeholders to the size, position, and style defined by the slide's layout/master, and removes manual slide-level formatting on placeholder text (direct font color changes, manual moves). Non-placeholder objects (free text boxes, inserted pictures) are untouched.
4. If you changed a *layout* after making slides, run **Reset** (or **Reset Slide**) to push the updated layout onto existing slides.

Real-world examples: five colleagues edited one business deck and titles now sit at five different heights; select all, Reset, done. A teacher reuses last semester's lecture and Resets all slides after updating the layout templates. A personal travel deck pasted slides from three old decks; Reset plus the new theme unifies them in seconds.

**Try it now.** Ruin a slide on purpose: drag its title up 2 inches, set one bullet to Comic Sans in red. Then select it and press **Home > Reset**. Confirm the title snaps back and the bullet formatting is gone. Note what Reset does *not* fix (objects you moved that are not placeholders), because that distinction matters.

---

## 2.9 Creating and Saving .potx Templates

**Explanation.** A **PowerPoint template (`.potx`)** is the deliverable of everything above: a file that stores the theme, slide master, custom layouts, placeholder prompts, backgrounds, and prebuilt example slides. Opening a `.potx` spawns a new `.pptx`-based presentation, so the template can never be accidentally overwritten by content authors. That property is what makes templates the correct distribution format for brand systems.

**Build and save a template:**

1. Start from a clean presentation (**File** > **New** > **Blank Presentation**), or from your best existing deck with the content deleted.
2. Open **View** > **Slide Master** and do the design work: theme colors and fonts (section 2.3), master background (2.7), logo and footer (2.5), and the set of layouts with their placeholders (2.6).
3. **Close Master View**. Now add 3-6 **sample slides**, one per custom layout, each filled with realistic dummy text ("Q3 revenue grew 14%..."). Sample slides teach authors what each layout is for and show the design in action. Keep them in the file; authors delete them after copying the layouts they need.
4. Delete any slides you do not want as examples.
5. **File** > **Save As** > choose location > in the **Save as type** dropdown pick **PowerPoint Template (`.potx`)** (use **PowerPoint Template (`.potx`)** not `.potm` macro-enabled unless you have macros).
6. PowerPoint usually jumps to the default Personal/Custom Office Templates folder: save there (name it `YourCompany-Deck-Template-v1.potx`) so it appears under **File** > **New** > **Personal**. To share it, also copy the file to a team SharePoint/OneDrive folder or email it; recipients double-click it (or use **File** > **New** > **Personal** after placing it in their templates folder) to generate fresh decks.
7. Related formats to know: `.thmx` = theme only (colors/fonts/effects), `.potx` = template (theme + masters + layouts + samples), `.ppsx` = slideshow that opens in presentation mode, `.pptm/.potm` = macro-enabled.

**Versioning tip:** put a version and date in the template's footer or sample slide ("YourCompany template v1.2, 2026"), and never overwrite a published template in place; bump the version so old decks stay reproducible.

Real-world examples: a business ships one `.potx` per brand division (commercial vs product) with shared masters. A university department distributes a thesis-defense template with a signature "Committee slide" layout. A personal freelancer keeps a `portfolio-2026.potx` so client proposals always match the website.

**Try it now.** Build the smallest useful template in 15 minutes: custom theme colors, one custom layout with an inserted Picture placeholder named "Hero image", and one sample slide. Save as `.potx`, close the file, then double-click it and confirm a brand-new untitled presentation appears with your layout in **Home** > **Layout**.

---

## 2.10 Design Ideas (PowerPoint Designer)

**Explanation.** **Design Ideas** (feature name: **PowerPoint Designer**) is the AI-assisted design panel. Add a picture, a list, or a few facts to a slide and Designer offers one-click professional layouts: it can crop photos into full-bleed compositions, build icon-and-text rows from bullet lists, convert date lists into timelines, and suggest consistent treatments across the deck. It is available in PowerPoint for Microsoft 365 and PowerPoint 2019/2021/2024 on desktop, and (more limited) on the web. It usually needs an internet connection because design decisions run as a service.

**Using it:**

1. On any slide, click **Design** > **Design Ideas** (right end of the ribbon). The **Designer** pane opens on the right and starts suggesting layouts for the current slide.
2. Click any suggestion to apply it. Scroll for more. Click the **X** on an idea's hover preview to tell Designer you dislike that direction (this refines future suggestions).
3. Keep the pane open and click through slides; Designer re-suggests per slide as content changes.
4. For a whole-deck suggestion flow: with the pane open, Designer also surfaces "Make my slide better" style recommendations as you add content.
5. If **Design Ideas** is missing: **File** > **Options** > **General** > tick **Automatically show me design options** (and check your Microsoft 365 license/internet connection). PowerPoint for the web has a smaller feature set than desktop.

**Designer and custom templates:** Microsoft documents that templates can be tuned to work *well* with Designer (custom templates that keep standard placeholders and layouts get smarter suggestions). And the reverse rule matters more: **Designer and master views do not mix well in one workflow**. Designer applies slide-level formatting tricks (cropped pictures, auto-positioned text) that fight hand-built master layouts. Pick a lane per deck:

- Structured/branded deck: build masters and layouts, use Designer only on hero/cover slides, then hand-check those slides against the template.
- Quick standalone deck: let Designer drive, but still fix fonts/colors to theme slots afterwards for consistency.

Real-world examples: a business analyst drops four KPI stats on a slide and applies Designer's big-number row instead of hand-aligning text boxes. A teacher turns three bullets about a process into Designer's SmartArt-like stepper instantly. A personal trip recap adds five photos and lets Designer build the collage grid.

**Try it now.** New slide, type three bullets ("On-time delivery 97%", "New deploys 42 per week", "Support tickets down 18%"), open **Design** > **Design Ideas**, and apply the big-stat callout suggestion. Then undo, apply the same idea on a slide using your custom master, and note whether it respected or fought your layout. Write down which of your custom layouts are "Designer-friendly" (simple title + content) and which are not.

---

## 2.11 Building a Simple Brand System in PowerPoint

**Explanation.** A **brand system** is the agreed, documented set of visual rules. In PowerPoint, the system is physically implemented as one `.potx` template plus a one-page spec. Keep it small enough that a non-designer can use it correctly. A complete-but-simple system for a company like YourCompany Inc contains exactly these decisions:

1. **Logo rules**: primary logo bottom-right of the master at 1.2 inches wide; monochrome white version on dark backgrounds; never rotate or recolor; keep 0.3 inch clear space.
2. **Color roles** (in theme slots so switching variants stays safe):
   - Text/Background Light 1 = `#FFFFFF` (slide base)
   - Text/Background Light 2 = Sand `#EDE6D6` (soft panels, table banding)
   - Text/Background Dark 1 = `#212121` (body text)
   - Accent 1 = Navy `#1F3864` (titles, primary shapes, chart series 1)
   - Accent 2 = Teal `#2E9BA6` (secondary shapes, chart series 2)
   - Accent 3 = `#F2F2F2` neutral gray for dividers
3. **Type scale**: headings Georgia (theme Heading font), body Calibri (theme Body font). Sizes: slide title 36-40pt, section header 24pt, body 16-18pt, caption/footer 10-11pt. Never introduce a third font or ad-hoc sizes.
4. **Layout library** (6 is plenty): Title Slide, Agenda/Section Header, Title and Content, Two Content, Photo + Caption, Closing.
5. **Footer strip**: "YourCompany Inc | Confidential | slide number" in 10pt gray at a fixed baseline on the master.
6. **Backgrounds**: white for content, Navy-to-navy gradient for title and closing, optional photo fill at 70% transparency behind section dividers.
7. **Usage rules in one sentence each**: max 6 bullets per slide; all charts use theme colors; photos always full-bleed or in a fixed 3:2 frame; no clip art, no WordArt, no accent lines under titles.

**Implementing it (build order):** theme colors and fonts first (Design > Variants), then Slide Master edits (logo, footer, master text styles), then the six layouts with placeholders, then sample slides, then save as `.potx` plus export one "spec slide" PNG/PDF that documents the rules.

**Maintaining it:** one owner, version-numbered file (`YourCompany-Deck-Template-v1.2.potx`), a changelog line in the spec, and a rule that decks for external audiences always start from the current template.

Real-world examples: a business hands sales one template and a one-page spec; brand consistency complaints drop to zero because defaults do the work. A classroom "brand" is the course identity: title style, diagram style, and a footer with course code and lecture number. A personal brand system keeps a job-seeker's portfolio, resume deck, and cover-letter one-pager visually identical.

**Try it now.** Write your one-page spec first (30 minutes, in any editor), covering the seven bullets above with your own values. Then implement only items 1-3 in PowerPoint (logo, theme colors, theme fonts) and screenshot the result. If the spec and the file disagree, fix the spec before building the layouts.

---

## Practice Projects (Hands-On)

Complete all five in order; each builds on the previous one.

**Project 1: YourCompany Master and Layouts.**
Build a blank deck whose Slide Master carries the YourCompany logo, the footer strip ("YourCompany Inc | Confidential"), and the master title/body text styles (Georgia 40pt Navy title; Calibri 24/20/18 body levels). Add two custom layouts: "Big Number" (title + one oversized content placeholder) and "Photo + Caption" (picture placeholder + caption text placeholder).
*Success criteria:* (a) a new slide with the "Big Number" layout shows the prompt text in the right place; (b) the logo cannot be selected in Normal view; (c) resizing the title on one slide and pressing Home > Reset restores it to the master position.

**Project 2: Theme Colors and Fonts Rescue.**
Take any old deck with at least 10 slides and messy colors (fixed colors are ideal). Define a custom theme color set and font set (sections 2.3), then convert every repeated object to theme slots and reset all slides.
*Success criteria:* (a) switching the theme variant recolors every title, shape fill, and chart series in the deck; (b) zero objects use "Standard Colors" or "More Colors" values (spot-check 5 objects); (c) all body text is Calibri and all titles Georgia without any manual font painting.

**Project 3: Background Gallery Deck.**
Create a 4-slide deck showing the four background families on four layouts: solid, gradient (2 stops), picture fill at 70% transparency, and one pattern fill. Each slide must carry readable 18pt body text over its background.
*Success criteria:* (a) each background is applied at layout/master level, not pasted as a slide-sized rectangle; (b) a colleague can read every slide at 3 meters on a projector; (c) a screenshot of the Format Background pane shows the fill type used on each slide.

**Project 4: The .potx Deliverable.**
Turn Projects 1-3 into one template: custom theme, edited master, 6 layouts, 4 realistic sample slides, version footer ("YourCompany template v1.0"). Save as `YourCompany-Deck-Template-v1.0.potx`.
*Success criteria:* (a) double-clicking the file opens a new *untitled* presentation (not the template itself); (b) all 6 layouts appear in Home > Layout with correct placeholder prompts; (c) a teammate who has never seen the brand can produce an on-brand 5-slide deck in 10 minutes using only the template.

**Project 5: Designer vs Master Shootout.**
Build the same 3-slide mini-deck twice: once purely with Design Ideas suggestions, once purely from your Project 4 template with no Designer. Compare for brand compliance, editability (can placeholders be Reset?), and time spent. Write a half-page verdict recommending one approach per deck type.
*Success criteria:* (a) both decks present the same 3 facts; (b) the template-based deck passes a full Reset on every slide with no layout breakage; (c) the verdict names at least one concrete failure mode you observed in each approach.

---

## Common Mistakes & Pitfalls

| Mistake | Why it hurts | Fix |
|---|---|---|
| Formatting fonts/colors slide by slide instead of in the theme or master | 50 slides to update per change; decks drift apart | Set theme colors/fonts once (Design > Variants > Colors/Fonts); use theme slots everywhere |
| Pasting the logo as a normal picture on each slide | Selectable, accidentally movable, bloats the file | Put it on the slide master or the relevant layout in View > Slide Master |
| Using "Standard Colors" or "More Colors" for repeated elements | Those colors are fixed values; themes and variants will not update them | Use Theme Colors slots (top dropdown row) for anything repeated |
| Building structure with free text boxes instead of layout placeholders | Reset cannot fix them; nothing snaps; no prompt text for teammates | Insert placeholders on layouts (Slide Master > Insert Placeholder) |
| Editing a layout after slides exist and wondering why nothing changed | Existing slides need the layout re-applied | Home > Reset (or right-click layout > Reset Slide) on affected slides |
| Expecting Slide Master in PowerPoint for the web | The web app has no Slide Master view | Use the desktop app for master/layout work (the web app can still apply themes) |
| Mixing Designer slides into a strict master-based deck | Designer resizes/repositions per-slide content at slide level and fights the template | Use Designer on standalone or hero slides only; verify against the template afterwards |
| Unreadable text over picture or gradient backgrounds | Contrast fails at the back of the room | Fade pictures to 60-80% transparency; keep body text contrast near 4.5:1; test at distance |
| Overusing pattern fills, heavy textures, and shadows | Dated, noisy, print-heavy looks | Keep fills flat or subtle gradient; effects from theme only |
| Saving the template as `.pptx` and mailing it around | Colleagues overwrite the master file with their content | Save as `.potx` and distribute the template (File > Save As > PowerPoint Template) |
| Adding a third font or 8 accent colors "just for one slide" | The system dies by a thousand exceptions | Extend the spec deliberately (new version) or do not do it |
| Footers typed as text boxes on one slide | Do not propagate, do not number, look inconsistent | Use Insert > Header & Footer with master-level placeholders |
| Forgetting sample slides in the template | Teammates ignore custom layouts and improvise | Keep 3-6 sample slides, one per layout, with realistic dummy content |
| Not versioning the template file | Old and new brand files circulate; nobody knows which is current | Name files with version + date; keep one owner and a changelog line |

---

## Key Takeaways

- Consistency comes from the design layers (theme, master, layouts, template), not from formatting slides one at a time. Format at the highest level where the statement stays true.
- A theme = 12 named colors + 2 named fonts + effects. Theme slots update everywhere at once; fixed ("standard"/custom) colors do not.
- Theme variants re-skin a deck in one click without touching content. Multiple masters = multiple themes in one file.
- The hierarchy is strict: Presentation > Slide Master (one per theme) > Slide Layouts > Slides. Master holds brand-wide elements (logo, footer, text styles); layouts hold structure (placeholder arrangements); slides hold content.
- Slide Master view (**View** > **Slide Master**) is where logos, watermarks, footers, slide numbers, backgrounds, and master text styles are edited once and inherited forever. Close with **Slide Master** tab > **Close Master View**.
- Placeholders are the contract between template and author: correct types and prompt text on layouts make decks self-assembling; **Home** > **Reset** restores any slide to its layout.
- Backgrounds come in solid, gradient, picture, and pattern fills via **Design** > **Format Background**; apply them at master/layout level and protect text contrast.
- `.potx` templates package the whole system and cannot be overwritten by content authors. Include sample slides and a version number.
- **Design Ideas / Designer** is a fast layout engine for standalone and hero slides, but it operates at slide level and can fight strict master-based templates; choose the workflow per deck.
- A simple brand system is small and documented: logo rules, color roles mapped to theme slots, two fonts with a fixed size scale, 5-6 layouts, a footer strip, background rules, and one-page usage rules.

---

## Further Learning

All links below are real Microsoft Support pages gathered during research for this module.

1. What is a slide master in PowerPoint? (Microsoft Support training): https://support.microsoft.com/en-us/powerpoint/training/what-is-a-slide-master-in-powerpoint
2. Customize a slide master: https://support.microsoft.com/en-us/powerpoint/training/customize-a-slide-master
3. Create and save a PowerPoint template (.potx): https://support.microsoft.com/en-us/powerpoint/create-and-save-a-powerpoint-template
4. Edit and re-apply a slide layout (the Reset workflow): https://support.microsoft.com/en-us/powerpoint/edit-and-re-apply-a-slide-layout
5. Change the background of slides: https://support.microsoft.com/en-us/powerpoint/change-the-background-of-slides
6. Remove or change the current theme (applying and switching themes): https://support.microsoft.com/en-us/powerpoint/remove-or-change-the-current-theme
7. Add color and design to your slides with themes (training): https://support.microsoft.com/en-us/powerpoint/training/add-color-and-design-to-your-slides-with-themes
8. Create your own theme in PowerPoint: https://support.microsoft.com/en-us/powerpoint/create-your-own-theme-in-powerpoint
9. Get design ideas for slides with PowerPoint Designer (training): https://support.microsoft.com/en-us/powerpoint/training/get-design-ideas-for-slides-with-powerpoint-designer
10. Insert or change the slide numbers, date, or footer for on-screen slides: https://support.microsoft.com/en-us/powerpoint/insert-or-change-the-slide-numbers-date-or-footer-for-on-screen-slides-in-powerpoint
11. Create a branded presentation template: https://support.microsoft.com/en-us/powerpoint/create-a-branded-presentation-template
12. Add the same image or watermark to every slide: https://support.microsoft.com/en-us/powerpoint/add-the-same-image-or-watermark-to-every-slide

---

*End of Module 02. Next: Module 03 - Working with Text and Content.*


## FILE: 03-Visual-Design/03-visual-design.md

# Module 03: Visual Design for Slides

---

**Module number:** 03
**Title:** Visual Design for Slides
**Level:** Intermediate
**Prerequisites:** Module 01 (PowerPoint fundamentals: the ribbon, slide basics, saving files), Module 02 (text and layout basics: placeholders, layouts, slide masters). Basic comfort selecting, moving, and resizing objects on a slide.
**Estimated study time:** 3.5 to 4.5 hours (plus 2 to 3 hours of hands-on practice projects)
**Next module:** Module 04 (Charts, Data Visualization, and Tables)

---

Welcome to the module that separates "someone who can make slides" from "someone whose slides people actually remember." Everything here works in Microsoft PowerPoint for Microsoft 365, PowerPoint 2021, and PowerPoint for the web, with only tiny differences in button placement that we will call out as we go. All examples use fictional data from a pretend company called YourCompany Inc. No real brands, people, or credentials appear anywhere in this module.

We will move from theory (design principles, typography, color) to the object toolbox (shapes, icons, images, SmartArt, screenshots) to the polish layer (grids, guides, Design Ideas) and finish with five practice projects you can build and keep.

---

## 1. Design Principles Applied to Slides: Contrast, Repetition, Alignment, Proximity

Every good-looking slide you have ever seen obeys four principles borrowed from graphic design: Contrast, Repetition, Alignment, and Proximity (often shortened to C.R.A.P., which design students never tire of mentioning). Slides are not documents. A slide is a projected, glanced-at, spoken-over object, so these four principles matter even more than they do on paper.

**Contrast.** If two things are different, make them obviously different. A headline that is 40 pt next to body text at 28 pt whispers "slightly different." A headline at 40 pt bold white on deep navy, next to body text at 20 pt in light gray, shouts "different." Contrast creates a reading order: the audience should know where to look first, second, and last within about two seconds. Use contrast in size, weight, color, and position. Never use contrast-subtly-washed-out-taupe-next-to-slightly-browner-taupe; that is not contrast, that is mud.

**Repetition.** Every element of your visual language should recur: one accent color used the same way everywhere, the same title position on every slide, the same icon style (line icons or filled icons, never both), the same chart palette. Repetition is what makes 30 slides feel like one deck instead of 30 posters. The slide master (covered in Module 02) is where you encode repetition so it happens automatically.

**Alignment.** Nothing should sit at an arbitrary position. Every text box, picture, and shape should align with something else on the slide. Aligning to invisible grid lines creates implied structure that the audience feels even when they cannot name it. The eye reads sloppiness in alignment as sloppiness in thinking.

**Proximity.** Related things belong close together; unrelated things belong far apart. If a caption describes a chart, it sits next to that chart, not on the other side of the slide. If three boxes describe one process and a fourth box is a footnote, group the three and separate the footnote. Proximity answers "what goes with what?" without a single word of explanation.

### The assertion-evidence slide model

The single highest-leverage slide structure for business and education is assertion-evidence. Instead of a topic label title ("Q3 Results") with a wall of bullets, write the entire point of the slide as a full-sentence assertion in the title ("Q3 revenue grew 18% driven by enterprise renewals") and support it with visual evidence: one chart, one diagram, one screenshot, one image. The audience can follow your argument from the titles alone, which is exactly what busy executives do.

**Step-by-step: rebuild a bullet slide as assertion-evidence**
1. Take any existing slide with a topic title and five bullets.
2. Ask: "What is the one sentence this slide is trying to prove?" Write that sentence into the title placeholder: **Home > click the title placeholder > type the assertion**, for example "YourCompany Inc. churn fell to 4% after the onboarding redesign".
3. Delete or shrink the bullet list to at most three short supporting points in a text box.
4. Insert the evidence: **Insert > Chart** for numbers, **Insert > SmartArt** for a process, **Insert > Pictures** for a photo.
5. Keep the title to one or two lines. If the assertion needs three lines, it is two assertions: split the slide.

**Real-world examples.**
- *Business:* A quarterly review slide titled "Enterprise renewals drove 72% of Q3 growth" with a single stacked column chart, instead of "Q3 Sales Update" with nine bullets.
- *Education:* A lecture slide titled "Photosynthesis converts light energy into chemical energy in the chloroplast" with one labeled diagram, instead of "Photosynthesis" with definitions in bullets.
- *Personal:* A wedding-planning slide titled "The garden venue saves $4,200 and seats all 120 guests" with a small comparison table and one photo of the venue.

**Try it now.** Open any deck you have already made. Pick the busiest slide. Rewrite its title as a full-sentence assertion with a number in it. Then delete half the body text and add one visual. Compare the two versions side by side. Which one could you present without reading the slide aloud?

---

## 2. Typography on Slides: Fonts That Survive the Projector

Projectors wash out fine detail, screens shrink pixels, and audiences sit up to 15 meters back. Slide typography has one rule above all others: **the person in the back row must be able to read it.** Everything else is detail.

**Size rules that work in practice.**
- **Titles: 36 to 44 pt.** For ballrooms and webinars viewed on phones, go to the top of that range or above.
- **Body text: 14 to 24 pt.** 24 pt is for key points you want noticed; 18 pt is a comfortable default; 14 pt is the absolute floor and only for genuinely secondary content such as source lines and footnotes.
- **The readable-from-the-back rule:** if a line of text cannot be read from the farthest seat in the room, it does not belong on the slide. A practical test: print the slide on paper, hold it at arm's length. If you squint, grow the font.
- Never shrink text to fit more content. Cut content instead. Slides are not documents, and a 10 pt wall of text is a confession that the slide should have been two slides or a handout.

**Font pairing.** Use at most two typefaces: one for headings, one for body. Reliable, always-installed, presentation-safe pairings: **Segoe UI Semibold headings with Segoe UI body** (the Microsoft 365 house style, clean and modern), **Verdana headings with Arial body** (maximum legibility at distance), or a single typeface used at two weights (Calibri Light headings, Calibri body). If your organization has a brand font, use it, but verify it exists on every machine that will run the show, and know that PowerPoint for the web substitutes missing fonts silently.

**Line spacing and density.**
- Line spacing: **Home > Line Spacing > 1.1 to 1.3** for body text. Single spacing (1.0) crowds; more than 1.5 wastes vertical space.
- Space before paragraphs: **Home > Line Spacing > Line Spacing Options > Spacing > Before: 6-10 pt** instead of blank lines.
- Six lines per slide is a healthy ceiling; six words per line is a healthy ceiling for bullets.

**Step-by-step: set typography for a whole deck**
1. **View > Slide Master.**
2. Select the master slide at the top of the thumbnail pane (the one that all layouts inherit from).
3. Click the title placeholder, set font and size: **Home > Font > Segoe UI Semibold, 40 pt.**
4. Click the body placeholder, set **Home > Font > Segoe UI, 20 pt**, then **Home > Line Spacing > 1.2**.
5. Set bullet text distance: **Home > Line Spacing > Line Spacing Options > Indent > Before text: 0.3", Hanging: 0.25".**
6. Repeat on the Title Slide and Section Header layouts if they should differ.
7. **View > Normal** to return. Every new slide now inherits these settings.

**Real-world examples.**
- *Business:* A 30-slide board deck in Segoe UI only, titles 40 pt bold, body 20 pt, one accent color for numbers. Readable from any seat.
- *Education:* A 60-slide biology lecture using Verdana 22 pt body so students in a 200-seat hall can copy notes without guessing.
- *Personal:* A graduation party slideshow with one display font for the title slide and Arial 24 pt for captions, so grandparents can read the captions from the sofa.

**Try it now.** Set the zoom to 25% (**View > Zoom > 25%**) and look at a slide. This approximates the back-of-room view. Anything you cannot resolve at 25% zoom is too small. Fix three slides using only font size and deletion.

---

## 3. Color Theory for Slides: Palettes, 60-30-10, and Accessibility

Color does three jobs on a slide: it groups (these three boxes belong together), it ranks (this number is the important one), and it brands (this is YourCompany Inc.'s deck). Color does not do a fourth job: decoration. Rainbow palettes are how amateur decks announce themselves.

**Building a palette.** Start from three colors and add neutrals:
1. **Primary:** your dominant color, usually the brand color or a deep neutral (dark navy, charcoal). Covers backgrounds and large areas.
2. **Secondary:** a supporting color from the same family or a calm complement. Covers secondary shapes, chart series.
3. **Accent:** exactly one attention-grabber (a warm orange, a vivid teal) reserved for the single most important thing on any slide.
4. **Neutrals:** white, near-white, mid-gray, near-black, for text, lines, and background.

**The 60-30-10 rule.** Borrowed from interior design and perfectly portable to slides: 60% of the visual area is the dominant color (usually the background and large fills), 30% is the secondary color (cards, chart bodies, headers), and 10% is the accent (the one number, the one call-to-action). On a typical slide with a white background this plays out as: white space 60%, navy blocks 30%, orange highlight 10%. The moment two colors fight for the 10% accent role, the slide loses its focal point.

**Contrast and accessibility.**
- **Insert > Accessibility > Check Accessibility** (**Review > Check Accessibility** in some versions) runs the built-in checker and flags missing alt text and low-contrast text.
- Text must be readable against its background. Practical targets: body text at least 4.5:1 contrast ratio, large display text at least 3:1. Near-black text (#1F1F1F or darker) on white or very light fills is always safe. White text only on dark fills.
- Never encode meaning in color alone ("the red bars are the failures"): add labels, patterns, or direct annotations, because color-blind viewers and grayscale printouts will lose it.

**Color-blind-safe palettes.** Roughly one man in twelve has red-green color vision deficiency. Safe practice:
- Avoid pure red next to pure green.
- Use blue-versus-orange as your main contrast pair; it survives all common color vision deficiencies.
- In charts, prefer the blue / orange / gray / yellow palette families, and vary shape or pattern as a second channel.
- Test with a color-blindness simulator before publishing (many free tools exist, and PowerPoint's Accessibility Checker warns on some contrast issues).

**Step-by-step: build and apply a theme color set**
1. **Design > Variants > Colors > Customize Colors.**
2. Under **Theme colors**, set Text/Background to near-black and white, then set Accent 1 to your primary, Accent 2 to your secondary, Accent 3 to your accent.
3. Name the set "YourCompany Palette" and click **Save.**
4. Apply colors through the theme slots (**Home > Font Color** and **Shape Fill** show theme colors first) so a future palette swap restyles the entire deck via **Design > Variants > Colors.**
5. Check contrast: **Review > Check Accessibility** and fix any flagged text.

**Real-world examples.**
- *Business:* YourCompany Inc. board template: 60% white, 30% dark navy cards and chart series, 10% amber for the one KPI number per slide.
- *Education:* A chemistry deck using blue-orange contrast for reactants versus products, with shapes and labels too, so color-blind students are never guessing.
- *Personal:* A travel recap with 60% photo area, 30% white caption panels, 10% coral for city names.

**Try it now.** Take one slide and repaint it with exactly three colors plus neutrals using the 60-30-10 split. Then use a color-blindness simulator (or mentally convert to grayscale by printing in black and white) and confirm the hierarchy still reads.

---

## 4. Shapes: Drawing, Aligning, Grouping, and Merge Shapes

Shapes are the raw material of every diagram, card, badge, and process arrow you will ever build. Mastering shape tools turns PowerPoint into a lightweight design program.

**Drawing shapes.**
1. **Insert > Shapes** and pick from Lines, Rectangles, Basic Shapes, Block Arrows, Equation Shapes, Flowchart, Stars and Banners, and Callouts.
2. Click and drag on the slide to draw. Hold **Shift** while dragging to constrain (perfect circles from the oval tool, perfect squares from the rectangle tool, straight 45-degree lines).
3. Hold **Ctrl** while dragging to draw from the center outward.
4. With the shape selected, style it: **Shape Format > Shape Fill, Shape Outline, Shape Effects.** Keep effects to a whisper: soft shadow or nothing. Heavy bevels date a deck fast.
5. Add text: select the shape and type, or right-click > **Edit Text.**

**Aligning and distributing.**
1. Select two or more objects (click one, then **Shift-click** the others, or **Ctrl-click** for a multiple selection; **Ctrl+A** selects everything on the slide).
2. **Shape Format > Align > Align Left** (or Align Center, Align Right, Align Top, Align Middle, Align Bottom).
3. **Shape Format > Align > Distribute Horizontally** or **Distribute Vertically** to make gaps between multiple objects perfectly even. Select three or more objects for distribution to matter.
4. Check **Shape Format > Align > Align to Slide** when you want objects centered on the slide itself rather than relative to each other.

**Grouping.**
1. Select the objects that belong together.
2. **Shape Format > Group > Group** (or press **Ctrl+G**).
3. Move, resize, or recolor the group as one unit. Enter a group to edit parts: right-click > **Group > Edit Group**, or just double-click a member.
4. Ungroup with **Shape Format > Group > Ungroup** (**Ctrl+Shift+G**). Pro tip: ungrouping a pasted SVG or SmartArt can convert it into editable shapes.

**Merge Shapes: the shape-customization superpower.** Merge Shapes (available when two or more shapes are selected: **Shape Format > Merge Shapes**) booleans shapes together like a vector design tool. Select the shapes in the correct order: the first-selected shape's formatting usually wins for fill in some operations.

- **Union:** fuses all selected shapes into one silhouette. Build a speech-bubble-plus-tail or a cloud-plus-pointer in seconds.
- **Combine:** unions but punches out overlapping areas, creating cut-outs. Draw a circle on a square, **Combine**, and you have a square with a circular hole.
- **Fragment:** shatters everything into separate pieces along every crossing line. This is how you slice an image or shape into a mosaic of tiles.
- **Intersect:** keeps only the overlapping area of all selected shapes. Crop a photo to a circle by intersecting a circle with the picture (select the picture first, then the circle).
- **Subtract:** removes the later-selected shapes from the first-selected shape. Select a rounded rectangle, then a small circle at its corner, **Subtract**, and you have a custom notch shape.

**Step-by-step: build a custom "arrow chevron card" with Merge Shapes**
1. **Insert > Shapes > Rectangle** and draw a 3" x 1.5" rounded rectangle.
2. **Insert > Shapes > Isosceles Triangle**, rotate it 90 degrees (**Shape Format > Rotate > Rotate Right 90**), and place it so its base overlaps the rectangle's right edge.
3. Select the rectangle first, then **Shift-click** the triangle.
4. **Shape Format > Merge Shapes > Union.** One clean chevron card.
5. Set **Shape Fill** to your secondary color, type a label such as "Phase 1: Discovery".
6. Duplicate the chevron (**Ctrl+D**) three times, use **Shape Format > Align > Align Middle** and **Distribute Horizontally**, then edit labels and use your accent color on the current phase only.

**Real-world examples.**
- *Business:* A four-phase roadmap built from unioned chevrons, aligned and distributed into a perfect row, with the current phase in the accent color.
- *Education:* A Venn diagram where two circles are **Combine**d with a third, filled at 30% transparency to show overlapping habitats.
- *Personal:* A wedding seating plan: rounded-rectangle tables labeled "Table 1" through "Table 8", aligned in a grid with Distribute, grouped per section.

**Try it now.** Build the chevron roadmap above with four phases and no gaps in spacing (verify with Distribute Horizontally). Then make a circle-with-square-hole shape using **Combine** and save it in your custom shape vocabulary.

---

## 5. Icons and SVG: Modern Symbols, Properly Recolored

Icons are the fastest way to make a slide look designed. Modern PowerPoint includes a licensed stock icon library, and SVG (Scalable Vector Graphics) icons can be inserted and edited like shapes.

**Inserting stock icons.**
1. **Insert > Icons** (in the Illustrations group). In PowerPoint for the web this appears as **Insert > Icons** too, with the same library.
2. Browse categories (Analytics, Arrows, Business, Communication, Education, and more) or search by keyword.
3. Click to select one or more icons, then **Insert.**
4. Resize proportionally by dragging a corner handle. Icons are vectors: they scale without pixelation, so 20 pt or 200 pt both look sharp.

**Recoloring icons.**
1. Select the icon.
2. **Graphics Format > Graphics Fill** and choose from theme colors (this is why theme slots matter: recoloring follows your palette).
3. For multi-part recoloring, convert the icon to shapes: right-click the icon > **Convert to Shape** (or **Graphics Format > Convert to Shape**), then **Graphics Format > Ungroup** and color each piece. Note: converting breaks the link to the icon library, so duplicate the original first if you might need it pristine.

**SVG icons.** SVGs (from your design team or any reputable icon library) insert via **Insert > Pictures > This Device** and behave as graphics objects: infinitely scalable, recolorable via **Graphics Format > Graphics Fill**, and convertible to shapes with **Convert to Shape** + **Ungroup** for full editability.

**Icon hygiene rules.**
- One icon style per deck: all outline or all filled, one line weight.
- One visual metaphor per concept: if "customer" is a person icon on slide 4, it is the same person icon on slide 22.
- Icons replace bullets; they do not decorate them. An icon plus a short label beats an icon plus a bullet paragraph.
- Never stretch an icon: resize from a corner handle with **Shift** held (or just use corner handles, which scale proportionally in current versions).

**Real-world examples.**
- *Business:* A benefits slide with three filled icons (shield = security, clock = time saved, coin stack = cost), each over a 3-word label, all in YourCompany navy with amber for the coin.
- *Education:* A lab safety slide using warning and equipment icons instead of a text list of rules.
- *Personal:* A honeymoon itinerary slide with plane, hotel, and camera icons marking the three legs of the trip.

**Try it now.** Open **Insert > Icons**, search "growth", and build a slide with exactly three icons, recolored to your theme palette, each with a one-word label. Convert one icon to a shape and recolor a single part of it. Delete everything and rebuild it faster the second time.

---

## 6. Images Done Right: Insert, Crop, Background Removal, Compression

Photography gives slides emotion and credibility. Done badly, it gives them stretch marks and 40-megabyte file sizes.

**Inserting images.**
1. **Insert > Pictures > This Device** (from your computer), **Stock Images** (licensed library including photos, cutout people, and illustrations), or **Online Pictures** (searches the web; check usage rights for anything published externally).
2. Click **Insert.** The image lands selected with the **Picture Format** tab open.

**Sizing without stretching.** This is the number one image mistake in the world.
- Always resize from a **corner** handle. Corner handles scale proportionally; side handles squash and stretch and must be avoided except for deliberate effects.
- To force proportionality on any handle: hold **Shift** while dragging (in current Microsoft 365 versions, corner handles are proportional by default).
- To set exact size: **Picture Format > Size** group, type height or width (with **Lock aspect ratio** checked in **Picture Format > Size dialog launcher > Size > Lock aspect ratio**).

**Cropping.**
1. Select the image, **Picture Format > Crop.** Black crop handles appear.
2. Drag the handles inward. Cropping hides area without deleting it (**Crop > Reset** restores the original).
3. **Crop to Shape:** **Picture Format > Crop > Crop to Shape > Oval** for a circular portrait.
4. **Picture Format > Crop > Aspect Ratio > 1:1** (square) or 16:9 (widescreen) for consistent framing across a photo wall.
5. **Crop > Fill** places the image inside a fixed frame (cropping as needed); **Crop > Fit** shrinks the image to fit and shows the whole thing (letterboxing may appear; fill the background shape with a soft color to make it intentional).

**Remove Background.**
1. Select the image, **Picture Format > Remove Background.**
2. PowerPoint auto-marks the area to remove (magenta). Use **Mark Areas to Keep** and **Mark Areas to Remove** (draw short lines over the misjudged regions) to refine.
3. Click **Keep Changes.** For clean cutouts of people and products, this beats manual erasing in seconds.

**Compressing pictures.**
1. Select any picture, **Picture Format > Compress Pictures** (the icon with four small arrows).
2. Choose compression options: **Apply only to this picture** off to compress all, **Delete cropped areas of pictures** on to permanently shed hidden pixels (do this only when you are certain you will not re-crop).
3. Pick the target: **E-mail (96 ppi)** for decks sent as attachments, **Screen (150 ppi)** for projector and webinar use, **Print (220 ppi)** when the deck will be printed.
4. **File > Save As** a copy first if you might need the high-resolution originals later.

**Real-world examples.**
- *Business:* A customer-story slide with a background-removed photo of a factory line composited over YourCompany navy, compressed to 150 ppi so the 30-slide deck emails at under 8 MB.
- *Education:* A history lecture with square-cropped portraits (**Crop > Aspect Ratio > 1:1**) arranged in a row so faces align despite original photos being different shapes.
- *Personal:* A baby-shower slideshow with circular cropped portraits (people), all resized from corner handles so nobody has a stretched face.

**Try it now.** Insert a stock photo, crop it to 1:1, then apply **Crop to Shape > Rounded Rectangle**. Use **Remove Background** on a second photo of a person, place the cutout over a colored rectangle, and finish with **Compress Pictures > 150 ppi**. Note the file size before and after in **File > Info.**

---

## 7. SmartArt: Choosing Layouts and Converting Bullets to SmartArt

SmartArt is PowerPoint's built-in diagram engine. It is the correct answer to "how do I show this relationship visually in 20 seconds," and it recolors to your theme automatically.

**Choosing the right layout.** **Insert > SmartArt** organizes layouts by what they mean:
- **List:** unordered items (Basic Block List, Vertical Curved List).
- **Process:** a sequence with direction (Basic Process, Chevron Process, Continuous Block Process).
- **Cycle:** a repeating loop (Basic Cycle, Radial Cycle).
- **Hierarchy:** org charts and trees (Hierarchy, Organization Chart, Horizontal Hierarchy).
- **Relationship:** connections and overlaps (Basic Venn, Radial Cluster).
- **Matrix:** four quadrants or 2x2 analyses (Basic Matrix, Grid Matrix).
- **Pyramid:** layered foundations (Basic Pyramid, Inverted Pyramid).

Rule of thumb: if the words have an order, use Process. If they have a boss, use Hierarchy. If they come back around, use Cycle. If there is no relationship at all, keep them as a list and do not force a diagram.

**Converting bullets to SmartArt (the 10-second upgrade).**
1. Click inside a bulleted text placeholder.
2. **Home > Convert to SmartArt** (in the Paragraph group; if it is not visible, use **Home > Paragraph group dialog launcher > SmartArt** or right-click the placeholder > **Convert to SmartArt**).
3. Hover the gallery thumbnails to live-preview. Click a layout (Basic Process or Vertical Bullet List are safe starts).
4. Not happy? While the SmartArt is selected, **SmartArt Design > Layouts** lets you swap to another type without retyping. **SmartArt Design > Text Pane** shows the underlying bullet outline you can edit like plain text.

**Editing and styling SmartArt.**
1. **SmartArt Design > Add Shape / Promote / Demote** adjusts structure as content changes.
2. **SmartArt Design > Change Colors** applies your theme's color variants; **SmartArt Styles** adds subtle effects (keep it flat or gentle).
3. Click individual shapes to override colors (this is how you mark the current phase in your accent).
4. Too complex? If you are adding shapes beyond about seven, the diagram is trying to be a handout. Split the slide or move the detail to **View > Notes Page.**

**Real-world examples.**
- *Business:* A five-bullet onboarding-process list converted to **Chevron Process** and recolored with the current step in amber.
- *Education:* Three ecosystem components turned into **Basic Cycle** to show the nutrient loop.
- *Personal:* A house-move checklist converted to **Vertical Curved List**, grouped into "Before", "Moving day", "After".

**Try it now.** Write five bullets describing how YourCompany Inc. handles a support ticket. Select the text box, **Home > Convert to SmartArt > Basic Process.** Then use **SmartArt Design > Change Colors** to apply theme colors and override the third step with your accent color. Swap the layout twice to see how meaning changes with shape.

---

## 8. Screenshots and Screen Clippings: Evidence From the Screen

When a slide needs to show software, a website, an error message, or a dashboard, a screenshot is the evidence. PowerPoint's built-in tools capture and insert in one move.

**Full-screen screenshots.**
1. Go to the slide where the image belongs.
2. **Insert > Screenshot.** The Available Windows gallery shows thumbnails of every open window.
3. Click one to insert it full-frame. It inserts at full size: resize from a corner and use **Crop** to keep only the relevant area.

**Screen clippings (partial capture).**
1. Open and arrange the window you want to capture, then return to PowerPoint (the clipping tool auto-hides the PowerPoint window).
2. **Insert > Screenshot > Screen Clipping.** The screen dims with a frosted overlay.
3. Drag a rectangle around the exact region. The clipping lands on the slide.
4. Tighten the edges with **Picture Format > Crop.**

**Polishing screenshots.**
- Blur or cover sensitive data: **Insert > Shapes > Rectangle** (no outline, fill matching the surface) over names, emails, or numbers. Real data must never appear in training materials; fake data like "YourCompany Inc. / user@example.com" stands in.
- Call out the point: **Insert > Shapes > Oval** with no fill and a thick accent outline around the button or field you are discussing, plus a one-line callout (**Insert > Shapes > Line + text box** or a **Callouts** shape).
- Keep text legible: if the UI text is unreadable at slide size, crop harder and show less of the window.

**Real-world examples.**
- *Business:* A training deck with a clipped region of the CRM order form, one amber oval around the "Approve" button, one caption: "Step 3: approve within 24 hours."
- *Education:* A software-usage lecture clipping the exact dialog students must fill in, with redacted sample fields.
- *Personal:* A "how to file our insurance claim" family-deck with clipped screenshots of each web form page and the sensitive fields covered.

**Try it now.** Open any application on your computer, then in PowerPoint use **Insert > Screenshot > Screen Clipping** to capture one control or field. Redact one piece of fake-sensitive text with a rectangle, and highlight the important control with an accent-colored oval. Caption it in six words or fewer.

---

## 9. Grids, Guides, and Alignment Tools: Precision Without Effort

Professional decks look calm because everything lines up to a hidden structure. PowerPoint gives you that structure.

**Gridlines and guides.**
1. **View > Gridlines** draws faint dotted grid marks on the editing canvas (never printed or presented).
2. **View > Guides** shows the horizontal and vertical center guides (blue dashed lines with measurements when dragged).
3. Add more guides: right-click a guide > **Add Vertical Guide** or **Add Horizontal Guide**, then drag it into position. A typical layout grid: guides at the left and right margins (for example 0.5" from each edge), one at the vertical center, and one at the title baseline.
4. Color-code a guide: right-click the guide > **Color** to distinguish margin guides from column guides.

**Snap behavior.**
1. **View > dialog launcher (tiny arrow) > Grid and Guides** (or right-click the slide background > **Grid and Guides**).
2. Keep **Snap objects to grid** on for coarse alignment and **Snap objects to other objects** on so edges and centers magnet together as you drag (orange smart guides flash when objects align).
3. To nudge an object off the grid: hold **Alt** while dragging (temporarily suspends snapping) or select the object and tap the arrow keys for pixel-scale nudges.

**Align, Distribute, Rotate, and the Selection Pane.**
- **Shape Format > Align** (or **Home > Arrange > Align**) gives Align Left/Center/Right/Top/Middle/Bottom and Distribute Horizontally/Vertically (see Section 4).
- **Shape Format > Rotate > Rotate Right/Left 90, Flip Vertical/Horizontal** for symmetric layouts.
- **Home > Arrange > Selection Pane** lists every object on the slide: rename objects ("title", "kpi-number", "chart-q3") for sanity, click the eye icon to hide/show while editing, and use it to grab objects buried under others.

**Step-by-step: set up a reusable layout grid**
1. **View > Guides** and **View > Gridlines.**
2. Drag vertical guides to 0.6" and 12.73" from center (the default guide reads its distance as you drag) to mark your left and right text margins.
3. Drag the horizontal center guide up to mark the title baseline, about 1.25" from the top.
4. Right-click each guide > **Add** copies where you need column boundaries for two- and three-up card layouts.
5. Save the file as a template: **File > Save As > PowerPoint Template (.potx)** so every future deck starts with the grid.

**Real-world examples.**
- *Business:* A KPI dashboard with four cards snapped to guides in a 2x2 grid, each card a grouped set of rectangle + number + label, perfectly distributed.
- *Education:* A timeline slide where six event markers are **Distribute**d Horizontally so the gap between years is visually honest.
- *Personal:* A photo collage where five pictures share the same top and bottom edges via **Align Top** and **Align Bottom**.

**Try it now.** Turn on guides and gridlines, set two margin guides, and place four boxes in a 2x2 layout using only Align and Distribute (no eyeballing). Then open the **Selection Pane** and name each box. Time yourself: the second 2x2 should take under 60 seconds.

---

## 10. Design Ideas and Avoiding the Dated Look

**Design Ideas** (also called Designer) is PowerPoint's automatic layout engine: it looks at your content and proposes complete, professional slide designs in the **Design Ideas** pane. It is the fastest polish in the software.

**Using Design Ideas.**
1. Open **Design > Design Ideas** (the pane opens on the right). In PowerPoint for the web the same feature appears under **Design > Designer.**
2. Put real content on the slide first (a title, a few lines, a picture): the pane suggests layouts matched to that content.
3. Click a suggestion to apply it. The slide is rebuilt with real shapes and pictures you can then edit.
4. Not seeing suggestions? Check that **Automatically show me design ideas** is enabled in **File > Options > General > PowerPoint Designer** (Windows), and that an internet connection is available, since Designer runs its service online.
5. Designer honors your theme: if your theme colors and fonts are set (Section 3 and Module 02), suggestions arrive in your brand automatically.

**When to accept and when to override.** Designer is excellent for: title slides, section dividers, photo slides, and "one big number" slides. Designer is a starting point only for dense analytic slides, where you should take its spacing ideas and then hand-tune with the alignment tools from Section 9.

**Avoiding clip art and other dated looks.** Dated styling is instantly recognizable and instantly discounted:
- **Clip art** (the cartoonish Office clip-art library) stopped being credible around 2012. Replace with stock icons (Section 5) or photography (Section 6).
- **Heavy 3-D effects:** bevels, embossing, extreme WordArt shadows, gradient rainbow fills. Keep fills flat; use at most a soft shadow (40% opacity, 3-5 pt blur) on cards.
- **Bullet walls and tiny text** (see Section 2).
- **More than two typefaces or more than one accent color** (see Section 3).
- **Stretched images** (see Section 6).
- **Default clip arrows and default chart colors** without theme application.
- **Transitions and animations as entertainment.** In business and education, **Transitions > Morph** (used sparingly for continuity between two related slides) and simple appear/fade animations are the entire safe list. Star wipes and bouncing text belong nowhere.

**Step-by-step: modernize a dated slide in five moves**
1. Delete clip art. Replace with one stock icon or one photo (**Insert > Icons** / **Insert > Pictures > Stock Images**).
2. Convert bullets to SmartArt (Section 7) or cut them to three lines.
3. Set titles 40 pt and body 20 pt (Section 2).
4. Recolor using theme slots and 60-30-10 (Section 3).
5. **Design > Design Ideas** and either accept a suggestion or use its spacing to realign manually (Section 9).

**Real-world examples.**
- *Business:* A 2014-era partner deck (clip art handshake, WordArt title) rebuilt with a photo title slide and three icon cards, and Design Ideas applied to the section dividers.
- *Education:* A geography lecture replacing cartoon globe clip art with real satellite photography and clean labeled callouts.
- *Personal:* A réunion invitation with a single photo, one accent color, and a Designer-suggested title layout in under five minutes.

**Try it now.** Find the most dated slide you own. Apply the five-move modernization above, then open **Design > Design Ideas** and apply one suggestion to the title slide. Save both versions and note which one you would send to a client.

---

## Hands-On Practice Projects

Build these five in order. Each one compounds skills from the previous projects.

**Project 1: The Assertion-Evidence Rebuild**
Take a five-slide deck you already have (or make a fake one about YourCompany Inc.'s quarterly results) and rebuild every slide in the assertion-evidence model: full-sentence assertion titles with numbers, one visual per slide, at most three short supporting points.
*Success criteria:* (a) every title is a complete sentence containing a number or specific claim; (b) no slide has more than three body lines; (c) each slide contains exactly one of: chart, SmartArt, photo, or icon set; (d) a reader who reads only the titles can summarize the deck's argument in one sentence.

**Project 2: The Brand System**
Build a reusable slide master and theme for "YourCompany Inc.": two typefaces, three theme colors plus neutrals, 60-30-10 applied across five demo slides (title, agenda, content, chart, closing).
*Success criteria:* (a) theme saved via **Design > Variants > Colors > Customize Colors** and fonts via **Customize Fonts**; (b) all five slides inherit type and color from **View > Slide Master** (change the master font once and all five update); (c) accent color appears on at most one element per slide; (d) **Review > Check Accessibility** reports no low-contrast text.

**Project 3: The Shape-Only Diagram**
Build a four-phase process roadmap using only shapes and Merge Shapes: chevron cards created with **Union**, aligned with **Align Middle**, spaced with **Distribute Horizontally**, and grouped per phase. No images allowed.
*Success criteria:* (a) chevrons are custom shapes made via **Merge Shapes > Union** of rectangle + triangle; (b) spacing between all four cards is mathematically even (verify with Distribute); (c) the current phase is in the accent color and all others in the secondary; (d) the entire roadmap moves as one grouped object; (e) no shape uses a 3-D or bevel effect.

**Project 4: The Polished Visual Deck (Images, Icons, Screenshots)**
Build a three-slide deck: one photo slide (cropped to 16:9, background-removed subject composited over a brand block), one icon slide (three theme-recolored icons with one-word labels), and one screenshot slide (screen clipping with a redacted field and an accent callout). Compress at the end.
*Success criteria:* (a) no image is stretched (check by measuring: width/height ratio equals the original); (b) icons all come from one style family and use theme colors; (c) the screenshot contains zero real personal data; (d) **File > Info** shows total size below 5 MB after **Compress Pictures > 150 ppi**; (e) every picture has alt text (**Picture Format > Alt Text**).

**Project 5: The Designer-Finished Deck**
Take Projects 1 through 4 output (or build a fresh six-slide YourCompany Inc. pitch) and finish it: use **Design > Design Ideas** on at least two slides, set up guides and align every object to them, convert one bullet list to SmartArt, and modernize anything that looks dated. Then rehearse: stand two meters from your screen and confirm everything is readable.
*Success criteria:* (a) at least two slides use a Design Ideas layout or its spacing principles; (b) every object on every slide snaps to a guide or aligns with another object (toggle **View > Guides** and look for floaters); (c) one bullet list is now SmartArt in a layout that matches its meaning; (d) zero clip art, zero stretched images, zero rainbow palettes; (e) the whole deck passes the arm's-length readability test.

---

## Common Mistakes & Pitfalls

| Mistake | Why it hurts | Fix |
|---|---|---|
| Shrinking fonts to fit more text | Back row cannot read; signals laziness | Cut content or split slides; keep body at 14-24 pt, titles 36-44 pt |
| Topic-label titles ("Q3 Update") | Audience must hear the speaker to get the point | Assertion-evidence titles: a full sentence with the claim and a number |
| Resizing pictures with side handles | Stretched faces and squashed logos look amateur | Drag corner handles only; keep **Lock aspect ratio** checked |
| Rainbow palettes and 5+ colors per slide | No focal point; everything competes | 60-30-10 with exactly one accent color |
| Red/green as the only differentiator | Invisible to color-blind viewers and in grayscale | Blue vs orange plus labels or patterns |
| Text under 14 pt anywhere | Unreadable from the back of any room | 14 pt floor; footnotes at 14 pt, everything else larger |
| Eyeballing positions ("looks about right") | Uneven gaps read as sloppy thinking | **View > Guides** + **Shape Format > Align / Distribute** |
| Clip art, WordArt shadows, heavy 3-D bevels | Instantly dates the deck to 2005 | Stock icons, photos, flat fills, soft shadows only |
| Stretching icons or mixing outline and filled styles | Breaks the visual language (violates repetition) | One icon style per deck; resize from corners |
| Ignoring **Remove Background** fringes | Halos of old background around cutouts | Zoom in and **Mark Areas to Remove** until the edge is clean |
| Forgetting to compress images | 40 MB decks bounce from email and stall presenters | **Picture Format > Compress Pictures > 150 ppi**, delete cropped areas at the end |
| SmartArt used where no relationship exists | Diagrams a list; confuses the logic | Use SmartArt only for process, cycle, hierarchy, relationship, matrix, or pyramid meaning |
| Sensitive data left in screenshots | Privacy or compliance incident | Cover with no-outline rectangles before presenting |
| Design Ideas applied blindly to data slides | Pretty layout that distorts the analysis | Take Designer spacing, hand-tune charts with Section 9 tools |
| Ignoring the Accessibility Checker | Deck fails inclusion and policy requirements | **Review > Check Accessibility** before every hand-off |
| Two accents fighting for attention | Neither number feels important | Exactly one accent element per slide |

---

## Key Takeaways

1. Contrast, Repetition, Alignment, and Proximity govern every slide decision; if a slide looks wrong, it is violating one of the four.
2. Assertion-evidence slides: the title is a full-sentence claim with a number, and one visual proves it. Titles alone should tell the story.
3. Typography at presentation distance: titles 36-44 pt, body 14-24 pt, line spacing 1.1-1.3, at most two typefaces, and nothing smaller than the back-row eye can read.
4. Color is for grouping, ranking, and branding: build a three-color palette plus neutrals, apply the 60-30-10 split, and never rely on color alone to carry meaning.
5. Shapes are design material: Align and Distribute for precision, Group for structure, and Merge Shapes (Union, Combine, Fragment, Intersect, Subtract) for custom geometry.
6. Icons should be one style, one metaphor, theme-recolored; SVGs and stock icons scale and recolor cleanly, and **Convert to Shape** unlocks piece-by-piece editing.
7. Images: crop before placing, never stretch (corner handles only), remove backgrounds for clean composites, and compress to 150 ppi before sharing.
8. SmartArt in the layout that matches meaning (Process, Cycle, Hierarchy, Relationship, Matrix, Pyramid) and **Home > Convert to SmartArt** is a ten-second upgrade from bullets.
9. Screenshots and screen clippings are evidence: capture exactly the region that matters, redact sensitive fields, and add one accent callout.
10. Guides, gridlines, Align, Distribute, and the Selection Pane create the invisible structure that makes a deck look professional; Design Ideas accelerates the polish, but dated looks (clip art, 3-D effects, stretched pictures) give a deck away every time.

---

## Further Learning

All URLs below were verified live during research for this module.

1. Presentation Guru: 5 Golden Rules for PowerPoint Design
   https://www.presentationguru.com/5-golden-rules-for-powerpoint-design/
2. Presentation Guru: The Assertion-Evidence Slide Structure
   https://www.presentationguru.com/the-assertion-evidence-slide-structure/
3. Presentation Guru (homepage and article library, ongoing slide design writing)
   https://www.presentationguru.com/
4. Think Outside the Slide (Dave Paradi's slide design and communication blog)
   https://www.thinkoutsidetheslide.com/
5. Microsoft Support: Make Your PowerPoint Presentations Accessible to People With Disabilities
   https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25
6. Duarte: Resources hub (guides, tools, and templates for presentation design)
   https://www.duarte.com/resources/
7. Duarte: Resources Blog (design and storytelling articles)
   https://www.duarte.com/resources/blog/
8. Duarte: Slidedocs Templates (document-style slide design templates)
   https://www.duarte.com/resources/guides-tools/slidedocs-templates/
9. Duarte: Tips for Crafting a Storytelling Presentation
   https://www.duarte.com/blog/tips-for-crafting-a-storytelling-presentation/
10. Duarte: Presenting Data Insights (visual design for data-heavy slides)
    https://www.duarte.com/presenting-data-insights/

---

*End of Module 03. Next: Module 04 (Charts, Data Visualization, and Tables).*


## FILE: 04-Tables-Charts-DataViz/04-tables-charts-dataviz.md

# Module 04: Tables, Charts & Data Visualization

> **Module number:** 04
> **Title:** Tables, Charts & Data Visualization
> **Level:** Intermediate
> **Prerequisites:** Module 01 (interface, slides, text boxes), Module 02 (shapes, formatting), Module 03 (images and SmartArt helpful but optional)
> **Estimated study time:** 90-120 minutes
> **Next module:** Module 05 (Transitions, Animation & Delivery)

---

## 0. Why This Module Matters

Numbers win arguments, but only when the audience can see the point. A wall of raw spreadsheet cells puts people to sleep; a well-chosen chart makes the conclusion obvious in three seconds. Tables and charts are the two workhorses of data storytelling in PowerPoint, and almost every business deck, classroom lecture, or pitch presentation needs at least one of them.

This module teaches you three skills in order:

1. **Structure**: building clean tables and inserting the right chart type.
2. **Style**: formatting both so they read instantly (and deleting the junk that hides the message).
3. **Honesty**: displaying data ethically so your visuals persuade without distorting.

By the end, you will choose chart types with intent, connect charts to Excel data correctly, and build simple infographic-style KPI callouts from shapes.

---

## 1. Creating and Formatting Tables

### What tables are for

A **table** is the right choice when the audience needs to look up specific values, compare exact numbers across a small grid, or read mixed text-and-number content (pricing tiers, feature matrices, schedules). Rule of thumb: **if the reader needs precision, use a table; if the reader needs a pattern or trend, use a chart.** Tables also beat charts when you have fewer than about 5 data points per series and no meaningful trend.

### Step-by-step: inserting a table

1. Click the **Insert** tab on the ribbon.
2. Click **Table**. A grid picker drops down.
3. Drag across the grid to select rows and columns (for example, 4 columns x 5 rows), or click **Insert Table...** and type exact numbers in the Columns and Rows boxes.
4. Click **OK** (if using the dialog) and the empty table appears on the slide with the cursor in the first cell.
5. Type your content. Press **Tab** to move to the next cell; **Shift+Tab** moves back. Pressing Tab in the last cell creates a new row automatically.

**Alternative route:** type your data in Excel first, select it, copy (Ctrl+C), then in PowerPoint use **Home > Paste** (or Ctrl+V). PowerPoint creates a table from the pasted cells.

### Step-by-step: structural edits (insert, delete, merge, split)

With the cursor inside the table, the **Table Design** and **Layout** contextual tabs appear on the ribbon.

- **Insert rows/columns:** Layout tab > **Insert Above**, **Insert Below**, **Insert Left**, or **Insert Right** (in the Rows & Columns group).
- **Delete:** Layout tab > **Delete** > Delete Columns / Delete Rows / Delete Table.
- **Merge cells:** select two or more cells, Layout tab > **Merge Cells**. Great for table titles spanning all columns.
- **Split cells or table:** Layout tab > **Split Cells** (specify columns and rows) or **Split Table** (splits above the selected row, useful for breaking a long table across two slides).
- **Distribute rows/columns evenly:** Layout tab > **Distribute Rows** / **Distribute Columns** so sizes are uniform.

### Step-by-step: table styles, banded rows, and manual formatting

1. Click anywhere in the table to select it.
2. Open the **Table Design** tab. The **Table Styles** gallery shows ready-made themes (light, dark, accent-colored).
3. Hover to live-preview, then click one to apply it. Use the scrollbar arrow at the gallery's right edge to see all styles.
4. In the **Table Style Options** group, toggle:
   - **Header Row** (emphasizes the first row, usually bold with a fill),
   - **Total Row** (emphasizes the last row for sums),
   - **Banded Rows** (alternating row shading so the eye tracks across long rows),
   - **First Column / Last Column** (emphasize label columns),
   - **Banded Columns** (same idea vertically).
5. Manual tweaks: select cells and use **Table Design > Shading** (fill color), **Borders** (add/remove border lines), or the mini toolbar and **Home** tab for font, size, color, and alignment.
6. Cell text alignment: Layout tab > **Align Top / Center / Bottom** and left/center/right options. Numbers conventionally go right-aligned or decimal-aligned; headers center or left.
7. **Cell margins and text direction:** Layout tab > **Cell Margins** (reduce to fit more text) and **Text Direction** (rotate text for narrow columns).

**Real-world examples**
- *Business:* a 3-column pricing table (Plan / Monthly cost / Features) with the middle plan shaded as "Most popular".
- *Education:* a lab schedule with merged header cells ("Week 1-2" spanning two date columns) and banded rows for readability.
- *Personal:* a household budget table where the total row is bold with a top border.

**Try it now:** Create a 4x5 table titled "YourCompany Inc Quarterly Sales". Columns: Quarter, North, South, Total. Fill it with fake numbers (for example, Q1: $10,000 / $7,500). Merge the top row as a title, apply a table style with banded rows, and bold the Total column.

---

## 2. Inserting Charts: The Chart Type Menu

### Step-by-step: inserting a chart

1. Click **Insert** tab > **Chart**.
2. The **Insert Chart** dialog opens with categories on the left.
3. Pick a chart type and subtype (preview appears on the right), then click **OK**.
4. PowerPoint inserts a sample chart AND opens a small **Excel-like data sheet** ("Chart in Microsoft PowerPoint") with placeholder numbers in rows and columns.
5. Replace the placeholder values with your own: click a cell and type. Change series names in the header row and categories in the first column.
6. Close the data sheet with the **X** in its corner. The chart updates instantly.
7. To reopen the data sheet later: right-click the chart > **Edit Data** (small sheet) or **Edit Data in Excel** (full Excel).

### The main chart types and when each earns its place

- **Clustered/Stacked Column:** vertical bars. Best for comparing values across categories (sales by region).
- **Clustered/Stacked Bar:** horizontal bars. Same job as column charts, but better when category labels are long (product names read horizontally).
- **Line:** trends over time. The default for anything with a time axis (months, years, quarters). Use for 3+ time points.
- **Pie:** parts of a whole. Only for composition where shares sum to 100% and you have 2-5 slices. Avoid beyond 5 slices or when comparing across groups.
- **Doughnut:** pie's cousin with a hole (can hold a center label like "Total: $40,000"). Same limitations as pie.
- **Area:** trend plus cumulative volume emphasis. Filled line charts; good for showing how a total grows over time and what composes it (stacked area).
- **Scatter (XY):** relationship/correlation between two numeric variables (ad spend vs revenue). Points plotted by X and Y values, no category axis.
- **Combo:** two chart types in one plot, typically columns plus a line on a secondary axis (monthly revenue as columns, profit margin % as line). Insert one chart type, then **Chart Design > Change Chart Type > Combo** at the bottom of the list.
- **Waterfall:** running totals with increases and decreases (revenue, minus costs, equals profit). Found under **Insert > Chart > Waterfall** (Office 2016 and later, including Microsoft 365).
- **Funnel:** stage-by-stage drop-off (leads > qualified > demos > closed). Also under the 2016+ chart set. Where a chart type is missing in an older PowerPoint, fake a funnel with stacked shapes or a stacked bar tapering down.

**Real-world examples**
- *Business:* quarterly sales columns with a trend line (combo) for the moving average.
- *Education:* a scatter chart of study hours vs quiz score to discuss correlation in class.
- *Personal:* a doughnut of monthly expense categories with the total spend in the center hole.

**Try it now:** Insert a clustered column chart. Replace the sample data with YourCompany Inc quarterly sales (Q1 $10,000, Q2 $14,000, Q3 $12,500, Q4 $18,000) for a single series named "Revenue". Close the sheet and note how the chart redraws.

---

## 3. Chart Chooser Logic: Which Chart for Which Story

Every chart answers one of four questions. Decide the question first, then pick the chart. This is the single highest-leverage habit in data visualization.

| Story intent | Question answered | Best chart types | Avoid |
|---|---|---|---|
| **Comparison** | Which is bigger? How do items rank? | Column, bar, bullet (shapes) | Pie for ranking |
| **Trend** | What is happening over time? | Line, area, column (few periods) | Pie, doughnut |
| **Composition** | What are the parts of the whole? | Pie (few parts), doughnut, 100% stacked bar/area | Pie with 8 slices |
| **Relationship** | Do two variables move together? | Scatter (XY), bubble | Line over categories |

### Decision rules in plain language

1. **Time on the axis?** Use a line chart. Always. Even with 4 quarters, a line implies continuity and makes slopes readable.
2. **Comparing categories with long names or many items?** Horizontal bar. The labels fit and the ranking reads top-to-bottom.
3. **Showing share of a whole with 5 or fewer parts that sum to 100%?** Pie or doughnut. Label with percentages directly on the slices and skip the legend.
4. **Showing share of a whole over time?** 100% stacked column or stacked area. Never a pie per time period (audiences cannot compare slices across pies).
5. **Two numeric variables, looking for correlation or outliers?** Scatter.
6. **A process losing volume at each stage?** Funnel, or a horizontal bar sorted descending.
7. **A waterfall of gains and losses building to a total?** Waterfall.
8. **Two different units on one slide (dollars and percentages)?** Combo chart with a secondary axis.

**Worked example (YourCompany Inc):** The CFO wants (a) "how did revenue trend this year?", (b) "which region leads?", (c) "how is revenue split by product?", and (d) "does ad spend predict revenue?". Answers: (a) line, (b) horizontal bar, (c) doughnut with 3 products, (d) scatter. Four questions, four different charts - resist reusing one chart for all of them.

**Try it now:** Write one sentence of story intent per slide idea ("show that South region is catching up"), then name the chart type you would use before inserting anything. Confirm each choice against the table above.

---

## 4. Editing Chart Data: The Embedded Excel Sheet

### How the data sheet works

When you insert a chart, PowerPoint creates an **embedded workbook** - a tiny Excel data file that lives inside your .pptx. The chart is a live view of that sheet.

### Step-by-step: editing data

1. Right-click the chart > **Edit Data**. The mini spreadsheet opens beside the slide.
2. Edit any cell; the chart updates as you type.
3. **Resize the data range:** the blue outline in the sheet marks the charted range. Drag the small square handle at the bottom-right corner to include more rows/columns, or drag the whole edge to move the range.
4. **Add a series or category:** just type into the next empty column or row and extend the range to include it.
5. **Remove a series:** delete its column values and shrink the range, or select the series in the chart and press Delete.
6. Want full Excel features (formulas, formatting)? Right-click > **Edit Data in Excel** to open the embedded workbook in the real Excel app.

**Real-world example:** a teacher keeps last semester's class average chart and, before the new term presentation, opens Edit Data and pastes the new cohort's scores over the old numbers. The chart style, colors, and labels stay untouched.

**Try it now:** On your sample column chart, add a second series named "Target" with values $11,000 per quarter. Extend the blue range to cover it and watch a second bar appear per quarter.

---

## 5. Linking vs Embedding Excel Data

### The two ways to connect PowerPoint to Excel

- **Embedding (default).** Copy cells in Excel and paste into PowerPoint (or Insert > Chart and type data). The data lives **inside** the .pptx. It never updates automatically and never breaks. File size grows slightly. This is right when the data is final or when you must email one self-contained file.
- **Linking.** Copy a range or chart in Excel, then in PowerPoint use **Home > Paste > Paste Special... > Paste link** and choose **Microsoft Excel Worksheet Object** or **Microsoft Excel Chart Object**. The slide stores only a **pointer to the source .xlsx file path**. When the source workbook changes and saves, PowerPoint can refresh the display.

### Step-by-step: creating a link and managing it

1. In Excel, copy the range or chart (Ctrl+C).
2. In PowerPoint, **Home** tab > click the **Paste** dropdown > **Paste Special...**
3. Select **Paste link** (radio button, bottom-left of the dialog), pick the object type, click **OK**.
4. To control update behavior: **File > Info > Edit Links to Files** (this command appears only when linked objects exist). Options:
   - **Update Now:** pull the latest values from the source immediately.
   - **Automatic update:** refresh every time the presentation opens.
   - **Break Link:** convert the object to a static snapshot (embedded image-like copy). Do this before distributing the deck.
   - **Change Source:** repoint the link if the .xlsx moved.
5. If the source file is missing when the deck opens, PowerPoint shows the last cached values and warns about the broken link - Fix it with Change Source, or Break Link to freeze the data.

**Link or embed? Quick chooser**
- Data changes weekly and the deck is re-shown often (ops review)? **Link.**
- Deck travels by email to people without your file share? **Embed**, or link now and **Break Link** before sending.
- Audit trail matters (the slide must match a saved workbook version)? **Link** so the source is the single truth.

**Real-world example:** YourCompany Inc runs a monthly business review. The analyst links the summary slide to `sales-master.xlsx` on the team drive; each month she updates the workbook, opens the deck, hits **Update Now**, and the slide is current in seconds.

**Try it now:** Make a tiny workbook with one column of numbers, copy it into PowerPoint twice: once with plain Ctrl+V (embedded) and once with Paste Special > Paste link. Change a number in the workbook and save. Use Edit Links to Files > Update Now and observe which copy changes.

---

## 6. Formatting Charts: Axes, Labels, Legends, Colors

Click a chart to select it. Two contextual tabs appear: **Chart Design** and **Format**.

### Step-by-step: adding and removing chart elements

1. Select the chart > **Chart Design** tab > **Add Chart Element** (top-left).
2. From the menu, toggle:
   - **Chart Title** and **Axis Titles** (name the units: "Revenue (USD)"),
   - **Data Labels** (values printed on marks; choose position: Center, Inside End, Outside End, Above),
   - **Legend** (place Right, Top, Bottom - bottom is most readable),
   - **Gridlines** (Major/Minor, horizontal and vertical - usually keep only major horizontal on column charts),
   - **Axes** (show/hide primary horizontal and vertical axes),
   - **Error Bars / Trendlines** (trendlines are gold for scatter and line charts: Add Chart Element > Trendline > Linear).
3. Shortcut: with the chart selected, click the green **+** button floating at its top-right corner to check/uncheck elements faster.

### Step-by-step: formatting axes and labels

1. Right-click the axis (for example, the vertical value axis) > **Format Axis...** The Format Axis pane opens on the right.
2. Useful settings:
   - **Bounds: Minimum / Maximum:** set exact axis endpoints (see Section 9 for ethics!).
   - **Units: Major / Minor:** control tick spacing (for example, major unit 5000).
   - **Number format:** choose currency, percentage, thousands separator, decimal places.
   - **Tick Marks and Labels:** hide tick marks for a cleaner look.
3. Data labels: right-click a label > **Format Data Label...** to show **Value**, **Category Name**, **Series Name**, **Percentage** (pie/doughnut), or a custom text box label. Use **Label Position** and number formats here too.
4. **Legend:** right-click > **Format Legend** to dock it inside/outside the plot and set font size (10-12 pt reads well).

### Step-by-step: coloring per point and chart templates

1. **One color per series:** click a bar once to select the series, click again to select a single point, then **Format** tab > **Shape Fill**. Use this to highlight one bar (for example, the current quarter) in dark blue and gray the rest.
2. **Series-level color:** click a mark once (whole series selected) and set Shape Fill, or use Chart Design > **Change Colors** for theme palettes.
3. **Save a chart template:** perfect a chart, then right-click its whitespace > **Save as Template...** and name it (for example, `YourCompany-Brand-Chart.crtx`). Reuse via **Chart Design > Change Chart Type > All Charts > Templates** folder.
4. **Format pane shortcuts:** right-click almost any chart part and pick the Format... item. Everything (fills, borders, gap width between columns, overlap of stacked series) lives in that pane. Gap width under **Series Options** controls bar thickness.

**Real-world examples**
- *Business:* highlight the one product line that missed target in red while the others stay brand blue.
- *Education:* axis title "Score (%)" with major gridlines at 20% intervals so students can read values quickly.
- *Personal:* a savings line chart with a linear trendline projecting the goal date.

**Try it now:** On your quarterly chart, add axis titles, place data labels Outside End formatted as currency with zero decimals, put the legend at the bottom, remove vertical gridlines, and color Q4 bars dark blue while the rest stay light blue. Save the result as a chart template.

---

## 7. Removing Chart Junk: The Data-Ink Ratio

Edward Tufte's **data-ink ratio** principle: every pixel of ink should show data. Ink spent on decoration is ink stolen from the message. Audiences decode cleaner charts faster and remember them longer.

### The junk checklist (delete these by default)

- **3-D effects, bevels, shadows, reflections:** they distort values and date the deck. Use flat 2-D always.
- **Heavy dark gridlines:** fade them to a light gray or remove them; keep at most major gridlines on one axis.
- **Redundant legends:** if each bar is labeled directly with its series name, the legend repeats information - delete it.
- **Redundant data labels on every mark** when the axis already carries the scale - label only the points that make the argument (first, last, best, worst).
- **Unnecessary axis lines, tick marks, and borders:** a thin baseline is enough on column charts.
- **Chart borders and plot-area fills:** make the background transparent or match the slide.
- **Default Office colors and fonts:** switch to your palette so the chart feels designed, not defaulted.
- **Exploding pie slices and drop shadows on pie charts:** decoration with no information.

### Step-by-step: a fast de-junk pass

1. Select the chart, press **Delete** on any element you cannot justify ("does this help answer the story question?").
2. Right-click gridlines > **Format Gridlines** > set Line color to very light gray, width 0.5-0.75 pt - or remove.
3. Right-click the chart area > **Format Chart Area** > **Fill: No fill**, **Border: No line**.
4. Right-click a data series > **Format Data Series** > set **Gap width** to 60-80% (bars a bit wider) and remove any effects (Effects icon > Shadow: None).
5. Reduce font sizes to a consistent 10-12 pt and one font family across title, axis, labels, legend.

**Real-world example:** a before/after audit of a YourCompany Inc slide: the "before" chart has 3-D tilted columns, rainbow colors, thick black gridlines, and a shadowed legend; the "after" is flat, two-tone, faint gridlines, direct labels. Audience comprehension time drops from several seconds to instant.

**Try it now:** Apply the junk checklist to one chart on your practice slide. Delete at least four items. Compare with a duplicate slide holding the "before" version.

---

## 8. Infographics from Shapes: Bullet Graphs and KPI Callouts

Not every visual needs the chart engine. PowerPoint shapes build lightweight infographics that stay crisp and editable.

### KPI callouts: big-number tiles

1. **Insert > Shapes > Rounded Rectangle**, draw a tile (for example, 2.5" x 1.5").
2. **Shape Fill** with your brand color (or white with a colored top bar drawn as a thin rectangle), **Shape Outline: No Outline**.
3. Add a text box on top (or right-click the shape > **Edit Text**) with:
   - Line 1: the metric label in small caps ("Quarterly Revenue").
   - Line 2: the number, very large and bold ("$54,500").
   - Line 3: a delta ("+12% vs Q3") in green (up) or red (down). Use **Insert > Symbol** or type "▲ / ▼" sparingly.
4. Group the pieces (select all, Ctrl+G) and duplicate the tile (Ctrl+D) to build a KPI strip of 3-4 tiles.

### Bullet graphs: bar + target + bands (built from shapes)

A bullet graph packs a value bar, a target marker, and qualitative bands (bad / OK / good) into one slim horizontal bar - Stephen Few's compact replacement for gauges.

1. Draw a wide background rectangle (the "performance bands" track), maybe 4" x 0.5".
2. Draw two or three thinner rectangles inside it with graded fills (light gray, mid gray, slightly darker) to represent poor/satisfactory/good ranges. Use **Shape Format > Align > Align Left** and **Distribute Horizontally** to tidy.
3. Draw the **actual value bar**: a rectangle of the same height family (say 0.3") filled with a strong dark color, width proportional to the value (for example, value 72 of max 100 = 72% of the track width).
4. Add the **target marker**: **Insert > Shapes > Line** (or a very thin rectangle, 0.04" wide, black), placed at the target position (for example, 80% of the track).
5. Label at the right: actual value in bold ("72"), target in small text ("target 80").
6. Group everything (Ctrl+G) and duplicate downward for a scorecard of metrics.

### Other shape-built infographic pieces

- **Progress bars:** rounded rectangle track + inner fill rectangle at X% width.
- **Simple funnels:** 3-5 trapezoids (Insert > Shapes > Trapezoid, resized narrower each step) with stage labels and counts.
- **Icon-plus-number rows:** Insert > **Icons** (Insert tab > Icons, or Insert > Pictures > Stock Images > Icons in newer builds), recolor to one accent, pair with a big number text box.

**Real-world examples**
- *Business:* an executive summary slide with four KPI tiles (Revenue $54,500, Pipeline $120,000, Win rate 32%, NPS 47) above three bullet graphs for quarterly goals.
- *Education:* a progress-bar row showing class assignment completion by week.
- *Personal:* a savings-goal bullet graph with bands for "behind plan / on plan / ahead".

**Try it now:** Build one KPI tile for "Quarterly Sales $54,500 +12%" and one bullet graph where the value bar reaches 72% and the target marker sits at 80%. Group each and align them side by side.

---

## 9. Ethical Data Display: Axes, Cherry-Picking, and Trust

A persuasive chart that misleads is a liability. Audiences forgive rough design; they do not forgive (or forget) being tricked. Three rules keep your visuals honest.

### Rule 1: Never truncate the value axis on bar or column charts

Bars encode value by **length/area**. Starting the vertical axis at 50 instead of 0 makes a 5% gap look like a 10x gap. Line charts of non-zero-based series can start above zero if the axis is clearly labeled and you are showing change, not magnitude - but bar and column charts must always start at zero.

- **Fix:** right-click the value axis > **Format Axis > Bounds > Minimum: 0** for bar/column charts.
- **If values are large and clustered** (say 95-100), prefer a line chart or dot plot over truncated bars.

### Rule 2: Show the whole story, not the cherry-picked slice

- Include all relevant time periods. If Q1-Q3 dipped and Q4 boomed, starting the axis at Q4 to claim momentum is cherry-picking.
- State the sample and date range in a subtitle ("All US regions, FY2025") so viewers know what is included and excluded.
- If you exclude an outlier, say why in a footnote.

### Rule 3: Match scale and area to real values

- **Pie and doughnut:** area is the message. Never explode or enlarge a favored slice to exaggerate it, and always make slices sum to 100% of one whole (do not mix "share of revenue" and "share of profit" in one pie).
- **Bubble and picture charts:** size scales by radius but eyes read area - keep radius proportional to value and label actual numbers.
- **Dual axes:** they can manufacture correlation. Label both axes clearly and keep the baseline relationship honest.
- **3-D charts:** perspective distorts values - banned outright (see Section 7).

### Bonus hygiene

- Label the source: "Source: YourCompany Inc internal sales data" in small gray text at the bottom.
- One message per chart; write the takeaway as the chart title ("South region grew 40% in Q4") instead of a generic title ("Sales by region").
- When uncertainty matters (small samples, forecasts), say so: add "projected" or error bars.

**Real-world example:** YourCompany Inc shows a revenue line chart of $48,000-$56,000 across four quarters. Sloppy version: y-axis from $45,000, colored as bars - a visual earthquake over a 6% swing. Honest version: a line chart with an honest scale, axis clearly labeled, title "Revenue steady, up 6% full year".

**Try it now:** Take any practice chart and deliberately break it (truncate the axis to exaggerate). Present "before and after" and write one sentence about how the truncated version could mislead a client.

---

## 10. Hands-On Practice Projects

1. **Quarterly Business Review Slide**
   Build one slide for YourCompany Inc: a formatted 5x4 sales table (four quarters x North/South/Total, values around $10,000 per quarter per region) above a clustered column chart of the same data.
   *Success criteria:* table has header row emphasis and banded rows; chart uses a table-derived embedded data sheet; data labels show currency; zero truncation (axis min = 0); one chart junk element removed; slide title states the takeaway.

2. **Chart Chooser Drill (4 slides)**
   Create four slides that answer: (a) revenue trend over 8 months, (b) ranking of 6 products by revenue, (c) revenue share of 3 products, (d) correlation between ad spend and leads. Insert the correct chart type on each with realistic fake data (for example, ad spend $2,000-$9,000, leads 40-180).
   *Success criteria:* each slide uses a distinct, appropriate chart type (line / horizontal bar / pie or doughnut / scatter); each chart has a descriptive takeaway title; scatter includes a linear trendline.

3. **Linked Live Report**
   Build a workbook `yourcompany-sales.xlsx` with monthly numbers, then create a slide containing (a) an embedded chart and (b) a Paste-link worksheet object to the same data. Update the workbook and refresh.
   *Success criteria:* both connection types present; Edit Links to Files shows one source; Update Now visibly refreshes only the linked object; the deck also exists in a "sent" copy with links broken (Break Link) and both copies render the same values.

4. **KPI Dashboard from Shapes**
   Build an executive summary slide with four KPI tiles (Revenue $54,500 +12%, Expenses $31,200 -4%, Margin 42% +2 pts, NPS 47 +5) and two bullet graphs (Quarterly sales: value 72 vs target 80; New customers: value 58 vs target 60) - all from shapes, no chart objects.
   *Success criteria:* all items built from shapes and grouped; consistent color logic (green delta up, red down); bullets include bands plus a distinct target marker; everything aligned on a grid (use Shape Format > Align tools).

5. **Ethical Makeover**
   Take a deliberately bad chart (truncated 3-D column chart with 8 pie-style colors, thick gridlines, and a legend duplicating data labels) and produce a corrected version on the same slide, with a one-line caption explaining the two biggest fixes.
   *Success criteria:* axis starts at zero (or converted to a line chart with an honest scale); 3-D and shadows removed; gridlines faded or deleted; legend redundancy resolved via direct labels; source line added ("Source: YourCompany Inc demo data"); caption names the two fixes.

---

## 11. Common Mistakes & Pitfalls

| Mistake | Why it hurts | Fix |
|---|---|---|
| Using a pie with more than 5 slices | Slices become uncompareable | Group small slices or use a bar chart |
| Truncated y-axis on bar/column charts | Exaggerates differences, misleads | Set axis Minimum to 0 (Format Axis > Bounds) |
| 3-D charts and bevels | Distorts values, looks dated | Use flat 2-D always |
| Editing the sample numbers but not the series names | Legends say "Series 1, Series 2" | Edit the header row in the data sheet |
| Forgetting to extend the blue data range | New columns of data do not appear in the chart | Drag the range corner to include new data |
| Sending a deck with live links to a missing source | Broken-link warnings, stale values | Use Edit Links to Files > Break Link before distribution |
| Legend plus direct data labels on every mark | Redundant ink, cluttered chart | Keep one labeling system, delete the other |
| One chart trying to show comparison AND trend AND composition | Message gets muddled | Split into two charts, one question each |
| Rainbow default color scheme | No hierarchy, nothing stands out | One accent color for the key series, grays for the rest |
| Typing numbers as text in the data sheet | Chart plots nothing or wrong | Re-enter values as numbers, check number formatting |
| Table rows without banding or borders on dense data | Readers lose their place row-to-row | Enable Banded Rows in Table Design |
| Exploding pie slices to "emphasize" | Area distortion reads as a larger share | Keep all slices flush; emphasize with color instead |

---

## 12. Key Takeaways

- **Question first, chart second.** Comparison, trend, composition, relationship: name the story, then pick the chart type that answers it.
- **Tables for precision, charts for patterns.** Small grids and mixed text/number content belong in tables (banded rows, merged headers, table styles).
- **Line for time, horizontal bar for long labels, pie/doughnut only for 5-or-fewer parts of one whole, scatter for relationships, combo for dual units, waterfall/funnel for bridges and drop-off.**
- **Every chart has a live embedded Excel sheet.** Right-click > Edit Data to change values; drag the blue range when data grows.
- **Link for live updates, embed for portability.** Paste Special > Paste link points at a file; Edit Links to Files handles Update Now, Change Source, and Break Link. Break links before shipping the deck.
- **Format for reading:** axis titles with units, direct data labels on the marks that matter, faded or removed gridlines, per-point color to spotlight one item, and chart templates (.crtx) to standardize.
- **Chase the data-ink ratio:** no 3-D, no shadows, no redundant legends or labels. Decoration is noise.
- **Shapes build infographics too:** KPI tiles, bullet graphs with value bar + target marker + bands, progress bars, and shape funnels, all grouped and aligned.
- **Ethics are a feature:** bar and column charts always start at zero, show the full time range, disclose sources and samples, and never distort area to flatter the story.

---

## 13. Further Learning

- PowerPoint help and support hub (tables, charts, and troubleshooting articles): https://support.microsoft.com/en-us/powerpoint
- Microsoft Learn training for PowerPoint (free guided modules): https://learn.microsoft.com/en-us/training/
- Microsoft Create templates (charts, dashboards, and infographic starting points): https://create.microsoft.com/


## FILE: 05-Transitions-Animations/05-transitions-animations.md

# Module 05: Transitions & Animations

> **Module number:** 05
> **Title:** Transitions & Animations
> **Level:** Intermediate+
> **Prerequisites:** Modules 01-04 (PowerPoint basics, slide layout, text and shapes, images and visual design). Comfort with slide sorter view and selecting objects on a slide.
> **Estimated study time:** 90-120 minutes (plus practice projects)
> **Next module:** Module 06 (Presenting with Confidence: Slide Show, Presenter View, and Delivery)

---

## 1. Transitions vs Animations: The Conceptual Difference

Every PowerPoint motion effect belongs to exactly one of two families, and confusing them is the single most common source of "why is my deck doing that?" frustration.

**Transitions** happen *between slides*. A transition is the visual effect used when the whole slide changes: the outgoing slide leaves, the incoming slide arrives, and the effect describes that swap. If you select slide 7 and apply a Push transition, the Push happens when you move from slide 6 to slide 7. A slide with "No Transition" simply cuts from the previous slide instantly, like a film cut.

**Animations** happen *on a slide*, to individual objects *while that slide is on screen*. A bullet list flying in line by line, a company logo spinning, an arrow traveling along a path to point at a chart: all animations. Animations never affect how slides change; they affect what happens after a slide has already arrived.

A useful mental model: transitions are the doors between rooms; animations are the furniture moving inside a room.

**Why the distinction matters in practice:**

1. **Different tabs.** Transitions live on the **Transitions** tab. Animations live on the **Animations** tab. If you are on the wrong tab, the options you need do not exist and you will think the feature is missing.
2. **Different selection targets.** Transitions apply to whole slides (selected in the slide thumbnail pane or Slide Sorter). Animations apply to selected objects (placeholders, text boxes, shapes, pictures, charts, SmartArt).
3. **Different playback rules.** Transition timing is governed by "Advance Slide" (On Mouse Click / After). Animation timing is governed by Start modes (On Click / With Previous / After Previous) plus delay, duration, and repeat. Both use seconds, but they run on separate clocks.
4. **Different design risks.** Over-using transitions makes navigation feel slow and gimmicky. Over-using animations makes content hard to follow. Restraint rules differ slightly (see Section 12).

**Real-world examples:**

- *Business:* A quarterly review deck uses one quiet Fade transition throughout, but animates each revenue chart so bars grow one region at a time while the presenter narrates.
- *Education:* A history lesson pushes slides left-to-right like a timeline, with no object animations at all except a map route drawn with a motion path.
- *Personal:* A wedding slideshow uses a gentle Dissolve transition between photos and one Fade entrance on each caption.

**Try it now:** Open any deck with at least three slides. Click slide 2's thumbnail, open the **Transitions** tab, and apply **Push**. Start the slide show (F5), advance from slide 1 to 2, and watch the whole slide move. Exit, then on slide 2 click the title text box, open the **Animations** tab, and apply **Fade**. Run the show again and notice that the effect fires on the title alone, inside slide 2. You have now seen both families fire separately.

---

## 2. The Transition Gallery: Fade, Push, Wipe, and Friends

Open the **Transitions** tab. The **Transition to This Slide** gallery shows the most-used effects; click the **More** arrow (the line with a triangle at the gallery's bottom-right) to see them all, grouped as Subtle, Exciting, and Dynamic Content.

The effects worth knowing by name:

- **None (Cut).** Instant change. Perfectly respectable and invisible. Great default for dense business decks.
- **Fade.** The old slide fades out as the new one fades in. Smooth, calm, professional. The safest "I want something but not too much" choice.
- **Push.** The new slide physically shoves the old one off screen. Use **Effect Options** to choose the direction (From Bottom reads like a page reveal, From Right reads like moving forward).
- **Wipe.** The new slide is uncovered like a squeegee pass. Effect Options gives direction. Good for "revealing" a build.
- **Morph.** The star of this module. Covered fully in Section 3.
- **Cover / Uncover.** One slide slides over the other (Cover) or the old one slides away (Uncover). Similar to Push but the second slide does not move.
- **Split / Box / Wheel / Clock.** Radial or shutter reveals. Fine occasionally, distracting in a loop.
- **Dissolve / Random Bars / Honeycomb / Vortex / Ripple / Glitter / Shred / Switch / Flip / Gallery / Cube / Doors / Window / Origami / Ferris Wheel / Conveyor / Pan / Prestige / Reveal.** The "Exciting" and "Dynamic Content" groups. Most are too busy for business use; test before committing.

Two gallery entries look similar but behave differently: **Dynamic Content** transitions (like Pan or Switch) move only the *content* between the slide's shared background, so background branding stays put while content slides. Standard transitions move the entire slide, background included.

**Exact steps, basic application:**

1. In the thumbnail pane, click the slide you want to affect (the transition plays when *entering* this slide).
2. Open the **Transitions** tab.
3. In **Transition to This Slide**, click an effect (or **More** to open the full gallery, then click one).
4. The slide previews immediately in the editing canvas. Click **Preview** (far left of the Transitions tab) to replay it.

**Apply one transition to the whole deck:** pick your effect, then in the **Timing** group click **Apply To All**. Every slide now enters with that effect. The status bar's transition icon tells you which slides carry a transition.

**Different transitions per slide:** select slide A only and apply Fade; select slide B only and apply Push. Never click **Apply To All** afterward (it spreads the current slide's settings everywhere). To batch-apply, Ctrl+click thumbnails, then click one gallery effect; useful for giving only section headers a distinctive Push.

**Real-world example (business):** YourCompany Inc's investor deck uses **None** for the 40 data slides (fast, no nonsense) but **Push From Right** on the four section dividers so the audience feels chapters turning. Total design impact: high. Total gimmickry: zero.

**Try it now:** Build a three-slide deck of blank slides with just titles: Start, Middle, End. Set slide 2 to Push (From Right) and slide 3 to Fade. Do not use Apply To All. Run the show (F5) and verify: slide 2 pushes in, slide 3 fades in. Then click Apply To All while slide 3 is selected and re-run to see what happens to slide 2.

---

## 3. Morph: The Killer Feature

**Morph** is the transition that makes people ask "how did you do that?" It looks at the outgoing slide and the incoming slide, finds objects that exist on both (matched by identity or by name), and smoothly tweens their position, size, rotation, and even color from one state to the other. If a circle is large and blue on slide 5 and small and red on slide 6, Morph animates it shrinking and recoloring along the way.

**How matching works:**

1. **Same object, copied.** If you duplicate a slide and then move/resize/recolor an object on the copy, PowerPoint knows it is the same object and morphs it. This is the reliable path.
2. **Name matching (the `!!` trick).** For objects that are *not* copies of each other, give both objects the exact same name in the **Selection Pane** (Home > Select > Selection Pane), and prefix the name with two exclamation marks, for example `!!Logo` on slide 1 and `!!Logo` on slide 2. The `!!` prefix forces Morph to match them even across different slide copies. Ordinary matching (without `!!`) works for same-named objects too, but `!!` is the documented forcing mechanism and is more reliable.
3. **Word matching.** Morph can match individual words between two text boxes, so a word can travel across the slide while the rest of the text fades. Enable via **Transitions > Effect Options > Words** (when available for the effect).

**The duplicate-slide Morph technique (the core workflow):**

1. Build your starting state on slide N exactly as you want it (object placed, sized, colored).
2. Right-click slide N's thumbnail and choose **Duplicate Slide**. Everything is now the "same object" on slide N+1.
3. On slide N+1, move, resize, rotate, recolor, or delete the objects into the *ending* state. Delete an object on N+1 and Morph will fade it out; add a new object on N+1 and Morph fades it in.
4. With slide N+1 selected, go to **Transitions** and click **Morph**. Set **Effect Options** to **Objects** (morph matched objects), **Words** (match words in text), or **Characters** (match individual letters).
5. Run the show across the two slides and watch.

**Shared-element motion (branding that stays put):** place your logo or slide furniture (footer, page number, side band) on the slide master or on both slides with `!!` names. Morph will hold the logo still or gently drift it while the content moves around it. This is exactly how polished product-launch videos look: the logo anchors, the content flows.

**Effect Options for Morph:**

- **Objects:** morphs matched shapes/pictures. The everyday choice.
- **Words:** matched words glide; unmatched words fade. Great for headline transformations ("Q3" becoming "Q4" by editing just the digit).
- **Characters:** individual letters fly to their new positions. Mesmerizing for a single headline; chaos for a paragraph.

**Real-world examples:**

- *Business:* Slide 12 shows a full org chart. Slide 13 is a duplicate where everything except the Sales team is dimmed and the Sales subtree has been enlarged to fill the slide. Morph zooms smoothly into the team being discussed instead of a jarring cut to a new diagram.
- *Education:* A chemistry deck morphs a single molecule shape from "reactant layout" to "product layout" across two duplicated slides, so bonds appear to reorganize.
- *Personal:* A travel photo grows from a thumbnail in a collage (slide A) to full-bleed on slide B via duplicate-and-resize Morph.

**Pitfalls:** Morph only fires between *consecutive* slides. It will not run if you hyperlink-jump past its target slide. Very complex slides with dozens of matched objects can morph into visual soup; morph one idea at a time.

**Try it now:** Insert a circle on a blank slide and duplicate the slide. On the copy, drag it to the opposite corner, resize it, change its fill. Apply **Morph** (Effect Options: Objects) to the second slide and present: the shape travels and transforms. Bonus: give two independently drawn shapes the same `!!Hero` name in the Selection Pane and confirm `!!` matching works.

---

## 4. Transition Effect Options, Duration, and Advance Timing

Once a transition is applied, the **Timing** group on the Transitions tab controls how it plays. These three or four small boxes matter more than the choice of effect itself.

**Effect Options** (left of the Timing group, active only when a transition is selected) changes the transition's *variant*: direction for Push/Wipe/Uncover (From Bottom/Left/Right/Top), Smoothly vs Through Black for Fade, Objects/Words/Characters for Morph, and so on. Always open this after picking an effect; the default direction is not always the right one. Push "From Right" signals forward progress; "From Left" reads as going back. Match the direction to your narrative.

**Duration** sets how long the transition takes, in seconds (format: `mm:ss.ss`; you can type `01.25` for 1.25 seconds). Rules of thumb:

- 0.5-0.75 seconds: snappy. Good for cuts-with-style like a fast Push.
- 1.0-1.5 seconds: comfortable. The sweet spot for Fade and Morph in most decks.
- 2.0+ seconds: slow and cinematic. Use only when the transition *is* the moment (a dramatic reveal), and only once or twice in a deck.

A deck of 60 slides at 2 seconds each is two full minutes of your talk spent purely on transitions. Do that math before setting durations.

**Advance Slide: On Mouse Click vs After:**

- **On Mouse Click** (default, usually kept): the slide changes only when the presenter clicks (or presses Space/Right Arrow). This is what you want for live talks, because the presenter controls pacing.
- **After [time]:** PowerPoint advances to the next slide automatically after the specified time elapses. Use this for self-running kiosks, lobby loops, photo slideshows, or a conference booth display.
- You can enable *both*: then whichever comes first wins. Presenters often set "After 00:05" as a safety net so a forgotten click does not stall a loop, while still being able to click ahead early.

**Apply To All** (rightmost button in the Timing group) copies the current slide's transition effect, effect option, duration, and advance settings to every slide in the presentation. It is a blunt instrument: it also overwrites per-slide customizations you may have made earlier. Workflow tip: decide and apply your house transition *first*, then customize individual slides afterward.

**Building a self-running loop (exact steps):**

1. Apply your transition to all slides (**Apply To All**).
2. In **Timing**, enable **After** and set `00:05`, uncheck **On Mouse Click** if you want a hands-free loop.
3. Go to **Slide Show > Set Up Slide Show** and check **Loop continuously until 'Esc'**.
4. Optionally use **Set Up Show > Browsed at a kiosk (full screen)** for unattended displays.

**Real-world example:** YourCompany Inc's trade-show booth runs a 12-slide loop: every slide uses Fade, Duration 1.00, Advance After 00:07, looping until Esc. Nobody has to touch it all day.

**Try it now:** Take any five-slide deck. Set Fade on slide 1, Duration `01.00`, then click **Apply To All**. Now set slide 3 alone to Morph with Duration `02.00` and confirm Apply To All is *not* clicked. Turn on **View > Show Transition Sound**-free playback via **Preview** and time the difference.

---

## 5. The Animation Pane: Your Control Room

The **Animation Pane** is where all serious animation work happens. Open it from the **Animations** tab, **Advanced** group, **Animation Pane** button. A docked panel appears on the right listing every animated object on the current slide, in playback order, with its effect type, start mode, and a timeline.

**Reading the pane:**

- Each row is one animation effect (an object with several effects has several rows).
- The icon at the left shows the category (green star: Entrance; yellow: Emphasis; red: Exit; dotted path: Motion Path).
- Tags like `1`, `2`, `3` mark click groups: everything tagged `1` plays on the first click. Rows with a "with previous" chain icon play automatically.
- The gray bars on the right are a time ruler: bar length = duration, bar position = start time. At a glance you see what moves together and what waits.

**Exact steps to build a sequence with the pane:**

1. Select an object on the slide.
2. **Animations >** choose an effect (or **Add Animation** to append without replacing; more on that in Section 6).
3. The effect appears in the Animation Pane.
4. In the **Timing** group set **Start** (On Click / With Previous / After Previous), **Duration**, and **Delay**.
5. To reorder: drag rows up/down in the pane, or select a row and click the re-order arrows at the pane's bottom (**Move Earlier** / **Move Later**).
6. To fine-tune: right-click a row for **Effect Options** (direction, sound, after-animation color), **Timing** (duration, delay, repeat, trigger), or **Remove**.
7. Click **Play From** or **Play** at the top of the pane to preview without entering slide show mode.

**Pane conveniences:** **Move Earlier / Move Later** beats dragging. Double-click a row for the multi-tab Effect Options dialog (Effect, Timing, Text Animation), which still exposes settings the ribbon hides: per-paragraph text animation and repeat counts.

**Real-world example (education):** A teacher builds a five-step solution on one slide. Five text boxes, each with an Entrance Fade, tagged 1 through 5 so each step appears on its own click while the class attempts the next step first. The Animation Pane shows the five click groups at a glance during rehearsal.

**Try it now:** Put three shapes on a blank slide. Select all three and apply **Appear**. Open the Animation Pane: three rows, tagged `1`, `2`, `3` (one click each). Set row 3's Start to **After Previous** so it follows row 2 automatically. Preview: two clicks total instead of three. This is the fix for click-heavy slides.

---

## 6. Animation Types: Entrance, Emphasis, Exit, Motion Paths

Select an object, open the **Animations** tab, and the gallery shows **Entrance** effects. Crucial gotcha: clicking a gallery tile *replaces* the object's existing animation. To add a *second* effect to the same object, you must use **Add Animation** (Advanced group) and pick from that dropdown. This trips up everyone once; it is the most-repeated pitfall in this module.

**Entrance (green):** the object arrives (Appear, Fade, Fly In, Float In, Split, Wipe, Zoom, Grow & Turn, Bounce, and more). Use these to reveal content in speaking order.

**Emphasis (yellow):** the visible object pulses attention (Spin, Grow/Shrink, Transparency, Fill/Font Color, Teeter, Wave). Use sparingly: one Grow/Shrink on a key number is good; five spinning arrows is noise.

**Exit (red):** the object leaves (Disappear, Fade, Fly Out, Float Out, Zoom, Split, Wipe). Exits clean the stage: an old chart flies out before its replacement flies in, avoiding stacked slides.

**Motion Paths (green dotted):** the object travels a preset (Lines, Arcs, Turns, Shapes, Loops) or drawn path (**Custom Path** freehand waypoints, **Scribble** freehand). See Section 11.

**Exact steps, adding multiple effects to one object:**

1. Select the object.
2. **Animations > Add Animation >** pick an **Entrance** (for example Fade). A row appears in the pane.
3. Keep the object selected. **Animations > Add Animation >** pick an **Emphasis** (for example Grow/Shrink). A second row appears *below* the first.
4. Again **Add Animation >** pick an **Exit** (for example Fade). Third row.
5. In the Animation Pane set starts: Entrance = On Click (or After Previous), Emphasis = After Previous with a Delay, Exit = After Previous.
6. Right-click the Grow/Shrink row > **Effect Options > Size** = 110%, check **Auto-reverse** so it swells and returns.

**Real-world examples:**

- *Business:* A pricing slide: three price cards Fade in one by one (Entrance), the recommended card does a single Grow/Shrink to 105% (Emphasis) when the presenter says "our recommendation", then a strike-through line Wipes across the old price (Entrance on the line) as the new price Fades in.
- *Education:* A timeline: milestone dots Appear along an arrow as each era is discussed; the "current era" dot Teeters once for emphasis.
- *Personal:* A quiz slide where wrong answers Fly Out (Exit) and the right answer Zooms in (Entrance).

**Try it now:** Create one rounded rectangle labeled "Key Insight". Give it, via Add Animation only: Entrance > Zoom, Emphasis > Grow/Shrink (110%, auto-reverse), Exit > Fade. Set Zoom = On Click, Grow/Shrink = After Previous with 1s delay, Exit = After Previous with 2s delay. Preview. If any effect overwrote another, you clicked the gallery instead of Add Animation; fix and note the difference.

---

## 7. Start Modes and Full Timing Control

Every animation row has a **Start** setting in **Timing** group of the Animations tab, and this setting is what separates a smooth build from a click-fest.

**Start modes:**

- **On Click:** waits for a mouse click (or keypress) to fire. Creates a numbered click group. Use when the reveal must match something you say at an unpredictable moment.
- **With Previous:** starts at the exact same moment as the previous animation row in the pane. Chain several together and one click launches the whole group in unison. When a row is the first on a slide and set to With Previous, it plays automatically when the slide appears (no click at all).
- **After Previous:** starts when the previous row finishes. Perfect for automatic sequences: fade A, then fade B, then fade C, each after the last.

**Duration** = how long the effect itself takes. **Delay** = dead time before the effect starts after its trigger point. Together they control rhythm. A tasteful cascade: three text boxes, Fade, Duration 0.50, Delay 0.00 / 0.25 / 0.50, all With Previous. One click, a gentle left-to-right ripple.

**Repeat** (hidden in the full Timing dialog: right-click a row > **Timing** tab > **Repeat** dropdown): None, 2, 3, 4, 5, 10, Until Next Click, Until End of Slide. "Until End of Slide" with a subtle Emphasis like Transparency pulse is a classic "look here" for a slide that sits on screen during a long discussion. Do not combine repeat with large motions.

**Other Timing dialog gems:**

- **Start ... on click of:** the trigger selector (Section 10).
- **Rewind when done playing:** snaps the object back to its pre-animation state (looping demos).
- **Smooth start / Smooth end** (Effect tab): easing. Keep some; 100% at both ends makes fast effects sluggish.
- **Sound** (Effect tab): leave None. Animation sounds lose rooms fast.

**Real-world example:** YourCompany Inc's countdown slide: the number "3" then "2" then "1" then "Launch!". Each number has Exit > Disappear (After Previous, Delay 0.75) and the next number's Entrance > Zoom (After Previous, Delay 0.00). One click at the top and the whole countdown runs hands-free.

**Try it now:** Put four text boxes on a slide. Set all four to Entrance > Fade, Start: With Previous, Duration 0.50, Delays 0.00, 0.30, 0.60, 0.90. Preview: one click should ripple all four. Then change box 3 to Start: On Click and observe it become a separate numbered click group in the pane.

---

## 8. Animating Text by Paragraph

Bullets that appear all at once kill pacing; bullets that appear one at a time are how presenters control attention. PowerPoint's **By Paragraph** animation gives you this per-line build without splitting text into separate boxes.

**Exact steps:**

1. Select the text placeholder or text box (selecting the whole object animates all its text together by default).
2. **Animations >** pick an Entrance (Fade, Fly In, Wipe). All lines animate as one unit initially.
3. Right-click the effect in the Animation Pane > **Effect Options** (or **Timing**) > the **Text Animation** tab.
4. Set **Group text** to **By 1st Level Paragraphs** (or By 2nd/3rd Level for deeper builds, or As One Object / All at Once).
5. Optionally check **In reverse order** to build from the last bullet to the first.
6. Decide the click behavior: uncheck **Automatically after [n] seconds** and leave "Start On Click" if you want one bullet per click; or set the effect's Start to After Previous with the text animation tab's auto-advance for a fully automatic reveal.
7. OK, then preview in the Animation Pane. Each paragraph shows as its own step, each tagged with its click number.

**Sub-bullets:** with Group text = By 2nd Level Paragraphs, a top-level bullet and its children can arrive as one beat while other top-level bullets arrive separately. Ideal for agenda slides where each section heading brings its own detail lines.

**Per-line animation effects:** in Effect Options for Fly In or similar, use **Animate text: As one object / All at once / By word** for character-level builds. "By word" with Fade produces a gentle typing reveal popular in keynote-style decks. Use it for one or two sentences only.

**Reverse direction gotcha:** for Wipe or Fly In on a bulleted list, Effect Options direction (From Bottom, etc.) interacts with paragraph order. Preview after every change; do not trust the default.

**Real-world examples:**

- *Business:* An agenda slide with five items, each arriving On Click as the chair introduces that agenda item. The pane shows click groups 1-5, giving the presenter full control.
- *Education:* A definition slide where the term appears first (separate text box, With Previous) and the definition fades in By Word while the teacher reads it aloud.
- *Personal:* A toast or vows slide where each line Fades in After Previous, 0.5s duration, 0.8s delay, so the text advances at reading speed with zero clicks.

**Try it now:** Paste five bullets about YourCompany Inc values into one placeholder. Apply Entrance > Fly In (From Bottom). In the Animation Pane, right-click the effect > Effect Options > Text Animation > Group text = By 1st Level Paragraphs. Press F5 on the slide and click through. Then switch Start to After Previous and set the text to advance automatically, and admire the difference between a click-build and a self-running build.

---

## 9. Animating Charts: Series, Category, and Build Steps

Charts animate as multi-part objects, and this is one of the highest-value techniques in business presenting: the chart grows while you narrate, instead of appearing complete and static.

**Exact steps:**

1. Click the chart to select it as a whole.
2. **Animations >** pick an entrance that suits the data: **Wipe** (From Bottom for columns rising; From Left for bars extending rightward), **Fade** for lines/pies, or **Zoom** for doughnuts.
3. The entire chart animates as one unit at first. To build it, right-click the chart's row in the Animation Pane > **Effect Options > Chart Animation** tab (this tab appears only for charts).
4. In **Group chart** choose one of:
   - **As One Object:** whole chart at once.
   - **By Series:** one data series (for example "2025 revenue") per step. Best for line charts and for comparing product lines over time.
   - **By Category:** one category (for example "Q1") per step, bringing all series' points for that category together. Best for clustered columns when you narrate quarter by quarter.
   - **By Element in Series** / **By Element in Category:** the most granular; every bar or point individually. Dramatic but easy to overdo and slow to play.
   - **By Element in Category, leaving gridlines/background first:** a sub-option, **Start animation by drawing the chart grid** (checkbox), makes the axes arrive before the data. Keep this checked so the chart frame exists before bars fly in.
5. Set the overall effect's Start mode. For a fully narrated build use **After Previous** with a small delay per step; for presenter-controlled steps use **On Click** (each category/series becomes its own click group).
6. Preview and check the pane: a built chart shows sub-rows nested under the chart effect.

**Direction matters:** Wipe From Bottom makes columns grow up from the axis (the only correct choice for column charts); From Top makes them hang downward, which misrepresents growth. For horizontal bar charts use Wipe From Left. For line charts use Wipe From Left so the line draws through time.

**Limitations and fixes:**

- One chart effect = one effect type (no Fade on series 1 plus Fly In on series 2). For that, build the chart from shapes or overlay two transparent-background charts.
- XY scatter and combo charts sometimes build oddly; test first and fall back to As One Object + Fade.
- Pie/doughnut: By Category reveals one slice per click around the wheel.

**Real-world example:** YourCompany Inc's revenue review: a clustered column chart of four quarters across three regions. Animation: Wipe From Bottom, Group chart = By Category, Start = On Click, "Start animation by drawing the chart grid" on. The CFO clicks once per quarter and talks; the chart never shows the answer before the commentary.

**Try it now:** Insert a clustered column chart (three categories, two series, fake data). Animate Wipe From Bottom, Effect Options > Chart Animation = By Category with gridlines first, Start = After Previous. Play it, then switch to By Series and judge which build tells the better story.

---

## 10. Trigger Animations: Click a Shape to Fire an Effect

Ordinary animations fire on slide-level clicks in fixed order. **Triggers** break the order: a specified effect fires only when the audience/presenter clicks (or hovers over) a specific object on the slide. Triggers turn a static slide into a small interactive widget: quiz answers, tabbed content, reveal-on-demand detail.

**Exact steps:**

1. Select the object that will *receive* the animation (for example a hidden answer text box). Give it an effect via **Animations > Add Animation**.
2. In the **Timing** group open the **Trigger** dropdown (or right-click the effect row in the Animation Pane > **Timing** > **Triggers** button).
3. Choose **On Click of** and pick the *trigger* shape from the list (for example a button labeled "Show answer"). The pane reorganizes: the effect nests under a **Trigger: [shape name]** header.
4. Optionally make the trigger shape itself look clickable: fill it like a button, add a soft shadow.
5. Test in Slide Show view (triggers do not fully exercise in the pane preview): clicking the button fires the effect; clicking anywhere else does not.

**Multiple effects per trigger:** point several effects at the same trigger, or wire several triggers on one slide for a clickable menu. To reset a reveal, add a triggered Exit or use **Rewind when done playing** with auto-reverse.

**Hover triggers:** **On Mouse Over** suits kiosks; in live talks a stray mouse wave misfires it. Prefer click triggers.

**Hygiene:** name trigger shapes and targets in the **Selection Pane** ("Btn-Answer2", "Txt-Answer2"). Trigger menus list shape names; "Rounded Rectangle 47" is unfindable.

**Real-world examples:**

- *Business:* A product comparison slide with three feature tabs along the top; clicking each tab triggers its feature panel to appear and the previous one to exit (each tab carries two triggered effects).
- *Education:* A quiz slide: "Why did the Roman Empire fall?" with four answer buttons; clicking each triggers "Correct/Incorrect" feedback text boxes. The teacher can take answers in any order.
- *Personal:* A "reveal the gender / reveal the price" party slide: one big button, one triggered Zoom entrance on the hidden text.

**Try it now:** Draw a button labeled "Reveal" and a text box reading "Q4 revenue: +18% YoY". Animate the text box Entrance > Zoom, then set its trigger to **On Click of: [the button shape]**. Press F5: clicking empty slide space should do nothing; clicking the button reveals the text. Bonus: add a second triggered effect, Exit > Fade, wired to a second button named "Hide".

---

## 11. Animation Painter and Custom Motion Paths

**Animation Painter** copies every animation (effects, timing, order) from one object and pastes it onto others. It lives on the **Animations** tab, **Advanced** group, and it is the cure for "I animated one bullet perfectly and now have 40 more".

**Exact steps:**

1. Select the object whose animation you want to copy (the source).
2. **Animations > Animation Painter** (single copy) or **double-click Animation Painter** (sticky mode, keeps applying until you press Esc).
3. Click each target object. Each gets the source's full animation set and timing.
4. Press Esc to release the painter.

**Format Painter** (Home) copies *appearance*; Animation Painter copies *behavior*. Use both (Format for look, Animation for motion) to build template-quality decks in minutes.

**Pitfall:** Animation Painter *replaces* a target's existing animations; it does not merge. Paint first, customize second. Painting across slides works: double-click the painter, scroll the thumbnails, click targets on other slides.

**Custom motion paths:**

1. Select the object.
2. **Animations > Add Animation > Motion Paths** at the bottom of the dropdown.
3. Choose a preset (Lines, Arcs, Shapes, Loops) or **Custom Path** (click-click-click to place waypoints, double-click to end) or **Scribble** (draw freehand).
4. The path appears on the object: a dotted line with a green start triangle and red end triangle. Drag the red end marker to reposition the destination, drag path points to reshape, use the yellow diamond handles (on some paths) to bend arcs.
5. Effect Options controls: **Locked / Unlocked** (does the path move with the object if you drag it later?), **Reverse Path Direction**, and for sequences, **Path End** snap choices (Object Center / Slide Center etc. for "Locked" relative options).
6. Timing: duration = travel time. A 3-inch move at 1.0s reads as gentle; at 0.25s it is a dart. Delay it so it travels *after* the object appears.

**Drawing tips:** straight travel = Lines + Effect Options direction (cleaner geometry). For curves, Custom Path with sparse clicks (PowerPoint smooths the polyline). Scribble suits one-off flourishes like circling a chart value.

**Real-world example (education):** A physics projectile demo: a ball (motion path: Arc, 1.5s, Smooth end) travels a parabola across a slide while dashed measurement text Fades in after it lands. Reusable every semester; Animation Painter copies the ball's arc onto the second demo object in seconds.

**Try it now:** Animate one text box Entrance > Fade (Start: With Previous) and then Emphasis > Grow/Shrink, exactly as you like. Use double-click Animation Painter and apply that pair to four other objects on the slide. Check the pane: five identical rows. Then draw a Custom Path on a shape and preview the shape gliding your drawn route.

---

## 12. Animation Restraint: The 3-Second Rule and What Not To Do

The difference between an amateur animated deck and a professional one is almost entirely *how little* animation is used. Motion is seasoning, not the meal.

**The 3-second rule:** any object's entire animated entrance should finish within about 3 seconds of its cue, and ideally within 1-2. Your audience came for the content; if they watch a 5-second Bounce, they are not listening to you. If you cannot say the sentence that accompanies the animation before it finishes, shorten the duration.

**When NOT to animate:**

- **Reference material.** Slides people will read, keep, or screenshot (appendix, data tables, spec sheets): no animation at all. Animation makes exports and printed handouts behave inconsistently and forces viewers to click to see content that should be visible at a glance.
- **When the slide must be scanned.** Executive summary slides work because eyes jump around the page. Revealing content piece by piece fights that.
- **When the deck will be distributed as a file.** Recipients clicking through an unfamiliar deck with 300 animations will experience chaos. Prefer static slides and let your email do the narrating.
- **Every slide, every object.** If literally everything moves, nothing stands out. A useful budget: animate on perhaps 1 in 4 slides, and only where movement adds meaning (sequence, causality, reveal, emphasis).
- **When it delays the punchline.** If the chart's conclusion is the point, show the whole chart and talk. Builds are for *process* (timeline, method steps, quarterly progression), not for withholding.

**Tacky effects to avoid (the hall of shame):**

- **Bounce** on more than zero objects per deck. (One playful use in an all-hands is the limit.)
- **Swivel, Grow & Turn, Spiral, Boomerang, Zip, Gunshot sound effects.** 1999 called.
- **Any sound effect** tied to an animation in a professional setting.
- **Checkerboard, Blinds, Comb, Random Bars, Honeycomb** as transitions between ordinary content slides. They scream clip art.
- **Vortex / Origami / Ferris Wheel / Conveyor** transitions. Theatrical to the point of parody; use only in deliberately playful personal projects.
- **Text By Character on paragraphs.** Fine for one 5-word headline; torture for a paragraph.
- **Automatic transitions faster than 2 seconds on dense slides.** The audience is still reading when the slide leaves.
- **Rotating logo loops with repeat Until End of Slide.** A spinning badge looks like a broken screensaver.

**The tasteful palette:** Entrance Fade / Wipe (From the direction content grows) / Appear / subtle Fly In / Zoom for one-off reveals; Morph between closely related slides; one Grow/Shrink for a key number; durations 0.5-1.5s; delays creating 0.2-0.3s cascades.

**Real-world example:** Two decks cover the same YourCompany Inc strategy. Deck A: every bullet Bounces in at 2s, every slide has a different transition, the org chart Vortexes. Deck B: static slides throughout, one Morph zoom into the priority team, one chart that builds By Category. Deck B will be called "polished" every time.

**Try it now:** Audit a recent deck with a stopwatch: click through every animated slide and count seconds lost to motion. If motion exceeds roughly 10% of slide-show time, halve durations, then delete half the effects. Re-run and compare your reaction.

---

## 13. Troubleshooting Animation Order and Playback

Things will misbehave. Here is the diagnosis table in prose.

**"Effects fire in the wrong order."** Rows fire top to bottom in the Animation Pane. Drag rows or use **Move Earlier / Move Later**. If two effects should run together but do not, the second is On Click or After Previous where it should be With Previous.

**"Everything waits for clicks" (click hell).** Check Start modes and click-group tags. Convert cascades to With Previous / After Previous with delays so one click runs a whole beat; keep animated slides to 2-3 click groups.

**"My second animation replaced the first."** You clicked the gallery instead of **Add Animation**. Re-create the first effect, then always use Add Animation for extras.

**"Morph didn't work."** Checklist: Morph is on the *incoming* slide; the slides are consecutive (no hyperlink jumps); objects are duplicates or share `!!` names; grouping matches across slides; Effect Options set to Objects/Words/Characters as intended.

**"Plays in preview but not in the slide show."** Usually a trigger waiting on a shape click (check the pane's Trigger headers), or the object sits behind a full-bleed shape.

**"Trigger won't fire."** Click the trigger shape precisely in Slide Show view. Make it big and opaque. Verify Timing > Triggers points to the right shape name (rename shapes first). Ungroup if the trigger is a grouped shape.

**"Chart build steps are missing."** The Chart Animation tab appears only when the chart object itself carries the effect. Re-select the chart, re-apply, reopen Effect Options. Combo/bubble charts may build only As One Object.

**"Text By Paragraph isn't splitting."** You animated the inner text box instead of the placeholder, or each bullet is its own text box (separate objects). Animate the real placeholder with By 1st Level Paragraphs, or standardize per-box animation with Animation Painter.

**"The deck lags on the presenting laptop."** 3D-ish transitions (Vortex, Prestige, Origami) and heavy bitmap effects are GPU-hungry. Simplify effects, compress pictures (Picture Format > Compress Pictures), close other apps, and always test on the actual machine and projector.

**"Audio behaves differently elsewhere."** Avoid animation sounds entirely. For deliberate narration use Insert > Audio, embed the media, and check File > Info > Optimize Media Compatibility before sharing.

**"I inherited a deck where everything moves."** Strip all transitions at once: Transitions > **None** > **Apply To All**. For animations, select rows in the Animation Pane and press Delete, slide by slide. Skip macro quick-fixes right before a meeting.

**Real-world example:** Five minutes before the YourCompany Inc board meeting, the build looks broken on the projector laptop: each bullet waits for its own click and the presenter expected auto-advance. Fix: select all rows in the pane for the text effect, set Start = After Previous, leave the first bullet On Click. One setting, show saved.

**Try it now:** Intentionally break a slide: apply three effects using the gallery (overwriting each other), then add a proper multi-effect object with Add Animation, then set one effect to a trigger on a tiny shape. Now fix the slide in under 3 minutes using only the Animation Pane. Repeat until fast; this is the skill that matters under pressure.

---

## Practice Projects

**Project 1: The Morph Product Zoom**
Build 4 slides for YourCompany Inc's imaginary "Widget Pro". Slide 1: a hero layout with five product images and the logo. Slides 2-4: duplicates where, each time, one product image grows to fill the slide while others fade away and the `!!Logo` holds position. Success criteria: (a) Morph applied to slides 2-4 only; (b) logo motion is minimal/anchored; (c) full sequence plays as one continuous zoom with zero clicks between slides 2-4 (set After advance or just click through and judge smoothness); (d) no object jumps or pops between states.

**Project 2: The Quarterly Chart Story**
One slide containing a clustered column chart of four quarters x two product lines for YourCompany Inc. Animate so the axes/grid draw first, then each quarter builds left to right (Wipe From Bottom, By Category), advancing On Click so the presenter can narrate. Add a second effect on a "Q4" callout shape: Entrance Zoom, Start After Previous, Delay 0.5s. Success criteria: (a) columns grow upward from the axis; (b) exactly 4 click groups; (c) the callout arrives automatically after the last category; (d) no effect replaces another (all added via Add Animation).

**Project 3: The Interactive Quiz Slide**
One slide, one question about imaginary company policy, four answer buttons, and four feedback text boxes (three "Not quite", one "Correct!"). Each feedback box is triggered by its own button and each also has an Exit effect triggered by a "Reset" button. Success criteria: (a) feedback only appears when its button is clicked, in any order; (b) Reset hides all revealed feedback; (c) trigger shapes clearly look clickable; (d) all shapes carry readable names in the Selection Pane.

**Project 4: The Self-Running Lobby Loop**
Six slides advertising YourCompany Inc's imaginary open day: title, three highlights, closing call to action. Requirements: one tasteful transition family (Fade or gentle Push) at 1.0s applied to all; at most 2 animated slides using cascades (With Previous + 0.25s delays, 0.5s durations); set every slide to advance After 00:07; enable Loop continuously until Esc in Set Up Slide Show. Success criteria: (a) hands-free playback cycles forever; (b) total transition time across the deck is under 7 seconds; (c) no effect on the deck would embarrass you in a boardroom; (d) text is fully readable within the 7-second window (test with a stopwatch and a friend).

**Project 5: The Build-and-Cleanup Timeline**
One slide showing a 5-step project timeline for the imaginary "Atlas Rollout". Requirements: 5 step boxes with Wipe entrances in sequence (After Previous cascade), 5 connector arrows with Appear/After Previous between them, then at the end the 2 "completed" steps get an Emphasis (Grow/Shrink 105%, auto-reverse) and the whole set's detail text fades in By Paragraph. Use Animation Painter to replicate the step animation across all five boxes. Success criteria: (a) the timeline visually "draws" left to right when one click starts it; (b) total build time under 8 seconds (3-second rule per beat); (c) the pane is cleanly ordered with explicit Start modes on every row; (d) Animation Painter was used at least once.

---

## Common Mistakes & Pitfalls

| Mistake | What goes wrong | Fix |
|---|---|---|
| Clicking the Animations gallery to add a 2nd effect | Replaces the first animation on the object | Always use **Add Animation** for 2nd+ effects |
| Applying a transition, then clicking Apply To All "to be safe" | Overwrites per-slide transition choices | Use Apply To All only right after picking your house transition |
| Expecting Morph to match objects that were drawn separately | Morph silently fades instead of gliding | Duplicate the slide, or give both objects the same `!!` name in the Selection Pane |
| Animating columns with Wipe From Top | Bars hang downward and misrepresent growth | Effect Options > From Bottom for column charts |
| Every bullet set to On Click | Presenter click-fests, dead air between reveals | Use With/After Previous cascades with 0.25s delays for most builds |
| Setting transition/animation durations too long | Audience watches motion instead of listening | 0.5-1.5s durations; the 3-second rule |
| Animating slides meant for handouts/reading | Recipients must click to reveal content they need to scan | Leave reference/appendix slides static |
| Adding sound effects to animations | Instant credibility loss in professional rooms | Sound: None. Always. |
| Group text left as "As One Object" when per-bullet reveal was wanted | Whole list arrives at once | Effect Options > Text Animation > By 1st Level Paragraphs |
| Using Bounce / Swivel / Spiral / Vortex anywhere serious | Deck reads as amateur clip art | Stick to Fade, Wipe, Appear, subtle Fly In, Zoom, Morph |
| Renaming nothing before wiring triggers | Trigger menu lists "Rectangle 47", wires to the wrong shape | Name shapes first (Btn-Reveal, Txt-Answer) in the Selection Pane |
| Morph on non-consecutive slides or across hyperlink jumps | Transition never fires | Morph only between adjacent slides in normal advance order |
| Animating the chart but losing the Chart Animation tab | No build-step controls | Re-select the chart object itself, then Effect Options |
| Chart gridlines not set to draw first | Data flies in over an empty void | Check "Start animation by drawing the chart grid" |
| Animation Painter applied to an object that already has effects | Existing effects silently wiped | Paint first, customize after |
| Never testing on the presenting laptop | Lag, stutter, font or aspect surprises | Full run-through on the actual machine + projector |
| Transition time adding up across a big deck | Minutes lost to pretty wipes | Cut the deck's total transition time budget (aim under 1 minute for 40+ slides) |
| Auto-advance After set too short on text-heavy slides | Slide leaves while audience reads | After time >= seconds needed to read the densest slide |
| Trigger shape tiny or hidden behind other objects | Clicks "do nothing" in the show | Big, opaque, clearly button-like trigger shapes |
| Animating every object "because we can" | Nothing stands out; audience fatigue | Budget: animate where motion adds meaning, roughly 1 slide in 4 |

---

## Key Takeaways

1. **Transitions move between slides; animations move objects within a slide.** Two families, two tabs, two timing systems. Keep them straight and half the confusion disappears.
2. **Morph is the highest-impact tool in the box.** It matches objects by copy-identity or by `!!` names in the Selection Pane, and the duplicate-slide technique (build state A, duplicate, rearrange to state B, apply Morph to the second slide) is the workflow that produces professional motion graphics without leaving PowerPoint.
3. **The gallery replaces; Add Animation appends.** This single distinction prevents the most common animation bug in the world.
4. **Start modes are the choreography.** On Click creates deliberate, presenter-controlled reveals; With Previous and After Previous (with delays) create smooth automatic cascades. Aim for few click groups per slide.
5. **Duration and delay are design choices, not trivia.** 0.5-1.5s durations, 0.2-0.3s cascade delays, and the 3-second rule keep motion invisible and content dominant.
6. **Text builds By Paragraph and charts build By Category/By Series** turn static walls of information into narration-paced stories. For column charts, Wipe From Bottom, gridlines first.
7. **Triggers create interactivity**: quizzes, tabs, reveal-on-demand. Name your shapes first, keep trigger buttons big, and prefer click over hover for live talks.
8. **Animation Painter clones behavior; Format Painter clones appearance.** Paint first, customize second.
9. **Restraint is the real pro move.** Static where content must be scanned; motion only where it adds sequence, causality, or emphasis; never a sound effect; never Bounce.
10. **Test everything in Slide Show view on the presenting machine.** The Animation Pane preview does not exercise triggers, Morph between slides, or real playback timing.

---

## Further Learning

- Microsoft PowerPoint support hub (transitions, animations, and everything else, with searchable articles): https://support.microsoft.com/en-us/powerpoint
- Microsoft 365 Training for PowerPoint (free modules and learning paths from the source): https://learn.microsoft.com/en-us/training/
- Create.microsoft.com (design ideas, templates, and inspiration for tasteful visual polish): https://create.microsoft.com/

*Practice beats reading here: rebuild Projects 1 and 2 until the Morph zoom and the chart build feel effortless, and you will have the motion vocabulary that covers 95% of real-world decks.*


## FILE: 06-Media-Interactivity/06-media-interactivity.md

# Module 06: Media & Interactivity

**Module number:** 06
**Title:** Media & Interactivity
**Level:** Advanced
**Prerequisites:** Modules 01-05 (interface basics, slide creation, text and shapes, images and icons, themes and layouts). A working microphone and (optionally) speakers or headphones. Sample video and audio files help but are not required.
**Estimated study time:** 90-120 minutes (plus project work)
**Next module:** 07 - Collaboration & Review (or the next module in your learning path)

This module turns a static slide deck into a rich, self-guided experience. You will embed and edit video, add narration and music, record your screen, wire up hyperlinks and action buttons, build interactive navigation with Zoom slides, create audience-specific Custom Shows, run kiosk-style self-playing presentations, export decks as MP4 or GIF, and make all of it accessible.

---

## 1. Inserting Video: This Device, Online, and Stock

**What it is.** PowerPoint lets you embed video from three sources: files saved on your computer ("This Device"), streamed online video (YouTube and other web sources), and Microsoft's built-in Stock Videos library. An embedded video becomes part of the .pptx file (when inserted from this device), while online video stays a live web link that needs an internet connection during the show.

**Step-by-step (video from this device):**
1. Select the slide where the video should appear.
2. Go to `Insert > Video > This Device`.
3. Browse to your file (MP4 is the safest format; MOV and AVI also work but are larger) and click `Insert`.
4. Drag the video frame into position and resize from the corner handles so it does not distort.
5. A new `Playback` tab appears in the ribbon whenever the video is selected.

**Step-by-step (online video):**
1. In your browser, copy the embed link or page URL of the video (for YouTube, use `Share > Copy` or copy the URL from the address bar).
2. In PowerPoint: `Insert > Video > Online Video`.
3. Paste the URL into the dialog and press `Enter` or click the search icon.
4. Select the thumbnail that appears and click `Insert`. The video frame shows a poster thumbnail with a play overlay.

**Step-by-step (stock video):**
1. `Insert > Video > Stock Videos`.
2. Search or browse categories (backgrounds, nature, technology, and so on).
3. Select one or more clips and click `Insert`. Stock clips are licensed for use in documents and presentations.

**Real-world examples.**
- *Business:* YourCompany Inc's quarterly review opens with a 20-second stock clip of a city skyline while music plays, then transitions to the agenda.
- *Education:* A biology teacher embeds a short cell-division clip from this device so it plays even if the classroom Wi-Fi fails.
- *Personal:* A wedding slideshow includes an online video message from a relative who could not attend.

**Format tips.** MP4 with H.264 video and AAC audio is the most compatible combination across Windows, Mac, and exported video. If a video refuses to play, re-encode it to MP4 with a free tool rather than fighting codecs.

**Try it now.** Insert any MP4 from your device on a blank slide, then insert one Stock Video on another slide. Compare the two: click each and note which ribbon tabs (`Video Format`, `Playback`) appear and whether the stock clip behaves differently from your file.

---

## 2. Video Editing: Trimming, Fade In/Out, and Poster Frames

**What it is.** PowerPoint includes a lightweight video editor so you do not need external software for common fixes: trimming off the dead seconds at the start or end, softening abrupt starts and stops with fades, and choosing the still frame that shows before playback (the poster frame).

**Step-by-step (trim):**
1. Select the video, then open the `Playback` tab.
2. Click `Trim Video`. The Trim Video dialog opens with a timeline.
3. Drag the green `Start Marker` and red `End Marker` to the moments you want, or type exact `Start Time` and `End Time` values (format MM:SS.t).
4. Click `Play` inside the dialog to preview, then `OK`. The original file is untouched; only the playback window changes.

**Step-by-step (fade in and fade out):**
1. With the video selected, open `Playback`.
2. Set `Fade In` (for example 1.00 second) and `Fade Out` (for example 1.50 seconds) in the editing group.
3. Preview in Slide Show mode (`F5`) to judge the feel. Short fades (0.5-2 seconds) look professional; long fades feel sluggish.

**Step-by-step (poster frame):**
1. Select the video and open `Playback > Poster Frame` (or `Video Format > Poster Frame` depending on version).
2. Choose `Image from File`, `Stock Images`, `Online`, or `Capture from Current Frame`. "Capture from Current Frame" grabs the frame currently shown under the playhead, which is ideal after trimming to the perfect moment.
3. The chosen still is what your audience sees before anyone presses play.

**Real-world examples.**
- *Business:* Trim a 3-minute product demo down to the 45 seconds that matter, add a 1-second fade in, and set the poster frame to the hero shot of the product.
- *Education:* Trim a recorded lab demonstration to just the experiment portion so class time is not wasted scrubbing.
- *Personal:* Set the poster frame of a travel video to the best sunset shot so the deck looks polished even if nobody plays the clip.

**Try it now.** Trim 5 seconds off the start of any video, add a 1-second fade in and 1-second fade out, and set the poster frame to a captured frame near the middle. Present the slide and watch how much more polished the clip feels.

---

## 3. Video Playback Options

**What it is.** The `Playback` tab controls how a video behaves during the show: whether it plays automatically or waits for a click, whether it expands to full screen, whether it loops, and whether the frame is hidden between plays. Getting these right is what separates a deck that "just works" from one where the presenter scrambles to find the play button live.

**The Playback ribbon controls:**
- `Start:` dropdown with `In Click Sequence`, `Automatically`, and `When Clicked On`. "In Click Sequence" plays when you advance to the animation step; "Automatically" plays as soon as the slide appears; "When Clicked On" waits for a click on the video object itself.
- `Play Full Screen:` the video expands to fill the entire screen during playback, then returns to the slide.
- `Loop until Stopped:` repeats the clip endlessly until you press `Esc` or advance.
- `Hide While Not Playing:` makes the video frame invisible except during playback (great for background loops).
- `Rewind after Playing:` snaps back to the start when finished, so a second play begins from the top.
- `Volume:` Low, Medium, High, or Mute.

**Step-by-step (auto-playing full-screen clip):**
1. Select the video, open `Playback`.
2. Set `Start > Automatically`.
3. Check `Play Full Screen`.
4. Optionally check `Loop until Stopped` and `Rewind after Playing`.
5. Test with `Slide Show > From Current Slide` (or `Shift+F5`).

**Step-by-step (click-to-play clip):**
1. Select the video, open `Playback`.
2. Set `Start > When Clicked On` so only a click on the video itself triggers it, and ordinary slide-advance clicks do not.
3. Enlarge the video frame to make the click target obvious.

**Animation tab alternative.** For finer control, select the video and open the `Animations` tab: the `Play`, `Pause`, and `Stop` effects can be added to the Animation Pane and triggered by click or by "With Previous"/"After Previous" for choreographed playback with animations.

**Real-world examples.**
- *Business:* A looping muted product video ("Hide While Not Playing" off, "Loop until Stopped" on) runs behind a trade-show kiosk slide.
- *Education:* A vocabulary video is set to "When Clicked On" so the teacher controls exactly when it plays during discussion.
- *Personal:* A highlight reel plays full screen automatically the moment its slide appears at a family reunion.

**Try it now.** Set one video to start automatically, loop, and play full screen. Then duplicate the slide and change it to "When Clicked On" with no full screen. Present both slides and feel the difference in control.

---

## 4. Inserting Audio: Music, Narration, and Sounds

**What it is.** PowerPoint supports audio in three roles: background music that spans slides, recorded narration (voice-over) per slide or for the whole deck, and sound effects triggered by clicks. The `Insert > Audio` menu offers `Audio on My PC`, `Stock Audio` (in current versions), and `Record Audio` (a quick in-app voice memo).

**Step-by-step (music that plays across slides):**
1. `Insert > Audio > Audio on My PC`, pick your MP3 or WAV, and click `Insert`. A speaker icon appears with a progress bar below it.
2. With the audio selected, open the `Playback` tab.
3. Set `Start > Play in Background` (this one-click preset sets automatic start, "Play Across Slides", "Loop until Stopped", and "Hide During Show"), or configure manually:
   - `Start > Automatically`
   - Check `Play Across Slides`
   - Check `Loop until Stopped` for long background loops
   - Check `Hide During Show` to hide the speaker icon
4. Set `Volume > Low` or `Medium` so music never drowns out a presenter or narration.

**Step-by-step (record narration per slide):**
1. Go to `Slide Show > Record Slide Show` (choose `Record from Current Slide` or `Record from Beginning`).
2. The Recording Studio view opens with a camera preview (toggle it off if unwanted), a big red `Record` button, and per-slide notes.
3. Click `Record`, speak for the current slide, then advance with the arrow keys or on-screen arrows. Timings and ink are captured too.
4. Click `Stop`, review with `Play`, then `Close` (X). Each slide now holds a narration audio object and an advance timing.
5. Selectively delete narration on a slide by selecting the speaker icon it contains and pressing `Delete`.

**Step-by-step (quick inline recording):**
1. `Insert > Audio > Record Audio`, name the clip, click `Record`, speak, click `Stop`, then `OK`. Useful for one-line verbal notes or a spoken greeting.

**Sound on click.** Select any shape or icon, then `Insert > Action > Play sound` and pick a built-in sound or `Other Sound` for your own file. This ties audio to a specific interactive object (covered further in Section 7).

**Real-world examples.**
- *Business:* YourCompany Inc's leave-behind deck has narration on every slide so prospects can "attend" the pitch asynchronously.
- *Education:* A flipped-classroom lecture records explanations over each slide; students watch at home and arrive ready for exercises.
- *Personal:* A memorial slideshow plays one meaningful song across all slides at low volume.

**Try it now.** Record a one-sentence narration on two consecutive slides with `Record Slide Show`, then play the two slides in Slide Show mode and confirm the audio advances automatically with the timings. Next, insert any music file and set it to `Play in Background` at low volume.

---

## 5. Compressing Media

**What it is.** Media bloat is the number-one cause of giant, slow, unemailable decks. A handful of untrimmed 1080p clips can push a .pptx past 200 MB. Compressing media re-encodes every embedded audio and video file at a lower quality tier and discards trimmed portions.

**Step-by-step:**
1. Go to `File > Info`.
2. Click `Compress Media` (it only appears when the presentation contains media). Choose a quality level:
   - `Full HD (1080p)` - quality preserved for large screens.
   - `HD (720p)` - the sweet spot for laptops, projectors, and webinars.
   - `Standard (480p)` - smallest files, fine for email attachments and on-screen review.
3. PowerPoint processes each clip and reports the before/after size per media item and in total. Keep the dialog open to compare.
4. Save the file (`Ctrl+S`). Note: compression is lossy. Save a copy first if you may need original quality later (`File > Save a Copy`).

**Related size hygiene.** Deleting cropped image areas (`File > Options > Advanced > Image Size and Quality > Discard editing data`) and avoiding embedded duplicate clips both shrink files. Trim first, then compress: trimmed-away footage is discarded during compression, compounding the savings.

**Real-world examples.**
- *Business:* A 185 MB partner deck compresses to 31 MB at HD so it passes the mail server's 50 MB limit.
- *Education:* A lecture deck with 12 embedded clips drops from 400 MB to 60 MB so it loads fast on school tablets.
- *Personal:* A vacation slideshow shrinks enough to upload to shared cloud storage without hitting quota.

**Try it now.** Open any deck with video, note its file size on the `File > Info` screen, run `Compress Media` at `Standard (480p)`, and record the new total. Undo is not available after saving, so work on a copy.

---

## 6. Screen Recording and Screenshots

**What it is.** PowerPoint's built-in screen recorder captures part or all of your screen with optional narration and drops the result straight onto the current slide as an editable video. The Screenshot tool grabs any open window or a custom region and inserts it as a picture. Both avoid the "export from another tool, then import" dance.

**Step-by-step (screen recording):**
1. Go to `Insert > Screen Recording` (on the `Insert` tab, far right).
2. PowerPoint minimizes and shows a dock at the top of the screen: `Record` (red circle), `Stop`, `Select Area`, `Audio` toggle, `Record Pointer` toggle.
3. Click `Select Area` and drag a marquee around the region you want (a browser window, a spreadsheet, a demo app). If you skip this, the entire screen is captured.
4. Turn `Audio` on if you want voice-over from your microphone. Note: PowerPoint's screen recorder captures microphone audio, not system audio, in most configurations; narrate rather than relying on app sounds.
5. Click `Record` (or press `Win+Shift+R`). Perform the demo. Pause with `Win+Shift+U` if needed.
6. Stop with `Win+Shift+Q` or the dock's `Stop` button. The capture appears on the current slide as a video object.
7. Trim, fade, and set playback exactly as in Sections 2 and 3.

**Step-by-step (screenshot):**
1. `Insert > Screenshot`.
2. Pick a window from the `Available Windows` gallery for a clean instant capture, or click `Screen Clipping` to drag-select a region of the last active window (PowerPoint minimizes while you clip).
3. The result is a picture: crop it (`Picture Format > Crop`), add a border, or apply a shadow like any image.

**Real-world examples.**
- *Business:* Record a 60-second walkthrough of YourCompany Inc's internal dashboard so sales reps can embed it in proposals.
- *Education:* Capture the exact dialog boxes of a statistics tool step by step so students can compare their screens to yours.
- *Personal:* Screenshot a booking confirmation and clip just the reservation number region for a trip-planning deck.

**Try it now.** Use `Insert > Screenshot > Screen Clipping` to grab one region of any open app. Then use `Insert > Screen Recording` to record 10 seconds of mouse movement over that app with audio off, and trim the clip to 5 seconds.

---

## 7. Hyperlinks: Internal, External, and Email

**What it is.** A hyperlink turns any text, shape, or picture into a clickable jump: to another slide in the deck, to a web page, to another file, or to an email compose window. Hyperlinks are the simplest building block of interactive, non-linear decks.

**Step-by-step (link to another slide):**
1. Select text or an object.
2. Press `Ctrl+K` (or `Insert > Link`).
3. Under `Link to:`, choose `Place in This Document`.
4. Pick the target slide from the list (best from `Slide Titles` view) and click `OK`.
5. Test in Slide Show mode: clicking the object jumps to that slide.

**Step-by-step (link to a web page):**
1. Select the object or text, press `Ctrl+K`.
2. Choose `Existing File or Web Page`, type or paste a full URL including `https://`, click `OK`.
3. Ctrl+click behavior: in Normal view links require Ctrl+click to follow; in Slide Show mode a plain click works.

**Step-by-step (email link):**
1. `Ctrl+K > E-mail Address`.
2. Type the address (for example `sales@yourcompany.example`) and an optional subject.
3. Clicking it in Slide Show mode opens the audience member's mail client with the fields prefilled.

**Clean design without underlines.** Hyperlinked text is underlined and recolored by the theme by default, which looks noisy in large doses. For clean looks:
- Apply links to whole shapes instead of text (`Ctrl+K` with the shape selected): no underline, and the click target is much bigger.
- Or select linked text, then `Home > Text Shadow`/font color adjustments to restyle it. To fully control link colors, edit theme colors: `Design > Variants > Colors > Customize Colors`, and set `Hyperlink` and `Followed Hyperlink` to tasteful tones (for example dark blue and gray).
- Shape buttons with a short label ("Learn more", "See pricing") read better than raw URLs printed on the slide.

**Tip: ScreenTips.** In the `Insert Hyperlink` dialog, click `ScreenTip` and type a short hover description ("Opens our pricing page"). It helps in kiosk mode.

**Real-world examples.**
- *Business:* YourCompany Inc's proposal deck links each agenda item to its detail slide, and the closing slide has one large "Email us" button.
- *Education:* A course overview links each topic card to the slide section that covers it, letting students jump to what they need.
- *Personal:* A recipe deck links each course to its full-page recipe slide.

**Try it now.** On one slide, add a rounded rectangle labeled "Next topic" and hyperlink it to slide 3 of your deck. Then add text reading "Contact us", hyperlink it to an email address with a subject line, and restyle it so no underline shows. Test both in Slide Show mode.

---

## 8. Action Buttons and Action Settings

**What it is.** Action buttons are ready-made shapes (arrows, home, information, film, sound, and so on) that come pre-wired with an action: jump to next/previous/first/last slide, open a URL, run a program, play a sound, or run a macro. `Action Settings` exposes the same wiring for any shape or object you already have, so your own brand-styled buttons can behave like action buttons.

**Step-by-step (insert an action button):**
1. `Insert > Shapes` and scroll to the `Action Buttons` category at the bottom of the gallery.
2. Draw the button (for example `Action Button: Home`) on the slide.
3. The `Action Settings` dialog opens automatically. Choose the `Mouse Click` tab (and optionally `Mouse Over` for hover behavior).
4. Select `Hyperlink to` and pick `Next Slide`, `Previous Slide`, `First Slide`, `Last Slide`, `End Show`, `Custom Show`, `URL`, `Other PowerPoint Presentation`, or `Other File`.
5. Optionally check `Play sound` and pick a sound. Click `OK`.

**Step-by-step (wire an existing shape):**
1. Select your own rounded rectangle or icon.
2. Go to `Insert > Action` (the `Action Settings` dialog opens with identical options).
3. Set `Hyperlink to > Slide...` and pick an exact target slide for full control.
4. Repeat the button on the Slide Master (`View > Slide Master`) so navigation appears on every slide automatically.

**Real-world examples.**
- *Business:* A self-running booth deck gets a persistent "Menu" home button on every slide so staff can reset it to the main menu between visitors.
- *Education:* Quiz slides use "Next question" and "Answer" buttons wired to hidden answer slides.
- *Personal:* A digital guestbook at a party has a "Sign the form" button that jumps to the feedback slide.

**Try it now.** Insert an `Action Button: Back or Previous` and wire it to `Previous Slide`. Add a second shape of your own design and use `Insert > Action` to wire it to `First Slide`. Present and click both.

---

## 9. Zoom Navigation: Slide Zoom, Section Zoom, Summary Zoom

**What it is.** Zoom (Insert > Zoom) creates thumbnail navigation that lets a presenter dive into slides or whole sections and return to an overview, like a mini website inside your deck. There are three types: `Slide Zoom` (jump to specific slides), `Section Zoom` (jump into a whole section and return), and `Summary Zoom` (PowerPoint auto-builds a menu slide of your sections). Note: Zoom is a modern PowerPoint feature; it exists in PowerPoint 2019/365 on Windows and Mac, and Zoom links degrade gracefully to ordinary jumps in older versions.

**Step-by-step (Section Zoom, the most common):**
1. Organize your deck into sections first: right-click between slides in the thumbnail pane and choose `Add Section` (for example "Products", "Pricing", "Team").
2. `Insert > Zoom > Section Zoom`.
3. Check the sections you want and click `Insert`. Thumbnail cards appear on the current slide.
4. Arrange the cards into a menu grid. With a card selected, the `Zoom` tab offers:
   - `Zoom Background` (makes the card's slide background transparent so thumbnails sit cleanly on your design).
   - `Return to Zoom` (checked: after showing that section, you bounce back to the menu; unchecked: you continue to the next slide).
   - `Change Image` (swap the thumbnail for a branded picture).
5. Resize and style the cards like pictures (borders, shadows, soft edges).

**Step-by-step (Slide Zoom):** `Insert > Zoom > Slide Zoom`, check individual slides, click `Insert`. Ideal for "choose your own topic" menus and Q&A jump lists.

**Step-by-step (Summary Zoom):** `Insert > Zoom > Summary Zoom`, choose sections, click `Insert`. PowerPoint creates a new summary slide with clickable section thumbnails, typically placed at the start of the summarized content.

**Real-world examples.**
- *Business:* YourCompany Inc's product menu slide shows four section thumbnails; a salesperson clicks "Pricing" only for price-sensitive buyers, then returns to the menu via `Return to Zoom`.
- *Education:* A revision deck is a summary zoom of five topic sections so each student navigates to their weak areas.
- *Personal:* A travel album menu zooms into "Lisbon", "Porto", and "Food" sections on demand.

**Try it now.** Add three sections to a deck with 2-3 slides each. Insert a `Summary Zoom` on slide 1, enable `Zoom Background` and `Return to Zoom`, then present: click into a section and confirm you return to the menu when the section ends.

---

## 10. Custom Shows: One Deck, Many Audiences

**What it is.** A Custom Show is a named subset of your slides stored inside the same file. Instead of maintaining separate decks for executives, engineers, and partners (and letting them drift out of sync), you keep one master deck and define a Custom Show per audience. Shows can be launched manually or via hyperlink, and can loop.

**Step-by-step (create a Custom Show):**
1. `Slide Show > Custom Slide Show > Custom Shows...`.
2. Click `New`. Name it (for example `Exec Briefing`).
3. In `Slides in presentation`, check the slides to include. Use `Up`/`Down` arrows to set their order (the show order can differ from deck order).
4. Click `OK`, then create another show (for example `Technical Deep Dive`) the same way. Close the dialog.

**Step-by-step (run and link a Custom Show):**
- Run it directly: `Slide Show > Custom Slide Show` and click the show's name.
- Link to it: on a shape, `Insert > Action > Hyperlink to > Custom Show`, pick the show, and decide whether `Show and return` (bounce back to the launching slide) is checked. This is how menu slides offer "5-minute version" and "20-minute version" buttons.

**Real-world examples.**
- *Business:* One YourCompany Inc master deck feeds three shows: `Exec Briefing` (6 slides), `Technical Deep Dive` (18 slides), `Partner Overview` (10 slides). Content edits once, propagate everywhere.
- *Education:* A teacher keeps one course deck and defines `Lesson 1`, `Revision`, and `Exam Prep` shows for different class days.
- *Personal:* A wedding reel has `Kids version` (fun photos only) and `Full story` shows.

**Try it now.** Create two Custom Shows from an existing deck: `Short` (3 slides) and `Long` (6 slides including those 3). Then add two buttons on slide 1, each with `Insert > Action > Hyperlink to > Custom Show` and `Show and return` enabled, and test both paths.

---

## 11. Kiosk Mode: Self-Running Decks

**What it is.** Kiosk mode turns a presentation into a self-contained interactive display for trade-show booths, reception areas, museum-style exhibits, and touch screens. In kiosk mode the deck runs full screen, mouse clicks do NOT advance slides (so random visitors cannot break the flow), and navigation happens only through your hyperlinks, action buttons, and Zoom menus. You can also make decks self-advancing with automatic timings.

**Step-by-step (enable kiosk mode):**
1. Go to `Slide Show > Set Up Slide Show`.
2. Under `Show type`, select `Browsed at a kiosk (full screen)`.
3. Optionally set `Loop continuously until 'Esc'` (usually implied by kiosk mode) and choose `Using timings, if present` under `Advance slides`.
4. Click `OK`. Start the show with `F5` and press `Esc` to exit.

**Step-by-step (auto-advance timings):**
1. `Transitions` tab, in the `Timing` group set `Advance Slide > After:` to a duration (for example `00:05.00` for 5 seconds).
2. Click `Apply To All` to set every slide, or set per slide for varied pacing (longer on dense slides).
3. Alternatively, use `Slide Show > Rehearse Timings` to record natural pacing by talking through the deck, then save the timings when prompted.

**Step-by-step (hidden slides):** Right-click a slide thumbnail > `Hide Slide`. Hidden slides are skipped in the show but reachable via hyperlink or action button, perfect for optional deep-dive slides.

**Real-world examples.**
- *Business:* YourCompany Inc's booth screen loops a kiosk deck with a Zoom menu, so visitors tap topics of interest and it never drifts to a broken state.
- *Education:* An open-day display runs a self-advancing 2-minute loop on a hallway screen with narration.
- *Personal:* A digital photo frame at home runs a looping slideshow with 6-second timings.

**Try it now.** Set all slides to advance after 3 seconds, enable `Browsed at a kiosk (full screen)`, and press `F5`. Confirm ordinary clicks do nothing, then press `Esc` to exit. Add one action button wired to `End Show` so users have an exit affordance if a human operator is nearby.

---

## 12. Export to Video (MP4) and GIF

**What it is.** You can turn a finished deck into a standalone video file: MP4 for full narrated walkthroughs (with audio and timings), or animated GIF for short loops to drop into chat, email, or a web page. Export is the natural end-point of this module: narrate, compress, then ship as a file anyone can play without PowerPoint.

**Step-by-step (export MP4):**
1. `File > Export > Create a Video` (or `File > Save As` and pick `MP4`/`MOV` from the file type dropdown).
2. Choose quality: `Full HD (1080p)` for large screens, `HD (720p)` for email and web, `Ultra HD (4K)` when detail matters.
3. Set `Use Recorded Timings and Narrations` (this includes your `Record Slide Show` narration and per-slide timings). If you have none, choose `Seconds spent on each slide` and type a default like 5.
4. Click `Create Video`, choose a filename and location, and click `Save`.
5. A progress bar appears on the status bar. Rendering is not instant: a 20-slide narrated deck can take several minutes. Wait for the bar to finish before opening the file.

**Step-by-step (export GIF):**
1. `File > Export > Create an Animated GIF`.
2. Choose a quality tier (Small, Medium, Large, Extra Large). The dialog shows approximate dimensions and a size estimate.
3. Set `Seconds spent on each slide` and whether to `Use Recorded Timings and Narrations` (narration is ignored in GIF, since GIF is silent).
4. Click `Create GIF`, pick a location, and save. For loops, the GIF repeats when embedded in web pages and chat tools that loop GIFs.

**Real-world examples.**
- *Business:* YourCompany Inc exports its narrated pitch to MP4 and posts it in the company LinkedIn feed and on the sales portal.
- *Education:* A teacher exports the lecture deck to MP4 so absent students can catch up, and exports a 3-slide GIF of the molecule animation for the class group chat.
- *Personal:* A birthday slideshow becomes an MP4 shared with family abroad.

**Try it now.** Take a 3-slide deck with narration, export it as `HD (720p)` MP4 using recorded timings, and play the result in a media player. Then export the same deck as a `Medium` GIF and check how much larger GIFs are per second of motion.

---

## 13. Media Accessibility: Captions and Alt Text

**What it is.** Accessible media means every viewer, including people who cannot hear audio or see a video frame clearly, can get the content. The two pillars are captions/subtitles for audio-visual material and alt text for every meaningful visual object. PowerPoint offers live AI-driven captions and subtitles in Slide Show mode (when connected to the internet) and manual alt text everywhere.

**Step-by-step (live captions and subtitles):**
1. Go to `Slide Show > Always Use Subtitles` to enable subtitles for every show.
2. Next to it, set `Subtitle Settings`: choose `Spoken Language` (what the presenter speaks) and `Subtitle Language` (what appears on screen).
3. Choose where captions appear: `Below Slide` (default, keeps slide content clear) or `Overlaid on Slide` (bottom or top of the slide).
4. Start the show: PowerPoint transcribes the microphone in real time and displays captions. An internet connection and a clear microphone improve accuracy substantially.

**Step-by-step (narration captions in exported video):** For precise captions in an MP4 export, narrate with `Record Slide Show`, then open `Insert > Captions` workflows available in current versions (for example `Insert > Video > Caption Insert` styles) or produce a caption sidecar file (VTT/SRT) and add it when publishing to platforms like YouTube, LinkedIn, or Stream, which render caption tracks on top of the MP4.

**Step-by-step (alt text on media and visuals):**
1. Right-click any video frame, audio icon, picture, chart, SmartArt, or shape and choose `Edit Alt Text` (or `Alt Text` in the right-click menu / `Accessibility` ribbon tab).
2. Describe the content and function in one or two sentences ("Bar chart showing Q1-Q4 revenue rising from 2.1 to 3.4 million US dollars"). For decorative shapes, check `Mark as decorative`.
3. Use the `Accessibility Checker`: `File > Info > Check for Issues > Check Accessibility`. It lists missing alt text, unclear link text (avoid "click here"), and reading order problems. Fix items in the pane that opens.

**Audio alternatives.** For sound-on-click cues, also give a visual signal (an animation or a text note), since not everyone perceives audio cues.

**Real-world examples.**
- *Business:* YourCompany Inc turns on subtitles for every webcast and runs the Accessibility Checker before sending decks to government clients with procurement accessibility requirements.
- *Education:* Captions let a hard-of-hearing student follow the live lecture; alt text on diagrams lets a screen-reader user study the exported handout.
- *Personal:* Alt text descriptions make a grandparent's photo slideshow meaningful to a blind family member listening with a screen reader.

**Try it now.** Enable `Always Use Subtitles`, present one slide while speaking for 15 seconds, and watch the captions appear. Then run `File > Info > Check for Issues > Check Accessibility` on a deck with two images and fix every flagged item.

---

## Practice Projects

Complete all five to consolidate the module. Each builds on skills from earlier sections.

**Project 1: The Multimedia Sales Pitch (video + audio + compression)**
Build an 8-slide YourCompany Inc sales deck that includes: one stock video as an intro background, one device video trimmed to 30 seconds with fade in/out and a custom poster frame, and low-volume background music playing across all slides.
*Success criteria:* (1) Video starts automatically, does not play full screen, has a 1-second fade in and 1.5-second fade out. (2) Poster frame is not the default first frame. (3) Music plays across slides, loops, and is hidden during the show. (4) File is under 50 MB after `Compress Media` at HD (720p). (5) Deck plays end to end with no clicks except slide advances.

**Project 2: The Screen-Recorded How-To (screen recording + narration)**
Produce a 5-slide tutorial deck teaching any software task, with a screen recording of the process embedded and trimmed to 60 seconds or less, narration recorded on at least three slides via `Record Slide Show`, and a screenshot with a caption callout.
*Success criteria:* (1) Recording was captured at `Select Area` scope (not the whole desktop) and trimmed to the essential steps. (2) Narration and slide timings are synchronized when played back. (3) Screenshot region excludes desktop clutter. (4) Exported as MP4 with `Use Recorded Timings and Narrations` and the audio is audible in the result.

**Project 3: The Interactive Menu (hyperlinks + action buttons + Zoom)**
Create a 12-slide interactive menu deck with three sections, a landing slide containing a Summary Zoom (or a hand-built menu of three shape buttons), `Return to Zoom` enabled, and a persistent `Home` action button on every slide (place it on the Slide Master).
*Success criteria:* (1) Every menu item reaches its section and the viewer returns to the menu afterward. (2) The Home button works from every slide. (3) Menu buttons are shapes with hyperlink-free clean text (no underlines anywhere in the deck). (4) At least one email link with a subject line exists on the final slide. (5) A tester who has never seen the deck can navigate to any section and back within 10 seconds.

**Project 4: The Audience-Switcher (Custom Shows + kiosk mode)**
From one master deck of at least 12 slides, define three Custom Shows (`Exec` 4 slides, `Technical` 8 slides, `Full` all slides) and a launcher slide with three action buttons (`Hyperlink to > Custom Show`, `Show and return` checked). Configure the deck to run in kiosk mode with 5-second auto-advance timings.
*Success criteria:* (1) Each button runs only its show and returns to the launcher. (2) In kiosk mode, raw mouse clicks do not advance or break the show. (3) The deck loops continuously until `Esc`. (4) One slide is hidden yet reachable via hyperlink. (5) Editing one slide's text visibly updates all three shows (proving single-source content).

**Project 5: The Accessible Video Handout (captions + alt text + export)**
Take any existing deck and make it publication-ready: enable `Always Use Subtitles` with correct spoken/subtitle languages, add alt text to every picture, chart, and video, mark decorative shapes as decorative, fix every `Check Accessibility` finding, then export as MP4 and as GIF.
*Success criteria:* (1) Accessibility Checker reports zero errors. (2) All alt text is descriptive (conveys data or meaning, not just "image1"). (3) Subtitles display correctly during a live slide show. (4) The MP4 export is HD (720p) or better and under 100 MB. (5) The GIF loops and is sized `Medium` or `Large`, and you can name one appropriate and one inappropriate use case for it.

---

## Common Mistakes & Pitfalls

| Mistake | Why it hurts | Fix |
|---|---|---|
| Embedding raw, untrimmed 1080p clips | Deck balloons to hundreds of MB; crashes on weak machines | Trim first (`Playback > Trim Video`), then `File > Info > Compress Media` at HD or 480p |
| Forgetting that online video needs internet | Clip shows a broken frame live on stage | Use `This Device` embeds for critical content; test online video on venue Wi-Fi |
| Default poster frame is an awkward first frame | Deck looks unprofessional before anyone presses play | `Playback > Poster Frame > Capture from Current Frame` after trimming |
| Setting `Start > In Click Sequence` and expecting autoplay | Video waits for a click and stalls the presenter | Use `Automatically` for autoplay, `When Clicked On` for deliberate playback |
| Music volume too loud over narration | Audience cannot hear the speaker or voice-over | `Playback > Volume > Low`, and mute music when narrating live |
| Hyperlinks underlined everywhere | Slides look like a 2005 web page | Link whole shapes instead of text; recolor theme `Hyperlink`/`Followed Hyperlink` colors |
| Links to guessed or copied-but-unchecked URLs | 404s in front of an audience | Type full URLs including `https://` and test every link in Slide Show mode before presenting |
| No navigation affordance in kiosk mode | Visitors get stuck on one slide | Add action buttons (`Home`, `Next`) and Zoom menus; always include an `End Show` or `Home` control |
| No `Return to Zoom` on section menus | Presenter dives into a section and has to scroll back manually | Check `Return to Zoom` on every Zoom card in menu slides |
| Compressing media before trimming | Trimmable footage is re-encoded and kept, wasting size | Trim first, compress second; then `Save` and re-check size on `File > Info` |
| Separate copies of the deck per audience | Versions drift; wrong deck shown to the wrong crowd | One master deck with Custom Shows per audience |
| Exporting video without timings/narration setting | Silent MP4 with 5-second flat slides | Choose `Use Recorded Timings and Narrations` in `File > Export > Create a Video` |
| GIF used for long narrated content | Huge file, no audio possible | GIF only for short silent loops (under ~30 seconds); use MP4 for everything else |
| Alt text missing or useless ("photo", "chart1") | Screen reader users get nothing | Describe content and takeaway ("Line chart of monthly signups doubling from Jan to Jun"); mark decoration as decorative |
| Narration left on a slide after a live rehearsal | Audio plays unexpectedly during a live talk | Delete narration per slide (select the speaker icon and `Delete`) or use `Slide Show > Set Up Slide Show > Show without narration` |
| Screen recording captures the entire desktop | Notifications and personal files leak into the video | Always use `Select Area` on the target window before `Record` |

---

## Key Takeaways

- Embed critical video from `This Device` (MP4/H.264) and treat online video as an internet-dependent bonus.
- Trim first, fade second, set the poster frame third, compress last: that order produces the smallest, most polished media.
- `Playback` settings (`Automatically` vs `When Clicked On`, `Play Full Screen`, `Loop until Stopped`, `Hide While Not Playing`, `Rewind after Playing`) define how a clip behaves during a live show; always test them in Slide Show mode.
- `Play in Background` is the one-click path for music across slides; `Record Slide Show` is the reliable path for narration and slide timings.
- `Insert > Screen Recording` with `Select Area` produces editable, trimmable demo videos without leaving PowerPoint.
- Hyperlinks and action buttons are the primitives of interactivity: wire them to slides, Custom Shows, URLs, and email, and style them as shapes to keep slides clean (no underlines).
- Zoom navigation (`Slide Zoom`, `Section Zoom`, `Summary Zoom` with `Return to Zoom`) creates menu-driven, non-linear presentations; organize slides into sections first.
- Custom Shows keep one source of truth for many audiences; kiosk mode (`Set Up Slide Show > Browsed at a kiosk`) makes decks click-proof and self-running with `After:` timings.
- Export narrated decks as MP4 (`Use Recorded Timings and Narrations`) and short silent loops as GIF.
- Accessibility is part of media work: enable subtitles, write real alt text, and clear the Accessibility Checker before sharing.

---

## Further Learning

- PowerPoint support hub (videos, how-tos, and captions/topics on media and slide shows): https://support.microsoft.com/en-us/powerpoint
- Microsoft Learn training for PowerPoint: https://learn.microsoft.com/en-us/training/
- Microsoft Create (templates and inspiration for video-rich and interactive decks): https://create.microsoft.com/

Tip: on the PowerPoint support hub, use the site search for `video`, `screen recording`, `kiosk`, or `accessibility` to reach the exact article you need without guessing deep links.


## FILE: 07-Delivery-Workflow/07-delivery-workflow.md

# Module 07: Delivery & Professional Workflow

**Module number:** 07
**Title:** Delivery & Professional Workflow
**Level:** Advanced
**Prerequisites:** Modules 01-06 (interface basics, slide creation, text and layouts, visual design, images/shapes/charts, animations and transitions). Comfort with the ribbon, Slide Master, and saving to OneDrive is assumed.
**Estimated study time:** 90-120 minutes
**Next module:** None (final module). Revisit Module 03 for content structure and Module 05 for visual polish as needed.

---

A beautiful deck is only half the job. The other half happens in the room (or the meeting link): you hit Play, the show runs, and your audience either follows your story or drowns in your slides. This module covers everything from the moment your design is "done" to the moment you hit the final slide: speaker notes, Presenter View, rehearsal and recording, live vs link vs video delivery, collaboration, accessibility, exporting and printing, protecting your file, managing large decks, and a pre-flight checklist that will save you from the classic disasters (wrong monitor, missing fonts, a 200 MB file nobody can open).

Treat this module as the professional's operating manual. Design wins attention; delivery wins the deal.

---

## 1. Speaker Notes: Prompts, Not Scripts

### Why it matters

Speaker notes are the text that appears in the notes pane below each slide (and on Notes Pages when printed). Their job is to remind *you* what to say, not to hand the audience a novel. The single biggest notes mistake is pasting your full script into the pane and then reading it verbatim during the show. Audiences can tell when you are reading, and reading kills eye contact, pacing, and energy.

Good notes are prompts: keywords, a story cue, a number you must not misquote, a transition line to the next slide. Think of them as sticky notes on a podium, not a teleprompter.

### What goes in good notes (and what does not)

- **Include:** your core message in one sentence, the 2-3 supporting points as short bullets, exact figures or quotes you must get right ("Q3 revenue: $4.2M, up 18%"), a cue for interaction ("ask the room: who has shipped a release this quarter?"), and a transition line ("next: why the timeline slips").
- **Exclude:** full paragraphs, your entire talk track, apologies to yourself, anything confidential you would not want projected if notes leak into the wrong view, and duplicate text from the slide itself.

### Step-by-step: writing notes

1. Open your presentation and click the slide you want to prep.
2. Click the notes pane at the bottom of Normal view. If you do not see it: **View > Notes** toggles the pane open.
3. Type your prompt. Example for a business slide titled "Q3 Results":
   - Core: "Best quarter in company history, but growth is slowing at the margin."
   - Points: "$4.2M revenue (+18% YoY)", "Churn ticked up 0.4pt, watch it", "Enterprise drove 70% of new ARR".
   - Cue: "Pause, ask CFO if she wants to add context on churn."
   - Transition: "Next: the plan to fix churn in Q4."
4. To review all notes at once: **View > Notes Page** shows one slide per page with its notes beneath, laid out for printing.
5. Resize the notes pane by dragging its top border up so you can type comfortably.

### Formatting notes

Notes accept basic formatting (bold, bullets) via the mini toolbar or **Home** tab while the cursor is in the pane. Keep formatting minimal; bold the figures you must not fumble, and nothing else. Note text uses the Notes Master styles: **View > Notes Master** if you want your company font in the notes pane globally.

### Real-world examples

- **Business (board update):** Slide shows only "Revenue: $4.2M". Notes carry the bridge explanation ("growth came from two enterprise renewals closing a week early; without them we are flat") so the slide stays clean but you can answer follow-ups.
- **Education (lecture):** Slide shows a diagram of the water cycle. Notes list the 90-second story about the field trip to the river, plus the two exam hints you will say out loud but never write on the slide.
- **Personal (wedding toast):** Slide is a photo montage. Notes are three words per slide: "college story", "the camping trip", "raise a glass".

### Try it now

Open any deck from earlier modules. On three slides, replace (or write) notes that contain exactly: one-sentence core message, two keyword bullets with at least one hard number, and one transition line to the next slide. Keep each notes block under 40 words. Then switch to **View > Notes Page** and confirm the notes read as prompts, not prose.

---

## 2. Presenter View: What You See vs What They See

### Why it matters

Presenter View is the cockpit. When you present with two displays (laptop + projector, or laptop + external monitor), your screen shows a private dashboard: current slide, next slide, your notes, a timer, and navigation tools. The audience sees only the current slide, full screen. Used well, Presenter View lets you speak from prompts, watch your pacing, and jump around the deck without the audience ever seeing the seams.

### What is on each screen

- **Audience screen (projector/second display):** the current slide only, full screen, with transitions and animations playing normally. No notes, no next slide, no UI.
- **Your screen (Presenter View):** large current slide, smaller "next slide" preview, your notes pane, elapsed-time timer (pausable), slide counter (for example 12 of 24), and buttons: pen/lasso/highlighter tools, **See all slides** (a zoomable grid of the whole deck for jumping), **Zoom into the slide**, **Black/White screen** (temporarily hide the slide), **Display Settings** (swap or duplicate displays), and **End Show**.

### Step-by-step: turning it on and presenting

1. Connect your second display (cable, or wireless cast). Tell the OS to **Extend** displays, not Duplicate (Windows: **Win+P > Extend**; macOS: **System Settings > Displays**, uncheck mirroring).
2. In PowerPoint: **Slide Show > Set Up Slide Show**. Under "Multiple monitors", set **Slide show monitor** to the external display (choose the monitor by name or "Automatic"), and tick **Use Presenter View**.
3. Shortcut: on the **Slide Show** tab, tick **Use Presenter View** in the Monitors group, and pick your monitor from the **Monitor** dropdown.
4. Start the show: press **F5** (from slide 1) or **Shift+F5** (from the current slide), or click **Slide Show > From Beginning**.
5. Verify immediately: glance at both screens before you say your first sentence. Audience should see the title slide full screen; you should see Presenter View.

### Presenter View keyboard shortcuts worth memorizing

- **N** or **Right Arrow** or **Space**: next animation/slide.
- **P** or **Left Arrow** or **Backspace**: previous.
- **B** then **.** (period): black screen and back. **W** then **.**: white screen.
- **Ctrl+L** (Cmd+L on Mac): laser pointer. **Ctrl+P**: pen. **Ctrl+E**: eraser for ink. **Ctrl+A**: arrow pointer.
- **Ctrl+S** or **G**: See all slides grid. **Esc**: end the show.
- **1** then **Enter**: jump to slide 1. Type any number then **Enter**: jump to that slide.

### Getting Presenter View on "any" setup

- **No second display, but a big TV via HDMI:** that TV *is* the second display; extend, do not mirror.
- **Only one output available (mirroring forced):** Presenter View cannot work mirrored. Use your phone or tablet as a second screen with the PowerPoint mobile app or a remote-presenter companion app, or fall back to printed notes and the on-screen slide counter.
- **Presenting from a browser (PowerPoint for the web):** Presenter View works when the browser lets you choose which screen to share. Start the show, then share only the slide-show window/screen.
- **Joining a Teams/Zoom call:** share the *slide show window* (Share > select the PowerPoint Slide Show window), not your whole desktop, and leave Presenter View on your primary screen. Never share your entire screen unless you want notes and your inbox visible.

### Troubleshooting: gray screens and wrong monitors

- **Gray/black screen on the projector:** the show is running on the wrong display. Press **Esc**, then **Slide Show > Set Up Slide Show > Slide show monitor**, pick the other display, restart. Or use **Display Settings** inside Presenter View to **Swap Presenter View and Slide Show**.
- **Presenter View is on the projector (the audience sees your notes!):** same fix, swap displays via **Display Settings > Swap** mid-show without ending the show. Do this calmly; the audience sees only a moment of the wrong feed if you are quick.
- **Duplicate mode is on and Presenter View will not appear:** set the OS to Extend (see above). Presenter View requires two independent displays.
- **Slide show spans two screens oddly:** right-click the desktop > Display settings, set both monitors to the same scaling or designate the projector as the display to "Show desktop only on 2".
- **Windows + a laptop lid:** closing the lid may sleep the laptop. Set **Power options > When I close the lid > Do nothing** for the presenting power plan before the event.

### Real-world examples

- **Business:** pitching to a client on their conference-room projector. Presenter View keeps your 12 talking-point notes on the laptop while the client sees only the pricing slide.
- **Education:** teaching in a lecture hall. You use **See all slides** to jump to a diagram two slides back when a student asks, without flipping visibly through the deck.
- **Personal:** a community club AGM. The timer keeps your 10-minute update to 10 minutes so the meeting stays on schedule.

### Try it now

Without any projector attached, press **Slide Show > Set Up Slide Show** and set "Show on" to a specific monitor with Presenter View enabled, then start the show and explore: open **See all slides**, draw with the pen (**Ctrl+P**, then drag on the slide), press **B** to black the screen and back, and check the timer. Notice what appears on the mirrored window vs the Presenter View window.

---

## 3. Rehearse Timings and Recording a Slide Show

### Why it matters

A 20-minute slot is a 20-minute slot. Rehearsing with timings teaches you where your talk actually runs long, and recording turns a good talk into an asset that scales (onboarding videos, flipped classrooms, async updates).

### Rehearse Timings

1. **Slide Show > Rehearse Timings.** PowerPoint starts the show from slide 1 with a timer toolbar (pause, repeat, and per-slide / total elapsed time).
2. Speak your talk at real pace. Click (or press **N**) when you would move to the next slide. The time spent on each slide is recorded.
3. When you finish, PowerPoint asks: "Do you want to save the new slide timings?" Click **Yes** to keep them (they attach to each slide), **No** to discard.
4. Review the results: **View > Slide Sorter** shows each slide's new advance time under its thumbnail. Adjust any slide manually by selecting it, opening the **Transitions** tab, and setting **Advance Slide > After:** to your edited value (for example 00:01:45). Untick **On Mouse Click** if you want the show to run on timers alone (kiosk mode).
5. To discard all timings: **Slide Show > Set Up Slide Show > uncheck "Use timings, if present"**, or per-slide, tick **On Mouse Click** and clear the **After** checkbox.

Timings do double duty: they pace a self-running kiosk deck and they seed your video export with per-slide durations.

### Recording a slide show (narration and video)

1. **Slide Show > Record Slide Show** and choose **Record from Current Slide** or **Record from Beginning**.
2. The recording studio opens: big preview, record button (circle), teleprompter-style notes on the right, camera toggle (adds a talking-head video bubble), microphone picker, and ink tools.
3. Click **Record** (3-second countdown). Speak, advance slides with clicks or arrows, and annotate with the pen as needed. Ink drawn while recording is captured and replayed.
4. Click **Pause** to take a breath; **Re-record** a slide by selecting it and recording again (previous recording for that slide is replaced).
5. Click **Stop**, then **Esc** to exit. Play the result with **Slide Show > Play from Start** to review.
6. To remove recordings: **Slide Show > Clear > Clear Timings on All Slides**, **Clear Narrations on All Slides**, or per-slide variants.

### Real-world examples

- **Business:** a quarterly all-hands deck gets rehearsed until it lands in exactly 15 minutes; the recorded version is posted for the remote office.
- **Education:** a professor records the lecture deck as a flipped-classroom video so class time is for exercises.
- **Personal:** recording a narrated photo book for relatives abroad who cannot attend the reunion.

### Try it now

Take any 5-slide deck and run **Rehearse Timings** while giving a pretend 2-minute talk. Save the timings, open **Slide Sorter**, and note the per-slide times. Then change one slide's time to exactly 00:00:30 via **Transitions > After**. Finally, record 20 seconds of narration on slide 1 only (**Record Slide Show > Record from Current Slide**) and play it back.

---

## 4. Live vs Link vs Video: Choosing How to Deliver

### Why it matters

The same deck can be delivered three ways, and the right choice depends on presence, polish, and reach. Professionals choose deliberately and often use two of the three.

### Presenting live

- **Best for:** pitches, Q&A-heavy sessions, teaching, anything where trust and feedback matter.
- **How:** Presenter View + rehearsal (see Sections 2-3). Plan for interaction in your notes.
- **Strengths:** adaptability (you can skip slides when a question lands early), energy, immediate read of the room.
- **Costs:** you must show up live, and it does not scale past one time slot.

### Sharing a link (cloud deck)

- **Best for:** reference decks, async updates, handouts, team reviews.
- **How:** save the deck to OneDrive or SharePoint (**File > Share > Share** or **File > Save As > OneDrive**). Choose link permissions: **Anyone with the link**, **People in YourCompany Inc with the link**, or **Specific people** (for example jane@acme.com). Decide **Can edit** vs **Can view**. Click **Copy link** and send it.
- **Strengths:** always current (edit once, everyone sees the latest), small footprint, comment-friendly.
- **Costs:** you lose delivery control (people skim at their own pace), and wrong permissions can leak content. Also note the recipient needs PowerPoint or PowerPoint for the web to view natively; that is why PDF export (Section 8) exists.

### Recording narrated video

- **Best for:** training, onboarding, product demos, conference talk distribution, flipped classrooms.
- **How:** record the slide show (Section 3), then **File > Export > Create a Video** (Section 8). Share the MP4 via your org's video platform or file share.
- **Strengths:** scales infinitely, consistent message, rewatches, captions possible.
- **Costs:** no live Q&A and re-edits mean re-rendering.

### Decision cheat sheet

| Situation | Best format | Also |
|---|---|---|
| Investor pitch | Live | Link as follow-up |
| New-hire onboarding | Video | Link to the deck for reference |
| Weekly team status | Link | Live walkthrough if contentious |
| University lecture | Live | Video for absent students |
| Product demo at a booth | Live (loop as video when booth is quiet) | Video |

### Real-world examples

- **Business:** You pitch live on Tuesday (Presenter View, rehearsed to 18 minutes), email the view-only link Wednesday morning, and post the 18-minute narrated MP4 to the intranet Friday.
- **Education:** Lectures delivered live and recorded; the recording is the study resource before exams.
- **Personal:** A wedding slideshow runs live at the dinner, then the narrated video goes to family who could not travel.

### Try it now

Pick one deck and plan a two-format delivery: write one sentence on why the primary format (live, link, or video) fits, and one on the secondary format you will also produce. Then save the deck to OneDrive and generate a **Can view** link (do not send it), noting the difference between "People in YourCompany Inc" and "Specific people" scopes.

---

## 5. Co-authoring, Comments, @mentions, Version History, Compare & Merge

### Why it matters

Real decks are team artifacts. Legal reviews the disclaimer, marketing polishes the headline, and the CFO fixes the numbers, often within the same afternoon. Cloud co-authoring, comments, and version history make that safe; Compare & Merge covers the messy reality of decks traveling by email.

### Co-authoring on OneDrive/SharePoint

1. Save the deck to OneDrive or SharePoint (**File > Share** prompts you if it is still local).
2. Invite collaborators: **File > Share > Share**, type jane@acme.com, choose **Can edit**, add a note, **Send** (or **Copy link**).
3. Collaborators open the link and edit simultaneously. Each person's cursor shows a name flag and a color. The status bar shows who else is in the file (**Editing** or **Viewing**).
4. Your edits save automatically (AutoSave toggle top-left). Conflicts are rare because slides lock while someone edits them; if two people edit the same slide offline, PowerPoint flags the conflict and lets you choose.

### Comments and @mentions

1. Select the object or click in the text, then **Review > New Comment** (or right-click > **New Comment**).
2. Type your note. Type **@** and start a name to mention a colleague (for example @jane); they get a notification and the comment becomes a task for them.
3. Reply threads: click **Reply** under a comment to discuss in context.
4. **Review > Show Comments** opens the Comments pane listing every thread; resolve a thread by clicking the **Resolve** checkmark (it stays in history, dimmed).
5. Comments are visible in the web app and desktop, and in **Review > Delete > Delete All Comments in Presentation** when you finalize.

### Version history

1. **File > Info > Version History** (or click the file-name/title area at the top of the window > **Version History** in modern builds).
2. The pane lists timestamped versions with author names (for example "jane@acme.com, Today 3:42 PM").
3. Click a version to open it read-only. Compare it to the current file, then **Restore** to roll back, or just copy slides out of it.
4. Version history is what makes aggressive editing safe: encourage your team to edit boldly and restore if it goes wrong.

### Compare & Merge (desktop PowerPoint)

1. With the destination deck open, **Review > Compare**. Pick another version of the presentation (the "source" file, for example a copy someone emailed back).
2. PowerPoint merges the two and opens the **Revisions** pane listing every difference by slide and author: changed text, images, animations, even formatting.
3. Review each change: tick the checkbox to accept it into your deck, untick to keep yours. Use **Accept All** / **Reject All** per slide if you trust the whole batch.
4. Save the merged result as a new file (for example "BoardDeck_v9_merged.pptx") so the originals survive.

### Real-world examples

- **Business:** Three regional leads co-author the annual plan deck in SharePoint on the same afternoon; comments with @mentions assign each region's data fixes; version history proves which numbers changed before the CFO review.
- **Education:** A course team co-authors a lecture deck; the teaching assistant comments on ambiguous exam hints; the professor merges the adjunct's offline edits with **Compare**.
- **Personal:** Two siblings co-author a memorial slideshow from different cities via OneDrive, resolving comments about photo captions.

### Try it now

Save a deck to OneDrive and share a **Can edit** link with jane@acme.com (do not actually send; use Copy link). Add a comment on slide 2 with an @mention. Then make a duplicate of the deck, change the title text on slide 1 in the copy, and use **Review > Compare** to merge the copy back. In the Revisions pane, accept the title change and save as "merged-practice.pptx". Finally, open **File > Info > Version History** and note how many versions were created.

---

## 6. Accessibility: Make Every Deck Usable by Everyone

### Why it matters

Roughly one in six people has a disability significant enough to affect how they consume content. Screen-reader users, people with low vision, color-blind viewers, and non-native speakers in a noisy room all benefit from accessible decks, and many organizations require it (procurement rules, public sector mandates). Accessibility also plain improves quality: a deck with real titles and reading order is better for everyone.

### The Accessibility Checker

1. **Review > Check Accessibility**. The **Accessibility** pane opens with issues grouped as Errors and Warnings, per slide and object.
2. Click an issue to jump to the offending object. Fix it (the pane explains why each issue matters and how to fix it).
3. Re-run the checker after fixes. Aim for zero errors before distribution; resolve warnings where practical.
4. Make it a habit: run the checker as the second-to-last step of every deck (Section 12's pre-flight checklist).

### Alt text (for images, shapes, charts, SmartArt)

1. Right-click the object > **View Alt Text** (or **Alt Text** in the ribbon's accessibility group; the **Alt Text** pane opens).
2. Write a concise description of what the object conveys, not its file name: "Bar chart: revenue by quarter, Q1 to Q4, rising from $2.1M to $4.2M". For purely decorative images, tick **Mark as decorative** so screen readers skip them.
3. Charts: describe the takeaway, not every bar. SmartArt: describe the process the diagram shows.
4. Never leave "image.png" or "Picture 4" as alt text; the checker will flag it.

### Reading order

1. **Home > Arrange > Selection Pane** (or **Review > Check Accessibility > Reading Order** in newer builds).
2. Screen readers read objects in the order shown in the Selection Pane (typically bottom-to-top of that list). Reorder with drag-and-drop or the **Reorder** arrows in the Reading Order pane.
3. Correct order: title first, then content in visual reading order (top-left to bottom-right), then decorative items last (or mark them decorative).
4. Test mentally: "If I could only hear this slide, would the story still make sense?"

### Slide titles and structure

- Give every slide a real title (even visually hidden ones): use the title placeholder. Duplicated or missing titles are the most common accessibility errors and the biggest annoyance in navigation.
- For a visually title-less slide, put the title in the title placeholder and use the **Arrange > Selection Pane > Hide** trick is not enough for accessibility; instead set the title font to match the background or place the title placeholder behind a full-bleed picture. Screen readers still get the title.
- Avoid using text boxes as fake titles; use real placeholders from the layout (**Home > Layout**).
- Use built-in layouts, not free-floating shapes, so the structure survives in Outline view and screen readers.

### Contrast and color

- Text needs a contrast ratio of at least **4.5:1** against its background (3:1 for 24pt+ or bold 18pt+ text). Use an online contrast checker or PowerPoint's own flags from the Accessibility Checker.
- Never convey meaning by color alone ("the red bars are declining"): add labels, patterns, or direct annotations.
- Check your theme colors (Section on Design, Module 04) with a color-blindness simulator mindset: red/green pairs are the usual offenders.

### Captions and subtitles for media

- **Video/audio captions:** insert a video, select it, then **Playback > Insert Captions** and load a WebVTT (.vtt) captions file. Set captions to show during playback.
- **Live subtitles (presenting):** **Slide Show > Always Use Subtitles**. Choose spoken language and subtitle language under **Subtitle Settings**. PowerPoint captions your speech live and displays subtitles at the bottom of the slide show; this is transformative for multilingual audiences and noisy rooms.
- For recorded shows, burned-in subtitles come from the captions or from the video platform after export.

### Real-world examples

- **Business:** A government-tender deck passes procurement accessibility review because every chart has alt text and the checker shows zero errors.
- **Education:** A hearing-impaired student follows lecture decks via live subtitles; classmates benefit too.
- **Personal:** A low-vision relative reads the reunion slideshow on a tablet with a screen reader because titles and reading order were set properly.

### Try it now

Break a deck on purpose: delete one slide's title, set an image's alt text to "Picture 1", and drop a light-gray text box on a white background. Then run **Review > Check Accessibility** and fix all three flagged issues. Finally, turn on **Slide Show > Always Use Subtitles** and run a 30-second show while speaking to see live captions appear.

---

## 7. Exporting: PDF, Video (MP4), and Animated GIF

### Why it matters

Delivery does not end at .pptx. PDFs survive any device, videos scale to any audience, and GIFs preview motion in places slides cannot go (chat, docs, web). Export quality is a professional signature: a blurry PDF handout says nobody checked.

### Export to PDF (print and handout quality)

1. **File > Export > Create PDF/XPS** (or **File > Save As** and pick PDF).
2. Click **Options** before publishing. Set:
   - **Publish what:** Standard (for screen) or Minimum size; for print-quality handouts choose Standard and keep "ISO 19005-1 compliant (PDF/A)" if archiving.
   - **Include:** slides, notes pages, or handout pages (choose slides-per-page layout, for example 3 slides with lines).
   - Tick **Document structure tags for accessibility** so screen readers can read the PDF.
3. Click **Publish** (or **Save**).
4. Verify the PDF opens correctly and fonts render (embed fonts on save: **File > Options > Save > Embed fonts in the file** before exporting, or use widely available fonts).

### Export to video (MP4)

1. **File > Export > Create a Video**.
2. Choose quality: **Full HD (1080p)** for most delivery, **Ultra HD (4K)** for large displays, **HD (720p)** for email-friendly files.
3. Set slide duration: "Use Recorded Timings and Narrations" if you recorded (Section 3); otherwise "Don't Use Recorded Timings" and set a default seconds-per-slide.
4. Optional: include narration/ink/clicks from the recording (**Use Recorded Timings...** covers this).
5. Click **Create Video**, name it (for example "Q4-AllHands.mp4"), and wait for the progress bar in the status bar. A 20-minute show at 1080p can take several minutes to render.
6. Play the MP4 in a media player and spot-check three points: opening slide, one animation-heavy slide, and the final slide. Confirm audio sync if narrated.

### Export to animated GIF

1. **File > Export > Create an Animated GIF**.
2. Pick quality/size (Small for chat, Medium for docs, Large for web hero).
3. Set seconds per slide and whether to use recorded timings.
4. **Create GIF**. Keep GIFs short (3-8 slides); file size grows fast and GIF is 256 colors, so photographic decks look rough.

### Real-world examples

- **Business:** Leave-behind PDF handouts with 3-slides-with-notes per page for a workshop; the narrated MP4 goes to the LMS.
- **Education:** Exam-review deck exported to PDF with notes pages so students get the explanations, not just the slides.
- **Personal:** An animated GIF of the birthday photo slideshow dropped into the family chat as a teaser, with the full video link after.

### Try it now

Export one deck three ways: (a) PDF with **Handouts, 3 slides per page** and notes included via Notes Pages export, (b) a 10-second-per-slide MP4 at Full HD without narrations, (c) an animated GIF at Medium quality. Open all three and note quality and file-size differences. Check which export preserved your animations (only the video and GIF).

---

## 8. Printing Handouts, Notes Pages, and Outlines

### Why it matters

Paper still happens: workshops, classrooms, board packs. Printing the wrong layout wastes paper and confuses audiences; the right layout doubles as note-taking stationery.

### Step-by-step

1. **File > Print** (Ctrl+P). The print pane shows a live preview.
2. Under **Settings**, the first big dropdown chooses the print layout:
   - **Full Page Slides:** one slide per page (usually wasteful).
   - **Notes Pages:** one slide per page with its speaker notes below. Ideal for the presenter's binder and for study packs.
   - **Outline:** text only (titles + body text from all slides). Perfect for handouts people will write on and for quick proofreading of structure.
   - **Handouts** variants: **1, 2, 3, 4, 6, 9 Slides Horizontal/Vertical**. The classic is **3 Slides** with ruled lines beside each slide for handwritten notes.
3. Options worth ticking: **Frame Slides** (adds a thin border so slides have edges on white paper), **Scale to Fit Paper**, **Print Comments** (off unless reviewing), **Print Hidden Slides** (off normally).
4. Choose color vs grayscale: **Color**, **Grayscale** (saves ink, keeps meaning if your design is not color-only), or **Pure Black and White** (line-art look; check contrast first).
5. Set copies and printer, then **Print**. To print to PDF instead, choose **Microsoft Print to PDF** or use Section 7's export.

### Layout recipes

- **Workshop handout:** 3 Slides Horizontal with lines + Frame Slides. Participants sketch notes next to each slide.
- **Speaker binder:** Notes Pages, single-sided, in a slim folder with a one-page run-of-show on top.
- **Editorial proof:** Outline view printed, then marked up with a pen before slide revisions.

### Real-world examples

- **Business:** A strategy offsite prints 3-slides-with-notes handouts for 20 attendees (20 sheets each, framed, grayscale where safe).
- **Education:** Lecture notes pages printed as the course pack.
- **Personal:** A printed Notes Pages version of the eulogy slideshow as backup if the projector fails.

### Try it now

Open **File > Print** and preview three layouts: **3 Slides** handout (tick **Frame Slides**), **Notes Pages**, and **Outline**. Print (or print-to-PDF) just the Notes Pages version and confirm every speaker note appears under its slide.

---

## 9. Protecting a Deck: Passwords, Read-Only, and the Document Inspector

### Why it matters

Decks carry strategy, pricing, and personal data (speaker notes can mention unannounced product names; document properties carry author names and comments). Before external distribution, lock what should be locked and scrub what should be scrubbed.

### Password protection (open and modify)

1. **File > Save As > Browse** (or **File > Info > Protect Presentation > Encrypt with Password**).
2. In Save As: click **Tools > General Options** and set:
   - **Password to open:** recipients must enter it to view at all.
   - **Password to modify:** they can view read-only without it but must enter it to edit (great for "please comment, don't rewrite").
3. Confirm the password and save. Warning: PowerPoint cannot recover a lost open password. Store it in your password manager.

### Mark as Final and Read-Only

- **File > Info > Protect Presentation > Mark as Final.** The file becomes read-only with a yellow bar; edits are discouraged but anyone can click **Edit Anyway**. Use it for polite finality, not real security.
- **File > Info > Protect Presentation > Always Open Read-Only:** opens in read-only until the user opts to edit. Good default for mass distribution.
- **File > Info > Protect Presentation > Restrict Access (IRM):** org-level rights management (view/edit/print per person) where your tenant supports it.

### Document Inspector (metadata and hidden content)

1. **File > Info > Check for Issues > Inspect Document**.
2. Keep all categories checked and click **Inspect**. Results may include: comments and revisions, document properties and personal information (author name, last edited by, company), invisible content, off-slide content, and speaker notes.
3. Click **Remove All** next to each category you want scrubbed (note: removing notes deletes them permanently from this copy; inspect a duplicate if you still need them internally).
4. Re-inspect to confirm clean, then save as a new file (for example "BoardDeck_external_clean.pptx").
5. Also check **Check for Accessibility** (Section 6) and **Check for Compatibility** here before wide distribution.

### Real-world examples

- **Business:** Pricing deck for a client: password to modify, Mark as Final for internal circulation, and a Document Inspector pass that removes the CFO's private notes and revision comments before it leaves the building.
- **Education:** Exam answer-key deck encrypted with a password given only to TAs.
- **Personal:** A memorial slideshow with old speaker notes scrubbed before copies go to the venue.

### Try it now

Duplicate a deck and practice on the copy: set a **password to modify** in Save As > Tools > General Options, apply **Mark as Final**, then run the **Document Inspector** and remove document properties and comments. Re-open the file and confirm the yellow Mark-as-Final bar and that the author metadata is blank.

---

## 10. Managing Large Decks: Sections, Slide Libraries, Splitting

### Why it matters

A 60-slide deck becomes unwieldy fast: navigation crawls, reordering is error-prone, and three contributors stomp on each other. Structure fixes this.

### Sections

1. Right-click between two slides in the thumbnail pane > **Add Section**. Name it (for example "Part 2: Market"). Or **Home > Section > Add Section**.
2. Collapse/expand sections with the small triangles beside section names to navigate quickly.
3. Reorder whole chapters by dragging a section header; PowerPoint moves all its slides at once.
4. Rename, remove, or move sections via **Home > Section** or right-click. In **Slide Sorter** (View > Slide Sorter), sections show as labeled bands, ideal for re-planning structure.
5. Sections travel with the file and survive in slide-sorter-based review workflows. They also print/export normally.

### Slide library (concept) and reuse

- A SharePoint **Slide Library** (classic SharePoint feature) lets a team publish single slides to a central store and insert them into many decks, with "update from library" prompts when the source changes. Modern practice approximates this with: a master "source of truth" deck in SharePoint, **Home > New Slide > Reuse Slides** to pull slides in from other files (tick **Keep source formatting** or let destination styles apply), and version history to track changes.
- Reuse Slides step-by-step: **Home > New Slide > Reuse Slides** > browse to the shared deck > click a slide to insert it. **Use Source Formatting** checkbox controls styling.

### Splitting a deck

1. **File > Save As** to create working copies (for example "Deck_Part1_Foundations.pptx").
2. In each copy, delete the slides that belong to other parts (keep sections aligned with split boundaries).
3. Keep a small "master index" deck with links (**Ctrl+K** hyperlink to other files or to a SharePoint folder) so navigation stays easy.
4. When to split: file over roughly 30-40 MB or 60+ slides, multiple independent audiences, or parallel editing pressure.

### Real-world examples

- **Business:** A 70-slide annual plan uses sections (Market, Product, GTA, Financials, Appendix); the appendix becomes a separate deck for deep-dive follow-ups.
- **Education:** A semester course is one deck per lecture, linked from an index deck; common definition slides live in a "source of truth" deck pulled in with Reuse Slides.
- **Personal:** A 200-photo memorial slideshow is split into "Early Years", "Family", "Later Years" sections for manageable editing.

### Try it now

Open any deck with 9+ slides and add three named sections (for example "Intro", "Body", "Close"). Collapse each in turn and confirm navigation works in Slide Sorter. Then drag one section to reorder the deck. Finally, split the deck: **Save As** "practice-split-A.pptx", delete one section from it, and use **Home > New Slide > Reuse Slides** to pull a slide back in from the original.

---

## 11. Pre-Flight Checklist: The 24-Hour Rule, Tech Check, Backup Plan

### Why it matters

Delivery failures are almost never about content. They are dead adapters, missing fonts, a deck that opens in Compatibility Mode with broken animations, and a 40 MB file stuck in Outbox. A pre-flight routine eliminates 95% of these.

### The 24-hour rule

Finish the deck 24 hours before you present. Not "finish rehearsing", finish the file. This gives you one full night for: a final proofread (fresh eyes catch what tired eyes miss), export of backups (Section 7), the tech check, and a rehearsal at full volume. Late-night content changes are the leading cause of next-day slide chaos: the wrong file version, half-done layouts, and zero rehearsal. If new information arrives inside the 24 hours, make the smallest possible change and stop.

### Tech check (day before, then 30 minutes early)

- **At the venue or with the real equipment:**
  1. Connect the actual adapter/cable you will use (carry your own dongle and a spare HDMI cable).
  2. Set displays to Extend, verify Presenter View (Section 2), confirm which physical screen the audience sees.
  3. Confirm fonts render correctly (or that fonts are embedded: **File > Options > Save > Embed fonts in the file**). Missing fonts silently substitute and wreck spacing.
  4. Test media: play 10 seconds of any video with sound through the room's actual audio path (HDMI audio, not laptop speakers). Test animations on the heaviest slide (parallax/morph/animated GIFs).
  5. Check projector brightness/keystone/aspect ratio in the room; walk to the back row and read your smallest text. If you cannot, fix sizes now, not later.
  6. Confirm network needs: if you demo a live site or present from a link, verify the venue's Wi-Fi with your own device, and have an offline copy anyway.
  7. Power: find an outlet, set the laptop power plan so the lid can close without sleeping (**When I close the lid > Do nothing**), and disable notifications (Windows Focus / Do Not Disturb) and auto-updates.
- **Online meetings:** test screen share of the slide-show *window*, subtitles, and narration audio with a colleague 30 minutes before.

### Backup plan (assume something fails)

1. **File backups, triple-copy rule:** (a) the .pptx on your laptop, (b) a copy in OneDrive/SharePoint with an offline-synced folder, (c) a PDF export (handout or full-page) on a USB stick and in your email drafts. The PDF is the universal parachute: it opens anywhere and preserves your content even if fonts, video, and PowerPoint are gone.
2. **Video backup:** if the deck is narrated, an MP4 copy covers "slides won't run" scenarios.
3. **Adapter kit:** HDMI cable, USB-C/HDMI adapter, VGA dongle for old projectors, clicker batteries, a 3.5mm audio cable for room sound.
4. **Plan B delivery:** if the projector dies, present from the laptop screen to the front row, hand out printed 3-slides-with-notes handouts, or fall back to the narrated MP4 you emailed earlier.
5. **Know your escape hatches:** your talk should survive with only your notes. Rehearse once with no slides at all. If you can give the 3-minute version standing in an elevator, the tech failures lose their power.

### The final pre-flight pass (30 minutes before)

- Open the deck from the USB stick or synced folder (the one you will actually present, not the one from your desktop).
- Run **Review > Check Accessibility** and fix any new errors.
- **File > Info > Check for Issues > Inspect Document** if the audience is external.
- Start the slide show and step through every transition and animation once. Esc.
- Silence your phone, close email and chat, enable Do Not Disturb, and keep water nearby.

### Real-world examples

- **Business:** A client pitch survives a dead HDMI port because the presenter's bag had a USB-C-to-HDMI adapter and the PDF leave-behind was already in the room.
- **Education:** A lecture hall PC with no PowerPoint? The narrated MP4 on the USB stick carries the class.
- **Personal:** A venue with no laptop? The printed Notes Pages copy becomes the script and the show runs from the photographer's tablet.

### Try it now

Run a mock pre-flight on any deck: set an alarm for a pretend presentation 24 hours out and write the three backup copies (pptx where, PDF where, USB). Export the PDF now. Rehearse the deck once with **Rehearse Timings** and once reading only your notes with the screen off. Note which slide you stumbled on and fix its notes before you finish.

---

## Practice Projects

1. **The Board Update (live delivery).** Build or reuse an 8-slide executive update for "YourCompany Inc Q3 results". Write prompt-style speaker notes on every slide (under 40 words each). Rehearse to exactly 8 minutes using **Rehearse Timings**, adjust timings in Slide Sorter, and present with Presenter View to an external display (or a mirrored second window).
   - **Success criteria:** notes are prompts (no paragraphs); saved timings show a total under 8:30; Presenter View confirmed with next-slide preview and notes visible only to you; per-slide times edited manually on at least one slide.

2. **The Accessible Lecture Pack (accessibility + print).** Take any 10-slide deck and make it fully accessible: real titles on every slide, alt text on every image/chart, corrected reading order, contrast checked, one video with captions or slide-show subtitles enabled. Export a **Notes Pages** PDF as the course pack.
   - **Success criteria:** Accessibility Checker shows zero errors; every visual object has meaningful alt text or is marked decorative; Selection Pane order matches visual reading order; PDF shows each slide with its notes beneath.

3. **The Async Training Video (record + export).** Record a narrated 5-slide onboarding mini-course with **Record Slide Show** (narration plus at least two ink annotations), then export to MP4 at 1080p using recorded timings.
   - **Success criteria:** every slide has narration and recorded timing; the MP4 plays with synchronized audio in a media player; at least one slide shows replayed ink; a PDF backup of the deck also exists.

4. **The Team Merge & Protect (collaboration + protection).** Save a deck to OneDrive and share **Can edit** with jane@acme.com; add one comment with an @mention and resolve it. Duplicate the deck offline, make 3 changes to the copy, then use **Review > Compare** to merge. Finish with password-to-modify protection and a Document Inspector pass that removes personal metadata.
   - **Success criteria:** version history shows at least 3 versions; the Revisions pane listed all 3 offline changes and all were accepted; the merged file saved under a new name; the file opens read-only-ish (password to modify prompts on edit); inspector reports no document properties or comments remaining.

5. **The Big-Deck Restructure (sections + split + pre-flight).** Organize a 20+ slide deck into 4 named sections, split it into two files (a main deck and an appendix) linked from an index slide, and run the full pre-flight: PDF backup produced, video or timings reviewed, tech-check script written (5 bullet steps you would run at the venue), and a no-slides verbal run-through done.
   - **Success criteria:** 4 named sections that collapse/expand and reorder cleanly in Slide Sorter; two standalone files that open correctly with at least one Reuse Slides insertion practiced; a written backup plan naming where the pptx, PDF, and USB copies live; a completed tech-check checklist.

---

## Common Mistakes & Pitfalls

| Mistake | Why it hurts | Fix |
|---|---|---|
| Writing full scripts into speaker notes | Kills eye contact; you read instead of talk | Prompts only: keywords, numbers, one transition line |
| Assuming mirrored displays will show Presenter View | Presenter View needs Extended desktop | Win+P > Extend; verify both screens before speaking |
| Presenter View on the projector | Audience sees your notes and next slide | Display Settings > Swap Presenter View and Slide Show |
| Gray/blank projector screen mid-show | Show is on the wrong display | Esc > Slide Show > Set Up Slide Show > pick correct monitor |
| No rehearsal at real pace | Talk runs 40% long and the ending gets cut | Rehearse Timings at full voice; trim to fit, not speak faster |
| Forgetting to clear test narrations | Export video with 3 seconds of "testing, testing" on slide 1 | Slide Show > Clear > Clear Narrations on All Slides before final recording |
| Sharing "Anyone with the link" internally | Sensitive deck becomes world-readable | Use "People in YourCompany Inc" or "Specific people"; set Can view for broad sends |
| Text boxes instead of title placeholders | Checker errors; screen readers and Outline break | Use real layout placeholders (Home > Layout) |
| Meaning conveyed by color alone | Color-blind and grayscale audiences lose the point | Add direct labels or patterns to charts |
| Empty or filename-based alt text | Screen readers say "image.png" | Describe the takeaway ("revenue rises 40% across Q1-Q4") |
| Exporting PDF without checking Options | Handouts arrive as one slide per page with no notes | File > Export > Options > Handouts 3-up or Notes Pages |
| Video export left at low resolution | Blurry on the conference-room 4K screen | Choose Full HD (1080p) or Ultra HD (4K); spot-check the MP4 |
| Finishing the deck the morning of | No backups, no rehearsal, and one bad edit away from disaster | The 24-hour rule: file final the day before |
| Only one copy of the deck | Laptop failure ends the presentation | Triple-copy: laptop, synced cloud, PDF on USB and in email |
| Losing the open-password | Permanently unrecoverable file | Store in password manager; prefer "password to modify" alone when possible |
| Skipping Document Inspector before external sends | Leaks author names, comments, hidden notes | File > Info > Check for Issues > Inspect Document > Remove All |
| Editing a 70-slide deck with no sections | Reordering chapters means dragging 20 thumbnails | Right-click > Add Section; drag whole sections |
| Two people editing the same offline copies | Wasted merge effort and conflicting numbers | Co-author in the cloud; use Compare & Merge only for email throwbacks |

---

## Key Takeaways

- Speaker notes are prompts: one core sentence, keyword bullets with hard numbers, and a transition line. Never a script.
- Presenter View is your cockpit: notes, next slide, timer, and slide grid on your screen; only the current slide on theirs. It requires an Extended desktop, and **Display Settings > Swap** fixes a wrong screen mid-show.
- **Rehearse Timings** makes pacing measurable; **Record Slide Show** turns one talk into an evergreen asset with narration, ink, and per-slide timings.
- Choose delivery deliberately: live for trust and Q&A, a cloud link for currency and reach, narrated video for scale. Most pro deliverables use two of the three.
- Co-author on OneDrive/SharePoint with AutoSave, discuss in comments with @mentions, roll back disasters with Version History, and reconcile offline edits with **Review > Compare**.
- Accessibility is a checklist, not a vibe: zero errors in the Accessibility Checker, real slide titles, meaningful alt text, correct reading order, 4.5:1 contrast, captions or live subtitles (**Slide Show > Always Use Subtitles**).
- Export with intent: PDF for handouts (Options > Handouts 3-up or Notes Pages), MP4 for narrated video (Full HD+, recorded timings), GIF for short teasers.
- Print the right layout: 3-slides-with-notes for workshops, Notes Pages for speaker binders, Outline for structural proofreads.
- Protect before you share: password to modify, Mark as Final (politeness only), and the Document Inspector for metadata, comments, and hidden content.
- Structure large decks with Sections; reuse common slides from a source deck; split when size or audiences diverge.
- The 24-hour rule, a real-equipment tech check, and a triple-copy backup plan (pptx + cloud + PDF on USB) prevent nearly every delivery disaster. Rehearse once with no slides at all and nothing can stop you.

---

## Further Learning

- Microsoft PowerPoint support and how-to documentation: https://support.microsoft.com/en-us/powerpoint
- Microsoft Learn training paths for PowerPoint: https://learn.microsoft.com/en-us/training/
- Microsoft Create templates and design resources: https://create.microsoft.com/


## FILE: 08-VBA-Automation/08-vba-automation.md

# Module 08: VBA Automation & Add-ins

> **Module Number:** 08
> **Title:** VBA Automation & Add-ins
> **Level:** Advanced+
> **Prerequisites:** Modules 01-07 (slides, layouts, themes, SmartArt, animation basics), comfort with the PowerPoint ribbon, basic willingness to read code. Prior Excel VBA exposure helps but is not required.
> **Estimated Study Time:** 150-180 minutes (plus practice project time)
> **Next Module:** 09 (Presentation Delivery & Speaker Tools)

---

## 8.1 Why Automate PowerPoint?

Automation is not about showing off with code. It is about removing work that a machine can do faster and more reliably than a human. In a corporate setting, the same three chores eat most of the hours: building near-identical decks over and over, keeping every slide on-brand, and applying the same edit across dozens of slides.

**The three big wins:**

1. **Batch deck generation.** Imagine YourCompany Inc runs a quarterly sales kickoff. You need 40 personalized decks, one per sales representative, each with a name slide, a territory map, and three quota slides. Doing this by hand means 40 times the copy-paste. With VBA you write one procedure that reads a list of representatives and produces all 40 decks while you get coffee.
2. **Consistent branding.** Branding drifts: someone types in Calibri when the brand font is Segoe UI, someone uses a blue that is 5 shades off, someone resizes a logo. A small macro can sweep every shape in a deck and normalize fonts, colors, and logo positions in seconds.
3. **Repetitive edits.** "Change the project code on all 60 slides from PRJ-111 to PRJ-204." "Delete every slide that mentions the old product name." "Add a confidentiality footer to all slides." These are perfect for code and terrible to do by hand.

**A fourth, quieter win: reliability.** A macro applied to 200 slides makes the same mistake (if any) 200 times consistently, which is easy to spot and fix once. A human doing it manually makes 200 different small mistakes.

**Real-world example (YourCompany Inc):** The marketing team receives a spreadsheet export every Monday with this week's webinar speakers: name, title, topic, and session time. They must turn each row into a branded "Meet the Speaker" slide in the master weekly deck. At 12 speakers a week that is 12 slides built by hand every Monday, or about 25 minutes of layout fiddling. The VBA routine in section 8.5 does it in about 4 seconds.

**When automation is the wrong tool:** see section 8.11. Short version: if the built-in Design Designer or the Morph transition can do it, use those first. They are faster to apply and cannot break with a compile error.

**Try it now:** Open any deck you have built during this course. Count how many slides you would have to touch to change the title font. Multiply that count by 2 minutes. That number is your automation payback budget: if writing a macro takes less time than that, the macro wins.

---

## 8.2 Enabling the Developer Tab and Macro Security

Before you can touch any automation features, you must un-hide the Developer tab and understand the security model. PowerPoint hides Developer by default precisely because macros are powerful, and powerful means dangerous in the wrong hands.

### Enable the Developer tab (exact steps)

1. Open PowerPoint and go to **File > Options**.
2. In the left pane of the PowerPoint Options dialog, click **Customize Ribbon**.
3. In the right-hand list titled "Main Tabs", find **Developer** (it is unchecked by default).
4. Check the box next to **Developer**.
5. Click **OK**. The Developer tab now appears in the ribbon between View and Help (position may vary by version).

### Macro security settings

Click **Developer > Macro Security** (this opens **Trust Center > Macro Settings**). You have four options:

| Setting | What it does | When to use |
|---|---|---|
| Disable all macros without notification | Blocks every macro silently | Locked-down corporate machines |
| Disable all macros with notification | Blocks macros but shows a yellow security bar with an "Enable Content" button (recommended default) | Everyday work |
| Disable all macros except digitally signed macros | Only runs macros from trusted publishers | Teams with code-signing certificates |
| Enable all macros (not recommended) | Runs everything, including malware | Only on isolated test VMs, never on a work machine |

**Recommended:** keep "Disable all macros with notification". You decide per file whether to trust it.

### Trusted locations

Instead of clicking "Enable Content" every time, you can designate folders whose files always run macros:

1. **File > Options > Trust Center > Trust Center Settings > Trusted Locations**.
2. Click **Add new location**, browse to a folder such as `C:\Users\Public\Documents\YourCompany-Macros\`, check "Subfolders of this location are also trusted" if useful, click **OK**.
3. Files opened from that folder run their macros without the security bar.

Use trusted locations for your own macro library. Do not mark your Downloads folder as trusted: that is the first place malware arrives.

### .pptx vs .pptm vs .ppam (file formats matter)

| Extension | Contains macros? | Notes |
|---|---|---|
| `.pptx` | No | The default. If you save a macro-enabled deck as .pptx, **the VBA code is silently discarded** (you get a warning dialog; read it). |
| `.pptm` | Yes | Macro-enabled presentation. Use for decks that carry their own code. |
| `.ppam` | Yes | PowerPoint Add-in. Loaded by the application, not opened as a visible deck. Used to distribute toolbars and macros (section 8.10). |
| `.ppt` / .pps | Legacy binary formats | Avoid for new work. |

**The single most common beginner loss:** writing three hours of code, saving as .pptx, closing, reopening, and finding the code gone. Save as .pptm **before** you write your first line.

**Try it now:** Enable the Developer tab, then create a blank presentation and immediately save it as `AutomationSandbox.pptm` in a folder you will use as a trusted location. Add that folder as a trusted location and confirm no security bar appears when you reopen the file.

---

## 8.3 Recording a Macro and Why PowerPoint's Recorder Disappoints

Excel users come to PowerPoint expecting the macro recorder to be a code generator. It is not. It is nearly useless here, and understanding why saves you frustration.

### How to record

1. **Developer > Record Macro** (or **View > Macros > Record Macro** in older layouts).
2. Give the macro a name like `RecordLayoutTest` (no spaces, must not start with a digit).
3. Optionally assign it a shortcut key and store it in this presentation or in a new add-in.
4. Perform actions: insert a shape, type text, move something, change a font.
5. **Developer > Stop Recording** (the same button toggles).

### What the recorder actually captures in PowerPoint

Unlike Excel (which records nearly every cell action as code), PowerPoint's recorder captures only a short list: mostly text editing, some font formatting, and slide-level actions. It does **not** record inserting shapes, moving shapes, changing slide layouts, applying animations, setting transitions, or resizing objects. That is a crippling gap for the very tasks you want to automate.

### The limits, honestly stated

- You cannot learn the object model by recording and reading code, the way you can in Excel.
- Recorded code is often verbose and uses `Select` and `Selection`, which is fragile (see section 8.12).
- There is no "relative reference" toggle like Excel's recorder offers.

### What the recorder IS good for

- Discovering exact property names for font and text formatting (record "make text bold Segoe UI 28pt dark red" and read what the generated code calls those properties).
- Quick personal keystroke-savers for tiny text edits.

**The practical takeaway:** in PowerPoint you learn by reading the object model (section 8.4) and by experimenting in the Immediate window, not by recording. Treat the recorder as a formatting-lookup tool only.

**Try it now:** Record a macro that types "YourCompany Inc" into a text box and formats it Segoe UI, 32 pt, bold, dark blue. Stop recording and view the code (**Developer > Macros > RecordLayoutTest > Edit**). Note how much of your action actually appears in the code. Save the code snippet as a formatting crib sheet for later.

---

## 8.4 The VBA Editor (VBE) and the PowerPoint Object Model

The Visual Basic Editor is where all code lives. Learn its four panels and you are halfway to productive.

### Opening and navigating the VBE

1. Press **Alt+F11** (or **Developer > Visual Basic**). The VBE opens as a separate window.
2. **Project Explorer** (Ctrl+R if missing): a tree of all open presentations and add-ins, each containing `Microsoft PowerPoint Objects` (like `ThisPresentation`) and `Modules`.
3. **Code window:** double-click any module in the Project Explorer to open its code. Each `Sub ... End Sub` block is one procedure.
4. **Immediate window** (Ctrl+G if missing): a scratchpad where single lines execute the moment you press Enter. This is the fastest way to test object model ideas.
5. **Properties window** (F4): shows properties of the selected object in the Project Explorer (mostly useful for add-in and userform work).

### Inserting a module

In the Project Explorer, right-click your presentation name (for example `VBAProject (AutomationSandbox.pptm)`), choose **Insert > Module**. A new `Module1` appears. Code in modules contains procedures you can run from **Developer > Macros**. Code placed in `ThisPresentation` runs in response to presentation events (such as `Presentation_Open`), which is how add-ins initialize themselves.

### The PowerPoint object model (the map of everything)

Think of the model as nested containers:

- **Application** - the PowerPoint program itself. Holds `Presentations` (all open decks), `SlideShowWindows`, and global settings.
- **Presentations** (collection) -> **Presentation** - one open deck. Holds `Slides`, `PageSetup`, `FullName` (its file path).
- **Slides** (collection) -> **Slide** - one slide. Holds `Shapes`, `SlideIndex`, `Layout`, `HeadersFooters`, and `TimeLine` (animation sequencing).
- **SlideRange** - a selection of one or more slides (a group of slides you are acting on together).
- **Shapes** (collection) -> **Shape** - any object on a slide: text box, picture, table, SmartArt, placeholder. This is where most automation happens.
- **TextFrame** -> **TextRange** - the text inside a shape and its formatting.
- **Sequence** -> **Effect** - entries on a slide's animation timeline (the object model name for what the Animations pane shows you).

**Mental model rule:** everything is "the thing contains a collection of smaller things". To reach a piece of text you walk down: `Application.ActivePresentation.Slides(3).Shapes("Title 1").TextFrame.TextRange.Text`.

**Try it now:** Press Alt+F11, Ctrl+G for the Immediate window, and type `? Application.ActivePresentation.Slides.Count` then Enter. It answers with the number of slides in your deck. Then type `? Application.ActivePresentation.Slides(1).Shapes.Count`. You have just queried the object model live.

---

## 8.5 Writing Sub Procedures: Slides, Shapes, and Text

A `Sub` procedure is a named block of code you can run. Everything you automate lives inside Subs.

### Anatomy of a Sub

```vba
' A Sub procedure: runs when you press F5 inside it or pick it from Developer > Macros
Sub HelloWorldSlide()
    ' Declare an object variable to hold the new slide we create
    Dim sld As Slide

    ' Add a slide with a title-only layout (ppLayoutTitleOnly = 11) to the ACTIVE presentation
    Set sld = Application.ActivePresentation.Slides.Add( _
        Index:=Application.ActivePresentation.Slides.Count + 1, _
        Layout:=ppLayoutTitleOnly)

    ' Put text into the title placeholder and format it
    With sld.Shapes.Title.TextFrame.TextRange
        .Text = "YourCompany Inc: Quarterly Update"
        .Font.Name = "Segoe UI"
        .Font.Size = 36
        .Font.Bold = msoTrue
    End With
End Sub
```

Line continuation is `_` (underscore preceded by a space) at the end of a line. Without it, one logical line must fit on one physical line.

### Add, modify, and delete slides

```vba
Sub SlideLifecycle()
    Dim sld As Slide
    Dim deck As Presentation
    Set deck = Application.ActivePresentation

    ' ADD: append a slide at the end using the Title and Content layout (ppLayoutText = 2)
    Set sld = deck.Slides.Add(deck.Slides.Count + 1, ppLayoutText)
    sld.Shapes.Title.TextFrame.TextRange.Text = "YourCompany Inc Product Roadmap"

    ' MODIFY: change the slide's layout after the fact and rename it in the selection pane
    sld.Layout = ppLayoutTitleOnly
    sld.Name = "RoadmapSlide"

    ' DUPLICATE: copy a slide (returns a SlideRange of 1 slide)
    Dim dup As SlideRange
    Set dup = sld.Duplicate
    dup(1).MoveTo deck.Slides.Count

    ' DELETE: remove the duplicate we just made
    dup.Delete
End Sub
```

### Add shapes and text boxes, and set text

```vba
Sub AddShapesAndText()
    Dim sld As Slide
    Set sld = Application.ActivePresentation.Slides(1)

    ' Add a rounded rectangle banner shape (msoShapeRoundedRectangle = 5)
    ' Arguments: type, Left, Top, Width, Height (all in points; 72 points = 1 inch)
    Dim banner As Shape
    Set banner = sld.Shapes.AddShape(msoShapeRoundedRectangle, 0, 0, 540, 60)

    ' Color the banner YourCompany brand blue and write text inside it
    banner.Fill.ForeColor.RGB = RGB(0, 74, 124)
    With banner.TextFrame.TextRange
        .Text = "YourCompany Inc Confidential"
        .Font.Color.RGB = RGB(255, 255, 255)
        .Font.Size = 18
        .ParagraphFormat.Alignment = ppAlignCenter
    End With

    ' Add a free-floating text box with the AddTextbox method
    ' Arguments: orientation (msoTextOrientationHorizontal = 1), Left, Top, Width, Height
    Dim tb As Shape
    Set tb = sld.Shapes.AddTextbox(msoTextOrientationHorizontal, 40, 300, 400, 80)
    tb.TextFrame.TextRange.Text = "Prepared by the YourCompany Enablement Team"

    ' DELETE a shape: remove any shape on this slide named "Old Logo"
    ' On Error Resume Next keeps the code running if no such shape exists (see 8.9)
    On Error Resume Next
    sld.Shapes("Old Logo").Delete
    On Error GoTo 0
End Sub
```

**Real-world example:** A legal disclaimer must appear on every slide of an external-facing deck. A 15-line Sub adds a text box with the disclaimer text in 9 pt gray at the bottom of every slide, deleting any pre-existing "Disclaimer" box first so the macro can be run repeatedly (this pattern is called making a macro *idempotent*).

**Try it now:** In the VBE, insert a module and paste the `HelloWorldSlide` Sub. Press F5 to run it. Check your slide show: a new final slide with a YourCompany title should appear. Now change the `.Text` line and run it again.

---

## 8.6 Variables, Object Variables, and Loops

### Variables and object variables

Use `Dim` to declare variables. Use `Set` when assigning **objects** (slides, shapes, presentations). Forgetting `Set` for objects is the number one beginner compile/runtime error.

```vba
Sub VariableBasics()
    ' Value variables: no Set needed
    Dim repName As String
    Dim quota As Double
    Dim targetCount As Integer
    repName = "Rep Exampleperson"   ' fake data: YourCompany Inc
    quota = 125000.5
    targetCount = 12

    ' Object variables: MUST use Set
    Dim sld As Slide
    Dim shp As Shape
    Set sld = Application.ActivePresentation.Slides(1)
    Set shp = sld.Shapes(1)

    ' Read object properties with plain dot notation
    Debug.Print repName, shp.Name, sld.SlideIndex

    ' Good hygiene: release object variables when done (optional in VBA but tidy)
    Set shp = Nothing
    Set sld = Nothing
End Sub
```

`Debug.Print` writes to the Immediate window (Ctrl+G), which is your best friend for quick inspection.

### Loops: For Each over slides and shapes

`For Each` walks a collection without you managing an index. This is the workhorse of PowerPoint automation.

```vba
' Sweep every slide and every shape: find and replace text deck-wide
Sub BulkFindReplace()
    Dim sld As Slide
    Dim shp As Shape

    ' Outer loop: every slide in the active presentation
    For Each sld In Application.ActivePresentation.Slides
        ' Inner loop: every shape on that slide
        For Each shp In sld.Shapes
            ' Only shapes that CAN hold text have a TextFrame with HasText
            If shp.HasTextFrame Then
                If shp.TextFrame.HasText Then
                    ' Replace old project code with the new one
                    ' TextRange.Replace returns the number of replacements made
                    shp.TextFrame.TextRange.Replace _
                        FindWhat:="PRJ-111", _
                        ReplaceWhat:="PRJ-204"
                End If
            End If
        Next shp
    Next sld

    MsgBox "Rebrand sweep complete for YourCompany Inc."
End Sub
```

### A counted For loop and If blocks

```vba
' Delete every slide AFTER slide 3 whose title contains "DRAFT"
Sub PurgeDraftSlides()
    Dim i As Long
    Dim sld As Slide

    ' IMPORTANT: when deleting in a loop, walk BACKWARDS (Step -1)
    ' Walking forward shifts indexes and makes you skip slides
    For i = Application.ActivePresentation.Slides.Count To 1 Step -1
        Set sld = Application.ActivePresentation.Slides(i)

        ' If blocks: only act on slides that HAVE a title
        If sld.Shapes.HasTitle Then
            If InStr(1, sld.Shapes.Title.TextFrame.TextRange.Text, "DRAFT", vbTextCompare) > 0 Then
                sld.Delete
            End If
        End If
    Next i
End Sub
```

Two If patterns to remember: `If ... Then ... End If` for multi-line blocks, and `If ... Then statement` (single line, no End If). `InStr` returns the position of a substring or 0 if absent. `vbTextCompare` makes the search case-insensitive.

**Try it now:** Run `BulkFindReplace` on a practice deck where you have manually typed "PRJ-111" on three different slides inside different shapes (title, body text box, and a table cell). Note: table cells are not reached via `TextFrame`; a real sweep also checks `shp.HasTable` and loops `shp.Table.Cell(r, c).Shape.TextFrame`. Extend the macro to handle that case.

---

## 8.7 Bulk Slide Generation from a List (and from Excel)

This is the payoff section: turning a list into finished slides.

### Generate from a list inside PowerPoint (array of fake data)

```vba
' Build one "Meet the Speaker" slide per entry in a VBA array
' Data is FAKE: YourCompany Inc sample speakers
Sub BulkSpeakerSlides()
    Dim names As Variant
    Dim titles As Variant
    Dim topics As Variant
    Dim times As Variant
    Dim i As Long
    Dim sld As Slide
    Dim deck As Presentation

    Set deck = Application.ActivePresentation

    ' Parallel arrays: index i lines up across all four (row i = one speaker)
    names = Array("Ada Exampleperson", "Bo Sampleson", "Cy Placeholder")
    titles = Array("VP of Sales", "Lead Engineer", "Customer Success Director")
    topics = Array("Territory Strategy", "Platform Deep Dive", "Renewals Playbook")
    times = Array("09:00-09:45", "10:00-10:45", "11:00-11:45")

    For i = 0 To UBound(names)
        ' Add a slide with the two-content-ish "Title Only" layout at the end
        Set sld = deck.Slides.Add(deck.Slides.Count + 1, ppLayoutTitleOnly)

        ' Name the slide so it is findable in the Selection Pane
        sld.Name = "Speaker_" & Replace(names(i), " ", "_")

        ' Title = speaker name
        sld.Shapes.Title.TextFrame.TextRange.Text = names(i)

        ' Body text box with the details, one line per property
        Dim tb As Shape
        Set tb = sld.Shapes.AddTextbox(msoTextOrientationHorizontal, 60, 160, 600, 200)
        With tb.TextFrame.TextRange
            .Text = titles(i) & vbCrLf & topics(i) & vbCrLf & "Session time: " & times(i)
            .Font.Name = "Segoe UI"
            .Font.Size = 20
            .Paragraphs(2).Font.Color.RGB = RGB(0, 74, 124)   ' highlight the topic
        End With
    Next i

    MsgBox UBound(names) + 1 & " speaker slides generated for the YourCompany kickoff."
End Sub
```

### Generate from Excel via early binding

Early binding means adding a reference to the Excel object library so the compiler knows its types. This gives you IntelliSense and compile-time checking.

**Steps to add the reference:** In the VBE, click **Tools > References**, scroll to **Microsoft Excel 16.0 Object Library** (the version number may differ), check it, click **OK**.

```vba
' Read rows from a workbook and build one slide per row.
' Workbook name and path are FAKE placeholders.
Sub BulkFromExcel()
    Dim xlApp As Object       ' declared As Object here only to keep the sample portable
    Dim wb As Workbook        ' early-bound type from the Excel reference
    Dim ws As Worksheet
    Dim r As Long
    Dim sld As Slide
    Dim tb As Shape

    ' Create a new hidden Excel instance (or use GetObject to attach to a running one)
    Set xlApp = CreateObject("Excel.Application")
    xlApp.Visible = False     ' run in the background; set True while debugging

    ' FAKE workbook name and path - replace with your own
    Set wb = xlApp.Workbooks.Open("C:\Users\Public\Documents\YourCompany-SpeakerList.xlsx")
    Set ws = wb.Worksheets("Speakers")

    ' Row 1 is the header; data starts at row 2. Column A=Name, B=Title, C=Topic, D=Time
    r = 2
    Do While ws.Cells(r, 1).Value <> ""
        Set sld = Application.ActivePresentation.Slides.Add( _
            Application.ActivePresentation.Slides.Count + 1, ppLayoutTitleOnly)

        sld.Shapes.Title.TextFrame.TextRange.Text = ws.Cells(r, 1).Value

        Set tb = sld.Shapes.AddTextbox(msoTextOrientationHorizontal, 60, 160, 600, 200)
        tb.TextFrame.TextRange.Text = ws.Cells(r, 2).Value & vbCrLf & _
                                      ws.Cells(r, 3).Value & vbCrLf & _
                                      "Session time: " & ws.Cells(r, 4).Value
        r = r + 1
    Loop

    ' Clean up the Excel instance so no orphan EXCEL.EXE lingers in Task Manager
    wb.Close SaveChanges:=False
    xlApp.Quit
    Set ws = Nothing: Set wb = Nothing: Set xlApp = Nothing

    MsgBox "Slides generated from the YourCompany speaker list."
End Sub
```

**Real-world example (YourCompany Inc):** Every Monday, `BulkFromExcel` runs against `YourCompany-SpeakerList.xlsx` (exported from the CRM) and produces the week's webinar deck skeleton in under 10 seconds. A human then spends their time on wording and visuals, not on text boxes.

**Try it now:** Create a workbook named `YourCompany-SpeakerList.xlsx` with a sheet named `Speakers`, headers `Name | Title | Topic | Time` in A1:D1, and three fake rows. Save the deck as .pptm, add the Excel reference, paste the macro, and run it. Verify three slides appear with correct content.

---

## 8.8 Formatting, Animations, and Exporting via VBA

### Colors, fonts, and positions

```vba
' Apply YourCompany brand standards across every slide
Sub BrandSweep()
    Dim sld As Slide
    Dim shp As Shape

    For Each sld In Application.ActivePresentation.Slides
        For Each shp In sld.Shapes
            ' Position the logo (named "BrandLogo") at the top-right, 0.5in margins
            If shp.Name = "BrandLogo" Then
                With Application.ActivePresentation.PageSetup
                    ' SlideWidth/SlideHeight are in points
                    shp.Left = .SlideWidth - shp.Width - 36   ' 36 pt = 0.5 inch
                    shp.Top = 36
                End With
            End If

            ' Normalize every text shape to the brand font and near-black text
            If shp.HasTextFrame Then
                If shp.TextFrame.HasText Then
                    shp.TextFrame.TextRange.Font.Name = "Segoe UI"
                    ' Skip titles so heading sizes are preserved
                    If Not (sld.Shapes.HasTitle) Then
                        shp.TextFrame.TextRange.Font.Color.RGB = RGB(33, 37, 41)
                    End If
                End If
            End If

            ' Re-tint any shape whose fill is old-brand teal to new-brand blue
            If shp.Fill.Visible = msoTrue Then
                If shp.Fill.ForeColor.RGB = RGB(0, 128, 128) Then   ' old teal
                    shp.Fill.ForeColor.RGB = RGB(0, 74, 124)        ' YourCompany blue
                End If
            End If
        Next shp
    Next sld
End Sub
```

Key facts: `RGB(red, green, blue)` takes 0-255 per channel; positions and sizes are in **points** (72 pt = 1 inch, 960x540 pt = a 16:9 slide at 13.33x7.5 inches); `Font.Name` sets the Latin typeface (use `Font.NameFarEast` for CJK text).

### Adding animations via VBA

Animations live on `Slide.TimeLine`. You build a **Sequence** of **Effect** objects. This is more verbose than the Animations pane, but it lets you animate 200 slides consistently.

```vba
' Fade in each bullet (each paragraph) of the body placeholder on click
Sub AnimateBullets()
    Dim sld As Slide
    Dim eff As Effect
    Dim body As Shape

    Set sld = Application.ActivePresentation.Slides(2)
    ' Assume the content placeholder is named "Content Placeholder 2" (check Selection Pane)
    Set body = sld.Shapes("Content Placeholder 2")

    ' Build one effect per paragraph for a by-paragraph build
    ' msoAnimEffectFade = 10 ; msoAnimTriggerOnPageClick = 1
    Dim i As Long
    For i = 1 To body.TextFrame.TextRange.Paragraphs.Count
        Set eff = sld.TimeLine.MainSequence.AddEffect( _
            Shape:=body, _
            effectId:=msoAnimEffectFade, _
            trigger:=msoAnimTriggerOnPageClick)
        ' Restrict the effect to just paragraph i (a text-level build unit)
        eff.EffectParameters.TextUnitEffect = msoAnimTextUnitEffectByParagraph
        eff.Timing.Duration = 0.5    ' half a second per fade
    Next i

    ' Add an Exit effect too: on the third click, fade the shape out
    Set eff = sld.TimeLine.MainSequence.AddEffect( _
        Shape:=body, effectId:=msoAnimEffectFade, trigger:=msoAnimTriggerOnPageClick)
    eff.Exit = msoTrue
End Sub
```

Also available: `eff.Timing.Duration` (seconds), `eff.EffectParameters.Direction`, and slide transitions via `sld.SlideShowTransition.EntryEffect` (for example `ppEffectFade`) with `sld.SlideShowTransition.AdvanceOnTime = msoTrue` and `AdvanceTime = 5` for auto-advancing kiosk decks.

### Exporting slides to images or PDF

```vba
' Export the whole deck to PDF and each slide to a PNG image folder
Sub ExportDeck()
    Dim deck As Presentation
    Dim sld As Slide
    Dim outFolder As String

    Set deck = Application.ActivePresentation
    ' FAKE output path - create the folder first
    outFolder = "C:\Users\Public\Documents\YourCompany-Exports\"

    ' 1) Whole deck to PDF (from slide 1 to the last slide, with metadata title)
    deck.ExportAsFixedFormat:=msoFalse  ' see corrected call below
    ' Correct signature: ExportAsFixedFormat(Path, FixedFormatType, Intent, FrameSlides, HandoutOrder, OutputType, PrintHiddenSlides, PrintRange, RangeType, SlideShowName, IncludeDocProperties, KeepIRMSettings, DocStructureTags, BitmapMissingFonts, UseISO19005_1)
    ' Simpler PDF route:
    deck.SaveAs outFolder & "Kickoff-Deck.pdf", ppSaveAsPDF

    ' 2) Every slide to PNG at 1600 pixels wide
    For Each sld In deck.Slides
        sld.Export outFolder & "Slide_" & Format(sld.SlideIndex, "00") & ".png", _
                   "PNG", 1600, 900
    Next sld

    MsgBox "Export complete: PDF plus PNG slides written to the YourCompany export folder."
End Sub
```

Note the two routes: `Presentation.SaveAs <path>, ppSaveAsPDF` is the simple way to write a PDF; `Slide.Export <path>, <filter>, <scaleWidth>, <scaleHeight>` writes one image per slide (filters: "PNG", "JPG", "BMP", "GIF", "TIF"). `Presentation.Export` (a method distinct from SaveAs and ExportAsFixedFormat) exports every slide as images in one call: `deck.Export outFolder, "PNG", 1600, 900`.

**Try it now:** Run `BrandSweep` on a deck where you deliberately used Times New Roman and teal fills, and verify everything normalizes. Then run `ExportDeck` and confirm a PDF and a numbered PNG set appear in your exports folder.

---

## 8.9 Error Handling Basics

Without error handling, the first problem stops your macro dead with a cryptic dialog. Two tiers of handling cover most automation.

### Tier 1: `On Error Resume Next` (use with care)

This tells VBA to skip any line that errors and continue. It is ideal for *optional* operations: deleting a shape that may not exist, applying a font that may not be installed, closing a workbook that may already be closed.

```vba
Sub SafeCleanup()
    Dim sld As Slide

    ' Resume Next ONLY around the risky optional action
    For Each sld In Application.ActivePresentation.Slides
        On Error Resume Next                    ' suppress the error...
        sld.Shapes("OldBanner").Delete          ' ...but ONLY this line can fail
        On Error GoTo 0                         ' IMMEDIATELY re-enable normal error reporting
    Next sld
End Sub
```

**The care instruction:** `On Error Resume Next` stays in effect until you turn it off with `On Error GoTo 0` or the Sub ends. If you leave it on for 200 lines, you will silently skip real bugs (a typo'd property name does nothing, and you never know why). The discipline: wrap the *smallest* possible region, then immediately `On Error GoTo 0`.

### Tier 2: `On Error GoTo` a handler (for reporting)

```vba
Sub GenerateDecksWithErrorReport()
    On Error GoTo Handler          ' any error jumps to the Handler label
    Dim i As Long
    Dim sld As Slide

    For i = 1 To 40
        Set sld = Application.ActivePresentation.Slides.Add( _
            Application.ActivePresentation.Slides.Count + 1, ppLayoutTitleOnly)
        sld.Shapes.Title.TextFrame.TextRange.Text = "YourCompany Rep Deck " & i
    Next i

    Exit Sub                       ' IMPORTANT: leave before falling into the handler

Handler:
    ' Err.Number and Err.Description capture what went wrong
    MsgBox "Generation stopped at rep " & i & "." & vbCrLf & _
           "Error " & Err.Number & ": " & Err.Description, vbExclamation
    Resume Next                    ' continue with the loop's next iteration
End Sub
```

Rules of thumb: every handler ends with `Resume Next` (continue), `Resume` (retry the failing line), or `Exit Sub` (stop); never let execution fall into a handler by accident (hence the `Exit Sub`); use `Err.Clear` if you check `Err.Number` repeatedly after `Resume Next`.

**Try it now:** Deliberately break `SafeCleanup` by misspelling a shape name while the error suppression is off, and watch the runtime error dialog. Then restore `On Error Resume Next` and confirm the macro completes silently. Notice how easy it is to hide a mistake: that is exactly why the suppression window must stay narrow.

---

## 8.10 Creating .ppam Add-ins and Where to Store Them

Once your macros prove useful, package them as a PowerPoint add-in (`.ppam`) so they are available in every deck without copying code around.

### Build the add-in

1. Start from a fresh presentation (or your macro library deck) containing all the Subs you want to ship, in one or two standard modules.
2. Open the VBE (Alt+F11), double-click `ThisPresentation`, and add an initializer if you want a custom toolbar or startup behavior:
   ```vba
   ' Runs automatically when PowerPoint loads this add-in
   Private Sub Presentation_Open()
       MsgBox "YourCompany Automation Pack loaded."   ' remove this once stable
   End Sub
   ```
3. Optional but recommended: add a custom ribbon/toolbar entry or at least document the macro names in a "How to run" text box in the source deck.
4. Go to **File > Save As**, choose the location, and set **Save as type** to **PowerPoint Add-in (*.ppam)**. Save as `YourCompany-Automation-Pack.ppam`.
5. PowerPoint saves the file and it is now a self-contained add-in.

### Where to store .ppam files

- **Default per-user location:** `%AppData%\Microsoft\AddIns` (for example `C:\Users\<you>\AppData\Microsoft\AddIns`). PowerPoint's Add-ins dialog looks here by default. Do not put real usernames in shared docs; this is just the standard path.
- **Shared/team location:** a read-only network folder such as `\\teamshare\YourCompany\AddIns\` that every user maps consistently.
- **Trusted location rule:** the folder holding your .ppam should also be a Trusted Location (section 8.2), or users will hit security prompts.

### Load the add-in

1. **Developer > Add-ins** (or **File > Options > Add-ins > Manage: PowerPoint Add-ins > Go**).
2. Click **Add New**, browse to `YourCompany-Automation-Pack.ppam`, click **OK**.
3. The add-in loads and its macros appear under **Developer > Macros**. Check **"Load behavior: Loaded"** and optionally "Load at startup" equivalent (add-ins in the list load automatically each session once added).

To update the add-in: unload it (**Remove** in the Add-ins dialog), edit the source deck's code, re-save as .ppam (same name), and add it again. Distribute updates by overwriting the .ppam in the shared folder.

**Real-world example (YourCompany Inc):** The enablement team ships `YourCompany-Automation-Pack.ppam` containing `BulkFromExcel`, `BrandSweep`, `SafeCleanup`, and `ExportDeck`. Everyone on the team loads it once; thereafter, any deck can be processed with a single macro run and no code copying.

**Try it now:** Turn your practice macros into `Practice-Pack.ppam`, save it to your AddIns folder, load it through the Add-ins dialog, close and reopen PowerPoint, and confirm the macros are still listed and runnable in a brand-new blank presentation.

---

## 8.11 When NOT to Use VBA (Use Design and Morph First)

Automation has a cost: code must be written, saved as .pptm or .ppam, debugged, and maintained. Before you write a line, rule out the built-in tools.

**Use the Design tab / Design Designer when:**
- You want a better-looking slide from existing content: **Design > Design Ideas (Designer)** proposes full layouts for free.
- You want consistent look across slides: apply a theme (**Design > Themes**) instead of code that sets fonts and colors one property at a time.

**Use Morph when:**
- You want an object to move smoothly between slides: duplicate the slide, move/resize the object on the copy, then **Transitions > Morph**. No animation code needed, and it is far more robust than animating positions with VBA.
- You want a "build-up" walkthrough of a diagram: arrange the intermediate states as slides and Morph between them.

**Use Replace/Selection Pane/Slide Master when:**
- A one-off text change across slides: **Home > Replace** does find-and-replace without code.
- Deleting or reordering a handful of slides: the slide sorter is faster than a Sub.
- Changing layout elements everywhere: edit the **Slide Master** (View > Slide Master) rather than looping over shapes.

**Use Excel/Word mail merge style tools when:**
- You are making one deck per person at small scale (2-5 copies): **File > Save a Copy** and the Replace feature beat writing and debugging a loop.

**Use VBA when:**
- The task repeats (weekly, monthly), the volume is high (20+ slides or 10+ decks), the rules are precise (exact colors, exact positions, exact text), or the source data is structured (a spreadsheet or CSV). Those are the four green lights.

**Decision shortcut:** If you can fully describe the task as "for each slide/row/shape, do X," it is automation territory. If the task needs judgment about visual balance, leave it to Design Designer and human taste.

**Try it now:** Take a plain three-bullet slide and improve it twice: once with **Design > Design Ideas**, and once by manually setting the font and colors. Time both. Now imagine doing the manual version 200 times. That comparison is your build-vs-automate decision tool.

---

## 8.12 PowerPoint + Excel Integration Patterns

PowerPoint rarely holds the master data; Excel does. Three proven integration patterns cover most real jobs.

### Pattern 1: PowerPoint reads Excel (data to slides)

Shown fully in section 8.7 (`BulkFromExcel`). Summary: create or attach to Excel with `CreateObject("Excel.Application")` or `GetObject(, "Excel.Application")`, open the workbook, loop rows, build slides. Always `Quit` and set variables to `Nothing` when you created the instance.

### Pattern 2: PowerPoint writes to Excel (slides to data)

```vba
' Inventory every slide into a workbook: one row per slide with title text and shape count
Sub DeckInventoryToExcel()
    Dim xlApp As Object
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim sld As Slide
    Dim r As Long

    Set xlApp = CreateObject("Excel.Application")
    xlApp.Visible = True
    Set wb = xlApp.Workbooks.Add
    Set ws = wb.Worksheets(1)

    ' Header row
    ws.Cells(1, 1).Value = "SlideIndex"
    ws.Cells(1, 2).Value = "SlideName"
    ws.Cells(1, 3).Value = "TitleText"
    ws.Cells(1, 4).Value = "ShapeCount"

    r = 2
    For Each sld In Application.ActivePresentation.Slides
        ws.Cells(r, 1).Value = sld.SlideIndex
        ws.Cells(r, 2).Value = sld.Name
        ' Guard: only read the title if the slide has one
        If sld.Shapes.HasTitle Then
            ws.Cells(r, 3).Value = sld.Shapes.Title.TextFrame.TextRange.Text
        Else
            ws.Cells(r, 3).Value = "(no title)"
        End If
        ws.Cells(r, 4).Value = sld.Shapes.Count
        r = r + 1
    Next sld

    ' FAKE save path for the exported inventory
    wb.SaveAs "C:\Users\Public\Documents\YourCompany-DeckInventory.xlsx"
    MsgBox "Inventory exported for the YourCompany deck."
End Sub
```

### Pattern 3: PowerPoint sends values to Excel formulas (numbers to models)

Finance decks often compute in Excel and present in PowerPoint. The pattern: open the model workbook, write scenario inputs into designated input cells (for example `ws.Range("B3").Value = 125000`), let Excel recalc (`xlApp.Calculate`), read the result cells (`ws.Range("B9").Value`), and write those results into chart labels or KPI text boxes on the slide. This keeps every formula in Excel (maintainable, auditable) and leaves PowerPoint purely presentational.

### Integration hygiene rules

- Never hard-code a path with a real username in shared code; use `Environ$("USERPROFILE")` or a configuration cell/named range to hold paths.
- Always clean up: `wb.Close False`, `xlApp.Quit`, `Set ... = Nothing`, otherwise orphan `EXCEL.EXE` processes accumulate.
- Prefer early binding (Tools > References) for development, and note that shipping to machines with different Office versions sometimes means late binding (`Dim wb As Object`) is the safer distribution choice.
- Wrap the whole integration in the Tier 2 error handler from section 8.9, so a missing workbook reports cleanly instead of crashing mid-generation.

**Try it now:** Run `DeckInventoryToExcel` on your practice deck and verify the workbook row count equals your slide count and every title is captured (or "(no title)" appears correctly). Then modify it to also dump each slide's first body text into a fifth column.

---

## Practice Projects (5)

Each project builds on the section noted. All data must be fictional (YourCompany Inc).

**Project 1: The Slide Factory**
Build a macro that generates 10 agenda slides from a VBA array of fake agenda items (item name, owner, minutes), each slide titled "Agenda Item N" with a formatted body box.
*Success criteria:* Running the macro once adds exactly 10 slides; running it again adds 10 more (it is repeatable and does not error); every body box uses Segoe UI 20 pt; item titles appear in the slide title placeholder.

**Project 2: The Brand Guardian**
Write `BrandSweepV2`: normalize all text to Segoe UI, recolor any shape fill that is not brand blue RGB(0, 74, 124) or white to brand blue, and reposition any shape named "BrandLogo" to top-right 0.5 inch margins on every slide.
*Success criteria:* On a deliberately messy 5-slide deck (wrong fonts, teal fills, logo misplaced), one run leaves zero non-brand fonts, zero teal fills, and the logo correctly placed on all 5 slides; running it twice produces no change (idempotent) and no errors.

**Project 3: The Monday Deck (Excel to PowerPoint)**
Create `YourCompany-SpeakerList.xlsx` (sheet `Speakers`, columns Name/Title/Topic/Time, 8 fake rows) and a macro using the Excel object library that produces one slide per row, names each slide `Speaker_<Name>`, and adds a per-slide fade animation on the body text.
*Success criteria:* 8 slides generated with correct content, slide names visible in the Selection Pane, each body text box has a Fade entrance effect, and the Excel instance fully exits (no orphan EXCEL.EXE in Task Manager).

**Project 4: The Distribution Kit**
Extend Project 3's flow to export the finished deck: one PDF of the whole deck plus one PNG per slide named `Slide_01.png`, `Slide_02.png`, ... into `C:\Users\Public\Documents\YourCompany-Exports\` (create the folder from code if missing using `MkDir`).
*Success criteria:* PDF exists and opens with the right slide count; PNG count equals slide count; filenames are zero-padded and sequential; re-running overwrites without erroring.

**Project 5: The Automation Pack**
Package your best three macros into `YourCompany-Automation-Pack.ppam`, saved in your AddIns folder, loaded via the Add-ins dialog.
*Success criteria:* After a full PowerPoint restart, the macros list under Developer > Macros in a brand-new blank presentation; each macro runs successfully on an unrelated deck; a colleague-style test (unload, re-add from the folder) works; a short README module (a "How to use" slide inside the source deck) documents each macro's purpose.

---

## Common Mistakes & Pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Saving macro code in a .pptx | All code is silently discarded on save | Save as .pptm (or .ppam for add-ins) BEFORE writing code |
| Forgetting `Set` for object variables | "Object required" or "ByRef argument type mismatch" errors | Use `Set x = <object expression>`; plain `=` is only for values |
| Deleting slides/shapes in a forward loop | Indexes shift as items are removed, so you skip items or error out | Loop backwards: `For i = count To 1 Step -1` |
| `Select`/`Selection` recorded code (recorder habits) | Fails when no window/selection is active; breaks in batch runs | Reference objects directly: `deck.Slides(3).Shapes(1)...` |
| Leaving `On Error Resume Next` on for whole procedures | Real bugs vanish silently; you ship broken output | Wrap only the risky line(s), then immediately `On Error GoTo 0` |
| Assuming shapes have text | `TextFrame.TextRange` errors on pictures and many autoshapes | Guard with `If shp.HasTextFrame Then If shp.TextFrame.HasText Then` |
| Ignoring tables, grouped shapes, and charts in sweeps | Bulk edits silently miss content | Also check `shp.HasTable` (loop cells), `shp.GroupItems` for groups, and `shp.HasChart` |
| Writing VBA for what Morph/Designer does in 2 clicks | Unmaintainable code for a solved problem | Rule out Design Designer, Morph, Replace, and Slide Master first (section 8.11) |
| Orphan Excel instances from `CreateObject` | Hidden EXCEL.EXE processes accumulate and lock files | Always `wb.Close False`, `xlApp.Quit`, `Set ... = Nothing` |
| Hard-coded file paths with real usernames | Breaks on every other machine; leaks identity in shared code | Use `Environ$("USERPROFILE")`, config cells, or trusted shared folders |
| Forgetting `Exit Sub` before a handler label | Execution falls into the handler after normal completion | Always `Exit Sub` (or `Exit Function`) on the line above the handler |
| Animating 200 slides by hand instead of by `TimeLine` code | Hours of clicking and inconsistent timings | Loop `sld.TimeLine.MainSequence.AddEffect` with fixed `Timing.Duration` |
| Not naming generated slides | Generated decks are impossible to navigate or debug | Set `sld.Name = "Prefix_" & key` as you create each slide |
| Trusting the macro recorder as a learning tool in PowerPoint | It captures almost nothing of the object model | Learn via the Immediate window and the object model map (section 8.4) |

---

## Key Takeaways

1. Automate only repetition at scale: if the task is "for each slide/row/shape, do X" and repeats weekly or covers 20+ items, VBA wins; otherwise use Design Designer, Morph, Replace, or the Slide Master.
2. File format first: save as .pptm (or .ppam for add-ins) before writing any code, or you will lose it.
3. PowerPoint's macro recorder is nearly useless for learning; the object model (Application > Presentation > Slide > Shape > TextFrame, plus TimeLine/Sequence for animation) is the real map.
4. `For Each` loops over `Slides` and `Shapes` are the workhorse; loop backwards when deleting, and always guard text access with `HasTextFrame` / `HasText`.
5. `Set` is mandatory for object variables; `Dim` plus `Set` is the pair that prevents the most common runtime errors.
6. Error handling has two tiers: narrow `On Error Resume Next` for optional actions (turn it off immediately with `On Error GoTo 0`), and `On Error GoTo Handler` with `Exit Sub` before the label for reporting and recovery.
7. Bulk generation from a list (arrays inside VBA, or rows in Excel via early binding) turns a 25-minute Monday chore into seconds, and idempotent macros can be run repeatedly without damage.
8. Formatting, colors (RGB), positions (points, 72 per inch), per-paragraph animations (`TimeLine.MainSequence.AddEffect`), and exports (`SaveAs ... ppSaveAsPDF`, `Slide.Export`) are all scriptable, making brand governance and distribution fully automatable.
9. Package proven macros as a .ppam in `%AppData%\Microsoft\AddIns` (or a shared trusted folder) so every deck can use them without code copying.
10. PowerPoint + Excel integration follows three patterns: Excel to slides (data to visuals), slides to Excel (inventory/audit), and values to Excel formulas (models compute, slides present). Always clean up Excel instances.

---

## Further Learning

- Microsoft PowerPoint support and how-to documentation: https://support.microsoft.com/en-us/powerpoint
- Microsoft Learn training path for PowerPoint: https://learn.microsoft.com/en-us/training/
- Microsoft Create templates and design resources (starter decks for your automation targets): https://create.microsoft.com/


## FILE: 09-Real-World-Projects/09-real-world-projects.md

# Module 9: Real-World Projects (Capstone Workbook)

**Module ID:** ppt-hero-09-projects
**Level:** All Levels (capstone, integrates Modules 1-8)
**Estimated Time:** 15-40 hours of project work (self-paced)
**Prerequisites:** Modules 1-8, or equivalent skill. Each brief names the modules it draws on.

## Metadata

| Field | Value |
|---|---|
| Applies to | PowerPoint for Microsoft 365, PowerPoint 2021/2019/2016 (feature notes where versions differ) |
| Format | 6 project briefs + capstone assignment + rubrics |
| Companion files | sample-01-starter-deck.pptx, sample-02-pitch-deck.pptx, sample-03-training-deck.pptx, sample-04-qbr-deck.pptx, sample-05-animated-demo.pptx, sample-06-brand-template.pptx, exercise-fix-this-deck.pptx |
| Rubric scale | 1 = missing/incorrect, 2 = attempted, 3 = competent, 4 = polished, 5 = portfolio-grade |
| Data rule | All orgs, people, and numbers in this module are fictional. Never use real client data in practice work. |

---

## How to Use These Projects (and Build a Portfolio)

Each project in this module is written as a client-style brief, the way a real assignment would arrive from a stakeholder. Work through them in order or pick the ones that match the work you want. Every brief has the same six parts: the scenario (the brief), the deliverables, a step-by-step build walkthrough with click paths that reference earlier modules, design decisions explained (the "why" behind layout, color, and chart choices), a slide-by-slide starter outline, and three ways to extend the project. Each ends with a 10-criterion self-grading rubric scored 1-5.

**How to get the most out of each project:**

1. **Read the brief once, then build.** Do not study the walkthrough first. Build your own pass, hit friction, then read the walkthrough to compare approaches. The gap between your attempt and the walkthrough is where the learning lives.
2. **Time yourself on the second run.** Rebuild one project against a clock after a week. Speed is a professional skill (Module 8 covers efficiency habits).
3. **Grade yourself honestly with the rubric.** Anything scoring 3 or below is a specific skill gap. Go back to the named module section, fix it, re-grade.
4. **Save every draft.** Keep `projectname-v1.pptx`, `v2`, `final`. Reviewers love seeing iteration, and you will learn more from diffing your own versions than from any tutorial.

**Portfolio advice.** A presentation portfolio is not a pile of .pptx files. It is 3-5 finished decks plus one before/after story. Export each finished deck to PDF (File > Export > Create PDF/XPS or Save As > PDF) and to a few PNG slide images (File > Save As > PNG, "All Slides") so reviewers can see your work without opening PowerPoint. The before/after piece is the highest-value item: take the broken `exercise-fix-this-deck.pptx`, fix it, and show original vs. rebuilt side by side with three sentences on what you changed and why. That demonstrates judgment, which is what clients hire.

**How to present your work.** When someone reviews your portfolio, do not read the slides aloud. Pick one project, give 60 seconds of context (who the audience was, what decision the deck had to support), then narrate two design decisions ("I put the KPI trend on one axis-free chart because the audience needed direction, not decimals"). Practicing this meta-commentary is exactly the speaker-notes discipline from Module 7.

Reference hubs for anything this workbook cannot cover: [PowerPoint support](https://support.microsoft.com/en-us/powerpoint) and [Microsoft Create templates](https://create.microsoft.com/).

---

## Project 1: Startup Pitch Deck (10-12 Slides)

**Modules applied:** 2 (structure), 3 (visual design), 4 (charts/graphics), 7 (storytelling & delivery)

### Scenario

YourCompany Inc is a fictional seed-stage startup that sells smart locker hardware to apartment buildings so residents can receive packages securely. Founder Maya Okafor is pitching angel investors next month. She has a working prototype and 3 pilot buildings (fictional: 412 units total) but no polished deck. Her ask: 750,000 in seed funding on a SAFE. She needs a 10-12 slide deck that runs in 8 minutes plus questions. The investors are not hardware people; they will care about the pain of package theft, the size of the opportunity, whether the unit economics work, and whether this team can execute.

### Deliverables

1. `yourcompany-pitch-v1.pptx` (10-12 content slides, 16:9)
2. A one-slide "problem" visual that a stranger can understand in 5 seconds
3. One market-size chart and one unit-economics chart (or combined financial slide)
4. Speaker notes on every slide, written as spoken sentences (Module 7)
5. A 2-slide appendix (pilot data detail, financial assumptions) that stays hidden unless asked
6. PDF export for email follow-up

### Step-by-Step Build Walkthrough

1. **Set up the file before any content.** Design > Slide Size > Widescreen (16:9). Home > Layout > apply a clean layout. This is Module 1 (interface, views) and Module 3 (theme setup).
2. **Pick ONE accent color and two neutrals.** Design > Variants > Colors > Customize Colors (Module 3). YourCompany: deep navy text (#1F2A44), one accent (signal orange #E8590C), light neutral background (#F7F7F5). Every highlight in the deck uses the accent. No second accent color.
3. **Set slide master fonts once.** View > Slide Master > Fonts > customize heading/body (Module 5, foreshadowing Project 6). This guarantees consistency without per-slide fixing.
4. **Build the arc first as titles only.** Create 10 blank slides and type title-only headlines that tell the story in order (Module 2 structure, Module 7 narrative arc). Read just the headlines aloud: if they do not form a coherent 60-second story, fix them before designing anything.
5. **Problem slide: make it felt.** Use one large number ("1 in 3 packages") as 96pt text plus a simple 3-icon strip (Module 4 SmartArt/icons). Insert > Icons > search "package", "home", "warning". Avoid a wall of bullet points; investors skim.
6. **Solution slide: show the product.** Insert > Pictures for a product photo, or Insert > Shapes to draw a simple locker schematic (Module 4). Keep annotations to 3 labels max.
7. **Market slide: honest TAM/SAM/SOM.** A stacked bar or 3 nested bars (Module 4 chart choice). TAM 2.1B, SAM 340M, SOM 18M (all fictional). Insert > Chart > Bar. Label with text boxes, delete chart junk (gridlines, legend if only one series).
8. **Traction slide: line chart of pilot growth.** Units under management by month over the 6 pilot months (412 units total). Insert > Chart > Line. Zero baseline on the Y axis (Module 4 honest axes).
9. **Business model / unit economics.** Hardware 349 per locker door, 12/month monitoring per building, 38% gross margin. Use a clean table (Insert > Table, 4 rows) or a waterfall-style column chart (Module 4). Numbers right-aligned in tables.
10. **Team slide: faces + one line of proof each.** Insert > Pictures, crop to circles (Picture Format > Crop > Crop to Shape > Oval, Module 3/4). One line per person: "Maya Okafor, CEO: 6 years logistics ops at Vantera" (fictional).
11. **The ask slide: one number, one use-of-funds bar.** 750,000 on a SAFE, with a simple horizontal bar showing allocation (45% hardware inventory, 30% engineering, 25% sales) (Module 4).
12. **Speaker notes pass.** View > Notes Page to write spoken-style notes (Module 7). Read each aloud; if a note takes longer than 45 seconds to say, it is too long.
13. **Rehearse and time.** Slide Show > Rehearse Timings; target 8 minutes (Module 7, Module 8). Export PDF for the follow-up email.

Match: build alongside `sample-02-pitch-deck.pptx` to compare your structure with a finished reference.

### Design Decisions Explained

- **Titles are assertions, not labels.** "Pilots cut theft to zero" beats "Pilot Results" (Module 7 assertion style). Investors scanning headlines alone should get the whole argument.
- **One accent color.** Attention is scarce in a pitch. If four things are orange, nothing is important. The accent appears at most twice per slide: the key number and the call to action.
- **Photos of the product beat diagrams of the business model.** Early-stage investors fund things they can picture. The schematic goes in the appendix.
- **Zero-based, uncluttered charts.** A truncated Y axis on a traction chart is the fastest way to lose trust with a numerate audience. Show the small honest number with a clear story instead.
- **Faces on the team slide.** Investment decisions are people decisions. Circles crop cleanly in rows and read as a consistent system (Module 3 alignment).

### Starter Outline (10 Slides)

| # | Title (assertion) | Content |
|---|---|---|
| 1 | Title: YourCompany Inc - secure package delivery for every building | Logo, founder name, date |
| 2 | One in three apartment residents lost a package last year | Big stat + 3 icons |
| 3 | YourCompany puts every delivery in a smart locker | Product photo + 3 labels |
| 4 | 412 pilot units, zero thefts since install | Line chart (pilot months) |
| 5 | A 2.1B market that parcel volume keeps growing | TAM/SAM/SOM bars |
| 6 | We make money twice: hardware and monitoring | Unit-economics table |
| 7 | No competitor owns the multi-family building | Simple 2x2 positioning (Module 4) |
| 8 | The team that has shipped logistics hardware before | 3 headshots + proof lines |
| 9 | Milestones: 5,000 doors in 18 months | Timeline SmartArt (Module 4) |
| 10 | We are raising 750,000 to hit those milestones | Use-of-funds bar |

Appendix (hidden): pilot building detail; financial assumptions.

### Three Ways to Extend

1. **Add a 90-second product video** with a poster frame and play-on-click (Module 6 multimedia).
2. **Build the "demo day" variant:** 5 slides, 3 minutes, 40pt minimum font - forces editing discipline (Module 8).
3. **Design a leave-behind one-pager** in the same theme (Module 3 consistency), as a handout export (Module 6 handouts).

### Self-Grading Rubric (10 criteria, 1-5 each)

| # | Criterion | Module |
|---|---|---|
| 1 | Headline story reads as a coherent arc with titles alone | 2, 7 |
| 2 | 10-12 slides, runs in 8 minutes with notes | 7 |
| 3 | Consistent theme: 1 accent + 2 neutrals, master fonts set | 3, 5 |
| 4 | Problem slide understandable in 5 seconds | 4 |
| 5 | All charts zero-based, labeled, no chart junk | 4 |
| 6 | Team slide uses cropped photos + one proof line each | 3 |
| 7 | Ask slide has one number and clear use of funds | 2 |
| 8 | Speaker notes in spoken language on every slide | 7 |
| 9 | 2 hidden appendix slides for tough questions | 1 |
| 10 | PDF export clean, no overflow or orphaned shapes | 8 |

---

## Project 2: Training / Workshop Deck

**Modules applied:** 2 (structure), 3 (visual design), 6 (notes, handouts, interactivity), 7 (delivery)

### Scenario

Greenfield Literacy Trust, a fictional nonprofit that trains volunteer reading tutors, needs a 90-minute onboarding workshop deck. Audience: 15-20 new volunteers, mixed comfort with technology, ages 18-70. The trainer, Daniel Reyes, wants: learning objectives up front, clear section breaks, activities every 20 minutes, and a printable handout volunteers take home. The deck must work both projected in a room and emailed as a self-study file, which means the speaker notes must carry the teaching.

### Deliverables

1. `greenfield-tutor-onboarding.pptx` (25-35 slides for 90 minutes)
2. Learning objectives slide (3-4 measurable objectives)
3. Section divider slides (4-5) with consistent design (Module 3)
4. Two activity slides with instructions and time boxes
5. Full speaker notes (Module 7) written so a substitute trainer could teach from them
6. Handout: Notes Pages or PDF handout export, 3 slides per page with lines (Module 6)

### Step-by-Step Build Walkthrough

1. **Start with the agenda as a table of contents slide** (Module 2): 4 sections with minutes per section. 90 minutes = 10 intro + 20x3 sections + 20 wrap/activities.
2. **Write learning objectives as observable actions.** "By the end, tutors can run a 20-minute reading session unaided" beats "understand session structure" (Module 2). Use Bloom-style verbs: list, demonstrate, plan, deliver.
3. **Design ONE divider layout and reuse it.** New Slide > Section Header layout, with big section number + title + "what you will be able to do after this section" line (Module 2, 3). Copy the slide and edit text; do not rebuild each time.
4. **Body slides: one idea per slide, 24pt+ minimum.** Use the 6x6 ceiling as a starting rule (Module 3) since a mixed-age room reads from the back row.
5. **Teach with diagrams, not paragraphs.** The "20-minute session flow" (warm-up 3, read-together 10, reflect 5, close 2) is a Process SmartArt (Insert > SmartArt > Process > Basic Chevron, Module 4).
6. **Activity slides use a repeatable template:** "Activity N" label, task in one sentence, time box in large type ("10 minutes"), output ("write 3 sentences on the card"), and a debrief question in the notes (Module 6 interactivity + Module 7 notes).
7. **Write the notes like a script.** Notes Page view, spoken language, including the debrief question and a common-mistake warning per section (Module 7).
8. **Add gentle interactivity.** For the in-room version, use a "raise your hand" poll-style slide (Module 6); optional: a hyperlink jump from agenda to sections (Ctrl+K on the section name) so the trainer can navigate questions out of order (Module 2 linking, Module 5).
9. **Build the handout.** File > Print > Full Page Slides dropdown > "3 Slides" handout with note lines (Module 6). Also export a Notes Pages PDF (File > Print > Notes Pages) as the trainer copy. Two exports, two audiences.
10. **Test the print.** Print one physical page of the handout to check contrast and margins; light-tinted backgrounds often print as gray mud, so keep handout-heavy slides near-white.

Match: `sample-03-training-deck.pptx` shows a finished section-divider system and activity layout.

### Design Decisions Explained

- **Objectives slide is slide 3, not slide 1.** Slide 1 title, slide 2 agenda, slide 3 objectives. Adults commit to learning when they know the payoff; the title earns attention first (Module 2).
- **Dividers with numbers reduce cognitive load.** Volunteers who drift can re-orient instantly ("we are in section 2 of 4"). Consistent divider geometry (Module 3) makes the number the only changing element, so scanning is instant.
- **24pt+ body text.** A room with a back row and older eyes is the worst case; design for it (Module 3 readability).
- **Activity slides are visually distinct** (accent-colored band) so the room shifts mode from listening to doing without a verbal cue. Color as a mode signal, not decoration.
- **Notes are the real deliverable.** A training deck's slides are prompts; the notes are the curriculum. This inverts the usual ratio: roughly 200-300 words of notes per content slide.

### Starter Outline (12 of 25-35 Slides)

| # | Slide | Purpose |
|---|---|---|
| 1 | Greenfield Tutor Onboarding | Title + date |
| 2 | Today: four sections in 90 minutes | Agenda with time boxes |
| 3 | By 10:30 you will be able to... | 4 measurable objectives |
| 4 | Section 1: Why reading tutoring works | Divider 1 |
| 5 | 20 minutes a week changes a reading level | One stat + source line |
| 6 | Section 2: The 20-minute session | Divider 2 |
| 7 | Every session has four parts | Chevron SmartArt |
| 8 | ACTIVITY 1: Sequence a session (10 min) | Activity template |
| 9 | Section 3: Choosing the right book | Divider 3 |
| 10 | ACTIVITY 2: Match 3 readers to books (15 min) | Activity template |
| 11 | Section 4: When a session goes sideways | Divider 4 |
| 12 | Your first session is booked | Wrap + contacts + handout reminder |

### Three Ways to Extend

1. **Record a narrated export** (Module 6: Slide Show > Record Slide Show) so absent volunteers get the taught version, not the bare slides.
2. **Add a knowledge-check quiz** with trigger-based answer reveals (Module 5/6) at the end of each section.
3. **Produce an accompanying one-page session planner** template as a handout page in the same deck (Module 6 handouts).

### Self-Grading Rubric

| # | Criterion | Module |
|---|---|---|
| 1 | 3-4 measurable learning objectives on slide 3 | 2 |
| 2 | 4-5 consistent section dividers with numbers | 2, 3 |
| 3 | Activity every ~20 minutes with time boxes | 6 |
| 4 | At least one SmartArt/diagram teaching a process | 4 |
| 5 | 24pt+ body text throughout | 3 |
| 6 | Speaker notes complete enough for a substitute | 7 |
| 7 | Handout export at 3 slides/page with lines | 6 |
| 8 | Notes Pages PDF trainer copy produced | 6 |
| 9 | Agenda slide includes section hyperlinks | 2, 5 |
| 10 | Prints legibly on a monochrome office printer | 3, 8 |

---

## Project 3: Quarterly Business Review (QBR)

**Modules applied:** 2, 3, 4 (charts and tables), 8 (accuracy and efficiency)

### Scenario

Meridian Freight Software (fictional) sells route-planning SaaS to mid-size carriers. VP of Customer Success Priya Nandan must deliver the Q3 QBR to the executive team and two board observers. Content: revenue and retention KPIs, a pipeline snapshot, top-10 accounts by ARR with health flags, wins and risks, and next quarter's plan. The audience is numerate and impatient; they will challenge any chart that hides a decline. Q3 fictional numbers: 4.2M ARR (up from 3.8M), net revenue retention 104%, churn 2 logos, pipeline 6.1M, win rate 31%.

### Deliverables

1. `meridian-qbr-q3.pptx` (12-16 slides + 4-6 appendix slides)
2. One KPI dashboard slide (4-6 metrics with trend indicators)
3. At least 3 charts, all with honest axes and source footnotes (Module 4)
4. A top-10 accounts table with health flags (Module 4 tables)
5. Risks slide with owners and mitigation dates
6. Appendix with methodology/definitions, hidden in the presented deck

### Step-by-Step Build Walkthrough

1. **Lock the layout system first.** Widescreen, one title-placeholder layout, consistent footer: "Meridian QBR Q3 | Confidential | Page N" via Insert > Header & Footer > apply to all (Module 1, 3). Executives notice footers and page numbers on dense decks.
2. **KPI dashboard slide.** Use one row of 5 metric "cards": metric name, value, delta vs. Q2, and a tiny sparkline. Build cards as grouped rectangles + text boxes (Insert > Shapes, Group with Ctrl+G, Module 4). ARR 4.2M (+10.5%), NRR 104%, gross churn 5.1%, pipeline 6.1M, win rate 31% (-2pts).
3. **Revenue trend chart.** Insert > Chart > Line, quarterly ARR for 6 quarters (fictional: 2.6, 2.9, 3.2, 3.5, 3.8, 4.2M). Y axis starts at zero. Data labels only on first and last points (Module 4 label selectively).
4. **Retention chart.** A clustered column of gross vs. net revenue retention by quarter. Both zero-based. Where a decline exists (win rate 33 to 31), say so in the title: "Win rate dipped to 31% as we moved upmarket". Honesty is a design decision (Module 4).
5. **Top-10 accounts table.** Insert > Table, 11 rows x 5 columns: Account, ARR, QoQ change, Health (R/A/G), Owner. Right-align numeric columns, use the accent color only for "At risk" flags (Module 3 color discipline, Module 4 tables). Thin borders only horizontal; kill the default heavy grid (Table Design > Borders).
6. **Pipeline snapshot.** A stacked bar by stage (Discovery 2.1M, Eval 1.9M, Negotiate 1.4M, Verbal 0.7M = 6.1M). Insert > Chart > Bar > Stacked (Module 4).
7. **Wins and risks as a two-column layout.** Risks each get: the risk, owner, mitigation date. Use a table rather than bullets so accountability is scannable (Module 2 grouping).
8. **Appendix with definitions.** One slide defining NRR, gross churn, pipeline coverage exactly as finance computes them (Module 4 chart honesty extends to definitions). Right-click section > Add Section, and hide the appendix section: Slide Show > Hide Slide on each appendix slide (Module 1).
9. **Accuracy pass.** Reconcile every chart number against the source spreadsheet; footnote each chart ("Source: Meridian finance warehouse, pulled 2031-10-04") (Module 8 review checklist).
10. **Build the leave-behind PDF** with appendix included (export after temporarily unhiding), while the presented .pptx keeps the appendix hidden (Module 8 output).

Match: `sample-04-qbr-deck.pptx` for a finished dashboard slide and flagged accounts table.

### Design Decisions Explained

- **KPI cards before any chart.** Executives want the verdict first; charts are evidence for questions (Module 2: answer first). Trend indicators (up/down arrows via Insert > Icons) let the room scan in 5 seconds.
- **Honest axes build political capital.** A QBR with a flattering truncated axis gets challenged in the room and distrusted for a year. Zero baselines and a title that admits the win-rate dip pre-empt the challenge (Module 4).
- **Tables for accounts, charts for trends.** Account-level rows are lookup tasks, not comparison tasks; tables win (Module 4 chart-choice logic). Charts compare patterns, tables retrieve facts.
- **Red flags use the accent color, everything else is neutral.** Scarcity of color means risk pops. No traffic-light rainbow on every cell (Module 3).
- **Footers and page numbers on dense decks.** Board observers cite slides in later meetings; page references make the deck quotable (Module 1).

### Starter Outline (14 Slides)

| # | Slide | Content |
|---|---|---|
| 1 | Q3 QBR: ARR 4.2M, retention steady | Title + date |
| 2 | Five numbers for Q3 | KPI dashboard cards |
| 3 | ARR grew 10.5% to 4.2M | Line chart, 6 quarters |
| 4 | NRR held at 104% while gross churn eased | Clustered column |
| 5 | Win rate dipped to 31% as we moved upmarket | Column chart + cause note |
| 6 | Pipeline of 6.1M covers 1.5x next quarter's target | Stacked bar by stage |
| 7 | Top 10 accounts drive 61% of ARR | Flagged table |
| 8 | Q3 wins: two carriers over 200 trucks | 3 bullets with proof |
| 9 | Three risks, each with an owner and date | Risk table |
| 10 | Q4 plan: upmarket focus, churn save program | 3 workstreams |
| 11 | Asks: two headcount, one pricing decision | Decision slide |
| 12 | Summary | 3 assertions |
| 13-14 | Appendix: metric definitions; full pipeline detail | Hidden |

### Three Ways to Extend

1. **Add a drill-down deck** linked from the accounts table (Ctrl+K to a detail slide per at-risk account) (Module 5 navigation).
2. **Build the dashboard as a reusable quarterly template** (.potx) - bridge to Project 6.
3. **Animate the ARR line quarter by quarter** with a By Category chart animation (Module 5) so Priya narrates the story of the quarter instead of revealing it all at once.

### Self-Grading Rubric

| # | Criterion | Module |
|---|---|---|
| 1 | KPI dashboard with 4-6 metrics and trend indicators | 4 |
| 2 | 3+ charts, all zero-based with source footnotes | 4 |
| 3 | Chart titles are assertions that admit declines | 4, 7 |
| 4 | Top-10 accounts table: aligned, minimal borders, flags | 4 |
| 5 | Risks have owner + mitigation date in table form | 2 |
| 6 | Appendix with metric definitions, hidden in present mode | 1, 4 |
| 7 | Footer with page numbers on every slide | 1 |
| 8 | Every number reconciled to a named source | 8 |
| 9 | Deck answers the exec questions in the first 2 slides | 2 |
| 10 | PDF leave-behind (with appendix) and pptx (appendix hidden) | 8 |

---

## Project 4: Conference Talk Deck

**Modules applied:** 2, 3, 7 (assertion-evidence, delivery), 8

### Scenario

Dr. Amara Bello, a fictional researcher at Northgate Institute, is giving a 25-minute keynote at a supply-chain technology conference: "Why Route Optimizers Fail in the Rain." Audience: 200 practitioners and researchers. She has a live demo of her weather-aware routing prototype but knows conference Wi-Fi fails at the worst moment. She wants assertion-evidence slides (no text-wall bullets), a story-driven flow with one recurring character (a fictional driver, "Route 71"), and backup slides that let her pivot to recorded evidence if the demo dies. She also needs practice discipline so she lands at 25 minutes.

### Deliverables

1. `route71-keynote.pptx` (20-26 slides for 25 minutes; roughly 1-1.5 min/slide)
2. Assertion-evidence slides throughout: claim headlines + visual evidence (Module 7)
3. A live-demo segment with 3 backup slides (screenshots/recording)
4. Speaker notes with time checkpoints every 5 minutes
5. A rehearsal log: 3 timed run-throughs with notes on where she overran

### Step-by-Step Build Walkthrough

1. **Find the story spine first.** Write the 6-beat arc in plain text before any slide work: hook (Route 71 stuck in a storm), problem (optimizers assume dry roads), insight (weather is a routing variable), method (her model), evidence (17% fewer late deliveries in pilot), close (call to action). Module 7.
2. **Convert beats to assertion titles.** Each title is a full-sentence claim ("Dry-road assumptions cost 17% on-time performance"). If a slide cannot make a claim, it does not belong (Module 7 assertion-evidence).
3. **One visual per slide carries the evidence.** Charts (Module 4) for the numbers, full-bleed photos (Insert > Pictures, Picture Format > Crop) for the story beats, big pull-quotes for the human moments. Maximum 6 words of body text besides the title on story slides.
4. **Design a signature slide style** so the deck looks like "hers": one recurring motif (a rain-blue accent #2B6CB0 over dark charcoal for keynotes; dark slides read well on conference projectors). Check contrast: light text on dark backgrounds needs 18pt+ (Module 3).
5. **Build the demo segment with failure in mind.** Demo slides: (a) demo title slide with a "what you are seeing" caption, (b) 3 backup slides: 2 screenshots with annotation callouts (Insert > Shapes > callout, Module 4) and 1 embedded recording (Insert > Video > This Video, with poster frame, Module 6). Backup slides sit after the main deck, hidden.
6. **Add time checkpoints in notes.** Every 5th slide, notes start with "[15:00 checkpoint]" (Module 7). If she is behind at a checkpoint, the notes name which slide to skip.
7. **Mark skip slides.** Two nice-to-have slides get "SKIP-OK" in the notes so she can cut live without panic (Module 7 Q&A and pacing).
8. **Rehearse three times with Rehearse Timings** (Slide Show > Rehearse Timings, Module 8) plus Presenter Coach-style self-review (record the screen: Insert > Screen Recording, Module 6). Log actual minutes per section in a notes table; adjust slide count, not speaking speed.
9. **Prepare the room kit:** PDF backup on a USB drive, the deck on laptop + cloud copy, video files embedded not linked (Module 6 embedding), presenter view tested (Slide Show > Use Presenter View, Module 7).
10. **Final checks:** spell-check (Module 8), fonts embedded (File > Options > Save > Embed fonts, Module 3) because conference laptops are strangers.

Match: `sample-01-starter-deck.pptx` as a template base you restyle; compare structure with `sample-02-pitch-deck.pptx` for assertion-title craft.

### Design Decisions Explained

- **Assertion-evidence beats bullets for keynotes.** A claim in the title makes the slide's point even for someone who arrives late; the visual below is the proof (Module 7). Bullets invite reading, and a read-aloud keynote dies.
- **One recurring character (Route 71) anchors abstraction.** Story continuity gives the audience a place to hang every technical point (Module 7 narrative). The storm frame returns in the close for symmetry.
- **Dark theme for the keynote context.** Projectors wash out light slides in dark rooms; charcoal backgrounds with light text hold contrast. This is audience-environment-driven design (Module 3), not taste.
- **Backup slides are hidden, not absent.** Hiding (Slide Show > Hide Slide) keeps flow clean while preserving the escape hatch (Module 1, 6). A demo failure becomes invisible to the audience.
- **Time checkpoints over speed-training.** Professionals do not talk faster; they cut content (Module 8). Named skip slides make cutting a pre-made decision.

### Starter Outline (22 Slides)

| # | Assertion title | Evidence visual |
|---|---|---|
| 1 | Why Route Optimizers Fail in the Rain | Title + storm photo |
| 2 | Route 71 was 40 minutes late on a 9-mile run | Map-like graphic + big number |
| 3 | Optimizers assume dry roads | Diagram of naive model (Module 4) |
| 4 | Rain changes three routing variables | 3-icon row |
| 5 | We modeled weather as a routing input | Simple model diagram |
| 6 | Method: 12 weeks, 2 fleets, weather-matched pairs | Timeline SmartArt |
| 7 | Weather-aware routing cut late deliveries 17% | Bar chart, zero-based |
| 8 | The gain concentrated in heavy rain | Line chart by condition |
| 9 | Cost per route rose only 1.2% | Column chart |
| 10 | LIVE DEMO: the prototype re-routes Route 71 | Demo title + caption |
| 11 | What breaks first is ETA trust, not distance | Pull quote |
| 12 | Three adoption blockers we did not expect | Numbered trio |
| 13 | Start with ETA accuracy, not optimization | Assertion + diagram |
| 14 | Route 71 made its window today | Storm photo returns (symmetry) |
| 15 | Call to action: publish your weather incident logs | One line + link as text |
| 16 | Summary: three claims to take home | 3 assertions |
| 17 | Q&A | Minimal slide |
| 18-20 | (Hidden) Demo backup: screenshot 1, screenshot 2, recording | Annotated |
| 21-22 | (Hidden) Deep-dive: model details, full results table | Dense appendix |

### Three Ways to Extend

1. **Cut a 5-minute "lightning" version** from the same deck (Module 8 editing discipline) as a second deliverable.
2. **Add an animated transition between the storm frames** using Morph on duplicated photos (preview of Project 5).
3. **Create a handout one-pager** of the three claims + method diagram for the conference bag (Module 6 handouts).

### Self-Grading Rubric

| # | Criterion | Module |
|---|---|---|
| 1 | Every title is a full-sentence claim | 7 |
| 2 | Slides are visual evidence with 6 or fewer body words | 3, 7 |
| 3 | Coherent story spine with recurring character/scene | 7 |
| 4 | 3 hidden demo-backup slides (2 annotated, 1 recording) | 6 |
| 5 | Videos embedded, not linked | 6 |
| 6 | Time checkpoints in notes every ~5 minutes | 7 |
| 7 | 2 slides marked skip-able for live cuts | 7, 8 |
| 8 | 3 timed rehearsals logged with adjustments | 8 |
| 9 | Fonts embedded; PDF backup exported | 3, 8 |
| 10 | 20-26 slides fit 25 minutes at 1-1.5 min each | 7 |

---

## Project 5: Animated Product Demo

**Modules applied:** 3, 5 (animation, Morph, triggers), 6 (video, kiosk mode), 8

### Scenario

VeloCabin (fictional) is launching an in-car smart display for ride-share drivers. Marketing lead Tomás Vidal needs a self-running product demo for a trade-show booth and a live-triggered version for the sales team. Requirements: smooth Morph sequences showing the device UI changing states (navigation to earnings to safety mode), trigger reveals for "ask us about X" side notes during live pitches, an embedded video placeholder for a 30-second product reel (to be shot later), and a kiosk loop that runs unattended at the booth with a 90-second total cycle. The sales version must never autoplay into the middle of a live conversation.

### Deliverables

1. `velocabin-demo.pptx` with two shows inside one file: sales (manual) and kiosk (auto), separated into sections
2. At least 3 Morph transitions between duplicated-state slides (Module 5)
3. At least 3 trigger-based reveals for live-pitch asides (Module 5)
4. One embedded video slide with poster frame and custom playback (Module 6), placeholder-safe
5. Kiosk version: auto-advance timings, looping (Module 6 setup show)
6. Animation documentation slide (in the deck's hidden section) so future editors know what is wired to what

### Step-by-Step Build Walkthrough

1. **Storyboard states before animating.** The device UI has 4 states: idle map, active route, earnings summary, safety mode. Draw each as its own slide using rounded rectangles, text, and a device frame (Insert > Shapes, Module 4). Animation planning is storyboarding first (Module 5).
2. **Build Morph pairs by duplication.** Create state A slide, right-click slide thumbnail > Duplicate Slide, then move/resize/replace elements on the copy to state B. Select state B slide, Transitions > Morph (Module 5). PowerPoint matches objects by identity, so always duplicate, never rebuild. Three pairs: idle to route, route to earnings, earnings to safety.
3. **Name your shapes for sanity.** Home > Select > Selection Pane: rename key objects ("device-screen", "route-line") (Module 5/8). Morph matching and trigger wiring both get easier to debug.
4. **Wire trigger reveals.** On the sales-demo slides, create an aside card (e.g., "Ask us about driver fatigue alerts"). Animations > Appear > Trigger > On Click of > a hotspot button shape (Module 5). The aside reveals only when the salesperson clicks the hotspot - live control, not timeline drift.
5. **Keep timeline animations minimal and ordered.** Where motion is not Morph, use simple Appear/Fade with "On Click" or short "After Previous" (Module 5 animation pane discipline). Avoid Fly In from every direction; motion should explain state change, not decorate.
6. **Embed the video placeholder.** Insert > Video > This Device, pick any 30-second clip for now (or a black placeholder clip). Playback > Start: Automatically or On Click depending on show type; set a poster frame (Playback > Poster Frame > Image From File) so the slide shows a clean still before play (Module 6). Keep the file embedded (Playback options default to embedded in modern PowerPoint).
7. **Build the kiosk section.** Duplicate the sales section, delete trigger-only asides (or set them to auto), then: Transitions > Advance Slide "After 00:05" per slide with durations tuned to a 90-second loop (Module 5 timings). Set video slides to auto-start.
8. **Enable loop mode.** Slide Show > Set Up Slide Show > "Browsed at a kiosk (full screen)" which auto-loops and disables casual click-advancing (Module 6 setup). Esc still exits for staff.
9. **Test both shows end to end.** F5 the sales version clicking every trigger; then run the kiosk version twice through the loop (Module 8 verification). Timing bugs hide at the loop seam - check the wrap from last slide back to first.
10. **Write the hidden animation doc slide:** table of slide, object, effect, trigger, purpose (Module 5 documentation habit). Future editors will thank you.

Match: `sample-05-animated-demo.pptx` for a working Morph pair and trigger aside you can open in the Animation Pane to study.

### Design Decisions Explained

- **Morph over keyframe animation because state changes are the story.** The audience should feel the UI transforming, not watch elements fly in (Module 5: transition supports meaning). Morph duplicates preserve object identity, which also makes edits propagate.
- **Triggers instead of timed sequences for live pitches.** A salesperson's timing is unpredictable; click-to-reveal asides never run ahead of the conversation (Module 5 trigger logic).
- **Two shows in one file, not two files.** Sales and booth versions share assets and brand; separating them by section keeps them in sync when the UI mockups change (Module 1 sections, Module 8 maintenance).
- **Poster frame on the video placeholder.** A raw first-frame or black rectangle looks unfinished at a trade show; a designed poster frame keeps the slide premium until playback (Module 6).
- **Kiosk mode both loops and locks.** Unattended booths attract curious fingers; kiosk mode prevents strangers from exiting into the editor (Module 6 security of show).
- **Documented triggers.** Trigger wiring is invisible in Normal view; a hidden doc slide is the difference between an editable deck and a mysterious one (Module 5, 8).

### Starter Outline (16-18 Slides)

| # | Slide | Technique |
|---|---|---|
| 1 | VeloCabin: the display that works while you drive | Title, fade in |
| 2 | The problem: drivers juggle three apps | 3-panel static |
| 3 | One display, three modes | Overview of states |
| 4 | State A: idle map | Base slide |
| 5 | State B: active route (Morph from 4) | Morph pair 1 |
| 6 | [Trigger aside] "Ask: reroute on incident" | Trigger reveal |
| 7 | State C: earnings summary (Morph from 5) | Morph pair 2 |
| 8 | [Trigger aside] "Ask: instant payout" | Trigger reveal |
| 9 | State D: safety mode (Morph from 7) | Morph pair 3 |
| 10 | [Trigger aside] "Ask: fatigue alerts" | Trigger reveal |
| 11 | Product reel (placeholder video) | Embedded video |
| 12 | Spec highlights | Table (Module 4) |
| 13 | Talk to us | Booth CTA |
| 14-16 | (Kiosk section) condensed 3-slide auto loop + reel | Timed advance |
| 17-18 | (Hidden) animation documentation; video replacement instructions | Doc slides |

### Three Ways to Extend

1. **Add a trigger-based "spec deep-dive" jump panel** so the salesperson can dive and return (Module 5 triggers + return-to-show links).
2. **Build an animated GIF teaser** of the Morph sequence for social (Module 6 export) or a narrated export of the kiosk loop.
3. **Add sound effects sparingly** on state changes (Module 6 audio), off by default for the sales version.

### Self-Grading Rubric

| # | Criterion | Module |
|---|---|---|
| 1 | 3+ Morph pairs created via duplication (objects matched) | 5 |
| 2 | 3+ trigger reveals wired to named hotspot shapes | 5 |
| 3 | Motion explains state change; no decorative fly-ins | 5 |
| 4 | Video embedded with designed poster frame | 6 |
| 5 | Kiosk version auto-advances to a 90-second loop | 5, 6 |
| 6 | Kiosk mode set (browsed at a kiosk), loops cleanly at seam | 6 |
| 7 | Sales and kiosk sections separated in one file | 1 |
| 8 | Selection Pane names used for animated objects | 5, 8 |
| 9 | Hidden animation documentation slide included | 5 |
| 10 | Both shows tested end to end (triggers clicked, loop twice) | 8 |

---

## Project 6: Branded Template System

**Modules applied:** 3 (theme/color), 5 (Slide Master and layouts), 8 (QA and handoff)

### Scenario

Harborline Credit Union (fictional) is tired of 14 departments producing 14 looks. Brand manager Ife Adeyemi commissions a PowerPoint template system: a master with the Harborline palette, 4 custom layouts, a .potx output anyone in the org can use, a one-page brand guidelines mini-doc for slide makers, and a usability test where a colleague who has never seen the template builds a 5-slide deck with it unaided. Brand basics (fictional): navy #14304F, sea-green accent #1F8A70, warm gray #F0EEE9 background, headings in Avenir Next (fallback Segoe UI), body Segoe UI, logo bottom-right at 20mm wide.

### Deliverables

1. `harborline-template.potx` (and the working .pptx source)
2. Slide Master work: theme colors, theme fonts, logo placement, background
3. 4 custom layouts: (a) Title, (b) Section Divider, (c) Title + Content (two-thirds body), (d) Data Layout (title + chart placeholder + footnote line)
4. One-page brand guidelines mini-doc (inside the template as slide 1 notes or as a separate 2-slide "how to use" file)
5. Usability test log from a second person (the test, their 5-slide deck, and the friction notes)
6. QA checklist completed (Module 8)

### Step-by-Step Build Walkthrough

1. **Start from the theme, not the master.** Design > Variants > Colors > Customize Colors: create "Harborline" with navy as Text/Background 1 pairing, sea-green as Accent 1, warm gray as Background 2 (Module 3). Design > Fonts > Customize Fonts: headings Avenir Next, body Segoe UI (Module 3). Naming the theme colors means every color picker shows brand names, not "Accent 1".
2. **Open the master.** View > Slide Master (Module 5). On the top (parent) master, place the logo bottom-right (Insert > Pictures, then Picture Format to size), set the warm gray background via Background Styles > Format Background, and confirm the placeholders use theme fonts. Changes here flow to all layouts - the core Master insight (Module 5).
3. **Build layout (a) Title.** Right-click a layout > Rename Layout "H-Title". Keep: title placeholder upper-left, subtitle below, logo region clear. Set title font size 40pt, color navy (select placeholder text, Home > Font Color > Theme: Navy) (Module 5).
4. **Build layout (b) Section Divider.** Insert Layout > Insert Placeholder > Text for a big section number + title. Reuse the Project 2 divider lesson: number + title + one-line promise. Force 60pt title size in the placeholder formatting so users cannot shrink it to 18pt (Module 5 placeholder locking of style).
5. **Build layout (c) Title + Content.** One content placeholder occupying the left two-thirds (Insert Placeholder > Content), reserving the right third whitespace for future-proofing. Two-thirds discipline creates consistent margins across decks (Module 3).
6. **Build layout (d) Data Layout.** Title placeholder + a chart placeholder (Insert Placeholder > Chart) at fixed size + a small text placeholder at the bottom for the "Source:" footnote. Baking the footnote line into the layout is how honest charting becomes the default (Module 4, 5).
7. **Add "how to use" slides at the top of the source file** (kept, not deleted): which layout to pick for which content, the do-not list (no rainbow colors, no clip art, do not resize the logo).
8. **Save as template.** File > Save As > PowerPoint Template (.potx). Save to the default custom templates folder so File > New > Personal shows it (Module 5, 8).
9. **Write the brand guidelines mini-doc.** 1-2 pages max (can be the deck's Notes Pages export): palette with hex codes and usage rules, font hierarchy (H1 40pt / H2 28pt / body 18pt), logo clear space and min size, chart color mapping (navy actuals, sea-green forecast), photo style. Export as PDF.
10. **Run the usability test.** Give a colleague only the .potx + the mini-doc: "Build a 5-slide deck introducing Harborline's student loan product. 20 minutes. Ask no questions." Log every friction point (could not find layout X, logo moved by accident, etc.). Fix the top 3 frictions in the template and re-test. The template is not done until a stranger succeeds with it (Module 8 verification).

Match: `sample-06-brand-template.pptx` as a worked example of master + 4 layouts; compare with `exercise-fix-this-deck.pptx` to see what templates prevent.

### Design Decisions Explained

- **Theme colors and fonts first, master second.** Theme-level decisions survive layout edits and appear by name in every picker. Master placement (logo, background) then enforces them structurally (Module 3, 5 layering).
- **4 layouts, not 12.** Every extra layout is a decision the user must make. Four covers ~95% of real slides: title, divider, content, data (Module 5 constraint thinking).
- **Locking styles in placeholders.** If users can shrink the divider title to 18pt, they will. Setting the size in the layout removes the failure mode without policing anyone (Module 5).
- **Data Layout bakes in the source footnote.** Honesty-by-default: the chart that ships gets a provenance line because the layout demands one (Module 4 + 5).
- **Two-thirds body width leaves intentional whitespace** and keeps text measure readable (Module 3). It also reserves a natural column for side images without redesign.
- **Usability testing with a naive colleague is the deliverable, not a courtesy.** Templates fail at the moment of first use by someone else; friction notes are the QA data (Module 8).

### Starter Outline (Source File Contents)

| Part | Contents |
|---|---|
| Slide 1-2 | How to use this template (keep in source, delete in use) |
| Slide 3 | H-Title layout example filled with sample title |
| Slide 4 | H-Divider layout example ("Section 2: Member Growth") |
| Slide 5 | H-Content layout example (2 bullets + one image placeholder note) |
| Slide 6 | H-Data layout example (dummy chart + "Source: Harborline analytics, 2031-Q2") |
| Slide 7 | Palette + type specimen (mini style tile) |
| Notes | Brand mini-doc text in Notes Pages of slides 3-7 for PDF export |

### Three Ways to Extend

1. **Add a dark variant theme** (navy background, warm gray text) with its own layout set for webinars (Module 3 contrast rules).
2. **Create 2 more layouts for common Harborline cases** (quote/testimonial, two-image comparison) after the usability test reveals demand (Module 5).
3. **Package a starter deck + template + mini-doc PDF as the onboarding kit**, distributed as a zip, with a 10-minute recorded walkthrough (Module 6 recording).

### Self-Grading Rubric

| # | Criterion | Module |
|---|---|---|
| 1 | Theme colors named "Harborline...", fonts themed (not manual) | 3 |
| 2 | Parent master: logo, background, font inheritance correct | 5 |
| 3 | Exactly 4 custom layouts, renamed clearly | 5 |
| 4 | Placeholder styles locked (title sizes enforced) | 5 |
| 5 | Data Layout includes source-footnote placeholder | 4, 5 |
| 6 | .potx saved and visible under File > New > Personal | 5, 8 |
| 7 | Brand mini-doc: palette hex, type hierarchy, logo rules, chart mapping | 3 |
| 8 | Usability test performed by a second, naive person | 8 |
| 9 | Top 3 frictions fixed and re-tested | 8 |
| 10 | QA checklist passed (theme intact in a fresh deck from .potx) | 8 |

---

## Capstone: Build for a Real Need

The six projects above are simulations. The capstone is real: find an actual person or group with an actual deck problem and solve it. Good candidates: a community group's fundraiser deck, a small business's sales one-pager in slide form, a class lecture you are asked to give, a volunteer org's annual report summary, or a talk proposal for a local meetup. The constraint that matters: the deck must be presented to real humans (3 or more) for a real purpose within 60 days.

**Deliverables:**

1. A one-paragraph needs brief you wrote after interviewing the stakeholder (who is the audience, what decision or action should the deck cause)
2. The deck itself (.pptx) applying Modules 2-7 as appropriate
3. A design rationale memo (1 page max): 3 design decisions and the why, each linked to a module principle
4. Evidence of delivery: the date presented, audience size, and 3 sentences of feedback collected (Module 7)
5. A v1-to-final archive showing at least 2 iterations (Module 8)

**Rules of the road.** Ask the stakeholder for brand assets (colors, logo) and use them (Project 6 skills); if none exist, choose a disciplined palette (Module 3). Replace all personal data in practice copies before adding anything to a portfolio. If the deck contains org-confidential numbers, produce a redacted portfolio version.

**Capstone rubric (10 criteria, 1-5):**

| # | Criterion | Module |
|---|---|---|
| 1 | Needs brief names audience and intended action/decision | 2 |
| 2 | Structure matches purpose (pitch, teach, review, or talk) | 2 |
| 3 | Visual system consistent (theme colors, alignment, type scale) | 3 |
| 4 | Any charts/tables honest, sourced, and appropriately typed | 4 |
| 5 | Multimedia or interactivity used only where it helps | 5, 6 |
| 6 | Speaker notes/Presenter-ready for the actual speaker | 7 |
| 7 | Rehearsed with timing to fit the real slot | 7, 8 |
| 8 | Actually presented to 3+ real people within 60 days | 7 |
| 9 | Feedback collected and one post-feedback revision made | 8 |
| 10 | Portfolio version prepared (PDF + redacted, before/after noted) | 8 |

Scoring guide: 40+ = portfolio-grade, submit it; 30-39 = solid, revise the lowest 3 scores; below 30 = pick the weakest criterion's module and redo that section of the workbook before re-attempting.

---

## Common Mistakes & Pitfalls

| Mistake | Why it hurts | Fix (module) |
|---|---|---|
| Building slides before writing the story spine | Produces pretty decks nobody remembers | Titles-only arc first (Module 2, 7) |
| Different fonts/colors per slide in project decks | Reads as amateur even when content is strong | Theme + master setup (Module 3, 5) |
| Truncated Y axes to exaggerate growth | Numerate audiences catch it and stop trusting you | Zero-based, sourced charts (Module 4) |
| Rainbow status colors on every table cell | Nothing looks important | One accent reserved for risk (Module 3) |
| Rebuilding (not duplicating) Morph states | Morph silently fails to match objects | Duplicate, then edit (Module 5) |
| Timed animations in live sales demos | Deck runs ahead of the conversation | Trigger reveals (Module 5) |
| Linked (not embedded) video | Breaks on any other computer | Embed + poster frame (Module 6) |
| Forgetting the kiosk loop seam test | Booth show freezes or flashes at wrap | Test two full loops (Module 6, 8) |
| Notes empty or written as bullet fragments | Substitutes and future-you cannot present | Spoken-language notes (Module 7) |
| Handouts printed as full slides | Wastes paper, no room for notes | 3-slides-per-page handout (Module 6) |
| No appendix for predictable questions | Tough questions derail the room | Hidden appendix slides (Module 1) |
| Template with 12 layouts nobody understands | Users pick wrong or avoid the template | 4 layouts max + usability test (Module 5, 8) |
| Two files for two show modes of one demo | They drift apart within a month | One file, two sections (Module 8) |
| Portfolio shipped as raw .pptx only | Reviewers cannot preview quickly | PDF + PNG exports + before/after (Module 8) |

## Key Takeaways

1. **Structure before pixels.** Every successful project here starts with audience + intended action, then a titles-only spine. Design serves the story (Modules 2, 7).
2. **Consistency is a system, not effort.** Theme colors, theme fonts, masters, and 4 layouts do the work that manual tidying cannot (Modules 3, 5).
3. **Honest visuals compound trust.** Zero-based axes, source footnotes, and titles that admit declines win long-term credibility (Module 4).
4. **Notes are the hidden deliverable.** Speakers, substitutes, and future editors live in the notes; write them in spoken language (Module 7).
5. **Design for failure modes.** Hidden backup slides for demos, kiosk locks for booths, trigger reveals for live pitch drift (Modules 5, 6).
6. **Test with strangers and against clocks.** Rehearsal timings, print tests, and a naive-user template test are what separate finished work from drafts (Module 8).
7. **A portfolio shows judgment.** Three finished decks plus one before/after fix of `exercise-fix-this-deck.pptx` with reasoning beats ten unannotated files.
8. **The capstone makes it real.** A deck presented to real humans, revised once on real feedback, is the proof of skill no exercise can give.


## FILE: 10-Sources-References/sources-references-index.md

# Sources & References Index

The full bibliography behind the PowerPoint Zero to Hero package: official documentation, tutorial sites, YouTube channels, books, courses, and communities. All external materials are referenced with attribution; no copyrighted content is reproduced in this package.

Legend: [Official] vendor documentation | [Tutorial] learning sites | [Video] YouTube channels | [Book] print/ebook | [Course] MOOC/platform | [Community] forums | [Templates] design resources

---

## 1. Official Documentation

| Source | What it covers | URL |
|--------|----------------|-----|
| [Official] Microsoft Support: PowerPoint hub | All PowerPoint help articles (searchable by feature) | https://support.microsoft.com/en-us/powerpoint |
| [Official] Microsoft Learn: training hub | Free guided modules and learning paths (search "PowerPoint") | https://learn.microsoft.com/en-us/training/ |
| [Official] Microsoft Create | Templates, design ideas, themes | https://create.microsoft.com/ |
| [Official] Microsoft 365 Roadmap | Upcoming PowerPoint features | https://www.microsoft.com/en-us/microsoft-365/roadmap |
| [Official] Microsoft Accessibility: PowerPoint | Accessibility guidance and checkers | https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25 |

Search tip: Microsoft article URLs change between releases. Navigate from the hubs above and search the exact feature name (e.g. "Morph transition", "slide master") to land on the current article.

## 2. Tutorial Sites

| Source | What it covers | URL |
|--------|----------------|-----|
| [Tutorial] Presentation Guru | Evidence-based presentation design articles | https://presentationguru.com/ |
| [Tutorial] Think Outside the Slide (Dave Paradi) | Chart choice, survey research, deck makeovers | https://www.thinkoutsidetheslide.com/ |
| [Tutorial] Duarte blog | Storytelling, visual design, slide craft | https://www.duarte.com/blog/ |
| [Tutorial] Slidesgo | Template galleries and design resources | https://slidesgo.com/ |
| [Tutorial] GoSkills PowerPoint course area | Structured MS PowerPoint lessons | https://goskills.com/microsoft-office |
| [Tutorial] Simon Sez IT | Step-by-step PowerPoint tutorials | https://www.simonsezit.com/ |
| [Tutorial] Ablebits / Spreadsheet-style Office tips | Task-focused how-tos | https://www.ablebits.com/ |
| [Tutorial] GCFLearnFree.org: PowerPoint basics | Free beginner lessons | https://edu.gcfglobal.org/en/powerpoint/ |

## 3. YouTube Channels

| Channel | Known for | URL |
|---------|-----------|-----|
| [Video] Leila Gharani | Design + productivity techniques | https://www.youtube.com/@LeilaGharani |
| [Video] Kevin Stratvert | Clear feature walkthroughs | https://www.youtube.com/@KevinStratvert |
| [Video] One Skill PowerPoint | Slide design art and tutorials (search on YouTube) | https://www.youtube.com/results?search_query=one+skill+powerpoint |
| [Video] Simon Sez IT | Full course-style walkthroughs | https://www.youtube.com/@SimonSezIT |
| [Video] Microsoft (official) | Official feature demos and webinars | https://www.youtube.com/@microsoft |
| [Video] PPT Guru | Design-focused PowerPoint tutorials | https://www.youtube.com/@PPTGuru |

Note: YouTube handles occasionally change. If a link 404s, search the channel name on YouTube.

## 4. Books

| Book | Author | Publisher / Year | ISBN | Best for |
|------|--------|------------------|------|----------|
| [Book] slide:ology | Nancy Duarte | O'Reilly, 2008 | 978-0-596-52236-0 | Visual slide design craft (Module 3) |
| [Book] Resonate | Nancy Duarte | Wiley, 2010 | 978-0-470-63201-7 | Story structure for presentations (Module 9 projects) |
| [Book] Presentation Zen | Garr Reynolds | New Riders, 2008 | 978-0-321-52565-9 | Simplicity and design thinking (Modules 2-3) |
| [Book] Beyond Bullet Points | Cliff Atkinson | Microsoft Press, 2011 (3rd ed.) | 978-0-7356-2387-3 | Assertion-evidence slide writing (Module 3) |
| [Book] The Non-Designer's Design Book | Robin Williams | Peachpit, 2014 (4th ed.) | 978-0-13-396615-2 | CRAP principles foundation (Module 3) |
| [Book] Storytelling with Data | Cole Nussbaumer Knaflic | Wiley, 2015 | 978-1-119-00225-3 | Chart communication (Module 4) |
| [Book] Speaking PowerPoint | Bruce Gabrielle | Insights Press, 2010 | 978-0-9842538-0-6 | Business deck structure (Module 9) |

ISBNs are provided for library/retail lookup; verify against your local catalog.

## 5. Courses & Certification

| Course / Cert | Provider | What it tests | URL |
|---------------|----------|---------------|-----|
| [Course] Coursera: presentation skills catalog | Various providers | Design and delivery courses (search "presentation skills") | https://www.coursera.org/search?query=presentation%20skills |
| [Course] Microsoft 365 Certified: Fundamentals learning path | Microsoft Learn | Broad MS 365 literacy | https://learn.microsoft.com/en-us/training/ |
| [Course] Presentation Skills / public speaking courses | edX, Coursera | Delivery (pairs with Module 7) | https://www.edx.org/ |
| [Official] MOS: Microsoft Office Specialist (PowerPoint) | Microsoft / Certiport | Certification exam outline | https://www.microsoft.com/en-us/learning/mos-certification.aspx |
| [Official] Certiport (MOS exam delivery) | Certiport | Register and find test centers for MOS exams | https://www.certiport.com/ |
| [Course] LinkedIn Learning | LinkedIn | PowerPoint tracks with certificates of completion | https://www.linkedin.com/learning/ |
| [Course] GCFLearnFree.org: PowerPoint | GCFGlobal | Free beginner track | https://edu.gcfglobal.org/en/powerpoint/ |

## 6. Communities

| Community | Good for | URL |
|-----------|----------|-----|
| [Community] r/powerpoint | Quick how-did-they-do-that answers | https://www.reddit.com/r/powerpoint/ |
| [Community] Microsoft Tech Community: PowerPoint | Feature questions, Microsoft staff replies | https://techcommunity.microsoft.com/ |
| [Community] Super User (PowerPoint tag) | Technical troubleshooting | https://superuser.com/questions/tagged/microsoft-powerpoint |
| [Community] Stack Overflow (powerpoint-vba tag) | VBA automation questions (Module 8) | https://stackoverflow.com/questions/tagged/powerpoint-vba |

## 7. Templates & Design Resources

| Resource | License / Terms | What to find | URL |
|----------|-----------------|--------------|-----|
| [Templates] Microsoft Create templates | Microsoft Services terms | Starter decks and themes | https://create.microsoft.com/ |
| [Templates] Slidesgo | Freemium (attribution for free tier) | Styled template structures | https://slidesgo.com/ |
| [Templates] Google Slides template galleries (for structural inspiration) | Google terms | Layout ideas transferable to PowerPoint | https://workspace.google.com/products/slides/ |
| [Templates] unDraw (illustrations) | Open license (MIT-style, free) | Flat illustrations instead of clip art | https://undraw.co/ |

## 8. Sample Data & Practice Content Inspiration

| Source | Maps to modules | Note |
|--------|-----------------|------|
| YourCompany Inc / TaskFlow Pro fictional datasets (in-repo) | Modules 4, 9; all sample decks | Original content created for this package; intentionally fake |
| Chart chooser frameworks (thinkoutsidetheslide.com surveys) | Module 4 | Design patterns inspired by public survey research, paraphrased |

---

## Attribution & Honesty Notes

- All trademarks (PowerPoint, Excel, Microsoft 365, Anki) belong to their owners; this package is not affiliated with or endorsed by any vendor.
- Books are cited, never reproduced. Quizzes, cheat sheets, flashcards, sample decks, and modules in this package are original content.
- Sample decks use only fictional brands, people, and numbers (YourCompany Inc, TaskFlow Pro, Jordan Ade).
- AI assistance disclosure: research compilation, drafts, datasets, quizzes, cheat sheets, and deck generation were produced with Hermes Agent (Nous Research) under human direction, review, and quality control by the repository owner. See CONTRIBUTORS.md.


## FILE: 11-Study-Plan/00-zero-to-hero-study-plans.md

# Zero to Hero Study Plans: 12 / 8 / 6 / 4 / 2 Weeks

**Choose the track that fits your schedule.** The content never changes, only the pace. Every track covers all 8 modules, the 6 real-world projects, and all quizzes. Faster tracks demand more hours per week and skip repetition, not material.

| Track | Weeks | Hours per week | Best for |
|------|-------|----------------|----------|
| [12-Week Mastery Track](#track-a-12-week-mastery) | 12 | 6-8 h | Beginners who want deep, lasting skill |
| [8-Week Standard Track](#track-b-8-week-standard) | 8 | 8-10 h | Most learners with a day job |
| [6-Week Accelerated Track](#track-c-6-week-accelerated) | 6 | 10-12 h | Learners with some Office experience |
| [4-Week Sprint Track](#track-d-4-week-sprint) | 4 | 12-15 h | Fast upskilling for a job or project |
| [2-Week Crash Track](#track-e-2-week-crash) | 2 | 18-25 h | Emergency prep (interview, certification, deadline) |

## How to Use Any Track

1. Pick a track below and copy its schedule into your own calendar.
2. Every study session follows the same rhythm:

| Step | Time | Activity |
|------|------|----------|
| 1 | 10 min | Review flashcards (Anki) from previous sessions |
| 2 | 40-60 min | Read the module section, follow along in PowerPoint |
| 3 | 30-45 min | Do the "Try it now" exercises and practice projects |
| 4 | 20 min | Take the module quiz, score it, note weak areas |
| 5 | 10 min | Log progress in the [Progress Tracker](progress-tracker.md) |

3. **Score rule (same in every track):** quiz 90%+ advance, 70-89% review weak areas then advance, below 70% restudy the module before moving on.
4. Use the sample decks in `sample-decks/` as reference companions. Open the matching deck while studying each topic and reverse-engineer how it was built.
5. Stuck or want variety? Swap in the AI-assisted prompts from `HOW-TO-USE-WITH-AI.md`.

---

## Track A: 12-Week Mastery

**Total: 72-96 hours. 5 study days per week (4 study + 1 review/project).**

| Week | Focus | Study Days (Mon-Thu) | Friday: Review & Build |
|------|-------|----------------------|------------------------|
| 1 | Module 1: Fundamentals | Interface, views, slides, text, outline, sections, formats | Quiz 1 + rebuild `sample-01-starter-deck.pptx` from scratch |
| 2 | Module 2: Design Foundations | Themes, masters, layouts, backgrounds, .potx templates | Quiz 2 + build a personal template (Project warm-up) |
| 3 | Module 3: Visual Design | Principles, typography, color, shapes, icons, images, SmartArt | Quiz 3 + redo a bad slide from `exercise-fix-this-deck.pptx` |
| 4 | Module 4: Tables, Charts & DataViz | Tables, chart types, chart chooser, Excel linking | Quiz 4 + recreate `sample-03-data-report-deck.pptx` charts |
| 5 | Module 5: Transitions & Animations | Transitions, Morph, animation pane, triggers, restraint | Quiz 5 + build one Morph sequence (like `sample-04`) |
| 6 | Module 6: Media & Interactivity | Video, audio, screen recording, links, Zoom, kiosk mode | Quiz 6 + add interactivity to last week's deck |
| 7 | Module 7: Delivery & Workflow | Notes, Presenter View, rehearsal, accessibility, export | Quiz 7 + rehearse a 5-minute talk with your deck |
| 8 | Module 8: VBA Automation | Developer tab, VBA basics, batch slide generation | Quiz 8 + automate one boring task you did manually |
| 9 | Projects 1-2 | Startup pitch deck + Training/workshop deck | Peer review your own decks with the pitfalls tables |
| 10 | Projects 3-4 | Quarterly business review + Conference talk deck | Full `exercise-fix-this-deck.pptx` challenge (find 20 issues) |
| 11 | Projects 5-6 | Animated product demo + Branded template system | Portfolio polish: consistent branding across all decks |
| 12 | Capstone & Assessment | Review weak areas from quiz scores; rewatch hard topics | Final: build a deck for a real need in your life, present it to a real human |

**12-week extras:** read one 'Further Learning' article per week beyond the modules. By week 12 you should have 8+ portfolio decks.

---

## Track B: 8-Week Standard

**Total: 64-80 hours. 5 study days per week. Modules pair up.**

| Week | Focus | Study Days (Mon-Thu) | Friday: Review & Build |
|------|-------|----------------------|------------------------|
| 1 | Modules 1-2 (Fundamentals + Design Foundations) | Mon-Tue: Module 1 core sections. Wed-Thu: Module 2 core sections | Quizzes 1-2 + build a personal template |
| 2 | Module 3 (Visual Design) | Principles, typography, color, shapes, images, SmartArt | Quiz 3 + redesign 3 bad slides from `exercise-fix-this-deck.pptx` |
| 3 | Module 4 (Tables, Charts & DataViz) | Tables, all chart types, chart chooser, Excel linking | Quiz 4 + rebuild `sample-03-data-report-deck.pptx` |
| 4 | Modules 5-6 (Animations + Media) | Mon-Tue: transitions, Morph, animations. Wed-Thu: media, links, Zoom | Quizzes 5-6 + replicate `sample-04-animated-product-demo.pptx` |
| 5 | Module 7 (Delivery & Workflow) | Presenter View, rehearsal, accessibility, export, handouts | Quiz 7 + rehearse a 5-minute talk |
| 6 | Module 8 (VBA Automation) | VBA basics, batch generation, add-ins | Quiz 8 + automate one repetitive task |
| 7 | Projects 1-4 | Pitch deck, training deck, QBR, conference talk (1 per day) | Fix-me deck challenge (find 20 issues) |
| 8 | Projects 5-6 + Capstone | Product demo, template system, then final real-need deck | Present the final deck to a real human |

**8-week rule:** skip nothing, but do only 2 practice projects per module instead of all 5.

---

## Track C: 6-Week Accelerated

**Total: 60-72 hours. 6 study days per week. For people who already know Word/Excel well.**

| Week | Focus | Daily Split |
|------|-------|-------------|
| 1 | Modules 1-2 | 3 days per module. Quiz each Friday-Saturday |
| 2 | Modules 3-4 | 3 days per module. Build `sample-03` charts as practice |
| 3 | Modules 5-6 | 3 days per module. Replicate `sample-04` animations |
| 4 | Modules 7-8 | 3 days per module. Automate one task with VBA |
| 5 | Projects 1-3 | Pitch deck (2 days), training deck (2 days), QBR (2 days) |
| 6 | Projects 4-6 + Capstone | 1 day each project, 3 days on final real-need deck + presentation |

**6-week rule:** read every module fully, but do the 3 most relevant practice projects per module. Sunday off.

---

## Track D: 4-Week Sprint

**Total: 48-60 hours. 6-7 study days per week. Intense but complete.**

| Week | Focus | Daily Split |
|------|-------|-------------|
| 1 | Modules 1-2-3 (2 days each) | Fundamentals, design foundations, visual design. Quizzes on day 6 |
| 2 | Modules 4-5-6 (2 days each) | Charts, animations, media. Replicate `sample-03` and `sample-04` |
| 3 | Modules 7-8 (3 days each) | Delivery workflow, VBA. Quizzes 7-8 on day 6-7 |
| 4 | Projects 1-6 (1 day each) | 6 mini-projects at speed, day 7: capstone deck + present it |

**4-week rule:** do 2 practice projects per module, review flashcards daily (20 cards/day), and treat every quiz as a gate.

---

## Track E: 2-Week Crash

**Total: 36-50 hours. 7 days a week, 2-4 sessions per day. For deadlines: interviews, certification exams, a big presentation.**

| Days | Focus | Sessions per day |
|------|-------|------------------|
| Day 1 | Module 1 + Module 2 (core sections only) | 3 sessions |
| Day 2 | Module 3 (typography, color, images, SmartArt) | 3 sessions |
| Day 3 | Module 4 (charts + table essentials) | 3 sessions |
| Day 4 | Module 5 (Morph + animation basics) + Module 6 (video, links, Zoom) | 3 sessions |
| Day 5 | Module 7 (Presenter View, rehearsal, export) + Quiz 7 | 3 sessions |
| Day 6 | Module 8 (record macros + simple VBA) + Quiz 8 | 3 sessions |
| Day 7 | Quizzes 1-6 retakes, fix weak areas | 3 sessions |
| Day 8 | Project 1 (pitch deck) + Project 2 (training deck) | 3 sessions |
| Day 9 | Project 3 (QBR) + Project 4 (conference talk) | 3 sessions |
| Day 10 | Project 5 (animated demo) + Project 6 (template system) | 3 sessions |
| Day 11 | `exercise-fix-this-deck.pptx` full challenge (find 20 issues) | 2 sessions |
| Day 12 | Capstone: build your real-need deck | 2 sessions |
| Day 13 | Rehearse capstone 3 times with Presenter View + record it | 2 sessions |
| Day 14 | Buffer: retake lowest quiz, polish portfolio, present capstone | 2 sessions |

**2-week rule:** read only the sections listed in each day's goal, skip 'Further Learning' reading, do 1 practice project per module, and use the AI tutor prompts to compress review time.

---

## After Any Track: Keep Growing

- Revisit `09-Real-World-Projects` and rebuild projects in a different style (minimalist vs illustrated)
- Turn real work needs into decks every week (practice is the real teacher)
- Read one 'Further Learning' source per week from any module
- Retake quizzes after 30 days to test retention
- Explore add-ins and VBA further once the fundamentals are automatic

## Files You Need

| File | Purpose |
|------|---------|
| [progress-tracker.md](progress-tracker.md) | Checkbox checklist for every skill |
| `../quizzes/quiz-01-*.md` to `quiz-08-*.md` | Module quizzes with answer keys |
| `../anki/powerpoint-flashcards.csv` | Daily spaced repetition |
| `../sample-decks/` | 7 decks to study and reverse-engineer |
| `../HOW-TO-USE-WITH-AI.md` | AI tutor prompts to speed up any track |


## FILE: 11-Study-Plan/progress-tracker.md

# Progress Tracker

Check off each skill as you master it. Pair this with any study plan in [00-zero-to-hero-study-plans.md](00-zero-to-hero-study-plans.md).

**Mastery rule:** you can check a skill only when you did it yourself in PowerPoint at least once without looking at the instructions.

## Module 1: Fundamentals

- [ ] Navigate all 5 views and explain when to use each
- [ ] Create a new presentation from a blank file and from a template
- [ ] Add, delete, duplicate, and reorder slides
- [ ] Choose the right slide layout and know placeholder vs text box
- [ ] Write and structure text in Outline view
- [ ] Apply bullet discipline (6x6 rule) to a wall of text
- [ ] Organize a 20+ slide deck with sections
- [ ] Set slide size (16:9 vs 4:3) and know when each applies
- [ ] Save as .pptx, .potx, .ppsx, and export to PDF
- [ ] Quiz 1 score: ___/70

## Module 2: Design Foundations

- [ ] Apply and switch themes and variants
- [ ] Explain the slide master > layout > slide hierarchy
- [ ] Edit the slide master: background, logo, footer, slide number
- [ ] Edit a slide layout and place placeholders correctly
- [ ] Build and save a .potx template from scratch
- [ ] Format backgrounds (solid, gradient, picture) tastefully
- [ ] Reset slides to fix drifted formatting
- [ ] Use Design Ideas and know its limits
- [ ] Quiz 2 score: ___/70

## Module 3: Visual Design

- [ ] Apply contrast, repetition, alignment, proximity to a slide
- [ ] Build an assertion-evidence slide instead of a topic slide
- [ ] Pair fonts and size text for back-of-room readability
- [ ] Build a 60-30-10 color palette with accessible contrast
- [ ] Merge shapes (union, fragment, subtract, combine, intersect)
- [ ] Insert and recolor icons and SVGs
- [ ] Crop and compress images without stretching them
- [ ] Convert bullets to SmartArt and pick the right layout
- [ ] Align a slide with gridlines and Align tools in under 60 seconds
- [ ] Quiz 3 score: ___/70

## Module 4: Tables, Charts & DataViz

- [ ] Format a table so it does not look like a spreadsheet dump
- [ ] Choose the correct chart type for comparison, trend, composition, relationship
- [ ] Create column, bar, line, pie, doughnut, scatter, and combo charts
- [ ] Edit chart data and know embedded vs linked Excel data
- [ ] Format a chart: labels, axes, legends, color per point
- [ ] Remove chart junk and defend the data-ink ratio
- [ ] Build a KPI callout and bullet-graph style visual from shapes
- [ ] Spot misleading charts (truncated axes, wrong pie use)
- [ ] Quiz 4 score: ___/70

## Module 5: Transitions & Animations

- [ ] Explain the difference between transition and animation
- [ ] Build a Morph sequence using the duplicate-slide technique
- [ ] Add entrance, emphasis, and exit animations correctly
- [ ] Set start (on click / with previous / after previous), delay, duration
- [ ] Animate text by paragraph and charts by category
- [ ] Create a trigger animation on a clickable shape
- [ ] Reuse animations with Animation Painter
- [ ] Apply the 3-second restraint rule and remove tacky effects
- [ ] Quiz 5 score: ___/70

## Module 6: Media & Interactivity

- [ ] Insert and trim video, set poster frame and autoplay
- [ ] Add audio across slides and record narration
- [ ] Use PowerPoint's screen recording
- [ ] Add internal and external hyperlinks cleanly
- [ ] Build action buttons for deck navigation
- [ ] Create Slide Zoom, Section Zoom, or Summary Zoom menus
- [ ] Build a Custom Show for a specific audience
- [ ] Set up kiosk mode for a self-running deck
- [ ] Export a deck to MP4 video
- [ ] Quiz 6 score: ___/70

## Module 7: Delivery & Workflow

- [ ] Write speaker notes that help you, not scripts that trap you
- [ ] Rehearse with Presenter View and Rehearse Timings
- [ ] Run the Accessibility Checker and fix the findings
- [ ] Add alt text to every meaningful image
- [ ] Co-author a deck and resolve comments
- [ ] Export to PDF and video with correct settings
- [ ] Print handouts (3 slides with notes lines)
- [ ] Compare and merge two versions of a deck
- [ ] Quiz 7 score: ___/70

## Module 8: VBA Automation

- [ ] Enable the Developer tab and macro security correctly
- [ ] Record a macro and explain its limits
- [ ] Read and modify simple VBA Sub procedures
- [ ] Use variables, loops (For Each), and If blocks in VBA
- [ ] Generate slides in bulk from a list of data
- [ ] Create or install a .ppam add-in
- [ ] Connect PowerPoint VBA to Excel data
- [ ] Quiz 8 score: ___/70

## Projects (Module 9)

- [ ] Project 1: Startup pitch deck (10-12 slides)
- [ ] Project 2: Training / workshop deck with speaker notes
- [ ] Project 3: Quarterly business review with charts
- [ ] Project 4: Conference talk deck (story-driven)
- [ ] Project 5: Animated product demo (Morph + triggers)
- [ ] Project 6: Branded template system (.potx)
- [ ] Capstone: deck for a real need, presented to a real human

## Sample Decks

- [ ] Studied `sample-01-starter-deck.pptx` and rebuilt it
- [ ] Reverse-engineered `sample-02-business-pitch-deck.pptx`
- [ ] Recreated the charts in `sample-03-data-report-deck.pptx`
- [ ] Replicated the animations in `sample-04-animated-product-demo.pptx`
- [ ] Practiced delivery with `sample-05-training-deck-notes.pptx`
- [ ] Modified `sample-06-brand-template.potx` with your own brand
- [ ] Found all 20 planted issues in `exercise-fix-this-deck.pptx`

## Final Scoreboard

| Quiz | Date | Score /70 | Retake /70 |
|------|------|-----------|------------|
| Quiz 1: Fundamentals | | | |
| Quiz 2: Design Foundations | | | |
| Quiz 3: Visual Design | | | |
| Quiz 4: Tables & Charts | | | |
| Quiz 5: Transitions & Animations | | | |
| Quiz 6: Media & Interactivity | | | |
| Quiz 7: Delivery & Workflow | | | |
| Quiz 8: VBA Automation | | | |

**Graduation criteria:** all boxes checked, all 8 quizzes at 63+/70 (90%+), capstone presented. You are PowerPoint hero.


## FILE: HOW-TO-USE-WITH-AI.md

# How to Use This Package With AI

Four ways to learn faster with AI tools, using the materials in this package. Setup guides are also inlined in the README.

---

## Option 1: NotebookLM (Recommended)

**What it is:** Google's free AI research tool. It answers questions using ONLY your uploaded sources, so it teaches from this curriculum and not from random web guesses.

**Setup:**
1. Go to [notebooklm.google.com](https://notebooklm.google.com) and sign in.
2. Create a notebook named `PowerPoint Zero to Hero`.

**Simplest path: one link, no downloads (recommended).** Click **Add source > Website** and paste this single link. NotebookLM then holds the whole course at once: every module, quiz, cheat sheet, walkthrough, and answer key.

```
https://raw.githubusercontent.com/tempesteni/Microsoft-PowerPoint-Zero-to-hero/main/curriculum-full.md
```

That is it, you are ready to learn. (If a tool ever truncates such a large page, use the per-file path below.)

3. Upload sources in this order (click Add Source for each, the manual path):

| Order | File | Why |
|-------|------|-----|
| 1 | `11-Study-Plan/00-zero-to-hero-study-plans.md` | Gives the AI the curriculum map |
| 2-10 | `01-Fundamentals/` through `09-Real-World-Projects/` module files | The lessons themselves |
| 11 | `10-Sources-References/sources-references-index.md` | Reference context |
| 12-19 | `quizzes/quiz-01-*.md` through `quiz-08-*.md` | Assessment content |
| 20-23 | `cheat-sheets/*.md` | Quick-reference context |
| 24 | `exercises/deck-build-briefs.md` | Practice briefs |

**Copy-paste prompts:**
```
I'm a complete beginner. Explain slide masters from Module 2 like I'm 10 years old, then give me 3 real exercises I can try in PowerPoint right now.
```
```
Quiz me on Module 4 (Tables & Charts). Ask 5 questions one at a time, wait for my answer, then grade me at the end and tell me what to review.
```
```
I have 2 hours today and I'm on the 6-week track in the study plan. What should I study today? Give me a minute-by-minute schedule.
```
```
I work in [your field]. Show me how to build a [monthly report] deck using Modules 3 and 4. Step-by-step, with the exact slide structure.
```
```
I'm about to take quiz-05. Give me a 5-minute refresher of the most important animation concepts and one common trap.
```
**Tip:** use Audio Overview for a podcast-style summary while commuting.

---

## Option 2: ChatGPT / Claude

**Quick-start prompt (paste this first):**
```
I'm learning Microsoft PowerPoint from a structured curriculum. I'll share modules one at a time. For each module:
1. Summarize the 5 most important concepts
2. Explain the hardest concept like I'm a beginner
3. Create 3 quiz questions and wait for my answers
4. Tell me what to focus on next

When I say "quiz me": give me 10 questions (mixed multiple-choice and hands-on tasks) and grade me.
When I say "practice": create a hands-on PowerPoint exercise for me.
When I say "explain [topic]": break it down step by step.

Ready? Here's Module 1: Fundamentals.

[PASTE THE CONTENT OF 01-Fundamentals/01-powerpoint-fundamentals.md HERE]
```

**Follow-up prompts:**
```
I finished Module [X]. Quiz me with 10 questions, then score me out of 100 and tell me which sections to reread.
```
```
I don't understand Morph transitions. Explain 3 ways: like I'm 10, with a business example, and by comparison with ordinary transitions I already know.
```
```
Here's my slide description: [describe]. Design it: give me the layout (positions and sizes in inches), font sizes, and a color palette with hex values.
```
```
Review this deck outline like a presentation coach: [paste outline]. Score it on story, structure, and visual design. Give me the 5 highest-impact fixes.
```

---

## Option 3: AI Agents / RAG Systems

This package is AI-native: every file is structured Markdown with self-contained `##` sections, ready for ingestion.

**Chunking strategy:**
```
Source format: Markdown (.md)
Split by: ## headings (each section is self-contained)
Chunk size: ~500-1500 tokens
Overlap: prepend the parent heading as context to each chunk
```

**Metadata schema:**
```json
{
  "module_number": "01-09",
  "difficulty": "beginner | intermediate | advanced",
  "topic": "fundamentals | design | visual-design | charts | animations | media | delivery | vba | projects",
  "content_type": "lesson | exercise | quiz | cheat_sheet | study_plan | walkthrough",
  "file_path": "relative/path/to/file.md"
}
```

**Agent modes:** Quiz (grade answers from quiz files), Explain (teach from module chunks), Practice (generate exercises from deck-build briefs), Progress (track via progress-tracker.md), Reference (answer from cheat sheets).

**Sample retrieval call:**
```python
chunks = vector_db.search(query=question, top_k=5, filter={"difficulty": user_level})
context = "\n\n".join(c.text for c in chunks)
# prompt: "You are a PowerPoint tutor. Use ONLY this context. Reference the module and section. Answer with an example and suggest what to learn next."
```

---

## Option 4: Anki (no AI, spaced repetition)

See `anki/README.md` for import steps. Short version: Anki > File > Import > `anki/powerpoint-flashcards.csv`, map Front/Back/Tags, import, then 5 new cards a day.

---

## Mixing Approaches

The fastest learners use 2+: e.g. self-study on weekdays, NotebookLM quizzing on weekends, Anki on the bus. Whatever combination you pick, run every quiz in `quizzes/` unassisted first, then use AI to review your mistakes.


## FILE: cheat-sheets/animation-quick-reference.md

# Animation Quick Reference

Purpose: how to animate in PowerPoint without making the audience seasick. Print this: 1 page, portrait, tape to your desk.

One-liner: transitions move between slides (slide to slide); animations move objects on a slide (object to object). Transitions live in the Transitions tab; animations live in the Animations tab.

## 1. The 3-Second Restraint Rule

| Rule | Detail |
|---|---|
| Whole animation sequence on a slide | Max 3 seconds total |
| Single effect duration | 0.25 to 0.5 s for text, up to 1.0 s for big visuals |
| Transitions | 0.5 to 0.75 s. Never longer. |
| Effects per slide | 1 effect type per slide (all Fade or all Wipe) |
| Effects per deck | 2 effect types max (one for text, one for visuals) |
| Purpose test | Every animation must reveal, sequence, or emphasize. If it only decorates, delete it. |

If an animation exists only because "it looks cool", it is costing you credibility. Restraint reads as confidence.

## 2. Animation Start Modes

| Start mode | What it does | When to use | Example |
|---|---|---|---|
| On Click | Plays when you click (advance build) | You narrate point by point and want to control pacing | Revealing 3 arguments one at a time |
| With Previous | Plays at same time as the previous effect (auto) | Paired builds: text + its icon appear together | Bullet + supporting icon fade in together |
| After Previous | Plays right after the previous effect finishes (auto) | Chain of items you want to flow without clicking | 4 bars growing in sequence while you talk |

| Combo pattern | Build it like this |
|---|---|
| Click for each major point | Point 1 (On Click), its icon (With Previous), Point 2 (On Click), its icon (With Previous) |
| One click reveals a full chain | First item (On Click), rest (After Previous, delay 0.2 s each) |
| Self-running kiosk slide | Everything (With Previous or After Previous), set Slide Transition > After: 00:05 |
| Chart build | Chart appears (On Click), then gridlines/series after previous in order |

Anti-pattern: more than 3 clicks per slide of builds. After 3 clicks the audience is waiting, not listening.

## 3. Morph: the Duplicate-Slide Technique (5 steps)

| Step | Action | Detail |
|---|---|---|
| 1 | Design the END state first | On slide A, place objects exactly where they should END up (zoomed map pin, big number, moved label) |
| 2 | Duplicate the slide | Ctrl+D to make slide B right after A. Slide B is your end state (or vice versa) |
| 3 | Set the START state on the earlier slide | On slide A, shrink/move/recolor the objects to their starting position |
| 4 | Apply Morph to the second slide | Select slide B, Transitions tab > Morph. Duration 0.5 to 1.0 s |
| 5 | Match objects with the Selection Pane (if needed) | Name matching objects the same ("!!pin") in Selection Pane (Alt+F10) so PowerPoint pairs them; use !! prefix to force pairing |

Morph works best for: zoom into a region of a map or screenshot, object fly-to-position, text that scales from small label to big headline, step-by-step diagram builds. Morph replaces 5 fiddly motion paths with one transition.

## 4. Trigger Animations in 4 Steps

Use triggers when the audience (not you) picks what happens: click a legend item to reveal its data, click a quiz option to show right/wrong.

| Step | Action | Detail |
|---|---|---|
| 1 | Apply the effect to the target | Select the object that should move/appear, Animations tab > add effect (e.g. Appear) |
| 2 | Open the trigger menu | Animation Pane > right-click the effect > Timing > Triggers > "Start effect on click of" |
| 3 | Pick the trigger object | Choose the clickable shape (a button, an option box, a legend key). It must be an object on the SAME slide |
| 4 | Test in Slide Show mode | Triggers only run in Slide Show, not in Normal view. Click the trigger, verify, click Esc |

Trigger rules: give trigger shapes a visible affordance (border, hover hint) or nobody will click them. Keep 1 to 3 triggers per slide. Escape hatch: also allow the slide to advance normally so a dead click never traps you.

## 5. Timing and Delay Guidance

| Parameter | Guidance |
|---|---|
| Duration: text lines (Fade) | 0.25 to 0.5 s |
| Duration: shapes / images | 0.5 s |
| Duration: big hero visual or Morph | 0.75 to 1.0 s |
| Duration: chart element build | 0.5 s per step |
| Delay between chained items | 0.1 to 0.3 s (After Previous + delay) |
| Delay between click-builds | 0 (you control it live) |
| Total per slide | 3 s ceiling (see restraint rule) |
| Transition duration | 0.5 to 0.75 s, uniform across the deck |
| Transition type | Pick ONE (Fade or Push). Uniformity beats variety. |
| Rehearse Timings | Use only for kiosk/self-running shows, never for live-presented decks |

Speed sanity check: if you have time to read a sentence while an effect plays, the effect is too slow. Cut duration in half.

## 6. The Tacky-Effects Ban List

| Banned | Why |
|---|---|
| Boomerang | Cartoon physics; destroys credibility |
| Bounce | Same |
| Spiral | Disorienting and slow |
| Swivel | Dated since 2003 |
| Grow and Shrink (as decoration) | Reads as a gimmick unless it IS the point of a Morph zoom |
| Random Bars | Visual static |
| Checkerboard | Disco |
| Blinds | Same |
| Dissolve In | Looks like a broken projector |
| Flash Once | Seizure risk in large rooms |
| Whip / Zip / Laser sound effects | Sound off, always |
| Typewriter on long paragraphs | Slower than reading; infuriating |
| Revolve / Roll / Compress | Nausea |
| More than 1 effect type per slide | Confetti, not clarity |
| Animating every bullet with a different effect | Guaranteed seasickness |

Safe list (use these only): Fade, Appear, Wipe (direction = meaning, e.g. wipe left-to-right for a timeline), Fly In (short distance, from same side), Zoom (for Morph-style emphasis), Grow/Spin only inside a Morph zoom. If the effect is not on this list, it is on the ban list.

## 7. Animation Pre-Flight Checklist

| Check | Yes / No |
|---|---|
| Every animation reveals, sequences, or emphasizes | |
| Whole slide animates in 3 s or less | |
| 1 effect type per slide, 2 per deck | |
| Start modes match intent (no accidental extra clicks) | |
| Morph pairs verified in Selection Pane | |
| Triggers tested in Slide Show mode, with an escape | |
| All ban-list effects removed | |
| Transition type and duration uniform across the deck | |
| Sound is off on every effect | |
| Deck still works if all animations fail (content readable statically) | |


## FILE: cheat-sheets/chart-chooser-cheat-sheet.md

# Chart Chooser Cheat Sheet

Purpose: pick the right chart in 5 seconds and clean it so the story is obvious. Print this: 2 pages, portrait, keep beside the chart builder.

Rule zero: a chart exists to prove one sentence. If you cannot write that sentence, do not build the chart.

## 1. Decision Table: Your Story Is... Use This Chart

| Your story is... | Question it answers | Use this chart | Example (fictional data) |
|---|---|---|---|
| Comparison across categories | Which is bigger? | Bar chart (vertical or horizontal) | Renewal rate by region: North 62%, South 55%, East 48% |
| Comparison, few values, big gap | How much bigger? | Horizontal bar, sorted desc | Plan attainment by team: Team A 118%, B 104%, C 87% |
| Comparison of 2 series per category | Which leads and by how much? | Grouped bar (or dumbbell for gap story) | Signups 2025 vs 2026 by quarter |
| Change over time | Is it rising, falling, seasonal? | Line chart | Monthly churn Jan to Dec: 3.1% to 1.8% |
| Change over time, many periods | What is the trend shape? | Line chart with light trendline | Weekly active users over 52 weeks |
| Cumulative total over time | How does the whole add up? | Area chart (stacked area for parts) | Cumulative revenue vs quota by month |
| Composition of a whole (parts) | What is the mix? | Stacked bar (100%) or column | Revenue mix: subscriptions 70%, services 20%, other 10% |
| Composition of a whole (one snapshot) | What share is the biggest slice? | Pie or donut (3 to 5 slices max) | Budget split: payroll 45%, infra 25%, marketing 20%, other 10% |
| Relationship between 2 variables | Do X and Y move together? | Scatter plot | Training hours vs error rate per employee |
| Relationship + size dimension | Does size matter too? | Bubble chart | Ad spend vs revenue, bubble = margin |
| Distribution | Where do values cluster? | Histogram | Deal cycle length across 200 deals |
| Ranking many items | Who is top and bottom? | Sorted horizontal bar (top 10) | NPS by product line, 12 lines, show best and worst 5 |
| Single number that matters | What is the KPI? | Big number card (no chart) | "23.4%" at 66 pt with a one-line qualifier |
| Progress to target | Are we there yet? | Bullet chart or progress bar | 73% of Q3 pipeline goal |
| Flow between stages | Where do we lose them? | Funnel (or bar chart of stages) | Trial to paid: 1000 to 310 to 92 |
| Geographic pattern | Where? | Map (choropleth or dot) | Customers per state |

## 2. When NOT to Use Each Chart

| Chart | Do not use when | Use instead |
|---|---|---|
| Pie | More than 5 slices (or 3 if labels differ much) | Sorted horizontal bar |
| Pie | Comparing 2 pies ("before vs after") | Two 100% stacked bars or a slope chart |
| Pie | Slices are near-equal (readers cannot judge angles) | Bar chart |
| Line | Data is categories, not time (regions, products) | Bar chart |
| Line | Fewer than 3 time points | Bars or just show the 2 numbers |
| Stacked bar | More than 4 to 5 segments per stack | Small multiples or "top 3 + other" |
| Stacked bar | You need precise per-segment comparison across stacks | Grouped bars |
| Dual-axis | Almost always; readers misread it | Two separate charts side by side |
| 3D anything | Always. 3D distorts values and looks dated | Flat 2D chart |
| Donut | More than 5 segments or you need the center for anything real | Bar chart |
| Bubble | More than about 20 bubbles or hard-to-explain size encoding | Scatter + a small table |
| Radar | More than 5 to 6 axes or 2 series | Small multiples of bars |
| Treemap | Audience needs to compare close values | Sorted bars |
| Gauge / speedometer | Always in business decks (chart junk) | Bullet chart or big number |
| Sparkline alone | The audience has never seen a sparkline | Add one labeled value next to it |
| Area | Values can go negative or overlap confusingly | Line chart |

Universal ban list: 3D columns, drop shadows on bars, gradient fills, exploding pie slices, clip-art icons as data marks, and rotated axis labels when horizontal bars would fix it.

## 3. Chart Cleanup Checklist (do all of these)

| Step | Action | Why |
|---|---|---|
| 1. Kill the chart junk | Delete gridlines (or 1 light gray horizontal set at most) | Ink that is not data is noise |
| 2. Legend | If 1 series: delete it, label the series at the end of the line | Legend forces eye ping-pong |
| 3. Legend | If 2 series: label directly at the series, or keep legend but move it to top-left in reading order | Same reason |
| 4. Data labels | Label only the points that carry the story (2 to 4 per chart) | Labeling all 30 points recreates a table |
| 5. Direct labeling | Category labels next to bars, not below a distant axis | Faster reading |
| 6. Axis | One axis is enough when values are labeled directly | Less chrome |
| 7. Honest axes | Numeric axis must start at zero for bars and areas | Non-zero baselines exaggerate change |
| 8. Honest axes | Line charts may truncate, but show the truncation clearly (axis break or note) | Truncation hides magnitude |
| 9. Honest axes | No reversed axes, no skipping intervals | Reversed axes invert the story |
| 10. Color | Story series in the 10% accent color, context series in gray | Pre-attentive highlight |
| 11. Color | Same category keeps the same color across every chart in the deck | Consistency |
| 12. Title | Chart title = the claim, not "Revenue by Quarter" | Assertion-evidence |
| 13. Units | Put units in the axis or label ("$K", "%"), not repeated 20 times | Clarity |
| 14. Sort | Sort bars by value, not alphabetically, unless category order is meaningful | Ranking shows instantly |
| 15. Font | Labels 10 to 14 pt minimum, one font family | Readable at distance |
| 16. Border | Delete the chart border and plot area fill | Cleaner silhouette |
| 17. Numbers | Consistent decimals: 12.3% not 12.31% in one place and 12% in another | Trust |
| 18. Source | Footnote: source + period + sample ("Internal CRM, Q1-Q3 2026, n=2,400") | Credibility |

## 4. Story-to-Chart in One Line (memorize)

| Story verb | Chart |
|---|---|
| Compares | Bar |
| Trends | Line |
| Composes | Stacked bar or small pie |
| Relates | Scatter |
| Distributes | Histogram |
| Ranks | Sorted horizontal bar |
| Targets | Bullet or big number |
| Flows | Funnel |
| Locates | Map |

## 5. Fix-a-Broken-Chart Examples (fictional data)

| Broken chart | Diagnosis | Fix |
|---|---|---|
| 8-slice pie of ticket types | Angles unreadable | Sorted horizontal bar, "top 5 + other" |
| 3D column of monthly sales | Perspective distorts heights | Flat columns, labels on Jun (142) and Dec (188) |
| Line chart of 5 product categories over 1 quarter | Categories are not time | Grouped bars |
| Dual axis: ad spend (bars) + revenue (line) | Two scales invite misreading | Two small charts side by side |
| Bar chart, axis starts at 30 | Bar at 60 looks 2x bar at 45 | Restart axis at zero, annotate the change instead |
| Stacked bar with 7 segments | Nobody can compare segment 4 | Collapse to top 3 + Other |
| Chart titled "Q3 Performance" | Says nothing | Retitle: "Q3 pipeline hit 73% of goal" |

## 6. 30-Second Chart Pre-Flight

| Check | Yes / No |
|---|---|
| Chart title states the claim | |
| Right chart type for the story verb | |
| Gridlines, borders, junk removed | |
| Labels are direct, not legend-dependent | |
| Axis starts at zero (or truncation is declared) | |
| 1 accent color for the story, rest gray | |
| Units and source noted | |
| Passes the 5-second glance test | |


## FILE: cheat-sheets/keyboard-shortcuts-cheat-sheet.md

# PowerPoint Keyboard Shortcuts Cheat Sheet

Purpose: every shortcut worth memorizing in PowerPoint, scannable in 10 seconds. Print this: 2 pages, portrait.

Legend: "Yes" = same on Mac. Ctrl on Windows = Cmd on Mac in nearly all cases.

## 1. File and App Control

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| Ctrl+N | New presentation | Yes |
| Ctrl+O | Open presentation | Yes |
| Ctrl+S | Save | Yes |
| Ctrl+Shift+S | Save As | Yes |
| Ctrl+P | Print with preview | Yes |
| Ctrl+W | Close presentation | Yes |
| Ctrl+Z | Undo | Yes |
| Ctrl+Y or F4 | Redo / repeat last action | Yes |
| Alt+F4 | Quit PowerPoint | Mac alt: Cmd+Q |
| F1 | Help | Yes |
| Ctrl+F1 | Collapse / expand Ribbon | Mac alt: Cmd+Opt+R |
| Alt, then letters | Ribbon KeyTips | No |
| Ctrl+K | Insert hyperlink | Yes |

## 2. Navigating and Slide Editing

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| Ctrl+M | New slide | Yes |
| Ctrl+D | Duplicate slide or object | Yes |
| Delete | Delete selected slide(s) | Yes |
| Ctrl+X / Ctrl+C / Ctrl+V | Cut / copy / paste | Yes |
| Ctrl+G / Ctrl+Shift+G | Group / ungroup | Yes |
| Page Down or Down | Next slide (Normal view) | Yes |
| Page Up or Up | Previous slide | Yes |
| Home / End | First / last slide | Yes |
| Ctrl+Up / Ctrl+Down | Move slide up / down in deck | Yes |
| Tab / Shift+Tab | Select next / previous object | Yes |
| Escape | Deselect or cancel | Yes |
| Ctrl+A | Select all objects or text | Yes |
| F6 | Cycle panes: thumbnail, canvas, notes, ribbon | Yes |
| F2 | Edit text in selected shape | Yes |

## 3. Text Formatting

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| Ctrl+B / Ctrl+I / Ctrl+U | Bold / italic / underline | Yes |
| Ctrl+E / Ctrl+L / Ctrl+R | Center / left / right align | Yes |
| Ctrl+J | Justify | Yes |
| Ctrl+T | Font dialog | Yes |
| Ctrl+Shift+> / Ctrl+Shift+< | Grow / shrink font | Yes |
| Ctrl+] / Ctrl+[ | Grow / shrink font 1 pt | Yes |
| Ctrl+Shift+L | Apply bullet | Yes |
| Shift+F3 | Cycle UPPERCASE / lowercase / Sentence | Yes |
| Ctrl+= / Ctrl+Shift+= | Subscript / superscript | Yes |
| Tab / Shift+Tab | Demote / promote bullet level | Yes |
| Ctrl+Enter | New slide (outside text edit) | Yes |

## 4. Selecting, Moving, Resizing Objects

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| Shift+click or Ctrl+click | Add object to selection | Yes |
| Arrow keys | Nudge object | Yes |
| Ctrl+Arrow keys | Fine nudge | Yes |
| Shift+drag | Constrain move to axis | Yes |
| Ctrl+drag | Copy while dragging | Yes |
| Ctrl+Shift+drag | Copy and constrain axis | Yes |
| Shift+drag corner | Resize keeping proportions | Yes |
| Ctrl+drag handle | Resize from center | Yes |
| Ctrl+Shift+C / Ctrl+Shift+V | Copy / paste formatting (Format Painter) | Yes |
| F4 | Repeat last formatting | Yes |
| Alt+drag handle | Resize without snapping | Yes |

## 5. Align, Distribute, Order (KeyTips after Alt)

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| Alt+H+G+A+L | Align left | Ribbon only |
| Alt+H+G+A+C | Align center horizontal | Ribbon only |
| Alt+H+G+A+T | Align top | Ribbon only |
| Alt+H+G+A+M | Align middle vertical | Ribbon only |
| Alt+H+G+R | Bring to front | Ribbon only |
| Alt+H+G+S | Send to back | Ribbon only |
| Alt+F9 | Show / hide alignment guides | No |
| Drag + orange guides | Snap and distribute equal spacing | Yes |
| F7 | Spell check | Yes |

## 6. Slideshow Control (during the show)

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| F5 | Start from first slide | Yes |
| Shift+F5 | Start from current slide | Yes |
| N, Space, Right, Enter, click | Next slide / build | Yes |
| P, Backspace, Left | Previous slide | Yes |
| B or period | Black screen toggle | Yes |
| W or comma | White screen toggle | Yes |
| Number + Enter (e.g. 7, Enter) | Jump to slide 7 | Yes |
| Ctrl+L | Laser pointer | Mac alt: Opt+Cmd+L |
| Ctrl+P / Ctrl+A | Pen / arrow pointer | Mac alt: Opt+Cmd+P |
| Ctrl+E | Erase annotations | Mac alt: Opt+Cmd+E |
| E | Erase pen markings | Yes |
| S | Stop / restart automatic show | Yes |
| F1 | List all show shortcuts | Yes |
| Esc | End show | Yes |

## 7. Presenter View

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| Alt+F5 | Start show in Presenter View | No |
| F5 with 2 monitors | Presenter View auto (if enabled) | Yes |
| Ctrl+P / Ctrl+A / Ctrl+E | Pen / arrow / erase | Yes |
| Ctrl+L | Laser pointer | Varies |
| S | Slide sorter panel in Presenter View | Varies |
| Esc | Exit Presenter View | Yes |
| Slide > Set Up Show | Toggle "Use Presenter View" | Yes |

## 8. VBA Editor

| Shortcut (Windows) | Action | Also on Mac? |
|---|---|---|
| Alt+F11 | Open / close VBA editor | Mac alt: Opt+F11 |
| Alt+F8 | Macro dialog (run macro) | Mac alt: Opt+F8 |
| Ctrl+G | Immediate window | Yes |
| F5 | Run current macro | Yes |
| F8 | Step into (debug line by line) | Yes |
| Shift+F8 | Step over | Yes |
| Ctrl+F8 | Step out | Yes |
| F9 / Ctrl+Shift+F9 | Toggle / clear breakpoints | Yes |
| F2 | Object Browser | Yes |
| Ctrl+R | Project Explorer | Yes |
| F7 | View code for object | Yes |
| Ctrl+F / Ctrl+H | Find / replace in code | Yes |
| F4 | Properties window | Yes |

## 9. Memorize These 15 First

| Shortcut | Why |
|---|---|
| F5 / Shift+F5 | Start show from first / current slide |
| Esc | Get out of anything |
| Ctrl+D | Duplicate anything |
| Ctrl+M | New slide |
| Ctrl+Shift+C / V | Copy / paste formatting |
| Ctrl+G / Ctrl+Shift+G | Group / ungroup |
| B (during show) | Blank the screen |
| Ctrl+L (during show) | Laser pointer |
| Shift+drag | Straight-line constrain |
| F4 | Repeat last action |
| Alt+F11 | VBA editor |
| Ctrl+K | Hyperlink |
| Tab (on canvas) | Cycle objects without mouse |
| Shift+F3 | Swap case |
| F7 | Spell check |


## FILE: cheat-sheets/slide-design-rules-cheat-sheet.md

# Slide Design Rules Cheat Sheet

Purpose: the one-page rules for slides that read fast and look professional. Print this: 1 page, portrait, pin it next to your monitor.

Design rule zero: a slide is a billboard, not a document. If the audience is reading, they are not listening.

## 1. Type and Size Rules

| Element | Size | Rule |
|---|---|---|
| Title | 36 to 44 pt | Max 2 lines. Never smaller than 30 pt in any room. |
| Body text | 14 to 24 pt | 18 to 24 pt for live rooms; 14 to 18 pt only for handout-style decks. |
| Subtitles / labels | 12 to 16 pt | Never below 12 pt. Nothing on a projected slide below 12 pt. |
| Axis labels on charts | 10 to 14 pt | Chart content should not be smaller than body text by more than one step. |
| Footnotes / source lines | 8 to 12 pt | Fine to be small, since nobody reads them out loud. |

| Type rule | Do | Do not |
|---|---|---|
| Fonts per deck | 1 sans (body) + optionally 1 serif (titles) | 3+ fonts or decorative / novelty fonts |
| Line length | 45 to 75 characters per line | Full-width paragraphs that wrap past 3 lines |
| Line spacing | 1.1 to 1.3 | Default tight spacing or double spacing |
| Emphasis | Bold or color, pick one | Bold + italic + underline + color at once |
| ALL CAPS | Short labels only (max 3 to 4 words) | Full sentences in caps (readability drops fast) |
| Alignment | Left-aligned for body, centered for titles | Justified text (uneven word gaps) |

## 2. Content Density: the 6x6 Rule

| Rule | Meaning | Realistic version |
|---|---|---|
| 6x6 classic | Max 6 bullets per slide, max 6 words per bullet | Fine for student and conference decks |
| 5x5 stricter | 5 bullets, 5 words each | Good default for business reviews |
| 1 idea per slide | One claim, one visual | The actual best rule. Break big slides into 3 smaller ones. |
| When you must be dense | Use a table or handout page, not a bullet wall | Dense = appendix or PDF companion, not projected |

Anti-pattern check: if the slide has more than about 40 words total on it, split it or move the text to the notes field.

## 3. Structure: Assertion-Evidence

| Part | What it is | Example (fictional data) |
|---|---|---|
| Assertion (the title) | A full sentence claim the slide proves | "Renewals rose 18% after the Q2 onboarding change" |
| Evidence (the body) | One chart, diagram, or 3 bullets that prove it | Bar chart of renewal rate, Jan to Jun |
| Old way (avoid) | Topic label title | "Renewal Results" (says nothing; audience waits for the point) |

| Slide job | Title pattern | Body should hold |
|---|---|---|
| Persuade | Claim sentence | Proof: numbers, quote, diagram |
| Orient | Agenda or roadmap (allowed as labels) | 3 to 6 sections with time estimates |
| Recap | "Three things to remember" | Exactly 3 bullets, no new information |

Test: cover the body. Can the title alone tell the story of the deck in order? If yes, your structure works.

## 4. Color: the 60-30-10 Rule

| Share | Use for | Example palette (fictional) |
|---|---|---|
| 60% | Background / dominant surface | Off-white #F7F5F0 or dark navy #1B2A41 |
| 30% | Secondary: text blocks, shapes, cards | Slate gray #4A5568, headings #2D3748 |
| 10% | Accent: highlights, key numbers, CTAs | Teal #14B8A6 or amber #F59E0B (one accent only) |

| Color rule | Pass condition |
|---|---|
| One accent color | Only 1 hue pops. Two accents = neither pops. |
| Contrast | Body text at least 4.5:1 against background (WCAG AA). Titles 3:1 or better. |
| Meaning color | Red/green only for good/bad meaning, and pair with + / - signs for color-blind readers |
| Brand color | Use it in the 10% accent slot or the 30% slot, never for everything |
| Dark mode decks | Light gray text (#E2E8F0) on dark background beats pure white on pure black |

## 5. CRAP Principles Checklist

| Principle | Question to ask | Failing sign |
|---|---|---|
| Contrast | Is it obvious what is important? | Everything same size, same weight, same gray |
| Repetition | Do fonts, colors, and layouts repeat across slides? | Slide 4 looks like it came from a different deck |
| Alignment | Is everything on a grid or snapping to guides? | Elements floating 5 px off from each other |
| Proximity | Are related items close, unrelated items spaced? | A label closer to the wrong chart than its own |

Quick pass: turn on View > Gridlines and Guides. Anything misaligned more than a hairline is visible from row 10 of the room.

## 6. Image Rules

| Rule | Do | Do not |
|---|---|---|
| Scaling | Crop hard to fill the space (crop to subject) | Stretch or squash to fit (aspect ratio never distorts) |
| Fill | Picture Fill in a shape, or Crop > Fill | Dragging corner handles at random |
| Size | Go big: full-bleed or half-slide minimum | Tiny 1-inch clip art in the corner |
| Relevance | Image supports the claim | Decorative stock photos of handshakes and globes |
| Source | Cite photographer or stock source in the footnote | Uncited images from a search engine |
| Screenshots | Zoom into the 1 region that matters | Whole-desktop screenshots with unreadable text |
| Resolution | At least 150 dpi at final projected size | Blurry upscaled thumbnails |

Micro-example of the crop rule: a 3:2 photo in a 16:9 frame should be cropped at the sides or top and bottom, never resized non-proportionally. Hold Shift while dragging a corner if you must free-resize.

## 7. The 5-Second Glance Test

| Step | How | Pass |
|---|---|---|
| 1. Show the slide for 5 seconds | Full screen, then press Esc or B | Ask: "What did you see?" |
| 2. Listener names the point | They should say the title's claim | If they say "um, numbers?" it failed |
| 3. Listener recalls one element | One number, one image | If zero, the slide is noise |
| 4. Check the title alone | Read only the titles in sequence | Story is coherent without any bodies |

Run this on every slide before you present. Anything failing twice gets split or deleted.

## 8. Before / After Micro-Examples

| Before (fails) | Problem | After (passes) |
|---|---|---|
| Title: "Q3 Overview" with 9 bullets, 11 pt | Topic title + density | Title: "Q3 revenue beat plan by 7%" + one chart + 3 bullets at 20 pt |
| Chart with gridlines, legend on right, default Office colors | Clutter + no hierarchy | One series in teal accent, others gray, data labels on the 2 key bars |
| Photo stretched to a square from a landscape | Distorted aspect ratio | Photo cropped to square around the subject, full-bleed left half |
| Body text 4 colors: red, green, blue, orange highlights | No accent logic | All body #2D3748, one number in teal + bold |
| 3 bullet paragraphs of 4 lines each at 14 pt | Handout on a slide | Move paragraphs to notes; slide gets 3 six-word bullets at 22 pt |
| Logo on every slide at 2 inches tall | Visual noise | Logo 0.6 inch in the corner, or on title and closing slides only |
| Justified paragraph with big word gaps | Poor typography | Left-aligned, ragged right |
| Screenshot of a full spreadsheet | Unreadable at distance | Cropped to 4 rows and 2 columns that prove the point, 18 pt labels added |

## 9. Pre-Flight Checklist (30 seconds)

| Check | Yes / No |
|---|---|
| Every title is a claim sentence (except agenda/recap) | |
| No slide over 40 words of body text | |
| Smallest text on any slide is 12 pt or larger | |
| One accent color only, contrast passes | |
| All images crop-fitted, never stretched | |
| Titles read as a story in sequence | |
| 5-second glance test passed on every slide | |
| Deleted at least 3 slides from the first draft | |


## FILE: quizzes/quiz-01-fundamentals.md

# Quiz 01: PowerPoint Fundamentals

**Module tested:** Module 1 (PowerPoint Zero to Hero) - Interface, views, slides, placeholders vs text boxes, outline view, bullet discipline, sections, slide size, file formats, saving/autosave, basic shortcuts

## Instructions

- Answer all 15 multiple-choice questions in Section A (3 points each).
- Complete all 5 practical challenges in Section B in PowerPoint (5 points each).
- Total: 70 points. Time limit: 30 minutes recommended.
- No notes or help files during the quiz. Work in a blank presentation unless a question says otherwise.
- All company data used in questions is fictional (YourCompany Inc).

## Scoring

| Score | Percentage | Result |
|---|---|---|
| 63-70 pts | 90%+ | Advance to the next module |
| 49-62 pts | 70-89% | Review your weak areas, then move on |
| Below 49 pts | Below 70% | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 questions, 3 points each = 45 points)

**1. (Easy)** You open PowerPoint for the first time and land on the startup screen. What is the name of the main horizontal strip across the top of the window that groups commands into tabs such as Home, Insert, and Design?

- A) The Status Bar
- B) The Ribbon
- C) The Quick Access Pane
- D) The Slide Sorter

**2. (Easy)** Which view shows thumbnails of all your slides in a grid so you can quickly reorder them?

- A) Normal view
- B) Reading view
- C) Slide Sorter view
- D) Presenter view

**3. (Easy)** You are typing a company overview for YourCompany Inc. The slide was created from a Title and Content layout and has a dotted-line box that says "Click to add text." What is that box called?

- A) A text box
- B) A placeholder
- C) A shape
- D) A content frame

**4. (Easy)** What is the main practical difference between a placeholder and a text box you insert yourself?

- A) Placeholders cannot hold text
- B) Text boxes are governed by the slide layout and placeholders are free-floating
- C) Placeholders are tied to the slide layout and inherit formatting from it; inserted text boxes are free-floating and keep only the formatting you apply
- D) There is no difference

**5. (Easy)** Which file format saves a presentation as a standard editable PowerPoint file?

- A) .potx
- B) .pptx
- C) .ppsx
- D) .pdf

**6. (Easy)** You want the slide content typed in Outline view to flow into the correct title and body areas automatically. What must you type into?

- A) Inserted text boxes
- B) The placeholders provided by the layout
- C) A table
- D) The Notes pane

**7. (Medium)** You are building the 2026 sales review deck for YourCompany Inc and have 40 slides with no structure. What is the best built-in feature to group related slides under headings like "Q1 Results" and "Q2 Forecast" in the thumbnail pane?

- A) Sections
- B) Custom shows
- C) Summary zoom
- D) Comments

**8. (Medium)** A colleague set your presentation's slide size to On-screen Show (16:9), but the YourCompany Inc annual report must be printed on standard letter paper in portrait orientation. Where do you change this?

- A) Home tab, Layout dropdown
- B) Design tab, Slide Size, then Custom Slide Size
- C) File, Options, Advanced
- D) View tab, Notes Master

**9. (Medium)** Which statement about Outline view is correct?

- A) It shows speaker notes only
- B) It displays slide titles and bullet text as a structured outline and lets you promote, demote, and reorder content quickly with Tab and Shift+Tab
- C) It hides all text and shows only pictures
- D) It is only available after you save the file

**10. (Medium)** In Outline view, what do Tab and Shift+Tab do to a line of text?

- A) Insert a tab space or remove a tab space
- B) Demote the line one outline level or promote it one level
- C) Bold or unbold the text
- D) Move the line to the next slide or previous slide

**11. (Medium)** Your bullet list on the YourCompany Inc product slide has 7 bullets, each holding two long sentences. What is the recommended bullet discipline fix?

- A) Keep all 7 bullets and shrink the font to 10 pt
- B) Cut the list to the key points, aim for a handful of bullets with a few words each, and move detail to the speaker notes
- C) Convert the bullets to a table
- D) Delete the bullets and paste them into the Notes pane as an image

**12. (Medium)** What does the .potx file extension indicate?

- A) A slide show that opens directly in presentation mode
- B) A read-only finished presentation
- C) A PowerPoint template that spawns a new presentation when opened, protecting the original
- D) A video export of the slides

**13. (Hard)** You are offline on a flight and notice AutoSave is greyed out in the top-left corner of PowerPoint. What is the most likely reason?

- A) The file has too many slides
- B) The presentation has never been saved, or it is saved somewhere without connected cloud storage such as OneDrive or SharePoint, so AutoSave cannot run
- C) AutoSave only works in Slide Sorter view
- D) AutoSave is disabled on all versions of PowerPoint

**14. (Hard)** Which action is the fastest way to reorder slide 12 to become slide 3 in a long deck while keeping its formatting intact?

- A) Copy the contents of slide 12 into a new slide 3 and delete slide 12
- B) Use Outline view or Slide Sorter to drag the whole slide 12 thumbnail to the position after slide 2
- C) Cut every slide after slide 2 and paste it after slide 12
- D) Save the file under a new name and rebuild the order

**15. (Hard)** Which pair of keyboard shortcuts correctly matches its function in PowerPoint?

- A) Ctrl+M inserts a new slide; Ctrl+D duplicates the selected slide or object
- B) Ctrl+M opens the master view; Ctrl+D deletes a slide
- C) Ctrl+N starts a slideshow; Ctrl+D draws a text box
- D) Ctrl+M moves a slide; Ctrl+D saves the file

---

## Section B: Practical Challenges (5 challenges, 5 points each = 25 points)

Perform each task in PowerPoint. Success criteria describe what a correct result looks like.

**P1. Build a starter deck.** Create a new blank presentation for YourCompany Inc and make exactly 4 slides: slide 1 uses the Title Slide layout with the title "YourCompany Inc Kickoff" and subtitle "Q1 Planning Session"; slides 2 to 4 use the Title and Content layout with the titles "Agenda", "Goals", and "Next Steps". Enter one placeholder bullet on each content slide.
*Success criteria:* 4 slides, correct layouts used (not text boxes typed over blank layouts), correct titles, one bullet visible on each of slides 2-4.

**P2. Organize with sections.** Add two sections to the deck from P1: name the first "Opening" containing slide 1, and the second "Planning" containing slides 2 to 4. Then collapse the "Planning" section so only its header shows.
*Success criteria:* Both section names appear above the correct slides in the thumbnail pane, and the Planning section is collapsed.

**P3. Fix slide size and inspect file formats.** Set the presentation from P1 to A4 paper size in landscape orientation using Custom Slide Size, and choose "Ensure Fit" if prompted. Then save the file twice: once as YourCompany-Kickoff.pptx and once as YourCompany-Kickoff.potx.
*Success criteria:* Slide size dialog shows A4 landscape; both files exist with the correct extensions; opening the .potx creates a new presentation rather than editing the template itself.

**P4. Rebuild a bad slide using placeholders and bullets.** On a new slide using the Title and Content layout, create the title "YourCompany Inc Values". In the CONTENT PLACEHOLDER (not a drawn text box), enter exactly 3 short bullets: "Integrity", "Innovation", "Customer First". Then split one of them into a second-level sub-bullet using Tab (then return it to level 1 with Shift+Tab before finishing).
*Success criteria:* The text sits inside the layout placeholder (moves with Reset), exactly 3 top-level bullets remain at the end, and the outline indentation levels were demonstrably changed and restored.

**P5. Use Outline view and shortcuts.** Switch to Outline view and add a new slide with the title "Q2 Forecast" containing 2 bullets: "Revenue target" and "Pipeline risks". Return to Normal view and use a keyboard shortcut to duplicate that slide once. Finish by pressing Ctrl+S to save.
*Success criteria:* The new slide and its bullets were created in Outline view, a duplicate slide exists (6 slides total if starting from the deck after P1-P4 additions), and the file is saved.

---

---

# ANSWER KEY (spoilers below)

**Section A**

1. **B** - The Ribbon is the tabbed command strip (Home, Insert, Design, etc.) across the top of the PowerPoint window.
2. **C** - Slide Sorter shows the whole deck as a grid of thumbnails, ideal for reordering and bulk work.
3. **B** - The dotted "Click to add text" box is a placeholder supplied by the slide's layout.
4. **C** - Placeholders belong to the layout and inherit its formatting; text boxes you insert are independent objects.
5. **B** - .pptx is the standard editable presentation format. .potx is a template, .ppsx opens as a show, .pdf is fixed-layout.
6. **B** - Only layout placeholders map to the outline structure; text typed in inserted text boxes does not appear in Outline view as structured content.
7. **A** - Sections let you name and collapse groups of slides in the thumbnail pane for organization.
8. **B** - Design tab, Slide Size, Custom Slide Size lets you pick paper size and orientation (portrait/landscape).
9. **B** - Outline view shows titles and bullet text as a structured outline for fast editing and reordering.
10. **B** - Tab demotes an outline line one level (sub-bullet); Shift+Tab promotes it back one level.
11. **B** - Bullet discipline means few bullets, few words each; details belong in speaker notes or the discussion.
12. **C** - .potx is a template: opening it creates a new presentation so the master stays clean.
13. **B** - AutoSave requires the file to be saved to connected cloud storage (OneDrive/SharePoint); local or unsaved files cannot use it.
14. **B** - Dragging the whole slide in the outline/sorter pane moves the entire slide with all formatting intact.
15. **A** - Ctrl+M inserts a new slide and Ctrl+D duplicates the selection.

**Section B - model solutions**

**P1:** File > New > Blank Presentation. Slide 1: Home > Layout > Title Slide; type title and subtitle into the placeholders. For slides 2-4: Ctrl+M for each, set Home > Layout > Title and Content, type titles and one bullet each in the content placeholder.

**P2:** Right-click above slide 1 > Add Section > name "Opening". Right-click above slide 2 > Add Section > name "Planning". Click the triangle/caret next to "Planning" to collapse it.

**P3:** Design > Slide Size > Custom Slide Size > set "Slides sized for" to A4 Paper (297x210 mm), orientation Landscape > OK > Ensure Fit. File > Save As > YourCompany-Kickoff.pptx (choose PowerPoint Presentation). Then File > Save As > YourCompany-Kickoff.potx (choose PowerPoint Template). Verify: double-clicking the .potx opens "Presentation1" or similar.

**P4:** New slide with Title and Content layout. Type title in the title placeholder. Click into the content placeholder and type the 3 bullets (Enter between each). Select a bullet and press Tab to demote it (Shift+Tab to promote again). Verify the text is in the placeholder: Home > Reset and the text stays put and realigns to the layout.

**P5:** View > Outline. Click at the end of the outline, press Enter to start a new slide, type "Q2 Forecast", press Enter then Tab (or use the demote button) and type "Revenue target", Enter, "Pipeline risks". Back in Normal view, select the slide thumbnail and press Ctrl+D to duplicate. Ctrl+S to save.


## FILE: quizzes/quiz-02-design-foundations.md

# Quiz 02: Design Foundations (Themes, Masters, and Templates)

**Module tested:** Module 2 (PowerPoint Zero to Hero) - Themes, variants, slide master vs layouts, editing masters, placeholders, .potx templates, backgrounds, Reset, Design Ideas

## Instructions

- Answer all 15 multiple-choice questions in Section A (3 points each).
- Complete all 5 practical challenges in Section B in PowerPoint (5 points each).
- Total: 70 points. Time limit: 30 minutes recommended.
- No notes or help files during the quiz. Work in a blank presentation unless a question says otherwise.
- All company data used in questions is fictional (YourCompany Inc).

## Scoring

| Score | Percentage | Result |
|---|---|---|
| 63-70 pts | 90%+ | Advance to the next module |
| 49-62 pts | 70-89% | Review your weak areas, then move on |
| Below 49 pts | Below 70% | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 questions, 3 points each = 45 points)

**1. (Easy)** Where do you find the built-in themes gallery in PowerPoint?

- A) Home tab
- B) Design tab
- C) Slide Show tab
- D) Review tab

**2. (Easy)** What is a theme in PowerPoint?

- A) A single font choice applied to one slide
- B) A coordinated set of colors, fonts, and effects that gives the whole presentation one consistent look
- C) A slide transition
- D) A saved selection of animations

**3. (Easy)** What is the relationship between the slide master and its layouts?

- A) They are unrelated
- B) The slide master is the parent that controls common formatting for the whole presentation; each layout is a child that defines the arrangement of placeholders for a slide type and inherits from the master
- C) Layouts control the master
- D) The slide master only affects the title slide

**4. (Easy)** You want to change the title font for EVERY slide in your YourCompany Inc deck at once. Where should you edit it?

- A) On each slide, one by one
- B) On the slide master (View > Slide Master)
- C) In the Notes pane
- D) In Print Preview

**5. (Easy)** What does the Reset button on the Home tab do to a slide?

- A) Deletes the slide
- B) Reapplies the layout's placeholder positions, sizes, and formatting to the slide, undoing manual formatting drift
- C) Restarts the slide show
- D) Clears the slide to blank

**6. (Easy)** A .potx file is best described as:

- A) A finished presentation delivered to a client
- B) A reusable template that generates a fresh presentation when opened, leaving the template itself unchanged
- C) A font package
- D) A video of the slides

**7. (Medium)** Your YourCompany Inc deck uses a theme, and leadership wants the same design but with a different coordinated color set. What is the fastest correct change?

- A) Recolor every slide manually
- B) On the Design tab, pick a different Variant of the same theme
- C) Change the slide master's background only
- D) Apply a transition

**8. (Medium)** What is the key difference between a theme and a theme variant?

- A) A variant is a new design; a theme is a font only
- B) A variant is an alternate color scheme, font set, or effect set offered WITHIN the same theme, letting you restyle without changing the theme itself
- C) Variants exist only in older PowerPoint versions
- D) There is no difference

**9. (Medium)** Where do you edit theme fonts (the heading and body font pair) so the change propagates through the deck?

- A) By selecting all text and choosing a font on the Home tab
- B) Design tab, Variants group, Fonts dropdown (or in Slide Master view via Background/Fonts styling)
- C) Insert tab, Text Box
- D) File, Info, Properties

**10. (Medium)** In Slide Master view, which statement is correct about placeholders?

- A) Placeholders cannot be moved on layouts
- B) Placeholder formatting and positioning set on the master or a layout flow to slides that use it; text typed on the master (like a logo caption) appears on all slides using that layout
- C) Master placeholders only affect slide 1
- D) Deleting a placeholder on a layout deletes all slides

**11. (Medium)** You applied a polished layout to the YourCompany Inc investor deck, but someone dragged the body placeholder around on slide 5. How do you snap slide 5 back to the layout's design?

- A) Press Ctrl+Z until the slide is gone
- B) Select slide 5 and click Home > Reset
- C) Delete slide 5
- D) Change the theme

**12. (Medium)** Where can you set a picture, solid fill, or gradient as a slide background?

- A) Insert tab, Pictures
- B) Design tab, Format Background (or Design > Background Styles > Format Background)
- C) View tab, Handout Master
- D) Transitions tab

**13. (Hard)** A colleague edits the Title and Content layout's title placeholder on the slide master and moves it up by 0.5 inch. What happens?

- A) Nothing changes on existing slides
- B) Every slide using that layout updates its title position (unless a slide has manual overrides that survive Reset only until Reset is used)
- C) Only new presentations change
- D) Only slide 1 changes

**14. (Hard)** Design Ideas (Designer) suggests layouts automatically. Which statement is most accurate?

- A) It redesigns the deck permanently with no undo
- B) It offers design suggestions based on your content and theme that you can preview and apply, and you can undo or pick another suggestion afterward
- C) It only works offline
- D) It replaces the need for the slide master entirely

**15. (Hard)** Your YourCompany Inc template (.potx) should enforce the brand fonts AND a fixed logo on every content slide. What is the correct build?

- A) Place the logo and set fonts on each slide of a .pptx and share it
- B) In Slide Master view, set the theme fonts and place the logo on the slide master or on each layout (so it appears in the placeholder-free zone), then save as .potx
- C) Save a .pptx as .pptx and rename the extension
- D) Add the logo in Presenter view

---

## Section B: Practical Challenges (5 challenges, 5 points each = 25 points)

Perform each task in PowerPoint. Success criteria describe what a correct result looks like.

**P1. Apply and vary a theme.** Create a new blank presentation for YourCompany Inc. Apply any built-in theme, then switch to a different Variant of that same theme. Add one Title and Content slide with the title "YourCompany Inc Overview" and one bullet.
*Success criteria:* The Design tab shows the theme applied; the variant change restyles colors/fonts without losing slide content; the slide text remains in place.

**P2. Edit the slide master.** Open Slide Master view. On the parent slide master (the top thumbnail), set the title placeholder text to 36 pt bold and move the body text placeholder slightly to the right. Close Master View and verify the change on a normal slide.
*Success criteria:* Title text on regular slides inherits 36 pt bold; body text inherits the new position; edits were made on the master, not on individual slides.

**P3. Create a custom layout change.** In Slide Master view, duplicate the "Title and Content" layout and rename it "YourCompany Report". On the duplicated layout, add a small text box with "CONFIDENTIAL" near the bottom of the slide. Close Master View and apply the "YourCompany Report" layout to one slide.
*Success criteria:* A custom layout named "YourCompany Report" exists; the slide using it shows "CONFIDENTIAL"; other layouts remain unchanged.

**P4. Background and Reset.** Set a solid background fill (any brand-acceptable color, e.g., dark blue) via Design > Format Background on one slide only (click "Apply to All" only if you intend all). Then manually move the title placeholder off-center on that slide and use Home > Reset to restore it.
*Success criteria:* The background fill appears on the intended slide(s); the manually moved title snaps back to the layout position after Reset.

**P5. Build and use a template.** Save the presentation from P1-P4 as YourCompany-Template.potx. Close it, then create a NEW presentation from that template (File > New > Personal/Custom > YourCompany-Template). Verify the theme, custom layout, and background survive in the new file.
*Success criteria:* The .potx exists; a new presentation spawned from it inherits the theme and the "YourCompany Report" layout; the template file itself is not modified by editing the new deck.

---

---

# ANSWER KEY (spoilers below)

**Section A**

1. **B** - The Design tab hosts the Themes gallery and Variants.
2. **B** - A theme bundles colors, fonts, and effects so the whole deck looks coordinated.
3. **B** - The master is the parent for common formatting; layouts are children defining placeholder arrangements and inherit from the master.
4. **B** - Edit the title formatting once on the slide master to update every slide that uses it.
5. **B** - Reset re-applies the layout's placeholder geometry and formatting, cleaning up manual drift.
6. **B** - .potx is a template: it spawns a new presentation and protects the original.
7. **B** - Variants provide alternate coordinated color/font/effect sets within the current theme.
8. **B** - A variant restyles within a theme; it is not a whole new design.
9. **B** - Theme fonts are managed from Design > Variants > Fonts (and can be customized there).
10. **B** - Master/layout placeholder formatting propagates to slides; text placed on a master appears wherever that master/layout is used.
11. **B** - Home > Reset snaps the slide's placeholders back to the layout design.
12. **B** - Design > Format Background sets solid, gradient, picture, or texture backgrounds.
13. **B** - Layout edits propagate to all slides using that layout; manual slide-level overrides persist until Reset is pressed.
14. **B** - Design Ideas is a suggestion engine you can preview, apply, undo, and swap.
15. **B** - Brand enforcement belongs in Slide Master view (theme fonts + logo on master/layouts) saved as .potx.

**Section B - model solutions**

**P1:** New blank presentation. Design tab > pick a theme from the gallery. In the Variants group, click a different variant thumbnail (or Variants > Colors). Home > New Slide > Title and Content; type "YourCompany Inc Overview" and one bullet in the placeholders.

**P2:** View > Slide Master. Select the top (largest) parent master thumbnail. Click the title placeholder, set font 36 pt bold (Home tab while in master view). Drag the body placeholder rightward. Slide Master tab > Close Master View. Check a normal slide to confirm inherited formatting.

**P3:** View > Slide Master. Right-click the "Title and Content" layout thumbnail > Duplicate Layout. Right-click the duplicate > Rename Layout > "YourCompany Report". Insert > Text Box > type "CONFIDENTIAL", position near the bottom. Close Master View. On a slide: Home > Layout > "YourCompany Report".

**P4:** Design > Format Background > Solid fill > pick dark blue. Use "Apply to All" only if you want every slide filled. On the target slide, drag the title placeholder somewhere off-center. Click Home > Reset and the title returns to the layout position.

**P5:** File > Save As > choose "PowerPoint Template (.potx)" > name "YourCompany-Template" > save (it lands in the Custom Office Templates folder). Close. File > New > Personal/Custom > YourCompany-Template. In the new deck, confirm the theme, the "YourCompany Report" layout (Home > Layout), and the background. The .potx on disk is unchanged.


## FILE: quizzes/quiz-03-visual-design.md

# Quiz 03: Visual Design Principles and Tools

**Module tested:** Module 3 (PowerPoint Zero to Hero) - CRAP principles, assertion-evidence, typography, color 60-30-10, contrast, merge shapes, icons/SVG, image cropping/compressing/no-stretch, SmartArt, alignment tools

## Instructions

- Answer all 15 multiple-choice questions in Section A (3 points each).
- Complete all 5 practical challenges in Section B in PowerPoint (5 points each).
- Total: 70 points. Time limit: 30 minutes recommended.
- No notes or help files during the quiz. Work in a blank presentation unless a question says otherwise.
- All company data used in questions is fictional (YourCompany Inc).

## Scoring

| Score | Percentage | Result |
|---|---|---|
| 63-70 pts | 90%+ | Advance to the next module |
| 49-62 pts | 70-89% | Review your weak areas, then move on |
| Below 49 pts | Below 70% | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 questions, 3 points each = 45 points)

**1. (Easy)** CRAP is a four-letter checklist for visual design. What does it stand for?

- A) Contrast, Repetition, Alignment, Proximity
- B) Color, Rhythm, Animation, Position
- C) Contrast, Ratio, Accent, Padding
- D) Clarity, Repetition, Arrangement, Proportion

**2. (Easy)** Which principle says related items should be grouped closely together, with more space between unrelated groups?

- A) Contrast
- B) Proximity
- C) Alignment
- D) Repetition

**3. (Easy)** The assertion-evidence slide structure recommends which pairing?

- A) A long paragraph heading with a small icon
- B) A full-sentence assertion as the headline (the takeaway claim) with supporting visual evidence (chart, image, diagram) below it
- C) A one-word title with five bullet points
- D) A decorative background with centered WordArt

**4. (Easy)** The 60-30-10 rule for color suggests roughly:

- A) 60% accent, 30% secondary, 10% background
- B) 60% dominant/background color, 30% secondary color, 10% accent color for emphasis
- C) Three colors in equal thirds
- D) Six colors, three colors, one color

**5. (Easy)** Why should you avoid stretching images to make them fit a placeholder?

- A) It makes the file too big
- B) Distorting the aspect ratio warps faces and logos and looks unprofessional; crop instead to keep proportions true
- C) Stretched images cannot be animated
- D) PowerPoint forbids stretching

**6. (Easy)** Where are the Align tools (Align Left, Align Middle, Distribute Horizontally, etc.) found?

- A) Home tab, Paragraph group
- B) Shape Format (or Picture Format) tab, Align dropdown
- C) Insert tab
- D) Review tab

**7. (Medium)** On a light background, a colleague uses light gray text and thin hairline rules. Which CRAP problem is this?

- A) Poor proximity
- B) Insufficient contrast: text and lines do not stand out from the background and will be unreadable at the back of the room
- C) Misalignment
- D) Overuse of repetition

**8. (Medium)** You have five equal partner logos to show for YourCompany Inc. What is the best use of Proximity and Alignment together?

- A) Scatter them at random positions for visual interest
- B) Group the logos together in one zone with even spacing (Distribute) and a shared baseline or centerline (Align)
- C) Stack them all in the corner
- D) Place each one in a separate corner of the slide

**9. (Medium)** What is the main typography guidance for slide body text in a projected presentation?

- A) Use as many fonts as possible for variety
- B) Limit yourself to one or two typefaces with clear hierarchy (a heading face and a body face) and keep body text large enough to read from the back of the room
- C) Use 8 pt text to fit more content
- D) Use script fonts for all body copy

**10. (Medium)** You want to build a custom icon shape in PowerPoint by cutting one shape out of another (for example, a ring with a notch). Which feature does this?

- A) Merge Shapes (Union, Combine, Fragment, Intersect, Subtract)
- B) Group
- C) Align
- D) Crop to Shape

**11. (Medium)** Why are SVG icons especially useful on slides?

- A) They are always animated
- B) They are vector graphics, so they scale from a tiny label to a full-slide graphic with no pixelation, and they can be converted to shapes and recolored
- C) They only work in black and white
- D) They cannot be resized

**12. (Medium)** A photo you pasted into the YourCompany Inc deck is 5 MB and the file must be emailed. What is the correct fix?

- A) Crop it on the slide and use Picture Format > Compress Pictures (with "Delete cropped areas" checked) to shrink it
- B) Scale it down with the corner handle and call it done
- C) Screenshot it and paste the screenshot
- D) Convert the whole deck to a video

**13. (Hard)** Your slide must show a 3-step process: Intake, Review, Approval. What is the strongest choice?

- A) A paragraph explaining the three steps
- B) SmartArt (for example, a Basic Chevron Process or similar process layout) so the sequence reads left to right with consistent shapes
- C) Three unrelated clip art images
- D) A pie chart

**14. (Hard)** Two objects overlap and you want the top one to visually pass through a hole in the bottom one. Which Merge Shapes operation cuts the top shape's outline out of the bottom shape?

- A) Union
- B) Combine
- C) Subtract (with the shapes in the correct selection order)
- D) Fragment

**15. (Hard)** In assertion-evidence style, what is wrong with a slide titled "Q3 Revenue" that shows a bar chart of three regions?

- A) Nothing
- B) The title is a topic label, not an assertion; it should state the takeaway claim, such as "Q3 Revenue Grew 18% on Strong West Region Sales", with the chart as evidence
- C) The chart should be a table
- D) The title should be in all caps

---

## Section B: Practical Challenges (5 challenges, 5 points each = 25 points)

Perform each task in PowerPoint. Success criteria describe what a correct result looks like.

**P1. Apply CRAP to a messy slide.** Build a slide with 4 short text blocks ("Quality", "Speed", "Support", "Price") for YourCompany Inc, initially scattered at random positions. Then fix the layout using Align and Distribute so the four blocks sit in a single row with equal gaps and a shared vertical center.
*Success criteria:* Four separate text blocks end up evenly distributed horizontally and vertically centered relative to each other, using the Align tools (not eyeballed placement).

**P2. Assertion-evidence rewrite.** Create a slide with the topic title "Customer Satisfaction" and 4 bullets of raw survey notes. Replace the topic title with a full-sentence assertion summarizing the finding ("Customer Satisfaction Rose to 92% After Support Reorg"), and reduce the body to one short supporting line or a single simple visual (for example, a large "92%" figure or a small chart).
*Success criteria:* Title is a complete claim sentence; body is one line or one visual, not the original 4 bullets.

**P3. Typography and hierarchy.** On one slide, create a heading and two body items for YourCompany Inc. Use exactly two fonts (for example, a display face for the heading, a plain face for the body) and set a clear size hierarchy (heading noticeably larger than body, body at a readable projected size, roughly 18 pt or larger).
*Success criteria:* Only two typefaces are used across the slide; heading and body sizes differ clearly; body text is at a readable size.

**P4. Color 60-30-10.** Design a simple slide with a dominant background area (60%), one secondary color block (30%), and one small accent element (10%) such as a highlighted callout or underline. Use three colors only.
*Success criteria:* Three colors total; the visual weight roughly matches 60-30-10 (large background, medium secondary, small accent); the accent is used just once or twice for emphasis.

**P5. Image discipline and shapes.** Insert any photo and a rectangle shape on one slide. (a) Crop the photo to a square using Crop (do not stretch it). (b) Use Compress Pictures with "Delete cropped areas of pictures" checked to reduce its size. (c) Use Merge Shapes > Subtract (correct selection order) to punch the square photo's shape out of the rectangle, or use Merge Shapes > Fragment to build a two-piece graphic. Report which merge operation you used.
*Success criteria:* Photo is cropped, not distorted (aspect ratio preserved via crop); compression was applied with cropped areas deleted; at least one Merge Shapes operation visibly altered the rectangle.

---

---

# ANSWER KEY (spoilers below)

**Section A**

1. **A** - CRAP = Contrast, Repetition, Alignment, Proximity.
2. **B** - Proximity groups related content and separates it from unrelated content.
3. **B** - Assertion-evidence pairs a claim-sentence headline with visual evidence beneath it.
4. **B** - 60% dominant (often background), 30% secondary, 10% accent for draws of attention.
5. **B** - Stretching distorts the aspect ratio and looks amateur; crop to fit instead.
6. **B** - Align and Distribute live under the Shape Format / Picture Format contextual tab's Align dropdown.
7. **B** - Light-on-light is a contrast failure; text must stand out from its background.
8. **B** - Group the logos in one zone (proximity) and align/distribute them for an even, ordered row.
9. **B** - One or two typefaces, clear hierarchy, readable projected sizes.
10. **A** - Merge Shapes combines or subtracts shapes to build custom geometry.
11. **B** - SVG is vector, so it scales losslessly and can be converted to shapes for recoloring.
12. **A** - Crop what you do not show, then Compress Pictures and delete cropped areas to shrink embedded image data.
13. **B** - SmartArt process layouts (like chevrons) encode sequence visually and consistently.
14. **C** - Subtract removes the second-selected shape's area from the first, effectively punching it out (selection order matters).
15. **B** - A topic label states no takeaway; assertion-evidence demands a claim title with the chart as proof.

**Section B - model solutions**

**P1:** Insert four text boxes with the four labels. Select all four (Shift+click). Shape Format > Align > Align Middle (shared vertical center), then Align > Distribute Horizontally (equal gaps). Optionally Align Center relative to the slide for final placement.

**P2:** Open the slide. Replace the title text with the claim sentence ("Customer Satisfaction Rose to 92% After Support Reorg"). Delete the four bullets. Insert one support element: a text box with a single line ("+6 pts vs Q2"), or Insert > Chart with one simple series, or a large "92%" text figure. Keep the rest of the slide area clean.

**P3:** Insert a text box heading (pick font A, e.g., 32-40 pt) and two body text boxes or bullets (font B, e.g., 20 pt). Change fonts from the Home tab font dropdown so only the two chosen faces appear. Confirm via selecting each element that the font names match the two-font limit.

**P4:** Insert a large rectangle covering the slide as the background (fill color 1 = dominant). Add a medium rectangle as a content zone (fill color 2 = secondary). Add a small element like a short thick underline or a small badge (fill color 3 = accent) used once or twice. Check the balance visually: big, medium, tiny.

**P5:** (a) Select photo > Picture Format > Crop > Crop to Shape: Square, or drag crop handles to a square while keeping proportions (use the corner handle or hold Shift where appropriate). (b) Picture Format > Compress Pictures > check "Delete cropped areas of pictures" > OK. (c) Insert a rectangle and place it so the photo shape overlaps it. Select the rectangle first, then the photo/shape. Shape Format > Merge Shapes > Subtract (cuts the second shape out of the first). Alternative: select both and use Fragment to split into pieces and delete or recolor one. State which operation you used.


## FILE: quizzes/quiz-04-tables-charts.md

# Quiz 4: Tables, Charts & Data Visualization

**Module tested:** Module 4 - Tables, Charts & Data Visualization
**Total points:** 70
**Time limit:** 25 minutes

## Instructions

1. Section A has 15 multiple-choice questions, 3 points each (45 points total). Choose the single best answer (A-D).
2. Section B has 5 practical challenges, 5 points each (25 points total). Perform each task in PowerPoint and check yourself against the success criteria.
3. Answer from what you learned in Module 4. Do not peek at the answer key until you have finished both sections.
4. Every scenario uses fictional data for YourCompany Inc only.

## Scoring

| Score | Points | Result |
|-------|--------|--------|
| 90% and above | 63-70 pts | Advance to the next module |
| 70-89% | 49-62 pts | Review your weak areas, then continue |
| Below 70% | Below 49 pts | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 x 3 = 45 points)

**1. (Easy)** You are building a quarterly review deck for YourCompany Inc and need one chart that shows how the total annual revenue is split across four product lines. Which chart type is the most direct fit?

A. Line chart
B. Pie chart
C. Scatter plot
D. Gantt chart

**2. (Easy)** You are presenting monthly order volumes for YourCompany Inc across all 12 months of the year, and the point is to show the upward or downward trend. Which chart best communicates this?

A. Pie chart
B. Line chart
C. Clustered column chart
D. Radar chart

**3. (Easy)** You already inserted a column chart on a slide, and finance sends corrected Q2 numbers. Where do you change the values behind the chart?

A. Type the new numbers directly into the chart bars
B. Right-click the chart and choose Edit Data
C. Delete the chart and start over
D. Use the Transitions tab

**4. (Easy)** You need a clean grid of 6 product names with their prices and stock counts on a single slide. What is the correct first step?

A. Insert tab, then Table, then choose the row and column count
B. Insert tab, then Chart, then choose Table
C. Home tab, then New Slide, then Table Layout
D. Design tab, then Variants, then Grid

**5. (Easy)** The Module 4 term "chart junk" refers to which of the following?

A. A corrupted chart file
B. Excessive decorative elements that add no information, such as heavy gridlines, 3D effects, or pointless icons
C. Any chart created with the default theme
D. Data points that are missing values

**6. (Easy)** What is the main structural difference between a clustered column chart and a clustered bar chart?

A. Column charts plot categories vertically as up-down bars; bar charts plot categories horizontally as left-right bars
B. Column charts can show two data series; bar charts can show only one
C. Column charts are for percentages; bar charts are for currency
D. There is no difference, they are the same chart

**7. (Medium)** You link a PowerPoint chart to an Excel workbook at C:\Data\YourCompany-forecast.xlsx. A colleague later updates that workbook with new figures. What happens to your chart when you next open the presentation on the same PC?

A. Nothing, charts never change after creation
B. The chart can refresh and pull the updated values from the workbook
C. The chart deletes itself
D. PowerPoint converts the chart to a picture

**8. (Medium)** You are analyzing whether advertising spend is related to weekly sales at YourCompany Inc. You have two numeric columns, spend and sales, for 30 weeks. Which chart is designed for this?

A. Pie chart
B. Stacked area chart
C. Scatter (XY) chart
D. Doughnut chart

**9. (Medium)** A manager wants a tiny 2% dip in YourCompany Inc revenue to look dramatic on a slide, and suggests starting the vertical axis at 95% of the values. What is the main ethical problem with this?

A. PowerPoint does not support axis editing
B. It visually exaggerates the change and can mislead the audience about the real size of the difference
C. It makes the file too large
D. It breaks the link to Excel

**10. (Medium)** You insert a 5-row, 4-column table and want it to be readable from the back of a room. Which combination follows good table design from Module 4?

A. Tiny 10 pt text, no header, rainbow cell fills
B. A clear header row, banded (alternating) row shading, and font large enough to read at distance
C. Borders on every cell in heavy black, no header
D. White text on pale yellow fills

**11. (Medium)** You must show a 5-stage approval process at YourCompany Inc (Draft, Review, Approve, Publish, Archive) as a single visual on one slide. Which approach best matches the Module 4 infographic guidance?

A. A pie chart with five slices
B. A horizontal chevron or arrow flow (or a process SmartArt) that reads left to right
C. A scatter plot with five points
D. Five separate tables stacked vertically

**12. (Medium)** Your Excel source has 12 columns but you want the chart to show only 3 of the data series. What do you do?

A. Delete the other 9 columns from the workbook permanently
B. In Edit Data, adjust the data range or clear the check marks for the series you do not want plotted
C. Cover the extra bars with white boxes
D. Change the chart to a pie chart

**13. (Hard)** You are distributing the final YourCompany Inc deck to people who will edit it on laptops that do not have the original Excel workbook. What is the key trade-off between linked and embedded chart data?

A. Linked data keeps the file smaller and updates from the source, but breaks if the source is missing; embedded data travels inside the presentation and works anywhere, but does not auto-update and grows the file
B. Linked data is more accurate than embedded data
C. Embedded data requires an internet connection to display
D. Linked data prints better than embedded data

**14. (Hard)** You must plot monthly revenue in dollars and profit margin in percent on the same chart, with very different magnitudes. Which is the sound solution?

A. Plot both on the primary axis and hope the lines cross
B. Use a combo chart with a secondary value axis for the percent series, and label both axes clearly
C. Shrink the percent numbers by 1000 and add a footnote
D. Use two 3D pie charts side by side

**15. (Hard)** Which of the following is the strongest example of ethical data display for a YourCompany Inc results slide?

A. A 3D pie chart with the largest slice exploded toward the audience
B. A zero-baseline column chart with direct value labels and the time period stated in the subtitle
C. A chart whose vertical axis is inverted to make growth look positive
D. A chart with the legend hidden and colors chosen to hide the worst-performing product

---

## Section B: Practical Challenges (5 x 5 = 25 points)

**1. Build a formatted table.**
On a blank slide, insert a 5-row by 4-column table listing 4 YourCompany Inc products with columns: Product, Q1 Units, Q2 Units, Q3 Units. Format it with a header row, banded rows, and 18 pt or larger body text.
*Success criteria:* 5x4 table exists, header row is visually distinct, rows alternate shading, all body text is 18 pt or larger.

**2. Create and update a chart.**
Using the table from Challenge 1, insert a clustered column chart showing Q1-Q3 units per product. Then use Edit Data to add a Q4 column of numbers and confirm the chart gains the new data.
*Success criteria:* Chart type is clustered column, one category per product, three or four series visible, and editing the data sheet visibly changes the chart.

**3. Link chart data to Excel.**
Create a chart whose data is linked to an external Excel workbook you saved as YourCompany-forecast.xlsx. Change one value in the workbook and verify the chart can show the update.
*Success criteria:* Chart is created from the external workbook (link, not just copy-pasted picture), and updating the workbook value updates the chart after a refresh or reopen.

**4. De-junk a chart.**
Insert a default chart, then clean it: remove heavy gridlines and any 3D or shadow effects, add direct value labels or a clean legend, and give it a plain title stating what the audience should see.
*Success criteria:* No 3D or shadow effects remain, gridlines are gone or minimal, values are readable without hunting, and the title states the message.

**5. Fix a misleading chart.**
Build a column chart for YourCompany Inc monthly revenue where the value axis starts above zero (for example starting at 90% of your smallest value), so the differences look huge. Then correct it so the display is honest.
*Success criteria:* The corrected chart starts the value axis at zero, the exaggerated impression is gone, and any broken axis case is clearly marked or avoided.

---

# ANSWER KEY

**STOP. SPOILERS BELOW.** Only read on after you have answered Sections A and B.

## Section A Answers

1. **B** - A pie chart directly shows parts of a whole for a single total. Four product lines of one quarter's revenue is a classic single-whole split, which is the one case a pie handles well.
2. **B** - A line chart is built for change over continuous time, and 12 monthly points with a trend is exactly its use case.
3. **B** - Right-click the chart and choose Edit Data (or Edit Data in Chart Design) opens the data sheet where you can change the values the chart is plotted from.
4. **A** - Tables are inserted from Insert > Table, where you pick the grid size first and fill in the content after.
5. **B** - Chart junk is any decoration that carries no data meaning: heavy gridlines, gratuitous 3D, clip-art icons, and similar clutter that lowers the data-to-ink ratio.
6. **A** - The difference is category orientation: column charts run categories left to right with vertical bars, bar charts run categories top to bottom with horizontal bars (also better for long category names).
7. **B** - With linked data, PowerPoint stores a connection to the workbook and can pull updated values when the link refreshes or the file reopens on the same PC.
8. **C** - A scatter (XY) chart is the standard tool for showing the relationship between two numeric variables across many observations.
9. **B** - Cutting the axis to a narrow band around the data magnifies small differences visually and misleads the audience about the true scale of the change. Ethical practice is a zero baseline for bar and column charts.
10. **B** - Readable tables use a distinct header, banded rows to guide the eye, restrained borders, and type sized for the room.
11. **B** - A left-to-right chevron or process graphic matches the "5-stage process" infographic pattern from Module 4. Pie and scatter charts cannot show sequence.
12. **B** - Edit Data exposes the plotted data range and series selection, so you can restrict the chart to the columns you want without damaging the workbook.
13. **A** - Linked data is small and live but depends on the source file path and presence; embedded data is self-contained and portable but static unless manually updated, and it adds to file size.
14. **B** - A combo chart with a secondary axis lets dollars and percent each use their own scale, with both axes labeled so nobody misreads the magnitudes.
15. **B** - Zero baseline, direct labels, and a stated time period are the core of honest chart display. Exploded 3D pies, inverted axes, and manipulative color all distort perception.

## Section B Model Solutions

**1. Formatted table**
1. Insert > Table > 5 columns is wrong; choose 4 columns and 5 rows.
2. Type the header row (Product, Q1 Units, Q2 Units, Q3 Units) and 4 product rows (for example Aurora, Beacon, Cascade, Dune).
3. Select the table, use Table Design: tick Header Row and Banded Rows, pick a restrained table style.
4. Select all cells and set font size to 18 pt or larger.

**2. Create and update a chart**
1. Select the table (or the data range), Insert > Chart > Clustered Column.
2. The data sheet opens with the table values; each product becomes a category, each quarter a series.
3. Add a Q4 column of numbers in the sheet; the chart picks up the new series.
4. Close the sheet; re-open with Edit Data any time to revise.

**3. Link chart data to Excel**
1. Create and save YourCompany-forecast.xlsx with sample rows of data.
2. In Excel, copy the data range. In PowerPoint use Home > Paste > Paste Special > Paste Link > Microsoft Excel Worksheet Object (or insert the chart from the workbook so a link is created).
3. Change one value in the workbook and save.
4. In PowerPoint, update links (right-click the object > Update Link, or reopen the file) and confirm the chart reflects the new value.

**4. De-junk a chart**
1. Select the chart and delete the horizontal gridlines (click each set of gridlines and press Delete).
2. Chart Design > Add Chart Element > Effects: remove any 3D, shadow, or bevel formatting; use flat fills.
3. Add Data Labels (Chart Element > Data Labels) or keep one simple legend.
4. Replace the generic title with a takeaway title, for example "Q3 Units Grew Across All Four Products".

**5. Fix a misleading chart**
1. Build a column chart of 12 monthly revenue values for YourCompany Inc.
2. Right-click the value axis > Format Axis > Bounds: set Minimum to a value near 90% of the smallest data point and observe how the columns appear to leap around.
3. Correct it: set the Minimum bound back to 0 (auto).
4. Confirm the visual differences now match the true proportions of the numbers, and never use a non-zero baseline on bars or columns without an explicit broken-axis marker.


## FILE: quizzes/quiz-05-transitions-animations.md

# Quiz 5: Transitions & Animations

**Module tested:** Module 5 - Transitions & Animations
**Total points:** 70
**Time limit:** 25 minutes

## Instructions

1. Section A has 15 multiple-choice questions, 3 points each (45 points total). Choose the single best answer (A-D).
2. Section B has 5 practical challenges, 5 points each (25 points total). Perform each task in PowerPoint and check yourself against the success criteria.
3. Answer from what you learned in Module 5. Do not peek at the answer key until you have finished both sections.
4. Every scenario uses fictional data for YourCompany Inc only.

## Scoring

| Score | Points | Result |
|-------|--------|--------|
| 90% and above | 63-70 pts | Advance to the next module |
| 70-89% | 49-62 pts | Review your weak areas, then continue |
| Below 70% | Below 49 pts | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 x 3 = 45 points)

**1. (Easy)** In a YourCompany Inc all-hands deck, what is the core difference between a transition and an animation?

A. A transition plays between slides; an animation plays on an object on a slide
B. A transition plays on objects; an animation plays between slides
C. They are two words for the same feature
D. Transitions are for video; animations are for audio

**2. (Easy)** Where do you find the gallery of slide-to-slide effects such as Fade and Push?

A. The Animations tab
B. The Transitions tab
C. The Insert tab
D. The Review tab

**3. (Easy)** You set a bullet point's start option to "After Previous". When will it play?

A. When you click the mouse or press a key
B. Immediately after the previous animation in the sequence finishes
C. At the same time as the previous animation
D. Only when you right-click it in Slide Show view

**4. (Easy)** Which pane shows the full list and order of every animation on the current slide?

A. The Selection Pane
B. The Animation Pane
C. The Slide Sorter
D. The Notes Pane

**5. (Easy)** What does the Morph transition do?

A. Deletes duplicate objects between slides
B. Smoothly animates matching objects from their position, size, or rotation on one slide to their state on the next
C. Converts shapes into pictures
D. Applies a random effect to each slide

**6. (Easy)** Which of the following best describes Module 5's "animation restraint" rule for business decks?

A. Every bullet should get a different effect so the audience stays awake
B. Use motion sparingly and consistently: one effect family, short durations, and only where motion adds meaning
C. Animations should always run 3 seconds or longer
D. Star and bounce effects are required on title slides

**7. (Medium)** You want a Morph "zoom in" where one small product image grows to fill the next slide. What is the correct setup?

A. Put the image only on the first slide and apply Morph to the second slide
B. Duplicate the slide, then on the second slide enlarge and reposition the same object, and apply Morph to the second slide
C. Insert the image twice with different names and apply Random Bars
D. Use Grow/Shrink on the first slide and Morph on the third

**8. (Medium)** You want a hint box to appear only when the presenter clicks a specific "Show answer" button on the slide. Which feature does this?

A. After Previous
B. A trigger animation tied to the button object
C. The transition's Apply To All
D. A custom show

**9. (Medium)** What is the difference between an animation's Duration and its Delay?

A. Duration is how long the effect takes to play; Delay is the wait between the animation's scheduled start and when it actually begins
B. Duration is the wait before starting; Delay is how long it plays
C. They are the same setting
D. Duration applies to transitions only; Delay applies to animations only

**10. (Medium)** Your chart has four quarterly series and you want each quarter to appear one click at a time during the commentary. What do you set?

A. Animate the chart with Effect Options set to a chart build such as By Series or By Category, with each step starting On Click
B. Insert four separate pictures of the chart
C. Apply the Morph transition four times
D. Set the whole chart to Play From Previous

**11. (Medium)** In the Animation Pane, the icons for animation 2 and 3 are stacked at the same vertical position with a "with previous" marker. What does this tell you?

A. Animations 2 and 3 play simultaneously with animation 1
B. Animations 2 and 3 are errors and will not play
C. Animations 2 and 3 play in reverse order
D. Animations 2 and 3 only play in Reading View

**12. (Medium)** You are projecting a formal results deck for YourCompany Inc in a large venue with a weak projector. Which animation and transition choices are safest?

A. Bounce on every bullet and a Checkerboard transition on every slide
B. Simple effects like Fade or Appear with short durations, and one understated transition used consistently
C. Fly In from all four directions to use the screen
D. No animations at all ever, in any deck

**13. (Hard)** You duplicated a slide for Morph, but on the second slide you replaced the logo with a brand-new copy of the same file. Morph now fades instead of moving it. Why, and what is the fix?

A. Morph only works on text; convert the logo to text
B. Morph matches objects by identity, not appearance; fix it by keeping the same object (duplicate the slide rather than re-inserting) or by giving both objects the same name in the Selection Pane
C. The transition duration is too short; set it to 10 seconds
D. Morph requires both slides to have different layouts

**14. (Hard)** You are building a self-running kiosk loop for a YourCompany Inc booth, and one slide must play entirely hands-free: three bullets then a chart build, roughly 15 seconds total. Which combination works?

A. All animations On Click and a manual presenter
B. Set the sequence to After Previous with set Durations and Delays that sum to about 15 seconds, plus a slide transition advance time
C. All animations With Previous with default 0.5 second timing and click-to-advance
D. Put the 15 seconds of content in the speaker notes

**15. (Hard)** Which statement about combining triggers and chart builds is correct?

A. Chart builds cannot have triggers; only text can
B. A trigger can start a chart build step when a specific object is clicked, letting you reveal a series only when you click its legend swatch or a custom button
C. Triggers only work in Reading View
D. A chart can have only one trigger and it must be the whole chart

---

## Section B: Practical Challenges (5 x 5 = 25 points)

**1. Build a Morph demonstration.**
Create two slides where the same rounded rectangle starts small in the corner on slide 1 and is large and centered on slide 2, connected by a Morph transition that visibly moves and grows it.
*Success criteria:* The rectangle is the same object carried across both slides (duplicate-slide method or matched names), Morph is applied to slide 2, and in Slide Show view it glides and grows rather than fading.

**2. Animate a bullet list step by step.**
On one slide, add a 4-line bullet list about YourCompany Inc quarterly wins. Make each line appear one at a time, fading in, first line On Click, the rest After Previous at about 1 second each.
*Success criteria:* 4 separate animations visible in the Animation Pane in the correct order, first is On Click, the other three are After Previous with roughly 1s duration.

**3. Build a chart by series.**
Insert a clustered column chart with 3 series and animate it so the series appear one per click using a chart build, with the legend included in the animation.
*Success criteria:* Effect Options for the chart animation shows a build step (By Series or By Category), each step advances On Click, and the legend participates in the build.

**4. Create a trigger interaction.**
Put a button labeled "Show answer" and a hidden text box with a short answer on a quiz slide. Configure the text box to appear only when the "Show answer" button is clicked.
*Success criteria:* The text box has an animation whose Trigger settings reference the button object, and clicking the button in Slide Show reveals the text while clicking elsewhere does not.

**5. Time an auto-advancing sequence.**
Make a single slide's content run hands-free in about 15 seconds: title first, three body lines after, each with sensible durations and delays, and the slide set to advance automatically after the animations complete.
*Success criteria:* No animation requires a click (all With Previous or After Previous), total runtime is close to 15 seconds, and the slide auto-advances via the Transitions timing options.

---

# ANSWER KEY

**STOP. SPOILERS BELOW.** Only read on after you have answered Sections A and B.

## Section A Answers

1. **A** - Transitions govern how one slide replaces another; animations govern how objects appear, move, or disappear within a single slide.
2. **B** - Slide-to-slide effects live on the Transitions tab, while object effects live on the Animations tab.
3. **B** - "After Previous" chains an animation to run right after the animation before it in the sequence ends, no click required.
4. **B** - The Animation Pane lists every animation on the slide in play order and shows their start modes and timings.
5. **B** - Morph tweens matched objects between two slides, animating position, size, rotation, and color changes smoothly.
6. **B** - Restraint means motion is used deliberately and consistently, not decoratively. One effect family, brief durations, and meaning-driven use.
7. **B** - Morph needs the same object in two different states on two adjacent slides. Duplicate the slide, resize the object on the copy, and apply Morph to the second slide.
8. **B** - A trigger binds an animation to a click on a specific object, so the hint box plays only when that particular button is clicked.
9. **A** - Duration is the length of the effect itself; Delay is the pause between when the animation is scheduled to start and when it actually begins.
10. **A** - Chart animations support build steps through Effect Options, so you can reveal by series or category one click at a time without faking it with pictures.
11. **A** - Icons stacked under animation 1 with the "with previous" marker indicate those animations run at the same time as animation 1 rather than after one another.
12. **B** - Understated effects and one consistent transition protect legibility and credibility. Restraint does not mean zero motion, it means purposeful motion.
13. **B** - Morph keys off object identity, not pixels. Duplicating the slide keeps the same object, or matching names in the Selection Pane pairs new copies.
14. **B** - Fully unattended playback needs all animations on With/After Previous plus explicit durations and delays, and the slide must advance on a timer set in Transitions.
15. **B** - Triggers can fire chart build steps from any object click, which enables click-to-reveal storytelling tied to a custom control.

## Section B Model Solutions

**1. Morph demonstration**
1. On slide 1, insert a rounded rectangle (Insert > Shapes), size it small and place it in a corner. Give it a name in the Selection Pane (Home > Select > Selection Pane), for example "HeroBox".
2. Right-click the slide 1 thumbnail > Duplicate Slide.
3. On slide 2, drag the same rectangle to the center and resize it large.
4. With slide 2 selected: Transitions > Morph, set Duration to about 1.0-1.5 s. Run Slide Show to confirm it glides and grows.

**2. Animate a bullet list step by step**
1. Insert a text box with 4 bullets (for example: "Revenue up 12%", "Two new regions opened", "Churn down to 4%", "Launched Aurora v2").
2. Select the text box, Animations > Fade.
3. Open the Effect Options dialog > Text Animation tab: set Group text to "By 1st Level Paragraphs" and uncheck "Automatically after" if present.
4. In the Animation Pane, set the first item to On Click and items 2-4 to After Previous (Animation Pane dropdown > Start > After Previous), each with Duration 1.0 s.

**3. Build a chart by series**
1. Insert a clustered column chart with 3 series and 4 categories (YourCompany Inc quarterly units).
2. Select the chart, Animations > Appear or Fade.
3. In the Animation Pane, open Effect Options > Chart Animation tab: set Group Chart to By Series (tick "Start animation by drawing the chart background" if you want the axes first).
4. Set each build step to On Click. Verify the legend animates in with the series.

**4. Create a trigger interaction**
1. Add a rounded rectangle labeled "Show answer" and a separate text box containing the answer, for example "Q3 margin rose to 28%".
2. Apply an entrance effect (Appear or Fade) to the answer text box.
3. In the Animation Pane, open Effect Options > Timing > Triggers > On click of > choose the "Show answer" button shape.
4. Test in Slide Show: clicking the button reveals the answer; clicking anywhere else does nothing.

**5. Time an auto-advancing sequence**
1. Animate the title (With Previous, Duration 0.5 s, Delay 0 s), then three body lines (After Previous, Duration 1.0 s each, Delays 1-2 s between) so the sum is about 15 s including an opening pause.
2. Confirm in the Animation Pane that no item says "On Click".
3. Transitions tab: set After to 15 s (or a little more than the animation total) and uncheck On Mouse Click.
4. Press F5 and confirm the slide runs itself and hands over to the next slide without input.


## FILE: quizzes/quiz-06-media-interactivity.md

# Quiz 6: Media & Interactivity

**Module tested:** Module 6 - Media & Interactivity
**Total points:** 70
**Time limit:** 25 minutes

## Instructions

1. Section A has 15 multiple-choice questions, 3 points each (45 points total). Choose the single best answer (A-D).
2. Section B has 5 practical challenges, 5 points each (25 points total). Perform each task in PowerPoint and check yourself against the success criteria.
3. Answer from what you learned in Module 6. Do not peek at the answer key until you have finished both sections.
4. Every scenario uses fictional data for YourCompany Inc only.

## Scoring

| Score | Points | Result |
|-------|--------|--------|
| 90% and above | 63-70 pts | Advance to the next module |
| 70-89% | 49-62 pts | Review your weak areas, then continue |
| Below 70% | Below 49 pts | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 x 3 = 45 points)

**1. (Easy)** You want a recorded product demo video to play from inside a YourCompany Inc slide. What is the standard route?

A. Insert tab > Video > Video on My PC, then pick the video file
B. Insert tab > Screenshot, then browse for the video file
C. Home tab > New Slide > Video Layout
D. Design tab > Background > Video

**2. (Easy)** The demo video is 3 minutes long but only the middle 40 seconds matter. Which tool do you use?

A. Crop
B. Trim Video on the Playback tab
C. Compress Media
D. The Animation Painter

**3. (Easy)** You want a video to begin playing the moment its slide appears, with no click. Where do you set this?

A. Transitions tab > Advance Slide
B. Playback tab > Start > Automatically
C. Insert tab > Action
D. File > Options > Advanced

**4. (Easy)** You want the words "See the full report" on a slide to open the YourCompany Inc intranet page during the show. What do you use?

A. A hyperlink on the text
B. A slide transition
C. A comment
D. A speaker note

**5. (Easy)** What does PowerPoint's screen recording feature let you do?

A. Record only audio narration
B. Record activity in another application or on the desktop and insert it as a video on the slide
C. Record who edits the presentation
D. Record a slide show as an audio podcast

**6. (Easy)** You added background music and a small speaker icon appears on the slide. During the show you want the icon invisible. What do you do?

A. Delete the audio after setting it to play
B. On the Playback tab, tick "Hide During Show"
C. Send the icon behind the slide background
D. Move the icon off the edge of the slide

**7. (Medium)** You want soft background music to continue across every slide of a 20-slide YourCompany Inc deck, looping if it runs out. Which settings do you combine?

A. Start: Automatically, Play Across Slides, and Loop Until Stopped on the Playback tab
B. Start: On Click and Trim to 5 seconds
C. Insert the same audio file on all 20 slides manually
D. Set the music as the slide transition sound only

**8. (Medium)** You want a rounded rectangle labeled "Agenda" to jump to slide 3 whenever a viewer clicks it in the show. What is the correct setup?

A. Format the rectangle with a theme color
B. Select the rectangle, Insert > Link > Place in This Document > slide 3 (or Insert > Action, mouse click, Hyperlink to, Slide 3)
C. Apply the Morph transition to the rectangle
D. Group the rectangle with slide 3's thumbnail

**9. (Medium)** Your deck has three sections (Sales, Product, Support) and you want an interactive menu that jumps to each section and returns to the menu afterward. Which feature is built for this?

A. Section Zoom with the return-to-zoom option
B. The Animation Pane
C. A custom show
D. Compress Media

**10. (Medium)** A sales manager presents to two audiences with the same deck file: a short 5-slide version for executives and the full 22-slide version for the team. Which feature lets both live in one file?

A. Custom shows
B. Hidden slides only
C. Trim Video
D. Action buttons

**11. (Medium)** You are setting up an unattended booth display that should loop a deck all day, blocking viewers from clicking into random slides. Which setting is the right one?

A. Reading View
B. Set Up Slide Show > "Browsed at a kiosk (full screen)", which loops continuously until Esc
C. Presenter View
D. Export to PDF

**12. (Medium)** What is the difference between Trim Video and Crop on a video object?

A. Trim removes unwanted time from the start or end of the clip; Crop removes unwanted areas of the picture frame
B. Trim changes the resolution; Crop changes the volume
C. They do the same thing
D. Trim works on audio; Crop works on video

**13. (Hard)** You must send a finished YourCompany Inc training deck to a client as a self-playing file with your narration and timings, viewable without PowerPoint. Which export fits?

A. Create PDF
B. Create a Video (MP4), which includes narrations, ink, and slide timings
C. Save as PPTX
D. Print handouts

**14. (Hard)** In a Section Zoom menu, a viewer clicks into the Product section, watches those slides, and then you want the show to return to the menu automatically after the section's last slide. What must be true?

A. The "Return to Zoom" option is enabled for that Section Zoom
B. The section slides must be hidden
C. The menu slide must use the Morph transition
D. The deck must be exported to video

**15. (Hard)** You are preparing a media-rich deck for an offline conference room. A 200 MB embedded video pushes the file over the USB transfer limit. What is the most sound approach?

A. Use Compress Media to reduce quality to a level the room can tolerate, and verify playback quality after
B. Delete the video and write a paragraph about it
C. Replace the video with a hyperlink to an online streaming page (the room is offline)
D. Split each video frame into pictures

---

## Section B: Practical Challenges (5 x 5 = 25 points)

**1. Insert, trim, and autoplay a video.**
Insert a video on a slide, cut roughly 5 seconds from the beginning using Trim Video, and configure it to start automatically and play full screen when its slide appears.
*Success criteria:* Video is embedded on the slide, its start point is trimmed (visible in the Trim dialog or playback bar), Start is set to Automatically, and "Full Screen" is ticked on the Playback tab.

**2. Looping background audio.**
Add an audio file to slide 1 and configure it as quiet background music across the whole YourCompany Inc deck, looping until stopped, with its icon hidden during the show and volume lowered.
*Success criteria:* Play Across Slides is enabled, Loop Until Stopped is ticked, Start is Automatically, volume is set to Low or Medium, and Hide During Show is ticked.

**3. Build an action-button menu.**
Create a menu slide with three labeled buttons (Sales, Product, Support) that jump to the matching slides, and add a "Menu" button on each of those three destination slides that returns to the menu slide.
*Success criteria:* Four distinct buttons total work as hyperlinks/actions and are clickable in Slide Show view, each landing on the correct slide in both directions.

**4. Create a Section Zoom.**
Organize a short deck into sections and insert a Summary or Section Zoom that navigates to one section, with "Return to Zoom" enabled so the show comes back to the zoom slide after the section ends.
*Success criteria:* Zoom object appears on the menu slide, clicking it in Slide Show enters the section, and the show returns to the menu slide after the section's last slide.

**5. Kiosk mode and export.**
Configure the deck to run unattended at a booth, looping continuously, and then export it as a video file that anyone can play without PowerPoint.
*Success criteria:* Set Up Slide Show uses "Browsed at a kiosk (full screen)" with loop until Esc, and File > Export > Create a Video produces an MP4 that plays in a standard media player.

---

# ANSWER KEY

**STOP. SPOILERS BELOW.** Only read on after you have answered Sections A and B.

## Section A Answers

1. **A** - Insert > Video > Video on My PC embeds (or links) a video file as an object on the slide that plays inside the deck.
2. **B** - Trim Video on the Playback tab sets new in and out points for the clip's playback without altering the original file.
3. **B** - The Playback tab's Start menu controls when a media object plays; "Automatically" starts it the moment the slide appears.
4. **A** - A hyperlink applied to text (Insert > Link) can open a web page during the show, which is the standard way to point at external resources.
5. **B** - Screen recording captures actions in another window or on the desktop and drops the result onto the current slide as a playable video.
6. **B** - "Hide During Show" on the Playback tab keeps the audio running while making its icon invisible in Slide Show view.
7. **A** - Play Across Slides carries the audio through the deck, Start Automatically removes the need to click, and Loop Until Stopped covers shows longer than the track.
8. **B** - Action buttons are ordinary shapes given a hyperlink or action setting (Insert > Action or Insert > Link) that fires on click during the show.
9. **A** - Zoom navigation is designed for click-to-section menus, and Section Zoom's return-to-zoom option brings the audience back to the menu slide automatically.
10. **A** - Custom shows store named subsets of slides inside one presentation file, so one deck can deliver two different running orders.
11. **B** - Kiosk mode ("Browsed at a kiosk") locks navigation to hyperlinks and actions only and loops the show until Esc is pressed, which is exactly what an unattended booth needs.
12. **A** - Trim edits the clip's timeline (in/out points); Crop edits the visible frame area of the video's picture.
13. **B** - Create a Video renders an MP4 that bakes in narrations, ink annotations, and recorded slide timings, and plays without PowerPoint.
14. **A** - With Return to Zoom enabled, the show jumps back to the zoom/menu slide once the section's slides have played, keeping the navigation loop intact.
15. **A** - Compress Media reduces embedded media size with a quality trade-off that should be checked on the venue's display. The other options break the offline, self-playing requirement.

## Section B Model Solutions

**1. Insert, trim, and autoplay a video**
1. Insert > Video > Video on My PC, choose your clip, and size it on the slide.
2. With the video selected: Playback tab > Trim Video. Set the Start point 5 seconds in (and adjust the End point if needed), then OK.
3. Playback tab: set Start to "Automatically" and tick "Full Screen".
4. Run Slide Show to confirm the trimmed clip begins on its own and fills the screen.

**2. Looping background audio**
1. Insert > Audio > Audio on My PC, pick the music file; PowerPoint places an icon on the slide.
2. Playback tab: set Start to "Automatically", tick "Play Across Slides" and "Loop Until Stopped", tick "Hide During Show", and set Volume to Low.
3. Optionally drag the icon to the slide margin or behind an object (it will be hidden in the show anyway).
4. Test by running the show across 2-3 slides and confirming the music never stops or restarts.

**3. Build an action-button menu**
1. On the menu slide, insert three rounded rectangles labeled Sales, Product, Support.
2. Select each: Insert > Link > Place in This Document > pick the matching slide (or Insert > Action > Mouse Click > Hyperlink to > Slide).
3. On the Sales, Product, and Support slides, add a smaller "Menu" rectangle with the link pointing back to the menu slide (copy-paste the button to keep it consistent).
4. Press F5 and click through every button in both directions to verify.

**4. Create a Section Zoom**
1. In Normal view, use the slide thumbnail right-click > Add Section to create named sections (for example, Sales, Product, Support).
2. On the menu slide: Insert > Zoom > Section Zoom (or Summary Zoom), tick the section you want, OK.
3. With the zoom object selected, tick "Return to Zoom" on the Zoom Tools/Zoom tab.
4. Run the show: click the zoom to enter the section, then let the section's slides finish and confirm you land back on the menu slide.

**5. Kiosk mode and export**
1. Slide Show > Set Up Slide Show > choose "Browsed at a kiosk (full screen)". This sets loop continuously until Esc and disables click-to-advance.
2. Confirm navigation still works through your action buttons and Zoom links.
3. File > Export > Create a Video, pick a resolution, and keep "Use Recorded Timings and Narrations" if present.
4. Save as MP4 and play it in a standard media player to verify the export.


## FILE: quizzes/quiz-07-delivery-workflow.md

# Quiz 7: Delivery and Workflow

**Module tested:** Module 7: Delivery and Workflow (speaker notes, Presenter View, Rehearse Timings, collaboration, accessibility, export, printing, protection, pre-flight)

**Instructions**

- Answer all 15 multiple-choice questions in Section A (3 points each) and complete the 5 practical challenges in Section B (5 points each).
- Time yourself: 45 minutes total. Work closed-book first; check the answer key only after scoring yourself.
- For Section B, actually perform each task in PowerPoint and verify every success criterion before marking it complete.
- All fictional data uses the company "YourCompany Inc".

**Scoring**

| Total points | Percentage | Result |
|---|---|---|
| 63-70 | 90%+ | Advance to the next module |
| 49-62 | 70-89% | Review your weak areas, then retake |
| Below 49 | Below 70% | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 questions, 3 points each = 45 points)

Difficulty legend: **E** = easy, **M** = medium, **H** = hard.

**1. (E)** Priya wants her speaker notes visible on her laptop screen while the audience sees only the slides on the projector. Which feature should she use?

- A) Reading View
- B) Presenter View
- C) Slide Sorter view
- D) The Notes Page layout

**2. (E)** Where do you type speaker notes in Normal view?

- A) The slide canvas in the text placeholder
- B) The Comments pane
- C) The Notes pane below the slide
- D) The Outline pane

**3. (E)** What does Rehearse Timings do?

- A) Records audio narration for every slide
- B) Records how long you spend on each slide and saves those durations as slide timings
- C) Sets a countdown timer the audience can see
- D) Locks the slide show to a fixed total length

**4. (E)** A colleague leaves feedback on one of your slides that appears as a small icon on the slide and in a side pane. What is this?

- A) A speaker note
- B) A comment
- C) A shape annotation
- D) A summary zoom

**5. (E)** Which file format preserves full editing fidelity, including VBA macros, when the presentation contains them?

- A) .pptx
- B) .pdf
- C) .pptm
- D) .ppsx

**6. (E)** What is alt text?

- A) Backup text stored with AutoRecover
- B) A text description of a picture, shape, or chart for people using screen readers
- C) The text shown in the slide footer
- D) An alternative font assigned in the theme

**7. (M)** Marcus is on stage and wants to jump to slide 12 without the audience seeing him scroll through slides 11 and 10. What should he do in Presenter View?

- A) Turn off the projector, navigate, then turn it back on
- B) Use the slide navigator grid to jump straight to slide 12
- C) Press Esc to end the show and restart on slide 12
- D) Drag the slide thumbnails on the audience screen

**8. (M)** Your team needs several people to edit the same cloud-hosted presentation at the same time. Which statement is correct?

- A) Only one person can open the file; others get read-only copies
- B) Co-authoring lets multiple people edit simultaneously, and their changes appear as they happen
- C) Each person must edit offline and then email the file back
- D) Co-authoring requires the file to be saved as .ppam

**9. (M)** After merging a colleague's copy of a presentation with yours, which feature lets you review every change slide by slide and accept or reject it?

- A) Compare & Merge
- B) Version History
- C) The Accessibility Checker
- D) Track Changes in the Notes pane

**10. (M)** What does the Accessibility Checker report?

- A) Font licensing problems
- B) Issues such as missing alt text, unclear reading order, and hard-to-read contrast that make the deck difficult for people with disabilities
- C) Slides that exceed the projector resolution
- D) Missing speaker notes

**11. (M)** Daniela must distribute a fixed, non-editable snapshot of her deck to 200 clients who may not have PowerPoint. What is the best export?

- A) Save as .pptx and email it
- B) Export as PDF
- C) Export as animated GIF
- D) Save as .ppam

**12. (M)** What is the main reason to export a self-running kiosk deck as an MP4 video?

- A) It makes the file size always smaller than the original
- B) It plays the recorded timings, narration, and animations consistently on any device without PowerPoint
- C) It adds speaker notes to the output
- D) It converts all shapes to accessible text

**13. (H)** Your deck uses fonts the venue's laptop does not have. Which combination best reduces pre-flight risk before presenting from that laptop?

- A) Embed the fonts when saving (File > Options > Save > Embed fonts in the file) and also export a PDF backup
- B) Convert all text to SmartArt
- C) Increase the font size and skip everything else
- D) Save the file as .ppsx so fonts are included automatically

**14. (H)** In the print options, what does "3 Slides" under Handouts produce, and why is it popular for training sessions?

- A) Three slides per page in a column with blank ruled lines for notes beside each slide
- B) Three slides per page with no notes space
- C) Three copies of one slide per page
- D) Three slides merged onto a single slide image

**15. (H)** Tomas marks his deck final using protection features, but a reviewer still needs to add comments without altering slide content. What is the best setup?

- A) Encrypt the file with a password the reviewer does not have
- B) Use Restrict Access / read-only recommended or Mark as Final as appropriate, since comments are feedback while content edits are what he must prevent; if true enforcement is needed, grant review-only permissions
- C) Delete the reviewer's copy of PowerPoint
- D) Save as .gif so nothing can be edited

---

## Section B: Practical Challenges (5 tasks, 5 points each = 25 points)

Complete each task in PowerPoint. Score yourself 1 point per verified success criterion.

**B1. Presenter View rehearsal.** Create a 4-slide practice deck called "Q7 Practice" with the fictional company "YourCompany Inc". Do the following: (a) type distinct speaker notes on all 4 slides, (b) run Rehearse Timings and save the timings so the show advances automatically, (c) confirm Presenter View shows the current slide, next slide, and your notes.

**B2. Collaboration round-trip.** (a) Save a copy of the deck to OneDrive or SharePoint to enable co-authoring, or explain in writing the exact steps to do so if offline. (b) Insert one comment on slide 2 tagging a fictional colleague. (c) Simulate Compare & Merge: use Review > Compare to merge a second copy with one changed slide, then step through the resulting Revisions and reject the change.

**B3. Accessibility pass.** On your 4-slide deck: (a) run the Accessibility Checker and clear or log every issue it reports, (b) add meaningful alt text to at least two images or shapes, (c) open the Selection Pane and confirm the reading order matches the intended visual order.

**B4. Export trio.** Export your deck as: (a) PDF (verify it opens and keeps 4 pages), (b) MP4 video using recorded timings (verify a saved .mp4 file exists), (c) GIF of the first slide only (verify the animated .gif file exists). Note the folder each file was saved in.

**B5. Handouts and pre-flight.** (a) Print-preview handouts with 3 Slides per page and confirm the ruled note lines appear, (b) save the deck with fonts embedded, (c) write a 6-point pre-flight checklist tailored to a live YourCompany Inc sales kickoff (beamer resolution, file backup on USB, Presenter View on/off, fonts, timing, offline access).

---

## Answer Key

*WARNING: spoilers below. Do not scroll past this line until you have finished and self-scored.*

**Section A answers**

1. **B** - Presenter View shows your notes, the current slide, the next slide, and a timer on your screen while the projector shows only the current slide.
2. **C** - The Notes pane sits below the slide canvas in Normal view and holds per-slide speaker notes.
3. **B** - Rehearse Timings records the duration you spend on each slide and offers to save those as slide timings for automatic advance.
4. **B** - Comments are attached to slides, show as small icons, and are collected in the Comments pane for threaded discussion.
5. **C** - Only the macro-enabled format .pptm stores VBA code; .pptx discards macros, and .pdf/.ppsx are not macro-editing formats.
6. **B** - Alt text is the description screen readers announce for non-text objects like pictures, shapes, and charts.
7. **B** - The navigator grid in Presenter View jumps directly to any slide; the audience sees only the destination slide, not the slides skipped.
8. **B** - Co-authoring on OneDrive or SharePoint lets multiple editors work simultaneously with near-live sync and presence indicators.
9. **A** - Compare & Merge combines copies and opens a Revisions pane where each change can be accepted or rejected individually.
10. **B** - The checker flags items such as missing alt text, unclear reading order, and poor contrast that block assistive technology users.
11. **B** - PDF is a fixed, universally viewable format that preserves layout without requiring PowerPoint or allowing edits.
12. **B** - MP4 bakes in timings, narration, and animations so playback is identical on any device with a media player, ideal for kiosks.
13. **A** - Embedding fonts prevents substitution on the venue machine, and a PDF backup covers the case where embedding fails or the file will not open.
14. **A** - The "3 Slides" handout prints three slide thumbnails in a column with lined note space beside them for handwriting.
15. **B** - Mark as Final or read-only discourages edits while still allowing the reviewer to see and add comments; real enforcement comes from permissions (review-only) rather than hiding the file.

**Section B model solutions**

**B1.** New presentation, add 4 slides with title+content. Click into the Notes pane under each slide and type distinct text. Slide Show > Rehearse Timings, advance through all 4 slides, press Esc, and choose Yes to save timings. To verify Presenter View: Slide Show > check "Use Presenter View" (Set Up Slide Show), then start the show and confirm the notes, current slide, and next slide appear on the presenter screen. Score: 1 pt notes on all slides, 1 pt timings saved (each slide shows its duration in Slide Sorter), 1 pt Presenter View turned on, 1 pt notes visible in Presenter View, 1 pt deck named "Q7 Practice".

**B2.** (a) File > Share > Save to Cloud (OneDrive/SharePoint) enables co-authoring; presence icons appear when others open it. Offline fallback: describe those exact steps in a note. (b) Insert > Comment on slide 2, type "Please confirm Q3 figures with Ana at YourCompany Inc". (c) Make a modified copy (change one slide), then Review > Compare and select the copy; PowerPoint merges and opens Revisions; use the pane's controls to reject the modification so the deck returns to its original state. Score: 1 pt cloud save/explanation, 1 pt comment inserted on slide 2, 1 pt compare performed, 1 pt change visible in Revisions, 1 pt change rejected.

**B3.** Review > Check Accessibility to open the checker; fix each listed issue (or record why it is a false positive). Right-click each picture/shape > Edit Alt Text and type a descriptive sentence (for example, "Bar chart showing YourCompany Inc Q3 revenue growth"). Open Home > Arrange > Selection Pane and drag items so the order top-to-bottom matches the reading sequence; re-run the checker to confirm. Score: 1 pt checker run, 1 pt issues fixed/logged, 1 pt alt text on 2+ objects, 1 pt reading order reviewed/reordered, 1 pt re-run shows improvement.

**B4.** File > Export > Create PDF/XPS for the PDF. File > Export > Create a Video with "Use Recorded Timings and Narrations", create the video, wait for rendering to finish, and confirm an .mp4 exists. File > Export > Create an Animated GIF, set the range to slide 1 only, export, and confirm the .gif exists. Score: 1 pt PDF opens with 4 pages, 1 pt MP4 exists and is non-empty, 1 pt GIF exists and animates, 1 pt timings option used for the video, 1 pt save locations recorded.

**B5.** File > Print > Settings > Full Page Slides dropdown > Handouts > 3 Slides and confirm the lined note column in the preview. File > Options > Save > check "Embed fonts in the file" (embed all characters), then save. Checklist should cover roughly: correct slide size and projector resolution tested, duplicate copy on USB and cloud, Presenter View enabled or disabled to match the venue, fonts embedded, rehearsed timings plus a fallback manual mode, offline copies available in case venue Wi-Fi fails. Score: 1 pt 3-slide handout previewed, 1 pt ruled lines confirmed, 1 pt fonts embedded, 1 pt checklist has 6 points, 1 pt checklist covers both tech and backup contingencies.

**Section A: 45 points. Section B: 25 points. Total: 70 points.**


## FILE: quizzes/quiz-08-vba-automation.md

# Quiz 8: VBA Automation

**Module tested:** Module 8: VBA Automation (Developer tab, macro security, file formats, VBE, object model, Subs, variables, loops, conditions, bulk generation, error handling, limits)

**Instructions**

- Answer all 15 multiple-choice questions in Section A (3 points each) and complete the 5 practical challenges in Section B (5 points each).
- Questions 13-15 are short code-reading items: read the Sub and pick what it does.
- Time yourself: 50 minutes total. For Section B, type the code yourself and run it before checking the model solutions.
- All fictional data uses the company "YourCompany Inc".

**Scoring**

| Total points | Percentage | Result |
|---|---|---|
| 63-70 | 90%+ | Advance to the next module |
| 49-62 | 70-89% | Review your weak areas, then retake |
| Below 49 | Below 70% | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 questions, 3 points each = 45 points)

Difficulty legend: **E** = easy, **M** = medium, **H** = hard.

**1. (E)** How do you enable the Developer tab on the ribbon?

- A) It appears automatically when you open any .pptm file
- B) File > Options > Customize Ribbon, then check Developer in the right-hand list
- C) Insert > Get Add-ins, search for "Developer"
- D) Review > Protect > Show Developer

**2. (E)** A saved presentation contains VBA code that must run next week. Which file extension must it use?

- A) .pptx
- B) .pptm
- C) .pdf
- D) .potx

**3. (E)** What is a .ppam file?

- A) A video export of a presentation
- B) A PowerPoint add-in file, typically used to distribute macros so they are available in every presentation
- C) A read-only handout template
- D) A compressed picture format

**4. (E)** What is the Visual Basic Editor (VBE)?

- A) The Notes pane in PowerPoint
- B) The separate window (Alt+F11) where you write, edit, and run VBA code
- C) A slide layout for code screenshots
- D) The Accessibility Checker's text mode

**5. (E)** Which VBA statement stores a reference to a slide in a variable named `sld`?

- A) `Dim sld As Slide`
- B) `Set sld = ActivePresentation.Slides(2)`
- C) `sld = ActivePresentation.Slides(2)`
- D) `Dim Set sld = Slide`

**6. (E)** In the PowerPoint object model, which object is the parent container of all slides?

- A) `Presentation`
- B) `Shape`
- C) `Comment`
- D) `Selection`

**7. (M)** Lina recorded a macro but wants to see and edit its code. Where does she go first?

- A) File > Options > Trust Center > Macro Settings
- B) Developer tab > Macros (or Alt+F8), select the macro, then click Edit to open the VBE
- C) Home > Replace > search for the macro name
- D) Slide Show > Rehearse Timings

**8. (M)** What is the purpose of macro security settings (Trust Center)?

- A) To make macros run faster
- B) To control which macros are allowed to run, protecting the machine from malicious code in downloaded files
- C) To convert VBA to JavaScript
- D) To password-protect slide content

**9. (M)** Which declaration correctly creates a variable that holds a reference to a TextFrame's text range?

- A) `Dim txt As String`
- B) `Dim rng As TextRange`
- C) `Dim txt As TextFrame`
- D) `Dim rng As Shape`

**10. (M)** What is the main structure of a Sub procedure?

- A) `Sub Name() ... End Sub` containing statements that perform an action when run
- B) `Function Name() ... End Function` only, since Subs cannot be run from PowerPoint
- C) `If Name Then ... End If`
- D) `For Each Name In Slides ... Next`

**11. (M)** When should you reach for VBA instead of manual editing?

- A) When you need to change one slide's title
- B) When you must repeat a mechanical task across many slides, such as generating 40 data slides from a table
- C) When you want better visual design for a single chart
- D) When you must deliver a deck in 5 minutes and have never used VBE

**12. (M)** Why is error handling (`On Error GoTo` / `MsgBox`) added to presentation macros?

- A) It makes the code compile in older PowerPoint versions
- B) It lets the macro report a clear message and stop cleanly instead of crashing with a cryptic run-time error
- C) It disables macro security
- D) It encrypts the VBA project

**13. (H, code reading)** What does this Sub do?

```vba
Sub FormatTitles()
    Dim sld As Slide
    For Each sld In ActivePresentation.Slides
        sld.Shapes(1).TextFrame.TextRange.Font.Bold = True
    Next sld
End Sub
```

- A) Deletes the first shape on every slide
- B) Bolds the text of the first shape on every slide
- C) Bolds only the title of the current slide
- D) Adds a new shape to every slide and bolds it

**14. (H, code reading)** What does this Sub do?

```vba
Sub AddStamps()
    Dim i As Integer
    For i = 1 To 3
        ActivePresentation.Slides.Add 1, ppLayoutBlank
        ActivePresentation.Slides(1).Shapes.AddTextbox( _
            msoTextOrientationHorizontal, 100, 100, 300, 50) _
            .TextFrame.TextRange.Text = "YourCompany Inc"
    Next i
End Sub
```

- A) Adds 3 blank slides at the beginning and puts a "YourCompany Inc" text box on each
- B) Adds 1 slide with 3 text boxes
- C) Replaces all text in the deck with "YourCompany Inc"
- D) Adds 3 text boxes to the current slide only

**15. (H, code reading)** What happens when this Sub runs?

```vba
Sub FixLabels()
    Dim sld As Slide
    For Each sld In ActivePresentation.Slides
        If sld.Shapes(1).HasTextFrame Then
            sld.Shapes(1).TextFrame.TextRange.Text = "Approved"
        End If
    Next sld
End Sub
```

- A) Every slide's first shape is deleted
- B) The first shape on each slide is renamed "Approved" in the Selection Pane
- C) On each slide, if the first shape can hold text, its text is replaced with "Approved"
- D) The macro fails because `If` cannot be used inside `For Each`

---

## Section B: Practical Challenges (5 tasks, 5 points each = 25 points)

Write and run real VBA in the VBE. Score yourself 1 point per verified success criterion. Use only "YourCompany Inc" as sample data.

**B1. Macro setup.** (a) Enable the Developer tab. (b) Create a new presentation and save it as "Q8 Automation.pptm". (c) Insert a standard module in the VBE and write a Sub named `HelloBox` that shows a message box with the text "YourCompany Inc automation online". (d) Run it from the Macros dialog and verify the box appears.

**B2. Loop over slides.** Write a Sub named `StampFooter` that uses a `For Each` loop to add the text "YourCompany Inc - Confidential" into a small text box at the bottom of every slide in the active presentation. Success: run it on a 3-slide test deck and see the text on all 3 slides.

**B3. Variables and Set.** Write a Sub named `SetTitle` that declares a `Slide` variable and a `String` variable with `Dim`, uses `Set` to point the slide variable at slide 1, and writes the string "Quarterly Kickoff" into the slide's title (or first text shape). Success: running it updates slide 1 visibly.

**B4. Conditional bulk build.** Write a Sub named `BuildAgenda` that loops 5 times and adds a new title-and-content slide each iteration, numbering each slide title "Agenda Item 1" through "Agenda Item 5". Inside the loop, use an `If` block so that when the number is 5 the body text reads "Wrap-up and Q&A" and otherwise it reads "Topic " & the number. Success: 5 new slides appear with the right titles and body text.

**B5. Error handling and judgment.** (a) Add `On Error GoTo ErrHandler` to `SetTitle` from B3 so that if the slide has no title placeholder, a `MsgBox` reports "No title found on this slide" instead of crashing; test it on a slide with no title. (b) In 3-4 sentences, name two situations where you should NOT use VBA and say what to do instead.

---

## Answer Key

*WARNING: spoilers below. Do not scroll past this line until you have finished and self-scored.*

**Section A answers**

1. **B** - The Developer tab is hidden by default and is turned on via File > Options > Customize Ribbon with the Developer checkbox.
2. **B** - VBA is only saved in macro-enabled formats: .pptm for presentations (or .ppam for add-ins); .pptx silently discards code.
3. **B** - A .ppam is an add-in package, the standard way to distribute macros so they load with PowerPoint and can serve all decks.
4. **B** - The VBE is the separate development window, opened with Alt+F11 or Developer > Visual Basic, where modules and code live.
5. **B** - Object references are assigned with `Set`; `Dim` only declares the variable's type, and `sld = ...` without `Set` is an object-assignment error.
6. **A** - The hierarchy runs Application > Presentation > Slide > Shape > TextFrame > TextRange, so `Presentation` contains the `Slides` collection.
7. **B** - Developer > Macros (Alt+F8) lists all macros; selecting one and clicking Edit jumps into the VBE at its code.
8. **B** - Trust Center macro settings control whether macros are disabled, enabled with notification, or trusted, blocking malicious code in files from the internet.
9. **B** - Text inside shapes is manipulated through a `TextRange` object (`Shape.TextFrame.TextRange`), so the variable is declared `As TextRange`.
10. **A** - A Sub is declared `Sub Name()` and closed with `End Sub`; it performs actions and can be run from the Macros dialog or assigned to a shape.
11. **B** - VBA pays off for repetitive mechanical work across many slides; one-off changes are faster by hand, and last-minute decks are a bad time to learn VBE.
12. **B** - `On Error GoTo` traps failures so the macro can explain the problem and exit gracefully instead of stopping with an unhandled run-time error.
13. **B** - The `For Each` visits every slide and `Shapes(1).TextFrame.TextRange.Font.Bold = True` bolds the text in the first shape on each one (the title in a standard layout).
14. **A** - The `For i = 1 To 3` loop runs 3 times; each iteration inserts a blank slide at position 1 and adds one text box containing "YourCompany Inc".
15. **C** - Inside the loop, the `If` checks `HasTextFrame` and only then replaces that shape's text with "Approved"; `If` is perfectly legal inside `For Each`.

**Section B model solutions**

**B1.** File > Options > Customize Ribbon > check Developer. Save As > "Q8 Automation.pptm" (choose PowerPoint Macro-Enabled Presentation). In VBE: Insert > Module, then type:

```vba
Sub HelloBox()
    MsgBox "YourCompany Inc automation online"
End Sub
```

Back in PowerPoint, Alt+F8 > HelloBox > Run. Score: 1 pt Developer tab visible, 1 pt saved as .pptm, 1 pt module with the Sub, 1 pt code compiles, 1 pt message box appears.

**B2.**

```vba
Sub StampFooter()
    Dim sld As Slide
    For Each sld In ActivePresentation.Slides
        sld.Shapes.AddTextbox(msoTextOrientationHorizontal, _
            100, 500, 400, 30).TextFrame.TextRange.Text = _
            "YourCompany Inc - Confidential"
    Next sld
End Sub
```

Score: 1 pt `Dim sld As Slide`, 1 pt `For Each ... Next`, 1 pt AddTextbox with a bottom-of-slide position, 1 pt correct text, 1 pt runs on all 3 slides.

**B3.**

```vba
Sub SetTitle()
    Dim sld As Slide
    Dim title As String
    Set sld = ActivePresentation.Slides(1)
    title = "Quarterly Kickoff"
    sld.Shapes(1).TextFrame.TextRange.Text = title
End Sub
```

(Using `sld.Shapes.Title.TextFrame.TextRange.Text = title` is also correct when a title placeholder exists.) Score: 1 pt `Dim` both variables, 1 pt `Set` used for the slide reference, 1 pt string assigned to the variable, 1 pt writes into the slide's title/first shape, 1 pt runs successfully.

**B4.**

```vba
Sub BuildAgenda()
    Dim i As Integer
    Dim sld As Slide
    For i = 1 To 5
        Set sld = ActivePresentation.Slides.Add( _
            ActivePresentation.Slides.Count + 1, ppLayoutText)
        sld.Shapes.Title.TextFrame.TextRange.Text = "Agenda Item " & i
        If i = 5 Then
            sld.Shapes(2).TextFrame.TextRange.Text = "Wrap-up and Q&A"
        Else
            sld.Shapes(2).TextFrame.TextRange.Text = "Topic " & i
        End If
    Next i
End Sub
```

Score: 1 pt `For i = 1 To 5` loop, 1 pt adds a slide each iteration, 1 pt numbered titles, 1 pt `If ... Then ... Else` block, 1 pt correct body text (item 5 differs).

**B5.** (a)

```vba
Sub SetTitle()
    Dim sld As Slide
    On Error GoTo ErrHandler
    Set sld = ActivePresentation.Slides(1)
    sld.Shapes.Title.TextFrame.TextRange.Text = "Quarterly Kickoff"
    Exit Sub
ErrHandler:
    MsgBox "No title found on this slide"
End Sub
```

Test on a blank-layout slide with no title placeholder: the message box appears and the macro stops cleanly. (b) Model answer for the judgment part: do not use VBA for one-off design tweaks (restyling a single slide is faster by hand in Normal view), and do not use VBA when a built-in feature already does the job (exporting PDF or running the Accessibility Checker are one-click commands). Do not use it either when the deck must be handed to users whose security policy blocks macros: build the content manually or deliver a .pptx/.pdf instead. Score: 1 pt `On Error GoTo` label present, 1 pt `MsgBox` in the handler, 1 pt `Exit Sub` before the handler, 1 pt tested on a no-title slide, 1 pt two sensible "do not use VBA" cases with alternatives.

**Section A: 45 points. Section B: 25 points. Total: 70 points.**


## FILE: quizzes/quiz-score-summary.md

# Quiz Score Summary: PowerPoint Zero to Hero

**Purpose:** track your self-assessment results across all 8 module quizzes, spot weak topics, and judge when you are ready to move on (and, ultimately, to sit the MOS exam).

**Instructions:** fill one row per quiz immediately after scoring. Each quiz is worth 70 points (15 multiple-choice at 3 points + 5 practical challenges at 5 points). Record the first attempt, then the retake after reviewing weak areas.

## Scoreboard

| Quiz | Module | Date | Score (/70) | % | Retake (/70) | Retake % | Weak topics |
|---|---|---|---|---|---|---|---|
| 1 | 01: Getting Started and Interface | | | | | | |
| 2 | 02: Creating Presentations | | | | | | |
| 3 | 03: Working with Slides | | | | | | |
| 4 | 04: Formatting and Design | | | | | | |
| 5 | 05: Tables, Charts, SmartArt | | | | | | |
| 6 | 06: Animation and Transitions | | | | | | |
| 7 | 07: Delivery and Workflow | | | | | | |
| 8 | 08: VBA Automation | | | | | | |
| **Totals** | **All modules** | | **/560** | **%** | **/560** | **%** | |

## How to interpret your scores

**Per quiz**

| Percentage | Points (/70) | What it means | What to do |
|---|---|---|---|
| 90%+ | 63-70 | Solid command of the module | Advance to the next module |
| 70-89% | 49-62 | Functional but with real gaps | Review the weak topics listed, then retake and record the retake score |
| Below 70% | Below 49 | Foundations are missing | Restudy the whole module (notes and practice files) before retaking |

**Across the whole set**

- **90%+ average (504+/560 first attempts):** you have absorbed the course. Move to exam-style practice (timed mock exams, no answer keys open).
- **70-89% average (392-503/560):** you are progressing well but carry gaps. Prioritize restudy of any quiz below 75% before starting certification prep; weak areas compound on the MOS exam where tasks mix topics.
- **Below 70% average (below 392/560):** do not rush ahead. Restudy the lowest two modules completely, retake those quizzes, and only then continue. Consistency beats speed.

**Readiness for MOS certification (PowerPoint)**

Consider yourself ready to schedule the MOS exam when all of the following are true:

1. Every quiz scores 85%+ (60+/70) on a first or retake attempt, with no quiz below 75%.
2. Section B practical challenges pass fully in real PowerPoint under time pressure, not just "on paper".
3. You can complete the practical tasks in Modules 2-7 with no help from the answer key, since the MOS exam is almost entirely hands-on project tasks.
4. You have done at least two full-length timed mock exams at 70%+.
5. Module 8 (VBA) is a bonus topic on the exam: treat a low score there as less critical than a low score in any of Modules 1-7.

If points 1-4 are not all met yet, keep using this scoreboard to close the gaps and retake. Re-record scores here each time so progress is visible.

*All fictional data in the quizzes uses "YourCompany Inc".*


## FILE: sample-decks/walkthrough-01-starter.md

# Walkthrough: sample-01-starter-deck.pptx

What to notice in the 7-slide starter deck (companion to **Module 1: Fundamentals**).

## The Point of This Deck

This is what "fundamentals done right" looks like: nothing fancy, nothing broken. Study it before you study style.

## What to Notice

1. **The structure is right, even though the build is simple.** Title slide, agenda, content slides, closing: consistent margins and flow throughout. One honest note: this deck was generated with free-floating text boxes rather than layout placeholders, so when you rebuild (exercise below), do it with real placeholders via Home > Layout. That is the Module 2 way, and it is what makes templates and Reset work.
2. **Bullet discipline.** Slide 3 ("Teams lose hours every day") uses 4-word bullets plus a stat callout ("11 hrs") instead of sentences. Compare with the word wall in `exercise-fix-this-deck.pptx` (issue 4) to see the difference 6x6 discipline makes. (Module 1)
3. **Assertion titles.** "Teams lose hours every day" states a conclusion. A weak deck would say "The Problem". (Modules 1, 3)
4. **16:9 slide size** throughout, consistent margins, everything on a grid. Select all shapes on any slide (Ctrl+A) and watch the Smart Guides confirm the alignment. (Module 1)
5. **Footer with slide numbers** on every content slide. Two clicks to set up properly via Insert > Header & Footer. (Module 2)
6. **Fictional but realistic data.** The "11 hrs" stat cites a fictional survey. Your decks need source lines too, even internal ones.

## Rebuild Exercise

Delete slide 4-7 and rebuild them from scratch. Success = a stranger cannot tell your slides from the originals. Time yourself: 20 minutes is a good target after Module 2.

## Where This Fits in Your Study

Week 1 of any study plan. Pair with `quiz-01-fundamentals.md` after rebuilding.


## FILE: sample-decks/walkthrough-02-pitch-deck.md

# Walkthrough: sample-02-business-pitch-deck.pptx

What to notice in the 12-slide pitch deck (companion to **Modules 2-3: Design**).

## The Point of This Deck

The visual-design showcase: one palette, one motif, varied layouts, and a story arc that sells.

## What to Notice

1. **The palette does the branding.** One dominant navy (roughly 60-30-10: navy dominant, ice-blue support, one warm accent used sparingly). Write down the three hex values you see and check that no slide invents a fourth color. (Module 3)
2. **One repeated motif.** Icons and stat blocks sit in the same style of container on every slide. That repetition is what makes 12 slides feel like one deck. (Module 3, CRAP: repetition)
3. **Layout variety without chaos.** Slide 2 is a stat trio, slide 3 a 3-step flow with icons, later slides use columns and callouts. Same skeleton family, different arrangements. Compare against a deck where every slide is title-plus-bullets. (Module 3)
4. **Type contrast.** Big bold display headings vs small body text. If you squint until text is unreadable, the slide still has a visible structure: that is the test. (Module 3 typography)
5. **The story arc.** Cost of chaos (problem) > one flow (solution) > how it works > market > traction with a chart > model > competition > team > ask. Slide titles alone should tell the whole pitch. Read just the 12 titles now. (Module 9, Project 1)
6. **The chart earns its place.** One chart on the traction slide with honest axes and direct labels. (Module 4)

## Rebuild Exercise

Rebuild the problem slide (slide 2) in a different palette (e.g. the terracotta scheme from `sample-05`). Notice which design decisions survive the swap (layout, contrast) and which were palette-dependent.

## Where This Fits in Your Study

Weeks 2-3 of the 12-week plan. Pair with `quiz-03-visual-design.md` and Brief 1 in `../exercises/deck-build-briefs.md`.


## FILE: sample-decks/walkthrough-03-data-report.md

# Walkthrough: sample-03-data-report-deck.pptx

What to notice in the 9-slide data report (companion to **Module 4: Tables, Charts & DataViz**).

## The Point of This Deck

Charts as arguments. Every visual here makes a claim and shows its evidence honestly.

## What to Notice

1. **Slide 2: KPIs show change, not just numbers.** "$247k +38% YoY" beats "$247k". Each stat pairs a number with its delta and timeframe. (Module 4)
2. **Slide 3: the title carries the finding.** "Revenue grew every quarter except a Q3 supply dip" is a sentence you could say out loud in a meeting. The chart underneath is the evidence, and the "Read this" sidebar tells the viewer what matters. (Module 3 assertion-evidence + Module 4)
3. **Slide 4: same data, two charts.** The wrong pie (time series in slices, unreadable) vs the right column chart. This is the chart-chooser lesson in one slide. Open both chart objects (double-click) and compare their data sheets: identical numbers. (Module 4, chart chooser)
4. **Slide 7: honest vs misleading axes.** The "axis cut at 50" version makes a small jump look dramatic. This is the fake-drama trap from the ethical-display section. Notice how the honest zero-baseline version changes the story's tone. (Module 4, ethical display)
5. **Table styling.** The top-accounts table uses banded rows and no heavy gridlines. Compare with the spreadsheet-dump look in the fix-me deck. (Module 4)
6. **Native chart objects.** Every chart here is an editable PowerPoint chart (right-click > Edit Data), not a screenshot. Yours should be too.

## Rebuild Exercise

Take real numbers from your own work (or make up 4 quarters), and build the honest/misleading pair yourself. Success = both charts from one data table, one deliberately wrong.

## Where This Fits in Your Study

Week 4 of the 12-week plan. Pair with `quiz-04-tables-charts.md` and Briefs 4-5 in `../exercises/deck-build-briefs.md`.


## FILE: sample-decks/walkthrough-04-animated-demo.md

# Walkthrough 04: Animated Product Demo (TaskFlow Pro)

**Deck:** `sample-04-animated-product-demo.pptx` (8 slides) | **Companion to:** Module 5, Transitions & Animations

This deck is a teaching artifact. Open it in PowerPoint 2019 or newer (Morph needs it), press F5, and use the notes below to reverse-engineer what is inside. All three animations were injected as raw XML, so what you see is exactly what the animation engine reads.

## What to notice

**1. The Morph zoom (slides 2 to 3).** Slide 2 is the "big picture": one large box named `!!RevenueEngine` with three dots below it (`!!Dot1` = Pipeline, `!!Dot2` = Automation, `!!Dot3` = Insights). Slide 3 zooms into the detail: the same `!!RevenueEngine` box shrank to a small header bar and the same three dots now sit on top of three component boxes. That is the Morph duplicate-slide technique: duplicate the slide, move/resize the *same* shapes, then Morph tweens the move. Select any shape and check Home > Arrange > Selection Pane: the paired shapes carry identical names. The `!!` prefix is the trick that **forces** PowerPoint to pair shapes by name instead of guessing by similarity. The transition lives on slide 3: Transitions tab shows Morph, Effect Options > By Object.

**2. The chart fade (slide 4).** The bar chart (four fictional quarters) has a Fade *entrance* effect. Open Animations > Animation Pane: one effect, Start: On Click. The effect was written as a `<p:timing>` block whose `<p:animEffect transition="in" filter="fade">` targets the chart's shape id. For the teaching version, set Effect Options > By Category in the Chart Animation tab and PowerPoint grows the build through Q1 to Q4.

**3. The click trigger (slide 6).** Click the small mint "i" circle during the slide show: the dark footnote appears. Nothing advances. In the Animation Pane this reads as a *trigger* group (star icon with a lightning mark). In the timing XML it is an interactive sequence (`<p:cTn nodeType="interactiveSeq">`) whose `stCondLst` carries `<p:cond evt="onClick"><p:tgtEl><p:spTgt spid="...">` targeting the `!!InfoIcon` shape, and that sequence reveals `!!FootnoteReveal` with a fade.

## Rebuild it yourself (Module 5 exercise)

1. Duplicate slide 2, shrink `!!RevenueEngine`, move the dots, add the three boxes. Set Morph on slide 3.
2. On slide 4 select the chart, Animations > Add Animation > Fade, then Chart Animation > By Category.
3. On slide 6 select the footnote, Animations > Trigger > On Click of > `!!InfoIcon`.

Slide 7 repeats this recipe in-deck so learners can work offline.


## FILE: sample-decks/walkthrough-05-training-deck.md

# Walkthrough: sample-05-training-deck-notes.pptx

What to notice in the 13-slide training deck (companion to **Module 7: Delivery & Workflow**).

## The Point of This Deck

A teachable deck: structure a live audience can follow, with speaker notes that carry the facilitator.

## What to Notice

1. **Speaker notes on every slide (13/13).** Open View > Notes Page and read them all at once. They are prompts ("point at each zone on your screen"), not scripts. Compare: a script makes you read aloud; a prompt makes you talk. (Module 7)
2. **Section dividers do real work.** The 3 dark "01 / 02 / 03" dividers split the hour into mental chapters. Note how the agenda slide maps 1:1 to the dividers. (Module 7, large-deck management)
3. **The activity slide is the peak, not an afterthought.** "Try it: 5 minutes" with exact steps, a time box, and a follow-up plan ("two volunteers share screens"). The notes coach the facilitator on pacing ("stay silent for the first minute"). (Module 7 rehearsal)
4. **Learning objectives slide states outcomes as verbs.** "Navigate, run, apply" - things the learner will DO, not topics that will be "covered". Steal this pattern for every training deck you build. (Module 9, Project 2)
5. **Teaching slides carry diagrams, not paragraphs.** The zone map (slide 5) and the board diagram (slide 9) are built from simple shapes. Anyone can rebuild them in 5 minutes, which means they can edit them live. (Module 3 shapes)
6. **The close loops back.** The recap quotes the agenda's three promises and adds one next step ("build one real board this week"). Note the notes instruct the facilitator to ask the room FIRST before reading the list. (Module 7)

## Rebuild Exercise

Write a 10-slide training deck for something YOU know (a recipe, a tool, a hobby) with notes on every slide. Then rehearse it with Presenter View (Module 7) and rewrite any note you actually read word-for-word.

## Where This Fits in Your Study

Week 7 of the 12-week plan. Pair with `quiz-07-delivery-workflow.md` and Brief 9 in `../exercises/deck-build-briefs.md`.


## FILE: sample-decks/walkthrough-06-brand-template.md

# Walkthrough: sample-06-brand-template.potx

What to notice in the brand template (companion to **Module 2: Design Foundations**).

## The Point of This File

A reusable `.potx` template for YourCompany Inc: 5 layout patterns plus a usage-example slide. This is what "consistent branding in 2 clicks" looks like.

## What Is Inside

| Slide | Layout pattern | Use for |
|-------|----------------|---------|
| 1 | Title (dark navy, gold tick) | Deck openers |
| 2 | Section Header ("01" + title) | Chapter breaks |
| 3 | Content (assertion title + text + visual area) | Standard slides |
| 4 | Two Content (side-by-side cards) | Comparisons, options |
| 5 | Closing (centered CTA) | Deck enders |
| 6 | How-to-use guide | Instructions (delete before use) |

## What to Notice

1. **The brand glue repeats.** The gold tick (top-left) and navy footer bar with logo placeholder appear on every slide via `brand_frame()`. One motif, consistent presence. (Module 2, Module 3)
2. **`.pptx` vs `.potx`.** Two files ship: `sample-06-brand-template.potx` (the actual template: its content type is `presentationml.template.main+xml`, so PowerPoint opens it as File > New, not as a normal deck) and `sample-06-brand-template.pptx` (a preview copy you can open normally and inspect). (Module 2 file formats)
3. **Placeholders are labeled for humans.** "YOUR LOGO (replace)", "Assertion Title Goes Here": a template should tell the next user what to do. Yours should too.
4. **Theme-safe colors.** Navy / sand / gold are set as consistent fills, so a theme swap restyles everything at once. Test it: Design > Variants > Colors.

## Install It

1. Copy `sample-06-brand-template.potx` into your PowerPoint templates folder (on Windows: `Documents\Custom Office Templates\`).
2. In PowerPoint: File > New > Personal. Your template appears there.
3. Replace the logo placeholder and footer text with your brand.

## Where This Fits in Your Study

Week 2 of the 12-week plan. Pair with `quiz-02-design-foundations.md` and Brief 10 in `../exercises/deck-build-briefs.md`.


## FILE: sample-decks/walkthrough-06-fix-this-deck.md

# Walkthrough: exercise-fix-this-deck.pptx

How to run the Fix-This-Deck challenge (companion to `../exercises/fix-this-deck-challenge.md`).

## The Point of This Deck

It is deliberately broken. This 2005-style sales deck for TaskFlow Pro contains exactly **20 planted issues** across design, content, accessibility, and technical hygiene. Your job: find them all.

## How to Run the Challenge

1. Open the deck and look for 5 minutes without touching anything.
2. List every problem you spot (the worksheet in `../exercises/fix-this-deck-challenge.md`).
3. Score: 1 point per issue. 16-20 = hero eyes, 11-15 = solid, 6-10 = revisit Modules 1-4, 0-5 = restudy and retry.
4. The answer key (20 issues, grouped in 4 categories) lives in the same challenge file, below the line. No spoilers here.
5. Rebuild the deck properly (Brief 3 in `../exercises/deck-build-briefs.md`).

## Technical Notes

- The tacky animations are real: every text shape on every slide has a Bounce entrance (yes, it is as annoying as it looks - that is issue material).
- The two charts are native chart objects, so you can inspect their axis settings and see exactly how the misleading one was built.
- All content is fictional (YourCompany Inc, `sales@acme.example`), including the deliberately dead hyperlink.

## Where This Fits in Your Study

Mid-course (weeks 3-4 of 12) after Modules 1-4, and again at the end as a final test. Try it twice: most learners jump 5+ points between attempts.


## FILE: exercises/deck-build-briefs.md

# Deck-Build Briefs: Practice Projects

10 build briefs to stretch your skills between modules. Each brief is a real-world request with constraints, like a client would give you. Build the deck in PowerPoint, then self-grade against the success criteria.

**How to use:** pick a brief at your level, build it in one sitting (30-90 min), grade yourself honestly, note weak skills in `../11-Study-Plan/progress-tracker.md`.

---

## Brief 1: The One-Slide Resume (Beginner, 30 min)

**Request:** a single slide that sells a fictional person (Jordan Ade, junior data analyst) to a hiring panel. Photo placeholder, 3 skill icons, one stat callout ("cleaned 50k rows"), contact line.
**Constraints:** one slide, max 40 words total, one accent color only.
**Success criteria:** readable at a glance in 5 seconds; no bullet list; aligned to a grid; no stretched images.

## Brief 2: Meeting Deck in 20 Minutes (Beginner, 20 min)

**Request:** a 5-slide deck for a fictional weekly team standup: title, 3 update slides (done / doing / blocked), next steps slide.
**Constraints:** built from a theme or template, every slide uses the correct layout placeholder, footer with slide numbers.
**Success criteria:** uses sections or clear slide titles; no default "Click to add title" anywhere; consistent fonts throughout.

## Brief 3: The Bullet Diet (Beginner+, 45 min)

**Request:** take the worst slide you can find (or a paragraph-heavy slide from `exercise-fix-this-deck.pptx`) and rebuild it assertion-evidence style: one-sentence headline claim + one supporting visual.
**Constraints:** max 12 words on the content area; must include one shape-based visual or icon row.
**Success criteria:** headline states a conclusion, not a topic; visual actually supports the claim; passes the "readable from the back" test.

## Brief 4: Chart Makeover (Intermediate, 45 min)

**Request:** given fictional quarterly revenue data (Q1 $42k, Q2 $51k, Q3 $47k, Q4 $63k), build one slide that tells the story "Q4 broke the trend upward". Two versions: one with a chart, one with shape-based KPI callouts.
**Constraints:** correct chart type for the story; no chart junk; honest axes (no truncation).
**Success criteria:** viewer gets the point in 3 seconds; legend/labels only where needed; pick your favorite of the two versions and defend why.

## Brief 5: The Data Report Slice (Intermediate, 60 min)

**Request:** a 4-slide mini report for a fictional product: overview slide with 3 KPIs, one chart slide, one table slide (top 5 customers), one conclusions slide.
**Constraints:** table styled (no spreadsheet look); chart uses linked or embedded data; consistent palette across all 4 slides.
**Success criteria:** every slide title is an assertion; KPIs show change (%, delta), not just raw numbers; one printed handout would look professional.

## Brief 6: The Morph Moment (Intermediate+, 45 min)

**Request:** a 3-slide "zoom into the detail" sequence using Morph: overview (a box labeled "Revenue Engine"), mid view (3 components), detail (one component expanded with numbers).
**Constraints:** use the duplicate-slide Morph technique; shared elements renamed so Morph matches them; no flying text.
**Success criteria:** motion is smooth and purposeful; a viewer says "that helped me understand", not "cool effect".

## Brief 7: The Animated Build (Intermediate+, 60 min)

**Request:** one chart slide where data reveals in sequence (Q1 first, then Q2-Q4 with "With Previous" after a delay), plus one trigger animation (click a "?" icon to reveal a footnote).
**Constraints:** entrance animations only where they aid the narrative; total animation time under 5 seconds; no sound effects.
**Success criteria:** animations fire in the right order every time; presenter could narrate over the build naturally.

## Brief 8: The Interactive Menu (Advanced, 60 min)

**Request:** a 7-slide self-guided deck: a menu slide with 3 buttons (Agenda A, B, C) using Summary Zoom or action buttons, 2 slides per section, and a "back to menu" button on every content slide.
**Constraints:** works in kiosk mode; dead-end slides forbidden; clean buttons (no default blue hyperlinks).
**Success criteria:** navigate the whole deck without the keyboard; every link lands where promised.

## Brief 9: The Rehearsed Talk (Advanced, 90 min)

**Request:** a 10-slide conference talk on any hobby or topic you know well, with speaker notes, then rehearse it twice using Presenter View and Rehearse Timings.
**Constraints:** 5-7 minute talk; notes are prompts, not scripts; run the Accessibility Checker and fix everything it reports.
**Success criteria:** timings recorded and reasonable (no slide longer than 90 seconds); alt text on every image; export a PDF that still looks right.

## Brief 10: The Template Factory (Advanced+, 120 min)

**Request:** build a branded .potx template system for a fictional brand (YourCompany Inc): slide master with logo and footer, 4 custom layouts (title, section header, content, closing), theme colors and fonts, then build 3 slides from it proving it works.
**Constraints:** all formatting lives in the master/layouts, not on individual slides; the template survives a "Reset" on every slide.
**Success criteria:** someone else can build a consistent deck from your template without instructions; changing the theme color updates every slide.

---

## Companion Files

| File | Use with |
|------|----------|
| `exercise-fix-this-deck.pptx` + `fix-this-deck-challenge.md` | Brief 3 and the find-20-issues challenge |
| `../sample-decks/` | Reference builds for every brief |
| `../cheat-sheets/` | Keep open while building |
| `../11-Study-Plan/progress-tracker.md` | Log every completed brief |


## FILE: exercises/fix-this-deck-challenge.md

# The Fix-This-Deck Challenge (Find 20 Issues)

Companion to `exercise-fix-this-deck.pptx` (deliberately broken 8-slide sales deck for a fictional product, YourCompany Inc's "TaskFlow Pro").

## How the Challenge Works

1. Open `exercise-fix-this-deck.pptx` and look at every slide for 5 full minutes without touching anything.
2. List every problem you spot: design, content, accessibility, and technical issues. There are **20 planted issues** in 4 categories.
3. Score: 16-20 found = hero eyes, 11-15 = solid, 6-10 = revisit Modules 1-4, 0-5 = restudy then retry.
4. Then rebuild the deck properly (Brief 3 in `deck-build-briefs.md`). Rebuilding is where the learning happens; spotting is just the warm-up.

## Issue Worksheet (write your findings before checking the key)

| # | Slide | Category (Design / Content / A11y / Tech) | What is wrong | Which module fixes it |
|---|-------|-------------------------------------------|---------------|-----------------------|
| 1 | | | | |
| 2 | | | | |
| ... up to 20 | | | | |

---

## ANSWER KEY (spoilers below the line)

The 20 planted issues, by category:

### Design Issues (7)

1. **Title slide stretched logo**: YourCompany Inc logo is dragged to non-proportional size (squashed wide). Fix: corner handles only (Module 3).
2. **Three fonts on one deck**: Calibri, Comic Sans, and Impact all in use. Fix: one theme font pair (Modules 2-3).
3. **Rainbow palette**: five accent colors with no system (green, purple, orange, red, teal on one slide). Fix: 60-30-10 palette (Module 3).
4. **Word wall**: slide 3 has 11 bullet lines of full sentences. Fix: assertion-evidence, 6x6 rule (Modules 1, 3).
5. **Nothing aligned**: text boxes and shapes each sit at their own x-position (jagged left edges). Fix: Align tools and gridlines (Module 3).
6. **Decorative clip art**: a 2003-style clip art graphic of a person carrying a giant folder. Fix: modern icons or SVG (Module 3).
7. **Low contrast**: light gray body text on a light yellow background on slide 5. Fix: contrast and accessibility (Module 3).

### Content Issues (5)

8. **Topic title, not a claim**: "Revenue" as a slide title instead of "Q4 revenue grew 38%". Fix: assertion-evidence titles (Module 3).
9. **Pie chart for trends**: a pie chart showing 8 quarters of revenue. Fix: line chart for trend (Module 4).
10. **Truncated axis**: a column chart starting the y-axis at 30k to exaggerate growth. Fix: ethical axes (Module 4).
11. **Chart junk**: gridlines, legend, data labels, AND axis titles all on one simple chart. Fix: data-ink ratio cleanup (Module 4).
12. **Fake precision**: "market share is 12.3847%" (7 significant figures). Fix: honest rounding (Module 4).

### Accessibility Issues (4)

13. **Missing alt text**: 3 meaningful images with no alt text. Fix: alt text + Accessibility Checker (Module 7).
14. **Reading order chaos**: screen reader would read decorative text before the headline. Fix: reading order pane (Module 7).
15. **No slide titles**: 5 of the 8 slides (agenda, revenue detail, market share, demo, close) have no title at all, and even the cover's heading is styled text instead of a title placeholder, so 6 slides total get flagged. That kills navigation and screen readers. Fix: real titles on every slide (Module 7).
16. **Video with no captions**: demo video has no captions or transcript. Fix: captions, media accessibility (Modules 6-7).

### Technical Issues (4)

17. **Default "Click to add title"** still visible on slide 7. Fix: layout/placeholder discipline (Module 1).
18. **Inconsistent slide size**: one slide pasted in from a 4:3 deck (black bars expected on screen). Fix: slide size + reset (Modules 1-2).
19. **Broken hyperlink**: the "Learn more" link points to a moved page (dead link). Fix: hyperlink hygiene (Module 6).
20. **Tacky animation**: "Bounce" entrance animation on every bullet of every slide with sound effect. Fix: animation restraint, the 3-second rule (Module 5).

## Grading Yourself

- **1 pt per issue spotted** (identify slide + what is wrong; category naming optional).
- Rebuild the deck as a clean version and compare against `sample-02-business-pitch-deck.pptx` styling to grade your fix quality.
- Log your score in `../11-Study-Plan/progress-tracker.md`.


## FILE: anki/README.md

# PowerPoint Flashcards for Anki

120 ready-made flashcards covering the full "PowerPoint Zero to Hero" curriculum.

## 1. Install Anki

Download Anki for free at <https://apps.ankiweb.net/> and install it (Windows, macOS, or Linux).

## 2. Import the deck

1. Open Anki and create or select a profile.
2. Go to **File > Import...** and choose `powerpoint-flashcards.csv`.
3. In the import dialog, set the field mapping exactly as below.

## 3. Field mapping

| CSV column | Anki field   | Notes                                        |
|------------|--------------|----------------------------------------------|
| Front      | Field 1      | The question / prompt (front of card)         |
| Back       | Field 2      | The answer (back of card)                     |
| Category   | Field 3: Tags| Lowercase hyphenated topic tags               |

Recommended import settings:

- Type: **Basic**
- Deck: create a new deck named `PowerPoint Zero to Hero`
- Check **"Allow HTML in fields"** (not required, but harmless)
- Field separator: **Comma**
- Check the preview to confirm every card splits into 3 fields, then click **Import**.

## 4. Study tip

Set new cards to **5 per day** and let spaced repetition do its work. Review every day
(Anki schedules cards just before you forget them), and hit "Again" honestly when you
miss one. Steady daily review beats cramming: 5 cards a day finishes the deck in
24 days and keeps ~90% retention long term.

## 5. Card count by category

| Category (tag)        | Cards |
|-----------------------|-------|
| fundamentals          |    15 |
| design-foundations    |    12 |
| visual-design         |    18 |
| tables-charts         |    18 |
| animations            |    16 |
| media-interactivity   |    14 |
| delivery-accessibility|    12 |
| vba                   |    10 |
| design-principles     |     5 |
| **Total**             | **120** |

Filter by tag in Anki (for example `tag:animations`) to drill a single topic before
working through that section of the course.


## FILE: anki/powerpoint-flashcards.csv

```csv
Front,Back,Category
"What is the default file format for a modern PowerPoint presentation?",pptx (Presentation Open XML). Older binary format is pptx's predecessor ppt, and macro-enabled decks are saved as pptm.,fundamentals
"What keyboard shortcut inserts a new slide?",Ctrl+M inserts a new slide below the current one in Normal view.,fundamentals
"What is the fastest way to duplicate a slide?",Select the slide thumbnail and press Ctrl+D (or right-click > Duplicate Slide).,fundamentals
"What is the difference between F5 and Shift+F5?",F5 starts the slide show from the first slide. Shift+F5 starts it from the currently selected slide.,fundamentals
"How do you exit a running slide show?",Press Esc. The slide show also ends after the last slide unless Loop mode is on.,fundamentals
"What is Normal view used for?",It is the main editing view with the slide pane, thumbnail rail, and Notes pane, used to build and edit individual slides.,fundamentals
"What is Slide Sorter view?",A grid of slide thumbnails for reordering, deleting, or applying transitions to many slides at once.,fundamentals
"What is Reading View?",It plays the slide show in the window with simple controls, useful for reviewing a deck without going full screen.,fundamentals
"What is a placeholder?",An empty container on a slide layout (title, text, picture, chart) that prompts you to click and add content.,fundamentals
"What are slide layouts?",Predefined arrangements of placeholders in the slide master (Title Slide, Title and Content, Two Content) that keep slides consistent.,fundamentals
"What are Sections and what are they for?",Named groups in the thumbnail rail that organize large decks, collapse for navigation, and can be collapsed or reordered as a block.,fundamentals
"How do you promote or demote a bullet level in the Outline pane?",Place the cursor in the line and press Tab to demote (deeper level) or Shift+Tab to promote (move up a level).,fundamentals
"What do Ctrl+Z and Ctrl+Y do?",Ctrl+Z undoes the last action and Ctrl+Y redoes it or repeats the last command.,fundamentals
"How do you save a deck as a PDF?",File > Save As (or Export) and choose PDF, or File > Export > Create PDF/XPS Document.,fundamentals
"What is AutoSave and what does it require?",AutoSave saves changes continuously to OneDrive or SharePoint. It is disabled for files stored only on the local machine.,fundamentals
"What is the Slide Master?",The top-level template that stores theme colors, fonts, background, and layouts for the whole presentation so global edits happen in one place.,design-foundations
"How do you open the Slide Master?",View tab > Slide Master. Click Close Master View on the ribbon when finished.,design-foundations
"What is the difference between a theme and a template?",A theme is a set of colors, fonts, and effects. A template is a theme plus saved content and layouts, saved with the potx extension.,design-foundations
"What is the hierarchy of PowerPoint formatting?",Theme > Slide Master > individual Layouts > individual slides. Formatting set at a higher level flows down to everything below it.,design-foundations
"Name the placeholder types managed in the master.",Title, body/text, date, footer, and slide number placeholders. Footer items are switched on via Insert > Header & Footer.,design-foundations
"How do you apply a footer and slide numbers to every slide?",Insert > Header & Footer, check Footer and Slide number, type the footer text, then click Apply to All.,design-foundations
"How do you change theme colors for the whole deck?",Design tab > Variants > Colors > Customize Colors, then edit accent and text colors and save as a custom color set.,design-foundations
"How do you set a background for all slides?",Right-click a slide > Format Background (or Design > Format Background). Hide background graphics on one slide by checking Hide background graphics in Format Background.,design-foundations
"What is the difference between the Notes Master and the Handout Master?",Notes Master controls printed speaker notes pages. Handout Master controls printed handouts with 1, 2, 3, 4, 6, or 9 slides per page.,design-foundations
"Why edit the Slide Master instead of each slide?",One edit to the master updates every slide and layout at once, guarantees consistency, and prevents drift as the deck grows.,design-foundations
"How do you save a custom template?",File > Save As and choose PowerPoint Template (potx). New presentations can then start from it via File > New > Personal.,design-foundations
"What is a theme variant and where do you find it?",Design tab > Variants are coordinated color, font, and effect sets that restyle the whole deck in one click while keeping layouts intact. Use the dropdowns to customize each aspect.,design-foundations
"What is the 6x6 rule?",No more than 6 bullets per slide and 6 words per bullet. It keeps slides scannable and stops the audience reading instead of listening.,visual-design
"What is the difference between a typeface and a font?",A typeface is the design family (Arial). A font is a specific size and weight of that typeface (Arial Bold 24pt).,visual-design
"Should slides use serif or sans-serif type?",Sans-serif (Arial, Calibri, Helvetica) reads better on screen at large sizes. Serif type is traditionally used for dense printed body text.,visual-design
"What is the minimum recommended body text size on a slide?",24pt for body text and 36pt or larger for titles. If text must shrink below 24pt, cut content instead.,visual-design
"How many typefaces should a deck use?",Two at most: one for headings and one for body text. Extra weights and sizes create variety without adding visual noise.,visual-design
"What contrast ratio should slide text meet for readability?",WCAG AA requires 4.5:1 for normal text and 3:1 for large text. Dark text on a light background or its inverse beats low-contrast pairings.,visual-design
"What are complementary colors?",Two colors opposite each other on the color wheel (blue and orange). They create strong contrast and work for emphasis.,visual-design
"What are analogous colors?",Three neighboring colors on the color wheel (blue, blue-green, green). They feel harmonious and work for backgrounds and calm themes.,visual-design
"What is the difference between RGB and CMYK?",RGB is additive light for screens (red, green, blue). CMYK is subtractive ink for print (cyan, magenta, yellow, key/black). Slides use RGB.,visual-design
"What is the 60-30-10 color rule?",About 60% dominant neutral, 30% secondary color, and 10% accent for emphasis. The accent highlights only what matters most.,visual-design
"What is visual hierarchy in slide design?",Arranging elements so the eye reads them in order of importance using size, weight, color, and position. The headline is always read first.,visual-design
"Why does alignment matter in slide layout?",Aligned elements look intentional and professional. Use Align tools and smart guides (Alt-drag or View > Guides) rather than placing by eye.,visual-design
"What is the principle of proximity?",Items that belong together should sit close together. Related bullets, titles, and captions group into clear visual units.,visual-design
"What does consistency mean in a deck?",Same fonts, colors, spacing, logo position, and layout logic on every slide. Consistency signals professionalism and reduces mental load.,visual-design
"What is white space and why is it valuable?",The empty area around and between elements. It separates groups, improves focus, and makes slides look premium rather than crammed.,visual-design
"How does the Z-pattern apply to slides?",The eye scans a slide left to right and top to bottom in a rough Z. Place the title top-left, key content in the middle, and the takeaway or logo at the bottom.,visual-design
"How do you keep color choices colorblind-friendly?",Never rely on red versus green alone to show meaning. Add labels, patterns, or position cues so meaning survives without color.,visual-design
"How do you match a color already used in the deck?",Shape Fill (or Text Fill) > Eyedropper, then click the target color on the slide to sample it exactly.,visual-design
"How do you insert a table?",Insert > Table and drag to pick rows and columns, or use Insert > Table > Insert Table and type the exact numbers.,tables-charts
"When should you use a table instead of a chart?",Use a table for exact values and lookups the audience must read. Use a chart when the audience should see a trend, comparison, or proportion at a glance.,tables-charts
"What is a column chart best for?",Comparing values across a few categories (quarterly revenue by region). Use a bar chart instead when category labels are long.,tables-charts
"What is a line chart best for?",Showing change over continuous time (monthly signups across a year). Keep it to 4 or fewer series so lines stay readable.,tables-charts
"What is the recommended maximum number of pie chart slices?",Five or fewer. Above that, switch to a bar chart because small slices are impossible to compare.,tables-charts
"Why use a horizontal bar chart for long category names?",Horizontal bars give long labels room to read left to right without rotating text or cramming columns.,tables-charts
"What is a scatter (XY) chart used for?",Plotting the relationship between two numeric variables (ad spend vs sales) to reveal correlation or outliers.,tables-charts
"How do you merge cells in a table?",Select the cells and click Table Layout > Merge Cells (or right-click > Merge Cells).,tables-charts
"How do you make table rows or columns equal in size?",Select them and use Table Layout > Distribute Rows or Distribute Columns.,tables-charts
"How should a table header row look?",Bold or a contrasting fill so it separates from data, and repeat it across pages in printed handouts via Table Layout > Repeat Header Rows.,tables-charts
"What is zebra striping in tables?",Alternating light row shading that helps the eye track across wide tables. Use subtle tints, not heavy borders.,tables-charts
"What are chart elements in PowerPoint?",Title, axis titles, legend, data labels, gridlines, and trendlines. Add or remove them from Chart Design > Add Chart Element.,tables-charts
"How do you edit the data behind a chart?",Chart Design > Edit Data opens the embedded worksheet (a trimmed Excel sheet). Type new values and the chart updates live.,tables-charts
"What is chart junk and how do you remove it?",Unnecessary ink like heavy gridlines, 3D effects, and redundant labels. Delete gridlines and 3D styles so the data is the only ink left.,tables-charts
"When should you use data labels instead of a value axis?",Use direct data labels on bars when you need exact values on a handful of points. Otherwise keep the axis and skip labels to reduce clutter.,tables-charts
"How do you animate a chart piece by piece?",Add an entrance effect to the chart, then in Effect Options choose By Series or By Category (and By Element in Series if needed).,tables-charts
"When is SmartArt a better choice than a chart?",SmartArt shows process, hierarchy, and relationships (cycles, org charts). Charts show numeric comparison and trends.,tables-charts
"What do table styles control?",A preset combination of banding, header emphasis, and border treatment. Apply one from Table Design and turn Banded Rows on or off there.,tables-charts
"What is the difference between a transition and an animation?",A transition plays when moving between slides. An animation plays on an object inside a single slide.,animations
"Name the four animation effect types.",Entrance (object appears), Emphasis (object draws attention), Exit (object disappears), and Motion Path (object moves along a drawn path).,animations
"What is the Animation Pane and how do you open it?",The sidebar that lists every effect in order with timing bars. Open it from Animations > Animation Pane.,animations
"What are the three Start options for an animation?",On Click, With Previous (starts with the prior effect), and After Previous (starts when the prior effect finishes).,animations
"What is a Trigger in PowerPoint animation?",An effect that starts only when you click a specific object or play a media bookmark, set under Trigger > On Click of.,animations
"What is the difference between Duration and Delay?",Duration is how long the effect plays. Delay is how long it waits before starting, measured in seconds.,animations
"What does the Morph transition do?",It animates objects between two slides by interpolating shared objects, creating smooth movement, resizing, and color shifts. Duplicate a slide, move or recolor an object, then apply Morph.,animations
"How do you apply one transition to the whole deck?",Set the transition on one slide in the Transitions tab and click Apply To All.,animations
"What is the Animation Painter?",In the Animations tab, it copies all animation effects from one object to another, like Format Painter for animations. Double-click it to paint multiple objects.,animations
"What do Effect Options control?",The variant of a chosen effect, such as direction (From Bottom), sequence (By Series for charts), or sound.,animations
"How do you make a slide advance without clicking?",Transitions tab > Timing > Advance Slide: uncheck On Mouse Click and check After, then set the time in seconds.,animations
"What is Rehearse Timings?",Slide Show > Rehearse Timings runs the deck with a stopwatch so PowerPoint records how long you spend on each slide and can auto-advance with those timings.,animations
"How do you set transition direction and sound?",Transitions tab > Effect Options picks the direction. The Sound dropdown adds a sound, which should normally stay (No Sound) for business decks.,animations
"Why avoid flashy transitions in a business deck?",Spin, Boomerang, and similar effects distract from content and can look unprofessional. Stick to Fade or Morph and apply them consistently.,animations
"What is a motion path animation?",An effect that moves an object along a preset or custom drawn line or curve. Edit the path by dragging its points in the Animation Pane.,animations
"What is the rule of thumb for animation use?",Animate only to reveal content in the order you will speak about it. If an effect does not help the explanation, delete it.,animations
"How do you insert a video?",Insert > Video > This Device (local file) or Online Video (YouTube or embed code). Recommended formats are MP4 with H.264 video and AAC audio.,media-interactivity
"What are the video playback start options?",Video Playback > Start: In Click Sequence, Automatically, or When Clicked On. Automatically is best for unattended kiosk shows.,media-interactivity
"How do you trim a video in PowerPoint?",Select the video, then Video Playback > Trim Video. Set Start and End points and click OK. The original file is unchanged.,media-interactivity
"What is a poster frame?",A still image shown on the video before playback starts, set from Video Format > Poster Frame > Image from File.,media-interactivity
"How do you insert audio on a slide?",Insert > Audio > Audio on My PC or Record Audio. A speaker icon appears and playback is controlled from the Audio Playback tab.,media-interactivity
"How do you make audio play across multiple slides?",Select the audio icon, then Audio Playback > Start > Automatically and check Play in Background, which loops and plays across slides until stopped.,media-interactivity
"How do you trim audio?",Select the audio icon and choose Audio Playback > Trim Audio, then set the start and end points.,media-interactivity
"How do you record the screen in PowerPoint?",Insert > Screen Recording, drag to select the area (or use Select All), choose whether to record audio and pointer, and click Record. Press Win+Shift+Q to stop.,media-interactivity
"What is the difference between Screenshot and Screen Clipping?",Insert > Screenshot captures a whole open window. Screen Clipping at the bottom of that gallery lets you drag-select part of the screen.,media-interactivity
"How do you create a hyperlink?",Select text or an object and press Ctrl+K (or Insert > Link), then choose a web page, another slide, a file, or an email address.,media-interactivity
"What are Action buttons and Action Settings?",Shape > Action Buttons provides arrow and home icons that run an action on click or mouseover, such as jumping to a slide, a URL, or running a macro.,media-interactivity
"What is PowerPoint Zoom?",Insert > Zoom offers Slide Zoom (jump to one slide), Section Zoom (jump to a section), and Summary Zoom (a live menu of sections you can return from).,media-interactivity
"How do you shrink a deck with heavy media?",File > Info > Compress Media to downsample videos and audio to Standard, HD, or Full HD quality before sharing the file.,media-interactivity
"How do you export a deck as a video?",File > Export > Create a Video, pick resolution (1080p is typical), choose whether to use recorded timings, and click Create Video to produce an MP4.,media-interactivity
"What is Presenter View and what does it require?",The speaker-facing screen showing current slide, next slide, notes, and a timer. It requires two displays (or Alt+F5 to preview it on one).,delivery-accessibility
"How do you turn the mouse into a laser pointer during a show?",Hold Ctrl and drag the mouse, or press Ctrl+L to toggle the laser pointer. Press Ctrl+A to switch back to the arrow.,delivery-accessibility
"What do the B and W keys do during a slide show?",B shows a black screen and W shows a white screen. Any keypress or click returns to the slide, useful for discussion.,delivery-accessibility
"How do you jump directly to a specific slide during a show?",Type the slide number and press Enter. Press Enter alone to jump to the first slide.,delivery-accessibility
"How do you see all slides during a running slide show?",Press S (or Ctrl+S) to open the All Slides thumbnail view, then click any slide to jump to it.,delivery-accessibility
"What is a Custom Slide Show?",Slide Show > Custom Slide Show > Custom Shows lets you define named subsets of slides from one deck for different audiences without duplicating the file.,delivery-accessibility
"What does the Accessibility Checker look for and where is it?",Review > Accessibility Checker flags missing alt text, low-contrast text, unclear hyperlink text, and reading order problems in the Accessibility pane.,delivery-accessibility
"What is alt text and why does it matter?",A short description of a picture, shape, or chart read aloud by screen readers. Add it in the alt text pane (right-click > Edit Alt Text) so visuals are not skipped.,delivery-accessibility
"How do you fix the reading order of a slide?",Open Home > Arrange > Selection Pane and reorder items; screen readers and Tab navigation read objects from the bottom of the list to the top.,delivery-accessibility
"How do you print speaker notes or handouts?",File > Print, then under Settings choose Notes Pages (one slide plus notes) or Handouts with 1 to 9 slides per page, then print or export to Word.,delivery-accessibility
"How do you share a deck so formatting stays intact?",Save to OneDrive and share a view link, or File > Export > Create PDF/XPS when the audience only needs to read. Send the pptx only when they must edit.,delivery-accessibility
"What accessibility basics should every slide meet?",Readable font size (24pt+), 4.5:1 contrast, alt text on images, meaningful hyperlink text (not "click here"), and logical reading order.,delivery-accessibility
"What is VBA in PowerPoint?",Visual Basic for Applications, the built-in programming language used to automate repetitive tasks and add custom interactivity to presentations.,vba
"How do you open the VBA editor?",Press Alt+F11 (or enable the Developer tab and click Visual Basic). Alt+F11 toggles between the editor and PowerPoint.,vba
"What file extension keeps macros?",pptm (macro-enabled presentation). Saving as pptx silently strips the macros.,vba
"What is the basic structure of a VBA macro?",Sub MacroName() ... End Sub. A macro is a Sub procedure that you run to perform its steps.,vba
"What does MsgBox do in VBA?",Displays a dialog with a message, for example MsgBox "Done" or MsgBox ActivePresentation.Slides.Count to show the slide count.,vba
"How do you enable the Developer tab?",File > Options > Customize Ribbon and check Developer in the right-hand list, then click OK.,vba
"How do you set macro security?",Developer > Macro Security chooses Disable with notification (default, prompts to enable signed or trusted macros) or other levels. Only enable macros from sources you trust.,vba
"How do you run a macro?",Press Alt+F8, select the macro name, and click Run (or assign it to a shape action or button).,vba
"How do you add a new slide with VBA?",ActivePresentation.Slides.Add Index:=ActivePresentation.Slides.Count + 1, Layout:=ppLayoutText adds a Title and Content slide at the end.,vba
"How do you step through VBA code line by line to debug?",Press F8 in the editor to step one line at a time and watch values in the Locals window. F5 runs to the next breakpoint or end.,vba
"What is the one-idea-per-slide rule?",Each slide makes exactly one point, stated in the headline. Supporting evidence stays on that slide and everything else moves to a new slide or the appendix.,design-principles
"What is the picture superiority effect?",People remember images far better than words. Pairs of a simple picture and a short phrase beat walls of text for recall.,design-principles
"What is cognitive load theory in slide design?",Working memory is limited, so slides must remove extraneous load (clutter, animation, tiny text) and let the audience absorb one idea at a time.,design-principles
"What is the rule of thirds for slide composition?",Divide the slide into a 3x3 grid and place the title along the top third and the focal element at an intersection, rather than dead center.,design-principles
"What is the data-ink ratio?",The share of ink that shows actual data. Raise it by deleting decorative chart ink so every mark carries information.,design-principles
```


## FILE: CONTRIBUTORS.md

# Contributors

- **[tempesteni](https://github.com/tempesteni)** - Project owner.
  Roles: concept and curriculum direction, scope decisions (5-length study plan system, multi-sample deck strategy), review, corrections, quality control, environment setup, publishing decisions.

- **[Hermes Agent](https://hermes-agent.nousresearch.com)** by Nous Research - AI engineering partner.
  Roles: research and source compilation, module authoring, quiz and answer-key generation, cheat sheet and flashcard authoring, sample deck generation (pptxgenjs / python-pptx), speaker notes and animation XML engineering, URL verification and dead-link repair, content and security verification, README and documentation.

## How This Was Built

Human direction + AI execution. The design targets (what "zero to hero" should contain, what good looks like, what to cut) came from the owner; the research, drafting, generation, and verification passes were executed by Hermes Agent under review. Quality gates (link checks, content checks, visual QA) were run before delivery.

All sample decks use fictional brands and data (YourCompany Inc, TaskFlow Pro). No real credentials, people, or company data appear anywhere in this package.


## FILE: path.md

# path.md: How This Package Was Built

Process documentation for the PowerPoint Zero to Hero package, written so anyone can rebuild or extend it.

## The Strategy

Same proven "study guide strategy" as the Microsoft-Excel-Zero-to-hero package: modules + quizzes + cheat sheets + practice artifacts + flashcards + multi-length study plans, packaged publish-ready with verification gates.

## Build Phases

1. **Scaffold** - 16 folders, planned content map (8 modules + projects + sources + study plan + 4 support folders + sample-decks).
2. **Study plans first** - 5 learner-selectable tracks (12/8/6/4/2 weeks) + progress tracker. Pace varies, content does not.
3. **Module research + writing** - 8 modules + 6 project briefs via parallel AI subagents (2 rounds: research-capped round, then skip-research fast path after timeouts proved research was the bottleneck).
4. **Supporting materials** - 8 quizzes (15 MC + 5 practical each, 70-pt scale), 4 cheat sheets, 120 Anki flashcards, 10 deck-build briefs, fix-this-deck challenge (20 planted issues, answer key).
5. **Sample decks** - 7 real .pptx artifacts (starter, pitch, data report, animated demo, training w/ notes, .potx template, deliberately-broken fix-me). Mix of AI-subagent builds and deterministic python-pptx/pptxgenjs generator scripts (kept in sample-decks/ so learners can study how the decks were generated).
6. **Verification gate** - files (33 checked, 0 empty), links (57 URLs curl-tested; 11 dead/typo'd found, all repaired and re-verified), content (0 em dashes, module cross-refs, consistency), security (0 tokens/wallets/real emails).
7. **Visual QA** - LibreOffice headless render (7 PDFs, 63 slide images), per-deck contact sheets, fresh-eyes AI visual inspection with fix loop.
8. **Docs** - README (comprehensive, inline AI setup guides), this file, CONTRIBUTORS, HOW-TO-USE-WITH-AI.

## Key Decisions

- **5 study plan lengths in one file** instead of 5 separate plans: learner picks a track; content stays identical.
- **Sample decks as first-class teaching artifacts** with walkthroughs, not screenshots: learners open and reverse-engineer real files.
- **The fix-me deck plants exactly 20 issues** matching the challenge answer key (7 design, 5 content, 4 accessibility, 4 technical).
- **Generators shipped alongside decks** (build_sample05.py, build_fixme.py, build_sample06.py): automation is itself a Module 8 lesson.
- **Animations via XML injection** (Morph transitions, Bounce entrances, trigger timing) since pptxgenjs/python-pptx cannot author motion: deck files carry real animation data.
- **Skip-research fast path** for authoring: web research was the timeout bottleneck; deep-link guessing was banned (Microsoft GUID URLs 404); all external URLs verified at the gate instead.

## Toolchain

pptxgenjs (npm) + python-pptx + markitdown + LibreOffice headless + poppler (pdftoppm) + Pillow (contact sheets). All run locally on Linux: no Microsoft Office required to build or verify.

## Extending

New module: drop `NN-topic/NN-topic.md` with the metadata block + self-contained `##` sections, then add its quiz, flashcards, and study-plan references. Re-run the link gate (curl every URL) before publishing.
