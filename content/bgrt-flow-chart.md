---
title: Explaining a Treatment Machine in One Figure
roles: [design]
tabs: [figures]
status: Designed August 2026
dates: August 2026
images:
  - src: assets/img/crop-bgrt-flow.png
    alt: A flow chart running the PET-guided pathway along the top and the image-guided pathway along the bottom, from simulation through delivery.
    caption: Part of the finished figure. Both pathways run in parallel from simulation to delivery, so the divergence lands visually instead of in a sentence.
---

### Problem

The RefleXion paper had to explain, to readers who had never seen the machine, how
PET-guided delivery differs from standard image-guided delivery, and it had to do so inside
a strict word limit against almost 4,000 words of supplement. Prose was not going to carry
it. Reviewers needed to see the two workflows side by side and find the one point where
they diverge.

### Solution

I designed a flow chart that runs both pathways in parallel from simulation through
delivery, so the divergence lands visually instead of being asserted in a sentence. I built
it in PowerPoint with Claude working in the same file: I directed the layout and the logic,
and the agent handled alignment, color, and scaling, which is the part that eats hours and
produces no insight. Then I wired the figure-rendering code to convert the slide to an
image and assemble it with the R-generated panels automatically, so the whole figure
rebuilds from source whenever the data changes.

### Result

It is the final figure in the manuscript, which is in co-author circulation. The method is
the part worth keeping: when a figure is assembled by a script rather than by hand,
revising it eight times costs nothing, and I revised that paper more than eight times.
