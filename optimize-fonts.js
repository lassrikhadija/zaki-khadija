const fs = require('fs');
const path = require('path');

const BASE = __dirname;

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

// Replace blocking Google Font link with async loading pattern
const OLD_FONT = `<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">`;

const NEW_FONT = `<link rel="preload" href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet"></noscript>`;

const htmlFiles = getAllHtmlFiles(BASE);
let updated = 0, skipped = 0;

for (const file of htmlFiles) {
  let content = fs.readFileSync(file, 'utf8');
  if (!content.includes(OLD_FONT)) { skipped++; continue; }

  content = content.replace(OLD_FONT, NEW_FONT);
  fs.writeFileSync(file, content, 'utf8');
  updated++;
  console.log('OK:', path.relative(BASE, file));
}

console.log(`\nDone: ${updated} files updated, ${skipped} unchanged.`);
