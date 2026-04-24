# `anubis/` — ANUBIS lab and autograde bundle

**ANUBIS** = **Android NetHunter Unified Breach Intelligence System** — Castalia’s **AI + Kali NetHunter** platform, served from [anubis.castalia.institute](https://anubis.castalia.institute).

This directory is **not** related to the NYU *Anubis LMS* open-source autograder. It is the versioned **lab + autograde** material that the ANUBIS control plane uses for course code `ains6302`.

- `assignments/module-N-lab/` — one folder per graded lab: `assignment.py`, `meta.yml`, `Dockerfile` (or equivalent OCI), `test.sh`, `pipeline` hooks.
- Instructors **publish** updates through Castalia’s ANUBIS deployment (admin + runbook) so the live workers match the `main` branch here.
