import os
ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

c = read("en/services.html")

c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title" id="creation-sites-montreal">',
    '<header class="section__header section__header--center">\n          <h2 class="section__title" id="creation-sites-montreal">',
    1
)
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title" id="services-seo-pme-montreal">',
    '<header class="section__header section__header--center">\n          <h2 class="section__title" id="services-seo-pme-montreal">',
    1
)
c = c.replace(
    '<header class="section__header">\n          <h2 class="section__title" id="strategies-marketing-digital-entreprises">',
    '<header class="section__header section__header--center">\n          <h2 class="section__title" id="strategies-marketing-digital-entreprises">',
    1
)

c = c.replace(
    'https://wa.me/15147910591?text=Bonjour%2C%20je%20voudrais%20plus%20d%27informations%20sur%20vos%20services.',
    'https://wa.me/15147910591?text=Hello%2C%20I%20would%20like%20more%20information%20about%20your%20services.'
)

write("en/services.html", c)
print("OK")
