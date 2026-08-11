# Studio Jam — Website

Single-page site for Studio Jam (formerly Claude & Co.), styled after the flat retro
color-block look of stellarmadecreative.com but built entirely on the Studio Jam brand:
teal 0B4F61, blush FFD7D9, berry 77565A, the Studio Jam Display font, the
hand-drawn star, and the squiggle pattern.

## Where to edit content

Everything editable lives in index.html — plain text between tags:

- Hero tagline — the hero-tag paragraph
- About copy & pillars — the about section
- Services list — the services section (8 cards)
- Package tiers & pricing — the packages section (Starter $400 / Growth $550 /
  Full $750, from the Kingdom Thread Co. proposal — adjust if the public rate card
  should differ)
- Process steps — the process section
- Contact email / Instagram — the contact section

Colors and fonts live in assets/style.css (the :root block at the top).
The font and all brand images are embedded directly in the files as base64 data
URIs, so the site is fully self-contained — two files, no asset folders.
