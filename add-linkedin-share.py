import os, glob

BASE = r"C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija"

LI_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" '
          'viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
          '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037'
          '-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c'
          '.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286z'
          'M5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065z'
          'm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 '
          '1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 '
          '22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>')

LI_BTN_STYLE = ("display:inline-flex;align-items:center;gap:.5rem;"
                "background:#0A66C2;color:#fff;font-size:.875rem;"
                "font-weight:600;padding:.5rem 1.25rem;border-radius:2rem;"
                "text-decoration:none;transition:opacity .2s")

SHARE_JS = ("window.open('https://www.linkedin.com/sharing/share-offsite/?url='"
            "+encodeURIComponent(window.location.href),'_blank',"
            "'width=600,height=600');return false;")

def share_block(label, aria):
    intro = "Cet article vous a été utile ? Partagez-le :" if "Partagez" in label else "Found this article helpful? Share it:"
    return (f'\n          <div style="margin-top:2rem;padding-top:1.5rem;'
            f'border-top:1px solid rgba(255,255,255,.07);text-align:center">\n'
            f'            <p style="font-size:.85rem;color:var(--color-text-muted);margin-bottom:.75rem">{intro}</p>\n'
            f'            <a href="#" onclick="{SHARE_JS}" '
            f'style="{LI_BTN_STYLE}" '
            f'aria-label="{aria}">'
            f'{LI_SVG} {label}</a>\n'
            f'          </div>')

FR_BLOCK = share_block("Partager sur LinkedIn", "Partager cet article sur LinkedIn")
EN_BLOCK = share_block("Share on LinkedIn",     "Share this article on LinkedIn")

articles = [f for f in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True)
            if "blog" in f and "index" not in f and ".git" not in f]

updated = skipped = already = 0

for path in articles:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "linkedin.com/sharing" in content:
        already += 1
        continue

    parts = path.replace("\\", "/").split("/")
    is_en = "en" in parts and parts.index("en") > parts.index("zaki-khadija")
    block = EN_BLOCK if is_en else FR_BLOCK

    if "</div><!-- /article-body -->" in content:
        content = content.replace("</div><!-- /article-body -->",
                                  block + "\n          </div><!-- /article-body -->", 1)
    elif "</article>" in content:
        content = content.replace("</article>", block + "\n        </article>", 1)
    else:
        skipped += 1
        continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    updated += 1

print(f"Done — updated:{updated}  already:{already}  skipped:{skipped}")
