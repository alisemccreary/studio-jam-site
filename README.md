# Studio Jam — Website

Single-page site for Studio Jam (formerly Claude & Co.), styled after the flat retro
color-block look of stellarmadecreative.com but built entirely on the Studio Jam brand:
teal 0B4F61, blush FFD7D9, berry 77565A, the Studio Jam Display font, the
hand-drawn star, and the squiggle pattern.

## Pages

index.html (home), about.html, services.html, packages.html, process.html,
contact.html, work-with-us.html (hiring), 404.html. Hosted on Vercel with clean
URLs (vercel.json), so about.html is served at /about. Every page is plain HTML and
can be edited directly.

tools/build_pages.py regenerates all pages from one script (shared nav, footer,
services, tiers, steps, testimonial). Use it when a change touches every page, e.g.
a new nav link. Run: python3 tools/build_pages.py. Editing a single page by hand is
fine too; just do not run the script afterwards without porting the edit into it.

## Where to edit content

- Hero tagline: index.html, the hero-tag paragraph
- Services, tiers, process steps, testimonial: tools/build_pages.py (SERVICES, TIERS,
  STEPS, QUOTE) or the matching page
- Job description: work-with-us.html
- Contact email and Instagram: EMAIL in tools/build_pages.py

Colors and fonts live in assets/style.css. Palette is the Studio Jam Brand Guide:
teal #0B4F61, pink #F8CBCC (the only pink), berry #753F4B, red #B93D46,
sage #849D9B, off-white #ECEEEF. Fonts: Closeout (headings) and Inclusive Sans
(body), both embedded as base64 in the stylesheet.
