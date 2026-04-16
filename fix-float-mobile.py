import sys, os, glob, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija'
all_html = glob.glob(os.path.join(base, '**', '*.html'), recursive=True)
EXCLUDE = {'contact.html', 'question.html', 'merci.html'}

# All variants of the hide rule found across files
HIDE_VARIANTS = [
    # minified
    '@media(max-width:768px){.float-bar{display:none!important}}',
    # with spaces
    '@media(max-width:768px){ .float-bar{display:none!important} }',
    # with comment before
    '/* Masquer la barre flottante sur mobile */\n    @media(max-width:768px){.float-bar{display:none!important}}',
    # EN comment
    '/* Hide floating bar on mobile */\n    @media(max-width:768px){.float-bar{display:none!important}}',
]

NEW_MOBILE = '@media(max-width:768px){.float-bar{flex-direction:column;gap:.4rem;bottom:1rem;right:.875rem}}'

updated = 0
for fp in sorted(all_html):
    if os.path.basename(fp) in EXCLUDE:
        continue
    try:
        content = open(fp, encoding='utf-8').read()
    except Exception:
        content = open(fp, encoding='latin-1').read()

    if 'float-bar' not in content:
        continue

    original = content

    for variant in HIDE_VARIANTS:
        if variant in content:
            content = content.replace(variant, NEW_MOBILE)

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f'  [OK] {os.path.relpath(fp, base)}')

print(f'\nDone: {updated} files updated.')
