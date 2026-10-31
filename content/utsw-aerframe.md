---
title: Radiolucent Patient Immobilization (AerFrame)
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: In final co-author circulation
dates: June 2026 – Present
images:
  - id: diagram
    src: assets/img/aerframe-diagram.png
    alt: A labeled line drawing of the radiolucent frame, naming the base, rails, compression arch, compression plate and screw, coordinate arch, laser box, and head rest.
    caption: The frame, labeled. The rails are the parts a beam can cross, which is where attenuation is highest. Device developed by Dr. Westover; figure from the manuscript.
  - id: setup
    src: assets/img/aerframe-setup.png
    alt: A schematic of the ion chamber measurement, with a block of solid water lying in the frame and beam angles of 0, 62.1, 90, and 180 degrees marked.
    caption: The ion chamber setup, and the beam angles we measured at. Cropped from a figure in the manuscript.
  - id: bysite
    src: assets/img/aerframe-by-site.png
    alt: A paired plot of target dose change for the legacy frame in red and the new frame in blue across lung, prostate, spine, and abdomen cases, with the new frame losing less dose in every site.
    caption: Dose to the target for each patient with the legacy frame and the new one. Cropped from a figure in the manuscript.
  - id: dose
    src: assets/img/crop-frame-dose.png
    alt: A dose distribution in false color through a phantom lying in the treatment frame, with the frame rails visible underneath.
    caption: Dose through a phantom lying in the frame. Cropped from a figure in the manuscript.
---

Dr. Westover developed and patented a patient immobilization frame made from a composite designed to let radiation pass through with minimal interference. The frame has been used at UT Southwestern for more than a year and is expected to be marketed to other treatment centers, but its effect on radiation delivery had not been systematically evaluated. Our study examined whether the frame allows radiation to reach the tumor without meaningfully changing the planned dose.

[figure: diagram]

Identifying suitable patients required manually screening approximately 50 medical records. Patients had to meet several criteria: treatment on a specific machine, an initial simulation using a legacy frame, and at least one treatment using the new frame. I excluded patients with unusable scans, incomplete treatment records, or unfamiliar immobilization devices, then selected 11 patients to represent several common treatment sites and techniques. The cohort included spine, prostate, lung, and abdominal tumors; different radiation delivery methods; patients with and without titanium hardware; and both front- and back-facing target positions.

Working with the medical physicists, I compared radiation doses with the frame present against doses calculated as if the frame were not there. We evaluated several treatment plans and supplemented the patient analysis with physical measurements using an ion chamber at three radiation energies and several beam angles.

[figure: setup, dose]

The new frame was substantially more transparent to radiation than the older frames. Across phantom measurements and patient treatment plans, it reduced the delivered dose by only 0.6% to 2.5%. Attenuation remained below 2% except when radiation passed directly through the side rails at the lowest energy, where it exceeded 3%.

[figure: bysite]

**Put simply, the new frame allows nearly all the radiation to pass through it and reach the tumor as planned.** This means clinicians can use it without having to modify their radiation treatment plans to account for the frame, unlike older immobilization devices that absorb more radiation. That is particularly useful for adaptive radiation therapy, where treatment plans are updated to match a patient's anatomy each day.

I wrote the first manuscript draft, which is now in final circulation among co-authors.

**Working title:** *Radiolucent Stereotactic Body Frame for Online Adaptive Radiation Therapy.*
