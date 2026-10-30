---
title: Jensen Lab, BYU
roles: [igem, wildcard]
tabs: [physical-sciences]
status: Ongoing
dates: August 2026 to present
heading_before: Jensen Lab
images:
  - size: wide
    src: assets/img/cryoet-poster.png
    alt: The conference poster, titled Can an AI Agent Collapse the Cryo-ET Learning Curve, with panels on how cryo-ET works, how the agent was used, excerpts from the session, what it got right, and a summary of the numbers.
    caption: The poster I presented at the Utah CryoEM Symposium in October 2026. Click it to read the panels.
  - size: small
    src: assets/img/cryoet-pipeline.png
    alt: Diagrams of the cryo-ET workflow, from growing cells through plunge freezing, milling, and tilting, then motion correction, alignment, reconstruction, and averaging.
    caption: The chain of steps a tilt series goes through before it answers anything. Learning it is normally the slow part.
  - size: small
    src: assets/img/cryoet-numbers.png
    alt: A summary panel reading 39 tilt series, 1,210 raw movies, zero workflow steps given, four packages installed, two wrong microscope values caught, and 24 minutes to the first tomogram.
    caption: What the agent did on the test set, including the two wrong values it caught in the microscope's own records.
---

I joined Dr. Grant Jensen's lab in August 2026. The lab does cryo-electron tomography:
freezing cells fast enough that the water never crystallizes, then imaging them from many
angles and rebuilding what the inside looked like, down to individual molecules sitting
where they actually sit. I work on two fronts there, imaging bacteria and parasites that
nobody has looked at this way, and testing whether an AI agent can get a new student
through the processing faster than the usual several months.

#### Why These Two Organisms

Both are tick-borne infections that often show up alongside Lyme disease, and patients
frequently carry more than one at a time. Neither genus has ever been imaged by cryo-ET,
so anything we get is the first picture anyone has of it. That is unusual. Most structural
targets have been worked over for years.

*Bartonella henselae* was the better one to start with for practical reasons. The cells run
0.3 to 0.5 µm across, small enough to freeze whole and image directly on BYU's Krios
without thinning them first, and they double in about three hours, so cultures do not hold
up the schedule. There is also a specific claim waiting to be tested. The bacterium carries
a dense coat of adhesin on its surface, and a published hypothesis says that coat blocks
the secretion system it uses to inject proteins into host cells. That argument rests on
phenotypes alone, because nobody has looked.

*Babesia duncani* is the harder one, which is why it runs second. It invades red blood
cells using a machine at one end called the apical complex, and a 2026 paper found a new
tubulin rosette at that end in a sister species using light microscopy. Light microscopy
cannot resolve what the rosette is made of or how it is arranged; cryo-ET can. These cells
are too thick to image whole, so they need focused ion beam milling at the University of
Utah, and no milling workflow exists for any *Babesia*. Part of the project is building
one.

I scoped and proposed both projects and wrote the plans. Dr. Jensen approved them in
October 2026. **Both are waiting on institutional biosafety approval, which comes before
anything is ordered or cultured, so there are no grids, no images, and no data yet.**

#### Can an AI Agent Shorten the Learning Curve?

Getting from raw tilt series to a biological answer means running a dozen specialized
programs, each with its own settings and its own ways of failing quietly. For my other
project I put a general-purpose AI coding agent at the controls of that chain, on 39 tilt
series of *E. coli*, with one rule: the agent proposes and runs, and a human approves,
overrides, or corrects every parameter. Every recommendation gets logged as accepted,
overridden, or an error a human caught, which is what turns an impression into a
measurement.

It caught two values the microscope itself had recorded wrong, and it checked its own tools
rather than trusting them. It also failed in ways worth writing down. I presented this at
the Utah CryoEM Symposium on October 8, 2026, and a manuscript is in preparation. This is
joint work with Chitral Chatterjee.

#### Cryo-EM Tacit Knowledge Database

A paper tells you what worked, not what the authors ruled out first or which step everyone
in the field quietly does differently. This project collects that reasoning through an AI
agent that interviews the authors of cryo-EM papers while they still remember it. Dr.
Jensen originated the idea and I am building it. Nothing is working yet.

#### Training at the Bench

In the lab's September 2026 bootcamp I grew *E. coli* BL21 Star (DE3) carrying a human
ferritin H expression plasmid, made LB and 2×YT media, and ran overnight starters,
induction, and a plasmid miniprep on the lab's protocol. I have done the culture steps so
far; purification and grid preparation come next. In October I took Thermo Fisher's
Resolution Evolution course, with hands-on time on the Vitrobot for plunge-freezing and on
the Krios.
