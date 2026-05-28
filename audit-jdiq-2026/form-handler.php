<?php
require_once dirname(__DIR__) . '/mail-config.php';
require_once dirname(__DIR__) . '/smtp-mailer.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /audit-jdiq-2026/');
    exit;
}

// Honeypot 1 : website_url_fake doit rester vide
if (!empty($_POST['website_url_fake'])) {
    header('Location: /audit-jdiq-2026/merci.html');
    exit;
}

// Honeypot 2 : phone_confirm doit rester vide
if (!empty($_POST['phone_confirm'])) {
    header('Location: /audit-jdiq-2026/merci.html');
    exit;
}

// Anti-spam : vérification du temps (minimum 5 secondes, max 2h)
$form_ts = intval($_POST['form_ts'] ?? 0);
$elapsed = ($form_ts > 0) ? (time() - $form_ts) : 999;
if ($elapsed < 5 || $elapsed > 7200) {
    header('Location: /audit-jdiq-2026/merci.html');
    exit;
}

// Collecte et nettoyage des champs
$clinic_name  = htmlspecialchars(trim($_POST['clinic_name']  ?? ''));
$full_name    = htmlspecialchars(trim($_POST['full_name']    ?? ''));
$email        = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$site_url     = htmlspecialchars(trim($_POST['site_url']     ?? ''));
$phone        = htmlspecialchars(trim($_POST['phone']        ?? ''));
$utm_source   = htmlspecialchars(trim($_POST['utm_source']   ?? ''));
$utm_medium   = htmlspecialchars(trim($_POST['utm_medium']   ?? ''));
$utm_campaign = htmlspecialchars(trim($_POST['utm_campaign'] ?? ''));
$utm_content  = htmlspecialchars(trim($_POST['utm_content']  ?? ''));

// Validation des champs obligatoires (site_url optionnel — dentiste sans site = lead création)
if (empty($clinic_name) || empty($full_name) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    header('Location: /audit-jdiq-2026/?erreur=1');
    exit;
}

// Préparation du courriel SMTP
$subject = "[JDIQ 2026] Demande d'audit — {$clinic_name}";
$body    = "Clinique     : {$clinic_name}\n"
         . "Nom complet  : {$full_name}\n"
         . "Courriel     : {$email}\n"
         . "Site web     : " . ($site_url ?: 'aucun') . "\n"
         . "Téléphone    : " . ($phone ?: 'aucun') . "\n"
         . "\n"
         . "--- UTM ---\n"
         . "Source       : " . ($utm_source   ?: 'aucun') . "\n"
         . "Medium       : " . ($utm_medium   ?: 'aucun') . "\n"
         . "Campaign     : " . ($utm_campaign ?: 'aucun') . "\n"
         . "Content      : " . ($utm_content  ?: 'aucun') . "\n"
         . "\n"
         . "Campagne     : JDIQ 2026 — Palais des congrès de Montréal\n";

try {
    smtp_send(MAIL_TO, $subject, $body, $email);
    // Log succès temporaire pour diagnostic
    $log_ok = date('Y-m-d H:i:s') . ' | SMTP OK | to=' . MAIL_TO . ' | from=' . $email . ' | clinic=' . $clinic_name . "\n";
    file_put_contents(dirname(__DIR__) . '/smtp-jdiq-debug.log', $log_ok, FILE_APPEND);
} catch (Exception $e) {
    // Log erreur temporaire pour diagnostic
    $log_err = date('Y-m-d H:i:s') . ' | SMTP ERROR | to=' . MAIL_TO . ' | ' . $e->getMessage() . "\n";
    file_put_contents(dirname(__DIR__) . '/smtp-jdiq-debug.log', $log_err, FILE_APPEND);
}

// HubSpot CRM — enregistrement du contact (Forms API)
// Split full_name en firstname / lastname sur le premier espace
$name_parts = explode(' ', trim($_POST['full_name'] ?? ''), 2);
$firstname  = $name_parts[0] ?? '';
$lastname   = $name_parts[1] ?? '';

$hs_data = json_encode([
    'fields' => [
        ['name' => 'firstname',    'value' => $firstname],
        ['name' => 'lastname',     'value' => $lastname],
        ['name' => 'company',      'value' => trim($_POST['clinic_name'] ?? '')],
        ['name' => 'email',        'value' => trim($_POST['email']       ?? '')],
        ['name' => 'website',      'value' => trim($_POST['site_url']    ?? '')],
        ['name' => 'phone',        'value' => trim($_POST['phone']       ?? '')],
        ['name' => 'jdiq_source',  'value' => 'JDIQ 2026'],
        ['name' => 'message',      'value' => 'Demande d\'audit via campagne propulso JDIQ 2026'],
    ],
    'context' => array_filter([
        'pageUri' => 'https://nextiweb.ca/audit-jdiq-2026/',
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

header('Location: /audit-jdiq-2026/merci.html');
exit;
