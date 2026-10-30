---
title: Diffusion MRI Pipeline and Web Application
roles: [igem, coding, design, wildcard]
tabs: [clinical-research, clinical-research-software]
status: Handed off to the clinical software team
dates: May 2026 – Present
images:
  - id: before
    src: assets/img/pipeline-before.png
    alt: The inherited pipeline interface, a single-patient step runner with one button per processing step.
    caption: Before. One patient at a time, with every step started by hand.
  - id: after
    src: assets/img/pipeline-after.png
    alt: The rebuilt bulk runner, with a queue for patient identifiers and a list of processing steps to choose from.
    caption: After. The bulk runner queues patients, schedules CPU and GPU work, and flags errors on its own.
  - id: viewer
    src: assets/img/dwi-viewer.png
    alt: The MRI viewer, showing the same slice across four sessions with a diffusion map overlaid and a whole-tumor histogram under each one.
    caption: The MRI viewer. The same slice across sessions, with a whole-tumor histogram under each.
  - id: histograms
    src: assets/img/dwi-histograms.png
    alt: A grid of histograms comparing ADC, Dp, Dt, and Fp across four sessions, one column per session.
    caption: Parameter comparison. Each measure's distribution, session by session.
  - id: creator
    src: assets/img/dwi-image-creator.png
    alt: The image creator's slice selection, with a strip of slices for each session and one slice marked to keep.
    caption: The image creator. Choose which slice to keep for each session, then render the panel.
  - id: threshold
    src: assets/img/dwi-threshold.png
    alt: The threshold creator, showing five sessions with a threshold contour drawn on the diffusion map of each.
    caption: The threshold creator.
  - id: fit
    size: small
    src: assets/img/fit-checker.png
    alt: The fit checker, with a diffusion map above and a plot of one voxel's measured signal against its IVIM and ADC fits.
    caption: The fit checker. Click a voxel to see its signal against both models.
  - id: poster
    size: wide
    src: assets/img/spri-poster.png
    alt: A conference poster titled From Bench to Beam, laid out in five numbered panels covering biology-guided radiotherapy, radiolucent immobilization, adaptive conventional treatment, adaptive SABR, and on-board diffusion imaging.
    caption: The poster covering all five studies, presented at the BYU Medical Society conference in August 2026 with the other intern. Click it to read the panels.
---

I joined the Radiation Oncology department at UT Southwestern in May 2026 and took over a diffusion MRI processing pipeline that had been developed by several graduate students. When the last student left, the software was still running from his personal account on a single GPU workstation. Its dependencies were tied to virtual environments that were difficult to reproduce, and the account was scheduled for deletion. A postdoctoral researcher hired for a different project was expected to take over the work, but the existing lung study could not be rerun without access to the original backend.

#### Rebuilding the Pipeline

I rebuilt the pipeline web interface and made the pipeline much more streamlined, using Claude Code as a development assistant while reviewing and verifying the scientific and computational decisions myself. The application handles the processing workflow from raw hospital imaging files through final analysis. It retrieves patient scans from hospital network shares, repairs corrupted files, converts DICOM images to NIfTI, identifies acquisition protocols, corrects geometric distortion, applies two neural-network denoising steps, fits intravoxel incoherent motion (IVIM) and apparent diffusion coefficient (ADC) models, and registers images across treatment sessions. It also checks intermediate results and flags potential errors.

#### Bulk Processing

I built a bulk-processing system around the pipeline so researchers no longer have to run each patient and processing step individually. Users enter patient identifiers and select the processing steps they need. Each patient gets a separate tab showing progress through the workflow, while the application manages CPU and GPU scheduling, monitors available disk space, archives completed studies to department servers, and packages the results for export. These upgrades allowed us to process patient data much quicker, advancing the rate of research in the department.

[figure: before, after]

The application processed all 76 patients in a pancreas study in approximately 2.5 days of continuous server time. For comparison, processing the 10-patient lung study using the previous workflow had taken approximately a week of manual work.

#### The Web Interface

I also developed the web interface for reviewing and analyzing the resulting images. Its main features include:

- **MRI Viewer:** Displays anatomical images, contours, and diffusion maps side by side across treatment sessions, with whole-tumor histograms for each session.
- **Parameter Comparison:** Allows researchers to compare ADC, Dp, Dt, Fp, and R measurements across treatment days.
- **Image Creator:** Generates publication-quality image panels from selected MRI slices.
- **Threshold Creator:** Applies user-defined cutoffs to diffusion maps to outline potentially treatment-resistant tumor regions and exports contours compatible with the treatment planning system.
- **Fit Checker:** Allows users to select individual voxels and compare measured MRI signals against both IVIM and ADC model fits.
- **Quality assessment:** Reports reliability statistics covering acquisition parameters, signal-to-noise ratios, geometric distortion, image registration, and model-fitting quality.

I intentionally developed these user interface upgrades so that any researcher in the department can easily access, process, and evaluate data. After I finished, the server and application were entirely stand alone. You could get any information on any patient that you needed without having to have access to the back end of the server.

#### Handoff

The project was subsequently transferred by hospital IT to the Radiation Oncology Application Team for further development toward universal use. They are now using this code in clinical studies. The MRI vendor also expressed interest in incorporating the processing workflow into its imaging system. I prepared the technical handoff documentation, including the remaining requirements for a clinical version, and trained the postdoctoral researcher who took over the project.

The pipeline code belongs to UT Southwestern and is tied to its internal systems, so it is not publicly available. The screenshots below show the web interface without patient-identifying information.

[figure: viewer, histograms]

[figure: creator, threshold]

[figure: fit]

[figure: poster]
