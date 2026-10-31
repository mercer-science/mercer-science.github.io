---
title: Publication Figures and Reproducible Pipelines
roles: [design]
tabs: [figures]
status: ""
dates: 2024 to present
images:
  - id: rpipe
    src: assets/img/crop-ethos-response.png
    alt: An R-generated line chart titled The reason to adapt changes, plotting the benefit of adapting for PTV coverage, lung V20, and esophagus sparing across six treatment weeks, with p-values.
    caption: An R-generated figure from the adaptive study, built straight from the raw export. Change the data, rerun, and the plot rebuilds itself.
  - id: panel
    src: assets/img/crop-responder-maps.png
    alt: A multi-panel figure of ADC and perfusion-fraction diffusion maps for one responding patient across treatment fractions, each with the tumor contour overlaid.
    caption: "A panel assembled in the imaging app's image creator: chosen slices and structures, rendered at publication quality and reproducible from the saved selection."
---

I build tools that make scientific figures reproducible from the moment they are configured. Rather than manually assembling plots in software, I have developed exportable interfaces that let researchers select the data, images, measurements, and visual elements they want to present, preview the result, and generate publication-ready figures from the same underlying configuration.

For the radiation oncology studies, I wrote R pipelines that generate figures and tables directly from raw data exports. Approximately 20 figures were developed for the RefleXion manuscript, alongside six automatically generated tables. When an error in the lung study was found to be capping a key measurement, correcting the data and rerunning the pipeline regenerated the figures consistently without manual editing.

[figure: rpipe]

I also developed an image-generation interface within the imaging application. Researchers can select image slices and anatomical structures, arrange them into panels, preview the layout at low resolution, and export publication-quality images. The interface preserves those selections and settings so that figures can be regenerated consistently, including at resolutions beyond the scanner's native output when needed.

[figure: panel]

The goal across these projects is to make a figure an exportable, reproducible product of its underlying data and configuration, rather than a manually assembled image that must be recreated whenever something changes.
