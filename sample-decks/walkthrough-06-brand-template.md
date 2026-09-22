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
