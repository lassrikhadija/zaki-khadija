import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija'

def get_html_files(d):
    files = []
    for root, dirs, fs in os.walk(d):
        dirs[:] = [x for x in dirs if x not in ['node_modules','.git','partials']]
        for f in fs:
            if f.endswith('.html') and 'backup' not in f:
                files.append(os.path.join(root, f))
    return files

files = get_html_files(base)

title_issues = []
desc_issues = []
h1_issues = []
canonical_issues = []
word_count_issues = []
h2_map = {}

for fp in files:
    rel = fp.replace(base + os.sep, '')
    try:
        content = open(fp, encoding='utf-8').read()
    except:
        content = open(fp, encoding='latin-1').read()

    # Title
    m = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        if len(title) > 60:
            title_issues.append((rel, len(title), title))

    # Meta description
    m = re.search(r'<meta\s[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.IGNORECASE)
    if not m:
        m = re.search(r'<meta\s[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, re.IGNORECASE)
    if m:
        desc = m.group(1).strip()
        if len(desc) > 155:
            desc_issues.append((rel, len(desc), desc))

    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
    for h1 in h1s:
        clean = re.sub(r'<[^>]+>', '', h1).strip()
        if len(clean) > 70:
            h1_issues.append((rel, len(clean), clean))

    # H2 collect
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL | re.IGNORECASE)
    for h2 in h2s:
        clean = re.sub(r'<[^>]+>', '', h2).strip()
        if clean:
            h2_map.setdefault(clean, []).append(rel)

    # Canonical
    m = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\'](.*?)["\']', content, re.IGNORECASE)
    if m:
        canonical = m.group(1).strip()
        # Derive expected URL path from file path
        url_path = fp.replace(base, '').replace('\\', '/').replace('/index.html', '/').rstrip('/')
        if not url_path:
            url_path = '/'
        canon_path = re.sub(r'https?://nextiweb\.ca', '', canonical).replace('/index.html', '/').rstrip('/')
        if not canon_path:
            canon_path = '/'
        if canon_path != url_path:
            canonical_issues.append((rel, url_path, canonical))

    # Word count
    text = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = [w for w in text.split() if len(w) > 2 and not w.startswith('{')]
    if len(words) < 200:
        word_count_issues.append((rel, len(words)))

# H2 duplicates
h2_dups = {h2: pages for h2, pages in h2_map.items() if len(pages) > 1}

print('=== TITLES > 60 chars (%d pages) ===' % len(title_issues))
for rel, n, t in sorted(title_issues, key=lambda x: -x[1]):
    print(f'  [{n}c] {rel}')
    print(f'       => {t}')

print()
print('=== META DESCRIPTIONS > 155 chars (%d pages) ===' % len(desc_issues))
for rel, n, d in sorted(desc_issues, key=lambda x: -x[1]):
    print(f'  [{n}c] {rel}')
    print(f'       => {d[:120]}...')

print()
print('=== H1 > 70 chars (%d) ===' % len(h1_issues))
for rel, n, h in h1_issues:
    print(f'  [{n}c] {rel}: {h[:100]}')

print()
print('=== H2 DUPLICATES (%d) ===' % len(h2_dups))
for h2, pages in sorted(h2_dups.items(), key=lambda x: -len(x[1])):
    if len(pages) > 3:
        print(f'  "{h2[:60]}" -> {len(pages)} pages')

print()
print('=== CANONICAL MISMATCHES (%d) ===' % len(canonical_issues))
for rel, path, canon in canonical_issues:
    print(f'  {rel}')
    print(f'    expected: {path}')
    print(f'    actual:   {canon}')

print()
print('=== LOW WORD COUNT < 200 (%d pages) ===' % len(word_count_issues))
for rel, n in sorted(word_count_issues, key=lambda x: x[1])[:15]:
    print(f'  [{n}w] {rel}')
