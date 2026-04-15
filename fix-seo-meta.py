import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija'

# ─── Fixes: {relative_path: {'title': new, 'desc': new, 'h1': new}} ──────────
FIXES = {
    'index.html': {
        'title': 'Agence web Montréal | SEO & Marketing digital | NEXTIWEB',
        'desc':  'NEXTIWEB crée des sites web rapides, optimisés SEO et pensés pour convertir vos visiteurs en clients. Audit gratuit pour PME à Montréal.',
    },
    'contact.html': {
        'title': 'Contact | Agence web à Montréal — NEXTIWEB',
        'desc':  'Contactez NEXTIWEB pour votre site web, SEO ou marketing digital. Réponse sous 24 h. Audit gratuit pour PME et entreprises de services.',
    },
    'ressources.html': {
        'title': 'Ressources web et SEO gratuites au Québec | NEXTIWEB',
        'desc':  'Guides gratuits sur la création de sites web, le SEO local, le marketing digital et la visibilité IA pour PME au Québec. Apprenez et décidez.',
    },
    'services.html': {
        'title': 'Services web, SEO et marketing digital | NEXTIWEB',
        'desc':  'Création de sites web, SEO et marketing digital à Montréal. NEXTIWEB accompagne les PME pour générer plus de leads qualifiés en ligne.',
    },
    'seo.html': {
        'title': 'SEO Montréal | Référencement naturel pour PME | NEXTIWEB',
        'desc':  'Services SEO à Montréal : SEO local, technique et contenu pour PME. Améliorez votre classement Google et attirez des clients qualifiés.',
    },
    'creation-site.html': {
        'desc':  'Création de sites web professionnels et convertissants à Montréal. Sites vitrines, refonte, SEO intégré. Obtenez plus de clients en ligne.',
    },
    'marketing-digital.html': {
        'desc':  'Marketing digital à Montréal : stratégie de contenu, optimisation de conversion. Augmentez vos leads qualifiés avec NEXTIWEB.',
    },
    'a-propos.html': {
        'title': 'À propos — Khadija AitLassri | NEXTIWEB Montréal',
    },
    'visibilite-ia.html': {
        'desc':  'Faites recommander votre entreprise par ChatGPT, Perplexity et Google IA. NEXTIWEB optimise votre contenu pour les moteurs IA (AEO/GEO).',
    },
    os.path.join('zones-desservies', 'canada.html'): {
        'title': 'Services web au Canada | PME | NEXTIWEB',
        'desc':  'NEXTIWEB accompagne les PME et entreprises de services au Canada en création web, SEO local et marketing digital. Résultats mesurables.',
    },
    os.path.join('zones-desservies', 'montreal.html'): {
        'title': 'Agence web Montréal | PME | NEXTIWEB',
        'desc':  'NEXTIWEB accompagne les PME à Montréal avec une stratégie web, SEO local et marketing digital pour attirer plus de clients qualifiés.',
    },
    os.path.join('zones-desservies', 'quebec.html'): {
        'title': 'Agence web Québec | PME | NEXTIWEB',
        'desc':  'NEXTIWEB accompagne les PME à Québec avec une stratégie web, SEO local et marketing digital pour attirer plus de clients qualifiés.',
    },
    os.path.join('zones-desservies', 'index.html'): {
        'desc':  'Découvrez les zones desservies par NEXTIWEB : Montréal, Québec et partout au Canada. Services web, SEO et marketing digital pour PME.',
    },
    os.path.join('local', 'seo-montreal.html'): {
        'title': 'Services SEO Montréal | PME | NEXTIWEB',
        'desc':  'Services SEO à Montréal pour PME : structure technique, contenu et maillage interne. Apparaissez en tête de Google pour vos mots-clés.',
    },
    os.path.join('local', 'marketing-digital-montreal.html'): {
        'title': 'Marketing digital Montréal | PME | NEXTIWEB',
        'desc':  'Marketing digital à Montréal pour PME : stratégie, contenu et conversion. NEXTIWEB vous aide à générer des leads qualifiés en ligne.',
    },
    os.path.join('local', 'creation-site-web-montreal.html'): {
        'desc':  'Création de sites web à Montréal pour PME : structure claire, SEO intégré et UX moderne. Attirez plus de clients qualifiés en ligne.',
    },
    # EN versions
    os.path.join('en', 'index.html'): {
        'title': 'Web Agency Montreal | SEO & Digital Marketing | NEXTIWEB',
        'desc':  'NEXTIWEB builds fast, SEO-optimized websites that convert visitors into clients. Free audit for SMEs in Montreal.',
    },
    os.path.join('en', 'contact.html'): {
        'title': 'Contact | Montreal Web Agency — NEXTIWEB',
        'desc':  'Contact NEXTIWEB for your website, SEO or digital marketing. Response within 24 h. Free audit for SMEs and service businesses.',
    },
    os.path.join('en', 'ressources.html'): {
        'title': 'SEO & Web Resources in Montreal | NEXTIWEB',
    },
    os.path.join('en', 'services.html'): {
        'title': 'Web Design, SEO & Digital Marketing Montreal | NEXTIWEB',
        'desc':  'NEXTIWEB is a Montreal web agency specialized in website design, SEO and digital marketing. Get more qualified leads with a strategy that works.',
    },
    os.path.join('en', 'visibilite-ia.html'): {
        'desc':  'Get recommended by ChatGPT, Perplexity and Google AI. NEXTIWEB optimizes your content for AI engines (AEO/GEO) to drive qualified traffic.',
    },
    os.path.join('en', 'zones-desservies', 'canada.html'): {
        'title': 'Web Services Canada | SMEs | NEXTIWEB',
    },
    os.path.join('en', 'zones-desservies', 'montreal.html'): {
        'title': 'Web Agency Montreal | SMEs | NEXTIWEB',
    },
    os.path.join('en', 'zones-desservies', 'quebec.html'): {
        'title': 'Web Agency Quebec City | SMEs | NEXTIWEB',
    },
    os.path.join('en', 'local', 'seo-montreal.html'): {
        'title': 'SEO Services Montreal | SMEs | NEXTIWEB',
    },
    os.path.join('en', 'local', 'marketing-digital-montreal.html'): {
        'title': 'Digital Marketing Montreal | SMEs | NEXTIWEB',
    },
}

updated = 0
for rel, fixes in FIXES.items():
    fp = os.path.join(base, rel)
    if not os.path.exists(fp):
        print(f'MISSING: {rel}')
        continue

    try:
        content = open(fp, encoding='utf-8').read()
    except:
        content = open(fp, encoding='latin-1').read()

    original = content

    # Fix title
    if 'title' in fixes:
        new_title = fixes['title']
        content = re.sub(
            r'(<title[^>]*>).*?(</title>)',
            lambda m: m.group(1) + new_title + m.group(2),
            content, flags=re.DOTALL
        )

    # Fix meta description
    if 'desc' in fixes:
        new_desc = fixes['desc']
        # Pattern 1: name first
        content = re.sub(
            r'(<meta\s[^>]*name=["\']description["\'][^>]*content=["\'])([^"\']*?)(["\'])',
            lambda m: m.group(1) + new_desc + m.group(3),
            content, flags=re.IGNORECASE
        )
        # Pattern 2: content first
        content = re.sub(
            r'(<meta\s[^>]*content=["\'])([^"\']*?)(["\'][^>]*name=["\']description["\'])',
            lambda m: m.group(1) + new_desc + m.group(3),
            content, flags=re.IGNORECASE
        )

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        # Verify
        new_title_check = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
        t = re.sub(r'<[^>]+>', '', new_title_check.group(1)).strip() if new_title_check else ''
        flag = 'OK' if len(t) <= 60 else f'STILL {len(t)}c'
        print(f'  [{flag}] {rel}')
    else:
        print(f'  [UNCHANGED] {rel}')

print(f'\nDone: {updated} files updated.')
