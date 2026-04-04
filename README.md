# NEXTIWEB — Site vitrine agence web Montréal

Site statique HTML/CSS de l'agence **NEXTIWEB**, optimisé pour le SEO local (Montréal / Québec / Canada), la conversion et la performance. Entièrement bilingue **français / anglais**.

---

## Objectifs du site

- Présenter NEXTIWEB comme une **agence web moderne** (création de sites, SEO, marketing digital, IA).
- Générer des **demandes d'audit gratuit** (formulaire de contact + clics téléphone/email).
- Dominer le **SEO local** à Montréal avec une architecture pilier/enfants/local.
- Accueillir un **blog évolutif** classé par catégories pour le référencement naturel à long terme.
- Servir de **vitrine de qualité** démontrant l'expertise UX/SEO/dev de l'agence.

---

## Architecture complète des fichiers

```
nextiweb-site/                              # Racine du projet
│
│ ── Pages principales (FR)
├── index.html                              # Accueil FR — hero WOW, métriques, FAQ, CTA
├── services.html                           # Page Pilier Services (vue d'ensemble)
├── creation-site.html                      # Enfant Services : Création de sites web
├── seo.html                                # Enfant Services : Référencement SEO
├── marketing-digital.html                  # Enfant Services : Marketing digital
├── secteurs.html                           # Secteurs d'activité ciblés
├── ressources.html                         # Hub ressources / guides
├── a-propos.html                           # À propos de NEXTIWEB
├── contact.html                            # Formulaire de contact / audit gratuit
├── mentions-legales.html                   # Mentions légales
├── politique-confidentialite.html          # Politique de confidentialité (Loi 25)
├── politique-cookies.html                  # Politique de cookies (Loi 25)
│
│ ── Blog FR (SEO long terme par catégorie)
├── blog/
│   ├── index.html                          # Hub blog : liste des catégories + barre de recherche
│   ├── creation-site/
│   │   └── index.html                      # Catégorie : Création de sites web
│   │       └── [article-slug].html         # Articles à venir (ex: wordpress-vs-sur-mesure.html)
│   ├── seo/
│   │   └── index.html                      # Catégorie : SEO & Référencement naturel
│   │       └── [article-slug].html         # Articles à venir (ex: seo-local-montreal-guide.html)
│   ├── marketing-digital/
│   │   └── index.html                      # Catégorie : Marketing digital
│   │       └── [article-slug].html         # Articles à venir
│   └── ia-automatisation/
│       └── index.html                      # Catégorie : IA & Automatisation (différenciateur fort)
│           └── [article-slug].html         # Articles à venir
│
│ ── Pages SEO locales FR (service + ville)
├── local/
│   ├── creation-site-web-montreal.html     # Création de site web à Montréal
│   ├── seo-montreal.html                   # SEO à Montréal
│   └── marketing-digital-montreal.html     # Marketing digital à Montréal
│   # À développer : /local/seo-quebec.html, /local/creation-site-laval.html, etc.
│
│ ── Pages zones géographiques FR
├── zones-desservies/
│   ├── index.html                          # Hub zones desservies
│   ├── montreal.html                       # Zone Montréal
│   ├── quebec.html                         # Zone Québec
│   └── canada.html                         # Zone Canada
│
│ ── Version anglaise EN (miroir complet)
├── en/
│   ├── index.html                          # Accueil EN
│   ├── services.html                       # Services EN
│   ├── creation-site.html                  # Website Design EN
│   ├── seo.html                            # SEO EN
│   ├── marketing-digital.html              # Digital Marketing EN
│   ├── secteurs.html                       # Industries EN
│   ├── ressources.html                     # Resources EN
│   ├── a-propos.html                       # About EN
│   ├── contact.html                        # Contact EN
│   ├── mentions-legales.html               # Legal Notice EN
│   ├── politique-confidentialite.html      # Privacy Policy EN
│   ├── politique-cookies.html              # Cookie Policy EN
│   │
│   ├── blog/                               # Blog EN (miroir du blog FR)
│   │   ├── index.html                      # Hub blog EN + barre de recherche
│   │   ├── website-design/
│   │   │   └── index.html                  # Category: Website Design
│   │   │       └── [article-slug].html     # Articles à venir
│   │   ├── seo/
│   │   │   └── index.html                  # Category: SEO & Search Engine Optimization
│   │   │       └── [article-slug].html
│   │   ├── digital-marketing/
│   │   │   └── index.html                  # Category: Digital Marketing
│   │   │       └── [article-slug].html
│   │   └── ai-automation/
│   │       └── index.html                  # Category: AI & Automation
│   │           └── [article-slug].html
│   │
│   ├── local/                              # Pages SEO locales EN
│   │   ├── creation-site-web-montreal.html
│   │   ├── seo-montreal.html
│   │   └── marketing-digital-montreal.html
│   │
│   └── zones-desservies/                   # Zones EN
│       ├── index.html
│       ├── montreal.html
│       ├── quebec.html
│       └── canada.html
│
│ ── Partials HTML (composants réutilisables)
├── partials/
│   ├── header.html                         # Structure header FR (référence)
│   └── footer.html                         # Structure footer FR (référence)
├── en/partials/
│   ├── header.html                         # Structure header EN (référence)
│   └── footer.html                         # Structure footer EN (référence)
│
│ ── Ressources statiques
├── assets/
│   ├── css/
│   │   └── styles.css                      # Styles globaux (dark/light mode, responsive, blog)
│   ├── js/
│   │   └── main.js                         # Script global : dark mode, langue switcher FR/EN,
│   │                                       #   menu hamburger mobile, cookie consent,
│   │                                       #   dot animation hero, top bar rotation
│   ├── img/
│   │   ├── logo/
│   │   │   ├── logo-nextiweb-agence-web-montreal.png  # Logo principal
│   │   │   ├── logo-nextiweb-dark.png
│   │   │   ├── logo-nextiweb-light.png
│   │   │   ├── logo-nextiweb-transparent.png
│   │   │   └── og-image-nextiweb.png       # Image Open Graph 1200×630 (réseaux sociaux)
│   │   └── hero/
│   │       └── hero-nextiweb.webp          # Image hero page d'accueil
│   └── icons/
│       ├── favicon.ico
│       ├── favicon-16.png
│       ├── favicon-32.png
│       └── favicon-180.png                 # Apple touch icon
│
│ ── SEO technique
├── sitemap.xml                             # Sitemap bilingue avec hreflang xhtml (FR+EN)
├── robots.txt                              # Directives robots → pointe vers sitemap
│
│ ── Scripts utilitaires
└── build-blog.js                           # Générateur Node.js des pages blog (à relancer
                                            #   pour créer de nouvelles catégories)
```

---

## Stratégie SEO — Architecture pilier/enfants/local

### Pages Services (Pilier → Enfants)

```
/services.html                ← Page pilier (vue d'ensemble)
  ├── /creation-site.html     ← Page enfant (profonde, unique)
  ├── /seo.html               ← Page enfant (profonde, unique)
  └── /marketing-digital.html ← Page enfant (profonde, unique)
```

Chaque page enfant vise une requête cible précise, renvoie vers le pilier et les pages sœurs (maillage interne).

### Pages locales (service + ville)

```
/local/creation-site-web-montreal.html
/local/seo-montreal.html
/local/marketing-digital-montreal.html
```

À développer : `/local/seo-quebec.html`, `/local/creation-site-laval.html`, etc.

### Blog (SEO long terme — autorité thématique)

```
/blog/                        ← Hub blog avec barre de recherche
  ├── /blog/creation-site/    ← Catégorie : sites web, UX, landing pages
  ├── /blog/seo/              ← Catégorie : SEO local, technique, contenu
  ├── /blog/marketing-digital/← Catégorie : Google Ads, réseaux sociaux, email
  └── /blog/ia-automatisation/← Catégorie : IA, ChatGPT, workflows (différenciateur)
```

**Chaque article** doit :
- Viser une requête longue traîne précise
- Avoir un `<title>` unique, une `<meta description>` unique
- Contenir un lien vers la page de service correspondante (maillage interne)
- Être ajouté au `sitemap.xml` après publication

### Priorités de publication suggérées

| Priorité | Catégorie | Exemple d'article |
|---|---|---|
| 1 | SEO | "SEO local Montréal : guide complet pour les PME" |
| 2 | Création site | "Combien coûte un site web à Montréal en 2026 ?" |
| 3 | IA & Automatisation | "ChatGPT pour les PME : 5 cas d'usage concrets" |
| 4 | Marketing digital | "Google Ads vs SEO : que choisir pour une PME ?" |

---

## Fonctionnalités techniques

| Fonctionnalité | Détail |
|---|---|
| **Dark / Light mode** | Basculement via JS + localStorage, icône ☀/☾ |
| **Bilingue FR/EN** | `/` = FR, `/en/` = EN — switcher dans le header |
| **Menu hamburger** | Drawer slide-in mobile (< 768px), overlay, fermeture Échap |
| **Cookie consent** | Banner RGPD/Loi 25 avec préférences granulaires |
| **Hero WOW** | Layout split 60/40, cartes glassmorphism, point lumineux animé |
| **Barre de recherche** | Présente sur les pages blog (FR + EN) |
| **Schema.org** | LocalBusiness + FAQPage sur les homepages FR et EN |
| **hreflang** | Toutes les pages avec balises alternate FR ↔ EN |
| **Sitemap bilingue** | `xhtml:link` hreflang dans chaque `<url>` |
| **NAP complet** | Montréal, QC, CA + 514-791-0591 + email dans tous les footers |
| **Open Graph** | Toutes les pages avec `og-image-nextiweb.png` (1200×630) |
| **Core Web Vitals** | Logo `width`/`height` + `loading="eager"` (CLS = 0) |
| **Responsive** | 3 breakpoints : 860px, 768px, 480px |

---

## NAP (Name / Address / Phone)

| Champ | Valeur |
|---|---|
| Nom | NEXTIWEB |
| Ville | Montréal, Québec, Canada |
| Téléphone | 514-791-0591 |
| Email | contact@nextiweb.ca |
| Site | https://nextiweb.ca |

> Le NAP est cohérent sur toutes les 48 pages (footer HTML + Schema.org JSON-LD).

---

## Ajouter un article de blog

1. Créer le fichier dans le bon dossier :
   - FR : `blog/seo/mon-article.html`
   - EN : `en/blog/seo/my-article.html`
2. Copier la structure d'une page catégorie existante
3. Adapter : `<title>`, `<meta description>`, `canonical`, `hreflang`, `og:*`
4. Ajouter le Schema.org `Article` ou `BlogPosting`
5. Ajouter l'URL dans `sitemap.xml`
6. Soumettre le sitemap dans Google Search Console

---

## Google Search Console

**Action requise :** Soumettre le sitemap à l'adresse :
```
https://nextiweb.ca/sitemap.xml
```

---

## Développement local

Ouvrir directement les fichiers HTML dans le navigateur, ou utiliser un serveur local :

```bash
# Avec Node.js
npx serve .

# Avec Python
python -m http.server 8080
```

---

*Site développé avec Claude Code — Architecture SEO, Design & Développement.*
