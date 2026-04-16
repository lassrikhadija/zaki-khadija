import sys, os, glob, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija'
all_html = glob.glob(os.path.join(base, '**', '*.html'), recursive=True)

# New round green-bordered question button CSS (minified)
NEW_QFLOAT = (
    '.question-float{display:flex;align-items:center;justify-content:center;'
    'width:44px;height:44px;background:var(--color-bg-alt);'
    'border:2px solid var(--color-primary);border-radius:50%;'
    'text-decoration:none;color:var(--color-primary);'
    'box-shadow:0 4px 16px rgba(0,230,118,.3);'
    'transition:transform .2s ease,box-shadow .2s ease;flex-shrink:0}'
)
NEW_QHOVER  = '.question-float:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,230,118,.55)}'
NEW_QLIGHT  = 'body.theme-light .question-float{background:#f0f0f0;border-color:var(--color-primary);color:var(--color-primary);box-shadow:0 4px 16px rgba(0,230,118,.2)}'

# Regex: replace the whole .phone-float / .question-float CSS block (minified)
PHONE_BLOCK = re.compile(
    r'\.(?:phone|question)-float\{[^}]+\}\s*'
    r'\.(?:phone|question)-float:hover\{[^}]+\}\s*'
    r'(?:\.(?:phone|question)-float svg\{[^}]+\}\s*)?',
    re.DOTALL
)
LIGHT_BLOCK = re.compile(
    r'body\.theme-light \.(?:phone|question)-float\{[^}]+\}'
)

# Also handle expanded FR format (from previous update-question-btn.py)
EXPANDED_BLOCK = re.compile(
    r'/\* Bouton question rond \*/\s*'
    r'\.question-float \{[^}]+\}\s*'
    r'\.question-float:hover \{[^}]+\}',
    re.DOTALL
)
NEW_EXPANDED = (
    '/* Bouton question rond */\n'
    '    .question-float {\n'
    '      display: flex;\n'
    '      align-items: center;\n'
    '      justify-content: center;\n'
    '      width: 44px;\n'
    '      height: 44px;\n'
    '      background: var(--color-bg-alt);\n'
    '      border: 2px solid var(--color-primary);\n'
    '      border-radius: 50%;\n'
    '      text-decoration: none;\n'
    '      color: var(--color-primary);\n'
    '      box-shadow: 0 4px 16px rgba(0,230,118,.3);\n'
    '      transition: transform .2s ease, box-shadow .2s ease;\n'
    '      flex-shrink: 0;\n'
    '    }\n'
    '    .question-float:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(0,230,118,.55); }'
)

updated = 0
for fp in sorted(all_html):
    try:
        content = open(fp, encoding='utf-8').read()
    except Exception:
        content = open(fp, encoding='latin-1').read()

    if 'question-float' not in content and 'phone-float' not in content:
        continue

    original = content

    # Fix minified CSS block
    content = PHONE_BLOCK.sub(NEW_QFLOAT + '\n    ' + NEW_QHOVER + '\n    ', content)
    content = LIGHT_BLOCK.sub(NEW_QLIGHT, content)

    # Fix expanded CSS block (index.html + some others)
    content = EXPANDED_BLOCK.sub(NEW_EXPANDED, content)

    # Also rename any stray .phone-float references in reduced-motion rule etc.
    content = content.replace('.phone-float', '.question-float')

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f'  [OK] {os.path.relpath(fp, base)}')

print(f'\nDone: {updated} files updated.')
