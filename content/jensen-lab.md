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

I joined Dr. Grant Jensen's lab in August 2026, where I work with cryo-electron tomography (cryo-ET). The technique involves rapidly freezing cells to preserve their native structure, then imaging them from multiple angles to reconstruct their internal organization at molecular resolution. My work in the lab has two main parts: imaging bacteria and parasites that have not previously been studied using cryo-ET, and exploring AI agents and skills to help researchers carry out the image-processing workflow.

[figure: pipeline]

#### Imaging Bartonella henselae and Babesia duncani

I proposed two projects involving organisms associated with tick-borne infections. Both can occur alongside Lyme disease, and patients may be infected with multiple organisms at once. I have tested positive for both of these pathogens through PCR. Neither genus has been studied using cryo-ET, so these projects will provide the first structural images of either organism using this technique.

*Bartonella henselae* a gram-negative bacterium primarily transmitted through scratches or bites from infected cats and is the primary cause of cat-scratch disease. It commonly causes swollen, tender lymph nodes, fever, fatigue, and headaches, but can occasionally lead to more serious neurological, ocular, or cardiac complications. Its cells are approximately 0.3–0.5 µm wide, allowing them to be frozen and imaged whole on BYU's Krios microscope without additional thinning. They also divide approximately every three hours, making it practical to maintain cultures.

There is also an interesting biological question behind the project. *B. henselae* has a dense surface layer of adhesins, and one published hypothesis proposes that this layer interferes with the bacterium's secretion system, which it uses to deliver proteins into host cells. This hypothesis is based on observed phenotypes rather than direct structural evidence. Cryo-ET could help determine whether the proposed interaction is supported by the organism's actual structure.

The second project focuses on *Babesia duncani*. These parasites invade red blood cells using a specialized structure at one end of the cell called the apical complex. They are a tick-borne, malaria-like parasite that infects red blood cells and causes babesiosis. Symptoms commonly include fever, chills, fatigue, sweating, headaches, and hemolytic anemia due to the destruction of infected red blood cells. Severe infections can cause organ dysfunction, particularly in immunocompromised individuals or those without a functioning spleen. A 2026 study identified a previously unreported tubulin rosette in the apical region of a related species using light microscopy. However, that technique cannot resolve the rosette's detailed molecular organization. Cryo-ET could provide a closer look.

This project presents additional technical challenges. *Babesia* cells are too thick to image intact, so they will require focused ion beam (FIB) milling at the University of Utah. No established FIB-milling workflow exists for *Babesia*, so developing and optimizing one is part of the project.

I developed the proposals and experimental plans for both projects, which Dr. Jensen approved in October 2026.

These studies are promising for biology and medical science because as someone learns the structure of a bacteria (through cryo-ET) it becomes a lot easier to develop therapeutics, etc for them.

#### Using AI to Accelerate Cryo-ET Processing

Processing cryo-ET data requires coordinating approximately a dozen specialized programs, each with its own parameters and potential failure points. Learning the workflow can take a researcher several months. Data in general is very difficult to process, and it is usually the bottle neck of this field of research.

In a separate project, I developed a workflow in which a general-purpose AI coding agent operates this processing pipeline. I tested it on 39 *E. coli* tilt series. The agent can recommend and execute processing steps. I also logged each recommendation as accepted, overridden, or an error identified by the human reviewer. This makes it possible to evaluate the agent's performance rather than simply judging whether it appears to work.

[figure: agent-loop]

During testing, the agent identified two incorrect values recorded by the microscope and independently checked the tools it was using. It also made mistakes, which have been documented as part of the evaluation. In every case, it eventually caught itself. I presented this work at the Utah CryoEM Symposium on October 8, 2026. A manuscript is currently in preparation, after a few instructory videos will be made. This is a collaborative project with Chitral Chatterjee.

[figure: numbers]

[figure: poster]

#### Building a Cryo-EM Knowledge Database

Another project in the lab addresses something that is difficult to learn from published papers: the practical knowledge researchers accumulate while developing and troubleshooting experiments. Papers generally describe the final methods, but not necessarily the approaches that were abandoned, the problems encountered, or the small adjustments that made a protocol work.

Dr. Jensen proposed creating a database to preserve this knowledge. I am developing an AI agent that interviews authors of cryo-EM papers and collects details about their experimental decisions and troubleshooting processes. It will then compile all of their information into a universal database that researchers around the world can use to learn and to train their AI agents. The project is still in development, and a working system has not yet been completed.
