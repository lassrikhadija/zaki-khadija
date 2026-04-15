const fs = require('fs');
const path = require('path');

const BASE = __dirname;

// ─── FAQ data: keyed by relative path ─────────────────────────────────────────
// Each page gets questions tightly aligned to its topic + conversion goal
const FAQ_DATA = {

  // ── Services overview ────────────────────────────────────────────────────────
  'services.html': [
    {
      q: "Quels services proposez-vous à Montréal ?",
      a: "NEXTIWEB offre trois services complémentaires : la création de sites web professionnels et convertissants, le référencement naturel (SEO) pour apparaître sur Google, et le marketing digital pour attirer et convertir vos clients cibles à Montréal et au Québec."
    },
    {
      q: "Puis-je combiner création de site, SEO et marketing digital ?",
      a: "Oui, c'est même notre approche recommandée. Un site web bien conçu sans trafic ne génère rien. Le SEO amène des visiteurs qualifiés, et le marketing digital amplifie les résultats. Nous proposons des forfaits intégrés pour les PME qui veulent une stratégie complète."
    },
    {
      q: "Par où commencer : site web, SEO ou marketing digital ?",
      a: "Tout dépend de votre situation. Si vous n'avez pas de site ou un site obsolète, on commence par la création. Si votre site existe mais est invisible sur Google, on attaque le SEO. Si vous avez déjà du trafic mais peu de conversions, on travaille la stratégie marketing. L'audit gratuit permet de définir la bonne priorité."
    },
    {
      q: "Travaillez-vous avec des PME ou aussi de grandes entreprises ?",
      a: "Nous nous spécialisons dans les PME, entreprises de services, indépendants et organisations B2B au Québec et au Canada. Notre approche 1-on-1 garantit un suivi personnalisé que les grandes agences ne peuvent pas offrir."
    },
    {
      q: "Comment se passe le démarrage d'un projet avec NEXTIWEB ?",
      a: "Tout commence par un audit gratuit de 30 minutes. On analyse votre site actuel, votre visibilité Google et vos objectifs. Ensuite, on vous présente une stratégie claire avec un plan d'action, des délais et un budget transparent. Aucun engagement requis pour l'audit."
    }
  ],

  'en/services.html': [
    {
      q: "What services does NEXTIWEB offer in Montreal?",
      a: "NEXTIWEB offers three complementary services: professional website design built to convert, SEO (search engine optimization) to rank on Google, and digital marketing to attract and convert your ideal clients in Montreal and across Quebec."
    },
    {
      q: "Can I combine website design, SEO and digital marketing?",
      a: "Yes — and it's our recommended approach. A well-designed website without traffic generates nothing. SEO brings qualified visitors, and digital marketing amplifies results. We offer integrated packages for SMEs who want a complete strategy."
    },
    {
      q: "Where do I start: website, SEO or digital marketing?",
      a: "It depends on your situation. No website or an outdated one? Start with design. Site exists but invisible on Google? Start with SEO. Good traffic but few conversions? Focus on marketing strategy. Our free audit helps identify the right priority."
    },
    {
      q: "Do you work with SMEs or larger companies too?",
      a: "We specialize in SMEs, service businesses, freelancers and B2B organizations in Quebec and Canada. Our 1-on-1 approach ensures personalized support that large agencies simply can't offer."
    },
    {
      q: "How does a project with NEXTIWEB get started?",
      a: "Everything starts with a free 30-minute audit. We analyze your current site, Google visibility and business goals, then present a clear strategy with an action plan, timelines and transparent pricing. No commitment required for the audit."
    }
  ],

  // ── Local — Création de site web Montréal ────────────────────────────────────
  'local/creation-site-web-montreal.html': [
    {
      q: "Combien coûte la création d'un site web à Montréal en 2025 ?",
      a: "À Montréal, un site vitrine professionnel coûte généralement entre 1 500 $ et 5 000 $. Un site e-commerce ou avec fonctionnalités avancées se situe entre 3 000 $ et 10 000 $. Chez NEXTIWEB, les projets PME démarrent à 1 800 $ avec SEO de base inclus."
    },
    {
      q: "Quelle agence web choisir à Montréal pour une PME ?",
      a: "Pour une PME montréalaise, privilégiez une agence spécialisée PME qui offre un suivi personnalisé, intègre le SEO dès la conception et livre un site rapide adapté au marché québécois. NEXTIWEB se distingue par son approche 1-on-1 et son expertise locale à Montréal."
    },
    {
      q: "Un site web conçu localement aide-t-il mon référencement à Montréal ?",
      a: "Oui. Un site conçu avec les mots-clés locaux montréalais, une fiche Google Business optimisée, des pages de localisation et une structure technique solide améliore considérablement votre visibilité dans les recherches locales comme « plombier Montréal » ou « comptable PME Montréal »."
    },
    {
      q: "Combien de temps faut-il pour créer un site web à Montréal ?",
      a: "En moyenne, 3 à 6 semaines pour un site vitrine professionnel : 1 semaine pour le design, 2 à 3 semaines pour le développement, 1 semaine de tests et révisions. Les délais varient selon la complexité du projet et la rapidité de vos retours."
    },
    {
      q: "Puis-je garder mon nom de domaine si je refais mon site ?",
      a: "Absolument. Votre nom de domaine actuel est transférable et réutilisable sur votre nouveau site. Nous gérons toutes les redirections pour préserver votre référencement SEO existant et éviter toute perte de trafic lors de la migration."
    }
  ],

  'en/local/creation-site-web-montreal.html': [
    {
      q: "How much does a website cost in Montreal in 2025?",
      a: "In Montreal, a professional showcase website typically costs between $1,500 and $5,000. E-commerce or feature-rich sites range from $3,000 to $10,000. At NEXTIWEB, SME projects start at $1,800 with basic SEO included."
    },
    {
      q: "Which web agency should I choose in Montreal for my SME?",
      a: "For a Montreal SME, look for an agency specialized in small businesses that offers personalized support, integrates SEO from day one and delivers a fast, Quebec-market-ready website. NEXTIWEB stands out for its 1-on-1 approach and local Montreal expertise."
    },
    {
      q: "Does a locally-designed website help my Montreal SEO ranking?",
      a: "Yes. A website built with local Montreal keywords, an optimized Google Business Profile, location pages and solid technical structure significantly improves your visibility in local searches like 'plumber Montreal' or 'accountant SME Montreal'."
    },
    {
      q: "How long does it take to build a website in Montreal?",
      a: "On average, 3 to 6 weeks for a professional showcase website: 1 week for design, 2 to 3 weeks for development, 1 week for testing and revisions. Timelines vary based on project complexity and how quickly you provide feedback."
    },
    {
      q: "Can I keep my domain name when rebuilding my website?",
      a: "Absolutely. Your current domain is fully transferable and reusable on your new site. We handle all redirects to preserve your existing SEO rankings and avoid any traffic loss during the migration."
    }
  ],

  // ── Local — SEO Montréal ─────────────────────────────────────────────────────
  'local/seo-montreal.html': [
    {
      q: "Pourquoi faire appel à une agence SEO à Montréal ?",
      a: "Une agence SEO montréalaise connaît les spécificités du marché local : mots-clés bilingues (FR/EN), comportement des chercheurs québécois, concurrence locale dans votre secteur. NEXTIWEB combine expertise technique SEO et connaissance du marché de Montréal pour des résultats concrets."
    },
    {
      q: "Comment le SEO local aide-t-il mon entreprise à Montréal ?",
      a: "Le SEO local positionne votre entreprise sur les recherches géolocalisées comme « avocat Montréal » ou « restaurant Plateau-Mont-Royal ». Il inclut l'optimisation de votre fiche Google Business, la cohérence de vos citations NAP (nom, adresse, téléphone) et des pages de localisation dédiées."
    },
    {
      q: "Combien coûte un service SEO à Montréal ?",
      a: "Un audit SEO initial coûte entre 300 $ et 600 $. Un mandat mensuel de référencement naturel à Montréal se situe généralement entre 800 $ et 3 000 $ selon la compétitivité du secteur et l'ampleur des travaux. NEXTIWEB propose des forfaits adaptés aux budgets PME."
    },
    {
      q: "En combien de temps mon site apparaît-il en première page Google à Montréal ?",
      a: "Les premiers résultats SEO apparaissent généralement en 3 à 6 mois pour des mots-clés locaux moins compétitifs. Pour des requêtes très concurrentielles à Montréal, prévoyez 6 à 12 mois. Le SEO est un investissement à long terme qui génère un trafic qualifié et durable."
    },
    {
      q: "Quelle est la différence entre SEO local et SEO classique ?",
      a: "Le SEO classique cible des mots-clés généraux (ex. « avocat fiscal »). Le SEO local ajoute une dimension géographique (ex. « avocat fiscal Montréal Plateau ») et intègre l'optimisation Google Maps, les avis clients et les citations locales. Pour une PME montréalaise, le SEO local donne des résultats beaucoup plus rapides."
    }
  ],

  'en/local/seo-montreal.html': [
    {
      q: "Why hire an SEO agency in Montreal?",
      a: "A Montreal SEO agency understands the local market: bilingual keywords (FR/EN), Quebec user behaviour and local competition in your industry. NEXTIWEB combines technical SEO expertise with deep knowledge of the Montreal market for measurable results."
    },
    {
      q: "How does local SEO help my Montreal business?",
      a: "Local SEO positions your business for geo-targeted searches like 'lawyer Montreal' or 'restaurant Plateau-Mont-Royal'. It includes optimizing your Google Business Profile, ensuring consistent NAP citations (name, address, phone) and creating dedicated location pages."
    },
    {
      q: "How much does SEO cost in Montreal?",
      a: "An initial SEO audit costs between $300 and $600. A monthly SEO retainer in Montreal typically ranges from $800 to $3,000 depending on industry competition and scope of work. NEXTIWEB offers packages adapted to SME budgets."
    },
    {
      q: "How long before my site ranks on page 1 of Google in Montreal?",
      a: "Initial SEO results typically appear in 3 to 6 months for less competitive local keywords. For highly competitive Montreal queries, expect 6 to 12 months. SEO is a long-term investment that generates sustainable qualified traffic."
    },
    {
      q: "What is the difference between local SEO and regular SEO?",
      a: "Regular SEO targets general keywords (e.g. 'tax lawyer'). Local SEO adds a geographic dimension (e.g. 'tax lawyer Montreal Plateau') and includes Google Maps optimization, customer reviews and local citations. For a Montreal SME, local SEO delivers much faster results."
    }
  ],

  // ── Local — Marketing digital Montréal ──────────────────────────────────────
  'local/marketing-digital-montreal.html': [
    {
      q: "Qu'est-ce que le marketing digital pour une PME à Montréal ?",
      a: "Le marketing digital regroupe toutes les actions en ligne pour attirer et convertir des clients : SEO, Google Ads, réseaux sociaux, email marketing, marketing de contenu et automatisation. Pour une PME montréalaise, il permet de rivaliser avec les grandes entreprises à moindre coût."
    },
    {
      q: "Quel budget prévoir pour le marketing digital d'une PME à Montréal ?",
      a: "Pour une PME à Montréal, un budget de départ de 1 000 $ à 3 000 $ par mois permet d'obtenir des résultats concrets. Google Ads démarre dès 500 $/mois, le SEO entre 800 $ et 2 000 $/mois. L'important est d'allouer le budget aux canaux les plus rentables pour votre secteur."
    },
    {
      q: "Google Ads ou SEO : quoi choisir pour mon entreprise à Montréal ?",
      a: "Les deux sont complémentaires. Google Ads génère des leads immédiats mais s'arrête quand le budget s'arrête. Le SEO prend 3 à 6 mois mais génère un trafic gratuit et durable. Pour une PME montréalaise qui veut des résultats rapides ET durables, on recommande une combinaison des deux."
    },
    {
      q: "Comment mesurer le retour sur investissement du marketing digital à Montréal ?",
      a: "Les KPIs clés pour une PME montréalaise : coût par lead (CPL), taux de conversion, retour sur dépenses publicitaires (ROAS), trafic organique et nombre de demandes de devis. NEXTIWEB configure Google Analytics et GTM pour suivre chaque conversion et optimiser vos campagnes en continu."
    },
    {
      q: "NEXTIWEB offre-t-il des services de marketing digital adaptés au marché québécois ?",
      a: "Oui. Notre approche tient compte des spécificités québécoises : bilinguisme FR/EN, comportements d'achat locaux, plateformes privilégiées (Google, Facebook, LinkedIn) et réglementations (loi 25 sur la protection des données). Nous créons des campagnes qui résonnent avec votre audience montréalaise."
    }
  ],

  'en/local/marketing-digital-montreal.html': [
    {
      q: "What is digital marketing for an SME in Montreal?",
      a: "Digital marketing includes all online actions to attract and convert clients: SEO, Google Ads, social media, email marketing, content marketing and automation. For a Montreal SME, it enables competing with larger companies at a lower cost."
    },
    {
      q: "What budget do I need for digital marketing in Montreal?",
      a: "For a Montreal SME, a starting budget of $1,000 to $3,000 per month delivers concrete results. Google Ads starts at $500/month, SEO between $800 and $2,000/month. The key is allocating budget to the most profitable channels for your industry."
    },
    {
      q: "Google Ads or SEO: which should I choose for my Montreal business?",
      a: "Both are complementary. Google Ads generates immediate leads but stops when the budget does. SEO takes 3 to 6 months but generates free, sustainable traffic. For a Montreal SME wanting both quick and lasting results, a combination of both is recommended."
    },
    {
      q: "How do I measure digital marketing ROI in Montreal?",
      a: "Key KPIs for a Montreal SME: cost per lead (CPL), conversion rate, return on ad spend (ROAS), organic traffic and number of quote requests. NEXTIWEB sets up Google Analytics and GTM to track every conversion and continuously optimize your campaigns."
    },
    {
      q: "Does NEXTIWEB offer digital marketing services tailored to the Quebec market?",
      a: "Yes. Our approach accounts for Quebec specifics: FR/EN bilingualism, local buying behaviours, preferred platforms (Google, Facebook, LinkedIn) and regulations (Law 25 on data protection). We create campaigns that resonate with your Montreal audience."
    }
  ],

  // ── Zones desservies ─────────────────────────────────────────────────────────
  'zones-desservies/montreal.html': [
    {
      q: "NEXTIWEB offre-t-il ses services dans tout Montréal ?",
      a: "Oui. NEXTIWEB accompagne les PME et entreprises de services dans tous les arrondissements de Montréal : Plateau-Mont-Royal, Rosemont, Villeray, Outremont, Westmount, Saint-Laurent, Laval et la grande région métropolitaine. Nos services sont 100 % en ligne, donc sans contrainte géographique."
    },
    {
      q: "Y a-t-il un avantage à travailler avec une agence web basée à Montréal ?",
      a: "Oui. Une agence montréalaise comprend le marché local, les mots-clés bilingues FR/EN, la concurrence dans votre secteur à Montréal et les comportements des consommateurs québécois. Elle peut aussi optimiser votre présence pour les recherches locales qui convertissent : « plombier Montréal » ou « restaurant NDG »."
    },
    {
      q: "Proposez-vous des rencontres en personne à Montréal ?",
      a: "Nos projets sont gérés entièrement en ligne (visioconférence, email, partage de documents). Cela nous permet d'être plus réactifs et de travailler avec des clients partout au Québec. Pour les clients montréalais qui préfèrent une rencontre en personne, c'est possible sur demande."
    },
    {
      q: "NEXTIWEB travaille-t-il avec des entreprises hors Montréal ?",
      a: "Absolument. Bien que basés à Montréal, nous accompagnons des entreprises partout au Québec (Québec, Laval, Longueuil, Sherbrooke, Gatineau) et au Canada. La distance n'est pas un obstacle pour la création de sites web, le SEO ou le marketing digital."
    }
  ],

  'en/zones-desservies/montreal.html': [
    {
      q: "Does NEXTIWEB offer services throughout Montreal?",
      a: "Yes. NEXTIWEB supports SMEs and service businesses in all Montreal boroughs: Plateau-Mont-Royal, Rosemont, Villeray, Outremont, Westmount, Saint-Laurent, Laval and the greater metropolitan area. Our services are 100% online, with no geographic constraints."
    },
    {
      q: "Is there an advantage to working with a Montreal-based web agency?",
      a: "Yes. A Montreal agency understands the local market, bilingual FR/EN keywords, competition in your sector in Montreal and Quebec consumer behaviour. It can also optimize your presence for local searches that convert: 'plumber Montreal' or 'restaurant NDG'."
    },
    {
      q: "Do you offer in-person meetings in Montreal?",
      a: "Our projects are managed entirely online (video calls, email, document sharing). This allows us to be more responsive and work with clients across Quebec. For Montreal clients who prefer an in-person meeting, it can be arranged upon request."
    },
    {
      q: "Does NEXTIWEB work with businesses outside Montreal?",
      a: "Absolutely. Although based in Montreal, we support businesses across Quebec (Quebec City, Laval, Longueuil, Sherbrooke, Gatineau) and Canada. Distance is no obstacle for website design, SEO or digital marketing."
    }
  ],

  'zones-desservies/quebec.html': [
    {
      q: "NEXTIWEB offre-t-il ses services dans la ville de Québec ?",
      a: "Oui. NEXTIWEB accompagne les PME et entreprises de services dans la région de Québec : Vieux-Québec, Sainte-Foy, Lévis, Beauport et toute la Capitale-Nationale. Nos services en ligne (création de site, SEO, marketing digital) sont accessibles sans déplacement."
    },
    {
      q: "Le SEO local fonctionne-t-il de la même façon à Québec qu'à Montréal ?",
      a: "Les principes sont identiques, mais les mots-clés, la concurrence et les comportements locaux diffèrent. À Québec, le marché est souvent moins compétitif qu'à Montréal, ce qui permet d'obtenir des résultats SEO plus rapidement pour des mots-clés comme « avocat Québec » ou « restaurant Vieux-Québec »."
    },
    {
      q: "Pourquoi choisir NEXTIWEB pour mon entreprise à Québec ?",
      a: "NEXTIWEB comprend le marché québécois dans son ensemble, y compris les spécificités de la région de Québec. Nous créons des sites web et des stratégies SEO adaptés à votre clientèle locale, avec un suivi personnalisé et des résultats mesurables — sans les frais d'une grande agence."
    }
  ],

  'en/zones-desservies/quebec.html': [
    {
      q: "Does NEXTIWEB offer services in Quebec City?",
      a: "Yes. NEXTIWEB supports SMEs and service businesses in the Quebec City region: Old Quebec, Sainte-Foy, Lévis, Beauport and all of the Capitale-Nationale. Our online services (website design, SEO, digital marketing) are accessible without travel."
    },
    {
      q: "Does local SEO work the same way in Quebec City as in Montreal?",
      a: "The principles are identical, but keywords, competition and local behaviour differ. In Quebec City, the market is often less competitive than Montreal, which means faster SEO results for keywords like 'lawyer Quebec City' or 'restaurant Old Quebec'."
    },
    {
      q: "Why choose NEXTIWEB for my Quebec City business?",
      a: "NEXTIWEB understands the Quebec market as a whole, including the specifics of the Quebec City region. We create websites and SEO strategies tailored to your local clientele, with personalized support and measurable results — without the fees of a large agency."
    }
  ],

  'zones-desservies/canada.html': [
    {
      q: "NEXTIWEB offre-t-il ses services à l'échelle nationale au Canada ?",
      a: "Oui. NEXTIWEB accompagne des PME et entreprises de services partout au Canada : Ontario (Toronto, Ottawa), Colombie-Britannique (Vancouver), Alberta (Calgary, Edmonton) et autres provinces. Nos services numériques sont accessibles sans contrainte géographique."
    },
    {
      q: "Pouvez-vous créer un site web bilingue français-anglais pour le marché canadien ?",
      a: "Absolument. La plupart de nos clients ont besoin d'un site bilingue FR/EN pour le marché canadien. Nous concevons des sites web avec une structure bilingue SEO-optimisée, des URLs distinctes pour chaque langue et un contenu adapté à chaque audience régionale."
    },
    {
      q: "Le SEO fonctionne-t-il différemment pour les entreprises canadiennes hors Québec ?",
      a: "Les principes SEO sont universels, mais les mots-clés, la concurrence et les comportements varient par province et ville. NEXTIWEB adapte chaque stratégie SEO au marché cible — que ce soit Toronto, Vancouver ou Ottawa — pour maximiser la visibilité locale de votre entreprise."
    }
  ],

  'en/zones-desservies/canada.html': [
    {
      q: "Does NEXTIWEB offer services nationally across Canada?",
      a: "Yes. NEXTIWEB supports SMEs and service businesses across Canada: Ontario (Toronto, Ottawa), British Columbia (Vancouver), Alberta (Calgary, Edmonton) and other provinces. Our digital services are accessible without geographic constraints."
    },
    {
      q: "Can you build a bilingual French-English website for the Canadian market?",
      a: "Absolutely. Most of our clients need a bilingual FR/EN website for the Canadian market. We design websites with an SEO-optimized bilingual structure, distinct URLs for each language and content tailored to each regional audience."
    },
    {
      q: "Does SEO work differently for Canadian businesses outside Quebec?",
      a: "SEO principles are universal, but keywords, competition and behaviour vary by province and city. NEXTIWEB tailors each SEO strategy to the target market — whether Toronto, Vancouver or Ottawa — to maximize local visibility for your business."
    }
  ],

  'zones-desservies/index.html': [
    {
      q: "Dans quelles régions NEXTIWEB offre-t-il ses services ?",
      a: "NEXTIWEB accompagne des entreprises à Montréal, Québec, Laval, Longueuil, Sherbrooke, Gatineau et partout au Canada. Nos services numériques (création web, SEO, marketing digital) sont accessibles dans toute la francophonie canadienne et au-delà."
    },
    {
      q: "Dois-je être à Montréal pour travailler avec NEXTIWEB ?",
      a: "Non. Nos projets se gèrent entièrement en ligne : appels vidéo, partage de documents, gestion de projet à distance. Nos clients sont répartis dans tout le Québec et au Canada. La localisation géographique n'a aucun impact sur la qualité du service."
    }
  ],

  'en/zones-desservies/index.html': [
    {
      q: "What regions does NEXTIWEB serve?",
      a: "NEXTIWEB supports businesses in Montreal, Quebec City, Laval, Longueuil, Sherbrooke, Gatineau and across Canada. Our digital services (web design, SEO, digital marketing) are accessible throughout French-speaking Canada and beyond."
    },
    {
      q: "Do I need to be in Montreal to work with NEXTIWEB?",
      a: "No. Our projects are managed entirely online: video calls, document sharing and remote project management. Our clients are spread across Quebec and Canada. Geographic location has no impact on service quality."
    }
  ],

  // ── À propos ─────────────────────────────────────────────────────────────────
  'a-propos.html': [
    {
      q: "Qui est derrière NEXTIWEB ?",
      a: "NEXTIWEB est fondé par Khadija AitLassri, spécialiste en création de sites web, SEO et marketing digital à Montréal. Après avoir reconstruit sa propre présence en ligne de zéro, Khadija accompagne les PME québécoises qui veulent un site qui travaille vraiment pour elles."
    },
    {
      q: "Pourquoi choisir NEXTIWEB plutôt qu'une grande agence web ?",
      a: "Chez NEXTIWEB, vous travaillez directement avec la fondatrice — pas avec un compte-gestionnaire junior. Cela garantit une compréhension profonde de votre business, une communication directe et des décisions rapides. Nous n'avons pas les frais généraux d'une grande agence, ce qui se reflète dans nos prix."
    },
    {
      q: "NEXTIWEB propose-t-il un suivi après le lancement du site ?",
      a: "Oui. Nous incluons 30 jours de suivi post-lancement dans tous nos projets. Au-delà, nous proposons des mandats de maintenance, de SEO continu et de marketing digital pour que votre site continue à générer des résultats dans la durée."
    },
    {
      q: "Comment NEXTIWEB travaille-t-il avec ses clients ?",
      a: "Notre processus est transparent et collaboratif : audit gratuit, stratégie claire, jalons définis, révisions incluses, livraison dans les délais. Vous êtes informé à chaque étape. Pas de surprises, pas de jargon, pas de frais cachés."
    }
  ],

  'en/a-propos.html': [
    {
      q: "Who is behind NEXTIWEB?",
      a: "NEXTIWEB was founded by Khadija AitLassri, a web design, SEO and digital marketing specialist based in Montreal. After rebuilding her own online presence from scratch, Khadija now supports Quebec SMEs who want a website that truly works for them."
    },
    {
      q: "Why choose NEXTIWEB over a large web agency?",
      a: "At NEXTIWEB, you work directly with the founder — not a junior account manager. This ensures deep understanding of your business, direct communication and fast decisions. We don't carry the overhead of a large agency, which is reflected in our pricing."
    },
    {
      q: "Does NEXTIWEB offer post-launch support?",
      a: "Yes. We include 30 days of post-launch monitoring in all projects. Beyond that, we offer ongoing maintenance, SEO and digital marketing retainers to ensure your site continues generating results over time."
    },
    {
      q: "How does NEXTIWEB work with its clients?",
      a: "Our process is transparent and collaborative: free audit, clear strategy, defined milestones, included revisions, on-time delivery. You're informed at every step. No surprises, no jargon, no hidden fees."
    }
  ],

  // ── Ressources ───────────────────────────────────────────────────────────────
  'ressources.html': [
    {
      q: "Les ressources de NEXTIWEB sont-elles vraiment gratuites ?",
      a: "Oui, toutes nos ressources (guides, articles, conseils) sont entièrement gratuites. Notre objectif est de vous donner les connaissances pour comprendre le web, le SEO et le marketing digital — et prendre des décisions éclairées pour votre entreprise, avec ou sans nous."
    },
    {
      q: "À qui s'adressent les guides de NEXTIWEB ?",
      a: "Nos ressources sont conçues pour les propriétaires de PME, indépendants et entrepreneurs québécois qui veulent comprendre comment fonctionne le web sans jargon technique. Que vous ayez un site ou pas, que vous connaissiez le SEO ou pas — nos guides partent de zéro."
    },
    {
      q: "Comment améliorer mon référencement Google sans faire appel à une agence ?",
      a: "Les bases du SEO que vous pouvez appliquer vous-même : optimiser vos balises title et meta description, créer du contenu qui répond aux questions de vos clients, obtenir des avis Google, remplir votre fiche Google Business et assurer la rapidité de votre site. Nos guides vous expliquent tout étape par étape."
    },
    {
      q: "Qu'est-ce que la visibilité IA et pourquoi c'est important pour mon entreprise ?",
      a: "La visibilité IA (AEO / GEO) c'est le fait d'être recommandé par des moteurs comme ChatGPT, Perplexity ou Google AI Overview quand quelqu'un pose une question liée à votre secteur. En 2026, de plus en plus de clients trouvent leurs fournisseurs via l'IA — être cité par ces moteurs génère du trafic qualifié gratuit."
    }
  ],

  'en/ressources.html': [
    {
      q: "Are NEXTIWEB's resources really free?",
      a: "Yes, all our resources (guides, articles, tips) are completely free. Our goal is to give you the knowledge to understand web, SEO and digital marketing — and make informed decisions for your business, with or without us."
    },
    {
      q: "Who are NEXTIWEB's guides designed for?",
      a: "Our resources are designed for SME owners, freelancers and Quebec entrepreneurs who want to understand how the web works without technical jargon. Whether you have a website or not, whether you know SEO or not — our guides start from scratch."
    },
    {
      q: "How can I improve my Google ranking without hiring an agency?",
      a: "SEO basics you can apply yourself: optimize your title and meta description tags, create content that answers your clients' questions, get Google reviews, complete your Google Business Profile and ensure your site loads fast. Our guides walk you through it all step by step."
    },
    {
      q: "What is AI visibility and why does it matter for my business?",
      a: "AI visibility (AEO/GEO) means being recommended by engines like ChatGPT, Perplexity or Google AI Overview when someone asks a question related to your industry. In 2026, more and more clients find their suppliers via AI — being cited by these engines generates free, qualified traffic."
    }
  ],

  // ── EN visibilite-ia (has FAQ HTML but missing JSON-LD) ─────────────────────
  'en/visibilite-ia.html': [
    {
      q: "What is the difference between SEO and AEO (Answer Engine Optimization)?",
      a: "SEO optimizes your site to rank in traditional search results (Google's blue links). AEO optimizes your content to be cited directly by AI engines like ChatGPT, Perplexity and Google AI Overview as the authoritative answer. Both are complementary and reinforce each other."
    },
    {
      q: "Do customers really find suppliers through ChatGPT?",
      a: "Yes, and the trend is accelerating. Over 30% of searches now start on AI engines, especially for professional service queries like 'best SEO agency Montreal' or 'how to create a website for my business'. Being cited by these engines generates qualified, zero-cost traffic."
    },
    {
      q: "How long does it take to see results from AI visibility optimization?",
      a: "Generally 4 to 8 weeks after content optimization — faster than traditional SEO. AI engines index and process content more dynamically than Google. The key is structuring your content to directly answer the questions your potential clients are asking."
    },
    {
      q: "Can I combine AI visibility with traditional SEO?",
      a: "Yes — and it's our recommended approach. Good SEO content naturally improves AI visibility, and AI-optimized content reinforces your SEO authority. NEXTIWEB develops integrated strategies that position you on both Google and AI engines simultaneously."
    }
  ]
};

// ─── Build JSON-LD block ───────────────────────────────────────────────────────
function buildFAQSchema(faqs) {
  const entities = faqs.map(f => ({
    "@type": "Question",
    "name": f.q,
    "acceptedAnswer": { "@type": "Answer", "text": f.a }
  }));
  return `\n  <script type="application/ld+json">\n  ${JSON.stringify({ "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities }, null, 2).replace(/\n/g, '\n  ')}\n  </script>`;
}

// ─── Main ─────────────────────────────────────────────────────────────────────
let updated = 0, skipped = 0;

for (const [rel, faqs] of Object.entries(FAQ_DATA)) {
  const fp = path.join(BASE, rel);
  if (!fs.existsSync(fp)) { console.log('MISSING:', rel); continue; }

  let content = fs.readFileSync(fp, 'utf8');

  if (content.includes('FAQPage')) { skipped++; console.log('SKIP (exists):', rel); continue; }

  const schema = buildFAQSchema(faqs);
  content = content.replace('</body>', schema + '\n</body>');

  fs.writeFileSync(fp, content, 'utf8');
  updated++;
  console.log(`OK [${faqs.length}Q]:`, rel);
}

console.log(`\nDone: ${updated} added, ${skipped} already had FAQ schema.`);
