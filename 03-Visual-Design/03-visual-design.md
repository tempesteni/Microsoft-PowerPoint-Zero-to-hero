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
