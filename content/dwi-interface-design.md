---
title: Designing the Diffusion MRI Workspace
roles: [design]
tabs: [clinical-interface-design]
status: Handed to the clinical software team
dates: May 2026 to present
images:
  - src: assets/img/pipeline-before.png
    alt: The inherited pipeline interface, a single-patient step runner with each processing step started by hand.
    caption: Before. One patient, one step at a time, each click waiting on a person who already knew which step came next.
  - src: assets/img/pipeline-after.png
    alt: The rebuilt bulk runner, showing a tab per patient and a queue of processing steps with status indicators.
    caption: After. A tab per patient, a queue that schedules itself, and errors surfaced where the user is already looking.
  - src: assets/img/fit-checker.png
    alt: The fit checker interface, showing a parametric map beside a plot of one voxel's measured signal with two model fits.
    caption: "The fit checker, built because physicists kept asking the same question: is this number real, or did the fit fail here?"
---

### Problem

The people who had to use this software were physicians and medical physicists, not
engineers, and the tool they had was built around the processing steps rather than around
anything they wanted to do. It ran one patient at a time. Every step was a button someone
had to press in the right order, and if a step failed you found out by noticing that
nothing happened. Nobody could tell whether a given number was trustworthy without going
back to the raw images by hand.

So the design question was not how to make the screens nicer. It was what the users were
actually trying to decide, and what the old tool made them do instead.

### Solution

I watched what people asked for and designed around the decisions rather than the pipeline.

**A physician wants to know what changed between treatment days.** That became a viewer
that lines up anatomy, contours, and parametric maps slice by slice, with whole-tumor
histograms per day, so the comparison is on one screen instead of in somebody's memory.
An early June version only stacked the same slice across days; after the physicians used
it, the July version added the histograms and the per-day parameter comparison, because
what they wanted was the distribution, not the picture.

**A physicist wants to know whether a number is real.** That became the fit checker: click
any voxel, see the measured signal with both model fits drawn through it, export the figure
and the data. It exists because the question kept coming up in meetings and the old answer
was a shrug.

**A physician wants to act on the result.** That became the threshold creator, which
applies a cutoff to outline the treatment-resistant core and exports contours the treatment
planning system can import. Design-wise this was the hardest piece, because the output had
to land inside software the physician already uses rather than ask them to learn mine.

**Everyone wants figures.** That became the image creator: pick slices and structures,
preview at low resolution, then render publication panels. I also set up an HTML preview so
drafts could be shared with the physicians without sending anything that needed installing.

**And nobody wants to babysit a queue.** The bulk runner takes a list of patients, gives
each one a tab, schedules CPU and GPU work, watches disk space, archives finished patients,
and raises errors where the user is already looking.

### Result

The application went from one person's workstation account to the team that maintains
clinical software, and it processed 76 patients in about 2.5 days where the old workflow
had taken a week for 10. A physician used the diffusion maps I loaded into the contouring
system as an overlay to redo 46 contours, which is the clearest evidence I have that the
interface changed what someone could do rather than just how it looked.

What I would do differently: I designed most of this from conversations and from watching
meetings, not from sitting beside someone while they used it. That is the gap in my design
process, and I know it.
