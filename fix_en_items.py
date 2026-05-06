import os
ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

# ── en/creation-site.html ──
c = read("en/creation-site.html")
c = c.replace(
    "Without a professional site, every new client depends on word of mouth &mdash; and stops there",
    "Without a pro site, every new client comes from word of mouth &mdash; and stops there"
)
write("en/creation-site.html", c)
print("creation-site EN: OK")

# ── en/seo.html ──
c = read("en/seo.html")
c = c.replace(
    "Every week without SEO = growth dependent on word of mouth and luck",
    "Every week without SEO = growth left to chance"
)
c = c.replace(
    "No data on where your clients come from &mdash; impossible to invest in the right place",
    "No data on client sources &mdash; impossible to invest wisely"
)
write("en/seo.html", c)
print("seo EN: OK")

# ── en/marketing-digital.html ──
c = read("en/marketing-digital.html")
c = c.replace(
    "You don&rsquo;t know where your clients come from, impossible to invest in the right place",
    "You don&rsquo;t know where clients come from &mdash; impossible to invest wisely"
)
c = c.replace(
    "A prospect not followed up within 48&nbsp;h has far fewer chances to convert",
    "A prospect not followed up within 48h rarely converts"
)
c = c.replace(
    "Your acquisition depends on word of mouth &mdash; unpredictable, impossible to scale",
    "Word-of-mouth only: unpredictable growth, impossible to scale"
)
write("en/marketing-digital.html", c)
print("marketing-digital EN: OK")
