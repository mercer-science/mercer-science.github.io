---
title: Heart and Blood Pressure App
roles: [design, coding, wildcard]
tabs: [other-ui-projects, software-projects]
status: Personal project
dates: 2026
images:
  - id: reading
    src: assets/img/heart-bp-reading.png
    alt: The BP Monitor reading screen, with large systolic, diastolic, and pulse tiles, a time stamp, and position and arm selectors, plus a POTS Check tab.
    caption: Logging a reading. Three numbers up front, then the context a reading needs to mean something.
  - id: trend
    src: assets/img/heart-bp-trend.png
    alt: A blood pressure trend chart plotting systolic and diastolic over three weeks, with dashed AHA cutoff lines and one reading's details called out below.
    caption: The trend, against the AHA cutoffs. One reading expands to its full detail on hover.
  - id: averages
    src: assets/img/heart-bp-averages.png
    alt: The BP Monitor averages screen, showing seated averages over 7 and 30 days and by context (wake-up, post-gym, bedtime) above a dated reading history.
    caption: Averages by window and by context, so a single high reading does not read as a trend.
---

A personal project I built to track my own blood pressure and heart rate. It logs a reading
in a few taps, records the context that changes the number (position, arm, time of day, and
an orthostatic POTS check), and keeps the history.

[figure: reading]

The design problem is the same one every health app has: a single number means little, so
the app shows each reading against the AHA cutoffs and rolls the history into averages by
window and by context, rather than leaving a wall of numbers to read.

[figure: trend, averages]
