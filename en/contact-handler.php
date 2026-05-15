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

// Anti-spam : time check (minimum 5 seconds, max 2h)
$form_ts = intval($_POST['form_ts'] ?? 0);
$elapsed = ($form_ts > 0) ? (time() - $form_ts) : 999;
if ($elapsed < 5 || $elapsed > 7200) {
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

// HubSpot CRM — contact registration (Forms API, no key required)
$hs_raw_projet = isset($_POST['projet']) ? implode(', ', (array)$_POST['projet']) : '';
$hs_data = json_encode([
    'fields' => [
        ['name' => 'firstname',          'value' => trim($_POST['prenom']     ?? '')],
        ['name' => 'company',            'value' => trim($_POST['entreprise'] ?? '')],
        ['name' => 'email',              'value' => trim($_POST['email']      ?? '')],
        ['name' => 'website',            'value' => trim($_POST['site']       ?? '')],
        ['name' => 'type_de_projet',     'value' => $hs_raw_projet],
        ['name' => 'message',            'value' => trim($_POST['details']    ?? '')],
        ['name' => 'consentement_loi25', 'value' => !empty($_POST['consent']) ? 'true' : 'false'],
    ],
    'context' => array_filter([
        'pageUri' => 'https://nextiweb.ca/en/contact.html',
        'hutk'    => $_COOKIE['hubspotutk'] ?? '',
    ]),
]);
$ch = curl_init('https://api.hsforms.com/submissions/v3/integration/submit/342806224/d115bad7-bd97-43c0-8845-fcdd16c47e56');
curl_setopt($ch, CURLOPT_POST,           true);
curl_setopt($ch, CURLOPT_POSTFIELDS,     $hs_data);
curl_setopt($ch, CURLOPT_HTTPHEADER,     ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT,        5);
curl_exec($ch);
curl_close($ch);

header('Location: /en/merci.html');
exit;
