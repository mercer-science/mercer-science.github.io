---
title: Extraction and Analysis Pipelines
roles: [coding]
tabs: [software-projects]
status: ""
dates: 2026
images: []
---

### Problem

Every one of the radiation oncology studies ran on data that a hospital generated for
treating patients, not for analysis. Structures are named differently by each physician,
sessions go missing, file names carry no information, and the same measurement means
different things on different machines. You cannot ask a clinical question until something
cleans that up, and doing it by hand means the answer changes every time you redo it.

### Solution

**C# inside the treatment planning system.** A script that walks every patient and plan,
finds the relevant structures despite inconsistent naming, pulls the dose data into
organized spreadsheets, and asks a human only when it genuinely cannot resolve a duplicate.

**Python for the parts with judgment in them.** Filtering raw exports into templates
designed with the physician; reconstructing respiratory motion from backup-plan contours
and running about 1,000 geometric checks per patient; recovering imaging dates for files
whose names had lost them; rebuilding per-patient outcome plots from a chart-review sheet.

**R for everything that becomes a figure or table.** Every panel and every table in those
manuscripts generates from the raw data. About 20 figures were drafted for one paper and
cut to a main set plus supplements, and six tables build themselves.

### Result

When I found the exporter bug that had been capping a key measurement, fixing it meant
rerunning the pipeline, and every figure in the paper rebuilt correctly. That is the
argument for writing the pipeline instead of the figure. The code itself belongs to UT
Southwestern and is tied to its systems, so it is not public.
