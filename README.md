# mercer-science.github.io

Russell Mercer's portfolio site for the Crocker Innovation Fellowship. Four role pages
(`/igem`, `/coding`, `/design`, `/wildcard`), each with a role switcher and its own tabs.
Plain HTML and CSS served from `main`. GitHub Pages runs no build.

## Running the Build on Windows

Open PowerShell in this folder and run:

```
python tools\build.py
```

That reads every markdown file in `content/` plus the tab tables in `content\tabs.yml`,
writes the four role pages and `index.html`, and prints a list of whatever still needs
your sign-off. Nothing else in the repo is touched, so re-running it is always safe.

To rebuild the four resume PDFs:

```
python tools\make_resumes.py
```

It prints each one through headless Edge into `assets\pdf\`. The intermediate HTML stays
beside the PDFs so you can open it in a browser and check the layout before printing.

Python needs `pyyaml`, which is already installed.

## Editing the Copy

One markdown file in `content/` holds one block of content, and the same block is reused
across roles and tabs rather than written twice. Edit the file, rerun `build.py`, and
refresh the page.

Frontmatter fields:

| Field | What it does |
|---|---|
| `title` | The block heading on the page |
| `roles` | Which of igem, coding, design, wildcard use it |
| `tabs` | Which tabs it appears on |
| `status` | Published, Submitted, Ongoing, and so on. Anything starting with "Ongoing" is highlighted |
| `dates` | Shown beside the status |
| `images` | A list of `src`, `alt`, and `caption`. Alt text is required |
| `hold` | Set `true` and the block is never published; the build lists it instead |
| `placeholder` | Set `true` to render a reserved, empty section |
| `needs` | A note about what is still missing, printed by the build |

The body is plain markdown: `###` headings for Problem, Solution, Result (or Question,
Approach, Status for work not yet at the bench), paragraphs, `-` lists, `**bold**`,
`*italic*`, and `[links](url)`. Keep raw HTML out of it, so these files can move to a
different site generator later without a rewrite.

## Where the Pages Come From

`content\tabs.yml` is the table of contents: it lists each role's tabs left to right and
each tab's blocks top to bottom. Resume stays first, CV stays last. To move a block,
move its name in that file.

## House Rules

- Title Case on tab labels, headings, buttons, and figure titles. Body text and captions
  stay in sentence case
- American English, Oxford comma
- Problem / Solution / Result for finished projects; Question / Approach / Status for work
  that has not reached the bench
- Every Jensen Lab project carries an Ongoing flag
- All text is real, selectable text. Nothing important lives only inside an image
