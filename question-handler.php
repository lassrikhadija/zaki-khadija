<?php
require_once __DIR__ . '/mail-config.php';
require_once __DIR__ . '/smtp-mailer.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /question.html');
    exit;
}

if (!empty($_POST['bot-field'])) {
    header('Location: /merci.html');
    exit;
}

$prenom   = htmlspecialchars(trim($_POST['prenom']   ?? ''));
$email    = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$question = htmlspecialchars(trim($_POST['question'] ?? ''));

if (empty($prenom) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($question)) {
    header('Location: /question.html?erreur=1');
    exit;
}

$subject = "Nouvelle question — $prenom";
$body    = "Prénom   : $prenom\n"
         . "Courriel : $email\n"
         . "Question : $question\n";

smtp_send(MAIL_TO, $subject, $body, $email);

header('Location: /merci.html');
exit;
