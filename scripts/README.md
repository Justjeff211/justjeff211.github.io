# Build scripts

These generated roadmap.html, certifications.html, calendar.html, journey.html,
writeups.html and skills.html. They're optional: every page is plain, complete
HTML you can edit directly, nothing on GitHub Pages depends on these scripts
running.

Use them only if you want to regenerate a page from scratch (e.g. after
editing the data near the top of a gen_*.py file). Run from the repo root:

    python3 scripts/gen_roadmap.py

build_pages.py holds the shared nav/footer template every page wraps around;
each gen_*.py holds that one page's content and data.

For small edits (fixing a date, tweaking a sentence), it's simpler to just
edit the .html file directly and skip these entirely.
