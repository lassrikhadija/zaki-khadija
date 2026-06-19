<?php
/**
 * Endpoint WebMCP — soumission d'un lead par un agent IA.
 * Réutilise le mailer + HubSpot du site, mais répond en JSON (succès/échec)
 * pour que l'agent sache si la demande a abouti.
 */
require_once __DIR__ . '/mail-config.php';
require_once __DIR__ . '/smtp-mailer.php';

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

function nw_out($ok, $msg, $code = 200) {
    http_response_code($code);
    echo json_encode(['success' => $ok, 'message' => $msg], JSON_UNESCAPED_UNICODE);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    nw_out(false, 'Méthode non autorisée.', 405);
}

// Corps JSON (repli sur form-encoded)
$raw = file_get_contents('php://input');
$in  = json_decode($raw, true);
if (!is_array($in)) { $in = $_POST; }

$prenom     = trim((string)($in['prenom']     ?? ''));
$email      = trim((string)($in['email']      ?? ''));
$entreprise = trim((string)($in['entreprise'] ?? ''));
$secteur    = trim((string)($in['secteur']    ?? ''));
$details    = trim((string)($in['details']    ?? ($in['message'] ?? '')));

// Validation
if ($prenom === '' || $entreprise === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    nw_out(false, "Champs requis manquants ou courriel invalide (prénom, entreprise, courriel).", 400);
}

// Anti-spam : contenu suspect (même logique que le formulaire)
$spam = 0;
if (preg_match('/https?:\/\//i', $details))    { $spam++; }
if (preg_match('/https?:\/\//i', $entreprise)) { $spam++; }
if (preg_match('/(ranking|seo service|package|pricing|we can help|reply yes)/i', $details)) { $spam++; }
if ($spam >= 2) {
    nw_out(false, "Demande non transmise (contenu signalé). Écrivez directement à contact@nextiweb.ca.", 422);
}

// Anti-abus : limite simple par IP (1 / 20 s), fail-open si écriture impossible
$ip   = $_SERVER['REMOTE_ADDR'] ?? 'x';
$lock = sys_get_temp_dir() . '/nw_mcp_' . md5($ip);
$now  = time();
if (is_file($lock) && ($now - (int)@file_get_contents($lock)) < 20) {
    nw_out(false, "Trop de demandes rapprochées. Réessayez dans un instant.", 429);
}
@file_put_contents($lock, (string)$now);

// Longueurs raisonnables
$prenom     = mb_substr($prenom, 0, 100);
$entreprise = mb_substr($entreprise, 0, 150);
$secteur    = mb_substr($secteur, 0, 100);
$details    = mb_substr($details, 0, 2000);
$projet     = $secteur !== '' ? "Audit gratuit — secteur : $secteur" : "Audit gratuit (demande via agent IA)";

// Courriel (même mécanisme éprouvé que le formulaire de contact)
$subject = "Lead via agent IA (WebMCP) — $prenom ($entreprise)";
$body    = "Source     : WebMCP (agent IA)\n"
         . "Prénom     : $prenom\n"
         . "Entreprise : $entreprise\n"
         . "Courriel   : $email\n"
         . "Secteur    : " . ($secteur !== '' ? $secteur : 'non précisé') . "\n"
         . "Détails    : " . ($details !== '' ? $details : 'aucun') . "\n";

$sent = false;
try { $sent = smtp_send(MAIL_TO, $subject, $body, $email); } catch (Exception $e) { $sent = false; }

// HubSpot CRM — réutilise l'intégration du formulaire.
// On évite le champ enum "type_de_projet" (rejet si valeur hors liste) : le secteur va dans "message".
// pageUri doit être une URL valide (un espace/parenthèses font rejeter la soumission).
$hs_message = $details;
if ($secteur !== '') { $hs_message = ($hs_message !== '' ? $hs_message . "\n" : '') . "Secteur : $secteur"; }
$hs_message = ($hs_message !== '' ? $hs_message . "\n" : '') . "Source : agent IA (WebMCP)";
$hs = json_encode([
    'fields' => [
        ['name' => 'firstname',          'value' => $prenom],
        ['name' => 'company',            'value' => $entreprise],
        ['name' => 'email',              'value' => $email],
        ['name' => 'message',            'value' => $hs_message],
        ['name' => 'consentement_loi25', 'value' => 'false'],
    ],
    'context' => ['pageUri' => 'https://nextiweb.ca/', 'pageName' => 'Demande via agent IA (WebMCP)'],
]);
$ch = curl_init('https://api.hsforms.com/submissions/v3/integration/submit/342806224/d115bad7-bd97-43c0-8845-fcdd16c47e56');
curl_setopt($ch, CURLOPT_POST,           true);
curl_setopt($ch, CURLOPT_POSTFIELDS,     $hs);
curl_setopt($ch, CURLOPT_HTTPHEADER,     ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT,        5);
$hs_resp = curl_exec($ch);
$hs_code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$ok  = $sent || ($hs_code >= 200 && $hs_code < 300);
$msg = $ok
    ? "Votre demande d'audit gratuit a bien été transmise à NEXTIWEB. L'équipe répond sous 24 h."
    : "L'envoi a échoué. Contactez NEXTIWEB directement : contact@nextiweb.ca / +1 514-791-0591.";
http_response_code(200);
echo json_encode(['success' => $ok, 'message' => $msg, '_diag' => ['mail' => $sent, 'hubspot' => $hs_code]], JSON_UNESCAPED_UNICODE);
exit;
