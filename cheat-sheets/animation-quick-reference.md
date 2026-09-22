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
