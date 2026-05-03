<?php
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /en/question.html');
    exit;
}

// Honeypot anti-spam
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

$to      = 'contact@nextiweb.ca';
$subject = "=?UTF-8?B?" . base64_encode("New question — $prenom") . "?=";
$body    = "First name : $prenom\n"
         . "Email      : $email\n"
         . "Question   : $question\n";

$headers  = "From: noreply@nextiweb.ca\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

mail($to, $subject, $body, $headers);

header('Location: /en/merci.html');
exit;
