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
