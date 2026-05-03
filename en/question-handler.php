<?php
require_once dirname(__DIR__) . '/mail-config.php';
require_once dirname(__DIR__) . '/smtp-mailer.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /en/question.html');
    exit;
}

if (!empty($_POST['bot-field'])) {
    header('Location: /en/merci.html');
    exit;
}

$prenom   = htmlspecialchars(trim($_POST['prenom']   ?? ''));
$email    = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$question = htmlspecialchars(trim($_POST['question'] ?? ''));

if (empty($prenom) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($question)) {
    header('Location: /en/question.html?error=1');
    exit;
}

$subject = "New question — $prenom";
$body    = "First name : $prenom\n"
         . "Email      : $email\n"
         . "Question   : $question\n";

smtp_send(MAIL_TO, $subject, $body, $email);

header('Location: /en/merci.html');
exit;
