import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

c = read("ressources.html")

# Titre encore trop long -> version courte sur une ligne
c = c.replace(
    'Ce qu’il y a ici — et ce qu’il n’y a pas',
    'Ce qu’il y a — et ce qu’il n’y a pas',
    1
)

# Premier item trop long -> raccourcir
c = c.replace(
    'Des guides rédigés par une professionnelle — pas générés par IA sans vérification',
    'Des guides rédigés par une professionnelle, vérifiés — pas générés par IA',
    1
)

write("ressources.html", c)
print("OK")
