import sys, os, re, glob
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija'
all_html = glob.glob(os.path.join(base, '**', '*.html'), recursive=True)
EXCLUDE = {'contact.html', 'question.html', 'merci.html'}

# ── CSS replacements ──────────────────────────────────────────────────────────

# FR expanded format
OLD_CSS_FR = """    /* Pilule "J'ai une question" */
    .question-float {
      display: flex;
      align-items: center;
      gap: .5rem;
      background: var(--color-bg-alt);
      border: 1px solid rgba(255,255,255,.12);
      border-radius: 2rem;
      padding: .6rem 1.1rem;
      text-decoration: none;
      color: var(--color-text);
      font-size: .875rem;
      font-weight: 600;
      box-shadow: 0 4px 16px rgba(0,0,0,.35);
      transition: transform .2s ease, box-shadow .2s ease;
    }
    .question-float:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(0,0,0,.45); color: var(--color-primary); }"""

NEW_CSS_FR = """    /* Bouton question rond */
    .question-float {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      background: var(--color-bg-alt);
      border: 1px solid rgba(255,255,255,.18);
      border-radius: 50%;
      text-decoration: none;
      color: var(--color-primary);
      box-shadow: 0 4px 16px rgba(0,0,0,.35);
      transition: transform .2s ease, box-shadow .2s ease;
      flex-shrink: 0;
    }
    .question-float:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(0,0,0,.45); }"""

# EN minified format
OLD_CSS_EN = """.question-float{display:flex;align-items:center;gap:.5rem;background:var(--color-bg-alt);border:1px solid rgba(255,255,255,.12);border-radius:2rem;padding:.6rem 1.1rem;text-decoration:none;color:var(--color-text);font-size:.875rem;font-weight:600;box-shadow:0 4px 16px rgba(0,0,0,.35);transition:transform .2s ease,box-shadow .2s ease}
    .question-float:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.45);color:var(--color-primary)}"""

NEW_CSS_EN = """.question-float{display:flex;align-items:center;justify-content:center;width:44px;height:44px;background:var(--color-bg-alt);border:1px solid rgba(255,255,255,.18);border-radius:50%;text-decoration:none;color:var(--color-primary);box-shadow:0 4px 16px rgba(0,0,0,.35);transition:transform .2s ease,box-shadow .2s ease;flex-shrink:0}
    .question-float:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.45)}"""

# Also fix hover-only line in EN files (some files may have just the hover)
OLD_HOVER_EN = """.question-float:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.45);color:var(--color-primary)}"""
NEW_HOVER_EN = """.question-float:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.45)}"""

# Light mode
OLD_LIGHT = """    body.theme-light .question-float {
      background: #fff;
      border-color: rgba(0,0,0,.1);
      color: #1a1a1a;"""
NEW_LIGHT = """    body.theme-light .question-float {
      background: #f0f0f0;
      border-color: rgba(0,0,0,.12);
      color: var(--color-primary);"""

OLD_LIGHT_EN = """body.theme-light .question-float{background:#fff;border-color:rgba(0,0,0,.1);color:#1a1a1a;"""
NEW_LIGHT_EN = """body.theme-light .question-float{background:#f0f0f0;border-color:rgba(0,0,0,.12);color:var(--color-primary);"""

# ── HTML replacement — remove text label, keep only SVG icon ─────────────────
# FR: remove "J'ai une question" text
HTML_FR = re.compile(
    r'(<a[^>]*class="question-float"[^>]*>\s*<svg[^>]*>.*?</svg>)\s*\n\s*J\'ai une question\s*\n(\s*</a>)',
    re.DOTALL
)
# EN: remove "I have a question" text
HTML_EN = re.compile(
    r'(<a[^>]*class="question-float"[^>]*>\s*<svg[^>]*>.*?</svg>)\s*\n\s*I have a question\s*\n(\s*</a>)',
    re.DOTALL
)

updated = 0
for fp in sorted(all_html):
    if os.path.basename(fp) in EXCLUDE:
        continue
    try:
        content = open(fp, encoding='utf-8').read()
    except Exception:
        content = open(fp, encoding='latin-1').read()

    if 'question-float' not in content:
        continue

    original = content
    rel = os.path.relpath(fp, base)

    # CSS
    content = content.replace(OLD_CSS_FR, NEW_CSS_FR)
    content = content.replace(OLD_CSS_EN, NEW_CSS_EN)
    content = content.replace(OLD_HOVER_EN, NEW_HOVER_EN)
    content = content.replace(OLD_LIGHT, NEW_LIGHT)
    content = content.replace(OLD_LIGHT_EN, NEW_LIGHT_EN)

    # HTML — remove text
    content = HTML_FR.sub(r'\1\n\2', content)
    content = HTML_EN.sub(r'\1\n\2', content)

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f'  [OK] {rel}')

print(f'\nDone: {updated} files updated.')
