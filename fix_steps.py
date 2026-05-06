import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

c = read("secteurs.html")

old_steps = '''                <ol class="steps">
                    <li class="steps__item">
                        <h3 class="steps__title">Analyse du marché et du positionnement</h3>
                        <p>Nous identifions vos services, vos cibles, vos concurrents et vos points de différenciation.</p>
                    </li>
                    <li class="steps__item">
                        <h3 class="steps__title">Structure des pages et messages clés</h3>
                        <p>Nous définissons l'arborescence, les priorités de contenu et les appels à l'action qui soutiennent vos objectifs.</p>
                    </li>
                    <li class="steps__item">
                        <h3 class="steps__title">Conception et optimisation</h3>
                        <p>Nous produisons une interface rapide, lisible et alignée avec votre niveau de gamme et votre audience.</p>
                    </li>
                    <li class="steps__item">
                        <h3 class="steps__title">Déploiement SEO local et conversion</h3>
                        <p>Nous renforçons la visibilité locale et la capacité du site à générer des demandes concrètes.</p>
                    </li>
                </ol>'''

new_steps = '''                <ol class="steps--visual">
                    <li class="steps__item">
                        <div class="steps__number">1</div>
                        <div class="steps__arrow">&#8594;</div>
                        <h3 class="steps__title">Analyse du marché et du positionnement</h3>
                        <p class="steps__text">Nous identifions vos services, vos cibles, vos concurrents et vos points de différenciation.</p>
                    </li>
                    <li class="steps__item">
                        <div class="steps__number">2</div>
                        <div class="steps__arrow">&#8594;</div>
                        <h3 class="steps__title">Structure des pages et messages clés</h3>
                        <p class="steps__text">Nous définissons l’arborescence, les priorités de contenu et les appels à l’action qui soutiennent vos objectifs.</p>
                    </li>
                    <li class="steps__item">
                        <div class="steps__number">3</div>
                        <div class="steps__arrow">&#8594;</div>
                        <h3 class="steps__title">Conception et optimisation</h3>
                        <p class="steps__text">Nous produisons une interface rapide, lisible et alignée avec votre niveau de gamme et votre audience.</p>
                    </li>
                    <li class="steps__item">
                        <div class="steps__number">4</div>
                        <h3 class="steps__title">Déploiement SEO local et conversion</h3>
                        <p class="steps__text">Nous renforçons la visibilité locale et la capacité du site à générer des demandes concrètes.</p>
                    </li>
                </ol>'''

if old_steps in c:
    c = c.replace(old_steps, new_steps, 1)
    write("secteurs.html", c)
    print("steps--visual : OK")
else:
    print("SKIP: pattern not found")
    # Debug: show what's around line 213
    lines = c.split('\n')
    for i, l in enumerate(lines[210:220], start=211):
        print(f"{i}: {repr(l)}")
