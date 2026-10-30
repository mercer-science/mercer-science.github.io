---
title: Building With AI, One Decision at a Time
roles: [design]
tabs: [ai]
status: ""
dates: 2026
images: []
---

Nearly everything on the Design tabs was built with an AI coding agent doing the typing. I
want to be precise about what that did and did not mean, because the distinction is the
whole point.

The clinical imaging application took weeks instead of months because the agent handled the
parts that are mechanical: wiring a viewer, scheduling GPU work, converting a slide to an
image and assembling it with plot panels. Every decision about what the user needed, which
comparison a physicist actually makes, and where a number should not be trusted came from
me, sitting in meetings with the people who would use it. The agent never met them.

The limit showed up clearly. Our research was new enough that there were few existing
patterns to draw on, and that is exactly where this kind of tool is weakest, since it works
from what has been done before. Where the work was ordinary, it flew. Where the work was
novel, I was back to thinking.

In the Jensen Lab I am now testing that boundary on purpose, logging every agent
recommendation in a processing pipeline as accepted, overridden, or an error I caught.
