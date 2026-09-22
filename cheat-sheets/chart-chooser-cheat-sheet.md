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
