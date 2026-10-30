---
title: Publication Figures and Reproducible Pipelines
roles: [design]
tabs: [figures]
status: ""
dates: 2024 to present
images:
  - src: assets/img/langmuir-fig2.png
    alt: Bar charts of film coverage and crystallite size against temperature, beside four electron micrographs of films grown at 22, 32, 42, and 52 degrees Celsius.
    caption: A published figure from our Langmuir paper. Charts and micrographs in one panel, so the numbers and the material they came from sit together. Ralph et al., Langmuir 2026;42(6):4475–4488.
---

Most of my figure work is not drawing. It is building the thing that draws the figure, so
the twelfth revision costs the same as the first.

For the radiation oncology studies I wrote R scripts that generate every figure and table
straight from the raw export. About 20 figures were drafted for the RefleXion paper and
narrowed to a main set plus supplements; six tables generate themselves. When I found a bug
that had been capping a key measurement in the lung study, fixing it meant re-exporting and
rerunning, and every figure rebuilt correctly without anyone touching a plot.

Inside the imaging application, the image creator does the same job for the parts a script
cannot choose: a physician picks slices and structures, previews at low resolution, and
then renders a publication-quality panel, with upsampling past the scanner's native
resolution when the figure needs it.

The design judgment that matters here is what goes in a panel together. The published
figure above puts coverage and crystallite size next to the micrographs of the films
themselves, because a reader who sees a bar chart alone has to take the claim on faith.
