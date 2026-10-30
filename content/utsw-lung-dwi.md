---
title: Lung Diffusion MRI on the MR-Linac
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: Manuscript submitted
dates: May 2026 – Present
images:
  - id: machine
    size: small
    src: assets/img/mr-linac.jpg
    alt: Russell standing beside the Elekta Unity MR-Linac at UT Southwestern.
    caption: The Elekta Unity MR-Linac, which records diffusion-weighted scans before each session.
  - id: responder
    size: wide
    src: assets/img/crop-responder-maps.png
    alt: Two rows of four false-color diffusion maps of one responding patient across fractions one, two, three, and five, the top row apparent diffusion coefficient and the bottom row perfusion fraction, with the tumor outlined in red.
    caption: One responding patient across treatment. Apparent diffusion coefficient above, perfusion fraction below, with the tumor outlined. Cropped from a figure in the submitted manuscript.
  - id: map
    src: assets/img/crop-dwi-map.png
    alt: A tissue-diffusion map of a lung tumor in false color, with three nested contours drawn on it.
    caption: "A tissue-diffusion map with three contours: the clinical target in yellow, a tighter tumor-only contour in red, and the diffusion-defined core in blue. Cropped from a figure in the submitted manuscript."
  - id: core
    src: assets/img/crop-resistant-core.png
    alt: A grayscale MRI slice of a tumor with yellow, red, and green contours nested inside one another.
    caption: The same idea on anatomy. Green is the treatment-resistant core that a boost would target, inside the clinical contour in red.
---

I worked with a team of medical physicists at UT Southwestern to investigate whether diffusion-weighted MRI could predict tumor response during radiation treatment. We studied 10 patients with ultra-central lung tumors receiving PULSAR (Personalized Ultrafractionated Stereotactic Adaptive Radiotherapy), a treatment in which radiation doses are delivered several weeks apart. Because responding tumors undergo changes in cellular structure that affect water movement, diffusion MRI may reveal treatment response before changes in tumor size become visible.

[figure: machine]

I processed and analyzed the patients' imaging data, developed methods to recover partially usable scans, and evaluated several diffusion models.

Our findings suggest that tissue diffusion and perfusion measurements can distinguish patients responding to treatment from those who are not as early as the third treatment fraction. This is particularly promising for PULSAR because it could allow physicians to assess treatment response while the radiation course is still underway, rather than waiting for changes in tumor size on follow-up imaging.

[figure: responder]

I also developed a thresholding method to identify potentially treatment-resistant regions within tumors, which could eventually help guide radiation dose adjustments.

[figure: map, core]

The study included 10 patients, eight of whom had completed treatment at the time of analysis. The findings are preliminary and require validation against clinical outcomes.

**Submitted manuscript:** *Onboard Intravoxel Incoherent Motion Diffusion-Weighted MRI Tracks Early Tumor-Volume Response in Ultra-Central Lung Tumors Treated With PULSAR.*
