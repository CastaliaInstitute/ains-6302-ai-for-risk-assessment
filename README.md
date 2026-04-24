# AINS6302 AI for Risk Assessment

Unified MyST Jupyter Book for `AINS6302 AI for Risk Assessment`, part of the
**Cybersecurity AI** specialization (AINS6300–AINS6302) in the
Aurnova MSAI program.

Teaches AI-based risk modeling and predictive analysis for cybersecurity decision-making. Covers quantitative risk (FAIR), vulnerability prioritization, attack-path analysis on graphs, and forecasting breach likelihood under uncertainty.

## Structure

```
intro.md              # Book landing page
syllabus.md           # Full syllabus
anubis.md             # ANUBIS = Android NetHunter Unified Breach Intelligence System (Kali NetHunter + AI)
modules/
  module-1/           # Quantitative Risk and Vulnerability Prioritization
    overview.md
    book-prose.md
    assignment.ipynb
    slides.ipynb
    narration.md
    instructor-notes.md
  module-2/           # Attack-Path Modeling and Breach Forecasting
    ...
notebooks/
  module-1-lab.ipynb  # Graded lab (ANUBIS)
  module-2-lab.ipynb
anubis/               # ANUBIS autograde / lab bundle
  assignments/
    module-1-lab/
    module-2-lab/
```

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html
```

## Export Formats

- `make html` builds the web version
- `make pdf` builds the LaTeX-based PDF export
- `make epub` builds the EPUB export

## Publishing

Push to `main` to publish the book via GitHub Pages.

## ANUBIS (Kali NetHunter + AI)

**ANUBIS** (Android NetHunter Unified Breach Intelligence System) is Castalia’s lab and breach-intelligence platform, served from <https://anubis.castalia.institute>. It is our **AI + [Kali NetHunter](https://www.kali.org/docs/nethunter/)** stack, **not** the unrelated NYU *Anubis LMS*.

This repository is a **GitHub template**. ANUBIS (or a Castalia course bot tied to it) can generate per-student private repositories from that template. When students push, the **ANUBIS** worker runs the tests and scoring hooks in `anubis/assignments/`.

See [`anubis.md`](anubis.md) for how Castalia **publishes** labs to the ANUBIS control plane and how the student `push` → `grade` loop works (our runbook, **not** the public NYU `anubis assignment` CLI).

## Licensing

Content &copy; Castalia Institute. Used under license by Aurnova
University for the MSAI program. See `LICENSE` for details.
