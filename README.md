# AINS6302 AI for Risk Assessment

Unified MyST Jupyter Book for `AINS6302 AI for Risk Assessment`, part of the
**Cybersecurity AI** specialization (AINS6300–AINS6302) in the
Aurnova MSAI program.

Teaches AI-based risk modeling and predictive analysis for cybersecurity decision-making. Covers quantitative risk (FAIR), vulnerability prioritization, attack-path analysis on graphs, and forecasting breach likelihood under uncertainty.

## Structure

```
intro.md              # Book landing page
syllabus.md           # Full syllabus
anubis.md             # Anubis LMS integration guide
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
  module-1-lab.ipynb  # Graded lab (Anubis)
  module-2-lab.ipynb
anubis/               # Anubis autograde assignment tree
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

## Anubis autograder

This repository is marked as a **GitHub template**. The Anubis
deployment at <https://anubis.castalia.institute> generates a
private student repository from this template. When students push
code, Anubis runs the autograde pipeline defined in `anubis/`.

See [`anubis.md`](anubis.md) for the instructor workflow
(`anubis assignment init`, `anubis assignment sync`) and the
student workflow (repo is provisioned, push to grade).

## Licensing

Content &copy; Castalia Institute. Used under license by Aurnova
University for the MSAI program. See `LICENSE` for details.
