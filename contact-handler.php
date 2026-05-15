<?php
require_once __DIR__ . '/mail-config.php';
require_once __DIR__ . '/smtp-mailer.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /contact.html');
    exit;
}

// Honeypot 1 : bot-field
if (!empty($_POST['bot-field'])) {
    header('Location: /merci.html');
    exit;
}

// Honeypot 2 : website_confirm doit rester vide
if (!empty($_POST['website_confirm'])) {
    header('Location: /merci.html');
    exit;
}

// Anti-spam : vérification du temps (minimum 5 secondes, max 2h)
$form_ts = intval($_POST['form_ts'] ?? 0);
$elapsed = ($form_ts > 0) ? (time() - $form_ts) : 999;
if ($elapsed < 5 || $elapsed > 7200) {
    header('Location: /merci.html');
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
    header('Location: /contact.html?erreur=1');
    exit;
}

// Anti-spam : détection de contenu suspect (liens dans les détails)
$details_raw = trim($_POST['details'] ?? '');
$spam_score = 0;
if (preg_match('/https?:\/\//i', $details_raw)) $spam_score++;
if (preg_match('/https?:\/\//i', $_POST['entreprise'] ?? '')) $spam_score++;
if (preg_match('/(ranking|seo service|package|pricing|we can help|reply yes)/i', $details_raw)) $spam_score++;
if ($spam_score >= 2) {
    header('Location: /merci.html'); // Rediriger silencieusement sans envoyer l'email
    exit;
}

$subject = "Nouveau audit gratuit — $prenom ($entreprise)";
$body    = "Prénom     : $prenom\n"
         . "Entreprise : $entreprise\n"
         . "Courriel   : $email\n"
         . "Site       : " . ($site ?: 'aucun') . "\n"
         . "Projet     : $projet\n"
         . "Détails    : " . ($details ?: 'aucun') . "\n";

try {
    smtp_send(MAIL_TO, $subject, $body, $email);
} catch (Exception $e) {
    // Envoi échoué — on redirige quand même vers merci.html
    // L'erreur est ignorée silencieusement pour ne pas bloquer l'utilisateur
}

// HubSpot CRM — enregistrement du contact (Forms API, aucune clé requise)
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
        'pageUri' => 'https://nextiweb.ca/contact.html',
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

header('Location: /merci.html');
exit;
