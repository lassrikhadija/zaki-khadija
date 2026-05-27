import re

css_path = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\css\styles.min.css'
out_path = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\css\critical.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

original_size = len(css.encode('utf-8'))


def split_top_level_rules(css_text):
    """Split CSS text into top-level rules using a bracket-depth counter."""
    rules = []
    depth = 0
    start = 0
    i = 0
    in_string = False
    string_char = None

    while i < len(css_text):
        ch = css_text[i]

        if in_string:
            backslash_before = (i > 0 and css_text[i - 1] == '\\')
            if ch == string_char and not backslash_before:
                in_string = False
        elif ch in ('"', "'"):
            in_string = True
            string_char = ch
        elif ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                rule = css_text[start:i + 1].strip()
                if rule:
                    rules.append(rule)
                start = i + 1
        i += 1

    # Capture any trailing content
    trailing = css_text[start:].strip()
    if trailing:
        rules.append(trailing)

    return rules


# Critical keyword patterns to match against the rule head (selector / at-rule)
CRITICAL_KEYWORDS = [
    ':root',
    'html{',
    'html,body',
    '*,*::before,*::after',
    'body{',
    'body.scrolled',
    'body.theme-light',
    'body.mobile-nav-active',
    '.top-bar',
    '.site-header',
    '.header__inner',
    '.logo',
    '.main-nav',
    '.nav__link',
    '.nav__item',
    '.nav__submenu',
    '.theme-toggle',
    '.language-switcher',
    '.hero-bg',
    '.hero-metric',
    '.hero-bg__',
    '#hero-stars',
    '.btn',
    '.assurance',
    '@keyframes',
    '@media (max-width:860px)',
    '@media (max-width:768px)',
    '@media (max-width:480px)',
    '.nav-toggle',
    '.mobile-nav',
    '.mobile-nav-overlay',
    '.mobile-nav__',
    '.container',
    'a{',
    'a:hover',
]


def is_critical(rule):
    """Return (True, matched_keyword) if the rule should be included in critical CSS."""
    # The selector / at-rule preamble is the text before the first '{'
    brace_pos = rule.find('{')
    head = rule[:brace_pos + 1] if brace_pos != -1 else rule
    for kw in CRITICAL_KEYWORDS:
        if kw in head:
            return True, kw
    return False, None


rules = split_top_level_rules(css)
print(f'Total top-level rules found: {len(rules)}')

critical_rules = []
skipped_sample = []

for rule in rules:
    ok, matched = is_critical(rule)
    if ok:
        critical_rules.append(rule)
    else:
        if len(skipped_sample) < 5:
            skipped_sample.append(rule[:100])

print(f'Critical rules matched: {len(critical_rules)}')
print(f'Skipped rules (sample of up to 5):')
for s in skipped_sample:
    print(f'  {s}')

critical_css = ''.join(critical_rules)
critical_size = len(critical_css.encode('utf-8'))
pct = critical_size / original_size * 100

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(critical_css)

print()
print('--- Sizes ---')
print(f'Original CSS : {original_size:,} bytes  ({original_size / 1024:.1f} KB)')
print(f'Critical CSS : {critical_size:,} bytes  ({critical_size / 1024:.1f} KB)')
print(f'Extracted    : {pct:.1f}%')
print(f'Written to   : {out_path}')
