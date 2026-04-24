# Anubis LMS Integration

This course is delivered through [Anubis LMS](https://anubis.castalia.institute)
as course code `ains6302`. Anubis autogrades student submissions
and provides a Cloud IDE so students do not need to install anything
locally.

## Architecture

```
[this repo]  ──(GitHub template)──▶  [student repo]
     │                                     │
     │  anubis/assignments/*                │  student pushes code
     ▼                                     ▼
[anubis assignment sync]             [Anubis pipeline]
     │                                     │
     └────▶ registers assignment ─────────┘
                  in ains6302
```

## Instructor workflow

From an Anubis Admin IDE at
<https://anubis.castalia.institute/admin/ide>:

1. Clone this repo inside the Admin IDE.
2. `cd anubis/assignments/module-1-lab`
3. Edit `assignment.py` to implement or extend the test cases.
4. Edit `meta.yml` to set release and due dates.
5. Run `anubis assignment sync` to push the assignment into the
   `ains6302` course.
6. Confirm the assignment appears at
   <https://anubis.castalia.institute/courses/ains6302>.

## Student workflow

1. Log in to <https://anubis.castalia.institute> and select
   `ains6302`.
2. Anubis generates a private GitHub repository for you from this
   template.
3. Open the Anubis Cloud IDE or clone locally.
4. Complete the lab notebook under `notebooks/module-N-lab.ipynb`.
5. Commit and push. Anubis runs the autograde pipeline and posts
   results to your Anubis dashboard before the deadline.
6. Late work is controlled by the `grace_date` in `meta.yml`.

## What Anubis grades

Anubis executes the tests in `anubis/assignments/module-N-lab/assignment.py`.
Those tests run the student's notebook (or extracted code) through
`exec_as_student(...)` and score the outputs. See
<https://anubis-lms.io/docs/autograding.html> for the full API.

## Manual regrade

If tests change mid-term, an instructor can trigger `Regrade All`
from the Anubis admin panel for this course; queued jobs re-run
every student submission against the new tests.
