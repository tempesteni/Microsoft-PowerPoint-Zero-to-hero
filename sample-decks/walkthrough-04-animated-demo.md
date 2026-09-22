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
