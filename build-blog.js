// Script de génération des pages blog NEXTIWEB
// Exécuter avec : node build-blog.js

const fs = require('fs');
const path = require('path');

const ROOT = __dirname;

const favicons = `  <link rel="icon" type="image/x-icon" href="/assets/icons/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/favicon-180.png">`;

function frHeader(activeBlog) {
  return `  <div class="top-bar"><div class="container top-bar__inner"><p class="top-bar__message" id="top-bar-message"></p></div></div>
  <header class="site-header">
    <div class="container header__inner">
      <a href="/" class="logo"><img src="/assets/img/logo/logo-nextiweb-agence-web-montreal.png" alt="NEXTIWEB - Agence web à Montréal" width="160" height="40" loading="eager"></a>
      <nav class="main-nav" aria-label="Navigation principale">
        <div class="nav__item">
          <a href="/services.html" class="nav__link">Services</a>
          <div class="nav__submenu">
            <a href="/creation-site.html" class="nav__submenu-link">Création de sites web</a>
            <a href="/seo.html" class="nav__submenu-link">Référencement SEO</a>
            <a href="/marketing-digital.html" class="nav__submenu-link">Marketing digital</a>
          </div>
        </div>
        <a href="/secteurs.html" class="nav__link">Secteurs</a>
        <a href="/blog/" class="nav__link${activeBlog ? ' nav__link--active' : ''}">Blog</a>
        <a href="/a-propos.html" class="nav__link">À propos</a>
        <a href="/contact.html" class="nav__link nav__link--cta">Demander mon audit gratuit</a>
      </nav>
      <button class="theme-toggle" type="button" aria-label="Changer de thème"></button>
    </div>
  </header>`;
}

function enHeader(activeBlog) {
  return `  <div class="top-bar"><div class="container top-bar__inner"><p class="top-bar__message" id="top-bar-message"></p></div></div>
  <header class="site-header">
    <div class="container header__inner">
      <a href="/en/index.html" class="logo"><img src="/assets/img/logo/logo-nextiweb-agence-web-montreal.png" alt="NEXTIWEB - Web agency in Montreal" width="160" height="40" loading="eager"></a>
      <nav class="main-nav" aria-label="Main navigation">
        <div class="nav__item">
          <a href="/en/services.html" class="nav__link">Services</a>
          <div class="nav__submenu">
            <a href="/en/creation-site.html" class="nav__submenu-link">Website Design</a>
            <a href="/en/seo.html" class="nav__submenu-link">SEO</a>
            <a href="/en/marketing-digital.html" class="nav__submenu-link">Digital Marketing</a>
          </div>
        </div>
        <a href="/en/secteurs.html" class="nav__link">Industries</a>
        <a href="/en/blog/" class="nav__link${activeBlog ? ' nav__link--active' : ''}">Blog</a>
        <a href="/en/a-propos.html" class="nav__link">About</a>
        <a href="/en/contact.html" class="nav__link nav__link--cta">Get My Free Audit</a>
      </nav>
      <button class="theme-toggle" type="button" aria-label="Toggle theme"></button>
    </div>
  </header>`;
}

const frFooter = `  <footer class="site-footer">
    <div class="container footer__inner">
      <div class="footer__col">
        <p class="footer__logo">NEXTIWEB</p>
        <p class="footer__text">Agence web spécialisée en création de sites web, SEO et marketing digital.</p>
        <address class="footer__address">Montréal, Québec, Canada<br><a href="tel:+15147910591">514-791-0591</a><br><a href="mailto:contact@nextiweb.ca">contact@nextiweb.ca</a></address>
      </div>
      <div class="footer__col">
        <h3 class="footer__title">Navigation</h3>
        <ul class="footer__list"><li><a href="/">Accueil</a></li><li><a href="/services.html">Services</a></li><li><a href="/blog/">Blog</a></li><li><a href="/a-propos.html">À propos</a></li><li><a href="/contact.html">Contact</a></li></ul>
      </div>
      <div class="footer__col">
        <h3 class="footer__title">Blog</h3>
        <ul class="footer__list"><li><a href="/blog/creation-site/">Création de sites</a></li><li><a href="/blog/seo/">SEO</a></li><li><a href="/blog/marketing-digital/">Marketing digital</a></li><li><a href="/blog/ia-automatisation/">IA &amp; Automatisation</a></li></ul>
      </div>
      <div class="footer__col">
        <h3 class="footer__title">Zones desservies</h3>
        <ul class="footer__list"><li><a href="/zones-desservies/montreal.html">Montréal</a></li><li><a href="/zones-desservies/quebec.html">Québec</a></li><li><a href="/zones-desservies/canada.html">Canada</a></li></ul>
      </div>
    </div>
    <div class="container footer__bottom"><p>© 2026 NEXTIWEB. Tous droits réservés.</p></div>
  </footer>`;

const enFooter = `  <footer class="site-footer">
    <div class="container footer__inner">
      <div class="footer__col">
        <p class="footer__logo">NEXTIWEB</p>
        <p class="footer__text">Web agency specialized in website design, SEO and digital marketing.</p>
        <address class="footer__address">Montreal, Quebec, Canada<br><a href="tel:+15147910591">514-791-0591</a><br><a href="mailto:contact@nextiweb.ca">contact@nextiweb.ca</a></address>
      </div>
      <div class="footer__col">
        <h3 class="footer__title">Navigation</h3>
        <ul class="footer__list"><li><a href="/en/index.html">Home</a></li><li><a href="/en/services.html">Services</a></li><li><a href="/en/blog/">Blog</a></li><li><a href="/en/a-propos.html">About</a></li><li><a href="/en/contact.html">Contact</a></li></ul>
      </div>
      <div class="footer__col">
        <h3 class="footer__title">Blog</h3>
        <ul class="footer__list"><li><a href="/en/blog/website-design/">Website Design</a></li><li><a href="/en/blog/seo/">SEO</a></li><li><a href="/en/blog/digital-marketing/">Digital Marketing</a></li><li><a href="/en/blog/ai-automation/">AI &amp; Automation</a></li></ul>
      </div>
      <div class="footer__col">
        <h3 class="footer__title">Areas Served</h3>
        <ul class="footer__list"><li><a href="/en/zones-desservies/montreal.html">Montreal</a></li><li><a href="/en/zones-desservies/quebec.html">Quebec City</a></li><li><a href="/en/zones-desservies/canada.html">Canada</a></li></ul>
      </div>
    </div>
    <div class="container footer__bottom"><p>© 2026 NEXTIWEB. All rights reserved.</p></div>
  </footer>`;

function frCTA() {
  return `    <section class="section section--cta">
      <div class="container section__header section__header--center">
        <h2 class="section__title">Prêt à développer votre présence en ligne\u00a0?</h2>
        <p class="section__text">Parlons de votre projet et voyons comment transformer votre site web en un véritable outil pour attirer des clients.</p>
        <a href="/contact.html" class="btn btn--primary">Demander mon audit gratuit</a>
      </div>
    </section>`;
}

function enCTA() {
  return `    <section class="section section--cta">
      <div class="container section__header section__header--center">
        <h2 class="section__title">Ready to grow your online presence?</h2>
        <p class="section__text">Let's talk about your project and see how we can turn your website into a real client-generating machine.</p>
        <a href="/en/contact.html" class="btn btn--primary">Request My Free Audit</a>
      </div>
    </section>`;
}

function breadcrumb(items) {
  return `    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      ${items.map((item, i) => i < items.length - 1
        ? `<a href="${item.href}">${item.label}</a> <span aria-hidden="true">›</span>`
        : `<span>${item.label}</span>`
      ).join(' ')}
    </nav>`;
}

// ============================================================
// 1. blog/index.html — FR
// ============================================================
const blogIndexFR = `<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog | Création de sites, SEO, Marketing &amp; IA | NEXTIWEB</title>
  <meta name="description" content="Conseils experts en création de sites web, SEO, marketing digital et IA pour les PME de Montréal à croître en ligne.">
  <meta property="og:type" content="website"><meta property="og:site_name" content="NEXTIWEB">
  <meta property="og:locale" content="fr_CA">
  <meta property="og:title" content="Blog NEXTIWEB | SEO, Sites web, Marketing &amp; IA">
  <meta property="og:description" content="Conseils experts pour propulser votre présence en ligne.">
  <meta property="og:url" content="https://nextiweb.ca/blog/">
  <meta property="og:image" content="https://nextiweb.ca/assets/img/logo/og-image-nextiweb.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Blog NEXTIWEB">
  <meta name="twitter:description" content="Conseils experts pour votre présence en ligne.">
  <link rel="canonical" href="https://nextiweb.ca/blog/">
  <link rel="alternate" hreflang="fr" href="https://nextiweb.ca/blog/">
  <link rel="alternate" hreflang="en" href="https://nextiweb.ca/en/blog/">
  <link rel="alternate" hreflang="x-default" href="https://nextiweb.ca/blog/">
${favicons}
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body class="theme-dark">
${frHeader(true)}
  <main>
    <section class="blog-hero section">
      <div class="container">
        <span class="blog-hero__kicker">Ressources &amp; conseils</span>
        <h1 class="blog-hero__title">Le Blog <span class="blog-hero__brand">NEXTIWEB</span></h1>
        <p class="blog-hero__subtitle">Conseils experts pour propulser votre présence en ligne — création de sites, SEO, marketing digital et IA.</p>
        <div class="blog-search" role="search">
          <input type="search" class="blog-search__input" placeholder="Rechercher un article..." aria-label="Rechercher un article">
          <button class="blog-search__btn" type="button">Rechercher</button>
        </div>
      </div>
    </section>
    <section class="blog-categories section section--alt-bg">
      <div class="container">
        <header class="section__header section__header--center">
          <h2 class="section__title">Explorez par catégorie</h2>
          <p class="section__subtitle">Quatre domaines d'expertise, des centaines de conseils à venir.</p>
        </header>
        <div class="blog-cat-grid">
          <a href="/blog/creation-site/" class="blog-cat-card blog-cat-card--site"><span class="blog-cat-card__icon">🖥</span><h3 class="blog-cat-card__title">Création de sites web</h3><p class="blog-cat-card__desc">Sites web, landing pages, UX/UI et performance</p><span class="blog-cat-card__link">Explorer →</span></a>
          <a href="/blog/seo/" class="blog-cat-card blog-cat-card--seo"><span class="blog-cat-card__icon">🔍</span><h3 class="blog-cat-card__title">SEO &amp; Référencement</h3><p class="blog-cat-card__desc">Référencement naturel, SEO local, technique</p><span class="blog-cat-card__link">Explorer →</span></a>
          <a href="/blog/marketing-digital/" class="blog-cat-card blog-cat-card--marketing"><span class="blog-cat-card__icon">📈</span><h3 class="blog-cat-card__title">Marketing digital</h3><p class="blog-cat-card__desc">Google Ads, réseaux sociaux, email marketing</p><span class="blog-cat-card__link">Explorer →</span></a>
          <a href="/blog/ia-automatisation/" class="blog-cat-card blog-cat-card--ia"><span class="blog-cat-card__icon">🤖</span><h3 class="blog-cat-card__title">IA &amp; Automatisation</h3><p class="blog-cat-card__desc">ChatGPT, workflows automatisés, outils IA</p><span class="blog-cat-card__link">Explorer →</span></a>
        </div>
      </div>
    </section>
    <section class="blog-posts section">
      <div class="container">
        <h2 class="section__title">Articles récents</h2>
        <p class="blog-empty">Les premiers articles arrivent bientôt. Revenez nous voir\u00a0!</p>
      </div>
    </section>
${frCTA()}
  </main>
${frFooter}
  <script src="/assets/js/main.js"></script>
</body>
</html>`;

// ============================================================
// FR Category pages builder
// ============================================================
function buildFRCategory({ slug, title, icon, desc, subtitle, hreflangEN, canonical }) {
  return `<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} — Blog | NEXTIWEB Montréal</title>
  <meta name="description" content="${desc}">
  <meta property="og:type" content="website"><meta property="og:site_name" content="NEXTIWEB">
  <meta property="og:locale" content="fr_CA">
  <meta property="og:title" content="${title} — Blog | NEXTIWEB">
  <meta property="og:description" content="${desc}">
  <meta property="og:url" content="https://nextiweb.ca/blog/${slug}/">
  <meta property="og:image" content="https://nextiweb.ca/assets/img/logo/og-image-nextiweb.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title} — Blog NEXTIWEB">
  <meta name="twitter:description" content="${desc}">
  <link rel="canonical" href="https://nextiweb.ca/blog/${slug}/">
  <link rel="alternate" hreflang="fr" href="https://nextiweb.ca/blog/${slug}/">
  <link rel="alternate" hreflang="en" href="https://nextiweb.ca/en/blog/${hreflangEN}/">
  <link rel="alternate" hreflang="x-default" href="https://nextiweb.ca/blog/${slug}/">
${favicons}
  <link rel="stylesheet" href="/assets/css/styles.css">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://nextiweb.ca/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://nextiweb.ca/blog/"},{"@type":"ListItem","position":3,"name":"${title}","item":"https://nextiweb.ca/blog/${slug}/"}]}
  </script>
</head>
<body class="theme-dark">
${frHeader(false)}
  <main>
${breadcrumb([{href:'/', label:'Accueil'},{href:'/blog/', label:'Blog'},{href:'', label:title}])}
    <section class="blog-hero section">
      <div class="container">
        <span class="blog-hero__kicker">Catégorie</span>
        <h1 class="blog-hero__title">${icon} ${title}</h1>
        <p class="blog-hero__subtitle">${subtitle}</p>
      </div>
    </section>
    <section class="blog-posts section">
      <div class="container">
        <p class="blog-empty">Les premiers articles de cette catégorie arrivent bientôt.</p>
        <div class="section__actions">
          <a href="/blog/" class="btn btn--ghost">← Retour au blog</a>
        </div>
      </div>
    </section>
${frCTA()}
  </main>
${frFooter}
  <script src="/assets/js/main.js"></script>
</body>
</html>`;
}

// ============================================================
// EN Index blog
// ============================================================
const blogIndexEN = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog | Website Design, SEO, Marketing &amp; AI | NEXTIWEB</title>
  <meta name="description" content="Expert tips on website design, SEO, digital marketing and AI to help Montreal SMEs grow online.">
  <meta property="og:type" content="website"><meta property="og:site_name" content="NEXTIWEB">
  <meta property="og:locale" content="en_CA">
  <meta property="og:title" content="NEXTIWEB Blog | SEO, Websites, Marketing &amp; AI">
  <meta property="og:description" content="Expert tips to boost your online presence.">
  <meta property="og:url" content="https://nextiweb.ca/en/blog/">
  <meta property="og:image" content="https://nextiweb.ca/assets/img/logo/og-image-nextiweb.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="NEXTIWEB Blog">
  <meta name="twitter:description" content="Expert tips for your online presence.">
  <link rel="canonical" href="https://nextiweb.ca/en/blog/">
  <link rel="alternate" hreflang="fr" href="https://nextiweb.ca/blog/">
  <link rel="alternate" hreflang="en" href="https://nextiweb.ca/en/blog/">
  <link rel="alternate" hreflang="x-default" href="https://nextiweb.ca/blog/">
${favicons}
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body class="theme-dark">
${enHeader(true)}
  <main>
    <section class="blog-hero section">
      <div class="container">
        <span class="blog-hero__kicker">Resources &amp; tips</span>
        <h1 class="blog-hero__title">The <span class="blog-hero__brand">NEXTIWEB</span> Blog</h1>
        <p class="blog-hero__subtitle">Expert tips to boost your online presence — website design, SEO, digital marketing and AI.</p>
        <div class="blog-search" role="search">
          <input type="search" class="blog-search__input" placeholder="Search articles..." aria-label="Search articles">
          <button class="blog-search__btn" type="button">Search</button>
        </div>
      </div>
    </section>
    <section class="blog-categories section section--alt-bg">
      <div class="container">
        <header class="section__header section__header--center">
          <h2 class="section__title">Browse by category</h2>
          <p class="section__subtitle">Four areas of expertise, hundreds of tips to come.</p>
        </header>
        <div class="blog-cat-grid">
          <a href="/en/blog/website-design/" class="blog-cat-card blog-cat-card--site"><span class="blog-cat-card__icon">🖥</span><h3 class="blog-cat-card__title">Website Design</h3><p class="blog-cat-card__desc">Websites, landing pages, UX/UI and performance</p><span class="blog-cat-card__link">Explore →</span></a>
          <a href="/en/blog/seo/" class="blog-cat-card blog-cat-card--seo"><span class="blog-cat-card__icon">🔍</span><h3 class="blog-cat-card__title">SEO &amp; Search</h3><p class="blog-cat-card__desc">Natural SEO, local SEO, technical optimization</p><span class="blog-cat-card__link">Explore →</span></a>
          <a href="/en/blog/digital-marketing/" class="blog-cat-card blog-cat-card--marketing"><span class="blog-cat-card__icon">📈</span><h3 class="blog-cat-card__title">Digital Marketing</h3><p class="blog-cat-card__desc">Google Ads, social media, email marketing</p><span class="blog-cat-card__link">Explore →</span></a>
          <a href="/en/blog/ai-automation/" class="blog-cat-card blog-cat-card--ia"><span class="blog-cat-card__icon">🤖</span><h3 class="blog-cat-card__title">AI &amp; Automation</h3><p class="blog-cat-card__desc">ChatGPT, automated workflows, AI tools</p><span class="blog-cat-card__link">Explore →</span></a>
        </div>
      </div>
    </section>
    <section class="blog-posts section">
      <div class="container">
        <h2 class="section__title">Recent articles</h2>
        <p class="blog-empty">First articles coming soon. Check back soon!</p>
      </div>
    </section>
${enCTA()}
  </main>
${enFooter}
  <script src="/assets/js/main.js"></script>
</body>
</html>`;

// ============================================================
// EN Category pages builder
// ============================================================
function buildENCategory({ slug, title, icon, desc, subtitle, hreflangFR, canonical }) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} — Blog | NEXTIWEB Montreal</title>
  <meta name="description" content="${desc}">
  <meta property="og:type" content="website"><meta property="og:site_name" content="NEXTIWEB">
  <meta property="og:locale" content="en_CA">
  <meta property="og:title" content="${title} — Blog | NEXTIWEB">
  <meta property="og:description" content="${desc}">
  <meta property="og:url" content="https://nextiweb.ca/en/blog/${slug}/">
  <meta property="og:image" content="https://nextiweb.ca/assets/img/logo/og-image-nextiweb.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title} — NEXTIWEB Blog">
  <meta name="twitter:description" content="${desc}">
  <link rel="canonical" href="https://nextiweb.ca/en/blog/${slug}/">
  <link rel="alternate" hreflang="fr" href="https://nextiweb.ca/blog/${hreflangFR}/">
  <link rel="alternate" hreflang="en" href="https://nextiweb.ca/en/blog/${slug}/">
  <link rel="alternate" hreflang="x-default" href="https://nextiweb.ca/blog/${hreflangFR}/">
${favicons}
  <link rel="stylesheet" href="/assets/css/styles.css">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://nextiweb.ca/en/index.html"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://nextiweb.ca/en/blog/"},{"@type":"ListItem","position":3,"name":"${title}","item":"https://nextiweb.ca/en/blog/${slug}/"}]}
  </script>
</head>
<body class="theme-dark">
${enHeader(false)}
  <main>
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/en/index.html">Home</a> <span aria-hidden="true">›</span> <a href="/en/blog/">Blog</a> <span aria-hidden="true">›</span> <span>${title}</span>
    </nav>
    <section class="blog-hero section">
      <div class="container">
        <span class="blog-hero__kicker">Category</span>
        <h1 class="blog-hero__title">${icon} ${title}</h1>
        <p class="blog-hero__subtitle">${subtitle}</p>
      </div>
    </section>
    <section class="blog-posts section">
      <div class="container">
        <p class="blog-empty">First articles in this category coming soon.</p>
        <div class="section__actions">
          <a href="/en/blog/" class="btn btn--ghost">← Back to blog</a>
        </div>
      </div>
    </section>
${enCTA()}
  </main>
${enFooter}
  <script src="/assets/js/main.js"></script>
</body>
</html>`;
}

// ============================================================
// Write all files
// ============================================================
function writeFile(filePath, content) {
  const fullPath = path.join(ROOT, filePath);
  fs.mkdirSync(path.dirname(fullPath), { recursive: true });
  fs.writeFileSync(fullPath, content, 'utf8');
  console.log('Created: ' + filePath);
}

writeFile('blog/index.html', blogIndexFR);
writeFile('en/blog/index.html', blogIndexEN);

// FR categories
writeFile('blog/creation-site/index.html', buildFRCategory({
  slug: 'creation-site',
  title: 'Création de sites web',
  icon: '🖥',
  desc: 'Conseils et guides sur la création de sites web, landing pages et UX pour les PME de Montréal.',
  subtitle: 'Guides, conseils et bonnes pratiques pour créer un site web performant.',
  hreflangEN: 'website-design'
}));

writeFile('blog/seo/index.html', buildFRCategory({
  slug: 'seo',
  title: 'SEO & Référencement naturel',
  icon: '🔍',
  desc: 'Stratégies SEO, référencement local et techniques pour améliorer votre visibilité sur Google à Montréal.',
  subtitle: 'Stratégies, techniques et conseils pour dominer Google.',
  hreflangEN: 'seo'
}));

writeFile('blog/marketing-digital/index.html', buildFRCategory({
  slug: 'marketing-digital',
  title: 'Marketing digital',
  icon: '📈',
  desc: 'Google Ads, réseaux sociaux, email marketing : stratégies digitales pour les PME de Montréal.',
  subtitle: 'Stratégies éprouvées pour attirer et convertir vos clients en ligne.',
  hreflangEN: 'digital-marketing'
}));

writeFile('blog/ia-automatisation/index.html', buildFRCategory({
  slug: 'ia-automatisation',
  title: 'IA & Automatisation',
  icon: '🤖',
  desc: 'Intelligence artificielle, workflows automatisés et outils IA pour les PME : guides pratiques par NEXTIWEB.',
  subtitle: 'Exploitez l\'intelligence artificielle et l\'automatisation pour faire croître votre business.',
  hreflangEN: 'ai-automation'
}));

// EN categories
writeFile('en/blog/website-design/index.html', buildENCategory({
  slug: 'website-design',
  title: 'Website Design',
  icon: '🖥',
  desc: 'Tips and guides on website design, landing pages and UX for Montreal SMEs.',
  subtitle: 'Guides, tips and best practices to build a high-performing website.',
  hreflangFR: 'creation-site'
}));

writeFile('en/blog/seo/index.html', buildENCategory({
  slug: 'seo',
  title: 'SEO & Search Engine Optimization',
  icon: '🔍',
  desc: 'SEO strategies, local search and techniques to improve your Google visibility in Montreal.',
  subtitle: 'Strategies, techniques and tips to dominate Google.',
  hreflangFR: 'seo'
}));

writeFile('en/blog/digital-marketing/index.html', buildENCategory({
  slug: 'digital-marketing',
  title: 'Digital Marketing',
  icon: '📈',
  desc: 'Google Ads, social media, email marketing: digital strategies for Montreal SMEs.',
  subtitle: 'Proven strategies to attract and convert your clients online.',
  hreflangFR: 'marketing-digital'
}));

writeFile('en/blog/ai-automation/index.html', buildENCategory({
  slug: 'ai-automation',
  title: 'AI & Automation',
  icon: '🤖',
  desc: 'Artificial intelligence, automated workflows and AI tools for SMEs: practical guides by NEXTIWEB.',
  subtitle: 'Leverage artificial intelligence and automation to grow your business.',
  hreflangFR: 'ia-automatisation'
}));

console.log('\nAll 10 blog pages created successfully!');
