---
title: Jensen Lab, BYU
roles: [igem, wildcard]
tabs: [physical-sciences]
status: ""
dates: August 2026 to present
heading_before: Jensen Lab
images:
  - id: pipeline
    size: wide
    src: assets/img/cryoet-pipeline.png
    alt: Diagrams of the cryo-ET workflow, from growing cells through plunge freezing, milling a lamella, and tilting the specimen for imaging.
    caption: "How a cell becomes a tilt series: grow, freeze, thin, then image from many angles."
  - id: agent-loop
    size: wide
    src: assets/img/cryoet-agent-loop.png
    alt: A diagram with the student on the left, the AI agent in the middle, and the computers on the right, with arrows running both ways between them.
    caption: "The loop, and the rules it runs under. The agent proposes and executes; I approve, override, or correct at every step."
  - id: numbers
    size: wide
    src: assets/img/cryoet-numbers.png
    alt: A summary panel reading 39 tilt series, 1,210 raw movies, zero workflow steps given, four packages installed, two wrong microscope values caught, and 24 minutes to the first tomogram.
    caption: The test set, and what the agent did with it.
  - id: poster
    size: wide
    src: assets/img/cryoet-poster.png
    alt: The conference poster, titled Can an AI Agent Collapse the Cryo-ET Learning Curve, laid out in six numbered sections across three columns.
    caption: The poster I presented at the Utah CryoEM Symposium, October 8, 2026. Click it to read the panels.
---

I joined Dr. Grant Jensen's lab in August 2026, where I work with cryo-electron tomography
(cryo-ET). The technique rapidly freezes cells to preserve their native structure, then
images them from many angles to reconstruct their internal organization at molecular
resolution. My work has two parts: imaging bacteria and parasites that have never been
studied this way, and building AI agents and skills that help researchers get through the
image-processing workflow.

[figure: pipeline]

#### Imaging Bartonella henselae and Babesia duncani

I proposed two projects on organisms associated with tick-borne infections. Both can occur
alongside Lyme disease, and a patient may carry several at once. I have tested positive for
both of these pathogens by PCR. Neither genus has been studied by cryo-ET, so these
projects would produce the first structural images of either organism using the technique.

*Bartonella henselae* is a gram-negative bacterium transmitted mainly through scratches or
bites from infected cats, and it is the primary cause of cat-scratch disease. It usually
brings swollen, tender lymph nodes, fever, fatigue, and headaches, though it can lead to
neurological, ocular, or cardiac complications. The cells run about 0.3 to 0.5 µm wide,
which means they can be frozen and imaged whole on BYU's Krios without additional thinning,
and they divide roughly every three hours, so cultures are practical to keep.

There is an interesting biological question behind the project. *B. henselae* carries a
dense surface layer of adhesins, and one published hypothesis holds that this layer
interferes with the secretion system the bacterium uses to deliver proteins into host
cells. That hypothesis rests on observed phenotypes rather than on direct structural
evidence. Cryo-ET could show whether the organism's actual structure supports it.

The second project is *Babesia duncani*, a tick-borne, malaria-like parasite that invades
red blood cells using a specialized structure at one end of the cell, the apical complex.
It causes babesiosis, which typically brings fever, chills, fatigue, sweating, headaches,
and hemolytic anemia as infected red blood cells are destroyed. Severe infections can cause
organ dysfunction, particularly in people who are immunocompromised or who have no
functioning spleen. A 2026 study identified a previously unreported tubulin rosette in the
apical region of a related species using light microscopy, but that technique cannot
resolve the rosette's molecular organization. Cryo-ET could provide a closer look.

This one carries extra technical difficulty. *Babesia* cells are too thick to image intact,
so they require focused ion beam (FIB) milling at the University of Utah, and no
established FIB-milling workflow exists for *Babesia*. Developing and optimizing one is
part of the project.

I wrote the proposals and experimental plans for both, and Dr. Jensen approved them in
October 2026.

Both matter beyond the pictures. Seeing how an organism is actually built is what makes it
possible to design against it, because a drug has to fit something real, and for these two
nobody has seen the thing yet.

#### Using AI to Accelerate Cryo-ET Processing

Processing cryo-ET data means coordinating about a dozen specialized programs, each with
its own parameters and its own failure points, and learning that workflow can take a
researcher several months. Processing is generally the bottleneck of the field.

In a separate project I built a workflow in which a general-purpose AI coding agent
operates that pipeline, and I tested it on 39 *E. coli* tilt series. The agent recommends
and executes processing steps, and I logged every recommendation as accepted, overridden,
or an error the human reviewer caught. That log is what makes it possible to evaluate the
agent's performance rather than judge whether it appears to work.

[figure: agent-loop]

During testing the agent identified two incorrect values recorded by the microscope and
independently checked the tools it was using. It also made mistakes, documented as part of
the evaluation; in every case it eventually caught itself. I presented this work at the
Utah CryoEM Symposium on October 8, 2026. A manuscript is in preparation, to follow a few
instructional videos. This is a collaborative project with Chitral Chatterjee.

[figure: numbers]

[figure: poster]

#### Building a Cryo-EM Knowledge Database

Another project addresses something papers teach poorly: the practical knowledge
researchers accumulate while developing and troubleshooting experiments. A paper describes
the final method, not the approaches abandoned along the way, the problems met, or the
small adjustments that made a protocol work.

Dr. Jensen proposed building a database to preserve that knowledge. I am developing an AI
agent that interviews the authors of cryo-EM papers about their experimental decisions and
their troubleshooting, then compiles what it gathers into a shared database researchers
anywhere can use, both to learn from and to train their own agents. The project is still in
development and a working system does not exist yet.

#### Training at the Bench

In the lab's September 2026 bootcamp I grew *E. coli* BL21 Star (DE3) carrying a human
ferritin H expression plasmid, prepared LB and 2×YT media, and ran overnight starters,
induction, and a plasmid miniprep on the lab's protocol. I have done the culture steps so
far. In October I completed Thermo Fisher's Resolution Evolution course, with hands-on time
on the Vitrobot for plunge-freezing and on the Krios.
