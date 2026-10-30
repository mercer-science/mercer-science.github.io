---
title: Lung Diffusion MRI on the MR-Linac
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: Submitted
dates: May 2026 to present
images:
  - src: assets/img/mr-linac.jpg
    alt: Russell standing beside the Elekta Unity MR-Linac at UT Southwestern.
    caption: The Elekta Unity MR-Linac, which images with MRI during treatment and quietly records diffusion-weighted scans before each session.
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

Of 55 sessions, 42 captured diffusion imaging, 41 were usable, and 34 had enough tumor
voxels to analyze. On-board signal-to-noise averaged about 8 against roughly 127 at
simulation. Contour-based diffusion changes agreed closely between the clinical and
adjusted contours. The piece I care about most is the threshold tool: a diffusion cutoff
that outlines a treatment-resistant core inside the clinical target, which could receive
extra dose in the same treatment and which also shows where the target should expand. Dr.
Deng presented examples from the paper and the pipeline at a physics conference last
summer. The manuscript is submitted to the *International Journal of Radiation Oncology,
Biology, Physics*.

The study is hypothesis-generating with 10 patients, missing data, and low on-board signal,
and the threshold is not yet tied to outcomes. Testing it against outcomes is what the
pancreas study began.
