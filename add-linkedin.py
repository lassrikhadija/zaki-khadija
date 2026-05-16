import os, glob, re

BASE = r"C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija"

LINKEDIN_COMPANY  = "https://www.linkedin.com/company/25819184/"
LINKEDIN_PERSONAL = "https://www.linkedin.com/in/khadija-ait-lassri/"

LI_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" '
          'viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
          '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037'
          '-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c'
          '.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286z'
          'M5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065z'
          'm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 '
          '1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 '
          '22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>')

LI_STYLE = ('display:inline-flex;align-items:center;gap:.4rem;'
            'color:var(--color-text-muted);font-size:.875rem;'
            'text-decoration:none;transition:color .2s')

def make_li_block(aria_label):
    link = (f'<a href="{LINKEDIN_COMPANY}" target="_blank" '
            f'rel="noopener noreferrer" aria-label="{aria_label}" '
            f'style="{LI_STYLE}">{LI_SVG} LinkedIn</a>')
    return f'</address>\n      <p style="margin-top:.75rem">{link}</p>\n      </div>'

FR_BLOCK = make_li_block("NEXTIWEB sur LinkedIn")
EN_BLOCK = make_li_block("NEXTIWEB on LinkedIn")

all_html = glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True)
all_html = [f for f in all_html if ".git" not in f and "node_modules" not in f]

updated = skipped = already = 0

for path in all_html:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if LINKEDIN_COMPANY in content:
        already += 1
        continue

    if "</address>" not in content or "site-footer" not in content:
        skipped += 1
        continue

    parts = path.replace("\\", "/").split("/")
    is_en = "en" in parts and parts.index("en") > parts.index("zaki-khadija")
    block = EN_BLOCK if is_en else FR_BLOCK

    # Replace </address> followed by optional spaces then </div> (first occurrence in footer)
    new_content = re.sub(r'</address>\s*\n\s*</div>', block, content, count=1)

    if new_content == content:
        skipped += 1
        continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Done — updated:{updated}  already_done:{already}  skipped:{skipped}")
