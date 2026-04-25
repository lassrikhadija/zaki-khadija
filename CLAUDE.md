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
/en/blog/website-design/ ← Articles blog EN — website design
/en/blog/seo/            ← Articles blog EN — SEO
/assets/css/             ← styles.min.css?v=3 (cache-busting actuel : v=3)
/assets/js/              ← main.min.js
/assets/img/logo/        ← logo-nextiweb-dark.png (84x48px)
```

### Pages principales FR
- `index.html` — Accueil
- `services.html` — Services (hub)
- `creation-site.html` — Création de sites web
- `seo.html` — Référencement SEO
- `marketing-digital.html` — Marketing digital
- `secteurs.html` — Secteurs / Industries
- `ressources.html` — Ressources
- `a-propos.html` — À propos
- `contact.html` — Contact (objectif : capture lead)
- `question.html` — Page question (tunnel de conversion)
- `merci.html` — Page merci post-soumission
- `blog/` — Hub blog FR

### Pages principales EN (miroir FR)
- `en/index.html`, `en/services.html`, `en/creation-site.html`, `en/seo.html`
- `en/marketing-digital.html`, `en/secteurs.html`, `en/ressources.html`
- `en/a-propos.html`, `en/contact.html`, `en/visibilite-ia.html`
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

### CSS cache-busting
```html
<link rel="stylesheet" href="/assets/css/styles.min.css?v=3">
```
**Règle :** incrémenter la version à chaque changement de CSS global.

### WhatsApp float bar
- FR : `https://wa.me/15147910591?text=Bonjour%2C%20je%20voudrais%20plus%20d%27informations%20sur%20vos%20services.`
- EN : `https://wa.me/15147910591?text=Hello%2C%20I%20would%20like%20more%20information%20about%20your%20services.`

### hreflang (articles bilingues)
```html
<link rel="alternate" hreflang="fr" href="https://nextiweb.ca/blog/creation-site/[slug-fr].html">
<link rel="alternate" hreflang="en" href="https://nextiweb.ca/en/blog/website-design/[slug-en].html">
<link rel="alternate" hreflang="x-default" href="https://nextiweb.ca/blog/creation-site/[slug-fr].html">
```

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

---

## 5. Historique des corrections majeures

| Commit | Description |
|--------|-------------|
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
Accueil → Services/Blog → Contact → question.html → merci.html
```

### Règle des 3 clics
Toute conversion (formulaire de contact, audit gratuit) doit être atteignable en **3 clics maximum** depuis la page d'accueil.

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
- **CTA principal :** "Demander mon audit gratuit" (FR) / "Get My Free Audit" (EN)
- **Auteure des articles :** Khadija AitLassri

---

## 8. Ce qui reste à faire (backlog)

### Blog (prochains articles)
- [ ] Articles blog FR : catégories Marketing Digital et IA & Automatisation (vides)
- [ ] Articles blog EN : catégories Digital Marketing et AI & Automation (vides)
- [ ] Audit du funnel avec le framework des 3 clics (voir section 6)

### UX / Conversion
- [ ] Appliquer le tableau de cartographie page par page (objectif / CTA / page suivante)
- [ ] Tester les 3 profils visiteurs (voir framework section 6)
- [ ] Vérifier que GA4 est configuré pour tracker les conversions (formulaire contact)

### Technique
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

*Dernière mise à jour : 25 avril 2026*
