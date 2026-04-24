# Module 2 — Instructor Notes: Attack-Path Modeling and Breach Forecasting

## Prerequisites check

Before running this module, students should be comfortable
with: Python, pandas, scikit-learn, Git, the command line, and
the Module 1
material.

## Pacing

| Segment             | Time   | Notes |
|---------------------|--------|-------|
| Concept lecture     | 60 min | Use `slides.ipynb` with RISE. |
| Worked example      | 30 min | Walk through the prose chapter examples. |
| Lab kickoff         | 15 min | Run the **ANUBIS** lab / IDE live with students. |
| Office hours        | —      | Expect questions about the adversarial / edge cases. |

## Common pitfalls

- Students conflate detection metrics (precision vs. recall vs.
  FPR) without considering deployment cost. Reinforce the
  cost-weighted framing early.
- Students sometimes treat ANUBIS/CI failures as grades rather
  than signals. Emphasize the push-and-iterate loop.

## Discussion prompts

- Where have you seen attack graphs and shortest-path-to-impact analysis in your own workplace?
- Where have you seen bayesian networks for compromise propagation in your own workplace?
- Where have you seen time-series forecasting of breach likelihood in your own workplace?
- Where have you seen communicating uncertainty to non-technical stakeholders in your own workplace?

## ANUBIS lab / autograde notes

The module lab is assessed on **ANUBIS**. The test file lives at
`anubis/assignments/module-2-lab/assignment.py`. If you
update tests mid-term, remember to:

1. `publish` per Castalia’s ANUBIS runbook (not the NYU *Anubis LMS* `sync`).
2. Trigger `Regrade All` from the admin panel.
