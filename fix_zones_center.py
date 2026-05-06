import os, re

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

files = [
    'zones-desservies/montreal.html',
    'zones-desservies/quebec.html',
    'zones-desservies/canada.html',
    'en/zones-desservies/montreal.html',
    'en/zones-desservies/quebec.html',
    'en/zones-desservies/canada.html',
]

for fname in files:
    c = read(fname)
    before = c.count('section__header--center')
    # Remplace tous les section__header sans --center
    c = re.sub(
        r'<header class="section__header">',
        '<header class="section__header section__header--center">',
        c
    )
    after = c.count('section__header--center')
    write(fname, c)
    print(f"{fname}: +{after - before} centres ({after} total)")

print("\nTermine.")
