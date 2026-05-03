<?php
// ── Configuration SMTP Hostinger ──────────────────────────────────────────
// IMPORTANT : modifier ce fichier DIRECTEMENT sur Hostinger (File Manager)
// Ne jamais committer le vrai mot de passe dans git.
// ──────────────────────────────────────────────────────────────────────────

define('SMTP_HOST', 'smtp.hostinger.com');
define('SMTP_PORT', 465);
define('SMTP_USER', 'contact@nextiweb.ca');
define('SMTP_PASS', 'VOTRE_MOT_DE_PASSE_ICI');   // ← changer ici sur le serveur
define('MAIL_FROM', 'contact@nextiweb.ca');
define('MAIL_TO',   'contact@nextiweb.ca');
