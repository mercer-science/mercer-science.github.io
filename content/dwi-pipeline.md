---
title: Diffusion MRI Pipeline and Web App
roles: [igem, coding, design, wildcard]
tabs: [clinical-research, clinical-research-software]
status: Handed to the clinical software team
dates: May 2026 to present
images:
  - src: assets/img/pipeline-before.png
    alt: The inherited pipeline interface, which ran one patient through one step at a time.
    caption: Before. The inherited tool ran one patient at a time, with every step started by hand.
  - src: assets/img/pipeline-after.png
    alt: The rebuilt bulk runner, with a tab per patient and a queue of processing steps.
    caption: After. The bulk runner queues patients, schedules CPU and GPU work, and flags errors on its own.
  - src: assets/img/fit-checker.png
    alt: The fit checker, showing a voxel's measured signal with biexponential IVIM and monoexponential ADC fits.
    caption: The fit checker. Click any point on a map to see its measured signal with both model fits, then export the figure and the data behind it.
---

### Problem

The department's diffusion MRI processing pipeline had passed through several graduate
students. When the last one left it was sitting in his personal account on one GPU
workstation, held together by virtual environments nobody could rebuild, and the account
was scheduled for deletion. A postdoc hired for different work was about to inherit it,
and the earlier lung study could not be rerun without back-end access.

### Solution

I rebuilt it as a web application, working with the Claude Code agent and checking every
scientific decision myself. It collects each patient's imaging from the hospital network
shares, repairs broken files, converts DICOM to NIfTI, detects the pulse protocol, corrects
distortion, runs two neural-network denoising steps, fits the IVIM and ADC models, and
registers the images across treatment days, flagging anything that looks wrong as it goes.
A bulk runner sits on top: enter the patient identifiers, pick the steps, and each patient
gets a tab that moves through the chain while the runner schedules CPU and GPU work,
watches disk space, archives finished patients to the server drives, and exports everything
as one zip.

The interface is where a physician or physicist actually works. An MRI viewer lines up
anatomy, contours, and parametric maps slice by slice with whole-tumor histograms per day.
A parameter comparison view puts ADC, Dp, Dt, Fp, and R side by side across days. An image
creator renders publication-quality panels from chosen slices. A threshold creator applies
a cutoff to outline the treatment-resistant core of a tumor and exports contours the
treatment planning system can import. The fit checker lets you click a single voxel and see
its measured signal against both model fits. Reliability statistics cover acquisition
parameters, signal-to-noise, geometric distortion, registration, and fit quality.

### Result

It processed all 76 pancreas patients in about 2.5 days of continuous server time. The
10-patient lung study had taken roughly a week by hand. Hospital IT moved the application
to the Radiation Oncology Application Team for clinical use, with a plan to run it on a
standalone server for the whole department, and the MRI vendor has asked about building the
processing into the machine. I wrote the hand-off document, which lists what a clinical
version still needs, and trained the postdoc who took it over.

The honest limit: a clinical version has to finish in three to five minutes at the console,
and mine takes about an hour per patient. That gap is the part of research I find most
interesting, and it is most of why I want to train as a physician-scientist.

The pipeline code belongs to UT Southwestern and is tied to its systems, so it is not
public. The screenshots above come from the application interface and carry no patient
information.
