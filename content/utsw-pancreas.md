---
title: Diffusion MRI in Pancreatic SBRT
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: Ongoing
dates: August 2026 to present
images: []
---

### Problem

The lung study produced a threshold tool that outlines treatment-resistant tissue, but
nothing tied it to what happened to the patients. Dr. Deng brought me onto a pancreas
study to start closing that gap: do the same diffusion measurements track how pancreatic
tumors respond to stereotactic radiation?

### Solution

I ran all 76 patients through the pipeline I had rebuilt, and 23 of them turned out to have
both complete diffusion imaging and outcome data. I did the chart review for response at
three months and for local and distant failure over time, since most three-month results
in this last-line population were stable or not evaluable. A Python script rebuilds each
patient's plot and notes from the chart-review sheet, so adding a patient does not mean
redrawing anything.

### Result

One early signal is worth the work: a patient who failed both locally and distantly about
eight months after treatment showed tissue diffusion falling by the third fraction, the
opposite of what a dying tumor does, while a patient with stable disease showed it rising.
In principle a physician could have seen that early enough to change the plan. The trends
run opposite to the lung study, and I think the spacing explains it, since these patients
were treated every two or three days rather than weeks apart, leaving less time for tissue
remodeling between pulses. Analysis is still underway.
