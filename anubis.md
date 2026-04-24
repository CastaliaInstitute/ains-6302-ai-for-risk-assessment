# ANUBIS (Android NetHunter Unified Breach Intelligence System)

**ANUBIS** is Castalia’s **AI + [Kali NetHunter](https://www.kali.org/docs/nethunter/)** platform: the **Android NetHunter Unified Breach Intelligence System**, deployed at [anubis.castalia.institute](https://anubis.castalia.institute).

> **Not** the unrelated open-source *Anubis LMS* (NYU) autograder used in some CS programs. In Castalia, **ANUBIS** is our breach-intelligence and hands-on security environment—NetHunter-class offensive tooling, unified telemetry and lab orchestration, and AI-assisted triage/assessment—used for this curriculum and for customers such as Aurnova.

## This course in ANUBIS (code `ains6302`)

Labs in this book are **assessed on the ANUBIS platform** (course code `ains6302`). The lab definitions, worker images, and scoring hooks live in the `anubis/assignments/` tree in *this* repository, alongside the Jupyter Book; Castalia’s control plane at `anubis.castalia.institute` runs the same definitions against student work.

## Architecture (high level)

```text
[this template repo]  ──(GitHub “template” flag)──▶  [student’s private course repo]
        │                                                    │
        │  anubis/assignments/* (tests + metadata)            │  push notebook / code
        ▼                                                    ▼
[Castalia runbook: publish]                      [ANUBIS autograde / lab worker]
        │                                                    │
        └──── registers lab + worker image ────────▶  ains6302
```

*Publish steps* (naming, dates, which worker image to use) are performed in the **ANUBIS** admin at `anubis.castalia.institute` and in Castalia’s internal runbook—they are **not** the public NYU *Anubis LMS* `anubis assignment init` / `anubis assignment sync` workflow.

## Instructor workflow (outline)

1. Develop or extend `anubis/assignments/module-N-lab/assignment.py` and `meta.yml` in this repository.
2. Set release, due, and any grace period in the course config (kept in sync with Populi/contract dates as needed).
3. **Publish** the updated lab to ANUBIS through the Castalia deployment process (ANUBIS admin + CI), so the worker image and test bundle match `main` here.
4. If scoring logic changes after release, use **regrade** from the ANUBIS course admin so all submissions re-run on the new tests.

## Student workflow (outline)

1. Sign in to the ANUBIS / course flow your cohort uses (served from `anubis.castalia.institute`).
2. Open your **ANUBIS-provisioned** lab workspace or the linked private GitHub repository created from this template.
3. Complete the graded work in `notebooks/module-N-lab.ipynb` (and any linked scripts).
4. **Push** to the default branch. ANUBIS runs the lab pipeline and surfaces results in the ANUBIS console; late rules follow the dates published for your cohort.

## What ANUBIS executes

For each module lab, the worker runs the checks in `anubis/assignments/module-N-lab/assignment.py`. All student code must be executed in the **sandboxed student context** the platform provides (the same *security model* as typical autograding: no running untrusted code with elevated privilege).

## Manual regrade

Instructors can trigger a full or partial **regrade** in ANUBIS so every submission re-runs after a test or image update.

---

*Internal reference only: Castalia’s ANUBIS API and worker contracts live in the institute runbook, not in third-party Anubis LMS documentation.*
