import re, os, glob

ROOT = "."

def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

# ── 1. CSS global : text-wrap:balance ──
css_path = os.path.join(ROOT, "assets/css/styles.min.css")
css = read(css_path)
old = ".section__title{font-size:2.5rem;margin-bottom:0.75rem;font-weight:700;letter-spacing:-0.02em;line-height:1.15}"
new = ".section__title{font-size:2.5rem;margin-bottom:0.75rem;font-weight:700;letter-spacing:-0.02em;line-height:1.15;text-wrap:balance}"
css = css.replace(old, new, 1)
css = re.sub(
    r'(\.section__subtitle\{)([^}]*)(\})',
    lambda m: m.group(1) + m.group(2) + (';text-wrap:balance' if 'text-wrap' not in m.group(2) else '') + m.group(3),
    css, count=1
)
write(css_path, css)
print("CSS: text-wrap:balance ajoute")

# ── 2. Bump CSS v5 → v6 sur tous les HTML ──
html_files = glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True)
bumped = 0
for fp in html_files:
    c = read(fp)
    if 'styles.min.css?v=5' in c:
        c = c.replace('styles.min.css?v=5', 'styles.min.css?v=6')
        write(fp, c)
        bumped += 1
print(f"Version bump: {bumped} fichiers v5->v6")

# ── 3. Items A trop longs ──
fixes_text = {
    'creation-site.html': [
        ('Un site lent ou brouillon fait fuir les visiteurs avant qu\'ils lisent une ligne',
         'Un site lent fait fuir les visiteurs avant le premier mot lu'),
        ('1 prospect perdu par semaine, c\'est une croissance offerte à un concurrent',
         '1 prospect/semaine perdu = croissance offerte à un concurrent'),
    ],
}
for fname, repls in fixes_text.items():
    c = read(fname)
    for old_t, new_t in repls:
        c = c.replace(old_t, new_t)
    write(fname, c)
print("Items A: raccourcis")

# ── 4. Ligne verte sous H1 des 3 pages service ──
GREEN_LINE = '\n        <div style="width:44px;height:3px;background:var(--color-primary);margin:1.25rem auto 0;border-radius:2px"></div>'
service_pages = ['creation-site.html', 'seo.html', 'marketing-digital.html']
for fname in service_pages:
    c = read(fname)
    old_end = '      </div>\n    </section>\n\n    <!-- ============================\n         A \xe2\x80\x94 AMPLIFIER'
    new_end = '      </div>' + GREEN_LINE + '\n    </section>\n\n    <!-- ============================\n         A \xe2\x80\x94 AMPLIFIER'
    if old_end in c:
        c = c.replace(old_end, new_end, 1)
        write(fname, c)
        print(f"Ligne verte: {fname} OK")
    else:
        # Try alternative matching
        marker = '    <!-- ============================\n         A'
        idx = c.find(marker)
        if idx > 0:
            # Find the </div>\n    </section> just before
            pos = c.rfind('      </div>\n    </section>', 0, idx)
            if pos >= 0:
                insert_after = pos + len('      </div>')
                c = c[:insert_after] + GREEN_LINE + c[insert_after:]
                write(fname, c)
                print(f"Ligne verte (alt): {fname} OK")
            else:
                print(f"SKIP ligne verte: {fname}")
        else:
            print(f"SKIP ligne verte: {fname}")

# ── 5. Guillemet decoratif dans section S ──
QUOTE_DECO = '<div aria-hidden="true" style="font-size:5rem;line-height:1;color:var(--color-primary);opacity:.15;font-family:Georgia,serif;font-weight:700;margin-bottom:-.5rem;text-align:center">&ldquo;</div>\n        '
for fname in service_pages:
    c = read(fname)
    marker = '        <p style="font-size:1.05rem;color:var(--color-text-muted);line-height:1.8;font-style:italic;margin-bottom:1.25rem">'
    if marker in c:
        c = c.replace(marker, QUOTE_DECO + marker, 1)
        write(fname, c)
        print(f"Guillemet: {fname} OK")
    else:
        print(f"SKIP guillemet: {fname}")

print("\nTermine.")
