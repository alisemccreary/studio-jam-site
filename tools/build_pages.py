import re, os, sys
import pathlib
SITE = str(pathlib.Path(__file__).resolve().parent.parent)
os.chdir(SITE)
idx = open('index.html', encoding='utf-8').read()

def data(cls):
    return re.search(r'<img class="%s[^"]*" src="([^"]+)"' % cls, idx).group(1)
STAR = "/assets/img/star-teal.png"; STAR_PINK = "/assets/img/star-pink.png"; LOGO = "/assets/img/logo.png"; MASCOT = "/assets/img/mascot-walk-pink.png"
FAV = 'data:image/png;base64,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'
CSSV = "53"
EMAIL = "alise@studiojamcreatives.com"

JSONLD = '''{"@context":"https://schema.org","@type":"ProfessionalService","name":"Studio Jam","alternateName":"Studio Jam Creatives","url":"https://studiojamcreatives.com/","email":"alise@studiojamcreatives.com","founder":{"@type":"Person","name":"Alise McCreary"},"description":"A creative marketing studio offering brand identity, website and Shopify design, social media management, and marketing and ads.","sameAs":["https://instagram.com/studiojamcreatives"],"knowsAbout":["Brand identity","Website design","Shopify","Social media management","Paid advertising","Email marketing"]}'''
def head(title, desc, path, noindex=False):
    url = "https://studiojamcreatives.com/" + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{FAV}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Studio Jam">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://studiojamcreatives.com/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B4F61">
<link rel="apple-touch-icon" href="/assets/img/icon-180.png">
<link rel="preload" href="/assets/fonts/closeout.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inclusive-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css?v={CSSV}">
{'<script type="application/ld+json">' + JSONLD + '</script>' if path == '' else ''}
</head>
<body>
<div id="sj-root">
<a class="skip" href="#main">Skip to content</a>
'''

NAV = [("about", "About"), ("services", "Services"), ("packages", "Packages"), ("process", "Process"), ("clients", "Clients"), ("work-with-us", "Work with us")]
def nav(current):
    CUR = ' aria-current="page"'
    links = "".join('\n    <a href="/%s"%s>%s</a>' % (slug, CUR if slug == current else "", label) for slug, label in NAV)
    cta_cur = CUR if current == "contact" else ""
    return f'''<!-- NAV -->
<header class="nav">
  <a class="nav-logo" href="/" aria-label="Studio Jam home"><img src="/assets/img/logo-lockup.png" alt="Studio Jam" width="900" height="206"></a>
  <nav class="nav-links" aria-label="Primary">{links}
    <a class="nav-cta" href="/contact"{cta_cur}>Let&rsquo;s jam</a>
  </nav>
</header>
'''

def ticker(text):
    t = text + " &#10039;&nbsp;"
    return f'''<!-- TICKER -->
<div class="ticker">
  <div class="ticker-track" aria-hidden="true">
    <span>{t}</span>
    <span>{t}</span>
  </div>
  <button class="ticker-toggle" type="button" aria-pressed="false" aria-label="Pause the scrolling banner"><span aria-hidden="true">&#10074;&#10074;</span></button>
</div>
'''
TICK_MAIN = "Creative Marketing Studio &#10039; Brand &#10039; Web &#10039; Social &#10039; Ads &#10039; Let&rsquo;s Go Dancing! &#10039; Creative Marketing Studio &#10039; Brand &#10039; Web &#10039; Social &#10039; Ads &#10039; Let&rsquo;s Go Dancing!"

DECO_DIMS = {"mascot-stand-pink.png": (420, 384), "mascot-walk-pink.png": (520, 562), "mascot-tall-pink.png": (229, 600), "mascot-stand.png": (420, 384), "mascot-walk.png": (520, 562), "mascot-tall.png": (229, 600)}
def page_hero(kicker, h1, tag, ctas, cls="", photo=None, alt="Alise McCreary, founder of Studio Jam", deco=None):
    c = "".join(f'\n    <a class="btn {k}" href="{h}">{t}</a>' for t, h, k in ctas)
    body = f'''    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="hero-tag">{tag}</p>
    <div class="hero-ctas">{c}
    </div>'''
    if photo:
        from PIL import Image as _I
        pw, ph = _I.open(os.path.join(SITE, 'assets', 'img', photo)).size
        wide = ' wide' if pw > ph else ''
        return f'''<section class="page-hero with-photo {cls}" id="top"><span id="main"></span>
  <img class="hero-star star-a" src="{STAR_PINK}" alt="" width="602" height="667">
  <div class="hero-grid">
    <div class="hero-copy">
{body}
    </div>
    <div class="photo-frame tilt-r{wide}">
      <img src="/assets/img/{photo}" srcset="/assets/img/{photo[:-4]}-600.jpg 600w, /assets/img/{photo} {pw}w" sizes="(max-width: 900px) 92vw, 440px" alt="{alt}" width="{pw}" height="{ph}">
    </div>
  </div>
</section>
'''
    d = f'\n  <img loading="lazy" decoding="async" class="deco {deco[1]}" src="/assets/img/{deco[0]}" alt="" width="{DECO_DIMS.get(deco[0], (400, 400))[0]}" height="{DECO_DIMS.get(deco[0], (400, 400))[1]}">' if deco else ''
    return f'''<section class="page-hero {cls}" id="top"><span id="main"></span>
  <img class="hero-star star-a" src="{STAR_PINK}" alt="" width="602" height="667">{d}
{body}
</section>
'''

def cta_band(kicker, h2, p, btn_text, btn_href="/contact", cls="contact"):
    return f'''<section class="{cls} has-chat">
  <img class="contact-star" src="{STAR}" alt="" width="602" height="667">
  <img loading="lazy" decoding="async" class="deco chat" src="/assets/img/mascot-chat.png" alt="" width="466" height="891">
  <p class="kicker">{kicker}</p>
  <h2>{h2}</h2>
  <p>{p}</p>
  <a class="btn btn-teal" href="{btn_href}">{btn_text}</a>
</section>
'''

def finalize(html):
    """Post-process a built page: <main> landmark, external-link hints."""
    html = html.replace('<span id="main"></span>', '')
    if '<main id="main">' not in html:
        i = html.find('<!-- TICKER -->'); j = html.find('<section', i)
        html = html[:j] + '<main id="main">\n' + html[j:]
        html = html.replace('<!-- FOOTER -->', '</main>\n<!-- FOOTER -->', 1)
    def hint(m):
        tag, inner = m.group(1), m.group(2)
        if 'aria-label=' in tag or 'new tab' in inner: return m.group(0)
        return tag + inner + '<span class="sr-only"> (opens in a new tab)</span></a>'
    html = re.sub(r'(<a [^>]*target="_blank"[^>]*>)(.*?)</a>', hint, html, flags=re.S)
    return html

def footer():
    return f'''<!-- FOOTER -->
<footer class="footer textured">
  <p class="footer-big">Stay jammin&rsquo;, folks</p>
  <nav class="footer-links" aria-label="Footer">
    <a href="/about">About</a>
    <a href="/services">Services</a>
    <a href="/packages">Packages</a>
    <a href="/process">Process</a>
    <a href="/clients">Clients</a>
    <a href="/work-with-us">Work with us</a>
    <a href="/contact">Contact</a>
    <a href="https://instagram.com/studiojamcreatives" target="_blank" rel="noopener">Instagram</a>
    <a class="mail" href="mailto:alise@studiojamcreatives.com">alise@studiojamcreatives.com</a>
  </nav>
  <div class="footer-row">
    <p>&copy; 2026 Studio Jam</p>
    <a href="#top">Back to top &#8593;</a>
  </div>
</footer>

</div>
<script>
(function () {{
  var tk = document.querySelector('.ticker'), tb = document.querySelector('.ticker-toggle');
  if (tk && tb) tb.addEventListener('click', function () {{
    var paused = tk.classList.toggle('paused');
    tb.setAttribute('aria-pressed', String(paused));
    tb.setAttribute('aria-label', paused ? 'Resume the scrolling banner' : 'Pause the scrolling banner');
    tb.firstElementChild.innerHTML = paused ? '&#9654;' : '&#10074;&#10074;';
  }});
}})();
(function () {{
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;
  var groups = ['.clientmap .place', '.service-grid .service', '.tier-grid .tier', '.job-grid .job-card', '.pillars li', '.steps .step', '.pillar-grid .pillar', '.service-rows .service-row', '.step-grid .step-card', '.tips li', '.faq .faq-item'];
  var singles = ['.kicker', 'h2', '.about-copy', '.hiring-copy', '.job-copy', '.packages-intro', '.fine-print', '.contact > p', '.hero-ctas', '.btn.btn-teal', '.ig', '.based', '.footer-big', '.quote', '.quote-by', '.story p', '.lead', '.teaser-link', '.photo-frame', '.deco', '.mapbox'];
  var targets = [];
  groups.forEach(function (sel) {{
    var els = document.querySelectorAll(sel);
    for (var i = 0; i < els.length; i++) {{
      els[i].style.setProperty('--reveal-delay', (i * 0.09) + 's');
      targets.push(els[i]);
    }}
  }});
  singles.forEach(function (sel) {{
    var els = document.querySelectorAll(sel);
    for (var i = 0; i < els.length; i++) targets.push(els[i]);
  }});
  targets.forEach(function (el) {{
    if (!el.closest('.hero') && !el.closest('.page-hero')) el.classList.add('reveal');
  }});
  var io = new IntersectionObserver(function (entries) {{
    entries.forEach(function (e) {{
      if (e.isIntersecting) {{
        var el = e.target;
        el.classList.add('in');
        io.unobserve(el);
        setTimeout(function () {{
          el.classList.remove('reveal');
          el.classList.remove('in');
          el.style.removeProperty('--reveal-delay');
        }}, 1100);
      }}
    }});
  }}, {{ threshold: 0.12, rootMargin: '0px 0px -40px 0px' }});
  document.querySelectorAll('.reveal').forEach(function (el) {{ io.observe(el); }});
  setTimeout(function () {{
    document.querySelectorAll('.reveal').forEach(function (el) {{ el.classList.add('in'); }});
  }}, 2200);
}})();
</script>
</body>
</html>
'''

# ---------------- shared content ----------------
SERVICES = [
  ("01", "Brand Identity",
   "Your look and your voice, working together. Logo suites, color, type, and the full visual songbook, built to flex from Instagram to storefront.",
   ["Logo suite &amp; submarks", "Color &amp; type systems", "Brand guides &amp; templates"],
   "Good for: new businesses, rebrands, and brands whose look has drifted from who they are."),
  ("02", "Web &amp; Shopify",
   "A home venue for your brand. Sites and Shopify storefronts designed, written, and built to launch, and to keep selling after launch day.",
   ["Custom website design", "Shopify setup &amp; launch", "Copy written, not just placed", "No unnecessary app fees, ever"],
   "Good for: shops, restaurants, and service businesses that need a site people actually use."),
  ("03", "Social Media Management",
   "Your feed, on beat. Content that sounds like you and shows up consistently: planned, produced, and posted.",
   ["Content, captions &amp; creative", "On-site content days &amp; filming", "Scheduling &amp; posting", "You approve before anything posts"],
   "Good for: owners who know what they want to say and are tired of being the one who has to post it."),
  ("04", "Marketing &amp; Ads",
   "Get seen. Get customers. Get repeat buyers. Paid ads, email, and partnerships played together, so every dollar has a job.",
   ["Paid ads on Meta &amp; Google", "Email marketing", "Brand &amp; partnership outreach", "Strategy &amp; reporting"],
   "Good for: businesses with a working offer that need more of the right people to see it."),
]

TIERS = [
  ("The Opener", "Where the show starts", False,
   ["Your main channel managed start to finish: planned, produced, posted", "A brand that shows up consistently where it matters most", "A monthly check-in and a plain-language recap of what worked"]),
  ("The Main Event", "The headline set", True,
   ["More channels in rotation, including email", "Campaigns, launches, and promotions join the mix", "Strategy calls and reporting, so every move has a reason"]),
  ("The Encore", "Full production", False,
   ["Everything in The Main Event, plus paid ads", "A dedicated team assembled around your account", "Alise stays your single point of contact, always"]),
]

STEPS = [
  ("01 / Discovery", "We get to know your business, your audience, and what you actually need. No upselling, no pressure.",
   "You get: a clear read on where you are and what is worth fixing first."),
  ("02 / Strategy", "A clear plan with priorities in order: what to fix first, what to build next, and what to leave alone.",
   "You get: a written plan you can hold me to."),
  ("03 / Build", "Brand, website, content: designed, written, and set up properly, with you approving every piece before it goes out.",
   "You get: finished work, on the timeline we agreed to."),
  ("04 / Launch + beyond", "Everything goes live, and month by month we double down on what&rsquo;s working and trim what isn&rsquo;t.",
   "You get: a recap every month in plain language, and one person to call."),
]

QUOTE = ("It is so much more than &ldquo;social media.&rdquo; They take away the worry, the planning, and the <em>what do I post?</em> and help me focus on what matters most to me. They understand my voice, my passions, my community. They don&rsquo;t just create for me, they create with me.",
         "Kristy Bridgers", "Sober and Social, Oxford, MS", "Social media management, on-site shooting, paid advertisements, and brand partnerships")

QUOTE2 = ("Working with Alise was incredible! After two failed experiences with other companies that just couldn&rsquo;t see my vision, I felt so fortunate to give it one last try. Alise immediately understood exactly what I wanted based on my notes and inspiration photos, and honestly made me feel like I wasn&rsquo;t crazy! She was incredibly quick, courteous, and responsive throughout the entire process. I couldn&rsquo;t be happier with the final result!",
          "Dayne Kennedy", "The Living Room Nail Salon + Spa", "Brand refinement and logo suite")

def testimonial(kicker="From a client", alt=False):
    q, who, biz, ctx = QUOTE2 if alt else QUOTE
    return f'''<!-- TESTIMONIAL -->
<section class="testimonial textured">
  <img loading="lazy" decoding="async" class="mono-mark" src="/assets/img/monogram-pink.png" alt="" width="300" height="129">
  <p class="kicker">{kicker}</p>
  <blockquote class="quote">&ldquo;{q}&rdquo;</blockquote>
  <p class="quote-by"><strong>{who}</strong> &middot; {biz}<br><span>{ctx}</span></p>
</section>
'''

def tier_cards():
    out = []
    for name, tag, pop, items in TIERS:
        lis = "".join(f"\n        <li>{i}</li>" for i in items)
        badge = '\n      <p class="badge">Crowd favorite</p>' if pop else ''
        out.append(f'''    <div class="tier{' tier-popular' if pop else ''}">{badge}
      <h3>{name}</h3>
      <p class="tier-tag">{tag}</p>
      <ul>{lis}
      </ul>
    </div>''')
    return "\n".join(out)

def service_cards():
    out = []
    for n, name, p, items, good in SERVICES:
        lis = "".join(f"\n        <li>{i}</li>" for i in items[:3])
        out.append(f'''    <div class="service">
      <span>{n}</span>{name}
      <p>{p}</p>
      <ul>{lis}
      </ul>
    </div>''')
    return "\n".join(out)

# ---------------- HOME ----------------
home = head("Studio Jam | Creative Marketing Studio",
            "Brand, web, social, and ads from one creative marketing studio. The range of an in-house team, and one person who actually picks up.", "")
home += nav("") + ticker(TICK_MAIN) + f'''
<!-- HERO -->
<section class="hero" id="top"><span id="main"></span>
  <img class="hero-star star-a" src="{STAR_PINK}" alt="" width="602" height="667">
  <h1 class="sr-only">Studio Jam, a creative marketing studio</h1>
  <img class="hero-logo" src="{LOGO}" alt="Studio Jam" width="1400" height="641">
  <img class="hero-mascot" src="{MASCOT}" alt="" width="520" height="562">
  <p class="hero-tag">A creative marketing studio with the full range of an in-house team, and the warmth of one person who actually picks up.</p>
  <div class="hero-ctas">
    <a class="btn btn-blush btn-solid" href="/contact">Start a project</a>
    <a class="btn btn-blush" href="/services">See what we do</a>
  </div>
</section>

<!-- ABOUT TEASER -->
<section class="about split" id="about">
  <div class="split-grid">
    <div class="photo-frame tilt-l">
      <img loading="lazy" decoding="async" src="/assets/img/alise-kick.jpg" srcset="/assets/img/alise-kick-600.jpg 600w, /assets/img/alise-kick.jpg 1200w" sizes="(max-width: 900px) 92vw, 440px" alt="Alise McCreary, founder of Studio Jam, kicking back on a stool" width="1200" height="800">
    </div>
    <div class="split-copy">
      <p class="kicker">The Studio</p>
      <h2>One studio. One point of contact. Full creative range.</h2>
      <p class="about-copy">Hi, I&rsquo;m Alise. Studio Jam exists for the business that needs an entire marketing department and can realistically afford one person. Brand, web, social, and ads, run by a founder who is actually in the room rather than a name on a proposal.</p>
      <ul class="pillars">
        <li>Hospitality first</li>
        <li>Sound books</li>
        <li>Honest business</li>
        <li>Strategic design</li>
      </ul>
      <a class="teaser-link" href="/about">Meet the studio &#8594;</a>
    </div>
  </div>
</section>

<!-- SERVICES TEASER -->
<section class="services" id="services">
  <img loading="lazy" decoding="async" class="deco kick" src="/assets/img/mascot-kick-pink.png" alt="" width="520" height="362">
  <p class="kicker">The Work</p>
  <h2>What we do</h2>
  <div class="service-grid">
{service_cards()}
  </div>
  <a class="btn btn-blush teaser-btn" href="/services">All services, in detail</a>
</section>



<!-- SETLIST -->
<section class="setlist">
  <p class="kicker">On tour</p>
  <p class="setlist-line">Three stops so far, six venues on the bill, and a home base in Colorado.</p>
  <ul class="setlist-names">
    <li>Fayetteville, AR</li>
    <li>North Mississippi</li>
    <li>Charlotte, NC</li>
  </ul>
  <a class="teaser-link" href="/clients">Follow the tour &#8594;</a>
</section>

{testimonial()}
<!-- PACKAGES TEASER -->
<section class="packages" id="packages">
  <p class="kicker">Marketing Management</p>
  <h2>Pick your set</h2>
  <p class="packages-intro">Three tiers of monthly marketing management. No rate cards, no one-size-fits-all. Each one is scoped to your business and your goals, and the show builds from there.</p>
  <div class="tier-grid">
{tier_cards()}
  </div>
  <p class="fine-print">Not sure which set? Tell me about your business and we&rsquo;ll scope it together. Packages flex to fit, and you can change tiers anytime.</p>
  <a class="teaser-link" href="/packages">Compare the sets &#8594;</a>
</section>

<!-- PROCESS TEASER -->
<section class="process" id="process">
  <img loading="lazy" decoding="async" class="deco walk" src="/assets/img/mascot-walk-pink.png" alt="" width="520" height="562">
  <p class="kicker">From hello to launch</p>
  <h2>How a jam session goes</h2>
  <div class="steps">
''' + "".join(f'''    <div class="step">
      <p class="step-num">{n}</p>
      <p>{p}</p>
    </div>
''' for n, p, _ in STEPS) + f'''  </div>
  <a class="teaser-link light" href="/process">See the whole process &#8594;</a>
</section>

<!-- CONTACT -->
<section class="contact has-chat" id="contact">
  <img class="contact-star" src="{STAR}" alt="" width="602" height="667">
  <img loading="lazy" decoding="async" class="deco chat" src="/assets/img/mascot-chat.png" alt="" width="466" height="891">
  <h2>Let&rsquo;s jam</h2>
  <p>Tell me about your business, what&rsquo;s working, and what&rsquo;s not. The first conversation is on the house, and there&rsquo;s no pitch at the end of it.</p>
  <a class="btn btn-teal" href="mailto:{EMAIL}">{EMAIL}</a>
  <p class="ig"><a href="https://instagram.com/studiojamcreatives" target="_blank" rel="noopener">@studiojamcreatives</a> on Instagram</p>
</section>

''' + footer()
open('index.html', 'w', encoding='utf-8').write(finalize(home))

# ---------------- ABOUT ----------------
about = head("About Studio Jam | Creative Marketing Studio", "The story, the mission, and the four pillars behind Studio Jam, a creative marketing studio founded by Alise McCreary.", "about")
about += nav("about") + ticker("The Studio &#10039; Hospitality First &#10039; Sound Books &#10039; Honest Business &#10039; Strategic Design &#10039; The Studio &#10039; Hospitality First &#10039; Sound Books &#10039; Honest Business &#10039; Strategic Design")
about += page_hero("The Studio", "Your marketing department, minus the department",
                   "Studio Jam exists for the business that needs an entire marketing team and can realistically afford one person.",
                   [("Start a project", "/contact", "btn-blush btn-solid"), ("See the work", "/services", "btn-blush")],
                   photo="alise-seated.jpg", alt="Alise McCreary, founder of Studio Jam, seated in a denim jacket")
about += f'''
<section class="story">
  <div class="story-inner">
    <p class="kicker">The story behind the name</p>
    <h2>A concert is where you see your favorite people live. Studio Jam is where you bring your favorite brand to life.</h2>
    <p>Jam is what everyone has called founder Alise McCreary&rsquo;s little brother for as long as anyone can remember. If you are going to name a business after a person, it may as well be the cooler sibling.</p>
    <p>The second half arrived by way of Northeast Mississippi. Alise grew up minutes outside Tupelo, in a part of the state that takes its music seriously, and it took early. Records at home, concerts whenever there were concerts, and a lasting conviction that the best thing a room can do is come alive all at once.</p>
    <p>Which is what a jam is. Not a performance, but musicians in a room with an idea and no finished version of it yet, listening harder than they are playing. The good part happens because everyone came prepared and then paid attention to each other.</p>
  </div>
</section>

<section class="mission">
  <div class="mission-inner">
    <div class="mission-copy">
      <p class="kicker">The mission</p>
      <h2>The better answer to a familiar bind</h2>
      <p class="lead">Hire the generalist and hope they cover everything, or hire the specialist and handle the rest yourself. Studio Jam is built as the third option: brand identity, websites, social, strategy, and creative direction, run by a founder who is actually in the room rather than a name on a proposal.</p>
      <p class="lead">The whole operation runs on hospitality, and that is not a metaphor. Alise spent eight years in hospitality management before she managed brands. A dining room teaches a specific discipline: anticipate the need, over-communicate, and make sure nobody has to ask for something they should already have.</p>
      <p class="lead aside">Oh, and always play good music during dinner.</p>
    </div>
    <div class="photo-frame tilt-r small">
      <img loading="lazy" decoding="async" src="/assets/img/alise-lookup.jpg" srcset="/assets/img/alise-lookup-600.jpg 600w, /assets/img/alise-lookup.jpg 1100w" sizes="(max-width: 900px) 92vw, 440px" alt="Alise McCreary looking up, hands folded on a stool" width="1100" height="1375">
    </div>
  </div>
</section>

<section class="tour-band">
  <p class="kicker">On the map</p>
  <h2>See where the tour has played</h2>
  <p class="packages-intro">Our clients are pinned across the South, from Fayetteville to Charlotte, with a home base in Colorado. Every stop is a business we work with, and every pin opens the bill.</p>
  <a class="btn btn-teal" href="/clients">See the tour</a>
</section>

{testimonial("What it feels like")}
''' + cta_band("Let&rsquo;s jam", "Sound like your kind of studio?", "Tell me about your business. The first conversation is on the house.", "Get in touch") + footer()
open('about.html', 'w', encoding='utf-8').write(finalize(about))

# ---------------- SERVICES ----------------
svc = head("Brand, Web, Social &amp; Ads Services | Studio Jam", "Brand identity, websites and Shopify, social media management, and marketing and ads. What Studio Jam does and what is included in each.", "services")
svc += nav("services") + ticker("Brand Identity &#10039; Web &amp; Shopify &#10039; Social Media Management &#10039; Marketing &amp; Ads &#10039; Brand Identity &#10039; Web &amp; Shopify &#10039; Social Media Management &#10039; Marketing &amp; Ads")
svc += page_hero("The Work", "Four services. One point of contact.",
                 "Everything a marketing department does, without the handoffs. Pick one, or let them play together.",
                 [("Start a project", "/contact", "btn-blush btn-solid"), ("See the packages", "/packages", "btn-blush")])
SVC_EXTRA = {
  "01": ("alise-think", 'Recently for: The Living Room Nail Salon + Spa'),
  "02": ("alise-seated", ""),
  "03": ("alise-lookup", 'Recently for: <a href="https://www.windowjoeoxford.com/" target="_blank" rel="noopener">Window Joe</a>, <a href="https://www.innatcarnallhall.com/restaurants-fayetteville-ar/lambeth-lounge-coffee-bar" target="_blank" rel="noopener">Lambeth Lounge</a>, <a href="https://www.innatcarnallhall.com/restaurants-fayetteville-ar" target="_blank" rel="noopener">Ella&rsquo;s Table</a>, <a href="https://www.marellemahjong.com/" target="_blank" rel="noopener">Marelle Mahjong</a>'),
  "04": ("alise-glasses", 'Recently for: <a href="https://instagram.com/kbridgers1" target="_blank" rel="noopener">Sober and Social</a>, <a href="https://jmservices.biz/" target="_blank" rel="noopener">JM Services</a>'),
}
rows = []
for n, name, p, items, good in SERVICES:
    lis = "".join(f"\n        <li>{i}</li>" for i in items)
    img, recent = SVC_EXTRA[n]
    recent_html = f'\n        <p class="recent">{recent}</p>' if recent else ""
    rows.append(f'''    <div class="service-row" id="s{n}">
      <div class="service-row-thumb"><img src="/assets/img/{img}-600.jpg" alt="" width="600" height="750" loading="lazy" decoding="async"></div>
      <div class="service-row-head">
        <span class="num">{n}</span>
        <h2>{name}</h2>
        <p class="good">{good}</p>{recent_html}
      </div>
      <div class="service-row-body">
        <p>{p}</p>
        <ul>{lis}
        </ul>
      </div>
    </div>''')
svc += '''
<section class="service-rows">
''' + "\n".join(rows) + '''
</section>

<section class="mix split">
  <div class="split-grid">
    <div class="split-copy">
      <p class="kicker">Better together</p>
      <h2>The services are built to play as a set</h2>
      <p class="packages-intro">A brand without a website has nowhere to send people. A website without content goes quiet. Content without a plan is just posting. Most clients start with one service and add the next when it makes sense, and monthly management ties it all together.</p>
      <a class="btn btn-teal" href="/packages">See monthly management</a>
    </div>
    <div class="photo-frame tilt-r">
      <img loading="lazy" decoding="async" src="/assets/img/alise-cream.jpg" srcset="/assets/img/alise-cream-600.jpg 600w, /assets/img/alise-cream.jpg 1100w" sizes="(max-width: 900px) 92vw, 440px" alt="Alise McCreary seated on a block, smiling" width="1100" height="1375">
    </div>
  </div>
</section>

''' + cta_band("Not sure where to start?", "That&rsquo;s what the first call is for", "Tell me what you sell and what is not working. I&rsquo;ll tell you honestly which of these you actually need, and which you don&rsquo;t.", "Book the first conversation") + footer()
open('services.html', 'w', encoding='utf-8').write(finalize(svc))

# ---------------- PACKAGES ----------------
pk = head("Monthly Marketing Management Packages | Studio Jam", "Three tiers of monthly marketing management from Studio Jam: The Opener, The Main Event, and The Encore. Scoped to your business, no rate cards.", "packages")
pk += nav("packages") + ticker("Pick Your Set &#10039; The Opener &#10039; The Main Event &#10039; The Encore &#10039; Pick Your Set &#10039; The Opener &#10039; The Main Event &#10039; The Encore")
pk += page_hero("Marketing Management", "Pick your set",
                "Three tiers of monthly marketing management. No rate cards, no one-size-fits-all. Each one is scoped to your business and your goals.",
                [("Let&rsquo;s talk", "/contact", "btn-blush btn-solid"), ("How it works", "#how", "btn-blush")],
                photo="alise-think.jpg", alt="Alise McCreary thinking it over, finger on chin")
pk += f'''
<section class="packages page-tiers">
  <h2 class="sr-only">The three sets</h2>
  <div class="tier-grid">
{tier_cards()}
  </div>
  <p class="fine-print">Every set is scoped to you. Packages flex to fit, and you can change tiers anytime.</p>
</section>

<section class="process how" id="how">
  <p class="kicker">How scoping works</p>
  <h2>Why there is no price list</h2>
  <div class="step-grid">
    <div class="step-card">
      <p class="step-num">01</p>
      <h3>You tell me about the business</h3>
      <p>What you sell, who buys it, what you have tried, and what a good year looks like. One conversation, no forms to fill out first.</p>
    </div>
    <div class="step-card">
      <p class="step-num">02</p>
      <h3>I scope a set around it</h3>
      <p>Channels, cadence, and what is in and out, written down. You see exactly what you are getting before anything starts.</p>
    </div>
    <div class="step-card">
      <p class="step-num">03</p>
      <h3>We start, then adjust</h3>
      <p>Month by month we double down on what is working and trim what is not. Moving between sets is a conversation, not a renegotiation.</p>
    </div>
  </div>
  <p class="fine-print light">A price list would mean charging a corner shop and a twelve-location brand the same number for very different work. Scoping first keeps it honest, which is one of the four things this studio runs on.</p>
</section>

{testimonial("From a client", alt=True)}
''' + cta_band("Let&rsquo;s jam", "Ready to pick your set?", "Send a note with your business name and what you are hoping to change. I&rsquo;ll come back with the right set for you, and no pressure.", "Send a note") + footer()
open('packages.html', 'w', encoding='utf-8').write(finalize(pk))

# ---------------- PROCESS ----------------
pr = head("How a Project Works | Studio Jam", "How a project with Studio Jam goes, from the first conversation to launch and the months after.", "process")
pr += nav("process") + ticker("Discovery &#10039; Strategy &#10039; Build &#10039; Launch + Beyond &#10039; Discovery &#10039; Strategy &#10039; Build &#10039; Launch + Beyond")
pr += page_hero("From hello to launch", "How a jam session goes",
                "Four steps, in order, every time. You always know what is happening, what is next, and who to call.",
                [("Start at step one", "/contact", "btn-blush btn-solid"), ("See the services", "/services", "btn-blush")],
                photo="alise-stand.jpg", alt="Alise McCreary standing on a block in a denim jacket")
pr += '''
<section class="process page-steps">
  <div class="steps big">
''' + "".join(f'''    <div class="step">
      <p class="step-num">{n}</p>
      <p>{p}</p>
      <p class="step-get">{g}</p>
    </div>
''' for n, p, g in STEPS) + '''  </div>
</section>

<section class="expect">
  <p class="kicker">What to expect</p>
  <h2>Three promises, every project</h2>
  <div class="pillar-grid three">
    <div class="pillar">
      <h3>Hospitality-forward marketing</h3>
      <p>Eight years in dining rooms taught me to anticipate the need, over-communicate, and make sure nobody has to chase an update. Every account is run that way, and most of the time we simply take the whole thing off your plate.</p>
    </div>
    <div class="pillar">
      <h3>Results that grow your business</h3>
      <p>Pretty is not the goal. More customers, more repeat buyers, and a brand that pulls its weight are. Every move gets measured against that, and we double down on what works.</p>
    </div>
    <div class="pillar">
      <h3>A brand that tells your story</h3>
      <p>Your business already has a story. The work is building a brand that reflects it, so the people who find you feel like they already know you.</p>
    </div>
  </div>
</section>

''' + cta_band("Let&rsquo;s jam", "Step one is a conversation", "Tell me about your business, what&rsquo;s working, and what&rsquo;s not. The first conversation is on the house.", "Start the conversation") + footer()
open('process.html', 'w', encoding='utf-8').write(finalize(pr))

# ---------------- CONTACT ----------------
ct = head("Contact Studio Jam | Let&rsquo;s Jam", "Get in touch with Studio Jam, a creative marketing studio. The first conversation is on the house.", "contact")
ct += nav("contact") + ticker("Let&rsquo;s Jam &#10039; Say Hello &#10039; Working With Clients Everywhere &#10039; Let&rsquo;s Jam &#10039; Say Hello &#10039; Working With Clients Everywhere")
ct += f'''<section class="page-hero with-photo contact-hero" id="top"><span id="main"></span>
  <img class="hero-star star-a" src="{STAR_PINK}" alt="" width="602" height="667">
  <div class="hero-grid">
    <div class="hero-copy">
      <p class="kicker">Say hello</p>
      <h1>Let&rsquo;s jam</h1>
      <p class="hero-tag">Tell me about your business, what&rsquo;s working, and what&rsquo;s not. The first conversation is on the house, and there&rsquo;s no pitch at the end of it.</p>
      <div class="hero-ctas">
        <a class="btn btn-blush btn-solid" href="mailto:{EMAIL}?subject=Let%27s%20jam">{EMAIL}</a>
        <a class="btn btn-blush" href="https://instagram.com/studiojamcreatives" target="_blank" rel="noopener">@studiojamcreatives</a>
      </div>
    </div>
    <div class="photo-frame tilt-r">
      <img src="/assets/img/alise-glasses.jpg" srcset="/assets/img/alise-glasses-600.jpg 600w, /assets/img/alise-glasses.jpg 1100w" sizes="(max-width: 900px) 92vw, 440px" alt="Alise McCreary in glasses, smiling" width="1100" height="1375">
    </div>
  </div>
</section>

<section class="contact-details">
  <div class="contact-grid">
    <div class="contact-card">
      <p class="kicker">What to put in the email</p>
      <ul class="tips">
        <li>Your business name and what you sell</li>
        <li>What you want to change: more customers, a better look, a website that works, someone to run social</li>
        <li>Anything you have tried before, and how it went</li>
        <li>A rough timeline, if you have one</li>
      </ul>
      <p class="tip-note">Two or three sentences is plenty. I&rsquo;ll reply with a few questions and a time to talk.</p>
    </div>
    <div class="contact-card teal">
      <p class="kicker">Good to know</p>
      <ul class="tips">
        <li>Working with clients everywhere. Most projects start with a short discovery call, on Zoom or in person</li>
        <li>You will always talk to Alise, not an account manager</li>
        <li>Looking for the job instead? <a href="/work-with-us">Work with us</a> has the details</li>
      </ul>
    </div>
  </div>
</section>

{testimonial("What clients say", alt=True)}
''' + footer()
open('contact.html', 'w', encoding='utf-8').write(finalize(ct))

# ---------------- CLIENTS ----------------
cl = head("The Studio Jam Tour | Studio Jam", "Every stop on the Studio Jam tour is a business we work with: Fayetteville, North Mississippi, Charlotte, and a Colorado home base. See who was on the bill at each stop.", "clients")
cl += nav("clients") + ticker("Now Touring &#10039; Fayetteville, AR &#10039; North Mississippi &#10039; Charlotte, NC &#10039; Home Base: Colorado &#10039; Now Touring &#10039; Fayetteville, AR &#10039; North Mississippi &#10039; Charlotte, NC &#10039; Home Base: Colorado")
cl += page_hero("Now touring", "The Studio Jam Tour",
                "Every stop is a business we work with. Here is where the tour has played so far, and who was on the bill.",
                [("Book your city", "/contact", "btn-blush btn-solid"), ("See the setlist", "/services", "btn-blush")], deco=("mascot-walk-pink.png", "walk"))
cl += open(os.path.join(SITE, "tools", "map_fragment.html"), encoding="utf-8").read()
cl += testimonial("Kristy, on working together") + testimonial("Dayne, on the brand refresh", alt=True).replace('class="testimonial textured"', 'class="testimonial textured alt"')
cl += cta_band("Next leg", "Want your city on the tour?", "Tell me about your business, what&rsquo;s working, and what&rsquo;s not. The first conversation is on the house.", "Add your stop") + footer()
open('clients.html', 'w', encoding='utf-8').write(finalize(cl))

# ---------------- WORK WITH US (rebuild with shared shell) ----------------
ww = head("Marketing Assistant Job, Fayetteville AR | Studio Jam", "Studio Jam is hiring a part-time marketing assistant / paid intern in Fayetteville, Arkansas. Email your resume and recent work to apply.", "work-with-us")
ww += nav("work-with-us") + ticker("Now Hiring &#10039; Fayetteville, Arkansas &#10039; Part-Time Marketing Assistant &#10039; Paid Internship &#10039; Let&rsquo;s Jam! &#10039; Now Hiring &#10039; Fayetteville, Arkansas &#10039; Part-Time Marketing Assistant &#10039; Paid Internship &#10039; Let&rsquo;s Jam!")
ww += page_hero("Work with us", "We&rsquo;re hiring in Fayetteville",
                "Studio Jam is looking for a part-time marketing assistant / paid intern in Fayetteville, Arkansas.",
                [("Send your resume", "#apply", "btn-blush btn-solid"), ("About the studio", "/about", "btn-blush")],
                photo="alise-stool.jpg", alt="Alise McCreary on a stool with her feet up, laughing")
ww += f'''
<!-- THE ROLE -->
<section class="job" id="role">
  <div class="job-inner">
    <p class="kicker">The role</p>
    <h2>Part-time marketing assistant</h2>
    <p class="job-copy">This is perfect for any student or young professional looking to add real digital media and marketing experience to their resume. (University of Arkansas students, we&rsquo;re looking at you.)</p>
    <ul class="pillars job-pills">
      <li>Part-time</li>
      <li>Paid</li>
      <li>Fayetteville, AR</li>
      <li>Students &amp; young pros welcome</li>
    </ul>

    <div class="job-grid">
      <div class="job-card">
        <h3>What you&rsquo;ll do</h3>
        <ul>
          <li>Scheduling photoshoots</li>
          <li>General administrative work</li>
          <li>Connecting with current clients on their marketing goals</li>
          <li>Onsite photo and video shoots (1 to 2 times per month)</li>
        </ul>
      </div>
      <div class="job-card job-card-teal">
        <h3>Who it&rsquo;s for</h3>
        <ul>
          <li>You want to learn how a creative marketing studio actually runs</li>
          <li>You&rsquo;re organized, curious, and comfortable talking with clients</li>
          <li>You do not have to be proficient, just willing to learn</li>
          <li>This could grow into a full-time position if you want it to</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- APPLY -->
<section class="contact apply" id="apply">
  <img class="contact-star" src="{STAR}" alt="" width="602" height="667">
  <p class="kicker">How to apply</p>
  <h2>Let&rsquo;s jam</h2>
  <p>Email your resume plus any recent work (class projects, content you&rsquo;ve made, anything you&rsquo;re proud of) to:</p>
  <a class="btn btn-teal" href="mailto:{EMAIL}?subject=Marketing%20Assistant%20%2D%20Fayetteville">{EMAIL}</a>
  <p class="ig">Know someone who&rsquo;d be perfect? Send them this page.</p>
</section>

''' + footer()
open('work-with-us.html', 'w', encoding='utf-8').write(finalize(ww))

# ---------------- 404 ----------------
nf = head("Wrong Venue | Studio Jam", "That page is not on the setlist. Head back to Studio Jam.", "404", noindex=True)
nf += nav("") + page_hero("404", "Wrong venue", "That page isn&rsquo;t on the setlist. The show is still on, though.",
                          [("Back to the main stage", "/", "btn-blush btn-solid"), ("Say hello", "/contact", "btn-blush")], cls="notfound", deco=("mascot-stand.png", "stand"))
nf += footer()
open('404.html', 'w', encoding='utf-8').write(finalize(nf))
print("pages built:", [f for f in os.listdir('.') if f.endswith('.html')])
