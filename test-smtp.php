<?php
// Script de diagnostic SMTP — À SUPPRIMER après test
// Accès : https://nextiweb.ca/test-smtp.php?token=nxw2026

if (($_GET['token'] ?? '') !== 'nxw2026') { http_response_code(403); exit('Accès refusé'); }

require_once __DIR__ . '/mail-config.php';
require_once __DIR__ . '/smtp-mailer.php';

echo "<pre>\n";
echo "=== Diagnostic SMTP NEXTIWEB ===\n\n";
echo "SMTP_HOST : " . SMTP_HOST . "\n";
echo "SMTP_PORT : " . SMTP_PORT . "\n";
echo "SMTP_USER : " . SMTP_USER . "\n";
echo "SMTP_PASS : " . (SMTP_PASS !== 'VOTRE_MOT_DE_PASSE_ICI' ? '*** défini (' . strlen(SMTP_PASS) . ' chars) ***' : '⚠️ PLACEHOLDER NON REMPLACÉ') . "\n";
echo "MAIL_TO   : " . MAIL_TO . "\n\n";

echo "Test connexion SSL...\n";
$ctx = stream_context_create(['ssl' => ['verify_peer' => true, 'verify_peer_name' => true, 'allow_self_signed' => false]]);
$sock = @stream_socket_client("ssl://" . SMTP_HOST . ":" . SMTP_PORT, $errno, $errstr, 10, STREAM_CLIENT_CONNECT, $ctx);

if (!$sock) {
    echo "❌ Connexion échouée : [$errno] $errstr\n";
    echo "\nSolution possible : vérifier que le port 465 est ouvert sur Hostinger.\n";
} else {
    echo "✅ Connexion SSL OK\n\n";
    fclose($sock);

    echo "Test envoi email...\n";
    try {
        $result = smtp_send(MAIL_TO, 'TEST SMTP — nextiweb.ca', "Test de diagnostic envoyé le " . date('Y-m-d H:i:s') . "\n\nSi vous recevez ce message, le SMTP fonctionne.", SMTP_USER);
        if ($result) {
            echo "✅ Email envoyé avec succès à " . MAIL_TO . "\n";
        } else {
            echo "❌ smtp_send() a retourné false (authentification ou envoi échoué)\n";
        }
    } catch (Exception $e) {
        echo "❌ Exception : " . $e->getMessage() . "\n";
    }
}

echo "\n=== PHP Info ===\n";
echo "PHP version : " . PHP_VERSION . "\n";
echo "PHP_INT_MAX : " . PHP_INT_MAX . " (" . (PHP_INT_SIZE === 8 ? '64-bit ✅' : '32-bit ⚠️') . ")\n";
echo "cURL activé : " . (function_exists('curl_init') ? '✅ oui' : '❌ non') . "\n";
echo "time()      : " . time() . "\n";
echo "</pre>";
