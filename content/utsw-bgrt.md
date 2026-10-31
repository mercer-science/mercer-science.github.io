---
title: Biology-Guided Radiotherapy on RefleXion
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: In final co-author circulation
dates: May 2026 – Present
images:
  - id: machine
    size: small
    src: assets/img/reflexion-machine.png
    alt: Russell standing beside the RefleXion biology-guided radiotherapy machine at UT Southwestern.
    caption: The RefleXion machine at UT Southwestern.
  - id: gantry
    size: small
    src: assets/img/reflexion-gantry.png
    alt: The inside of the RefleXion gantry, showing the linear accelerator and PET detectors.
    caption: Inside the gantry during the engineer walkthrough.
  - id: flow
    size: wide
    src: assets/img/crop-bgrt-flow.png
    alt: A flow chart running the PET-guided pathway along the top and the image-guided pathway along the bottom, from simulation through delivery.
    caption: The comparison figure I designed, with both pathways side by side. Cropped from the manuscript figure.
---

RefleXion is a new radiation therapy system that uses PET imaging to locate a tumor and track it during treatment, allowing the radiation beam to effectively follow the tumor in real time. Although the system had been used to treat patients for more than a year, its delivered dose had not yet been independently evaluated or compared with standard image-guided radiotherapy. Our study examined whether the technology delivered on its promise of more precise treatment.

After observing a treatment and an engineer walkthrough to understand the system, I developed an automated workflow to extract and analyze treatment-planning data. I wrote a C# script to pull dose information for every patient and plan from Aria-Eclipse (the hospital medical physics database) into organized spreadsheets. Because physicians use inconsistent names and groupings for anatomical structures, the script identifies most structures automatically and flags ambiguous cases for human review. A Python script then organizes the exports into analysis templates developed with Dr. Westover, and R scripts generate the figures and tables directly from the underlying data.

[figure: machine, gantry]

During the study, we also investigated whether respiratory motion could explain some of the differences we observed in organ doses. Post-treatment evaluations typically assume that organs remain in the same positions they occupied during simulation, even though the tumor moves with breathing. Since respiratory motion was not directly recorded, I created software that could reconstruct it using contours from each patient's backup plan. I then developed an algorithm to measure each organ's distance from the target and ran approximately 1,000 checks per patient to evaluate whether motion could account for the dose differences.

Across 17 patients, the PET-guided plans treated a target volume 19% smaller than the image-guided backup plans. The target was smaller in 15 patients and unchanged in two, with greater reductions among tumors that moved more during breathing. That precision came with trade-offs: the PET-guided plans produced a wider intermediate-dose region and higher maximum doses to the spinal cord and heart. Our analysis suggested these differences arose primarily during treatment planning rather than delivery, making them potential targets for improvement.

[figure: flow]

A physicist on the team shared our organ-dose findings with manufacturer contacts around the summer physics meeting. The company is now revising its post-treatment evaluation process for an upcoming release. The manuscript presents both the advantages and limitations of the technology, including findings that are less favorable than the commercially appealing narrative. After more than eight rounds of revision, including two complete restarts, it is now in final circulation among the co-authors.

**Manuscript:** *Dosimetric Cost of a Smaller Target When Using Biology-Guided Radiation Therapy for Lung Cancer.*
