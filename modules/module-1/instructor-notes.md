# Module 1 — Instructor Notes: Quantitative Risk and Vulnerability Prioritization

## Prerequisites check

Before running this module, students should be comfortable
with: Python, pandas, scikit-learn, Git, the command line, and
the Module prerequisite-course
material.

## Pacing

| Segment             | Time   | Notes |
|---------------------|--------|-------|
| Concept lecture     | 60 min | Use `slides.ipynb` with RISE. |
| Worked example      | 30 min | Walk through the prose chapter examples. |
| Lab kickoff         | 15 min | Run the Anubis IDE live with students. |
| Office hours        | —      | Expect questions about the adversarial / edge cases. |

## Common pitfalls

- Students conflate detection metrics (precision vs. recall vs.
  FPR) without considering deployment cost. Reinforce the
  cost-weighted framing early.
- Students sometimes treat Anubis failures as grades rather
  than signals. Emphasize the push-and-iterate loop.

## Discussion prompts

- Where have you seen the fair model: loss event frequency and magnitude in your own workplace?
- Where have you seen cvss, epss, and the kev catalog — what each actually measures in your own workplace?
- Where have you seen monte carlo simulation of annualized loss in your own workplace?
- Where have you seen prioritization as a budgeted optimization problem in your own workplace?

## Anubis autograde notes

The module lab is graded by Anubis. The test file lives at
`anubis/assignments/module-1-lab/assignment.py`. If you
update tests mid-term, remember to:

1. `anubis assignment sync` from an Admin IDE.
2. Trigger `Regrade All` from the admin panel.
