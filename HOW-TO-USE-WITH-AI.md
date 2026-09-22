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
