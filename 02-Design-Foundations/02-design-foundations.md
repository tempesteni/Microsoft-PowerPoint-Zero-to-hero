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
