"""Build the CV, both the PDF and the markup the CV tab renders.

Run from the repo root:  python tools/make_cv.py

Same arrangement as make_resumes.py: the facts live here once, build.py renders
this markup on the page, and the PDF prints from it, so the page and the
download cannot disagree.

Ported from Russell Mercer CV.docx. Three things were changed on the way over,
because this one is public:
  - The draft's [TODO: authors and title] markers are gone. Each entry says what
    the work is and where it stands instead of advertising a gap
  - The phlebotomy certification carries its end date, since it has expired
  - The phone number is left off. Email and the profile links are enough for a
    public page; add it back to CONTACT below if you want it
"""

import html
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_resumes  # noqa: E402  (shares the headless-Edge printing helper)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "pdf")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

NAME = "Russell W. Mercer"
CONTACT = [
    "Provo, UT",
    "rmercer2@byu.edu",
    "linkedin.com/in/russell-mercer",
    "orcid.org/0009-0003-6387-969X",
    "github.com/mercer-science",
]

# Each section is a heading plus entries. An entry is either
#   {"what", "where", "dates", "note", "bullets"}  for a position, or
#   {"text", "dates"}                              for a single line.
SECTIONS = [
    {
        "heading": "Education",
        "entries": [
            {
                "what": "Brigham Young University, Provo, UT",
                "dates": "January 2024 – April 2028 (Expected)",
                "note": "B.S. in Biochemistry, Minor in Computer Science "
                        "(machine learning emphasis)",
                "bullets": [
                    "Cumulative GPA 3.99; Science GPA 3.99",
                    "Advanced biochemistry, pre-medical, and machine learning coursework",
                ],
            },
            {"text": "Medical College Admission Test (MCAT): 519, 96th percentile",
             "dates": "August 2026"},
        ],
    },
    {
        "heading": "Research Experience",
        "entries": [
            {
                "what": "Biochemistry Research Assistant, Jensen Lab, BYU",
                "dates": "August 2026 – Present",
                "note": "Department of Chemistry and Biochemistry. Mentor: Grant J. Jensen, "
                        "PhD, Dean, College of Physical and Mathematical Sciences; "
                        "with Chitral Chatterjee",
                "bullets": [
                    "Scoped and proposed two cryo-electron tomography projects, approved by "
                    "the PI and awaiting institutional biosafety review: the surface "
                    "architecture of <i>Bartonella henselae</i>, and the apical complex of "
                    "<i>Babesia duncani</i>",
                    "Testing whether a general-purpose AI coding agent can shorten the "
                    "cryo-electron tomography learning curve for a new researcher without "
                    "replacing the understanding the work normally builds",
                    "Processing 39 tilt series of cryo-FIB-milled, exponentially growing "
                    "<i>E. coli</i> through motion correction, alignment, reconstruction, "
                    "missing-wedge correction, template matching, classification, and "
                    "subtomogram averaging, ending in a ribosome neighbor analysis",
                    "Recording which agent recommendations are accepted, overridden, or "
                    "caught as errors, and packaging the workflow as a reusable agent skill",
                ],
            },
            {
                "what": "Clinical Research Assistant, UT Southwestern Medical Center",
                "dates": "May 2026 – Present",
                "note": "Radiation Oncology, Kenneth Westover, MD, PhD (May to August 2026); "
                        "Medical Physics, Jie Deng, PhD (August 2026 to present)",
                "bullets": [
                    "Started through the BYU Summer Premedical Research Internship, funded by "
                    "the BYU Simmons Center for Cancer Research; on site in Dallas, TX through "
                    "August 2026 and remote since",
                    "Four studies: lung and pancreas diffusion-weighted MRI on the Elekta Unity "
                    "MR-Linac, biology-guided radiotherapy on RefleXion, and radiolucent patient "
                    "immobilization. First author on three manuscripts, one submitted and two in "
                    "final co-author circulation, with more in preparation",
                    "Rebuilt the department's diffusion MRI processing pipeline into a web "
                    "application with a bulk runner, viewer, threshold tool, and fit checker; "
                    "ran 76 patients in about 2.5 days of server time, and hospital IT moved it "
                    "to the Radiation Oncology Application Team for clinical use",
                    "Wrote the C#, Python, and R extraction and figure pipelines behind the "
                    "studies; abstracted clinical data in Epic; wrote the hand-off document and "
                    "trained the postdoc who inherited the pipeline",
                    "Offered a continuing position in Medical Physics after the summer internship",
                ],
            },
            {
                "what": "Chemistry Research Assistant, Stowers Lab, BYU",
                "dates": "April 2024 – May 2026",
                "note": "Department of Chemistry and Biochemistry. Mentor: Kara J. Stowers, PhD",
                "bullets": [
                    "Synthesized surface-bound metal-organic framework thin films "
                    "(CuBDC/DABCO, HKUST-1) by spin coating and studied their structure and "
                    "decomposition",
                    "Helped build, repair, and maintain a flow reactor and an ultra-high-vacuum "
                    "chamber reaching about 10⁻¹⁰ Torr, with X-ray photoelectron spectroscopy "
                    "and mass spectrometry",
                    "Trained newer lab members in spin coating and SEM imaging",
                    "Supported by a BYU Undergraduate Research Award; still contributing to a "
                    "manuscript in preparation",
                ],
            },
        ],
    },
    {
        "heading": "Publications",
        "subheads": True,
        "entries": [
            {"subhead": "Peer-Reviewed"},
            {"text": "Ralph AD, <b>Mercer RW</b>, Hall SB, Butikofer BC, Collins CS, "
                     "Sturgill CJ, Minson PS, Stefik M, Stowers KJ. Ambient pressure "
                     "fabrication of Cu<sub>x</sub>Zn<sub>1−x</sub>(BDC)<sub>2</sub>DABCO thin "
                     "films through spin-coating and their temperature-dependent structural "
                     "development. <i>Langmuir</i>. 2026;42(6):4475–4488. "
                     "doi:10.1021/acs.langmuir.5c05182"},
            {"subhead": "Submitted"},
            {"text": "<b>Mercer RW</b>, et al. Onboard intravoxel incoherent motion "
                     "diffusion-weighted MRI tracks early tumor-volume response in ultra-central "
                     "lung tumors treated with PULSAR. UT Southwestern. Submitted to the "
                     "<i>International Journal of Radiation Oncology, Biology, Physics</i>, "
                     "October 2026."},
            {"subhead": "In Co-Author Circulation"},
            {"text": "<b>Mercer RW</b>, et al. Dosimetric cost of a smaller target when using "
                     "biology-guided radiation therapy for lung cancer. UT Southwestern."},
            {"text": "<b>Mercer RW</b>, et al. Radiolucent stereotactic body frame for online "
                     "adaptive radiation therapy. UT Southwestern."},
            {"text": "Benefits of weekly on-demand adaptive radiation therapy for locally "
                     "advanced lung cancer in responders. Co-author. UT Southwestern."},
            {"text": "Online adaptive radiation therapy for early-stage lung SABR. Co-author. "
                     "UT Southwestern."},
            {"subhead": "In Preparation"},
            {"text": "<b>Mercer RW</b>, et al. Pancreas diffusion-weighted MRI on the Elekta "
                     "Unity MR-Linac. UT Southwestern."},
            {"text": "<b>Mercer RW</b>, Chatterjee C, Jensen GJ. Using an AI coding agent to "
                     "learn cryo-electron tomography processing. Jensen Lab, BYU."},
            {"text": "Co-author, surface chemistry in the Stowers Lab ultra-high-vacuum "
                     "chamber. BYU."},
            {"text": "Author order on manuscripts still in review is not final.",
             "quiet": True},
        ],
    },
    {
        "heading": "Presentations and Abstracts",
        "entries": [
            {"text": "<b>Mercer RW</b>, Chatterjee C, Jensen GJ. Can an AI agent collapse the "
                     "cryo-ET learning curve? Poster, Utah CryoEM Symposium, Brigham Young "
                     "University, Provo, UT.", "dates": "October 2026"},
            {"text": "Invited guest talk on UT Southwestern research and AI in research. "
                     "HL 385R, Healthcare Research Hub, BYU Healthcare Leadership, Marriott "
                     "School of Business, Provo, UT.", "dates": "October 2026"},
            {"text": "UT Southwestern radiation oncology research. Poster, BYU Medical Society, "
                     "Provo, UT.", "dates": "August 2026"},
            {"text": "UT Southwestern radiation oncology research. Oral presentation, BYU "
                     "Simmons Center for Cancer Research, Provo, UT.", "dates": "August 2026"},
            {"text": "Metal-organic framework thin films. American Chemical Society Spring "
                     "Meeting, Atlanta, GA.", "dates": "March 2026"},
            {"text": "Metal-organic framework thin films. BYU Student Research Conference, "
                     "Provo, UT.", "dates": "February 2026"},
            {"text": "Fast room temperature synthesis and characterization of a surface bound "
                     "metal organic framework without the use of a self-assembling monolayer. "
                     "BYU Student Research Conference, Provo, UT.", "dates": "March 2025"},
        ],
    },
    {
        "heading": "Honors, Awards, and Funding",
        "entries": [
            {"text": "SCCR Fellow, BYU Simmons Center for Cancer Research (funded summer "
                     "research at UT Southwestern)", "dates": "2026"},
            {"text": "Outstanding Analytical Chemist Award, BYU", "dates": "2025"},
            {"text": "Dean's List, BYU (Winter, Spring, and Fall 2024; Fall 2025)",
             "dates": "2024 – 2025"},
            {"text": "Undergraduate Research Award, BYU (awarded each semester)",
             "dates": "2024 – 2026"},
            {"text": "Stoney Black Flight of the Phoenix Award, Air Academy High School "
                     "Marching Band", "dates": "2021"},
            {"text": "Eagle Scout, Boy Scouts of America", "dates": "2020"},
        ],
    },
    {
        "heading": "Clinical Experience",
        "entries": [
            {
                "what": "Medical Assistant, Health Plus Clinic, Springville, UT",
                "dates": "July 2025 – April 2026",
                "bullets": [
                    "Assisted a D.O. and a P.A. with patient care and clinical procedures",
                    "Kept medical records accurate and compliant; completed HIPAA and medical "
                    "assistant training",
                ],
            },
            {
                "what": "Volunteer, Utah State Hospital, Provo, UT",
                "dates": "May 2025 – Present",
                "bullets": [
                    "Physical Therapy (May 2025 to present): guide 10+ mental health patients "
                    "through therapeutic exercise and help the physical therapist keep sessions "
                    "safe and encouraging",
                    "Pediatric Center (September 2025 to January 2026): led group activities "
                    "for pediatric mental health patients",
                    "Pediatric Mentor (December 2025 to May 2026): met one-on-one with "
                    "pediatric mental health patients",
                ],
            },
        ],
    },
    {
        "heading": "Physician Shadowing",
        "entries": [
            {"text": "Steven M. Grover, Robotic Gynecologic Surgery, Utah Valley Hospital, "
                     "3.5 hours", "dates": "October 2026"},
            {"text": "Thomas Fowler, Allergy, 4 hours", "dates": "June 2026"},
            {"text": "Stanford C. Taylor, Retina Surgery, Pueblo, CO, 6 hours",
             "dates": "April 2026"},
            {"text": "Matheson Harris, Plastic Surgery (Facial Reconstruction), Utah Surgical, "
                     "7.5 hours", "dates": "November 2025"},
            {"text": "Michael Benson, Psychiatry, Utah State Hospital, 8 hours",
             "dates": "August 2025"},
            {"text": "Dan Baer, Pain Management (PM&amp;R), 3.5 hours", "dates": "July 2025"},
            {"text": "James Barrott, General Surgery; Joshua Jaramillo, Trauma Surgery and ICU; "
                     "Eric Cannon, Anesthesia. Scheduled.", "dates": "November – December 2026"},
        ],
    },
    {
        "heading": "Leadership and Teaching",
        "entries": [
            {
                "what": "Officer, BYU AI Association",
                "dates": "September 2026 – Present",
                "bullets": [
                    "Lead the weekly AI in Research meeting",
                    "Speak about AI in research to other colleges across the university, and "
                    "meet with professors and labs about using it in their own work",
                    "Represented the association at BYU's AI for Social Innovation Conference, "
                    "on the Data Sovereignty and Inclusion working table",
                ],
            },
            {
                "what": "Pre-Med Peer Mentor, BYU Pre-Med Association",
                "dates": "October 2026 – Present",
                "bullets": ["Mentor pre-med students on coursework, research, and clinical "
                            "experience"],
            },
            {
                "what": "Lead Program Director, BYU Y-Serve, Early Learning Essentials",
                "dates": "August 2024 – Present",
                "bullets": [
                    "Program Director from August 2024; Lead Program Director since March 2025",
                    "Recruit volunteers, organize events, and manage communication for a program "
                    "serving preschoolers from low-income families",
                ],
            },
            {
                "what": "University Peer Mentor, BYU Office of First Year Experience",
                "dates": "June 2024 – February 2025",
                "bullets": [
                    "Co-taught two sections of Introduction to University (UNIV 101) with faculty",
                    "Mentored 45 first-year students through regular one-on-one meetings; "
                    "completed QPR gatekeeper training",
                ],
            },
            {
                "what": "Full-Time Missionary, California Riverside Mission",
                "dates": "October 2021 – December 2023",
                "note": "The Church of Jesus Christ of Latter-day Saints",
                "bullets": [
                    "Led and supported small groups of fellow volunteers",
                    "Planned and gave 80+ trainings on teaching skills to groups of 8 to 100 "
                    "volunteers; mentored four new volunteers one-on-one",
                    "Worked in the mission office coordinating housing and travel logistics and "
                    "managing technology",
                ],
            },
            {
                "what": "Squad Leader, Air Academy High School Marching Band, "
                        "Colorado Springs, CO",
                "dates": "May 2020 – May 2021",
                "bullets": ["Led the trumpet section; the band won two state championships and "
                            "marched in the 2018 Rose Parade"],
            },
        ],
    },
    {
        "heading": "Service",
        "entries": [
            {"text": "Volunteer, Global Early Detection Initiative, Utah Chapter "
                     "(community outreach)", "dates": "August 2026 – Present"},
            {"text": "Church Instructor, The Church of Jesus Christ of Latter-day Saints",
             "dates": "August 2026 – Present"},
            {"text": "Congregation Activities Committee and Leadership Council",
             "dates": "September 2025 – April 2026"},
            {"text": "Congregation Clerk (records) and Leadership Council",
             "dates": "May 2024 – August 2024"},
            {"text": "Boy Scouts of America; Eagle Scout project for the National Mill Dog "
                     "Rescue", "dates": "2014 – 2020"},
        ],
    },
    {
        "heading": "Certifications and Training",
        "entries": [
            {"text": "Thermo Fisher Scientific \"Resolution Evolution\" cryo-EM training "
                     "(Vitrobot, Krios)", "dates": "October 2026"},
            {"text": "Epic for Research Coordinators, UT Southwestern", "dates": "May 2026"},
            {"text": "SCCR Research Ethics Seminar, BYU", "dates": "April 2026"},
            {"text": "NHCO Certified Phlebotomy Technician (two-year certification, expired)",
             "dates": "June 2024 – June 2026"},
            {"text": "QPR Suicide Prevention Gatekeeper Training, BYU", "dates": "2024"},
        ],
    },
    {
        "heading": "Conferences Attended",
        "entries": [
            {"text": "AI for Social Innovation Conference, BYU Ballard Center, Aspen Grove, UT",
             "dates": "October 2026"},
            {"text": "Utah CryoEM Symposium, Brigham Young University", "dates": "October 2026"},
            {"text": "American Chemical Society Spring Meeting, Atlanta, GA",
             "dates": "March 2026"},
        ],
    },
    {
        "heading": "Skills",
        "entries": [
            {"text": "<b>Laboratory:</b> bacterial culture and plasmid work, SEM, "
                     "ultra-high-vacuum systems, XPS, mass spectrometry, spin coating, flow "
                     "reactor operation, Vitrobot, Krios cryo-TEM"},
            {"text": "<b>Computational:</b> Python, R, C#, Java, shell, Git and GitHub, ImageJ, "
                     "Epic, cryo-ET processing software, DICOM and medical imaging pipelines, "
                     "GPU workflows; AI coding agents since 2024, including agent skills and hooks"},
            {"text": "<b>Communication:</b> first author on three manuscripts and a co-author on "
                     "several more; six research presentations and an invited guest talk; "
                     "figure, poster, and interface design"},
        ],
    },
    {
        "heading": "Activities",
        "entries": [
            {"text": "BYU Fencing Club", "dates": "August 2026 – Present"},
            {"text": "Intramural Ultimate Frisbee, BYU", "dates": "May 2025 – December 2025"},
        ],
    },
]

CSS = """
@page { size: letter; margin: 0.6in 0.65in; }
* { box-sizing: border-box; }
body { margin:0; font: 9.7pt/1.38 Calibri, "Segoe UI", Arial, sans-serif; color:#1b1b1f; }
.cv-top { text-align:center; border-bottom:1.2pt solid #1f4f7a; padding-bottom:6pt;
          margin-bottom:9pt; }
.cv-top h1 { margin:0; font-size:21pt; letter-spacing:-0.3pt; color:#13334f; }
.cv-top .contact { margin-top:3pt; font-size:8.8pt; color:#3f4a55; }
h2 { font-size:10pt; text-transform:uppercase; letter-spacing:0.7pt; color:#1f4f7a;
     border-bottom:0.6pt solid #c9d4de; margin:11pt 0 4pt; padding-bottom:2pt;
     page-break-after:avoid; }
h3 { font-size:9.3pt; font-style:italic; color:#3f4a55; margin:7pt 0 2pt;
     page-break-after:avoid; }
.entry { margin-bottom:5pt; page-break-inside:avoid; }
.line1 { display:flex; justify-content:space-between; gap:10pt; align-items:baseline; }
.what { font-weight:700; }
.dates { color:#56606b; font-size:8.8pt; white-space:nowrap; }
.note { color:#3f4a55; font-style:italic; font-size:9.2pt; }
.quiet { color:#56606b; font-size:8.8pt; font-style:italic; }
ul { margin:2pt 0 0; padding-left:12pt; }
li { margin:1pt 0; }
.cite { padding-left:14pt; text-indent:-14pt; margin-bottom:3pt; }
"""


def entry_html(e):
    if e.get("subhead"):
        return "<h3>%s</h3>" % e["subhead"]
    if e.get("text") and not e.get("what"):
        cls = "entry cite" + (" quiet" if e.get("quiet") else "")
        if e.get("dates"):
            return ('<div class="%s"><div class="line1"><span>%s</span>'
                    '<span class="dates">%s</span></div></div>'
                    % (cls, e["text"], e["dates"]))
        return '<div class="%s">%s</div>' % (cls, e["text"])
    bits = ['<div class="entry"><div class="line1"><span class="what">%s</span>'
            '<span class="dates">%s</span></div>' % (e["what"], e.get("dates", ""))]
    if e.get("note"):
        bits.append('<div class="note">%s</div>' % e["note"])
    if e.get("bullets"):
        bits.append("<ul>%s</ul>" % "".join("<li>%s</li>" % b for b in e["bullets"]))
    bits.append("</div>")
    return "".join(bits)


def cv_body():
    """The CV itself, without a page wrapper. build.py renders this on the site."""
    out = ['<div class="cv-top"><h1>%s</h1><p class="contact">%s</p></div>'
           % (html.escape(NAME), " &nbsp;·&nbsp; ".join(CONTACT))]
    for sec in SECTIONS:
        out.append("<section><h2>%s</h2>%s</section>"
                   % (sec["heading"], "".join(entry_html(e) for e in sec["entries"])))
    return "\n".join(out)


def build_html():
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Russell Mercer CV</title><style>%s</style></head><body>
%s
</body></html>""" % (CSS, cv_body())


def main():
    os.makedirs(OUT, exist_ok=True)
    htm = os.path.join(OUT, "russell-mercer-cv.html")
    pdf = os.path.join(OUT, "russell-mercer-cv.pdf")
    with open(htm, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build_html())
    if os.path.exists(EDGE):
        make_resumes.print_pdf(htm, pdf)
        print("wrote %s" % os.path.basename(pdf))
    else:
        print("Edge not found at %s; wrote HTML only." % EDGE)


if __name__ == "__main__":
    sys.exit(main())
