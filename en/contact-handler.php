<?php
require_once dirname(__DIR__) . '/mail-config.php';
require_once dirname(__DIR__) . '/smtp-mailer.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /en/contact.html');
    exit;
}

// Honeypot 1 : bot-field
if (!empty($_POST['bot-field'])) {
    header('Location: /en/merci.html');
    exit;
}

// Honeypot 2 : website_confirm doit rester vide
if (!empty($_POST['website_confirm'])) {
    header('Location: /en/merci.html');
    exit;
}

// Anti-spam : vérification du temps (minimum 5 secondes)
$form_ts = intval($_POST['form_ts'] ?? 0);
if ($form_ts === 0 || (time() * 1000 - $form_ts) < 5000) {
    header('Location: /en/merci.html');
    exit;
}

$prenom     = htmlspecialchars(trim($_POST['prenom']     ?? ''));
$entreprise = htmlspecialchars(trim($_POST['entreprise'] ?? ''));
$email      = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$site       = htmlspecialchars(trim($_POST['site']       ?? ''));
$projet     = isset($_POST['projet']) ? implode(', ', (array)$_POST['projet']) : '';
$projet     = htmlspecialchars(trim($projet));
$details    = htmlspecialchars(trim($_POST['details']    ?? ''));

if (empty($prenom) || empty($entreprise) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($projet)) {
    header('Location: /en/contact.html?error=1');
    exit;
}

// Anti-spam : détection de contenu suspect
$details_raw = trim($_POST['details'] ?? '');
$spam_score = 0;
if (preg_match('/https?:\/\//i', $details_raw)) $spam_score++;
if (preg_match('/https?:\/\//i', $_POST['entreprise'] ?? '')) $spam_score++;
if (preg_match('/(ranking|seo service|package|pricing|we can help|reply yes)/i', $details_raw)) $spam_score++;
if ($spam_score >= 2) {
    header('Location: /en/merci.html');
    exit;
}

$subject = "New free audit — $prenom ($entreprise)";
$body    = "First name : $prenom\n"
         . "Company    : $entreprise\n"
         . "Email      : $email\n"
         . "Website    : " . ($site ?: 'none') . "\n"
         . "Project    : $projet\n"
         . "Details    : " . ($details ?: 'none') . "\n";

try {
    smtp_send(MAIL_TO, $subject, $body, $email);
} catch (Exception $e) {
    // Silent fail — redirect anyway
}

header('Location: /en/merci.html');
exit;
