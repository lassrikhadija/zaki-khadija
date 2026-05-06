import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

c = read("secteurs.html")

old_style_end = '    body.theme-light .audit-pill{display:flex;align-items:center;gap:.35rem;padding:0 .875rem;height:44px;background:var(--color-primary);border-radius:22px;color:#000;font-weight:700;font-size:.78rem;text-decoration:none;white-space:nowrap;box-shadow:0 4px 16px rgba(0,230,118,.45);transition:transform .2s ease,box-shadow .2s ease;flex-shrink:0}\n  </style>'

new_style_end = (
    '    body.theme-light .audit-pill{display:flex;align-items:center;gap:.35rem;padding:0 .875rem;height:44px;background:var(--color-primary);border-radius:22px;color:#000;font-weight:700;font-size:.78rem;text-decoration:none;white-space:nowrap;box-shadow:0 4px 16px rgba(0,230,118,.45);transition:transform .2s ease,box-shadow .2s ease;flex-shrink:0}\n'
    '    /* Steps visuels */\n'
    '    .steps--visual{list-style:none!important;display:grid!important;grid-template-columns:repeat(4,1fr)!important;gap:1.5rem!important;padding:0!important;margin:2rem 0!important;counter-reset:none}\n'
    '    .steps--visual .steps__item{position:relative;padding:1.75rem 1.25rem 1.75rem!important;display:flex!important;flex-direction:column!important;gap:.75rem!important;background:rgba(255,255,255,.04);border:1.5px solid rgba(255,255,255,.08);border-radius:16px;transition:border-color .2s,background .2s}\n'
    '    .steps--visual .steps__item:hover{border-color:var(--color-primary);background:rgba(0,230,118,.05)}\n'
    '    .steps--visual .steps__number{width:44px;height:44px;border-radius:50%;background:var(--color-primary);color:#000;font-weight:800;font-size:1.1rem;display:flex!important;align-items:center;justify-content:center;flex-shrink:0}\n'
    '    .steps--visual .steps__arrow{position:absolute;top:50%;right:-1.1rem;transform:translateY(-50%);color:var(--color-primary);font-size:1.2rem;font-weight:700;z-index:1;line-height:1}\n'
    '    .steps--visual .steps__title{font-size:1rem!important;font-weight:700!important;color:var(--color-text)!important;margin:0!important;line-height:1.4}\n'
    '    .steps--visual .steps__text{font-size:.875rem!important;color:var(--color-text-muted)!important;line-height:1.65!important;margin:0!important}\n'
    '    @media(max-width:900px){.steps--visual{grid-template-columns:repeat(2,1fr)!important}.steps--visual .steps__arrow{display:none!important}}\n'
    '    @media(max-width:560px){.steps--visual{grid-template-columns:1fr!important}}\n'
    '  </style>'
)

if old_style_end in c:
    c = c.replace(old_style_end, new_style_end, 1)
    write("secteurs.html", c)
    print("Steps CSS inline: OK")
else:
    print("SKIP: pattern not found")
