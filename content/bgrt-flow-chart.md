---
title: RefleXion Treatment Workflow Figure
roles: [design]
tabs: [figures]
status: Designed August 2026
dates: August 2026
images:
  - id: flow
    src: assets/img/crop-bgrt-flow.png
    alt: A flow chart running the PET-guided pathway along the top and the image-guided pathway along the bottom, from simulation through delivery.
    caption: Part of the finished figure. Both pathways run in parallel from simulation to delivery, so the divergence lands visually instead of in a sentence.
---

The RefleXion manuscript needed to explain how PET-guided radiation delivery differs from conventional image-guided delivery. The distinction is not easy to communicate to readers unfamiliar with the system, particularly within a strict word limit and alongside nearly 4,000 words of supplementary material. A side-by-side visual was more effective than trying to explain both workflows in prose.

I designed a flowchart showing both treatment pathways in parallel, from simulation through delivery, making the key differences immediately visible. I built the figure in PowerPoint with Claude assisting directly in the file. I directed the layout and scientific logic while using the agent to handle alignment, color, and scaling.

[figure: flow]

I then developed a figure-generation workflow that converts the PowerPoint slide into an image and combines it with panels generated in R. This allows the complete figure to be rebuilt automatically from its source components whenever the underlying data or manuscript needs to change.

The figure is included in the manuscript, which is currently in final co-author circulation.
