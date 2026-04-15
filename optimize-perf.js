const fs = require('fs');
const path = require('path');

const BASE = __dirname;

// ─── Helpers ────────────────────────────────────────────────────────────────

function getAllHtmlFiles(dir, files = []) {
  const items = fs.readdirSync(dir);
  for (const item of items) {
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (!['node_modules', '.git'].includes(item)) getAllHtmlFiles(full, files);
    } else if (item.endsWith('.html')) {
      files.push(full);
    }
  }
  return files;
}

// ─── Transformations ─────────────────────────────────────────────────────────

function wrapLogoInPicture(content) {
  // Match ANY img tag referencing logo-nextiweb-dark.png NOT already in <picture>
  // Strategy: find <picture> blocks first, leave them alone; wrap bare <img> tags
  return content.replace(
    /(?<!<picture[^>]*>\s*<source[^>]*>\s*)(<img\s[^>]*logo-nextiweb-dark\.png[^>]*>)(?!\s*<\/picture>)/g,
    (match, imgTag) => {
      // Already inside <picture>? skip
      return `<picture>\n          <source srcset="/assets/img/logo/logo-nextiweb-dark.webp" type="image/webp">\n          ${imgTag}\n        </picture>`;
    }
  );
}

function addLazyLoadingToImages(content) {
  // Add loading="lazy" to all <img> that:
  //  - do NOT have loading= already
  //  - are NOT the logo (logo already has loading="eager")
  //  - are NOT a hero image
  return content.replace(
    /<img\s([^>]*?)>/g,
    (match, attrs) => {
      if (/loading=/.test(attrs)) return match; // already has loading attr
      if (/logo-nextiweb/.test(attrs)) return match; // logo handled separately
      if (/hero-agence/.test(attrs)) return match; // hero handled separately
      return `<img ${attrs.trimEnd()} loading="lazy">`;
    }
  );
}

function addDeferToScripts(content) {
  // Add defer to external script tags that:
  // - have a src= attribute (external JS)
  // - are NOT GTM (already async)
  // - are NOT already defer or async
  return content.replace(
    /<script\s([^>]*?src=[^>]*?)>/g,
    (match, attrs) => {
      if (/defer/.test(attrs) || /async/.test(attrs)) return match; // already optimized
      if (/googletagmanager/.test(attrs)) return match; // GTM skip
      return `<script ${attrs.trimEnd()} defer>`;
    }
  );
}

function addPreloadHints(content) {
  // Add preload for logo WebP in <head> if not already present
  if (content.includes('preload') && content.includes('logo-nextiweb-dark.webp')) return content;
  if (!content.includes('logo-nextiweb-dark')) return content;

  const preloadTag = `  <link rel="preload" href="/assets/img/logo/logo-nextiweb-dark.webp" as="image" type="image/webp" fetchpriority="high">`;

  // Insert after <meta charset line
  return content.replace(
    /(<meta charset[^>]*>)/,
    `$1\n${preloadTag}`
  );
}

// ─── Main ─────────────────────────────────────────────────────────────────────

const htmlFiles = getAllHtmlFiles(BASE);
let updated = 0, skipped = 0;

for (const file of htmlFiles) {
  let content = fs.readFileSync(file, 'utf8');
  const original = content;

  // 1. Wrap logo in <picture> for WebP
  content = wrapLogoInPicture(content);

  // 2. Add loading="lazy" to body images
  content = addLazyLoadingToImages(content);

  // 3. Add defer to external scripts
  content = addDeferToScripts(content);

  // 4. Preload logo WebP
  content = addPreloadHints(content);

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    updated++;
    console.log('OK:', path.relative(BASE, file));
  } else {
    skipped++;
  }
}

console.log(`\nDone: ${updated} files updated, ${skipped} unchanged.`);
