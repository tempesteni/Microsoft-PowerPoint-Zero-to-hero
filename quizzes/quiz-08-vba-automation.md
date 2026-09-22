# Quiz 8: VBA Automation

**Module tested:** Module 8: VBA Automation (Developer tab, macro security, file formats, VBE, object model, Subs, variables, loops, conditions, bulk generation, error handling, limits)

**Instructions**

- Answer all 15 multiple-choice questions in Section A (3 points each) and complete the 5 practical challenges in Section B (5 points each).
- Questions 13-15 are short code-reading items: read the Sub and pick what it does.
- Time yourself: 50 minutes total. For Section B, type the code yourself and run it before checking the model solutions.
- All fictional data uses the company "YourCompany Inc".

**Scoring**

| Total points | Percentage | Result |
|---|---|---|
| 63-70 | 90%+ | Advance to the next module |
| 49-62 | 70-89% | Review your weak areas, then retake |
| Below 49 | Below 70% | Restudy the module before retaking |

---

## Section A: Multiple Choice (15 questions, 3 points each = 45 points)

Difficulty legend: **E** = easy, **M** = medium, **H** = hard.

**1. (E)** How do you enable the Developer tab on the ribbon?

- A) It appears automatically when you open any .pptm file
- B) File > Options > Customize Ribbon, then check Developer in the right-hand list
- C) Insert > Get Add-ins, search for "Developer"
- D) Review > Protect > Show Developer

**2. (E)** A saved presentation contains VBA code that must run next week. Which file extension must it use?

- A) .pptx
- B) .pptm
- C) .pdf
- D) .potx

**3. (E)** What is a .ppam file?

- A) A video export of a presentation
- B) A PowerPoint add-in file, typically used to distribute macros so they are available in every presentation
- C) A read-only handout template
- D) A compressed picture format

**4. (E)** What is the Visual Basic Editor (VBE)?

- A) The Notes pane in PowerPoint
- B) The separate window (Alt+F11) where you write, edit, and run VBA code
- C) A slide layout for code screenshots
- D) The Accessibility Checker's text mode

**5. (E)** Which VBA statement stores a reference to a slide in a variable named `sld`?

- A) `Dim sld As Slide`
- B) `Set sld = ActivePresentation.Slides(2)`
- C) `sld = ActivePresentation.Slides(2)`
- D) `Dim Set sld = Slide`

**6. (E)** In the PowerPoint object model, which object is the parent container of all slides?

- A) `Presentation`
- B) `Shape`
- C) `Comment`
- D) `Selection`

**7. (M)** Lina recorded a macro but wants to see and edit its code. Where does she go first?

- A) File > Options > Trust Center > Macro Settings
- B) Developer tab > Macros (or Alt+F8), select the macro, then click Edit to open the VBE
- C) Home > Replace > search for the macro name
- D) Slide Show > Rehearse Timings

**8. (M)** What is the purpose of macro security settings (Trust Center)?

- A) To make macros run faster
- B) To control which macros are allowed to run, protecting the machine from malicious code in downloaded files
- C) To convert VBA to JavaScript
- D) To password-protect slide content

**9. (M)** Which declaration correctly creates a variable that holds a reference to a TextFrame's text range?

- A) `Dim txt As String`
- B) `Dim rng As TextRange`
- C) `Dim txt As TextFrame`
- D) `Dim rng As Shape`

**10. (M)** What is the main structure of a Sub procedure?

- A) `Sub Name() ... End Sub` containing statements that perform an action when run
- B) `Function Name() ... End Function` only, since Subs cannot be run from PowerPoint
- C) `If Name Then ... End If`
- D) `For Each Name In Slides ... Next`

**11. (M)** When should you reach for VBA instead of manual editing?

- A) When you need to change one slide's title
- B) When you must repeat a mechanical task across many slides, such as generating 40 data slides from a table
- C) When you want better visual design for a single chart
- D) When you must deliver a deck in 5 minutes and have never used VBE

**12. (M)** Why is error handling (`On Error GoTo` / `MsgBox`) added to presentation macros?

- A) It makes the code compile in older PowerPoint versions
- B) It lets the macro report a clear message and stop cleanly instead of crashing with a cryptic run-time error
- C) It disables macro security
- D) It encrypts the VBA project

**13. (H, code reading)** What does this Sub do?

```vba
Sub FormatTitles()
    Dim sld As Slide
    For Each sld In ActivePresentation.Slides
        sld.Shapes(1).TextFrame.TextRange.Font.Bold = True
    Next sld
End Sub
```

- A) Deletes the first shape on every slide
- B) Bolds the text of the first shape on every slide
- C) Bolds only the title of the current slide
- D) Adds a new shape to every slide and bolds it

**14. (H, code reading)** What does this Sub do?

```vba
Sub AddStamps()
    Dim i As Integer
    For i = 1 To 3
        ActivePresentation.Slides.Add 1, ppLayoutBlank
        ActivePresentation.Slides(1).Shapes.AddTextbox( _
            msoTextOrientationHorizontal, 100, 100, 300, 50) _
            .TextFrame.TextRange.Text = "YourCompany Inc"
    Next i
End Sub
```

- A) Adds 3 blank slides at the beginning and puts a "YourCompany Inc" text box on each
- B) Adds 1 slide with 3 text boxes
- C) Replaces all text in the deck with "YourCompany Inc"
- D) Adds 3 text boxes to the current slide only

**15. (H, code reading)** What happens when this Sub runs?

```vba
Sub FixLabels()
    Dim sld As Slide
    For Each sld In ActivePresentation.Slides
        If sld.Shapes(1).HasTextFrame Then
            sld.Shapes(1).TextFrame.TextRange.Text = "Approved"
        End If
    Next sld
End Sub
```

- A) Every slide's first shape is deleted
- B) The first shape on each slide is renamed "Approved" in the Selection Pane
- C) On each slide, if the first shape can hold text, its text is replaced with "Approved"
- D) The macro fails because `If` cannot be used inside `For Each`

---

## Section B: Practical Challenges (5 tasks, 5 points each = 25 points)

Write and run real VBA in the VBE. Score yourself 1 point per verified success criterion. Use only "YourCompany Inc" as sample data.

**B1. Macro setup.** (a) Enable the Developer tab. (b) Create a new presentation and save it as "Q8 Automation.pptm". (c) Insert a standard module in the VBE and write a Sub named `HelloBox` that shows a message box with the text "YourCompany Inc automation online". (d) Run it from the Macros dialog and verify the box appears.

**B2. Loop over slides.** Write a Sub named `StampFooter` that uses a `For Each` loop to add the text "YourCompany Inc - Confidential" into a small text box at the bottom of every slide in the active presentation. Success: run it on a 3-slide test deck and see the text on all 3 slides.

**B3. Variables and Set.** Write a Sub named `SetTitle` that declares a `Slide` variable and a `String` variable with `Dim`, uses `Set` to point the slide variable at slide 1, and writes the string "Quarterly Kickoff" into the slide's title (or first text shape). Success: running it updates slide 1 visibly.

**B4. Conditional bulk build.** Write a Sub named `BuildAgenda` that loops 5 times and adds a new title-and-content slide each iteration, numbering each slide title "Agenda Item 1" through "Agenda Item 5". Inside the loop, use an `If` block so that when the number is 5 the body text reads "Wrap-up and Q&A" and otherwise it reads "Topic " & the number. Success: 5 new slides appear with the right titles and body text.

**B5. Error handling and judgment.** (a) Add `On Error GoTo ErrHandler` to `SetTitle` from B3 so that if the slide has no title placeholder, a `MsgBox` reports "No title found on this slide" instead of crashing; test it on a slide with no title. (b) In 3-4 sentences, name two situations where you should NOT use VBA and say what to do instead.

---

## Answer Key

*WARNING: spoilers below. Do not scroll past this line until you have finished and self-scored.*

**Section A answers**

1. **B** - The Developer tab is hidden by default and is turned on via File > Options > Customize Ribbon with the Developer checkbox.
2. **B** - VBA is only saved in macro-enabled formats: .pptm for presentations (or .ppam for add-ins); .pptx silently discards code.
3. **B** - A .ppam is an add-in package, the standard way to distribute macros so they load with PowerPoint and can serve all decks.
4. **B** - The VBE is the separate development window, opened with Alt+F11 or Developer > Visual Basic, where modules and code live.
5. **B** - Object references are assigned with `Set`; `Dim` only declares the variable's type, and `sld = ...` without `Set` is an object-assignment error.
6. **A** - The hierarchy runs Application > Presentation > Slide > Shape > TextFrame > TextRange, so `Presentation` contains the `Slides` collection.
7. **B** - Developer > Macros (Alt+F8) lists all macros; selecting one and clicking Edit jumps into the VBE at its code.
8. **B** - Trust Center macro settings control whether macros are disabled, enabled with notification, or trusted, blocking malicious code in files from the internet.
9. **B** - Text inside shapes is manipulated through a `TextRange` object (`Shape.TextFrame.TextRange`), so the variable is declared `As TextRange`.
10. **A** - A Sub is declared `Sub Name()` and closed with `End Sub`; it performs actions and can be run from the Macros dialog or assigned to a shape.
11. **B** - VBA pays off for repetitive mechanical work across many slides; one-off changes are faster by hand, and last-minute decks are a bad time to learn VBE.
12. **B** - `On Error GoTo` traps failures so the macro can explain the problem and exit gracefully instead of stopping with an unhandled run-time error.
13. **B** - The `For Each` visits every slide and `Shapes(1).TextFrame.TextRange.Font.Bold = True` bolds the text in the first shape on each one (the title in a standard layout).
14. **A** - The `For i = 1 To 3` loop runs 3 times; each iteration inserts a blank slide at position 1 and adds one text box containing "YourCompany Inc".
15. **C** - Inside the loop, the `If` checks `HasTextFrame` and only then replaces that shape's text with "Approved"; `If` is perfectly legal inside `For Each`.

**Section B model solutions**

**B1.** File > Options > Customize Ribbon > check Developer. Save As > "Q8 Automation.pptm" (choose PowerPoint Macro-Enabled Presentation). In VBE: Insert > Module, then type:

```vba
Sub HelloBox()
    MsgBox "YourCompany Inc automation online"
End Sub
```

Back in PowerPoint, Alt+F8 > HelloBox > Run. Score: 1 pt Developer tab visible, 1 pt saved as .pptm, 1 pt module with the Sub, 1 pt code compiles, 1 pt message box appears.

**B2.**

```vba
Sub StampFooter()
    Dim sld As Slide
    For Each sld In ActivePresentation.Slides
        sld.Shapes.AddTextbox(msoTextOrientationHorizontal, _
            100, 500, 400, 30).TextFrame.TextRange.Text = _
            "YourCompany Inc - Confidential"
    Next sld
End Sub
```

Score: 1 pt `Dim sld As Slide`, 1 pt `For Each ... Next`, 1 pt AddTextbox with a bottom-of-slide position, 1 pt correct text, 1 pt runs on all 3 slides.

**B3.**

```vba
Sub SetTitle()
    Dim sld As Slide
    Dim title As String
    Set sld = ActivePresentation.Slides(1)
    title = "Quarterly Kickoff"
    sld.Shapes(1).TextFrame.TextRange.Text = title
End Sub
```

(Using `sld.Shapes.Title.TextFrame.TextRange.Text = title` is also correct when a title placeholder exists.) Score: 1 pt `Dim` both variables, 1 pt `Set` used for the slide reference, 1 pt string assigned to the variable, 1 pt writes into the slide's title/first shape, 1 pt runs successfully.

**B4.**

```vba
Sub BuildAgenda()
    Dim i As Integer
    Dim sld As Slide
    For i = 1 To 5
        Set sld = ActivePresentation.Slides.Add( _
            ActivePresentation.Slides.Count + 1, ppLayoutText)
        sld.Shapes.Title.TextFrame.TextRange.Text = "Agenda Item " & i
        If i = 5 Then
            sld.Shapes(2).TextFrame.TextRange.Text = "Wrap-up and Q&A"
        Else
            sld.Shapes(2).TextFrame.TextRange.Text = "Topic " & i
        End If
    Next i
End Sub
```

Score: 1 pt `For i = 1 To 5` loop, 1 pt adds a slide each iteration, 1 pt numbered titles, 1 pt `If ... Then ... Else` block, 1 pt correct body text (item 5 differs).

**B5.** (a)

```vba
Sub SetTitle()
    Dim sld As Slide
    On Error GoTo ErrHandler
    Set sld = ActivePresentation.Slides(1)
    sld.Shapes.Title.TextFrame.TextRange.Text = "Quarterly Kickoff"
    Exit Sub
ErrHandler:
    MsgBox "No title found on this slide"
End Sub
```

Test on a blank-layout slide with no title placeholder: the message box appears and the macro stops cleanly. (b) Model answer for the judgment part: do not use VBA for one-off design tweaks (restyling a single slide is faster by hand in Normal view), and do not use VBA when a built-in feature already does the job (exporting PDF or running the Accessibility Checker are one-click commands). Do not use it either when the deck must be handed to users whose security policy blocks macros: build the content manually or deliver a .pptx/.pdf instead. Score: 1 pt `On Error GoTo` label present, 1 pt `MsgBox` in the handler, 1 pt `Exit Sub` before the handler, 1 pt tested on a no-title slide, 1 pt two sensible "do not use VBA" cases with alternatives.

**Section A: 45 points. Section B: 25 points. Total: 70 points.**
