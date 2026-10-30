---
title: Lung Diffusion MRI on the MR-Linac
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: Submitted
dates: May 2026 to present
images:
  - size: small
    src: assets/img/mr-linac.jpg
    alt: Russell standing beside the Elekta Unity MR-Linac at UT Southwestern.
    caption: The Elekta Unity MR-Linac, which images with MRI during treatment and quietly records diffusion-weighted scans before each session.
  - size: small
    src: assets/img/crop-dwi-map.png
    alt: A tissue-diffusion map of a lung tumor in false color, with three nested contours drawn on it.
    caption: "A tissue-diffusion map with three contours: the clinical target in yellow, a tighter tumor-only contour in red, and the diffusion-defined core in blue. Cropped from a figure in the submitted manuscript."
  - size: small
    src: assets/img/crop-resistant-core.png
    alt: A grayscale MRI slice of a tumor with yellow, red, and green contours nested inside one another.
    caption: The same idea on anatomy. Green is the treatment-resistant core that a boost would target, inside the clinical contour in red.
---

### Problem

The Unity combines an MRI scanner with a linear accelerator, and before every treatment it
records diffusion-weighted images that nobody used clinically. Dying tumors lose cells, so
water moves more freely through them, which should show up as a rising apparent diffusion
coefficient. If that holds, a physician could see a tumor responding during treatment,
weeks before it shrinks on CT. These patients received PULSAR, where the radiation pulses
are spaced weeks apart, and no one had published diffusion imaging in PULSAR patients.

### Solution

I worked with a team of medical physicists on 10 patients, each carrying about 10 GB and
more than 10,000 DICOM images with meaningless file names, all processed on hospital
servers. Every patient was missing at least one diffusion series, because therapists had
not backed them up and the consoles had been wiped. The scan field often was not centered
on the tumor, so contours ran outside the map, and only 50.9 percent of sessions had data
usable as scoped; I found a way to include partially covered sessions rather than drop
them. The simulation scanner had 15 to 20 times the signal-to-noise of the machine itself,
so the two could not be compared directly.

Rather than force the original claim, I reframed the study into three aims: whether
quantitative diffusion values can be pulled reliably from the machine's own imaging,
whether those values move opposite to tumor volume as biology predicts, and how a
diffusion-defined target would differ from the clinical one. Out of curiosity I made
per-session histograms and saw values piling up at exactly 3. The exporter was capping
them, which had been dragging later-fraction averages down. I fixed the pipeline,
re-exported, and reran everything; because the figures rebuild from raw data, the fix cost
an afternoon instead of a month.

### Result

The biexponential model fit the on-board signal better than the standard one, which is the
first useful finding: the simple measure everyone reaches for was the wrong one here.
Changes measured inside the clinical target and inside a tight tumor-only contour agreed
almost exactly, so the result does not depend on who drew the contour. Through the third
fraction, tissue diffusion and perfusion fraction separated responders from
non-responders, and the conventional measure did not. Over the full course only tissue
diffusion held that separation.

The piece I care about most is the threshold tool: a diffusion cutoff that outlines a
treatment-resistant core inside the clinical target, which could take extra dose in the
same treatment, and which also shows where the target should expand. Dr. Deng presented
examples from the paper and the pipeline at a physics conference last summer.

Eight of the ten patients had finished treatment at data lock, so this is
hypothesis-generating, and the threshold is not yet tied to outcomes. Testing it against
outcomes is what the pancreas study began.

Submitted title: *Onboard Intravoxel Incoherent Motion Diffusion-Weighted MRI Tracks Early
Tumor-Volume Response in Ultra-Central Lung Tumors Treated With PULSAR.*
