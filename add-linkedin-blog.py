import os, glob

BASE = r"C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija"
LINKEDIN_PERSONAL = "https://www.linkedin.com/in/khadija-ait-lassri/"

# HTML : nom auteure → lien LinkedIn
OLD_AUTHOR_HTML = '<span class="article-meta__author">Khadija AitLassri</span>'
NEW_AUTHOR_HTML = (f'<a href="{LINKEDIN_PERSONAL}" target="_blank" '
                   f'rel="noopener noreferrer" class="article-meta__author" '
                   f'style="text-decoration:none;color:inherit" '
                   f'aria-label="Profil LinkedIn de Khadija AitLassri">'
                   f'Khadija AitLassri</a>')

# Schema FR
OLD_SCHEMA_FR = ('"author": {"@type": "Person", "name": "Khadija AitLassri", '
                 '"url": "https://nextiweb.ca/a-propos.html"}')
NEW_SCHEMA_FR = (f'"author": {{"@type": "Person", "name": "Khadija AitLassri", '
                 f'"url": "https://nextiweb.ca/a-propos.html", '
                 f'"sameAs": ["{LINKEDIN_PERSONAL}"]}}')

# Schema EN
OLD_SCHEMA_EN = ('"author": {"@type": "Person", "name": "Khadija AitLassri", '
                 '"url": "https://nextiweb.ca/en/a-propos.html"}')
NEW_SCHEMA_EN = (f'"author": {{"@type": "Person", "name": "Khadija AitLassri", '
                 f'"url": "https://nextiweb.ca/en/a-propos.html", '
                 f'"sameAs": ["{LINKEDIN_PERSONAL}"]}}')

all_articles = [f for f in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True)
                if "blog" in f and "index" not in f and ".git" not in f]

updated_html = updated_schema = already = 0

for path in all_articles:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if LINKEDIN_PERSONAL in content:
        already += 1
        continue

    changed = False

    # HTML author link
    if OLD_AUTHOR_HTML in content:
        content = content.replace(OLD_AUTHOR_HTML, NEW_AUTHOR_HTML, 1)
        updated_html += 1
        changed = True

    # Schema FR
    if OLD_SCHEMA_FR in content:
        content = content.replace(OLD_SCHEMA_FR, NEW_SCHEMA_FR, 1)
        updated_schema += 1
        changed = True

    # Schema EN
    if OLD_SCHEMA_EN in content:
        content = content.replace(OLD_SCHEMA_EN, NEW_SCHEMA_EN, 1)
        updated_schema += 1
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

print(f"HTML auteure mis à jour : {updated_html}")
print(f"Schema author mis à jour : {updated_schema}")
print(f"Déjà fait (skip) : {already}")
