---
title: Biology-Guided Radiotherapy on RefleXion
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: In final co-author circulation
dates: May 2026 to present
images:
  - size: small
    src: assets/img/reflexion-machine.png
    alt: Russell standing beside the RefleXion biology-guided radiotherapy machine at UT Southwestern.
    caption: The RefleXion machine at UT Southwestern, which steers the beam using the tumor's live PET signal.
  - size: small
    src: assets/img/reflexion-gantry.png
    alt: The inside of the RefleXion gantry, showing the linear accelerator and PET detectors.
    caption: Inside the gantry during an engineer walkthrough. The PET detectors ride with the linear accelerator.
  - src: assets/img/crop-bgrt-flow.png
    alt: A flow chart running the PET-guided pathway along the top and the image-guided pathway along the bottom, from simulation through delivery.
    caption: The figure I designed to put both pathways side by side, so a reader can find the one point where they diverge. Cropped from the manuscript figure.
---

### Problem

RefleXion is a new machine, cleared by the FDA and installed at only a few U.S. centers.
The patient takes up a PET tracer, two detectors on the gantry find the tumor, and the beam
follows it in real time. More than a year after the first patients finished treatment,
nobody had checked independently whether the delivered dose matched the plan, or how it
compared with standard image-guided radiotherapy. The technology is commercially stalled
for want of exactly that evidence.

### Solution

I watched a treatment and an engineer walkthrough first, so I understood the workflow
before touching the data. Then I exported the plans into Aria-Eclipse and wrote a C# script
that pulls the relevant dose data for every patient and plan into organized spreadsheets.
The hard part was naming: every physician draws and labels structures differently, so a
lung might be one structure or two, and a patient might carry several planning target
volumes with unrelated names. The script resolves most of that on its own and asks a human
only when it genuinely cannot tell two structures apart. A Python step filters the raw
export into templates I designed with Dr. Westover, and R scripts build every figure and
table from the raw data automatically.

Partway through, a physicist raised a problem that could have explained my less favorable
organ-dose findings: post-treatment evaluation assumes organs sit where they were at
simulation, even though the beam follows a moving tumor. To test it I extracted dose
fall-off metrics, reconstructed each patient's respiratory motion from the backup plan's
contours since motion is recorded nowhere, wrote an algorithm for each organ's distance
from the target, and ran about 1,000 checks per patient that flagged every case for or
against the effect.

### Result

Nearly all of those checks supported my conclusion that the effect was minor. Across 17
patients, the PET-guided plan treated a target 19 percent smaller than the image-guided
backup, smaller in 15 of 17 patients and unchanged in 2, and the reduction grew with how
far the tumor moved with breathing. The cost shows up elsewhere: a wider
intermediate-dose region, and higher spinal cord and heart maxima. Those originate in
planning rather than in delivery, which matters, because it means they are fixable.

A physicist on the team took the organ-dose findings to his contacts at the manufacturer
around the summer physics meeting, and the company is revising its post-treatment
evaluation in an upcoming release. The paper says plainly where the technology helps and
where it does not, which is not the commercially convenient answer. I rewrote it more than
eight times, including two complete restarts, and it is in final circulation among
co-authors now.

Published title: *Dosimetric Cost of a Smaller Target When Using Biology-Guided Radiation
Therapy for Lung Cancer.*
