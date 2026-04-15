const fs = require('fs');
const path = require('path');

const GTM_HEAD = `  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-TS5WZHQ6');</script>
  <!-- End Google Tag Manager -->`;

const GTM_BODY = `  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TS5WZHQ6"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->`;

function getAllHtmlFiles(dir, files = []) {
  const items = fs.readdirSync(dir);
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory()) {
      if (!['partials', 'node_modules', '.git'].includes(item)) {
        getAllHtmlFiles(fullPath, files);
      }
    } else if (item.endsWith('.html') && item !== 'assurance-bar-new.html') {
      files.push(fullPath);
    }
  }
  return files;
}

const baseDir = __dirname;
const htmlFiles = getAllHtmlFiles(baseDir);
let updated = 0, skipped = 0;

for (const file of htmlFiles) {
  let content = fs.readFileSync(file, 'utf8');

  // Déjà présent ?
  if (content.includes('GTM-TS5WZHQ6')) {
    skipped++;
    continue;
  }

  // Injecter dans <head> après <meta charset ou après <head>
  if (content.includes('<meta charset')) {
    content = content.replace(/(<meta charset[^>]*>)/, `$1\n${GTM_HEAD}`);
  } else if (content.includes('<head>')) {
    content = content.replace('<head>', `<head>\n${GTM_HEAD}`);
  }

  // Injecter après <body ...>
  content = content.replace(/(<body[^>]*>)/, `$1\n${GTM_BODY}`);

  fs.writeFileSync(file, content, 'utf8');
  updated++;
  console.log('✅', path.relative(baseDir, file));
}

console.log(`\nTerminé : ${updated} fichiers mis à jour, ${skipped} déjà configurés.`);
