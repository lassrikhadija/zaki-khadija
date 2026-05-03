<?php
function smtp_send(string $to, string $subject, string $body, string $reply_to = ''): bool {
    $host = SMTP_HOST;
    $port = SMTP_PORT;
    $user = SMTP_USER;
    $pass = SMTP_PASS;
    $from = MAIL_FROM;

    $ctx = stream_context_create(['ssl' => [
        'verify_peer'       => true,
        'verify_peer_name'  => true,
        'allow_self_signed' => false,
    ]]);

    $sock = @stream_socket_client("ssl://{$host}:{$port}", $errno, $errstr, 15, STREAM_CLIENT_CONNECT, $ctx);
    if (!$sock) return false;

    $r = fn() => fgets($sock, 512);
    $w = fn(string $s) => fputs($sock, $s . "\r\n");

    $r(); // 220 greeting

    $w("EHLO nextiweb.ca");
    while ($line = $r()) { if (isset($line[3]) && $line[3] === ' ') break; }

    $w("AUTH LOGIN");
    $r(); // 334

    $w(base64_encode($user));
    $r(); // 334

    $w(base64_encode($pass));
    $auth = $r();
    if (substr(trim($auth), 0, 3) !== '235') { fclose($sock); return false; }

    $w("MAIL FROM:<{$from}>");  $r();
    $w("RCPT TO:<{$to}>");       $r();
    $w("DATA");                  $r(); // 354

    $subj_encoded = "=?UTF-8?B?" . base64_encode($subject) . "?=";
    $msg  = "From: NEXTIWEB <{$from}>\r\n";
    $msg .= "To: {$to}\r\n";
    if ($reply_to) $msg .= "Reply-To: {$reply_to}\r\n";
    $msg .= "Subject: {$subj_encoded}\r\n";
    $msg .= "MIME-Version: 1.0\r\n";
    $msg .= "Content-Type: text/plain; charset=UTF-8\r\n";
    $msg .= "Content-Transfer-Encoding: 8bit\r\n";
    $msg .= "\r\n" . $body . "\r\n.\r\n";

    fputs($sock, $msg);
    $r();

    $w("QUIT");
    fclose($sock);
    return true;
}
