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
