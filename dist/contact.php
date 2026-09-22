<?php
// Eden Corporate Mobility — traitement du formulaire de contact (Hostinger / PHP 8)
// Configuration :
$to      = "contact@edencorporatemobility.com";   // À CONFIRMER : adresse qui reçoit les demandes
$from    = "no-reply@edencorporatemobility.com";  // Adresse expéditeur (doit exister sur le domaine pour éviter le spam)
$subjectPrefix = "[Site web] ";

function clean($v) { return trim(strip_tags((string)$v)); }
if ($_SERVER["REQUEST_METHOD"] !== "POST") { header("Location: /", true, 302); exit; }

$lang    = ($_POST["lang"] ?? "fr") === "en" ? "en" : "fr";
$back    = $lang === "en" ? "/en/contact/" : "/contact/";
if (!empty($_POST["website"])) { header("Location: $back?sent=1", true, 303); exit; } // pot de miel anti-spam

$name    = clean($_POST["name"] ?? "");
$company = clean($_POST["company"] ?? "");
$role    = clean($_POST["role"] ?? "");
$email   = clean($_POST["email"] ?? "");
$phone   = clean($_POST["phone"] ?? "");
$message = clean($_POST["message"] ?? "");

if ($name === "" || $company === "" || $message === "" || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  header("Location: $back?error=1", true, 303); exit;
}

$subject = $subjectPrefix . ($lang === "en" ? "New request from " : "Nouvelle demande de ") . $company;
$body = "Nom : $name\nEntreprise : $company\nFonction : $role\nEmail : $email\nTéléphone : $phone\nLangue : $lang\n\nMessage :\n$message\n";
$headers = "From: Eden Corporate Mobility <$from>\r\nReply-To: $email\r\nContent-Type: text/plain; charset=UTF-8\r\n";

@mail($to, "=?UTF-8?B?" . base64_encode($subject) . "?=", $body, $headers);
header("Location: $back?sent=1", true, 303);
exit;
