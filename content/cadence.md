---
title: Cadence, a Spaced-Repetition App
roles: [design]
tabs: [other-ui-projects]
status: Ongoing, early MVP
dates: 2026 to present
images: []
needs: Screenshots from Russell. The repository stays private, so the screens are the only thing a reviewer can see.
---

### Problem

Anki is the tool most medical students live in, and its interface is a decade of accreted
options stacked on a scheduler most users never see. The scheduling is the good part. The
experience of sitting down to 400 due cards is not.

### Solution

Cadence is a rewrite of the parts that matter, built with React, TypeScript, and the FSRS
scheduler, which models memory directly rather than nudging intervals by fixed multipliers.
The design work is deciding what to leave out: a card should take one decision, the queue
should tell you how long it will take before you start, and the settings a user actually
changes should not be buried under the ones they never will.

### Status

**Ongoing.** It is an early minimum viable product, and the repository is private, so the
screenshots are what I can show.
