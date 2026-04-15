import sys, os, re, glob
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija'

# Find all HTML files (excluding tunnel pages that have no float bar)
EXCLUDE = {'contact.html', 'question.html', 'merci.html'}
all_html = glob.glob(os.path.join(base, '**', '*.html'), recursive=True)
html_files = [f for f in all_html if os.path.basename(f) not in EXCLUDE]

# ── CSS replacement ──────────────────────────────────────────────────────────
OLD_CSS_PHONE = r"""    /* Pilule téléphone */
    .phone-float {
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
    .phone-float:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(0,0,0,.45); }
    .phone-float svg { color: var(--color-primary); flex-shrink: 0; }"""

NEW_CSS_QUESTION = """    /* Pilule "J'ai une question" */
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

# Also fix the light-mode rule
OLD_CSS_LIGHT = """    body.theme-light .phone-float {
      background: #fff;
      border-color: rgba(0,0,0,.1);
      color: #1a1a1a;"""
NEW_CSS_LIGHT = """    body.theme-light .question-float {
      background: #fff;
      border-color: rgba(0,0,0,.1);
      color: #1a1a1a;"""

# Fix the reduced-motion rule
OLD_MOTION = "not(.phone-float)"
NEW_MOTION = "not(.question-float)"

# ── HTML replacement ─────────────────────────────────────────────────────────
# Phone link (multiline)
PHONE_PATTERN = re.compile(
    r'<a\s+href="tel:[^"]*"\s+class="phone-float"[^>]*>.*?</a>',
    re.DOTALL
)
QUESTION_HTML_FR = (
    '<a href="/question.html" class="question-float" aria-label="Poser une question à NEXTIWEB">'
    '\n      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>'
    '</svg>\n      J\'ai une question\n    </a>'
)
QUESTION_HTML_EN = (
    '<a href="/question.html" class="question-float" aria-label="Ask NEXTIWEB a question">'
    '\n      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>'
    '</svg>\n      I have a question\n    </a>'
)

# Also update the comment above the float bar
OLD_COMMENT = "<!-- Barre flottante bas droite : téléphone + WhatsApp -->"
NEW_COMMENT = "<!-- Barre flottante bas droite : question + WhatsApp -->"

# ── Process ──────────────────────────────────────────────────────────────────
updated = 0
skipped = 0

for fp in sorted(html_files):
    # Only process files that actually have phone-float
    try:
        content = open(fp, encoding='utf-8').read()
    except Exception:
        content = open(fp, encoding='latin-1').read()

    if 'phone-float' not in content:
        continue

    original = content
    rel = os.path.relpath(fp, base)

    # Determine FR or EN
    is_en = rel.startswith('en' + os.sep) or rel.startswith('en/')
    question_html = QUESTION_HTML_EN if is_en else QUESTION_HTML_FR

    # 1. CSS phone-float block
    content = content.replace(OLD_CSS_PHONE, NEW_CSS_QUESTION)

    # 2. CSS light-mode rule
    content = content.replace(OLD_CSS_LIGHT, NEW_CSS_LIGHT)

    # 3. Reduced-motion rule
    content = content.replace(OLD_MOTION, NEW_MOTION)

    # 4. HTML phone link
    content = PHONE_PATTERN.sub(question_html, content)

    # 5. Comment
    content = content.replace(OLD_COMMENT, NEW_COMMENT)

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f'  [OK] {rel}')
    else:
        skipped += 1
        print(f'  [SKIP] {rel}')

print(f'\nDone: {updated} updated, {skipped} skipped.')
