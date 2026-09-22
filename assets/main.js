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
      var sec = doc.getElementById("contact"); if (sec) sec.scrollIntoView({ block: "start" });
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

/* ---------- V2 : animations ---------- */
(function () {
  "use strict";
  var doc = document, html = doc.documentElement;
  html.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Apparition au défilement */
  var targets = doc.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    targets.forEach(function (t) { io.observe(t); });
  } else { targets.forEach(function (t) { t.classList.add("in"); }); }

  /* En-tête au défilement */
  var head = doc.querySelector(".site-head");
  function onScroll() { if (head) head.classList.toggle("scrolled", window.scrollY > 24); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* Diaporama du hero */
  var slides = doc.querySelectorAll("#hero-slides .slide"), dots = doc.querySelectorAll("#hero-dots button");
  if (slides.length > 1) {
    var cur = 0, timer = null;
    function show(i) {
      slides[cur].classList.remove("is-active"); if (dots[cur]) dots[cur].removeAttribute("aria-current");
      cur = (i + slides.length) % slides.length;
      slides[cur].classList.add("is-active"); if (dots[cur]) dots[cur].setAttribute("aria-current", "true");
    }
    function play() { if (!reduce && !timer) timer = setInterval(function () { show(cur + 1); }, 6000); }
    function stop() { clearInterval(timer); timer = null; }
    dots.forEach(function (d, i) { d.addEventListener("click", function () { stop(); show(i); play(); }); });
    doc.addEventListener("visibilitychange", function () { doc.hidden ? stop() : play(); });
    play();
  }

  /* Compteurs */
  var counters = doc.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return; io2.unobserve(e.target);
        var end = parseFloat(e.target.getAttribute("data-count")), t0 = null;
        if (reduce) { e.target.textContent = end; return; }
        function step(ts) { if (!t0) t0 = ts; var p = Math.min((ts - t0) / 1400, 1); e.target.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (c) { io2.observe(c); });
  }
})();
