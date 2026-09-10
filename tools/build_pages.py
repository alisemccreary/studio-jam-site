import re, os, sys
import pathlib
SITE = str(pathlib.Path(__file__).resolve().parent.parent)
os.chdir(SITE)
idx = open('index.html', encoding='utf-8').read()

def data(cls):
    return re.search(r'<img class="%s[^"]*" src="([^"]+)"' % cls, idx).group(1)
STAR = data('contact-star'); LOGO = data('hero-logo'); MASCOT = data('hero-mascot')
FAV = re.search(r'<link rel="icon" type="image/png" href="([^"]+)"', idx).group(1)
CSSV = "17"
EMAIL = "alise@studiojamcreatives.com"

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
<link rel="stylesheet" href="/assets/style.css?v={CSSV}">
</head>
<body>
<div id="sj-root">
'''

NAV = [("about", "About"), ("services", "Services"), ("packages", "Packages"), ("process", "Process"), ("work-with-us", "Work with us")]
def nav(current):
    CUR = ' aria-current="page"'
    links = "".join('\n    <a href="/%s"%s>%s</a>' % (slug, CUR if slug == current else "", label) for slug, label in NAV)
    cta_cur = CUR if current == "contact" else ""
    return f'''<!-- NAV -->
<header class="nav">
  <a class="nav-logo" href="/">Studio <span class="jam">Jam</span></a>
  <nav class="nav-links">{links}
    <a class="nav-cta" href="/contact"{cta_cur}>Let&rsquo;s jam</a>
  </nav>
</header>
'''

def ticker(text):
    t = text + " &#10039;&nbsp;"
    return f'''<!-- TICKER -->
<div class="ticker" aria-hidden="true">
  <div class="ticker-track">
    <span>{t}</span>
    <span>{t}</span>
  </div>
</div>
'''
TICK_MAIN = "Creative Marketing Studio &#10039; Brand &#10039; Web &#10039; Social &#10039; Ads &#10039; Let&rsquo;s Go Dancing! &#10039; Creative Marketing Studio &#10039; Brand &#10039; Web &#10039; Social &#10039; Ads &#10039; Let&rsquo;s Go Dancing!"

def page_hero(kicker, h1, tag, ctas, cls="", photo=None, alt="Alise McCreary, founder of Studio Jam", deco=None):
    c = "".join(f'\n    <a class="btn {k}" href="{h}">{t}</a>' for t, h, k in ctas)
    body = f'''    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="hero-tag">{tag}</p>
    <div class="hero-ctas">{c}
    </div>'''
    if photo:
        return f'''<section class="page-hero with-photo {cls}" id="top">
  <img class="hero-star star-a" src="{STAR}" alt="">
  <div class="hero-grid">
    <div class="hero-copy">
{body}
    </div>
    <div class="photo-frame tilt-r">
      <img src="/assets/img/{photo}" alt="{alt}" width="1100" height="1375">
    </div>
  </div>
</section>
'''
    d = f'\n  <img class="deco {deco[1]}" src="/assets/img/{deco[0]}" alt="">' if deco else ''
    return f'''<section class="page-hero {cls}" id="top">
  <img class="hero-star star-a" src="{STAR}" alt="">{d}
{body}
</section>
'''

def cta_band(kicker, h2, p, btn_text, btn_href="/contact", cls="contact"):
    return f'''<section class="{cls} has-chat">
  <img class="contact-star" src="{STAR}" alt="">
  <img class="deco chat" src="/assets/img/mascot-chat.png" alt="" width="466" height="891">
  <p class="kicker">{kicker}</p>
  <h2>{h2}</h2>
  <p>{p}</p>
  <a class="btn btn-teal" href="{btn_href}">{btn_text}</a>
</section>
'''

def footer():
    return f'''<!-- FOOTER -->
<footer class="footer textured">
  <p class="footer-big">Stay jammin&rsquo;, folks</p>
  <nav class="footer-links">
    <a href="/about">About</a>
    <a href="/services">Services</a>
    <a href="/packages">Packages</a>
    <a href="/process">Process</a>
    <a href="/work-with-us">Work with us</a>
    <a href="/contact">Contact</a>
    <a href="https://instagram.com/studiojamcreatives" target="_blank" rel="noopener">Instagram</a>
  </nav>
  <div class="footer-row">
    <p>&copy; 2026 Studio Jam &middot; Fayetteville, Arkansas</p>
    <a href="#top">Back to top &#8593;</a>
  </div>
</footer>

</div>
<script>
(function () {{
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;
  var groups = ['.service-grid .service', '.tier-grid .tier', '.job-grid .job-card', '.pillars li', '.steps .step', '.pillar-grid .pillar', '.service-rows .service-row', '.step-grid .step-card', '.tips li', '.faq .faq-item'];
  var singles = ['.kicker', 'h2', '.about-copy', '.hiring-copy', '.job-copy', '.packages-intro', '.fine-print', '.contact > p', '.hero-ctas', '.btn.btn-teal', '.ig', '.based', '.footer-big', '.quote', '.quote-by', '.story p', '.lead', '.teaser-link', '.photo-frame', '.deco'];
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
  ("01 / Discovery", "We get to know your business, your audience, and what you actually need. No upselling, no jargon.",
   "You get: a clear read on where you are and what is worth fixing first."),
  ("02 / Strategy", "A clear plan with priorities in order: what to fix first, what to build next, and what to leave alone.",
   "You get: a written plan you can hold me to."),
  ("03 / Build", "Brand, website, content: designed, written, and set up properly, with you approving every piece before it goes out.",
   "You get: finished work, on the timeline we agreed to."),
  ("04 / Launch + beyond", "Everything goes live, and month by month we double down on what&rsquo;s working and trim what isn&rsquo;t.",
   "You get: a recap every month in plain language, and one person to call."),
]

QUOTE = ("It is so much more than &ldquo;social media.&rdquo; They take away the worry, the planning, and the <em>what do I post?</em> and help me focus on what matters most to me. They understand my voice, my passions, my community. They don&rsquo;t just create for me, they create with me.",
         "Kristy Bridgers", "Sober and Social, Oxford, MS", "Social media management, content days, brand design, and partnership outreach since April 2026")

def testimonial(kicker="From a client"):
    q, who, biz, ctx = QUOTE
    return f'''<!-- TESTIMONIAL -->
<section class="testimonial textured">
  <img class="mono-mark" src="/assets/img/monogram-pink.png" alt="" width="300" height="129">
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
            "Brand design, websites, social media, and ads from one creative marketing studio in Fayetteville, Arkansas. The range of an in-house team, and one person who actually picks up.", "")
home += nav("") + ticker(TICK_MAIN) + f'''
<!-- HERO -->
<section class="hero" id="top">
  <img class="hero-star star-a" src="{STAR}" alt="">
  <h1 class="sr-only">Studio Jam, a creative marketing studio</h1>
  <img class="hero-logo" src="{LOGO}" alt="Studio Jam">
  <img class="hero-mascot" src="{MASCOT}" alt="">
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
      <img src="/assets/img/alise-kick.jpg" alt="Alise McCreary, founder of Studio Jam, kicking back on a stool" width="1200" height="800">
    </div>
    <div class="split-copy">
      <p class="kicker">The Studio</p>
      <h2>One studio. One point of&nbsp;contact. Full creative&nbsp;range.</h2>
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
  <img class="deco kick" src="/assets/img/mascot-kick.png" alt="" width="520" height="362">
  <p class="kicker">The Work</p>
  <h2>What we do</h2>
  <div class="service-grid">
{service_cards()}
  </div>
  <a class="btn btn-blush teaser-btn" href="/services">All services, in detail</a>
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
  <img class="deco walk" src="/assets/img/mascot-walk.png" alt="" width="520" height="562">
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
  <img class="contact-star" src="{STAR}" alt="">
  <img class="deco chat" src="/assets/img/mascot-chat.png" alt="" width="466" height="891">
  <h2>Let&rsquo;s jam</h2>
  <p>Tell me about your business, what&rsquo;s working, and what&rsquo;s not. The first conversation is on the house, and there&rsquo;s no pitch at the end of it.</p>
  <a class="btn btn-teal" href="mailto:{EMAIL}">{EMAIL}</a>
  <p class="ig"><a href="https://instagram.com/studiojamcreatives" target="_blank" rel="noopener">@studiojamcreatives</a> on Instagram</p>
  <p class="based">Based in Fayetteville, Arkansas. Working with clients everywhere.</p>
</section>

''' + footer()
open('index.html', 'w', encoding='utf-8').write(home)

# ---------------- ABOUT ----------------
about = head("About | Studio Jam", "The story, the mission, and the four pillars behind Studio Jam, a creative marketing studio founded by Alise McCreary.", "about")
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
      <img src="/assets/img/alise-lookup.jpg" alt="Alise McCreary looking up, hands folded on a stool" width="1100" height="1375">
    </div>
  </div>
</section>

<section class="pillars-section">
  <p class="kicker">Studio pillars</p>
  <h2>What the studio runs on</h2>
  <div class="pillar-grid">
    <div class="pillar">
      <h3>Hospitality first</h3>
      <p>Eight years of hospitality management leaves a person certain that the work is only half of it. The other half is how someone feels while it is being done, and that is the half most studios quietly decline to manage. Nobody should have to chase this one for an update.</p>
    </div>
    <div class="pillar">
      <h3>Sound books</h3>
      <p>A studio that cannot keep its own finances in order has no standing to advise anyone else on theirs. Honest pricing, invoices that arrive when they were promised, and enough margin to turn down work that is wrong for both sides.</p>
    </div>
    <div class="pillar">
      <h3>Honest business</h3>
      <p>Clients hear what the studio actually believes, including when that is not what they hoped to hear. No manufactured urgency, no scope padded to look impressive, no hidden timelines.</p>
    </div>
    <div class="pillar">
      <h3>Strategic design</h3>
      <p>Beautiful is the easy part, and it is the part that fails quietly when nothing underneath it is true. Every project starts with the business, the audience, and the competition, well before anyone opens a design file.</p>
    </div>
  </div>
</section>

{testimonial("What it feels like")}
''' + cta_band("Let&rsquo;s jam", "Sound like your kind of studio?", "Tell me about your business. The first conversation is on the house.", "Get in touch") + footer()
open('about.html', 'w', encoding='utf-8').write(about)

# ---------------- SERVICES ----------------
svc = head("Services | Studio Jam", "Brand identity, websites and Shopify, social media management, and marketing and ads. What Studio Jam does and what is included in each.", "services")
svc += nav("services") + ticker("Brand Identity &#10039; Web &amp; Shopify &#10039; Social Media Management &#10039; Marketing &amp; Ads &#10039; Brand Identity &#10039; Web &amp; Shopify &#10039; Social Media Management &#10039; Marketing &amp; Ads")
svc += page_hero("The Work", "Four services. One point of contact.",
                 "Everything a marketing department does, without the handoffs. Pick one, or let them play together.",
                 [("Start a project", "/contact", "btn-blush btn-solid"), ("See the packages", "/packages", "btn-blush")],
                 deco=("mascot-tall.png", "tall"))
rows = []
for n, name, p, items, good in SERVICES:
    lis = "".join(f"\n        <li>{i}</li>" for i in items)
    rows.append(f'''    <div class="service-row" id="s{n}">
      <div class="service-row-head">
        <span class="num">{n}</span>
        <h2>{name}</h2>
        <p class="good">{good}</p>
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
      <img src="/assets/img/alise-cream.jpg" alt="Alise McCreary seated on a block, smiling" width="1100" height="1375">
    </div>
  </div>
</section>

''' + cta_band("Not sure where to start?", "That&rsquo;s what the first call is for", "Tell me what you sell and what is not working. I&rsquo;ll tell you honestly which of these you actually need, and which you don&rsquo;t.", "Book the first conversation") + footer()
open('services.html', 'w', encoding='utf-8').write(svc)

# ---------------- PACKAGES ----------------
pk = head("Packages | Studio Jam", "Three tiers of monthly marketing management from Studio Jam: The Opener, The Main Event, and The Encore. Scoped to your business, no rate cards.", "packages")
pk += nav("packages") + ticker("Pick Your Set &#10039; The Opener &#10039; The Main Event &#10039; The Encore &#10039; Pick Your Set &#10039; The Opener &#10039; The Main Event &#10039; The Encore")
pk += page_hero("Marketing Management", "Pick your set",
                "Three tiers of monthly marketing management. No rate cards, no one-size-fits-all. Each one is scoped to your business and your goals.",
                [("Get scoped", "/contact", "btn-blush btn-solid"), ("How it works", "#how", "btn-blush")],
                photo="alise-think.jpg", alt="Alise McCreary thinking it over, finger on chin")
pk += f'''
<section class="packages page-tiers">
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
  <p class="fine-print light">A price list would mean charging a two-person shop and a twelve-location brand the same number for very different work. Scoping first keeps it honest, which is one of the four things this studio runs on.</p>
</section>

{testimonial("From The Main Event")}
''' + cta_band("Let&rsquo;s jam", "Ready to pick your set?", "Send a note with your business name and what you are hoping to change. I&rsquo;ll come back with a scoped set and no pressure.", "Get scoped") + footer()
open('packages.html', 'w', encoding='utf-8').write(pk)

# ---------------- PROCESS ----------------
pr = head("Process | Studio Jam", "How a project with Studio Jam goes, from the first conversation to launch and the months after.", "process")
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
      <h3>You approve everything</h3>
      <p>Nothing posts, publishes, or launches without your sign-off. You will never be surprised by your own marketing.</p>
    </div>
    <div class="pillar">
      <h3>One person to call</h3>
      <p>Alise runs every account. If a team joins the project, every communication still flows through her.</p>
    </div>
    <div class="pillar">
      <h3>Plain language, always</h3>
      <p>No jargon in the plan, no jargon in the recap. If you cannot explain it to a friend, it is not finished.</p>
    </div>
  </div>
</section>

''' + cta_band("Let&rsquo;s jam", "Step one is a conversation", "Tell me about your business, what&rsquo;s working, and what&rsquo;s not. The first conversation is on the house.", "Start the conversation") + footer()
open('process.html', 'w', encoding='utf-8').write(pr)

# ---------------- CONTACT ----------------
ct = head("Contact | Studio Jam", "Get in touch with Studio Jam, a creative marketing studio in Fayetteville, Arkansas. The first conversation is on the house.", "contact")
ct += nav("contact") + ticker("Let&rsquo;s Jam &#10039; Fayetteville, Arkansas &#10039; Working With Clients Everywhere &#10039; Let&rsquo;s Jam &#10039; Fayetteville, Arkansas &#10039; Working With Clients Everywhere")
ct += f'''<section class="page-hero with-photo contact-hero" id="top">
  <img class="hero-star star-a" src="{STAR}" alt="">
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
      <img src="/assets/img/alise-glasses.jpg" alt="Alise McCreary in glasses, smiling" width="1100" height="1375">
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
        <li>Based in Fayetteville, Arkansas, working with clients everywhere</li>
        <li>Most projects start with a short discovery call, on Zoom or in person</li>
        <li>You will always talk to Alise, not an account manager</li>
        <li>Looking for the job instead? <a href="/work-with-us">Work with us</a> has the details</li>
      </ul>
    </div>
  </div>
</section>

{testimonial("What clients say")}
''' + footer()
open('contact.html', 'w', encoding='utf-8').write(ct)

# ---------------- WORK WITH US (rebuild with shared shell) ----------------
ww = head("Work With Us | Studio Jam", "Studio Jam is hiring a part-time marketing assistant / paid intern in Fayetteville, Arkansas. Email your resume and recent work to apply.", "work-with-us")
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
  <img class="contact-star" src="{STAR}" alt="">
  <p class="kicker">How to apply</p>
  <h2>Let&rsquo;s jam</h2>
  <p>Email your resume plus any recent work (class projects, content you&rsquo;ve made, anything you&rsquo;re proud of) to:</p>
  <a class="btn btn-teal" href="mailto:{EMAIL}?subject=Marketing%20Assistant%20%2D%20Fayetteville">{EMAIL}</a>
  <p class="ig">Know someone who&rsquo;d be perfect? Send them this page.</p>
</section>

''' + footer()
open('work-with-us.html', 'w', encoding='utf-8').write(ww)

# ---------------- 404 ----------------
nf = head("Wrong Venue | Studio Jam", "That page is not on the setlist. Head back to Studio Jam.", "404", noindex=True)
nf += nav("") + page_hero("404", "Wrong venue", "That page isn&rsquo;t on the setlist. The show is still on, though.",
                          [("Back to the main stage", "/", "btn-blush btn-solid"), ("Say hello", "/contact", "btn-blush")], cls="notfound", deco=("mascot-stand.png", "stand"))
nf += footer()
open('404.html', 'w', encoding='utf-8').write(nf)
print("pages built:", [f for f in os.listdir('.') if f.endswith('.html')])
