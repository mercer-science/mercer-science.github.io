---
title: Diffusion MRI in Pancreatic SBRT
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: Ongoing
dates: August 2026 to present
images: []
---

### The Study

Building on our lung study, I joined Dr. Deng's pancreatic cancer study to investigate whether diffusion MRI measurements track tumor response to stereotactic radiation. I processed all 76 patients through the pipeline I rebuilt and identified 23 with both complete imaging and outcome data. I then reviewed their medical records to document treatment response and track local and distant disease progression.

### An Early Signal

One early observation is particularly interesting: a patient who later experienced both local and distant disease progression showed decreasing tissue diffusion by the third treatment fraction, while a patient with stable disease showed increasing diffusion. These trends are opposite to what we observed in the lung study. I suspect the difference may relate to treatment timing: pancreatic patients receive radiation every two to three days rather than several weeks apart, potentially leaving less time for tissue remodeling between treatments.

### Automating the Analysis

I also developed a Python script that automatically generates patient-specific plots and summaries from the chart-review data. Analysis is ongoing, and we are evaluating whether these early diffusion changes consistently correspond to treatment outcomes across the cohort.
