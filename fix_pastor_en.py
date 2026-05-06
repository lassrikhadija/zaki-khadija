import os

ROOT = "."
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(c)

WHATSAPP_FR = 'https://wa.me/15147910591?text=Bonjour%2C%20je%20voudrais%20plus%20d%27informations%20sur%20vos%20services.'
WHATSAPP_EN = 'https://wa.me/15147910591?text=Hello%2C%20I%20would%20like%20more%20information%20about%20your%20services.'

def amplify(col1_items, col2_items):
    li1 = "\n".join(f"              <li>{i}</li>" for i in col1_items)
    li2 = "\n".join(f"              <li>{i}</li>" for i in col2_items)
    return (
        "\n    <!-- ============================\n"
        "         A — AMPLIFY\n"
        "         ============================ -->\n"
        '    <section class="section">\n'
        '      <div class="container">\n'
        '        <div class="split">\n'
        '          <div class="split__column">\n'
        '            <h2 class="split__title">What you\'re losing without knowing it</h2>\n'
        '            <ul class="split__list">\n'
        + li1 + "\n"
        '            </ul>\n'
        '          </div>\n'
        '          <div class="split__column">\n'
        '            <h2 class="split__title">What it concretely costs you</h2>\n'
        '            <ul class="split__list">\n'
        + li2 + "\n"
        '            </ul>\n'
        '          </div>\n'
        '        </div>\n'
        '      </div>\n'
        '    </section>\n\n'
    )

def story(quote):
    return (
        "    <!-- ============================\n"
        "         S — STORY\n"
        "         ============================ -->\n"
        '    <section class="section section--dark">\n'
        '      <div class="container section__header section__header--center" style="max-width:680px">\n'
        f'        <p style="font-size:1.05rem;color:var(--color-text-muted);line-height:1.8;font-style:italic;margin-bottom:1.25rem">{quote}</p>\n'
        '        <p style="color:var(--color-primary);font-weight:700;font-size:.95rem">&mdash;&nbsp;Khadija AitLassri, founder of NEXTIWEB</p>\n'
        '        <p style="color:var(--color-text-muted);font-size:.875rem;margin-top:.5rem">Computer scientist and former entrepreneur &mdash; <a href="/en/a-propos.html" style="color:var(--color-primary)">read my story&nbsp;&rarr;</a></p>\n'
        '      </div>\n'
        '    </section>\n\n'
    )

pages = {
    "en/creation-site.html": {
        "alt_anchor": '    <section class="section section--alt-bg">\n      <div class="container">\n        <header class="section__header">\n          <h2 class="section__title" id="pourquoi-site-web-montreal">',
        "amplify": amplify(
            [
                "Prospects judge your credibility in under 3 seconds",
                "A slow or poorly structured site drives away more than half your visitors before they read a line",
                "You explain yourself what your site should be convincing for you",
                "Without a professional site, every new client depends on word of mouth &mdash; and stops there",
            ],
            [
                "1 prospect lost per week = thousands of dollars a year",
                "A site with no clear call to action = every visit invested at a loss",
                "Your competitors absorb the clients who could have called you",
                "Every day without a redesign, the gap with your competitor grows",
            ]
        ),
        "story": story("&ldquo;&nbsp;I built my first site myself. Clean code, solid structure. And I waited for clients. Zero contact for months. It wasn&rsquo;t a code problem &mdash; it was a strategy problem. That&rsquo;s what NEXTIWEB fixes.&nbsp;&rdquo;"),
    },
    "en/seo.html": {
        "alt_anchor": '    <section class="section section--alt-bg">\n      <div class="container">\n        <header class="section__header">\n          <h2 class="section__title" id="pourquoi-seo-montreal">',
        "amplify": amplify(
            [
                "Page 1 captures nearly all clicks &mdash; if you&rsquo;re not there, you don&rsquo;t exist for those prospects",
                "Your competitor captures every click you could have received",
                "You spend on ads what SEO would do for free long-term",
                "Every week without SEO = growth dependent on word of mouth and luck",
            ],
            [
                "Months of work published online&hellip; that nobody finds on Google",
                "A recurring ad budget to compensate for avoidable invisibility",
                "Your qualified prospects land on a better-positioned competitor",
                "No data on where your clients come from &mdash; impossible to invest in the right place",
            ]
        ),
        "story": story("&ldquo;&nbsp;When I launched my first site, it was technically flawless. But invisible on Google. I learned that SEO isn&rsquo;t improvised &mdash; it&rsquo;s built with the right keywords, the right structure and consistency. That&rsquo;s the method I apply for every NEXTIWEB client.&nbsp;&rdquo;"),
    },
    "en/marketing-digital.html": {
        "alt_anchor": '    <section class="section section--alt-bg">\n      <div class="container">\n        <header class="section__header">\n          <h2 class="section__title" id="digital-marketing-components">',
        "amplify": amplify(
            [
                "Your site generates traffic that doesn&rsquo;t convert &mdash; every visit is a missed opportunity",
                "You don&rsquo;t know where your clients come from, impossible to invest in the right place",
                "A prospect not followed up within 48&nbsp;h has far fewer chances to convert",
                "Your acquisition depends on word of mouth &mdash; unpredictable growth, impossible to scale",
            ],
            [
                "Ad budget wasted on a vague target and a site that doesn&rsquo;t convert",
                "Warm leads that come back later&hellip; to a competitor who followed up",
                "No visibility on your real marketing ROI &mdash; decisions made in the dark",
                "Random growth while your competitors build a system that runs itself",
            ]
        ),
        "story": story("&ldquo;&nbsp;I spent on ads before having a real strategy. Budget gone, zero results. Real digital growth doesn&rsquo;t come from a single action &mdash; it comes from a coordinated system where every lever reinforces the others. That&rsquo;s what NEXTIWEB builds with you.&nbsp;&rdquo;"),
    },
}

for fname, cfg in pages.items():
    c = read(fname)

    # Insert A + S before first section--alt-bg
    anchor = cfg["alt_anchor"]
    idx = c.find(anchor, c.find('<main>'))
    if idx >= 0:
        insert = cfg["amplify"] + cfg["story"] + '    <!-- ============================\n         T — TRANSFORMATION\n         ============================ -->\n'
        c = c[:idx] + insert + c[idx:]
        print(f"PASTOR A+S: {fname} OK")
    else:
        print(f"SKIP {fname}: anchor not found")

    # WhatsApp EN
    c = c.replace(WHATSAPP_FR, WHATSAPP_EN)

    write(fname, c)
    print(f"Saved: {fname}")

print("\nTermine.")
