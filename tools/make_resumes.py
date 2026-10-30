"""Build four tailored one-page resume PDFs from one set of facts.

Run from the repo root:  python tools/make_resumes.py

The facts are identical across the four roles. Only the headline, the order of
the sections, and the order inside Skills change, which is what the Crocker
role specs asked for. Writes assets/pdf/russell-mercer-resume-<role>.pdf and
leaves the intermediate HTML in assets/pdf/ so the layout can be checked in a
browser.

Printing uses Microsoft Edge in headless mode, which is already on this machine.
"""

import html
import os
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "pdf")

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

CONTACT = [
    "rmercer2@byu.edu",
    "linkedin.com/in/russell-mercer",
    "github.com/mercer-science",
    "orcid.org/0009-0003-6387-969X",
]

EDUCATION = {
    "heading": "Education",
    "entries": [{
        "role": "Brigham Young University",
        "org": "Provo, UT",
        "dates": "Jan 2024 – Apr 2028 (Expected)",
        "lines": [
            "B.S. Biochemistry; Minor in Computer Science, with machine learning courses",
            "GPA 3.99 &nbsp;·&nbsp; Science GPA 3.99 &nbsp;·&nbsp; MCAT 519 (96th percentile)",
        ],
        "bullets": [],
    }],
}

RESEARCH = {
    "heading": "Research Experience",
    "entries": [
        {
            "role": "Biochemistry Research Assistant",
            "org": "Jensen Lab, BYU",
            "dates": "Aug 2026 – Present",
            "lines": [],
            "bullets": [
                "Scoped two cryo-electron tomography projects on bacterial and parasite "
                "ultrastructure, both approved by the PI and awaiting biosafety review",
                "Testing whether an AI coding agent can run the cryo-ET processing pipeline "
                "with a human approving every step; poster, Utah CryoEM Symposium 2026",
                "Building an AI agent with Dr. Jensen that interviews cryo-EM authors to collect "
                "the tacit knowledge that never reaches print",
            ],
        },
        {
            "role": "Clinical Research Assistant",
            "org": "UT Southwestern Medical Center, Dallas, TX",
            "dates": "May 2026 – Present",
            "lines": [],
            "bullets": [
                "Four studies of MR-guided and biology-guided radiotherapy; first author on three "
                "manuscripts, one submitted and two in final co-author circulation",
                "Rebuilt the department's diffusion MRI pipeline into a web application now "
                "held by the Radiation Oncology Application Team",
                "Wrote the C#, Python, and R extraction and figure pipelines behind the studies",
            ],
        },
        {
            "role": "Chemistry Research Assistant",
            "org": "Stowers Lab, BYU",
            "dates": "Apr 2024 – May 2026",
            "lines": [],
            "bullets": [
                "Second author, <i>Langmuir</i> 2026, on spin-coated metal-organic framework thin films",
                "Helped build and maintain a flow reactor and a UHV chamber (~10⁻¹⁰ Torr, XPS, mass spec)",
                "Trained two newer students in spin coating and SEM imaging",
            ],
        },
    ],
}

# The Coding and Design resumes lead with projects, so Research is cut to the
# facts a reviewer needs and the detail lives in the project sections above it.
RESEARCH_SHORT = {
    "heading": "Research Experience",
    "entries": [
        {
            "role": "Biochemistry Research Assistant",
            "org": "Jensen Lab, BYU",
            "dates": "Aug 2026 – Present",
            "lines": [],
            "bullets": [
                "Two cryo-electron tomography projects I scoped and the PI approved, awaiting "
                "biosafety review; AI agent study presented at the Utah CryoEM Symposium 2026",
            ],
        },
        {
            "role": "Clinical Research Assistant",
            "org": "UT Southwestern Medical Center, Dallas, TX",
            "dates": "May 2026 – Present",
            "lines": [],
            "bullets": [
                "Four studies of MR-guided and biology-guided radiotherapy; first author on three "
                "manuscripts, one submitted and two in final co-author circulation",
            ],
        },
        {
            "role": "Chemistry Research Assistant",
            "org": "Stowers Lab, BYU",
            "dates": "Apr 2024 – May 2026",
            "lines": [],
            "bullets": [
                "Second author, <i>Langmuir</i> 2026; built and maintained a flow reactor and a "
                "UHV chamber (~10⁻¹⁰ Torr, XPS); trained two newer students",
            ],
        },
    ],
}

LEADERSHIP_SHORT = {
    "heading": "Leadership and Service",
    "entries": [
        {
            "role": "Officer",
            "org": "BYU AI Association",
            "dates": "Sep 2026 – Present",
            "lines": [],
            "bullets": [
                "Lead the weekly AI in Research meeting; speak about AI in research to other "
                "colleges across the university and meet with professors and labs",
            ],
        },
        {
            "role": "Lead Program Director",
            "org": "BYU Y-Serve, Early Learning Essentials",
            "dates": "Aug 2024 – Present",
            "lines": [],
            "bullets": ["Run a volunteer program serving preschoolers from low-income families"],
        },
        {
            "role": "Pre-Med Peer Mentor",
            "org": "BYU Pre-Med Association",
            "dates": "Oct 2026 – Present",
            "lines": [],
            "bullets": ["Mentor pre-med students; co-taught two university courses as a BYU peer mentor, 2024 – 2025"],
        },
    ],
}

SOFTWARE = {
    "heading": "Software and Projects",
    "entries": [
        {
            "role": "Diffusion MRI Pipeline and Web App",
            "org": "UT Southwestern",
            "dates": "2026",
            "lines": [],
            "bullets": [
                "Rebuilt a fragile single-workstation pipeline into a web application: bulk "
                "runner with CPU/GPU scheduling, MRI viewer, image creator, threshold tool "
                "that exports contours to the planning system, and voxel-level fit checker",
                "Processed 76 patients in ~2.5 days of server time; handed off with "
                "documentation and training for the postdoc who took it over",
            ],
        },
        {
            "role": "Clinical Data Extraction and Figure Pipelines",
            "org": "UT Southwestern",
            "dates": "2026",
            "lines": [],
            "bullets": [
                "C# script that pulls dose data for every patient despite inconsistent "
                "structure naming; Python filtering and ~1,000 geometric checks per patient",
                "R pipelines that regenerate every figure and table from raw data",
            ],
        },
        {
            "role": "Open Source",
            "org": "github.com/mercer-science",
            "dates": "2026",
            "lines": [],
            "bullets": [
                "<b>paper-engine</b>: skills and scripts that carry an academic paper from "
                "idea toward draft; <b>github-ai-project-manager</b>: skills and hooks that "
                "let an AI agent maintain a research project on GitHub",
                "Full-stack Java client-server chess application (C S 240)",
            ],
        },
    ],
}

DESIGN = {
    "heading": "Design and Build Projects",
    "entries": [
        {
            "role": "Clinical Imaging Workspace",
            "org": "UT Southwestern",
            "dates": "2026",
            "lines": [],
            "bullets": [
                "Designed and built the interface physicians and medical physicists use: "
                "viewer with per-day histograms, parameter comparison, publication image "
                "creator, threshold creator, and a fit checker answering whether a number is real",
                "Iterated from physician feedback; the diffusion overlay let a physician redo 46 contours",
            ],
        },
        {
            "role": "Figures, Posters, and Identity",
            "org": "BYU and UT Southwestern",
            "dates": "2025 – 2026",
            "lines": [],
            "bullets": [
                "Designed a treatment-workflow comparison figure assembled automatically from "
                "slide art and R panels, so revisions cost nothing",
                "Six research posters and talk decks across chemistry, medicine, and structural biology",
                "Rebuilt the SPRI program mark on an axis model after feedback showed the "
                "original read wrong; delivered as an interactive kit",
            ],
        },
    ],
}

CLINICAL = {
    "heading": "Clinical Experience",
    "entries": [
        {
            "role": "Medical Assistant",
            "org": "Health Plus Clinic, Springville, UT",
            "dates": "Jul 2025 – Apr 2026",
            "lines": [],
            "bullets": ["Assisted a D.O. and a P.A. with patient care, procedures, and documentation"],
        },
        {
            "role": "Volunteer",
            "org": "Utah State Hospital, Provo, UT",
            "dates": "May 2025 – Present",
            "lines": [],
            "bullets": ["Guide mental health patients through physical therapy; mentored "
                        "pediatric mental health patients"],
        },
    ],
}

LEADERSHIP = {
    "heading": "Leadership and Service",
    "entries": [
        {
            "role": "Officer",
            "org": "BYU AI Association",
            "dates": "Sep 2026 – Present",
            "lines": [],
            "bullets": [
                "Lead the weekly AI in Research meeting; speak to other colleges across the "
                "university and meet with professors and labs about using AI in their work",
                "Represented the association at BYU's AI for Social Innovation Conference, "
                "on the Data Sovereignty and Inclusion working table",
            ],
        },
        {
            "role": "Lead Program Director",
            "org": "BYU Y-Serve, Early Learning Essentials",
            "dates": "Aug 2024 – Present",
            "lines": [],
            "bullets": ["Run a volunteer program serving preschoolers from low-income families"],
        },
        {
            "role": "Pre-Med Peer Mentor",
            "org": "BYU Pre-Med Association",
            "dates": "Oct 2026 – Present",
            "lines": [],
            "bullets": ["Mentor pre-med students on coursework, research, and applications"],
        },
        {
            "role": "University Peer Mentor",
            "org": "BYU Office of First Year Experience",
            "dates": "Jun 2024 – Feb 2025",
            "lines": [],
            "bullets": ["Co-taught two university courses and mentored 45 freshmen"],
        },
    ],
}

SIDE_AWARDS = {
    "heading": "Awards",
    "items": [
        "<b>SCCR Fellow</b>, BYU Simmons Center for Cancer Research, 2026",
        "<b>Outstanding Analytical Chemist</b>, 2025",
        "<b>Dean's List</b>, four semesters, 2024 – 2025",
        "<b>Undergraduate Research Award</b>, each semester, Stowers Lab",
    ],
}

SIDE_PUBS = {
    "heading": "Publications",
    "items": [
        "Ralph AD, <b>Mercer RW</b>, et al. <i>Langmuir</i> 2026;42(6):4475–88.",
        "<b>First author on three manuscripts:</b> one submitted (<i>Int J Radiat Oncol "
        "Biol Phys</i>) and two in final co-author circulation.",
        "Co-author on two more in final circulation, with others in preparation.",
    ],
}

SIDE_PRESENTATIONS = {
    "heading": "Presentations",
    "items": [
        "Utah CryoEM Symposium, 2026",
        "BYU Simmons Center for Cancer Research, 2026",
        "BYU Medical Society, 2026",
        "ACS Spring Meeting, Atlanta, 2026",
        "BYU Student Research Conference, 2025 and 2026",
    ],
}

SKILLS_WETLAB = [
    "<b>Wet Lab:</b> bacterial culture and plasmid work, MOF synthesis, spin coating, SEM, "
    "UHV and XPS, Vitrobot, Krios cryo-TEM",
    "<b>Computation:</b> Python, R, C#, Java, shell, Git, AI coding agents, DICOM and image pipelines",
    "<b>Communication:</b> first author on three manuscripts; six research presentations",
]

SKILLS_CODE = [
    "<b>Languages:</b> Python, R, C#, Java, shell",
    "<b>Tools:</b> Git and GitHub, AI coding agents and agent skills, web applications, "
    "GPU workflows, DICOM and medical imaging",
    "<b>Coursework:</b> C S 111, 235, 236, 240; machine learning courses C S 312 and 470 planned; MATH 213, 215; STAT 121",
    "<b>Lab:</b> SEM, UHV and XPS, Vitrobot, Krios, bacterial culture",
]

SKILLS_DESIGN = [
    "<b>Design:</b> user research with clinicians, interface design, data visualization, "
    "figure and poster design, rapid prototyping",
    "<b>Tools:</b> PowerPoint, ImageJ, ggplot2 and matplotlib, HTML and CSS, SVG",
    "<b>Code:</b> Python, R, C#, Java, AI coding agents",
    "<b>Lab and Clinical:</b> SEM, UHV, cryo-EM sample preparation, clinical data abstraction",
]

SKILLS_BALANCED = [
    "<b>Lab:</b> cryo-EM sample preparation, bacterial culture, MOF synthesis, SEM, UHV and XPS",
    "<b>Code:</b> Python, R, C#, Java, shell, AI coding agents, imaging pipelines",
    "<b>Clinical:</b> chart review, clinical data abstraction, medical assisting, study design",
    "<b>Leadership:</b> program direction, mentoring, cross-disciplinary teams, AI policy discussion",
]

ROLES = {
    "igem": {
        # Russell's own wording, from the resume he wrote himself.
        "headline": "Biochemistry student preparing for medical school, with research in "
                    "radiation oncology, surface chemistry, and cryo-electron tomography. "
                    "Enjoys learning new things and being challenged in new ways.",
        "main": [EDUCATION, RESEARCH, CLINICAL, LEADERSHIP],
        "skills": SKILLS_WETLAB,
        "side": [SIDE_PUBS, SIDE_AWARDS, SIDE_PRESENTATIONS],
    },
    "coding": {
        "headline": "Biochemistry student preparing for medical school, who writes the "
                    "software behind his research in radiation oncology, surface chemistry, "
                    "and cryo-electron tomography. Enjoys learning new things and being "
                    "challenged in new ways.",
        "main": [EDUCATION, SOFTWARE, RESEARCH_SHORT, LEADERSHIP_SHORT],
        "skills": SKILLS_CODE,
        "side": [SIDE_PUBS, SIDE_AWARDS, SIDE_PRESENTATIONS],
    },
    "design": {
        "headline": "Biochemistry student preparing for medical school, who designs the tools "
                    "and interfaces clinicians and researchers use, from radiation oncology to "
                    "the lab bench. Enjoys learning new things and being challenged in new "
                    "ways.",
        "main": [EDUCATION, DESIGN, RESEARCH_SHORT, LEADERSHIP_SHORT],
        "skills": SKILLS_DESIGN,
        "side": [SIDE_PUBS, SIDE_AWARDS, SIDE_PRESENTATIONS],
    },
    "wildcard": {
        "headline": "Biochemistry student preparing for medical school, with research in "
                    "radiation oncology, surface chemistry, and cryo-electron tomography, and "
                    "the code and leadership that tie them together. Enjoys learning new "
                    "things and being challenged in new ways.",
        "main": [EDUCATION, RESEARCH, CLINICAL, LEADERSHIP],
        "skills": SKILLS_BALANCED,
        "side": [SIDE_PUBS, SIDE_AWARDS, SIDE_PRESENTATIONS],
    },
}

CSS = """
@page { size: letter; margin: 0.45in 0.5in; }
* { box-sizing: border-box; }
body { margin:0; font: 9.1pt/1.28 Calibri, "Segoe UI", Arial, sans-serif; color:#1b1b1f; }
.top { display:flex; justify-content:space-between; align-items:flex-start; gap:12pt;
       border-bottom:1.2pt solid #1f4f7a; padding-bottom:5pt; margin-bottom:7pt; }
.who h1 { margin:0; font-size:21pt; letter-spacing:-0.4pt; color:#13334f; }
.who p { margin:1.5pt 0 0; font-size:8.9pt; line-height:1.3; font-style:italic;
         color:#3f4a55; max-width:30em; }
.contact { text-align:right; font-size:8.4pt; color:#3f4a55; line-height:1.45; white-space:nowrap; }
.cols { display:flex; gap:14pt; align-items:flex-start; }
.main { flex:1 1 68%; }
.side { flex:0 0 29%; }
h2 { font-size:9.4pt; text-transform:uppercase; letter-spacing:0.6pt; color:#1f4f7a;
     border-bottom:0.6pt solid #c9d4de; margin:7pt 0 2.5pt; padding-bottom:1.5pt; }
.side h2 { margin-top:0; }
.side h2 + * { margin-top:0; }
.side section + section h2 { margin-top:9pt; }
.entry { margin-bottom:4pt; }
.entry .line1 { display:flex; justify-content:space-between; gap:8pt; }
.entry .what { font-weight:700; }
.entry .org { font-style:italic; color:#3f4a55; }
.entry .dates { color:#56606b; font-size:8.5pt; white-space:nowrap; }
.entry .note { color:#3f4a55; }
ul { margin:1pt 0 0; padding-left:11pt; }
li { margin:0.6pt 0; }
.side ul { padding-left:9pt; }
.side li { margin:1.4pt 0; font-size:8.6pt; line-height:1.3; }
.skills li { margin:1.4pt 0; }
"""


def print_pdf(src_html, pdf_path):
    """Print an HTML file to PDF through headless Edge.

    Edge keeps a disk cache, and printing the same path twice can hand back the
    previous render, which is how a stale PDF slips out. Giving it a throwaway
    cache and profile each time removes that.
    """
    cache = tempfile.mkdtemp(prefix="edge-print-")
    try:
        subprocess.run(
            [EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             "--user-data-dir=%s" % cache, "--disk-cache-dir=%s" % os.path.join(cache, "c"),
             "--print-to-pdf=%s" % pdf_path, src_html],
            check=True, capture_output=True, timeout=180)
        # Edge can still be flushing the file when it exits, which is how a
        # half-written PDF gets read back. Wait for the size to settle.
        last, stable = -1, 0
        for _ in range(60):
            size = os.path.getsize(pdf_path) if os.path.exists(pdf_path) else -1
            stable = stable + 1 if size == last and size > 0 else 0
            if stable >= 3:
                break
            last = size
            time.sleep(0.1)
    finally:
        shutil.rmtree(cache, ignore_errors=True)


def entry_html(e):
    bits = ['<div class="entry"><div class="line1"><span><span class="what">%s</span>'
            '%s</span><span class="dates">%s</span></div>'
            % (e["role"],
               (' &nbsp;·&nbsp; <span class="org">%s</span>' % e["org"]) if e.get("org") else "",
               e["dates"])]
    for line in e.get("lines", []):
        bits.append('<div class="note">%s</div>' % line)
    if e.get("bullets"):
        bits.append("<ul>%s</ul>" % "".join("<li>%s</li>" % b for b in e["bullets"]))
    bits.append("</div>")
    return "".join(bits)


def section_html(sec):
    return '<section><h2>%s</h2>%s</section>' % (
        sec["heading"], "".join(entry_html(e) for e in sec["entries"]))


def side_html(sec):
    return '<section><h2>%s</h2><ul>%s</ul></section>' % (
        sec["heading"], "".join("<li>%s</li>" % i for i in sec["items"]))


def resume_body(role_id):
    """The resume itself, without a page wrapper.

    build.py drops this straight into the Resume tab, so the page and the PDF
    come from one set of facts and cannot drift apart.
    """
    role = ROLES[role_id]
    main = "".join(section_html(s) for s in role["main"])
    main += '<section><h2>Skills</h2><ul class="skills">%s</ul></section>' % "".join(
        "<li>%s</li>" % s for s in role["skills"])
    side = "".join(side_html(s) for s in role["side"])
    return """<div class="top">
<div class="who"><h1>Russell Mercer</h1><p>%s</p></div>
<div class="contact">%s</div>
</div>
<div class="cols"><div class="main">%s</div><div class="side">%s</div></div>""" % (
        html.escape(role["headline"]), "<br>".join(CONTACT), main, side)


def build_html(role_id, role):
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Russell Mercer Resume, %s</title><style>%s</style></head><body>
%s
</body></html>""" % (html.escape(role_id), CSS, resume_body(role_id))


def main():
    os.makedirs(OUT, exist_ok=True)
    if not os.path.exists(EDGE):
        print("Edge not found at %s; wrote HTML only." % EDGE)
    for role_id, role in ROLES.items():
        htm = os.path.join(OUT, "russell-mercer-resume-%s.html" % role_id)
        pdf = os.path.join(OUT, "russell-mercer-resume-%s.pdf" % role_id)
        with open(htm, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(build_html(role_id, role))
        if os.path.exists(EDGE):
            print_pdf(htm, pdf)
            print("wrote %s" % os.path.basename(pdf))
        else:
            print("wrote %s" % os.path.basename(htm))


if __name__ == "__main__":
    sys.exit(main())
