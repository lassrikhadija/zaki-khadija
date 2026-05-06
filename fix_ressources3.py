import os
ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

c = read("ressources.html")
c = c.replace(
    'Des guides rédigés par une professionnelle, vérifiés — pas générés par IA',
    'Des guides rédigés par une professionnelle, vérifiés',
    1
)
write("ressources.html", c)
print("OK")
