# Module 06: Media & Interactivity

**Module number:** 06
**Title:** Media & Interactivity
**Level:** Advanced
**Prerequisites:** Modules 01-05 (interface basics, slide creation, text and shapes, images and icons, themes and layouts). A working microphone and (optionally) speakers or headphones. Sample video and audio files help but are not required.
**Estimated study time:** 90-120 minutes (plus project work)
**Next module:** 07 - Collaboration & Review (or the next module in your learning path)

This module turns a static slide deck into a rich, self-guided experience. You will embed and edit video, add narration and music, record your screen, wire up hyperlinks and action buttons, build interactive navigation with Zoom slides, create audience-specific Custom Shows, run kiosk-style self-playing presentations, export decks as MP4 or GIF, and make all of it accessible.

---

## 1. Inserting Video: This Device, Online, and Stock

**What it is.** PowerPoint lets you embed video from three sources: files saved on your computer ("This Device"), streamed online video (YouTube and other web sources), and Microsoft's built-in Stock Videos library. An embedded video becomes part of the .pptx file (when inserted from this device), while online video stays a live web link that needs an internet connection during the show.

**Step-by-step (video from this device):**
1. Select the slide where the video should appear.
2. Go to `Insert > Video > This Device`.
3. Browse to your file (MP4 is the safest format; MOV and AVI also work but are larger) and click `Insert`.
4. Drag the video frame into position and resize from the corner handles so it does not distort.
5. A new `Playback` tab appears in the ribbon whenever the video is selected.

**Step-by-step (online video):**
1. In your browser, copy the embed link or page URL of the video (for YouTube, use `Share > Copy` or copy the URL from the address bar).
2. In PowerPoint: `Insert > Video > Online Video`.
3. Paste the URL into the dialog and press `Enter` or click the search icon.
4. Select the thumbnail that appears and click `Insert`. The video frame shows a poster thumbnail with a play overlay.

**Step-by-step (stock video):**
1. `Insert > Video > Stock Videos`.
2. Search or browse categories (backgrounds, nature, technology, and so on).
3. Select one or more clips and click `Insert`. Stock clips are licensed for use in documents and presentations.

**Real-world examples.**
- *Business:* YourCompany Inc's quarterly review opens with a 20-second stock clip of a city skyline while music plays, then transitions to the agenda.
- *Education:* A biology teacher embeds a short cell-division clip from this device so it plays even if the classroom Wi-Fi fails.
- *Personal:* A wedding slideshow includes an online video message from a relative who could not attend.

**Format tips.** MP4 with H.264 video and AAC audio is the most compatible combination across Windows, Mac, and exported video. If a video refuses to play, re-encode it to MP4 with a free tool rather than fighting codecs.

**Try it now.** Insert any MP4 from your device on a blank slide, then insert one Stock Video on another slide. Compare the two: click each and note which ribbon tabs (`Video Format`, `Playback`) appear and whether the stock clip behaves differently from your file.

---

## 2. Video Editing: Trimming, Fade In/Out, and Poster Frames

**What it is.** PowerPoint includes a lightweight video editor so you do not need external software for common fixes: trimming off the dead seconds at the start or end, softening abrupt starts and stops with fades, and choosing the still frame that shows before playback (the poster frame).

**Step-by-step (trim):**
1. Select the video, then open the `Playback` tab.
2. Click `Trim Video`. The Trim Video dialog opens with a timeline.
3. Drag the green `Start Marker` and red `End Marker` to the moments you want, or type exact `Start Time` and `End Time` values (format MM:SS.t).
4. Click `Play` inside the dialog to preview, then `OK`. The original file is untouched; only the playback window changes.

**Step-by-step (fade in and fade out):**
1. With the video selected, open `Playback`.
2. Set `Fade In` (for example 1.00 second) and `Fade Out` (for example 1.50 seconds) in the editing group.
3. Preview in Slide Show mode (`F5`) to judge the feel. Short fades (0.5-2 seconds) look professional; long fades feel sluggish.

**Step-by-step (poster frame):**
1. Select the video and open `Playback > Poster Frame` (or `Video Format > Poster Frame` depending on version).
2. Choose `Image from File`, `Stock Images`, `Online`, or `Capture from Current Frame`. "Capture from Current Frame" grabs the frame currently shown under the playhead, which is ideal after trimming to the perfect moment.
3. The chosen still is what your audience sees before anyone presses play.

**Real-world examples.**
- *Business:* Trim a 3-minute product demo down to the 45 seconds that matter, add a 1-second fade in, and set the poster frame to the hero shot of the product.
- *Education:* Trim a recorded lab demonstration to just the experiment portion so class time is not wasted scrubbing.
- *Personal:* Set the poster frame of a travel video to the best sunset shot so the deck looks polished even if nobody plays the clip.

**Try it now.** Trim 5 seconds off the start of any video, add a 1-second fade in and 1-second fade out, and set the poster frame to a captured frame near the middle. Present the slide and watch how much more polished the clip feels.

---

## 3. Video Playback Options

**What it is.** The `Playback` tab controls how a video behaves during the show: whether it plays automatically or waits for a click, whether it expands to full screen, whether it loops, and whether the frame is hidden between plays. Getting these right is what separates a deck that "just works" from one where the presenter scrambles to find the play button live.

**The Playback ribbon controls:**
- `Start:` dropdown with `In Click Sequence`, `Automatically`, and `When Clicked On`. "In Click Sequence" plays when you advance to the animation step; "Automatically" plays as soon as the slide appears; "When Clicked On" waits for a click on the video object itself.
- `Play Full Screen:` the video expands to fill the entire screen during playback, then returns to the slide.
- `Loop until Stopped:` repeats the clip endlessly until you press `Esc` or advance.
- `Hide While Not Playing:` makes the video frame invisible except during playback (great for background loops).
- `Rewind after Playing:` snaps back to the start when finished, so a second play begins from the top.
- `Volume:` Low, Medium, High, or Mute.

**Step-by-step (auto-playing full-screen clip):**
1. Select the video, open `Playback`.
2. Set `Start > Automatically`.
3. Check `Play Full Screen`.
4. Optionally check `Loop until Stopped` and `Rewind after Playing`.
5. Test with `Slide Show > From Current Slide` (or `Shift+F5`).

**Step-by-step (click-to-play clip):**
1. Select the video, open `Playback`.
2. Set `Start > When Clicked On` so only a click on the video itself triggers it, and ordinary slide-advance clicks do not.
3. Enlarge the video frame to make the click target obvious.

**Animation tab alternative.** For finer control, select the video and open the `Animations` tab: the `Play`, `Pause`, and `Stop` effects can be added to the Animation Pane and triggered by click or by "With Previous"/"After Previous" for choreographed playback with animations.

**Real-world examples.**
- *Business:* A looping muted product video ("Hide While Not Playing" off, "Loop until Stopped" on) runs behind a trade-show kiosk slide.
- *Education:* A vocabulary video is set to "When Clicked On" so the teacher controls exactly when it plays during discussion.
- *Personal:* A highlight reel plays full screen automatically the moment its slide appears at a family reunion.

**Try it now.** Set one video to start automatically, loop, and play full screen. Then duplicate the slide and change it to "When Clicked On" with no full screen. Present both slides and feel the difference in control.

---

## 4. Inserting Audio: Music, Narration, and Sounds

**What it is.** PowerPoint supports audio in three roles: background music that spans slides, recorded narration (voice-over) per slide or for the whole deck, and sound effects triggered by clicks. The `Insert > Audio` menu offers `Audio on My PC`, `Stock Audio` (in current versions), and `Record Audio` (a quick in-app voice memo).

**Step-by-step (music that plays across slides):**
1. `Insert > Audio > Audio on My PC`, pick your MP3 or WAV, and click `Insert`. A speaker icon appears with a progress bar below it.
2. With the audio selected, open the `Playback` tab.
3. Set `Start > Play in Background` (this one-click preset sets automatic start, "Play Across Slides", "Loop until Stopped", and "Hide During Show"), or configure manually:
   - `Start > Automatically`
   - Check `Play Across Slides`
   - Check `Loop until Stopped` for long background loops
   - Check `Hide During Show` to hide the speaker icon
4. Set `Volume > Low` or `Medium` so music never drowns out a presenter or narration.

**Step-by-step (record narration per slide):**
1. Go to `Slide Show > Record Slide Show` (choose `Record from Current Slide` or `Record from Beginning`).
2. The Recording Studio view opens with a camera preview (toggle it off if unwanted), a big red `Record` button, and per-slide notes.
3. Click `Record`, speak for the current slide, then advance with the arrow keys or on-screen arrows. Timings and ink are captured too.
4. Click `Stop`, review with `Play`, then `Close` (X). Each slide now holds a narration audio object and an advance timing.
5. Selectively delete narration on a slide by selecting the speaker icon it contains and pressing `Delete`.

**Step-by-step (quick inline recording):**
1. `Insert > Audio > Record Audio`, name the clip, click `Record`, speak, click `Stop`, then `OK`. Useful for one-line verbal notes or a spoken greeting.

**Sound on click.** Select any shape or icon, then `Insert > Action > Play sound` and pick a built-in sound or `Other Sound` for your own file. This ties audio to a specific interactive object (covered further in Section 7).

**Real-world examples.**
- *Business:* YourCompany Inc's leave-behind deck has narration on every slide so prospects can "attend" the pitch asynchronously.
- *Education:* A flipped-classroom lecture records explanations over each slide; students watch at home and arrive ready for exercises.
- *Personal:* A memorial slideshow plays one meaningful song across all slides at low volume.

**Try it now.** Record a one-sentence narration on two consecutive slides with `Record Slide Show`, then play the two slides in Slide Show mode and confirm the audio advances automatically with the timings. Next, insert any music file and set it to `Play in Background` at low volume.

---

## 5. Compressing Media

**What it is.** Media bloat is the number-one cause of giant, slow, unemailable decks. A handful of untrimmed 1080p clips can push a .pptx past 200 MB. Compressing media re-encodes every embedded audio and video file at a lower quality tier and discards trimmed portions.

**Step-by-step:**
1. Go to `File > Info`.
2. Click `Compress Media` (it only appears when the presentation contains media). Choose a quality level:
   - `Full HD (1080p)` - quality preserved for large screens.
   - `HD (720p)` - the sweet spot for laptops, projectors, and webinars.
   - `Standard (480p)` - smallest files, fine for email attachments and on-screen review.
3. PowerPoint processes each clip and reports the before/after size per media item and in total. Keep the dialog open to compare.
4. Save the file (`Ctrl+S`). Note: compression is lossy. Save a copy first if you may need original quality later (`File > Save a Copy`).

**Related size hygiene.** Deleting cropped image areas (`File > Options > Advanced > Image Size and Quality > Discard editing data`) and avoiding embedded duplicate clips both shrink files. Trim first, then compress: trimmed-away footage is discarded during compression, compounding the savings.

**Real-world examples.**
- *Business:* A 185 MB partner deck compresses to 31 MB at HD so it passes the mail server's 50 MB limit.
- *Education:* A lecture deck with 12 embedded clips drops from 400 MB to 60 MB so it loads fast on school tablets.
- *Personal:* A vacation slideshow shrinks enough to upload to shared cloud storage without hitting quota.

**Try it now.** Open any deck with video, note its file size on the `File > Info` screen, run `Compress Media` at `Standard (480p)`, and record the new total. Undo is not available after saving, so work on a copy.

---

## 6. Screen Recording and Screenshots

**What it is.** PowerPoint's built-in screen recorder captures part or all of your screen with optional narration and drops the result straight onto the current slide as an editable video. The Screenshot tool grabs any open window or a custom region and inserts it as a picture. Both avoid the "export from another tool, then import" dance.

**Step-by-step (screen recording):**
1. Go to `Insert > Screen Recording` (on the `Insert` tab, far right).
2. PowerPoint minimizes and shows a dock at the top of the screen: `Record` (red circle), `Stop`, `Select Area`, `Audio` toggle, `Record Pointer` toggle.
3. Click `Select Area` and drag a marquee around the region you want (a browser window, a spreadsheet, a demo app). If you skip this, the entire screen is captured.
4. Turn `Audio` on if you want voice-over from your microphone. Note: PowerPoint's screen recorder captures microphone audio, not system audio, in most configurations; narrate rather than relying on app sounds.
5. Click `Record` (or press `Win+Shift+R`). Perform the demo. Pause with `Win+Shift+U` if needed.
6. Stop with `Win+Shift+Q` or the dock's `Stop` button. The capture appears on the current slide as a video object.
7. Trim, fade, and set playback exactly as in Sections 2 and 3.

**Step-by-step (screenshot):**
1. `Insert > Screenshot`.
2. Pick a window from the `Available Windows` gallery for a clean instant capture, or click `Screen Clipping` to drag-select a region of the last active window (PowerPoint minimizes while you clip).
3. The result is a picture: crop it (`Picture Format > Crop`), add a border, or apply a shadow like any image.

**Real-world examples.**
- *Business:* Record a 60-second walkthrough of YourCompany Inc's internal dashboard so sales reps can embed it in proposals.
- *Education:* Capture the exact dialog boxes of a statistics tool step by step so students can compare their screens to yours.
- *Personal:* Screenshot a booking confirmation and clip just the reservation number region for a trip-planning deck.

**Try it now.** Use `Insert > Screenshot > Screen Clipping` to grab one region of any open app. Then use `Insert > Screen Recording` to record 10 seconds of mouse movement over that app with audio off, and trim the clip to 5 seconds.

---

## 7. Hyperlinks: Internal, External, and Email

**What it is.** A hyperlink turns any text, shape, or picture into a clickable jump: to another slide in the deck, to a web page, to another file, or to an email compose window. Hyperlinks are the simplest building block of interactive, non-linear decks.

**Step-by-step (link to another slide):**
1. Select text or an object.
2. Press `Ctrl+K` (or `Insert > Link`).
3. Under `Link to:`, choose `Place in This Document`.
4. Pick the target slide from the list (best from `Slide Titles` view) and click `OK`.
5. Test in Slide Show mode: clicking the object jumps to that slide.

**Step-by-step (link to a web page):**
1. Select the object or text, press `Ctrl+K`.
2. Choose `Existing File or Web Page`, type or paste a full URL including `https://`, click `OK`.
3. Ctrl+click behavior: in Normal view links require Ctrl+click to follow; in Slide Show mode a plain click works.

**Step-by-step (email link):**
1. `Ctrl+K > E-mail Address`.
2. Type the address (for example `sales@yourcompany.example`) and an optional subject.
3. Clicking it in Slide Show mode opens the audience member's mail client with the fields prefilled.

**Clean design without underlines.** Hyperlinked text is underlined and recolored by the theme by default, which looks noisy in large doses. For clean looks:
- Apply links to whole shapes instead of text (`Ctrl+K` with the shape selected): no underline, and the click target is much bigger.
- Or select linked text, then `Home > Text Shadow`/font color adjustments to restyle it. To fully control link colors, edit theme colors: `Design > Variants > Colors > Customize Colors`, and set `Hyperlink` and `Followed Hyperlink` to tasteful tones (for example dark blue and gray).
- Shape buttons with a short label ("Learn more", "See pricing") read better than raw URLs printed on the slide.

**Tip: ScreenTips.** In the `Insert Hyperlink` dialog, click `ScreenTip` and type a short hover description ("Opens our pricing page"). It helps in kiosk mode.

**Real-world examples.**
- *Business:* YourCompany Inc's proposal deck links each agenda item to its detail slide, and the closing slide has one large "Email us" button.
- *Education:* A course overview links each topic card to the slide section that covers it, letting students jump to what they need.
- *Personal:* A recipe deck links each course to its full-page recipe slide.

**Try it now.** On one slide, add a rounded rectangle labeled "Next topic" and hyperlink it to slide 3 of your deck. Then add text reading "Contact us", hyperlink it to an email address with a subject line, and restyle it so no underline shows. Test both in Slide Show mode.

---

## 8. Action Buttons and Action Settings

**What it is.** Action buttons are ready-made shapes (arrows, home, information, film, sound, and so on) that come pre-wired with an action: jump to next/previous/first/last slide, open a URL, run a program, play a sound, or run a macro. `Action Settings` exposes the same wiring for any shape or object you already have, so your own brand-styled buttons can behave like action buttons.

**Step-by-step (insert an action button):**
1. `Insert > Shapes` and scroll to the `Action Buttons` category at the bottom of the gallery.
2. Draw the button (for example `Action Button: Home`) on the slide.
3. The `Action Settings` dialog opens automatically. Choose the `Mouse Click` tab (and optionally `Mouse Over` for hover behavior).
4. Select `Hyperlink to` and pick `Next Slide`, `Previous Slide`, `First Slide`, `Last Slide`, `End Show`, `Custom Show`, `URL`, `Other PowerPoint Presentation`, or `Other File`.
5. Optionally check `Play sound` and pick a sound. Click `OK`.

**Step-by-step (wire an existing shape):**
1. Select your own rounded rectangle or icon.
2. Go to `Insert > Action` (the `Action Settings` dialog opens with identical options).
3. Set `Hyperlink to > Slide...` and pick an exact target slide for full control.
4. Repeat the button on the Slide Master (`View > Slide Master`) so navigation appears on every slide automatically.

**Real-world examples.**
- *Business:* A self-running booth deck gets a persistent "Menu" home button on every slide so staff can reset it to the main menu between visitors.
- *Education:* Quiz slides use "Next question" and "Answer" buttons wired to hidden answer slides.
- *Personal:* A digital guestbook at a party has a "Sign the form" button that jumps to the feedback slide.

**Try it now.** Insert an `Action Button: Back or Previous` and wire it to `Previous Slide`. Add a second shape of your own design and use `Insert > Action` to wire it to `First Slide`. Present and click both.

---

## 9. Zoom Navigation: Slide Zoom, Section Zoom, Summary Zoom

**What it is.** Zoom (Insert > Zoom) creates thumbnail navigation that lets a presenter dive into slides or whole sections and return to an overview, like a mini website inside your deck. There are three types: `Slide Zoom` (jump to specific slides), `Section Zoom` (jump into a whole section and return), and `Summary Zoom` (PowerPoint auto-builds a menu slide of your sections). Note: Zoom is a modern PowerPoint feature; it exists in PowerPoint 2019/365 on Windows and Mac, and Zoom links degrade gracefully to ordinary jumps in older versions.

**Step-by-step (Section Zoom, the most common):**
1. Organize your deck into sections first: right-click between slides in the thumbnail pane and choose `Add Section` (for example "Products", "Pricing", "Team").
2. `Insert > Zoom > Section Zoom`.
3. Check the sections you want and click `Insert`. Thumbnail cards appear on the current slide.
4. Arrange the cards into a menu grid. With a card selected, the `Zoom` tab offers:
   - `Zoom Background` (makes the card's slide background transparent so thumbnails sit cleanly on your design).
   - `Return to Zoom` (checked: after showing that section, you bounce back to the menu; unchecked: you continue to the next slide).
   - `Change Image` (swap the thumbnail for a branded picture).
5. Resize and style the cards like pictures (borders, shadows, soft edges).

**Step-by-step (Slide Zoom):** `Insert > Zoom > Slide Zoom`, check individual slides, click `Insert`. Ideal for "choose your own topic" menus and Q&A jump lists.

**Step-by-step (Summary Zoom):** `Insert > Zoom > Summary Zoom`, choose sections, click `Insert`. PowerPoint creates a new summary slide with clickable section thumbnails, typically placed at the start of the summarized content.

**Real-world examples.**
- *Business:* YourCompany Inc's product menu slide shows four section thumbnails; a salesperson clicks "Pricing" only for price-sensitive buyers, then returns to the menu via `Return to Zoom`.
- *Education:* A revision deck is a summary zoom of five topic sections so each student navigates to their weak areas.
- *Personal:* A travel album menu zooms into "Lisbon", "Porto", and "Food" sections on demand.

**Try it now.** Add three sections to a deck with 2-3 slides each. Insert a `Summary Zoom` on slide 1, enable `Zoom Background` and `Return to Zoom`, then present: click into a section and confirm you return to the menu when the section ends.

---

## 10. Custom Shows: One Deck, Many Audiences

**What it is.** A Custom Show is a named subset of your slides stored inside the same file. Instead of maintaining separate decks for executives, engineers, and partners (and letting them drift out of sync), you keep one master deck and define a Custom Show per audience. Shows can be launched manually or via hyperlink, and can loop.

**Step-by-step (create a Custom Show):**
1. `Slide Show > Custom Slide Show > Custom Shows...`.
2. Click `New`. Name it (for example `Exec Briefing`).
3. In `Slides in presentation`, check the slides to include. Use `Up`/`Down` arrows to set their order (the show order can differ from deck order).
4. Click `OK`, then create another show (for example `Technical Deep Dive`) the same way. Close the dialog.

**Step-by-step (run and link a Custom Show):**
- Run it directly: `Slide Show > Custom Slide Show` and click the show's name.
- Link to it: on a shape, `Insert > Action > Hyperlink to > Custom Show`, pick the show, and decide whether `Show and return` (bounce back to the launching slide) is checked. This is how menu slides offer "5-minute version" and "20-minute version" buttons.

**Real-world examples.**
- *Business:* One YourCompany Inc master deck feeds three shows: `Exec Briefing` (6 slides), `Technical Deep Dive` (18 slides), `Partner Overview` (10 slides). Content edits once, propagate everywhere.
- *Education:* A teacher keeps one course deck and defines `Lesson 1`, `Revision`, and `Exam Prep` shows for different class days.
- *Personal:* A wedding reel has `Kids version` (fun photos only) and `Full story` shows.

**Try it now.** Create two Custom Shows from an existing deck: `Short` (3 slides) and `Long` (6 slides including those 3). Then add two buttons on slide 1, each with `Insert > Action > Hyperlink to > Custom Show` and `Show and return` enabled, and test both paths.

---

## 11. Kiosk Mode: Self-Running Decks

**What it is.** Kiosk mode turns a presentation into a self-contained interactive display for trade-show booths, reception areas, museum-style exhibits, and touch screens. In kiosk mode the deck runs full screen, mouse clicks do NOT advance slides (so random visitors cannot break the flow), and navigation happens only through your hyperlinks, action buttons, and Zoom menus. You can also make decks self-advancing with automatic timings.

**Step-by-step (enable kiosk mode):**
1. Go to `Slide Show > Set Up Slide Show`.
2. Under `Show type`, select `Browsed at a kiosk (full screen)`.
3. Optionally set `Loop continuously until 'Esc'` (usually implied by kiosk mode) and choose `Using timings, if present` under `Advance slides`.
4. Click `OK`. Start the show with `F5` and press `Esc` to exit.

**Step-by-step (auto-advance timings):**
1. `Transitions` tab, in the `Timing` group set `Advance Slide > After:` to a duration (for example `00:05.00` for 5 seconds).
2. Click `Apply To All` to set every slide, or set per slide for varied pacing (longer on dense slides).
3. Alternatively, use `Slide Show > Rehearse Timings` to record natural pacing by talking through the deck, then save the timings when prompted.

**Step-by-step (hidden slides):** Right-click a slide thumbnail > `Hide Slide`. Hidden slides are skipped in the show but reachable via hyperlink or action button, perfect for optional deep-dive slides.

**Real-world examples.**
- *Business:* YourCompany Inc's booth screen loops a kiosk deck with a Zoom menu, so visitors tap topics of interest and it never drifts to a broken state.
- *Education:* An open-day display runs a self-advancing 2-minute loop on a hallway screen with narration.
- *Personal:* A digital photo frame at home runs a looping slideshow with 6-second timings.

**Try it now.** Set all slides to advance after 3 seconds, enable `Browsed at a kiosk (full screen)`, and press `F5`. Confirm ordinary clicks do nothing, then press `Esc` to exit. Add one action button wired to `End Show` so users have an exit affordance if a human operator is nearby.

---

## 12. Export to Video (MP4) and GIF

**What it is.** You can turn a finished deck into a standalone video file: MP4 for full narrated walkthroughs (with audio and timings), or animated GIF for short loops to drop into chat, email, or a web page. Export is the natural end-point of this module: narrate, compress, then ship as a file anyone can play without PowerPoint.

**Step-by-step (export MP4):**
1. `File > Export > Create a Video` (or `File > Save As` and pick `MP4`/`MOV` from the file type dropdown).
2. Choose quality: `Full HD (1080p)` for large screens, `HD (720p)` for email and web, `Ultra HD (4K)` when detail matters.
3. Set `Use Recorded Timings and Narrations` (this includes your `Record Slide Show` narration and per-slide timings). If you have none, choose `Seconds spent on each slide` and type a default like 5.
4. Click `Create Video`, choose a filename and location, and click `Save`.
5. A progress bar appears on the status bar. Rendering is not instant: a 20-slide narrated deck can take several minutes. Wait for the bar to finish before opening the file.

**Step-by-step (export GIF):**
1. `File > Export > Create an Animated GIF`.
2. Choose a quality tier (Small, Medium, Large, Extra Large). The dialog shows approximate dimensions and a size estimate.
3. Set `Seconds spent on each slide` and whether to `Use Recorded Timings and Narrations` (narration is ignored in GIF, since GIF is silent).
4. Click `Create GIF`, pick a location, and save. For loops, the GIF repeats when embedded in web pages and chat tools that loop GIFs.

**Real-world examples.**
- *Business:* YourCompany Inc exports its narrated pitch to MP4 and posts it in the company LinkedIn feed and on the sales portal.
- *Education:* A teacher exports the lecture deck to MP4 so absent students can catch up, and exports a 3-slide GIF of the molecule animation for the class group chat.
- *Personal:* A birthday slideshow becomes an MP4 shared with family abroad.

**Try it now.** Take a 3-slide deck with narration, export it as `HD (720p)` MP4 using recorded timings, and play the result in a media player. Then export the same deck as a `Medium` GIF and check how much larger GIFs are per second of motion.

---

## 13. Media Accessibility: Captions and Alt Text

**What it is.** Accessible media means every viewer, including people who cannot hear audio or see a video frame clearly, can get the content. The two pillars are captions/subtitles for audio-visual material and alt text for every meaningful visual object. PowerPoint offers live AI-driven captions and subtitles in Slide Show mode (when connected to the internet) and manual alt text everywhere.

**Step-by-step (live captions and subtitles):**
1. Go to `Slide Show > Always Use Subtitles` to enable subtitles for every show.
2. Next to it, set `Subtitle Settings`: choose `Spoken Language` (what the presenter speaks) and `Subtitle Language` (what appears on screen).
3. Choose where captions appear: `Below Slide` (default, keeps slide content clear) or `Overlaid on Slide` (bottom or top of the slide).
4. Start the show: PowerPoint transcribes the microphone in real time and displays captions. An internet connection and a clear microphone improve accuracy substantially.

**Step-by-step (narration captions in exported video):** For precise captions in an MP4 export, narrate with `Record Slide Show`, then open `Insert > Captions` workflows available in current versions (for example `Insert > Video > Caption Insert` styles) or produce a caption sidecar file (VTT/SRT) and add it when publishing to platforms like YouTube, LinkedIn, or Stream, which render caption tracks on top of the MP4.

**Step-by-step (alt text on media and visuals):**
1. Right-click any video frame, audio icon, picture, chart, SmartArt, or shape and choose `Edit Alt Text` (or `Alt Text` in the right-click menu / `Accessibility` ribbon tab).
2. Describe the content and function in one or two sentences ("Bar chart showing Q1-Q4 revenue rising from 2.1 to 3.4 million US dollars"). For decorative shapes, check `Mark as decorative`.
3. Use the `Accessibility Checker`: `File > Info > Check for Issues > Check Accessibility`. It lists missing alt text, unclear link text (avoid "click here"), and reading order problems. Fix items in the pane that opens.

**Audio alternatives.** For sound-on-click cues, also give a visual signal (an animation or a text note), since not everyone perceives audio cues.

**Real-world examples.**
- *Business:* YourCompany Inc turns on subtitles for every webcast and runs the Accessibility Checker before sending decks to government clients with procurement accessibility requirements.
- *Education:* Captions let a hard-of-hearing student follow the live lecture; alt text on diagrams lets a screen-reader user study the exported handout.
- *Personal:* Alt text descriptions make a grandparent's photo slideshow meaningful to a blind family member listening with a screen reader.

**Try it now.** Enable `Always Use Subtitles`, present one slide while speaking for 15 seconds, and watch the captions appear. Then run `File > Info > Check for Issues > Check Accessibility` on a deck with two images and fix every flagged item.

---

## Practice Projects

Complete all five to consolidate the module. Each builds on skills from earlier sections.

**Project 1: The Multimedia Sales Pitch (video + audio + compression)**
Build an 8-slide YourCompany Inc sales deck that includes: one stock video as an intro background, one device video trimmed to 30 seconds with fade in/out and a custom poster frame, and low-volume background music playing across all slides.
*Success criteria:* (1) Video starts automatically, does not play full screen, has a 1-second fade in and 1.5-second fade out. (2) Poster frame is not the default first frame. (3) Music plays across slides, loops, and is hidden during the show. (4) File is under 50 MB after `Compress Media` at HD (720p). (5) Deck plays end to end with no clicks except slide advances.

**Project 2: The Screen-Recorded How-To (screen recording + narration)**
Produce a 5-slide tutorial deck teaching any software task, with a screen recording of the process embedded and trimmed to 60 seconds or less, narration recorded on at least three slides via `Record Slide Show`, and a screenshot with a caption callout.
*Success criteria:* (1) Recording was captured at `Select Area` scope (not the whole desktop) and trimmed to the essential steps. (2) Narration and slide timings are synchronized when played back. (3) Screenshot region excludes desktop clutter. (4) Exported as MP4 with `Use Recorded Timings and Narrations` and the audio is audible in the result.

**Project 3: The Interactive Menu (hyperlinks + action buttons + Zoom)**
Create a 12-slide interactive menu deck with three sections, a landing slide containing a Summary Zoom (or a hand-built menu of three shape buttons), `Return to Zoom` enabled, and a persistent `Home` action button on every slide (place it on the Slide Master).
*Success criteria:* (1) Every menu item reaches its section and the viewer returns to the menu afterward. (2) The Home button works from every slide. (3) Menu buttons are shapes with hyperlink-free clean text (no underlines anywhere in the deck). (4) At least one email link with a subject line exists on the final slide. (5) A tester who has never seen the deck can navigate to any section and back within 10 seconds.

**Project 4: The Audience-Switcher (Custom Shows + kiosk mode)**
From one master deck of at least 12 slides, define three Custom Shows (`Exec` 4 slides, `Technical` 8 slides, `Full` all slides) and a launcher slide with three action buttons (`Hyperlink to > Custom Show`, `Show and return` checked). Configure the deck to run in kiosk mode with 5-second auto-advance timings.
*Success criteria:* (1) Each button runs only its show and returns to the launcher. (2) In kiosk mode, raw mouse clicks do not advance or break the show. (3) The deck loops continuously until `Esc`. (4) One slide is hidden yet reachable via hyperlink. (5) Editing one slide's text visibly updates all three shows (proving single-source content).

**Project 5: The Accessible Video Handout (captions + alt text + export)**
Take any existing deck and make it publication-ready: enable `Always Use Subtitles` with correct spoken/subtitle languages, add alt text to every picture, chart, and video, mark decorative shapes as decorative, fix every `Check Accessibility` finding, then export as MP4 and as GIF.
*Success criteria:* (1) Accessibility Checker reports zero errors. (2) All alt text is descriptive (conveys data or meaning, not just "image1"). (3) Subtitles display correctly during a live slide show. (4) The MP4 export is HD (720p) or better and under 100 MB. (5) The GIF loops and is sized `Medium` or `Large`, and you can name one appropriate and one inappropriate use case for it.

---

## Common Mistakes & Pitfalls

| Mistake | Why it hurts | Fix |
|---|---|---|
| Embedding raw, untrimmed 1080p clips | Deck balloons to hundreds of MB; crashes on weak machines | Trim first (`Playback > Trim Video`), then `File > Info > Compress Media` at HD or 480p |
| Forgetting that online video needs internet | Clip shows a broken frame live on stage | Use `This Device` embeds for critical content; test online video on venue Wi-Fi |
| Default poster frame is an awkward first frame | Deck looks unprofessional before anyone presses play | `Playback > Poster Frame > Capture from Current Frame` after trimming |
| Setting `Start > In Click Sequence` and expecting autoplay | Video waits for a click and stalls the presenter | Use `Automatically` for autoplay, `When Clicked On` for deliberate playback |
| Music volume too loud over narration | Audience cannot hear the speaker or voice-over | `Playback > Volume > Low`, and mute music when narrating live |
| Hyperlinks underlined everywhere | Slides look like a 2005 web page | Link whole shapes instead of text; recolor theme `Hyperlink`/`Followed Hyperlink` colors |
| Links to guessed or copied-but-unchecked URLs | 404s in front of an audience | Type full URLs including `https://` and test every link in Slide Show mode before presenting |
| No navigation affordance in kiosk mode | Visitors get stuck on one slide | Add action buttons (`Home`, `Next`) and Zoom menus; always include an `End Show` or `Home` control |
| No `Return to Zoom` on section menus | Presenter dives into a section and has to scroll back manually | Check `Return to Zoom` on every Zoom card in menu slides |
| Compressing media before trimming | Trimmable footage is re-encoded and kept, wasting size | Trim first, compress second; then `Save` and re-check size on `File > Info` |
| Separate copies of the deck per audience | Versions drift; wrong deck shown to the wrong crowd | One master deck with Custom Shows per audience |
| Exporting video without timings/narration setting | Silent MP4 with 5-second flat slides | Choose `Use Recorded Timings and Narrations` in `File > Export > Create a Video` |
| GIF used for long narrated content | Huge file, no audio possible | GIF only for short silent loops (under ~30 seconds); use MP4 for everything else |
| Alt text missing or useless ("photo", "chart1") | Screen reader users get nothing | Describe content and takeaway ("Line chart of monthly signups doubling from Jan to Jun"); mark decoration as decorative |
| Narration left on a slide after a live rehearsal | Audio plays unexpectedly during a live talk | Delete narration per slide (select the speaker icon and `Delete`) or use `Slide Show > Set Up Slide Show > Show without narration` |
| Screen recording captures the entire desktop | Notifications and personal files leak into the video | Always use `Select Area` on the target window before `Record` |

---

## Key Takeaways

- Embed critical video from `This Device` (MP4/H.264) and treat online video as an internet-dependent bonus.
- Trim first, fade second, set the poster frame third, compress last: that order produces the smallest, most polished media.
- `Playback` settings (`Automatically` vs `When Clicked On`, `Play Full Screen`, `Loop until Stopped`, `Hide While Not Playing`, `Rewind after Playing`) define how a clip behaves during a live show; always test them in Slide Show mode.
- `Play in Background` is the one-click path for music across slides; `Record Slide Show` is the reliable path for narration and slide timings.
- `Insert > Screen Recording` with `Select Area` produces editable, trimmable demo videos without leaving PowerPoint.
- Hyperlinks and action buttons are the primitives of interactivity: wire them to slides, Custom Shows, URLs, and email, and style them as shapes to keep slides clean (no underlines).
- Zoom navigation (`Slide Zoom`, `Section Zoom`, `Summary Zoom` with `Return to Zoom`) creates menu-driven, non-linear presentations; organize slides into sections first.
- Custom Shows keep one source of truth for many audiences; kiosk mode (`Set Up Slide Show > Browsed at a kiosk`) makes decks click-proof and self-running with `After:` timings.
- Export narrated decks as MP4 (`Use Recorded Timings and Narrations`) and short silent loops as GIF.
- Accessibility is part of media work: enable subtitles, write real alt text, and clear the Accessibility Checker before sharing.

---

## Further Learning

- PowerPoint support hub (videos, how-tos, and captions/topics on media and slide shows): https://support.microsoft.com/en-us/powerpoint
- Microsoft Learn training for PowerPoint: https://learn.microsoft.com/en-us/training/
- Microsoft Create (templates and inspiration for video-rich and interactive decks): https://create.microsoft.com/

Tip: on the PowerPoint support hub, use the site search for `video`, `screen recording`, `kiosk`, or `accessibility` to reach the exact article you need without guessing deep links.
