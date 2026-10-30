---
title: Radiolucent Patient Immobilization (AerFrame)
roles: [igem, coding, wildcard]
tabs: [clinical-research, clinical-research-software]
status: In final co-author circulation
dates: June 2026 to present
images:
  - src: assets/img/crop-frame-dose.png
    alt: A dose distribution in false color through a phantom lying in the treatment frame, with the frame rails visible underneath.
    caption: Dose through a phantom lying in the frame. The rails are the parts that matter, since a beam crossing one is where attenuation climbs. Cropped from a figure in the manuscript.
---

### Problem

Dr. Westover invented and patented a patient immobilization frame built from a composite
that is nearly transparent to radiation. It has been in use at UT Southwestern for over a
year and will be marketed to other centers, but no physics study existed to show how much
dose the older frames were absorbing before the beam reached the tumor.

### Solution

The cohort did not exist in any database. A patient had to have been treated on a specific
machine, simulated in a legacy frame, and treated at least once in the new one, so I
hand-screened about 50 patients' records and threw out warped scans, patients never
treated, and unfamiliar frames. From what was left I picked 11 patients to mirror real
practice: 3 spine, 3 prostate, 3 lung, and 2 abdomen, mixing fixed-field and arc therapy,
some with titanium hardware, across two legacy frame types and both anterior and posterior
target positions. I ran the attenuation calculations with the physicists, compared
12-field, 18-field, and arc plans with the frame masked to air against the frame present,
and added ion-chamber bench measurements at 6, 10, and 15 MV across several beam angles.

### Result

The new frame reads at about −928 Hounsfield units on patient imaging against −713 for the
legacy frame, which is the physical reason for everything that follows. Measured
attenuation stayed under 2 percent anywhere away from the side rails, and crossed 3 percent
only for beams passing through a rail at the lowest energy. Across the phantom and patient
plans it stayed between 0.6 and 2.5 percent.

That number matters more than it sounds. Adaptive systems replan on the anatomy of the day
and typically do not model the frame at all, so a frame this transparent can be used on
current platforms without modeling it, and a legacy frame cannot. I wrote the first draft
and the manuscript is in final circulation among co-authors. The limits are plain: eleven
patients at one institution, with a dosimetric endpoint rather than a clinical one.

Working title: *Radiolucent Stereotactic Body Frame for Online Adaptive Radiation
Therapy.*

The device diagram comes from Dr. Westover's patent and stays off this site until he says
otherwise.
