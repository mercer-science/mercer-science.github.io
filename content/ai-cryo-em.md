---
title: An AI Agent for Cryo-ET Processing
roles: [igem, coding, wildcard]
tabs: [physical-sciences, ai]
status: Ongoing, manuscript in preparation
dates: August 2026 to present
images: []
---

### Question

Turning thousands of tilted images of a frozen cell into a three-dimensional map means
chaining together a dozen specialized programs, each with its own settings and its own ways
of failing. Learning that chain normally takes months. Can a general-purpose AI coding
agent carry a newcomer through it without removing the understanding the work is supposed
to build?

### Approach

The test set is 39 tilt series of cryo-focused-ion-beam-milled *E. coli* in exponential
growth, collected on a Krios at 300 kV. The agent proposes each step, installs and
configures the tool, and runs it, while a human approves, overrides, or corrects every
parameter. The chain runs from motion correction through alignment and reconstruction,
missing-wedge correction, template matching, classification, and subtomogram averaging,
ending in an analysis of whether ribosomes sit alone or in pairs and chains. Every
recommendation gets logged as accepted, overridden, or an error a human caught, which is
what makes the claim measurable rather than anecdotal. The workflow is packaged as a
reusable agent skill so the next person in the lab starts further along. This is joint
work with Chitral Chatterjee in Dr. Jensen's lab.

### Status

**Ongoing.** I presented this as a poster, *Can an AI Agent Collapse the Cryo-ET Learning
Curve?*, at the Utah CryoEM Symposium at BYU on October 8, 2026. A manuscript is in
preparation.
