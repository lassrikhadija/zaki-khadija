import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

STEPS_CSS = (
    '    body.theme-light .audit-pill{display:flex;align-items:center;gap:.35rem;padding:0 .875rem;height:44px;background:var(--color-primary);border-radius:22px;color:#000;font-weight:700;font-size:.78rem;text-decoration:none;white-space:nowrap;box-shadow:0 4px 16px rgba(0,230,118,.45);transition:transform .2s ease,box-shadow .2s ease;flex-shrink:0}\n'
    '    /* Steps visuels */\n'
    '    .steps--visual{list-style:none!important;display:grid!important;grid-template-columns:repeat(4,1fr)!important;gap:1.5rem!important;padding:0!important;margin:2rem 0!important}\n'
    '    .steps--visual .steps__item{position:relative;padding:1.75rem 1.25rem!important;display:flex!important;flex-direction:column!important;gap:.65rem!important;background:rgba(255,255,255,.04);border:1.5px solid rgba(255,255,255,.08);border-radius:16px;transition:border-color .2s,background .2s}\n'
    '    .steps--visual .steps__item:hover{border-color:var(--color-primary);background:rgba(0,230,118,.05)}\n'
    '    .steps--visual .steps__number{width:44px;height:44px;border-radius:50%;background:var(--color-primary);color:#000;font-weight:800;font-size:1.1rem;display:flex!important;align-items:center;justify-content:center;flex-shrink:0}\n'
    '    .steps--visual .steps__arrow{position:absolute;top:50%;right:-1.1rem;transform:translateY(-50%);color:var(--color-primary);font-size:1.2rem;font-weight:700;z-index:1;line-height:1}\n'
    '    .steps--visual .steps__title{font-size:1rem!important;font-weight:700!important;color:var(--color-text)!important;margin:0!important;line-height:1.35}\n'
    '    .steps--visual .steps__text{font-size:.875rem!important;color:var(--color-text-muted)!important;line-height:1.6!important;margin:0!important;flex:1}\n'
    '    .steps--visual .steps__link{font-size:.85rem;font-weight:700;color:var(--color-primary);text-decoration:none;margin-top:.25rem;transition:opacity .2s}\n'
    '    .steps--visual .steps__link:hover{opacity:.75}\n'
    '    @media(max-width:900px){.steps--visual{grid-template-columns:repeat(2,1fr)!important}.steps--visual .steps__arrow{display:none!important}}\n'
    '    @media(max-width:560px){.steps--visual{grid-template-columns:1fr!important}}\n'
    '  </style>'
)

OLD_STYLE_END = '    body.theme-light .audit-pill{display:flex;align-items:center;gap:.35rem;padding:0 .875rem;height:44px;background:var(--color-primary);border-radius:22px;color:#000;font-weight:700;font-size:.78rem;text-decoration:none;white-space:nowrap;box-shadow:0 4px 16px rgba(0,230,118,.45);transition:transform .2s ease,box-shadow .2s ease;flex-shrink:0}\n  </style>'

WHATSAPP_FR = 'https://wa.me/15147910591?text=Bonjour%2C%20je%20voudrais%20plus%20d%27informations%20sur%20vos%20services.'
WHATSAPP_EN = 'https://wa.me/15147910591?text=Hello%2C%20I%20would%20like%20more%20information%20about%20your%20services.'

# ═══════════════════════════════════════════
# en/secteurs.html
# ═══════════════════════════════════════════
c = read("en/secteurs.html")

# 1. Centrer les 3 headers manquants
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title">Industries where our approach works particularly well</h2>',
    '<header class="section__header section__header--center">\n          <h2 class="section__title">Industries where our approach works particularly well</h2>',
    1
)
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title">What we adapt according to your industry</h2>',
    '<header class="section__header section__header--center">\n          <h2 class="section__title">What we adapt according to your industry</h2>',
    1
)
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title">A common method, adjusted to your reality</h2>',
    '<header class="section__header section__header--center">\n          <h2 class="section__title">A common method, adjusted to your reality</h2>',
    1
)

# 2. Convertir ol.steps → steps--visual
old_ol = '''        <ol class="steps">
          <li class="steps__item">
            <h3 class="steps__title">Market and positioning analysis</h3>
            <p>We identify your services, target clients, competitors and differentiation points.</p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Page structure and key messages</h3>
            <p>We define the architecture, content priorities and calls to action that support your goals.</p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Design and optimization</h3>
            <p>We produce a fast, readable interface aligned with your market positioning and audience.</p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Local SEO and conversion deployment</h3>
            <p>We strengthen local visibility and the site\'s ability to generate concrete requests.</p>
          </li>
        </ol>'''

new_ol = '''        <ol class="steps--visual">
          <li class="steps__item">
            <div class="steps__number">1</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">Market and positioning analysis</h3>
            <p class="steps__text">We identify your services, target clients, competitors and differentiation points.</p>
          </li>
          <li class="steps__item">
            <div class="steps__number">2</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">Page structure and key messages</h3>
            <p class="steps__text">We define the architecture, content priorities and calls to action that support your goals.</p>
          </li>
          <li class="steps__item">
            <div class="steps__number">3</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">Design and optimization</h3>
            <p class="steps__text">We produce a fast, readable interface aligned with your market positioning and audience.</p>
          </li>
          <li class="steps__item">
            <div class="steps__number">4</div>
            <h3 class="steps__title">Local SEO and conversion deployment</h3>
            <p class="steps__text">We strengthen local visibility and the site\'s ability to generate concrete requests.</p>
          </li>
        </ol>'''

if old_ol in c:
    c = c.replace(old_ol, new_ol, 1)
    print("secteurs EN: ol converti")
else:
    print("secteurs EN: SKIP ol")

# 3. CSS inline
if OLD_STYLE_END in c:
    c = c.replace(OLD_STYLE_END, STEPS_CSS, 1)
    print("secteurs EN: CSS inline OK")
else:
    print("secteurs EN: SKIP CSS")

# 4. WhatsApp EN
c = c.replace(WHATSAPP_FR, WHATSAPP_EN)
print("secteurs EN: WhatsApp EN OK")

write("en/secteurs.html", c)


# ═══════════════════════════════════════════
# en/ressources.html
# ═══════════════════════════════════════════
c = read("en/ressources.html")

# 1. Centrer les 3 headers manquants
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title">Topics we cover</h2>',
    '<header class="section__header section__header--center">\n          <h2 class="section__title">Topics we cover</h2>',
    1
)
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title">What you\'ll find in this section</h2>',
    '<header class="section__header section__header--center">\n          <h2 class="section__title">What you\'ll find in this section</h2>',
    1
)
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title">How to use these resources for your project</h2>',
    '<header class="section__header section__header--center">\n          <h2 class="section__title">Where to start based on your situation</h2>',
    1
)

# 2. Convertir ol.steps → steps--visual avec liens
old_ol = '''        <ol class="steps">
          <li class="steps__item">
            <h3 class="steps__title">Clarify your offer and priority pages</h3>
            <p>Start by defining which services to highlight and which pages need to convert first.</p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Structure SEO and internal linking</h3>
            <p>Work on the relationship between your services, industries and geographic areas to avoid a scattered site.</p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Optimize messages and calls to action</h3>
            <p>Good traffic without a clear message converts poorly. Resources also help better frame your content.</p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Move to execution</h3>
            <p>Once priorities are set, connect design, technical work, SEO and conversion in one direction.</p>
          </li>
        </ol>'''

new_ol = '''        <ol class="steps--visual">
          <li class="steps__item">
            <div class="steps__number">1</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">You don\'t have a website yet</h3>
            <p class="steps__text">Understand what makes a site generate clients — before choosing a platform or an agency.</p>
            <a href="/en/blog/website-design/" class="steps__link">Website design &#8594;</a>
          </li>
          <li class="steps__item">
            <div class="steps__number">2</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">Your site generates nothing</h3>
            <p class="steps__text">Local SEO and conversion — often, it\'s not the design that\'s the problem.</p>
            <a href="/en/blog/seo/" class="steps__link">Understand SEO &#8594;</a>
          </li>
          <li class="steps__item">
            <div class="steps__number">3</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">You rank on Google, you want to go further</h3>
            <p class="steps__text">AEO and AI visibility — the lever few Quebec agencies have mastered yet.</p>
            <a href="/en/blog/ai-automation/" class="steps__link">Explore AI visibility &#8594;</a>
          </li>
          <li class="steps__item">
            <div class="steps__number">4</div>
            <h3 class="steps__title">You want to delegate everything now</h3>
            <p class="steps__text">Free audit — we analyze your situation and tell you exactly what to do, no commitment.</p>
            <a href="/en/contact.html" class="steps__link">Get my free audit &#8594;</a>
          </li>
        </ol>'''

if old_ol in c:
    c = c.replace(old_ol, new_ol, 1)
    print("ressources EN: ol converti")
else:
    print("ressources EN: SKIP ol")

# 3. CSS inline
if OLD_STYLE_END in c:
    c = c.replace(OLD_STYLE_END, STEPS_CSS, 1)
    print("ressources EN: CSS inline OK")
else:
    print("ressources EN: SKIP CSS")

# 4. WhatsApp EN
c = c.replace(WHATSAPP_FR, WHATSAPP_EN)
print("ressources EN: WhatsApp EN OK")

write("en/ressources.html", c)
print("\nTermine.")
