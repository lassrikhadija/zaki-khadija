<?php
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /en/contact.html');
    exit;
}

// Honeypot anti-spam
if (!empty($_POST['bot-field'])) {
    header('Location: /en/merci.html');
    exit;
}

$prenom     = htmlspecialchars(trim($_POST['prenom']     ?? ''));
$entreprise = htmlspecialchars(trim($_POST['entreprise'] ?? ''));
$email      = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$site       = htmlspecialchars(trim($_POST['site']       ?? ''));
$objectif   = htmlspecialchars(trim($_POST['objectif']   ?? ''));
$details    = htmlspecialchars(trim($_POST['details']    ?? ''));

if (empty($prenom) || empty($entreprise) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($objectif)) {
    header('Location: /en/contact.html?error=1');
    exit;
}

$to      = 'contact@nextiweb.ca';
$subject = "=?UTF-8?B?" . base64_encode("New free audit — $prenom ($entreprise)") . "?=";
$body    = "First name : $prenom\n"
         . "Company    : $entreprise\n"
         . "Email      : $email\n"
         . "Website    : " . ($site ?: 'none') . "\n"
         . "Goal       : $objectif\n"
         . "Details    : " . ($details ?: 'none') . "\n";

$headers  = "From: noreply@nextiweb.ca\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

mail($to, $subject, $body, $headers);

header('Location: /en/merci.html');
exit;
