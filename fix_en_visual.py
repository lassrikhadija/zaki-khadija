import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

GREEN_LINE = '\n        <div style="width:44px;height:3px;background:var(--color-primary);margin:1.25rem auto 0;border-radius:2px"></div>'
QUOTE_DECO = '<div aria-hidden="true" style="font-size:5rem;line-height:1;color:var(--color-primary);opacity:.15;font-family:Georgia,serif;font-weight:700;margin-bottom:-.5rem;text-align:center">&ldquo;</div>\n        '
QUOTE_P    = '<p style="font-size:1.05rem;color:var(--color-text-muted);line-height:1.8;font-style:italic;margin-bottom:1.25rem">'

# ── Helper : insérer ligne verte avant </section> du hero ──
def add_green_line(c):
    # Le hero se ferme juste avant la section A
    anchor = '      </div>\n    </section>\n\n\n    <!-- ============================\n         A — AMPLIFY'
    idx = c.find(anchor)
    if idx >= 0:
        insert_pos = idx + len('      </div>')
        c = c[:insert_pos] + GREEN_LINE + c[insert_pos:]
        return c, True
    return c, False

# ── Helper : insérer guillemet déco dans section S ──
def add_quote_deco(c):
    if QUOTE_P in c and QUOTE_DECO not in c:
        c = c.replace(QUOTE_P, QUOTE_DECO + QUOTE_P, 1)
        return c, True
    return c, False

# ════════════════════════════════════════
# en/creation-site.html
# ════════════════════════════════════════
c = read("en/creation-site.html")

c, ok = add_green_line(c)
print(f"creation-site EN — ligne verte: {'OK' if ok else 'SKIP'}")
c, ok = add_quote_deco(c)
print(f"creation-site EN — guillemet: {'OK' if ok else 'SKIP'}")

# Raccourcir les items A trop longs
c = c.replace(
    "A slow or poorly structured site drives away more than half your visitors before they read a line",
    "A slow or messy site loses visitors before they read a single word"
)
c = c.replace(
    "You explain yourself what your site should be convincing for you",
    "You explain what your site should convince on its own"
)

write("en/creation-site.html", c)

# ════════════════════════════════════════
# en/seo.html
# ════════════════════════════════════════
c = read("en/seo.html")

c, ok = add_green_line(c)
print(f"seo EN — ligne verte: {'OK' if ok else 'SKIP'}")
c, ok = add_quote_deco(c)
print(f"seo EN — guillemet: {'OK' if ok else 'SKIP'}")

# Raccourcir items A trop longs
c = c.replace(
    "Page 1 captures nearly all clicks &mdash; if you&rsquo;re not there, you don&rsquo;t exist for those prospects",
    "Nearly all clicks go to page 1 &mdash; absent from it, you simply don&rsquo;t exist"
)
c = c.replace(
    "Your qualified prospects land on a better-positioned competitor",
    "Your qualified prospects land on a better-ranked competitor"
)

write("en/seo.html", c)

# ════════════════════════════════════════
# en/marketing-digital.html
# ════════════════════════════════════════
c = read("en/marketing-digital.html")

c, ok = add_green_line(c)
print(f"marketing-digital EN — ligne verte: {'OK' if ok else 'SKIP'}")
c, ok = add_quote_deco(c)
print(f"marketing-digital EN — guillemet: {'OK' if ok else 'SKIP'}")

# Raccourcir items A trop longs
c = c.replace(
    "Your site generates traffic that doesn&rsquo;t convert &mdash; every visit is a missed opportunity",
    "Your site gets traffic that doesn&rsquo;t convert &mdash; every visit wasted"
)
c = c.replace(
    "Your acquisition depends on word of mouth &mdash; unpredictable growth, impossible to scale",
    "Your acquisition depends on word of mouth &mdash; unpredictable, impossible to scale"
)
c = c.replace(
    "Random growth while your competitors build a system that runs itself",
    "Stagnation while your competitors build a system that runs itself"
)

write("en/marketing-digital.html", c)

print("\nTermine.")
