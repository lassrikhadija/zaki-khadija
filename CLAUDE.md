# NEXTIWEB — Mémoire de projet (CLAUDE.md)

> Fichier lu automatiquement par Claude à chaque session.  
> Mis à jour au fil du projet. Ne pas supprimer.

---

## 1. Contexte du projet

**Client / Propriétaire :** Khadija AitLassri  
**Email :** khadija.lassri@gmail.com  
**Agence :** NEXTIWEB — agence web spécialisée création de sites, SEO, marketing digital  
**Adresse :** Montréal, Québec, Canada | 514-791-0591 | contact@nextiweb.ca  
**Repo GitHub :** https://github.com/lassrikhadija/zaki-khadija  
**Branche principale :** `main`  
**Dossier local :** `C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija`

---

## 2. Architecture du site

### Structure des dossiers
```
/                        ← Pages FR (version principale)
/en/                     ← Pages EN (version anglophone)
/blog/creation-site/     ← Articles blog FR — création de sites
/blog/seo/               ← Articles blog FR — SEO
/blog/marketing-digital/ ← Articles blog FR — marketing (vide)
/blog/ia-automatisation/ ← Articles blog FR — IA (vide)
/en/blog/website-design/ ← Articles blog EN — website design
/en/blog/seo/            ← Articles blog EN — SEO
/en/blog/digital-marketing/ ← Articles blog EN — marketing (vide)
/en/blog/ai-automation/  ← Articles blog EN — AI (vide)
/assets/css/             ← styles.min.css?v=3 (cache-busting actuel : v=3)
/assets/js/              ← main.min.js
/assets/img/logo/        ← logo-nextiweb-dark.png (84x48px)
```

### Pages principales FR
- `index.html` — Accueil
- `services.html` — Services (hub — ses 3 CTAs vers service pages sont INTENTIONNELS)
- `creation-site.html` — Création de sites web
- `seo.html` — Référencement SEO
- `marketing-digital.html` — Marketing digital
- `secteurs.html` — Secteurs / Industries
- `ressources.html` — Ressources
- `a-propos.html` — À propos
- `contact.html` — Contact tunnel (noindex, Netlify form → /merci.html)
- `question.html` — Question rapide tunnel (noindex, Netlify form → /merci.html)
- `merci.html` — Page merci post-soumission (noindex, GA4 event generate_lead)
- `blog/` — Hub blog FR

### Pages principales EN (miroir FR)
- `en/index.html`, `en/services.html`, `en/creation-site.html`, `en/seo.html`
- `en/marketing-digital.html`, `en/secteurs.html`, `en/ressources.html`
- `en/a-propos.html`
- `en/contact.html` — Contact tunnel EN (noindex, Netlify form → /en/merci.html) ← refondé 25/04
- `en/question.html` — Question rapide tunnel EN (noindex, Netlify form → /en/merci.html) ← créé 25/04
- `en/merci.html` — Page merci EN (noindex, GA4 event generate_lead) ← créé 25/04
- `en/blog/` — Hub blog EN

### Zones desservies
- `zones-desservies/montreal.html`, `quebec.html`, `canada.html`
- `en/zones-desservies/` — mêmes pages EN

---

## 3. Standards techniques établis

### Navigation (FR)
```html
Services (submenu: Création de sites web / Référencement SEO / Marketing digital)
Secteurs | Ressources | Blog | À propos | [CTA] Demander mon audit gratuit
```

### Navigation (EN)
```html
Services (submenu: Website Design / SEO / Digital Marketing)
Industries | Resources | Blog | About | [CTA] Get My Free Audit
```

### CTA principal — labels unifiés
- **FR :** "Je veux mon audit gratuit" → `/contact.html`
- **EN :** "Get My Free Audit" → `/en/contact.html`
- **RÈGLE :** Même label sur TOUTES les pages. Ne jamais utiliser "offert", "maintenant", "Démarrer mon projet" ou tout autre variante.

### Footer standardisé (uniformisé le 6 juin 2026)
- **UN seul footer de référence** sur toutes les pages `<footer class="site-footer">` : FR = `partials/footer.html`, EN = `en/partials/footer.html`. Toute modif du footer DOIT être faite sur ces 2 fichiers de référence PUIS resynchronisée sur toutes les pages (les partials ne sont pas inclus dynamiquement — le HTML est dupliqué dans chaque page).
- **Structure (mise à jour 6 juin 2026) :** 5 colonnes (Identité + Navigation + Services + **Secteurs** + Zones desservies) + bande Nextiweb Studio + ligne copyright.
- **Slogan unique FR :** « Agence web spécialisée en création de sites web, SEO, marketing digital et visibilité IA à Montréal. »
- **Colonne Services (4 liens) :** Création de sites web · Référencement SEO · Marketing digital · Visibilité IA.
- **Colonne Secteurs (ajoutée 6 juin 2026) :** les 9 secteurs (Cliniques dentaires, Ostéopathes, Avocats, Courtiers immobiliers, Restaurants, Traiteur, Fleuriste, Construction et rénovation, Services à domicile) + « Tous les secteurs ». EN = titre « Industries », mêmes liens vers `/en/...`.
- **Ligne copyright (footer__bottom) :** UNIQUEMENT `© 2026 NEXTIWEB · NEQ 2272348204`. **Ne PAS y mettre les liens légaux** : `main.js` injecte automatiquement une ligne `.footer__legal` avec confidentialité + cookies + mentions légales + bouton « Gérer mes cookies » (Loi 25). Les ajouter dans le HTML crée un doublon.
- **Exception :** les pages tunnel `contact.html` / `question.html` / `merci.html` (FR + EN) n'ont PAS ce footer (footer minimal volontaire — ne pas y ajouter le footer complet).
- **Resynchronisation :** régénérer les pages en remplaçant le bloc `<footer class="site-footer">…</footer>` par le contenu du partial correspondant, en conservant la fin de ligne propre à chaque fichier (les articles de blog sont en LF, le reste en CRLF).

### CSS cache-busting
```html
<link rel="stylesheet" href="/assets/css/styles.min.css?v=8">
```
**Règle :** incrémenter la version à chaque changement de CSS global (version actuelle : `v=8`). Modifier **styles.min.css** (servi) ET **styles.css** (source), puis bumper la version sur toutes les pages.
**Accessibilité (6 juin 2026) :** skip-link « Aller au contenu » / « Skip to content » ajouté en 1ʳᵉ position dans `<body>` sur toutes les pages, avec ancre `id="main"` sur `<main>` (WCAG 2.4.1). CSS `.skip-link` dans le CSS global (caché hors focus). La page `audit-jdiq-2026/merci.html` a sa propre copie inline (pas de CSS global).
**Note :** `backdrop-filter` retiré du `.site-header` le 6 juin 2026 — il causait des traînées de peinture (ghosting) au scroll sur Android. Le fond du header étant opaque, aucun impact visuel.

### WhatsApp float bar
- FR : `https://wa.me/15147910591?text=Bonjour%2C%20je%20voudrais%20plus%20d%27informations%20sur%20vos%20services.`
- EN : `https://wa.me/15147910591?text=Hello%2C%20I%20would%20like%20more%20information%20about%20your%20services.`
- **ATTENTION :** Sur les pages EN, le float bar question doit pointer vers `/en/question.html` (pas `/question.html`)

### hreflang (articles bilingues)
```html
<link rel="alternate" hreflang="fr" href="https://nextiweb.ca/blog/creation-site/[slug-fr].html">
<link rel="alternate" hreflang="en" href="https://nextiweb.ca/en/blog/website-design/[slug-en].html">
<link rel="alternate" hreflang="x-default" href="https://nextiweb.ca/blog/creation-site/[slug-fr].html">
```

### Formulaires (handlers PHP — Netlify abandonné)
> Netlify a été un essai puis supprimé. Les formulaires sont désormais traités côté serveur par des handlers PHP. **Ne plus utiliser `data-netlify`.**
- FR contact : `method="POST"` → `action="/contact-handler.php"` (`id="audit-form"`)
- FR question : `method="POST"` → `action="/question-handler.php"` (`id="question-form"`)
- EN contact : `method="POST"` → `action="/en/contact-handler.php"` (`id="audit-form"`)
- EN question : `method="POST"` → `action="/en/question-handler.php"` (`id="question-form"`)
- **Anti-spam :** honeypot `name="bot-field"` (champ caché) vérifié par les handlers PHP — **ne pas supprimer**. `contact-handler.php` a un 2ᵉ honeypot `website_confirm`.
- Config mail : `mail-config.php` / `smtp-mailer.php`.
- **Note hébergement :** `_redirects` et `_headers` sont au format Netlify/Cloudflare Pages → **inactifs sur Apache/PHP**. Les vraies redirections 301/410 et en-têtes de sécurité vivent dans `.htaccess` (migration faite le 6 juin 2026 : 301 WordPress + consolidation Core Web Vitals + 410 `/feed/` + HSTS + Permissions-Policy). `_redirects`/`_headers` conservés mais désormais redondants. **CSP non encore en place** (à ajouter avec tests pour ne pas bloquer GTM/GA/polices).

### GA4 — tracking conversion
- `merci.html` et `en/merci.html` poussent chacun un event `generate_lead` via dataLayer :
```html
<script>
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({ event: 'generate_lead', form_name: 'audit-gratuit[-en]', language: 'fr|en' });
</script>
```
- **À faire dans GTM :** Trigger Custom Event `generate_lead` → Tag GA4 Event `generate_lead`
- **À faire dans GA4 :** Admin → Événements → marquer `generate_lead` comme conversion
- **GTM container :** `GTM-TS5WZHQ6`

### Schema.org (articles)
Chaque article contient 3 blocs JSON-LD : `Article` + `FAQPage` + `BreadcrumbList`

### FAQ accordion (inline JS)
```html
<script>
  document.querySelectorAll('.article-faq__btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var item = this.closest('.article-faq__item');
      var isOpen = item.classList.contains('is-open');
      document.querySelectorAll('.article-faq__item').forEach(function(el){
        el.classList.remove('is-open');
        el.querySelector('.article-faq__btn').setAttribute('aria-expanded','false');
      });
      if(!isOpen){item.classList.add('is-open');this.setAttribute('aria-expanded','true');}
    });
  });
</script>
```

### Layout article (2 colonnes)
```css
.article-layout { display:grid; grid-template-columns:1fr 280px; gap:3rem; }
@media(max-width:900px){ .article-layout{grid-template-columns:1fr} .article-sidebar{display:none} }
```

---

## 4. Articles de blog publiés

### Français (6 articles)
| Fichier | Titre | Date | Durée |
|---------|-------|------|-------|
| `blog/creation-site/comment-fonctionne-site-web.html` | Comment fonctionne un site web | 17 avr 2026 | 12 min |
| `blog/creation-site/vitrine-landing-ecommerce.html` | Vitrine, landing page ou e-commerce | 17 avr 2026 | 9 min |
| `blog/creation-site/choisir-format-site-web.html` | Choisir le bon format de site web | 22 avr 2026 | 10 min |
| `blog/creation-site/html-css-js-guide-dirigeant.html` | HTML, CSS, JS — guide dirigeant | 22 avr 2026 | 10 min |
| `blog/creation-site/ux-structure-contenu.html` | UX et structure de contenu | 22 avr 2026 | 11 min |
| `blog/seo/performance-core-web-vitals.html` | Core Web Vitals 2026 | 24 avr 2026 | 9 min |

### Anglais (6 articles — traductions FR→EN)
| Fichier | Titre | Date | Durée |
|---------|-------|------|-------|
| `en/blog/website-design/how-does-a-website-work.html` | How Does a Website Work | 17 avr 2026 | 12 min |
| `en/blog/website-design/website-types-comparison.html` | Business Website vs Landing Page vs E-commerce | 17 avr 2026 | 9 min |
| `en/blog/website-design/choose-website-format.html` | The Right Format for Your Budget | 22 avr 2026 | 10 min |
| `en/blog/website-design/html-css-js-guide-business-owner.html` | HTML, CSS and JavaScript: Guide for Business Owners | 22 avr 2026 | 10 min |
| `en/blog/website-design/ux-content-structure.html` | UX and Content Structure | 22 avr 2026 | 11 min |
| `en/blog/seo/core-web-vitals-guide.html` | Core Web Vitals 2026 | 24 avr 2026 | 9 min |

### Catégories vides (FR + EN)
- `blog/marketing-digital/` et `en/blog/digital-marketing/` — aucun article
- `blog/ia-automatisation/` et `en/blog/ai-automation/` — aucun article

---

## 5. Historique des corrections majeures

| Commit | Description |
|--------|-------------|
| `27c940b` | Blog EN — 5 pages index/catégories : double breadcrumb, question float, CTA, footer doublon |
| `26f71cd` | Blog toboggan — 12 articles FR+EN : pause CTA → page service, labels unifiés |
| `75463a5` | Refonte en/contact.html en tunnel identique au FR |
| `2b55ac1` | Création en/question.html (miroir FR) |
| `8e93264` | GA4 tracking : dataLayer generate_lead sur merci.html + en/merci.html créé + en/contact.html Netlify |
| `0ece008` | Toboggan EN — 6 pages : uniformisation CTAs + suppression liens de dispersion |
| `db58fb6` | Toboggan FR — creation-site, seo, marketing-digital, secteurs |
| `3e4c97d` | Toboggan FR — services.html |
| `76e8b72` | Toboggan FR — a-propos.html |
| `92041a1` | Toboggan FR — ressources.html + merci.html |
| `fac23ed` | 6 articles EN publiés + index mis à jour |
| `204ce1e` | CSS bump v2→v3 sur 59 pages |
| `bcf156b` | Fix débordement texte mobile articles blog |
| `aab0ba7` | Ajout Blog dans menu mobile |
| `2d169f5` | Fix contraste PageSpeed (2 problèmes) |
| `672f433` | Articles 5 et 6 FR (Core Web Vitals + UX) |
| `0b00c65` | Article 4 FR (HTML/CSS/JS guide dirigeant) |
| `921d1cd` | Suppression stats inventées, sources réelles ajoutées |
| `8db8a2a` | Uniformisation menu navigation FR + EN |
| `de5a9d8` | Tunnel de conversion : question.html + merci.html |

---

## 6. Philosophie UX du site (décisions stratégiques)

### Principe du toboggan
Chaque page a **un seul objectif** et **une seule action** clairement demandée au visiteur. Les pages s'enchaînent comme un toboggan — on ne laisse pas le visiteur hésiter sur quoi faire ensuite.

**Funnel principal :**
```
Accueil → Services/Blog → [Page service ou article] → Contact → merci
```

### Hub vs page de conversion — distinction critique
- **`services.html`** est un HUB : ses 3 CTAs vers les pages service sont INTENTIONNELS, c'est le but de la page. Ne jamais supprimer ces liens.
- **`a-propos.html`, `secteurs.html`** sont des pages de CONFIANCE : les cartes projets ne doivent PAS avoir de liens sortants vers les services — seul le CTA final convertit.

### Règle des 3 clics
Toute conversion (formulaire de contact, audit gratuit) doit être atteignable en **3 clics maximum** depuis la page d'accueil.

### Règle des CTAs blog (défini le 25 avril 2026)
Chaque article a **2 CTAs** :
1. **CTA contextuel** (milieu d'article) → page SERVICE correspondante
   - Article création-site → `/creation-site.html` "Voir nos services création web →"
   - Article SEO → `/seo.html` "Voir notre service SEO →"
   - Article marketing → `/marketing-digital.html`
   - EN : même logique vers `/en/[service].html`
2. **CTA final** (fin d'article) → `/contact.html` "Je veux mon audit gratuit →"
3. **Section bottom** → `/contact.html` "Je veux mon audit gratuit" (sans flèche)

**Funnel blog :**
```
Article → CTA contextuel → Page service → CTA service → /contact.html
       → CTA final ──────────────────────────────────→ /contact.html
```

### Framework de validation UX (défini le 25 avril 2026)
Pour valider que le toboggan fonctionne :

**Niveau 1 — Cartographie :**
Tableau à 4 colonnes par page : `Page | Objectif unique | CTA demandé | Page suivante`

**Niveau 2 — Audit 3 clics :**
Tester 3 profils visiteurs (sait ce qu'il veut / hésitant / vient du blog)

**Niveau 3 — Métriques :**
- Taux de rebond > 70% sur page clé = signal d'alarme
- Chemin de navigation GA4 = voir où les visiteurs "s'échappent"
- Taux de clic CTA < 2% = CTA mal placé
- Taux de conversion Contact < 1% = friction dans formulaire

**Test terrain :**
Donner l'URL à quelqu'un qui ne connaît pas le site et lui dire : *"Trouve comment les contacter."* Observer sans intervenir.

---

## 7. Contenu et style éditorial

- **Langue :** Français canadien (FR) + Anglais canadien (EN)
- **Prix :** Toujours en CAD, fourchettes sourcées (pas de chiffres inventés)
- **Sources citées :** NNGroup, Google Search Central, Deloitte Milliseconds Make Millions, HTTP Archive Web Almanac 2024, Unbounce, Clevr Solutions, DesignEdge Canada
- **Ton :** Direct, professionnel, sans jargon inutile
- **CTA principal FR :** "Je veux mon audit gratuit" → `/contact.html`
- **CTA principal EN :** "Get My Free Audit" → `/en/contact.html`
- **Auteure des articles :** Khadija AitLassri

---

## 8. Ce qui reste à faire (backlog)

### Blog (priorité)
- [ ] Articles blog FR : catégories **Marketing Digital** et **IA & Automatisation** (vides)
- [ ] Articles blog EN : catégories **Digital Marketing** et **AI & Automation** (vides)

### GA4 / GTM (à faire manuellement dans les interfaces)
- [ ] GTM : créer Trigger Custom Event `generate_lead` + Tag GA4 Event → publier container
- [ ] GA4 : Admin → Événements → marquer `generate_lead` comme conversion
- [ ] Vérifier les données dans GA4 après publication GTM (mode Aperçu pour tester)

### UX / Validation
- [ ] Audit 3 clics avec 3 profils visiteurs (voir framework section 6)
- [ ] Vérifier Core Web Vitals réels via Search Console (données CrUX 28 jours)
- [ ] Tester PageSpeed sur mobile pour les pages de service clés

---

## 9. Commandes utiles

```bash
# Aller dans le projet
cd "C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija"

# Voir les fichiers modifiés
git status

# Committer et pousser
git add [fichiers]
git commit -m "description"
git push origin main
```

---

*Dernière mise à jour : 25 avril 2026 — Session toboggan EN + GA4 + blog CTAs + blog EN audit*
