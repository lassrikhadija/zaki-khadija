<?php
// ── Configuration SMTP Hostinger ──────────────────────────────────────────
// Le mot de passe NE doit PAS être ici (git pull l'écraserait à chaque déploiement).
// Il est lu depuis : 1) la variable d'env SMTP_PASS, sinon 2) le fichier non versionné
// smtp-pass.php (à créer une seule fois sur le serveur, jamais touché par git) :
//     <?php return 'LE_VRAI_MOT_DE_PASSE';
// ──────────────────────────────────────────────────────────────────────────

define('SMTP_HOST', 'smtp.hostinger.com');
define('SMTP_PORT', 465);
define('SMTP_USER', 'contact@nextiweb.ca');
// Mot de passe : env, sinon fichier non versionné smtp-pass.php → jamais écrasé par git
define('SMTP_PASS', getenv('SMTP_PASS') ?: (is_file(__DIR__ . '/smtp-pass.php') ? trim((string) (include __DIR__ . '/smtp-pass.php')) : ''));
define('MAIL_FROM', 'contact@nextiweb.ca');
define('MAIL_TO',   'contact@nextiweb.ca');
