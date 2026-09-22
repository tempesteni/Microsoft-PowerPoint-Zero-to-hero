# PowerPoint Flashcards for Anki

120 ready-made flashcards covering the full "PowerPoint Zero to Hero" curriculum.

## 1. Install Anki

Download Anki for free at <https://apps.ankiweb.net/> and install it (Windows, macOS, or Linux).

## 2. Import the deck

1. Open Anki and create or select a profile.
2. Go to **File > Import...** and choose `powerpoint-flashcards.csv`.
3. In the import dialog, set the field mapping exactly as below.

## 3. Field mapping

| CSV column | Anki field   | Notes                                        |
|------------|--------------|----------------------------------------------|
| Front      | Field 1      | The question / prompt (front of card)         |
| Back       | Field 2      | The answer (back of card)                     |
| Category   | Field 3: Tags| Lowercase hyphenated topic tags               |

Recommended import settings:

- Type: **Basic**
- Deck: create a new deck named `PowerPoint Zero to Hero`
- Check **"Allow HTML in fields"** (not required, but harmless)
- Field separator: **Comma**
- Check the preview to confirm every card splits into 3 fields, then click **Import**.

## 4. Study tip

Set new cards to **5 per day** and let spaced repetition do its work. Review every day
(Anki schedules cards just before you forget them), and hit "Again" honestly when you
miss one. Steady daily review beats cramming: 5 cards a day finishes the deck in
24 days and keeps ~90% retention long term.

## 5. Card count by category

| Category (tag)        | Cards |
|-----------------------|-------|
| fundamentals          |    15 |
| design-foundations    |    12 |
| visual-design         |    18 |
| tables-charts         |    18 |
| animations            |    16 |
| media-interactivity   |    14 |
| delivery-accessibility|    12 |
| vba                   |    10 |
| design-principles     |     5 |
| **Total**             | **120** |

Filter by tag in Anki (for example `tag:animations`) to drill a single topic before
working through that section of the course.
