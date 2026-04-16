import sys, os, glob
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija'

all_html = glob.glob(os.path.join(base, 'en', '**', '*.html'), recursive=True)

updated = 0
for fp in sorted(all_html):
    try:
        content = open(fp, encoding='utf-8').read()
    except Exception:
        content = open(fp, encoding='latin-1').read()

    if 'phone-float' not in content:
        continue

    original = content

    # Replace all CSS/HTML references: .phone-float → .question-float
    content = content.replace('.phone-float', '.question-float')

    # Add color to hover rule (minified format)
    content = content.replace(
        '.question-float:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.45)}',
        '.question-float:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.45);color:var(--color-primary)}'
    )
    # Also handle expanded format (in case)
    content = content.replace(
        '.question-float:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(0,0,0,.45); }',
        '.question-float:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(0,0,0,.45); color: var(--color-primary); }'
    )

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        rel = os.path.relpath(fp, base)
        print(f'  [OK] {rel}')

print(f'\nDone: {updated} EN files fixed.')
