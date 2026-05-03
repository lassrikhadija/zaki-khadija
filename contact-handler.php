<?php
require_once __DIR__ . '/mail-config.php';
require_once __DIR__ . '/smtp-mailer.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /contact.html');
    exit;
}

if (!empty($_POST['bot-field'])) {
    header('Location: /merci.html');
    exit;
}

$prenom     = htmlspecialchars(trim($_POST['prenom']     ?? ''));
$entreprise = htmlspecialchars(trim($_POST['entreprise'] ?? ''));
$email      = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$site       = htmlspecialchars(trim($_POST['site']       ?? ''));
$objectif   = htmlspecialchars(trim($_POST['objectif']   ?? ''));
$details    = htmlspecialchars(trim($_POST['details']    ?? ''));

if (empty($prenom) || empty($entreprise) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($objectif)) {
    header('Location: /contact.html?erreur=1');
    exit;
}

$subject = "Nouveau audit gratuit — $prenom ($entreprise)";
$body    = "Prénom     : $prenom\n"
         . "Entreprise : $entreprise\n"
         . "Courriel   : $email\n"
         . "Site       : " . ($site ?: 'aucun') . "\n"
         . "Objectif   : $objectif\n"
         . "Détails    : " . ($details ?: 'aucun') . "\n";

smtp_send(MAIL_TO, $subject, $body, $email);

header('Location: /merci.html');
exit;
