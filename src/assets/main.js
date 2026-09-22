/* Eden Corporate Mobility — scripts (aucune dépendance) */
(function () {
  "use strict";
  var doc = document, html = doc.documentElement, lang = html.getAttribute("data-lang") || "fr";

  /* ---------- Menu mobile ---------- */
  var toggle = doc.getElementById("nav-toggle"), nav = doc.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); toggle.focus(); }
    });
  }

  /* ---------- Formulaire de contact ---------- */
  var form = doc.getElementById("contact-form"), ok = doc.getElementById("form-ok");
  if (form) {
    if (/[?&]sent=1/.test(location.search) && ok) {
      ok.hidden = false; form.querySelector(".form-grid").hidden = true; form.querySelector("button[type=submit]").hidden = true;
      ok.setAttribute("tabindex", "-1"); ok.focus();
    }
    form.addEventListener("submit", function (e) {
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (el) {
        var f = el.closest(".field"), bad = !el.value.trim() || (el.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value));
        if (f) f.classList.toggle("invalid", bad);
        if (bad && valid) { el.focus(); valid = false; }
      });
      if (!valid) { e.preventDefault(); }
    });
  }

  /* ---------- Mesure d'audience (uniquement avec consentement) ---------- */
  var gaId = html.getAttribute("data-ga"), consent = doc.getElementById("consent");
  var KEY = "ecm-consent", SIX_MONTHS = 1000 * 60 * 60 * 24 * 182;
  function readChoice() {
    try { var v = JSON.parse(localStorage.getItem(KEY) || "null"); if (v && Date.now() - v.t < SIX_MONTHS) return v.c; } catch (err) {}
    return null;
  }
  function saveChoice(c) { try { localStorage.setItem(KEY, JSON.stringify({ c: c, t: Date.now() })); } catch (err) {} }
  function loadGA() {
    if (!gaId) return;
    var s = doc.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(gaId); doc.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    gtag("js", new Date()); gtag("config", gaId, { anonymize_ip: true });
    doc.querySelectorAll('a[href^="tel:"]').forEach(function (a) { a.addEventListener("click", function () { gtag("event", "call_click", { language: lang }); }); });
  }
  if (gaId && consent) {
    var choice = readChoice();
    if (choice === "allow") loadGA();
    else if (choice === null) {
      consent.hidden = false;
      consent.querySelectorAll("[data-consent]").forEach(function (b) {
        b.addEventListener("click", function () {
          var c = b.getAttribute("data-consent"); saveChoice(c); consent.hidden = true; if (c === "allow") loadGA();
        });
      });
    }
  }
})();
