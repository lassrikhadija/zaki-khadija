import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

def amplify(col1_items, col2_items):
    li1 = "\n".join(f"              <li>{i}</li>" for i in col1_items)
    li2 = "\n".join(f"              <li>{i}</li>" for i in col2_items)
    return (
        "\n    <!-- ============================\n"
        "         A — AMPLIFIER\n"
        "         ============================ -->\n"
        '    <section class="section">\n'
        '      <div class="container">\n'
        '        <div class="split">\n'
        '          <div class="split__column">\n'
        '            <h2 class="split__title">Ce que vous perdez sans le savoir</h2>\n'
        '            <ul class="split__list">\n'
        + li1 + "\n"
        '            </ul>\n'
        '          </div>\n'
        '          <div class="split__column">\n'
        '            <h2 class="split__title">Ce que ça coûte concrètement</h2>\n'
        '            <ul class="split__list">\n'
        + li2 + "\n"
        '            </ul>\n'
        '          </div>\n'
        '        </div>\n'
        '      </div>\n'
        '    </section>\n\n'
    )

def story(quote):
    return (
        "    <!-- ============================\n"
        "         S — HISTOIRE\n"
        "         ============================ -->\n"
        '    <section class="section section--dark">\n'
        '      <div class="container section__header section__header--center" style="max-width:680px">\n'
        f'        <p style="font-size:1.05rem;color:var(--color-text-muted);line-height:1.8;font-style:italic;margin-bottom:1.25rem">{quote}</p>\n'
        '        <p style="color:var(--color-primary);font-weight:700;font-size:.95rem">&mdash;&nbsp;Khadija AitLassri, fondatrice NEXTIWEB</p>\n'
        '        <p style="color:var(--color-text-muted);font-size:.875rem;margin-top:.5rem">Informaticienne et ancienne entrepreneur &mdash; <a href="/a-propos.html" style="color:var(--color-primary)">lire mon histoire&nbsp;&rarr;</a></p>\n'
        '      </div>\n'
        '    </section>\n\n'
    )

pages = {
    "creation-site.html": {
        "t_id": "pourquoi-site-web-montreal",
        "o1_id": "types-sites-web",
        "o2_id": "notre-processus-creation-site",
        "t2_id": "standards-techniques-site",
        "amplify": amplify(
            [
                "Vos prospects jugent votre crédibilité en moins de 3 secondes",
                "Un site lent ou mal structuré fait fuir plus de la moitié des visiteurs avant qu'ils lisent une ligne",
                "Vous expliquez vous-même ce que votre site devrait convaincre à votre place",
                "Sans site professionnel, chaque nouveau client dépend du bouche-à-oreille &mdash; et s'arrête là",
            ],
            [
                "1 prospect perdu par semaine = des milliers de dollars par an",
                "Un site sans appel à l'action clair = chaque visite investie à perte",
                "Vos concurrents absorbent les clients qui auraient pu vous appeler",
                "Chaque jour sans refonte, l'écart avec votre concurrent se creuse",
            ]
        ),
        "story": story("&laquo;&nbsp;J'ai créé mon premier site moi-même. Code propre, structure solide. Et j'ai attendu les clients. Zéro contact pendant des mois. Ce n'était pas un problème de code &mdash; c'était un problème de stratégie. C'est ce que NEXTIWEB corrige.&nbsp;&raquo;"),
    },
    "seo.html": {
        "t_id": "pourquoi-seo-montreal",
        "o1_id": "piliers-seo",
        "o2_id": "notre-approche-seo",
        "t2_id": "resultats-seo",
        "amplify": amplify(
            [
                "75&nbsp;% des gens ne passent jamais la page 1 &mdash; si vous n'y êtes pas, vous n'existez pas pour eux",
                "Votre concurrent capte chaque clic que vous auriez pu recevoir",
                "Vous dépensez en publicité ce que le SEO ferait gratuitement sur le long terme",
                "Chaque semaine sans SEO = croissance dépendante du bouche-à-oreille et du hasard",
            ],
            [
                "Des mois de travail mis en ligne... que personne ne trouve sur Google",
                "Un budget publicitaire récurrent pour compenser une invisibilité évitable",
                "Vos prospects qualifiés atterrissent chez un concurrent mieux positionné",
                "Aucune donnée sur d'où viennent vos clients &mdash; impossible d'investir au bon endroit",
            ]
        ),
        "story": story("&laquo;&nbsp;Quand j'ai lancé mon premier site, il était techniquement irréprochable. Mais invisible sur Google. J'ai compris que le SEO ne s'improvise pas &mdash; il se construit avec les bons mots-clés, la bonne structure et de la régularité. C'est la méthode que j'applique pour chaque client NEXTIWEB.&nbsp;&raquo;"),
    },
    "marketing-digital.html": {
        "t_id": "digital-marketing-components",
        "o1_id": "digital-strategy-b2b",
        "o2_id": "notre-processus-marketing",
        "t2_id": "marketing-metrics",
        "amplify": amplify(
            [
                "Votre site génère du trafic qui ne convertit pas &mdash; chaque visite est une occasion manquée",
                "Vous ne savez pas d'où viennent vos clients, impossible d'investir au bon endroit",
                "Un prospect non rellancé dans les 48&nbsp;h a 80&nbsp;% moins de chances de convertir",
                "Votre acquisition dépend du bouche-à-oreille &mdash; croissance imprévisible, impossible à scaler",
            ],
            [
                "Budget publicitaire gaspillé sur une cible floue et un site qui ne convertit pas",
                "Des leads tièdes qui reviennent plus tard... chez un concurrent qui les a rellancés",
                "Aucune visibilité sur votre ROI marketing réel &mdash; décisions prises à l'aveugle",
                "Croissance au hasard pendant que vos concurrents construisent un système qui tourne seul",
            ]
        ),
        "story": story("&laquo;&nbsp;J'ai dépensé en publicité avant d'avoir une vraie stratégie. Budget épuisé, résultats nuls. La vraie croissance digitale ne vient pas d'une seule action &mdash; elle vient d'un système coordonné où chaque levier renforce les autres. C'est ce que NEXTIWEB construit avec vous.&nbsp;&raquo;"),
    },
}

for fname, cfg in pages.items():
    c = read(fname)

    # 1 — Commenter P (premier section--dark dans main)
    p_anchor = '    <section class="section section--dark">'
    idx = c.find(p_anchor, c.find('<main>'))
    if idx >= 0:
        comment_p = ('    <!-- ============================\n'
                     '         P — PROBLÈME\n'
                     '         ============================ -->\n')
        c = c[:idx] + comment_p + c[idx:]

    # 2 — Inser A+S avant le premier section--alt-bg (apres le P)
    alt_anchor = '    <section class="section section--alt-bg">'
    idx = c.find(alt_anchor, c.find('<main>'))
    if idx >= 0:
        comment_t = ('    <!-- ============================\n'
                     '         T — TRANSFORMATION\n'
                     '         ============================ -->\n')
        c = c[:idx] + cfg["amplify"] + cfg["story"] + comment_t + c[idx:]

    # 3 — Commenter O1, O2, T2 en trouvant leur section parente
    for label, h2_id in [
        ("O — OFFRE",                       cfg["o1_id"]),
        ("O — OFFRE (processus)",            cfg["o2_id"]),
        ("T — TRANSFORMATION (résultats)", cfg["t2_id"]),
    ]:
        h2_marker = f'id="{h2_id}"'
        pos_h2 = c.find(h2_marker)
        if pos_h2 >= 0:
            pos_sec = c.rfind('\n    <section class', 0, pos_h2)
            if pos_sec >= 0:
                comment = (f'\n    <!-- ============================\n'
                           f'         {label}\n'
                           f'         ============================ -->')
                c = c[:pos_sec] + comment + c[pos_sec:]

    # 4 — Commenter R
    r_anchor = '    <section class="section section--cta">'
    comment_r = ('    <!-- ============================\n'
                 '         R — RÉPONSE (CTA)\n'
                 '         ============================ -->\n')
    c = c.replace(r_anchor, comment_r + r_anchor, 1)

    write(fname, c)
    print(f"PASTOR applique : {fname}")

print("Termine.")
