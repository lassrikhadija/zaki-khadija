import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

c = read("ressources.html")

# ── 1. Ajouter section__header--center aux 2 sections sans ──
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title" id="sujets-ressources">',
    '<header class="section__header section__header--center">\n          <h2 class="section__title" id="sujets-ressources">',
    1
)
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title">Par où commencer selon votre situation</h2>',
    '<header class="section__header section__header--center">\n          <h2 class="section__title">Par où commencer selon votre profil</h2>',
    1
)

# ── 2. Raccourcir le titre trop long ──
c = c.replace(
    'Ce que vous trouverez ici — et ce que vous ne trouverez pas',
    'Ce qu’il y a ici — et ce qu’il n’y a pas',
    1
)

# ── 3. Convertir ol.steps en steps--visual avec liens propres ──
old_ol = '''        <ol class="steps">
          <li class="steps__item">
            <h3 class="steps__title">Vous n\'avez pas encore de site</h3>
            <p>Commencez par comprendre ce qui fait qu\'un site génère des clients — avant de choisir une plateforme ou de contacter une agence. <a href="/blog/creation-site/" style="color:var(--color-accent)">Créer un site web →</a></p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Vous avez un site mais il ne génère rien</h3>
            <p>Lisez d\'abord sur le SEO local et la conversion — souvent, ce n\'est pas le design qui pose problème. <a href="/blog/seo/" style="color:var(--color-accent)">Comprendre le SEO →</a></p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Vous êtes bien positionné sur Google mais voulez aller plus loin</h3>
            <p>Découvrez l\'AEO et la visibilité IA — le prochain levier de croissance que peu d\'agences québécoises maîtrisent encore. <a href="/blog/ia-automatisation/" style="color:var(--color-accent)">Explorer la visibilité IA →</a></p>
          </li>
          <li class="steps__item">
            <h3 class="steps__title">Vous voulez tout déléguer dès maintenant</h3>
            <p>Passez directement à l\'audit gratuit. On analyse votre situation et on vous dit exactement ce qu\'il faut faire — sans engagement. <a href="/contact.html" style="color:var(--color-accent)">Demander mon audit →</a></p>
          </li>
        </ol>'''

new_ol = '''        <ol class="steps--visual">
          <li class="steps__item">
            <div class="steps__number">1</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">Vous n\'avez pas encore de site</h3>
            <p class="steps__text">Comprenez ce qui fait qu\'un site génère des clients — avant de choisir une plateforme ou une agence.</p>
            <a href="/blog/creation-site/" class="steps__link">Créer un site web &#8594;</a>
          </li>
          <li class="steps__item">
            <div class="steps__number">2</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">Votre site ne génère rien</h3>
            <p class="steps__text">Le SEO local et la conversion — souvent, ce n\'est pas le design qui pose problème.</p>
            <a href="/blog/seo/" class="steps__link">Comprendre le SEO &#8594;</a>
          </li>
          <li class="steps__item">
            <div class="steps__number">3</div>
            <div class="steps__arrow">&#8594;</div>
            <h3 class="steps__title">Vous êtes sur Google, vous voulez aller plus loin</h3>
            <p class="steps__text">L\'AEO et la visibilité IA — le levier que peu d\'agences québécoises maîtrisent encore.</p>
            <a href="/blog/ia-automatisation/" class="steps__link">Explorer la visibilité IA &#8594;</a>
          </li>
          <li class="steps__item">
            <div class="steps__number">4</div>
            <h3 class="steps__title">Vous voulez tout déléguer maintenant</h3>
            <p class="steps__text">Audit gratuit — on analyse votre situation et on vous dit exactement ce qu\'il faut faire, sans engagement.</p>
            <a href="/contact.html" class="steps__link">Demander mon audit &#8594;</a>
          </li>
        </ol>'''

if old_ol in c:
    c = c.replace(old_ol, new_ol, 1)
    print("ol steps converti: OK")
else:
    print("SKIP ol: pattern not found")
    lines = c.split('\n')
    for i, l in enumerate(lines[260:285], start=261):
        print(f"{i}: {repr(l)}")

# ── 4. Injecter le CSS steps--visual inline ──
old_style_end = '    body.theme-light .audit-pill{display:flex;align-items:center;gap:.35rem;padding:0 .875rem;height:44px;background:var(--color-primary);border-radius:22px;color:#000;font-weight:700;font-size:.78rem;text-decoration:none;white-space:nowrap;box-shadow:0 4px 16px rgba(0,230,118,.45);transition:transform .2s ease,box-shadow .2s ease;flex-shrink:0}\n  </style>'

new_style_end = (
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

if old_style_end in c:
    c = c.replace(old_style_end, new_style_end, 1)
    print("CSS steps inline: OK")
else:
    print("SKIP CSS: pattern not found")

write("ressources.html", c)
print("Termine.")
