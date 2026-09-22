# Module 08: VBA Automation & Add-ins

> **Module Number:** 08
> **Title:** VBA Automation & Add-ins
> **Level:** Advanced+
> **Prerequisites:** Modules 01-07 (slides, layouts, themes, SmartArt, animation basics), comfort with the PowerPoint ribbon, basic willingness to read code. Prior Excel VBA exposure helps but is not required.
> **Estimated Study Time:** 150-180 minutes (plus practice project time)
> **Next Module:** 09 (Presentation Delivery & Speaker Tools)

---

## 8.1 Why Automate PowerPoint?

Automation is not about showing off with code. It is about removing work that a machine can do faster and more reliably than a human. In a corporate setting, the same three chores eat most of the hours: building near-identical decks over and over, keeping every slide on-brand, and applying the same edit across dozens of slides.

**The three big wins:**

1. **Batch deck generation.** Imagine YourCompany Inc runs a quarterly sales kickoff. You need 40 personalized decks, one per sales representative, each with a name slide, a territory map, and three quota slides. Doing this by hand means 40 times the copy-paste. With VBA you write one procedure that reads a list of representatives and produces all 40 decks while you get coffee.
2. **Consistent branding.** Branding drifts: someone types in Calibri when the brand font is Segoe UI, someone uses a blue that is 5 shades off, someone resizes a logo. A small macro can sweep every shape in a deck and normalize fonts, colors, and logo positions in seconds.
3. **Repetitive edits.** "Change the project code on all 60 slides from PRJ-111 to PRJ-204." "Delete every slide that mentions the old product name." "Add a confidentiality footer to all slides." These are perfect for code and terrible to do by hand.

**A fourth, quieter win: reliability.** A macro applied to 200 slides makes the same mistake (if any) 200 times consistently, which is easy to spot and fix once. A human doing it manually makes 200 different small mistakes.

**Real-world example (YourCompany Inc):** The marketing team receives a spreadsheet export every Monday with this week's webinar speakers: name, title, topic, and session time. They must turn each row into a branded "Meet the Speaker" slide in the master weekly deck. At 12 speakers a week that is 12 slides built by hand every Monday, or about 25 minutes of layout fiddling. The VBA routine in section 8.5 does it in about 4 seconds.

**When automation is the wrong tool:** see section 8.11. Short version: if the built-in Design Designer or the Morph transition can do it, use those first. They are faster to apply and cannot break with a compile error.

**Try it now:** Open any deck you have built during this course. Count how many slides you would have to touch to change the title font. Multiply that count by 2 minutes. That number is your automation payback budget: if writing a macro takes less time than that, the macro wins.

---

## 8.2 Enabling the Developer Tab and Macro Security

Before you can touch any automation features, you must un-hide the Developer tab and understand the security model. PowerPoint hides Developer by default precisely because macros are powerful, and powerful means dangerous in the wrong hands.

### Enable the Developer tab (exact steps)

1. Open PowerPoint and go to **File > Options**.
2. In the left pane of the PowerPoint Options dialog, click **Customize Ribbon**.
3. In the right-hand list titled "Main Tabs", find **Developer** (it is unchecked by default).
4. Check the box next to **Developer**.
5. Click **OK**. The Developer tab now appears in the ribbon between View and Help (position may vary by version).

### Macro security settings

Click **Developer > Macro Security** (this opens **Trust Center > Macro Settings**). You have four options:

| Setting | What it does | When to use |
|---|---|---|
| Disable all macros without notification | Blocks every macro silently | Locked-down corporate machines |
| Disable all macros with notification | Blocks macros but shows a yellow security bar with an "Enable Content" button (recommended default) | Everyday work |
| Disable all macros except digitally signed macros | Only runs macros from trusted publishers | Teams with code-signing certificates |
| Enable all macros (not recommended) | Runs everything, including malware | Only on isolated test VMs, never on a work machine |

**Recommended:** keep "Disable all macros with notification". You decide per file whether to trust it.

### Trusted locations

Instead of clicking "Enable Content" every time, you can designate folders whose files always run macros:

1. **File > Options > Trust Center > Trust Center Settings > Trusted Locations**.
2. Click **Add new location**, browse to a folder such as `C:\Users\Public\Documents\YourCompany-Macros\`, check "Subfolders of this location are also trusted" if useful, click **OK**.
3. Files opened from that folder run their macros without the security bar.

Use trusted locations for your own macro library. Do not mark your Downloads folder as trusted: that is the first place malware arrives.

### .pptx vs .pptm vs .ppam (file formats matter)

| Extension | Contains macros? | Notes |
|---|---|---|
| `.pptx` | No | The default. If you save a macro-enabled deck as .pptx, **the VBA code is silently discarded** (you get a warning dialog; read it). |
| `.pptm` | Yes | Macro-enabled presentation. Use for decks that carry their own code. |
| `.ppam` | Yes | PowerPoint Add-in. Loaded by the application, not opened as a visible deck. Used to distribute toolbars and macros (section 8.10). |
| `.ppt` / .pps | Legacy binary formats | Avoid for new work. |

**The single most common beginner loss:** writing three hours of code, saving as .pptx, closing, reopening, and finding the code gone. Save as .pptm **before** you write your first line.

**Try it now:** Enable the Developer tab, then create a blank presentation and immediately save it as `AutomationSandbox.pptm` in a folder you will use as a trusted location. Add that folder as a trusted location and confirm no security bar appears when you reopen the file.

---

## 8.3 Recording a Macro and Why PowerPoint's Recorder Disappoints

Excel users come to PowerPoint expecting the macro recorder to be a code generator. It is not. It is nearly useless here, and understanding why saves you frustration.

### How to record

1. **Developer > Record Macro** (or **View > Macros > Record Macro** in older layouts).
2. Give the macro a name like `RecordLayoutTest` (no spaces, must not start with a digit).
3. Optionally assign it a shortcut key and store it in this presentation or in a new add-in.
4. Perform actions: insert a shape, type text, move something, change a font.
5. **Developer > Stop Recording** (the same button toggles).

### What the recorder actually captures in PowerPoint

Unlike Excel (which records nearly every cell action as code), PowerPoint's recorder captures only a short list: mostly text editing, some font formatting, and slide-level actions. It does **not** record inserting shapes, moving shapes, changing slide layouts, applying animations, setting transitions, or resizing objects. That is a crippling gap for the very tasks you want to automate.

### The limits, honestly stated

- You cannot learn the object model by recording and reading code, the way you can in Excel.
- Recorded code is often verbose and uses `Select` and `Selection`, which is fragile (see section 8.12).
- There is no "relative reference" toggle like Excel's recorder offers.

### What the recorder IS good for

- Discovering exact property names for font and text formatting (record "make text bold Segoe UI 28pt dark red" and read what the generated code calls those properties).
- Quick personal keystroke-savers for tiny text edits.

**The practical takeaway:** in PowerPoint you learn by reading the object model (section 8.4) and by experimenting in the Immediate window, not by recording. Treat the recorder as a formatting-lookup tool only.

**Try it now:** Record a macro that types "YourCompany Inc" into a text box and formats it Segoe UI, 32 pt, bold, dark blue. Stop recording and view the code (**Developer > Macros > RecordLayoutTest > Edit**). Note how much of your action actually appears in the code. Save the code snippet as a formatting crib sheet for later.

---

## 8.4 The VBA Editor (VBE) and the PowerPoint Object Model

The Visual Basic Editor is where all code lives. Learn its four panels and you are halfway to productive.

### Opening and navigating the VBE

1. Press **Alt+F11** (or **Developer > Visual Basic**). The VBE opens as a separate window.
2. **Project Explorer** (Ctrl+R if missing): a tree of all open presentations and add-ins, each containing `Microsoft PowerPoint Objects` (like `ThisPresentation`) and `Modules`.
3. **Code window:** double-click any module in the Project Explorer to open its code. Each `Sub ... End Sub` block is one procedure.
4. **Immediate window** (Ctrl+G if missing): a scratchpad where single lines execute the moment you press Enter. This is the fastest way to test object model ideas.
5. **Properties window** (F4): shows properties of the selected object in the Project Explorer (mostly useful for add-in and userform work).

### Inserting a module

In the Project Explorer, right-click your presentation name (for example `VBAProject (AutomationSandbox.pptm)`), choose **Insert > Module**. A new `Module1` appears. Code in modules contains procedures you can run from **Developer > Macros**. Code placed in `ThisPresentation` runs in response to presentation events (such as `Presentation_Open`), which is how add-ins initialize themselves.

### The PowerPoint object model (the map of everything)

Think of the model as nested containers:

- **Application** - the PowerPoint program itself. Holds `Presentations` (all open decks), `SlideShowWindows`, and global settings.
- **Presentations** (collection) -> **Presentation** - one open deck. Holds `Slides`, `PageSetup`, `FullName` (its file path).
- **Slides** (collection) -> **Slide** - one slide. Holds `Shapes`, `SlideIndex`, `Layout`, `HeadersFooters`, and `TimeLine` (animation sequencing).
- **SlideRange** - a selection of one or more slides (a group of slides you are acting on together).
- **Shapes** (collection) -> **Shape** - any object on a slide: text box, picture, table, SmartArt, placeholder. This is where most automation happens.
- **TextFrame** -> **TextRange** - the text inside a shape and its formatting.
- **Sequence** -> **Effect** - entries on a slide's animation timeline (the object model name for what the Animations pane shows you).

**Mental model rule:** everything is "the thing contains a collection of smaller things". To reach a piece of text you walk down: `Application.ActivePresentation.Slides(3).Shapes("Title 1").TextFrame.TextRange.Text`.

**Try it now:** Press Alt+F11, Ctrl+G for the Immediate window, and type `? Application.ActivePresentation.Slides.Count` then Enter. It answers with the number of slides in your deck. Then type `? Application.ActivePresentation.Slides(1).Shapes.Count`. You have just queried the object model live.

---

## 8.5 Writing Sub Procedures: Slides, Shapes, and Text

A `Sub` procedure is a named block of code you can run. Everything you automate lives inside Subs.

### Anatomy of a Sub

```vba
' A Sub procedure: runs when you press F5 inside it or pick it from Developer > Macros
Sub HelloWorldSlide()
    ' Declare an object variable to hold the new slide we create
    Dim sld As Slide

    ' Add a slide with a title-only layout (ppLayoutTitleOnly = 11) to the ACTIVE presentation
    Set sld = Application.ActivePresentation.Slides.Add( _
        Index:=Application.ActivePresentation.Slides.Count + 1, _
        Layout:=ppLayoutTitleOnly)

    ' Put text into the title placeholder and format it
    With sld.Shapes.Title.TextFrame.TextRange
        .Text = "YourCompany Inc: Quarterly Update"
        .Font.Name = "Segoe UI"
        .Font.Size = 36
        .Font.Bold = msoTrue
    End With
End Sub
```

Line continuation is `_` (underscore preceded by a space) at the end of a line. Without it, one logical line must fit on one physical line.

### Add, modify, and delete slides

```vba
Sub SlideLifecycle()
    Dim sld As Slide
    Dim deck As Presentation
    Set deck = Application.ActivePresentation

    ' ADD: append a slide at the end using the Title and Content layout (ppLayoutText = 2)
    Set sld = deck.Slides.Add(deck.Slides.Count + 1, ppLayoutText)
    sld.Shapes.Title.TextFrame.TextRange.Text = "YourCompany Inc Product Roadmap"

    ' MODIFY: change the slide's layout after the fact and rename it in the selection pane
    sld.Layout = ppLayoutTitleOnly
    sld.Name = "RoadmapSlide"

    ' DUPLICATE: copy a slide (returns a SlideRange of 1 slide)
    Dim dup As SlideRange
    Set dup = sld.Duplicate
    dup(1).MoveTo deck.Slides.Count

    ' DELETE: remove the duplicate we just made
    dup.Delete
End Sub
```

### Add shapes and text boxes, and set text

```vba
Sub AddShapesAndText()
    Dim sld As Slide
    Set sld = Application.ActivePresentation.Slides(1)

    ' Add a rounded rectangle banner shape (msoShapeRoundedRectangle = 5)
    ' Arguments: type, Left, Top, Width, Height (all in points; 72 points = 1 inch)
    Dim banner As Shape
    Set banner = sld.Shapes.AddShape(msoShapeRoundedRectangle, 0, 0, 540, 60)

    ' Color the banner YourCompany brand blue and write text inside it
    banner.Fill.ForeColor.RGB = RGB(0, 74, 124)
    With banner.TextFrame.TextRange
        .Text = "YourCompany Inc Confidential"
        .Font.Color.RGB = RGB(255, 255, 255)
        .Font.Size = 18
        .ParagraphFormat.Alignment = ppAlignCenter
    End With

    ' Add a free-floating text box with the AddTextbox method
    ' Arguments: orientation (msoTextOrientationHorizontal = 1), Left, Top, Width, Height
    Dim tb As Shape
    Set tb = sld.Shapes.AddTextbox(msoTextOrientationHorizontal, 40, 300, 400, 80)
    tb.TextFrame.TextRange.Text = "Prepared by the YourCompany Enablement Team"

    ' DELETE a shape: remove any shape on this slide named "Old Logo"
    ' On Error Resume Next keeps the code running if no such shape exists (see 8.9)
    On Error Resume Next
    sld.Shapes("Old Logo").Delete
    On Error GoTo 0
End Sub
```

**Real-world example:** A legal disclaimer must appear on every slide of an external-facing deck. A 15-line Sub adds a text box with the disclaimer text in 9 pt gray at the bottom of every slide, deleting any pre-existing "Disclaimer" box first so the macro can be run repeatedly (this pattern is called making a macro *idempotent*).

**Try it now:** In the VBE, insert a module and paste the `HelloWorldSlide` Sub. Press F5 to run it. Check your slide show: a new final slide with a YourCompany title should appear. Now change the `.Text` line and run it again.

---

## 8.6 Variables, Object Variables, and Loops

### Variables and object variables

Use `Dim` to declare variables. Use `Set` when assigning **objects** (slides, shapes, presentations). Forgetting `Set` for objects is the number one beginner compile/runtime error.

```vba
Sub VariableBasics()
    ' Value variables: no Set needed
    Dim repName As String
    Dim quota As Double
    Dim targetCount As Integer
    repName = "Rep Exampleperson"   ' fake data: YourCompany Inc
    quota = 125000.5
    targetCount = 12

    ' Object variables: MUST use Set
    Dim sld As Slide
    Dim shp As Shape
    Set sld = Application.ActivePresentation.Slides(1)
    Set shp = sld.Shapes(1)

    ' Read object properties with plain dot notation
    Debug.Print repName, shp.Name, sld.SlideIndex

    ' Good hygiene: release object variables when done (optional in VBA but tidy)
    Set shp = Nothing
    Set sld = Nothing
End Sub
```

`Debug.Print` writes to the Immediate window (Ctrl+G), which is your best friend for quick inspection.

### Loops: For Each over slides and shapes

`For Each` walks a collection without you managing an index. This is the workhorse of PowerPoint automation.

```vba
' Sweep every slide and every shape: find and replace text deck-wide
Sub BulkFindReplace()
    Dim sld As Slide
    Dim shp As Shape

    ' Outer loop: every slide in the active presentation
    For Each sld In Application.ActivePresentation.Slides
        ' Inner loop: every shape on that slide
        For Each shp In sld.Shapes
            ' Only shapes that CAN hold text have a TextFrame with HasText
            If shp.HasTextFrame Then
                If shp.TextFrame.HasText Then
                    ' Replace old project code with the new one
                    ' TextRange.Replace returns the number of replacements made
                    shp.TextFrame.TextRange.Replace _
                        FindWhat:="PRJ-111", _
                        ReplaceWhat:="PRJ-204"
                End If
            End If
        Next shp
    Next sld

    MsgBox "Rebrand sweep complete for YourCompany Inc."
End Sub
```

### A counted For loop and If blocks

```vba
' Delete every slide AFTER slide 3 whose title contains "DRAFT"
Sub PurgeDraftSlides()
    Dim i As Long
    Dim sld As Slide

    ' IMPORTANT: when deleting in a loop, walk BACKWARDS (Step -1)
    ' Walking forward shifts indexes and makes you skip slides
    For i = Application.ActivePresentation.Slides.Count To 1 Step -1
        Set sld = Application.ActivePresentation.Slides(i)

        ' If blocks: only act on slides that HAVE a title
        If sld.Shapes.HasTitle Then
            If InStr(1, sld.Shapes.Title.TextFrame.TextRange.Text, "DRAFT", vbTextCompare) > 0 Then
                sld.Delete
            End If
        End If
    Next i
End Sub
```

Two If patterns to remember: `If ... Then ... End If` for multi-line blocks, and `If ... Then statement` (single line, no End If). `InStr` returns the position of a substring or 0 if absent. `vbTextCompare` makes the search case-insensitive.

**Try it now:** Run `BulkFindReplace` on a practice deck where you have manually typed "PRJ-111" on three different slides inside different shapes (title, body text box, and a table cell). Note: table cells are not reached via `TextFrame`; a real sweep also checks `shp.HasTable` and loops `shp.Table.Cell(r, c).Shape.TextFrame`. Extend the macro to handle that case.

---

## 8.7 Bulk Slide Generation from a List (and from Excel)

This is the payoff section: turning a list into finished slides.

### Generate from a list inside PowerPoint (array of fake data)

```vba
' Build one "Meet the Speaker" slide per entry in a VBA array
' Data is FAKE: YourCompany Inc sample speakers
Sub BulkSpeakerSlides()
    Dim names As Variant
    Dim titles As Variant
    Dim topics As Variant
    Dim times As Variant
    Dim i As Long
    Dim sld As Slide
    Dim deck As Presentation

    Set deck = Application.ActivePresentation

    ' Parallel arrays: index i lines up across all four (row i = one speaker)
    names = Array("Ada Exampleperson", "Bo Sampleson", "Cy Placeholder")
    titles = Array("VP of Sales", "Lead Engineer", "Customer Success Director")
    topics = Array("Territory Strategy", "Platform Deep Dive", "Renewals Playbook")
    times = Array("09:00-09:45", "10:00-10:45", "11:00-11:45")

    For i = 0 To UBound(names)
        ' Add a slide with the two-content-ish "Title Only" layout at the end
        Set sld = deck.Slides.Add(deck.Slides.Count + 1, ppLayoutTitleOnly)

        ' Name the slide so it is findable in the Selection Pane
        sld.Name = "Speaker_" & Replace(names(i), " ", "_")

        ' Title = speaker name
        sld.Shapes.Title.TextFrame.TextRange.Text = names(i)

        ' Body text box with the details, one line per property
        Dim tb As Shape
        Set tb = sld.Shapes.AddTextbox(msoTextOrientationHorizontal, 60, 160, 600, 200)
        With tb.TextFrame.TextRange
            .Text = titles(i) & vbCrLf & topics(i) & vbCrLf & "Session time: " & times(i)
            .Font.Name = "Segoe UI"
            .Font.Size = 20
            .Paragraphs(2).Font.Color.RGB = RGB(0, 74, 124)   ' highlight the topic
        End With
    Next i

    MsgBox UBound(names) + 1 & " speaker slides generated for the YourCompany kickoff."
End Sub
```

### Generate from Excel via early binding

Early binding means adding a reference to the Excel object library so the compiler knows its types. This gives you IntelliSense and compile-time checking.

**Steps to add the reference:** In the VBE, click **Tools > References**, scroll to **Microsoft Excel 16.0 Object Library** (the version number may differ), check it, click **OK**.

```vba
' Read rows from a workbook and build one slide per row.
' Workbook name and path are FAKE placeholders.
Sub BulkFromExcel()
    Dim xlApp As Object       ' declared As Object here only to keep the sample portable
    Dim wb As Workbook        ' early-bound type from the Excel reference
    Dim ws As Worksheet
    Dim r As Long
    Dim sld As Slide
    Dim tb As Shape

    ' Create a new hidden Excel instance (or use GetObject to attach to a running one)
    Set xlApp = CreateObject("Excel.Application")
    xlApp.Visible = False     ' run in the background; set True while debugging

    ' FAKE workbook name and path - replace with your own
    Set wb = xlApp.Workbooks.Open("C:\Users\Public\Documents\YourCompany-SpeakerList.xlsx")
    Set ws = wb.Worksheets("Speakers")

    ' Row 1 is the header; data starts at row 2. Column A=Name, B=Title, C=Topic, D=Time
    r = 2
    Do While ws.Cells(r, 1).Value <> ""
        Set sld = Application.ActivePresentation.Slides.Add( _
            Application.ActivePresentation.Slides.Count + 1, ppLayoutTitleOnly)

        sld.Shapes.Title.TextFrame.TextRange.Text = ws.Cells(r, 1).Value

        Set tb = sld.Shapes.AddTextbox(msoTextOrientationHorizontal, 60, 160, 600, 200)
        tb.TextFrame.TextRange.Text = ws.Cells(r, 2).Value & vbCrLf & _
                                      ws.Cells(r, 3).Value & vbCrLf & _
                                      "Session time: " & ws.Cells(r, 4).Value
        r = r + 1
    Loop

    ' Clean up the Excel instance so no orphan EXCEL.EXE lingers in Task Manager
    wb.Close SaveChanges:=False
    xlApp.Quit
    Set ws = Nothing: Set wb = Nothing: Set xlApp = Nothing

    MsgBox "Slides generated from the YourCompany speaker list."
End Sub
```

**Real-world example (YourCompany Inc):** Every Monday, `BulkFromExcel` runs against `YourCompany-SpeakerList.xlsx` (exported from the CRM) and produces the week's webinar deck skeleton in under 10 seconds. A human then spends their time on wording and visuals, not on text boxes.

**Try it now:** Create a workbook named `YourCompany-SpeakerList.xlsx` with a sheet named `Speakers`, headers `Name | Title | Topic | Time` in A1:D1, and three fake rows. Save the deck as .pptm, add the Excel reference, paste the macro, and run it. Verify three slides appear with correct content.

---

## 8.8 Formatting, Animations, and Exporting via VBA

### Colors, fonts, and positions

```vba
' Apply YourCompany brand standards across every slide
Sub BrandSweep()
    Dim sld As Slide
    Dim shp As Shape

    For Each sld In Application.ActivePresentation.Slides
        For Each shp In sld.Shapes
            ' Position the logo (named "BrandLogo") at the top-right, 0.5in margins
            If shp.Name = "BrandLogo" Then
                With Application.ActivePresentation.PageSetup
                    ' SlideWidth/SlideHeight are in points
                    shp.Left = .SlideWidth - shp.Width - 36   ' 36 pt = 0.5 inch
                    shp.Top = 36
                End With
            End If

            ' Normalize every text shape to the brand font and near-black text
            If shp.HasTextFrame Then
                If shp.TextFrame.HasText Then
                    shp.TextFrame.TextRange.Font.Name = "Segoe UI"
                    ' Skip titles so heading sizes are preserved
                    If Not (sld.Shapes.HasTitle) Then
                        shp.TextFrame.TextRange.Font.Color.RGB = RGB(33, 37, 41)
                    End If
                End If
            End If

            ' Re-tint any shape whose fill is old-brand teal to new-brand blue
            If shp.Fill.Visible = msoTrue Then
                If shp.Fill.ForeColor.RGB = RGB(0, 128, 128) Then   ' old teal
                    shp.Fill.ForeColor.RGB = RGB(0, 74, 124)        ' YourCompany blue
                End If
            End If
        Next shp
    Next sld
End Sub
```

Key facts: `RGB(red, green, blue)` takes 0-255 per channel; positions and sizes are in **points** (72 pt = 1 inch, 960x540 pt = a 16:9 slide at 13.33x7.5 inches); `Font.Name` sets the Latin typeface (use `Font.NameFarEast` for CJK text).

### Adding animations via VBA

Animations live on `Slide.TimeLine`. You build a **Sequence** of **Effect** objects. This is more verbose than the Animations pane, but it lets you animate 200 slides consistently.

```vba
' Fade in each bullet (each paragraph) of the body placeholder on click
Sub AnimateBullets()
    Dim sld As Slide
    Dim eff As Effect
    Dim body As Shape

    Set sld = Application.ActivePresentation.Slides(2)
    ' Assume the content placeholder is named "Content Placeholder 2" (check Selection Pane)
    Set body = sld.Shapes("Content Placeholder 2")

    ' Build one effect per paragraph for a by-paragraph build
    ' msoAnimEffectFade = 10 ; msoAnimTriggerOnPageClick = 1
    Dim i As Long
    For i = 1 To body.TextFrame.TextRange.Paragraphs.Count
        Set eff = sld.TimeLine.MainSequence.AddEffect( _
            Shape:=body, _
            effectId:=msoAnimEffectFade, _
            trigger:=msoAnimTriggerOnPageClick)
        ' Restrict the effect to just paragraph i (a text-level build unit)
        eff.EffectParameters.TextUnitEffect = msoAnimTextUnitEffectByParagraph
        eff.Timing.Duration = 0.5    ' half a second per fade
    Next i

    ' Add an Exit effect too: on the third click, fade the shape out
    Set eff = sld.TimeLine.MainSequence.AddEffect( _
        Shape:=body, effectId:=msoAnimEffectFade, trigger:=msoAnimTriggerOnPageClick)
    eff.Exit = msoTrue
End Sub
```

Also available: `eff.Timing.Duration` (seconds), `eff.EffectParameters.Direction`, and slide transitions via `sld.SlideShowTransition.EntryEffect` (for example `ppEffectFade`) with `sld.SlideShowTransition.AdvanceOnTime = msoTrue` and `AdvanceTime = 5` for auto-advancing kiosk decks.

### Exporting slides to images or PDF

```vba
' Export the whole deck to PDF and each slide to a PNG image folder
Sub ExportDeck()
    Dim deck As Presentation
    Dim sld As Slide
    Dim outFolder As String

    Set deck = Application.ActivePresentation
    ' FAKE output path - create the folder first
    outFolder = "C:\Users\Public\Documents\YourCompany-Exports\"

    ' 1) Whole deck to PDF (from slide 1 to the last slide, with metadata title)
    deck.ExportAsFixedFormat:=msoFalse  ' see corrected call below
    ' Correct signature: ExportAsFixedFormat(Path, FixedFormatType, Intent, FrameSlides, HandoutOrder, OutputType, PrintHiddenSlides, PrintRange, RangeType, SlideShowName, IncludeDocProperties, KeepIRMSettings, DocStructureTags, BitmapMissingFonts, UseISO19005_1)
    ' Simpler PDF route:
    deck.SaveAs outFolder & "Kickoff-Deck.pdf", ppSaveAsPDF

    ' 2) Every slide to PNG at 1600 pixels wide
    For Each sld In deck.Slides
        sld.Export outFolder & "Slide_" & Format(sld.SlideIndex, "00") & ".png", _
                   "PNG", 1600, 900
    Next sld

    MsgBox "Export complete: PDF plus PNG slides written to the YourCompany export folder."
End Sub
```

Note the two routes: `Presentation.SaveAs <path>, ppSaveAsPDF` is the simple way to write a PDF; `Slide.Export <path>, <filter>, <scaleWidth>, <scaleHeight>` writes one image per slide (filters: "PNG", "JPG", "BMP", "GIF", "TIF"). `Presentation.Export` (a method distinct from SaveAs and ExportAsFixedFormat) exports every slide as images in one call: `deck.Export outFolder, "PNG", 1600, 900`.

**Try it now:** Run `BrandSweep` on a deck where you deliberately used Times New Roman and teal fills, and verify everything normalizes. Then run `ExportDeck` and confirm a PDF and a numbered PNG set appear in your exports folder.

---

## 8.9 Error Handling Basics

Without error handling, the first problem stops your macro dead with a cryptic dialog. Two tiers of handling cover most automation.

### Tier 1: `On Error Resume Next` (use with care)

This tells VBA to skip any line that errors and continue. It is ideal for *optional* operations: deleting a shape that may not exist, applying a font that may not be installed, closing a workbook that may already be closed.

```vba
Sub SafeCleanup()
    Dim sld As Slide

    ' Resume Next ONLY around the risky optional action
    For Each sld In Application.ActivePresentation.Slides
        On Error Resume Next                    ' suppress the error...
        sld.Shapes("OldBanner").Delete          ' ...but ONLY this line can fail
        On Error GoTo 0                         ' IMMEDIATELY re-enable normal error reporting
    Next sld
End Sub
```

**The care instruction:** `On Error Resume Next` stays in effect until you turn it off with `On Error GoTo 0` or the Sub ends. If you leave it on for 200 lines, you will silently skip real bugs (a typo'd property name does nothing, and you never know why). The discipline: wrap the *smallest* possible region, then immediately `On Error GoTo 0`.

### Tier 2: `On Error GoTo` a handler (for reporting)

```vba
Sub GenerateDecksWithErrorReport()
    On Error GoTo Handler          ' any error jumps to the Handler label
    Dim i As Long
    Dim sld As Slide

    For i = 1 To 40
        Set sld = Application.ActivePresentation.Slides.Add( _
            Application.ActivePresentation.Slides.Count + 1, ppLayoutTitleOnly)
        sld.Shapes.Title.TextFrame.TextRange.Text = "YourCompany Rep Deck " & i
    Next i

    Exit Sub                       ' IMPORTANT: leave before falling into the handler

Handler:
    ' Err.Number and Err.Description capture what went wrong
    MsgBox "Generation stopped at rep " & i & "." & vbCrLf & _
           "Error " & Err.Number & ": " & Err.Description, vbExclamation
    Resume Next                    ' continue with the loop's next iteration
End Sub
```

Rules of thumb: every handler ends with `Resume Next` (continue), `Resume` (retry the failing line), or `Exit Sub` (stop); never let execution fall into a handler by accident (hence the `Exit Sub`); use `Err.Clear` if you check `Err.Number` repeatedly after `Resume Next`.

**Try it now:** Deliberately break `SafeCleanup` by misspelling a shape name while the error suppression is off, and watch the runtime error dialog. Then restore `On Error Resume Next` and confirm the macro completes silently. Notice how easy it is to hide a mistake: that is exactly why the suppression window must stay narrow.

---

## 8.10 Creating .ppam Add-ins and Where to Store Them

Once your macros prove useful, package them as a PowerPoint add-in (`.ppam`) so they are available in every deck without copying code around.

### Build the add-in

1. Start from a fresh presentation (or your macro library deck) containing all the Subs you want to ship, in one or two standard modules.
2. Open the VBE (Alt+F11), double-click `ThisPresentation`, and add an initializer if you want a custom toolbar or startup behavior:
   ```vba
   ' Runs automatically when PowerPoint loads this add-in
   Private Sub Presentation_Open()
       MsgBox "YourCompany Automation Pack loaded."   ' remove this once stable
   End Sub
   ```
3. Optional but recommended: add a custom ribbon/toolbar entry or at least document the macro names in a "How to run" text box in the source deck.
4. Go to **File > Save As**, choose the location, and set **Save as type** to **PowerPoint Add-in (*.ppam)**. Save as `YourCompany-Automation-Pack.ppam`.
5. PowerPoint saves the file and it is now a self-contained add-in.

### Where to store .ppam files

- **Default per-user location:** `%AppData%\Microsoft\AddIns` (for example `C:\Users\<you>\AppData\Microsoft\AddIns`). PowerPoint's Add-ins dialog looks here by default. Do not put real usernames in shared docs; this is just the standard path.
- **Shared/team location:** a read-only network folder such as `\\teamshare\YourCompany\AddIns\` that every user maps consistently.
- **Trusted location rule:** the folder holding your .ppam should also be a Trusted Location (section 8.2), or users will hit security prompts.

### Load the add-in

1. **Developer > Add-ins** (or **File > Options > Add-ins > Manage: PowerPoint Add-ins > Go**).
2. Click **Add New**, browse to `YourCompany-Automation-Pack.ppam`, click **OK**.
3. The add-in loads and its macros appear under **Developer > Macros**. Check **"Load behavior: Loaded"** and optionally "Load at startup" equivalent (add-ins in the list load automatically each session once added).

To update the add-in: unload it (**Remove** in the Add-ins dialog), edit the source deck's code, re-save as .ppam (same name), and add it again. Distribute updates by overwriting the .ppam in the shared folder.

**Real-world example (YourCompany Inc):** The enablement team ships `YourCompany-Automation-Pack.ppam` containing `BulkFromExcel`, `BrandSweep`, `SafeCleanup`, and `ExportDeck`. Everyone on the team loads it once; thereafter, any deck can be processed with a single macro run and no code copying.

**Try it now:** Turn your practice macros into `Practice-Pack.ppam`, save it to your AddIns folder, load it through the Add-ins dialog, close and reopen PowerPoint, and confirm the macros are still listed and runnable in a brand-new blank presentation.

---

## 8.11 When NOT to Use VBA (Use Design and Morph First)

Automation has a cost: code must be written, saved as .pptm or .ppam, debugged, and maintained. Before you write a line, rule out the built-in tools.

**Use the Design tab / Design Designer when:**
- You want a better-looking slide from existing content: **Design > Design Ideas (Designer)** proposes full layouts for free.
- You want consistent look across slides: apply a theme (**Design > Themes**) instead of code that sets fonts and colors one property at a time.

**Use Morph when:**
- You want an object to move smoothly between slides: duplicate the slide, move/resize the object on the copy, then **Transitions > Morph**. No animation code needed, and it is far more robust than animating positions with VBA.
- You want a "build-up" walkthrough of a diagram: arrange the intermediate states as slides and Morph between them.

**Use Replace/Selection Pane/Slide Master when:**
- A one-off text change across slides: **Home > Replace** does find-and-replace without code.
- Deleting or reordering a handful of slides: the slide sorter is faster than a Sub.
- Changing layout elements everywhere: edit the **Slide Master** (View > Slide Master) rather than looping over shapes.

**Use Excel/Word mail merge style tools when:**
- You are making one deck per person at small scale (2-5 copies): **File > Save a Copy** and the Replace feature beat writing and debugging a loop.

**Use VBA when:**
- The task repeats (weekly, monthly), the volume is high (20+ slides or 10+ decks), the rules are precise (exact colors, exact positions, exact text), or the source data is structured (a spreadsheet or CSV). Those are the four green lights.

**Decision shortcut:** If you can fully describe the task as "for each slide/row/shape, do X," it is automation territory. If the task needs judgment about visual balance, leave it to Design Designer and human taste.

**Try it now:** Take a plain three-bullet slide and improve it twice: once with **Design > Design Ideas**, and once by manually setting the font and colors. Time both. Now imagine doing the manual version 200 times. That comparison is your build-vs-automate decision tool.

---

## 8.12 PowerPoint + Excel Integration Patterns

PowerPoint rarely holds the master data; Excel does. Three proven integration patterns cover most real jobs.

### Pattern 1: PowerPoint reads Excel (data to slides)

Shown fully in section 8.7 (`BulkFromExcel`). Summary: create or attach to Excel with `CreateObject("Excel.Application")` or `GetObject(, "Excel.Application")`, open the workbook, loop rows, build slides. Always `Quit` and set variables to `Nothing` when you created the instance.

### Pattern 2: PowerPoint writes to Excel (slides to data)

```vba
' Inventory every slide into a workbook: one row per slide with title text and shape count
Sub DeckInventoryToExcel()
    Dim xlApp As Object
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim sld As Slide
    Dim r As Long

    Set xlApp = CreateObject("Excel.Application")
    xlApp.Visible = True
    Set wb = xlApp.Workbooks.Add
    Set ws = wb.Worksheets(1)

    ' Header row
    ws.Cells(1, 1).Value = "SlideIndex"
    ws.Cells(1, 2).Value = "SlideName"
    ws.Cells(1, 3).Value = "TitleText"
    ws.Cells(1, 4).Value = "ShapeCount"

    r = 2
    For Each sld In Application.ActivePresentation.Slides
        ws.Cells(r, 1).Value = sld.SlideIndex
        ws.Cells(r, 2).Value = sld.Name
        ' Guard: only read the title if the slide has one
        If sld.Shapes.HasTitle Then
            ws.Cells(r, 3).Value = sld.Shapes.Title.TextFrame.TextRange.Text
        Else
            ws.Cells(r, 3).Value = "(no title)"
        End If
        ws.Cells(r, 4).Value = sld.Shapes.Count
        r = r + 1
    Next sld

    ' FAKE save path for the exported inventory
    wb.SaveAs "C:\Users\Public\Documents\YourCompany-DeckInventory.xlsx"
    MsgBox "Inventory exported for the YourCompany deck."
End Sub
```

### Pattern 3: PowerPoint sends values to Excel formulas (numbers to models)

Finance decks often compute in Excel and present in PowerPoint. The pattern: open the model workbook, write scenario inputs into designated input cells (for example `ws.Range("B3").Value = 125000`), let Excel recalc (`xlApp.Calculate`), read the result cells (`ws.Range("B9").Value`), and write those results into chart labels or KPI text boxes on the slide. This keeps every formula in Excel (maintainable, auditable) and leaves PowerPoint purely presentational.

### Integration hygiene rules

- Never hard-code a path with a real username in shared code; use `Environ$("USERPROFILE")` or a configuration cell/named range to hold paths.
- Always clean up: `wb.Close False`, `xlApp.Quit`, `Set ... = Nothing`, otherwise orphan `EXCEL.EXE` processes accumulate.
- Prefer early binding (Tools > References) for development, and note that shipping to machines with different Office versions sometimes means late binding (`Dim wb As Object`) is the safer distribution choice.
- Wrap the whole integration in the Tier 2 error handler from section 8.9, so a missing workbook reports cleanly instead of crashing mid-generation.

**Try it now:** Run `DeckInventoryToExcel` on your practice deck and verify the workbook row count equals your slide count and every title is captured (or "(no title)" appears correctly). Then modify it to also dump each slide's first body text into a fifth column.

---

## Practice Projects (5)

Each project builds on the section noted. All data must be fictional (YourCompany Inc).

**Project 1: The Slide Factory**
Build a macro that generates 10 agenda slides from a VBA array of fake agenda items (item name, owner, minutes), each slide titled "Agenda Item N" with a formatted body box.
*Success criteria:* Running the macro once adds exactly 10 slides; running it again adds 10 more (it is repeatable and does not error); every body box uses Segoe UI 20 pt; item titles appear in the slide title placeholder.

**Project 2: The Brand Guardian**
Write `BrandSweepV2`: normalize all text to Segoe UI, recolor any shape fill that is not brand blue RGB(0, 74, 124) or white to brand blue, and reposition any shape named "BrandLogo" to top-right 0.5 inch margins on every slide.
*Success criteria:* On a deliberately messy 5-slide deck (wrong fonts, teal fills, logo misplaced), one run leaves zero non-brand fonts, zero teal fills, and the logo correctly placed on all 5 slides; running it twice produces no change (idempotent) and no errors.

**Project 3: The Monday Deck (Excel to PowerPoint)**
Create `YourCompany-SpeakerList.xlsx` (sheet `Speakers`, columns Name/Title/Topic/Time, 8 fake rows) and a macro using the Excel object library that produces one slide per row, names each slide `Speaker_<Name>`, and adds a per-slide fade animation on the body text.
*Success criteria:* 8 slides generated with correct content, slide names visible in the Selection Pane, each body text box has a Fade entrance effect, and the Excel instance fully exits (no orphan EXCEL.EXE in Task Manager).

**Project 4: The Distribution Kit**
Extend Project 3's flow to export the finished deck: one PDF of the whole deck plus one PNG per slide named `Slide_01.png`, `Slide_02.png`, ... into `C:\Users\Public\Documents\YourCompany-Exports\` (create the folder from code if missing using `MkDir`).
*Success criteria:* PDF exists and opens with the right slide count; PNG count equals slide count; filenames are zero-padded and sequential; re-running overwrites without erroring.

**Project 5: The Automation Pack**
Package your best three macros into `YourCompany-Automation-Pack.ppam`, saved in your AddIns folder, loaded via the Add-ins dialog.
*Success criteria:* After a full PowerPoint restart, the macros list under Developer > Macros in a brand-new blank presentation; each macro runs successfully on an unrelated deck; a colleague-style test (unload, re-add from the folder) works; a short README module (a "How to use" slide inside the source deck) documents each macro's purpose.

---

## Common Mistakes & Pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Saving macro code in a .pptx | All code is silently discarded on save | Save as .pptm (or .ppam for add-ins) BEFORE writing code |
| Forgetting `Set` for object variables | "Object required" or "ByRef argument type mismatch" errors | Use `Set x = <object expression>`; plain `=` is only for values |
| Deleting slides/shapes in a forward loop | Indexes shift as items are removed, so you skip items or error out | Loop backwards: `For i = count To 1 Step -1` |
| `Select`/`Selection` recorded code (recorder habits) | Fails when no window/selection is active; breaks in batch runs | Reference objects directly: `deck.Slides(3).Shapes(1)...` |
| Leaving `On Error Resume Next` on for whole procedures | Real bugs vanish silently; you ship broken output | Wrap only the risky line(s), then immediately `On Error GoTo 0` |
| Assuming shapes have text | `TextFrame.TextRange` errors on pictures and many autoshapes | Guard with `If shp.HasTextFrame Then If shp.TextFrame.HasText Then` |
| Ignoring tables, grouped shapes, and charts in sweeps | Bulk edits silently miss content | Also check `shp.HasTable` (loop cells), `shp.GroupItems` for groups, and `shp.HasChart` |
| Writing VBA for what Morph/Designer does in 2 clicks | Unmaintainable code for a solved problem | Rule out Design Designer, Morph, Replace, and Slide Master first (section 8.11) |
| Orphan Excel instances from `CreateObject` | Hidden EXCEL.EXE processes accumulate and lock files | Always `wb.Close False`, `xlApp.Quit`, `Set ... = Nothing` |
| Hard-coded file paths with real usernames | Breaks on every other machine; leaks identity in shared code | Use `Environ$("USERPROFILE")`, config cells, or trusted shared folders |
| Forgetting `Exit Sub` before a handler label | Execution falls into the handler after normal completion | Always `Exit Sub` (or `Exit Function`) on the line above the handler |
| Animating 200 slides by hand instead of by `TimeLine` code | Hours of clicking and inconsistent timings | Loop `sld.TimeLine.MainSequence.AddEffect` with fixed `Timing.Duration` |
| Not naming generated slides | Generated decks are impossible to navigate or debug | Set `sld.Name = "Prefix_" & key` as you create each slide |
| Trusting the macro recorder as a learning tool in PowerPoint | It captures almost nothing of the object model | Learn via the Immediate window and the object model map (section 8.4) |

---

## Key Takeaways

1. Automate only repetition at scale: if the task is "for each slide/row/shape, do X" and repeats weekly or covers 20+ items, VBA wins; otherwise use Design Designer, Morph, Replace, or the Slide Master.
2. File format first: save as .pptm (or .ppam for add-ins) before writing any code, or you will lose it.
3. PowerPoint's macro recorder is nearly useless for learning; the object model (Application > Presentation > Slide > Shape > TextFrame, plus TimeLine/Sequence for animation) is the real map.
4. `For Each` loops over `Slides` and `Shapes` are the workhorse; loop backwards when deleting, and always guard text access with `HasTextFrame` / `HasText`.
5. `Set` is mandatory for object variables; `Dim` plus `Set` is the pair that prevents the most common runtime errors.
6. Error handling has two tiers: narrow `On Error Resume Next` for optional actions (turn it off immediately with `On Error GoTo 0`), and `On Error GoTo Handler` with `Exit Sub` before the label for reporting and recovery.
7. Bulk generation from a list (arrays inside VBA, or rows in Excel via early binding) turns a 25-minute Monday chore into seconds, and idempotent macros can be run repeatedly without damage.
8. Formatting, colors (RGB), positions (points, 72 per inch), per-paragraph animations (`TimeLine.MainSequence.AddEffect`), and exports (`SaveAs ... ppSaveAsPDF`, `Slide.Export`) are all scriptable, making brand governance and distribution fully automatable.
9. Package proven macros as a .ppam in `%AppData%\Microsoft\AddIns` (or a shared trusted folder) so every deck can use them without code copying.
10. PowerPoint + Excel integration follows three patterns: Excel to slides (data to visuals), slides to Excel (inventory/audit), and values to Excel formulas (models compute, slides present). Always clean up Excel instances.

---

## Further Learning

- Microsoft PowerPoint support and how-to documentation: https://support.microsoft.com/en-us/powerpoint
- Microsoft Learn training path for PowerPoint: https://learn.microsoft.com/en-us/training/
- Microsoft Create templates and design resources (starter decks for your automation targets): https://create.microsoft.com/
