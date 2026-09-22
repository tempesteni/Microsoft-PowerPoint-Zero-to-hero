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
