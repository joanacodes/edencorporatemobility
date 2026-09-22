# -*- coding: utf-8 -*-
"""
Eden Corporate Mobility — générateur de site statique (FR / EN).
Usage : py build.py   →  régénère le site à la racine du dépôt (le dossier parent). GitHub Pages sert cette racine telle quelle.

Toutes les informations "à confirmer" sont centralisées dans SITE ci-dessous.
"""
import os, re, shutil, json, html, datetime, hashlib
from pathlib import Path
import content_fr, content_en, images

ROOT = Path(__file__).resolve().parent
DIST = ROOT.parent   # racine du dépôt

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION — À COMPLÉTER / CONFIRMER
# ─────────────────────────────────────────────────────────────────────────────
SITE = {
    "url": "https://edencorporatemobility.com",       # sans slash final. Choisir www ou non-www et s'y tenir.
    "name": "Eden Corporate Mobility",
    "phone_display": "+33 1 84 16 18 06",
    "phone_tel": "+33184161806",
    "whatsapp": "",                                     # ex. "33612345678" (sans +). Vide = bouton masqué.
    "email": "contact@edencorporatemobility.com",       # À CONFIRMER
    "form_endpoint": "https://formsubmit.co/contact@edencorporatemobility.com",  # FormSubmit : même email ; après activation, remplacer par l'alias https://formsubmit.co/el/xxxx
    "hours_fr": "Lundi–vendredi, 9h–18h (heure de Paris)",   # À CONFIRMER
    "hours_en": "Monday–Friday, 9am–6pm (Paris time, CET)",  # À CONFIRMER
    "address_lines": ["14 rue de Champigny", "94370 Sucy-en-Brie, France"],   # siège social (source : RNE / societe.com)
    "linkedin": "",                                     # ex. "https://www.linkedin.com/company/eden-corporate-mobility"
    "analytics_id": "",                                 # ex. "G-XXXXXXXXXX". Vide = aucun cookie, aucun bandeau.
    "legal": {                                          # Mentions légales (source : RNE / societe.com, 03/09/2026) — vérifier sur le Kbis
        "raison_sociale": "EDENEL PATRIMOINE GESTION RESEAUX & SERVICES (nom commercial : Eden Corporate Mobility)",
        "forme": "société par actions simplifiée au capital de 2 500 €",
        "siren": "104 632 591",
        "rcs": "RCS Créteil 104 632 591 — SIRET 104 632 591 00012 — code APE 6831Z",
        "tva": "FR62 104632591",
        "directeur": "Ayajénu Hounnou, Président (à confirmer)",
        "immatriculation": "Carte professionnelle (loi Hoguet) n° [à compléter], délivrée par la CCI [à compléter] — Garantie financière : [organisme, adresse, montant] — [Détention / non-détention de fonds]",
        "host": "Hostinger International Ltd, 61 Lordou Vironos Street, 6023 Larnaca, Chypre — hostinger.fr (à vérifier sur votre contrat)",
    },
    "stats": [],                                        # ex. [{"n": "120", "suffix": "+", "label_fr": "collaborateurs logés", "label_en": "employees housed"}] — vide = section masquée
    "terms": {                                          # CGV — À CONFIRMER (valeurs par défaut prudentes)
        "devis_validite": "30 jours",
        "acompte": "30 %",
        "delai_paiement": "30",
        "annulation_delai": "15 jours",
        "annulation_frais": "50 %",
        "assurance": "souscrite auprès de [assureur, n° de contrat]",
    },
    "year": datetime.date.today().year,
    "lastmod": datetime.date.today().isoformat(),
}

LANGS = {
    "fr": {"pages": content_fr.PAGES, "ui": content_fr.UI, "prefix": ""},
    "en": {"pages": content_en.PAGES, "ui": content_en.UI, "prefix": "en/"},
}

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def tokens(lang):
    t = {
        "name": SITE["name"], "phone": SITE["phone_display"], "email": SITE["email"], "url": SITE["url"],
        "hours": SITE["hours_fr"], "hours_en": SITE["hours_en"], "lastmod": SITE["lastmod"],
        "address": ", ".join(SITE["address_lines"]),
    }
    t.update(SITE["legal"]); t.update(SITE["terms"])
    if lang == "en":
        t["hours"] = SITE["hours_en"]
        # English wording for term defaults
        t["devis_validite"] = t["devis_validite"].replace("jours", "days")
        t["annulation_delai"] = t["annulation_delai"].replace("jours", "days")
    return t

def fill(s, lang):
    tk = tokens(lang)
    return re.sub(r"\{\{(\w+)\}\}", lambda m: tk.get(m.group(1), m.group(0)), s)

def esc(s):  # attribute-safe
    return html.escape(s or "", quote=True)

def url_for(lang, slug):
    p = LANGS[lang]["prefix"]
    if slug == "":
        return "/" + p
    return "/" + p + slug + "/"

def abs_url(lang, slug):
    return SITE["url"] + url_for(lang, slug)

def find_page(lang, key):
    for p in LANGS[lang]["pages"]:
        if p["key"] == key:
            return p
    raise KeyError(key)

def img_tag(file, lang, cls="", loading="lazy", extra=""):
    w, h = images.SIZE[file]
    return f'<img src="/assets/img/{file}" alt="{esc(images.ALT[lang].get(file, ""))}" width="{w}" height="{h}" loading="{loading}"{(" class=" + chr(34) + cls + chr(34)) if cls else ""}{extra}>'

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s or "")

ICONS = {
    "housing": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5M5 10v10h14V10M10 20v-6h4v6"/></svg>',
    "transport": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 16V9a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v7M4 16h16M6 16v3M18 16v3M4 12h16M8 8h8"/></svg>',
    "wellbeing": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21c-5-2.5-8-6-8-10a6 6 0 0 1 8-5.6A6 6 0 0 1 20 11c0 4-3 7.5-8 10z"/><path d="M12 8v6M9 11h6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v12H3zM3 7l9 6 9-6"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19.4L4 20z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 1a5 5 0 0 1-2-2l1-1-1-2z"/></svg>',
}

# ─────────────────────────────────────────────────────────────────────────────
# SECTION RENDERERS
# ─────────────────────────────────────────────────────────────────────────────
def r_heading(sec, level=2):
    h = sec.get("heading")
    return f"<h{level}>{h}</h{level}>" if h else ""

def r_prose(sec, lang):
    return f'<section class="sec prose"><div class="wrap narrow">{r_heading(sec)}{sec["html"]}</div></section>'

def r_features(sec, lang):
    items = ""
    for it in sec["items"]:
        icon = ICONS.get(it.get("icon", ""), "")
        link = f'<a class="more" href="{it["href"]}">{it["link"]}</a>' if it.get("href") else ""
        pic = f'<figure class="feature-img">{img_tag(it["img"], lang)}</figure>' if it.get("img") else ""
        items += f'<div class="feature">{pic}{("<span class=ico>"+icon+"</span>") if icon else ""}<h3>{it["title"]}</h3><p>{it["text"]}</p>{link}</div>'
    intro = f'<p class="lead">{sec["intro"]}</p>' if sec.get("intro") else ""
    return f'<section class="sec"><div class="wrap">{r_heading(sec)}{intro}<div class="features">{items}</div></div></section>'

def r_segments(sec, lang):
    rows = ""
    for it in sec["items"]:
        pic = f'<span class="seg-img">{img_tag(it["img"], lang)}</span>' if it.get("img") else ""
        rows += f'<li><a href="{it["href"]}">{pic}<span class="seg-title">{it["title"]}</span><span class="seg-text">{it["text"]}</span></a></li>'
    intro = f'<p class="lead">{sec["intro"]}</p>' if sec.get("intro") else ""
    return f'<section class="sec" id="{sec.get("id","")}"><div class="wrap">{r_heading(sec)}{intro}<ul class="segments{" has-img" if any(i.get("img") for i in sec["items"]) else ""}">{rows}</ul></div></section>'

def r_steps(sec, lang):
    rows = ""
    for i, it in enumerate(sec["items"], 1):
        rows += f'<li><span class="num" aria-hidden="true">{i}</span><div><h3>{it["title"]}</h3><p>{it["text"]}</p></div></li>'
    return f'<section class="sec sec-tint"><div class="wrap">{r_heading(sec)}<ol class="steps">{rows}</ol></div></section>'

def r_faq(sec, lang, page):
    rows = ""
    for it in sec["items"]:
        rows += f'<details class="faq"><summary>{it["q"]}</summary><div class="faq-a">{it["a"]}</div></details>'
    more = f'<p class="center"><a class="more" href="{sec["more_href"]}">{sec["more"]}</a></p>' if sec.get("more_href") else ""
    return f'<section class="sec"><div class="wrap narrow">{r_heading(sec)}{rows}{more}</div></section>'

def r_team(sec, lang):
    cards = ""
    for m in sec["members"]:
        ini = "".join(w[0] for w in m["name"].split()[:2])
        cards += f'<div class="member"><span class="mono" aria-hidden="true">{ini}</span><h3>{m["name"]}</h3><p class="role">{m["role"]}</p><p>{m["text"]}</p></div>'
    intro = f'<p class="lead">{sec["intro"]}</p>' if sec.get("intro") else ""
    return f'<section class="sec"><div class="wrap">{r_heading(sec)}{intro}<div class="team">{cards}</div></div></section>'

def r_quote(sec, lang):
    return f'<section class="sec sec-tint"><div class="wrap narrow"><figure class="quote"><blockquote>{sec["text"]}</blockquote><figcaption>{sec["author"]}{(" — "+sec["meta"]) if sec.get("meta") else ""}</figcaption></figure></div></section>'

def r_logos(sec, lang):
    names = "".join(f"<li>{n}</li>" for n in sec["names"])
    return f'<section class="sec logos"><div class="wrap"><p class="logos-h">{sec["heading"]}</p></div><div class="marquee"><ul>{names}</ul><ul aria-hidden="true">{names}</ul></div></section>'

def r_twocol(sec, lang):
    pic = f'<figure class="tc-img">{img_tag(sec["img"], lang)}</figure>' if sec.get("img") else ""
    return f'<section class="sec"><div class="wrap twocol"><div class="col-a"><h2>{sec["heading"]}</h2>{sec.get("aside","")}{pic}</div><div class="col-b">{sec["html"]}</div></div></section>'

def r_contact(sec, lang, page):
    ui = LANGS[lang]["ui"]
    wa = ""
    if SITE["whatsapp"]:
        wa = f'<a class="btn btn-ghost" href="https://wa.me/{SITE["whatsapp"]}" rel="noopener">{ICONS["whatsapp"]}WhatsApp</a>'
    f = sec["form"]
    fields = ""
    for fld in f["fields"]:
        req = " required" if fld.get("req") else ""
        req_mark = ' <span class="req" aria-hidden="true">*</span>' if fld.get("req") else ""
        if fld["type"] == "textarea":
            fields += f'<div class="field wide"><label for="f-{fld["name"]}">{fld["label"]}{req_mark}</label><textarea id="f-{fld["name"]}" name="{fld["name"]}" rows="5"{req}></textarea></div>'
        else:
            fields += f'<div class="field"><label for="f-{fld["name"]}">{fld["label"]}{req_mark}</label><input id="f-{fld["name"]}" name="{fld["name"]}" type="{fld["type"]}"{req} autocomplete="{fld.get("ac","on")}"></div>'
    return f'''
<section class="sec contact-sec" id="contact"><div class="wrap contact-grid">
  <div class="contact-side">
    <h2>{sec["heading"]}</h2>
    <p class="lead">{sec["intro"]}</p>
    <p class="big-phone"><a href="tel:{SITE["phone_tel"]}">{SITE["phone_display"]}</a></p>
    <p class="muted">{ui["hours"]}</p>
    <p class="btn-row"><a class="btn btn-primary" href="tel:{SITE["phone_tel"]}">{ICONS["phone"]}{ui["call"]}</a>{wa}</p>
    <p><a class="more" href="mailto:{SITE["email"]}">{SITE["email"]}</a></p>
    {sec.get("aside","")}
  </div>
  <form class="contact-form" method="post" action="{SITE["form_endpoint"]}" id="contact-form" novalidate>
    <h2 class="h3">{f["heading"]}</h2>
    <p class="muted">{f["intro"]}</p>
    <div class="form-ok" id="form-ok" hidden>{f["success"]}</div>
    <div class="form-grid">{fields}</div>
    <div class="hp" aria-hidden="true"><label>Website<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
    <input type="hidden" name="_subject" value="{f["subject"]}">
    <input type="hidden" name="_next" value="{abs_url(lang, page["slug"])}?sent=1#contact">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="Langue" value="{lang}">
    <p class="muted small">{f["privacy"]}</p>
    <button class="btn btn-primary" type="submit">{f["submit"]}</button>
  </form>
</div></section>'''

def r_cta(sec, lang):
    ui = LANGS[lang]["ui"]
    ctc = find_page(lang, "contact")
    return f'''
<section class="sec cta-band"><div class="wrap">
  <h2>{sec["heading"]}</h2>
  <p>{sec["text"]}</p>
  <p class="btn-row"><a class="btn btn-light" href="tel:{SITE["phone_tel"]}">{ICONS["phone"]}{ui["call_number"]}</a><a class="btn btn-outline" href="{url_for(lang, ctc["slug"])}">{ui["describe"]}</a></p>
  <p class="cta-hours">{ui["hours"]}</p>
</div></section>'''

def r_media(sec, lang):
    rows = ""
    for i, it in enumerate(sec["items"]):
        rev = " rev" if (i % 2 == 1) != bool(sec.get("start_rev")) else ""
        rows += f'<div class="media-row{rev}"><figure>{img_tag(it["img"], lang)}</figure><div class="media-text"><h2>{it["heading"]}</h2>{it["html"]}</div></div>'
    return f'<section class="sec media"><div class="wrap">{rows}</div></section>'

def r_stats(sec, lang):
    items = [x for x in SITE["stats"] if x.get("n")]
    if not items:
        return ""
    li = "".join(f'<li><span class="stat-n"><span data-count="{x["n"]}">0</span>{x.get("suffix","")}</span><span class="stat-l">{x["label_" + lang]}</span></li>' for x in items)
    return f'<section class="sec stats"><div class="wrap"><ul>{li}</ul></div></section>'

RENDER = {
    "prose": r_prose, "features": r_features, "segments": r_segments, "steps": r_steps,
    "team": r_team, "quote": r_quote, "logos": r_logos, "twocol": r_twocol, "cta": r_cta, "media": r_media, "stats": r_stats,
}

def render_sections(page, lang):
    out = []
    for sec in page.get("sections", []):
        t = sec["type"]
        if t == "faq":
            out.append(r_faq(sec, lang, page))
        elif t == "contact":
            out.append(r_contact(sec, lang, page))
        else:
            out.append(RENDER[t](sec, lang))
    return "\n".join(out)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CHROME
# ─────────────────────────────────────────────────────────────────────────────
def r_header(page, lang):
    ui = LANGS[lang]["ui"]
    nav = ""
    for key, label in ui["nav"]:
        p = find_page(lang, key)
        cur = ' aria-current="page"' if p["key"] == page["key"] else ""
        nav += f'<li><a href="{url_for(lang, p["slug"])}"{cur}>{label}</a></li>'
    other = "en" if lang == "fr" else "fr"
    alt = url_for(other, page["alt"])  # alt slug in other language
    return f'''
<a class="skip" href="#main">{ui["skip"]}</a>
<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{url_for(lang, "")}" aria-label="{SITE["name"]}"><span class="brand-eden">Eden</span><span class="brand-sub">Corporate Mobility</span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" id="nav-toggle"><span></span><span></span><span></span><span class="sr">{ui["menu"]}</span></button>
    <nav id="nav" class="nav" aria-label="{ui["nav_label"]}">
      <ul>{nav}</ul>
      <div class="nav-extra">
        <a class="lang" href="{alt}" lang="{other}" hreflang="{other}">{ui["switch"]}</a>
        <a class="btn btn-contact head-contact" href="#contact">{ICONS["mail"]}<span>{ui["contact"]}</span></a>
      </div>
    </nav>
  </div>
</header>'''

def r_footer(page, lang):
    ui = LANGS[lang]["ui"]
    cols = ""
    for title, keys in ui["footer_cols"]:
        links = ""
        for key in keys:
            p = find_page(lang, key)
            links += f'<li><a href="{url_for(lang, p["slug"])}">{p["nav"]}</a></li>'
        cols += f'<div><h2 class="foot-h">{title}</h2><ul>{links}</ul></div>'
    other = "en" if lang == "fr" else "fr"
    addr = "<br>".join(SITE["address_lines"])
    li = f'<li><a href="{SITE["linkedin"]}" rel="noopener">LinkedIn</a></li>' if SITE["linkedin"] else ""
    return f'''
<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <p class="brand"><span class="brand-eden">Eden</span><span class="brand-sub">Corporate Mobility</span></p>
      <p>{ui["footer_tagline"]}</p>
      <address>{addr}<br><a href="tel:{SITE["phone_tel"]}">{SITE["phone_display"]}</a><br><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></address>
      <ul class="foot-social">{li}<li><a href="{url_for(other, page["alt"])}" hreflang="{other}" lang="{other}">{ui["switch_long"]}</a></li></ul>
    </div>
    {cols}
  </div>
  <div class="wrap foot-bottom"><p>© {SITE["year"]} {SITE["name"]}. {ui["rights"]}</p></div>
</footer>
<div class="call-bar" role="region" aria-label="{ui["call"]}">
  <a class="btn btn-primary" href="tel:{SITE["phone_tel"]}">{ICONS["phone"]}{ui["call"]}</a>
  {"" if not SITE["whatsapp"] else f'<a class="btn btn-ghost" href="https://wa.me/{SITE["whatsapp"]}" rel="noopener">{ICONS["whatsapp"]}WhatsApp</a>'}
  <a class="btn btn-ghost" href="#contact">{ICONS["mail"]}{ui["write"]}</a>
</div>'''

def r_hero(page, lang):
    ui = LANGS[lang]["ui"]
    ctc = find_page(lang, "contact")
    h = page["hero"]
    slides = "".join(f'<div class="slide{" is-active" if i == 0 else ""}">{img_tag(sl, lang, loading=("eager" if i == 0 else "lazy"), extra=(" fetchpriority=\"high\"" if i == 0 else ""))}</div>' for i, sl in enumerate(h["slides"]))
    dots = "".join(f'<button type="button" data-slide="{i}" aria-label="{ui["slide"]} {i + 1}"{" aria-current=\"true\"" if i == 0 else ""}></button>' for i in range(len(h["slides"])))
    pills = "".join(f'<li><a href="{href}">{ICONS[ic]}<span>{lab}</span></a></li>' for ic, lab, href in h["pills"])
    return f'''
<section class="hero">
  <div class="hero-slides" id="hero-slides" aria-hidden="true">{slides}</div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="kicker">{h["kicker"]}</p>
      <h1>{page["h1"]}</h1>
      <p class="lead">{h["lead"]}</p>
      <p class="btn-row"><a class="btn btn-light" href="tel:{SITE["phone_tel"]}">{ICONS["phone"]}{ui["call_number"]}</a><a class="btn btn-outline" href="#contact">{ui["describe"]}</a></p>
      <ul class="hero-pills">{pills}</ul>
    </div>
    <aside class="call-card" aria-labelledby="cc-h">
      <p id="cc-h" class="cc-h">{h["card_title"]}</p>
      <a class="cc-phone" href="tel:{SITE["phone_tel"]}">{SITE["phone_display"]}</a>
      <p class="cc-hours">{ui["hours"]}</p>
      <ul class="cc-list">{"".join(f"<li>{x}</li>" for x in h["card_points"])}</ul>
    </aside>
  </div>
  <div class="wrap hero-foot"><div class="hero-dots" id="hero-dots">{dots}</div><p class="hero-note">{h["note"]}</p></div>
</section>'''

def r_pagehead(page, lang):
    ui = LANGS[lang]["ui"]
    home = url_for(lang, "")
    crumbs = f'<nav class="crumbs" aria-label="{ui["breadcrumb"]}"><ol><li><a href="{home}">{ui["home"]}</a></li>'
    if page.get("parent"):
        par = find_page(lang, page["parent"])
        crumbs += f'<li><a href="{url_for(lang, par["slug"])}">{par["nav"]}</a></li>'
    crumbs += f'<li aria-current="page">{page["nav"]}</li></ol></nav>'
    lead = f'<p class="lead">{page["lead"]}</p>' if page.get("lead") else ""
    if page.get("image"):
        photo = f'<div class="ph-img" aria-hidden="true">{img_tag(page["image"], lang, loading="eager", extra=" fetchpriority=\"high\"")}</div>'
        return f'<div class="page-head has-photo">{photo}<div class="wrap narrow">{crumbs}<h1>{page["h1"]}</h1>{lead}</div></div>'
    return f'<div class="page-head"><div class="wrap narrow">{crumbs}<h1>{page["h1"]}</h1>{lead}</div></div>'

# ─────────────────────────────────────────────────────────────────────────────
# STRUCTURED DATA
# ─────────────────────────────────────────────────────────────────────────────
def jsonld(page, lang):
    ui = LANGS[lang]["ui"]
    org = {
        "@type": ["Organization", "ProfessionalService"],
        "@id": SITE["url"] + "/#org",
        "name": SITE["name"],
        "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/logo.svg",
        "image": SITE["url"] + "/assets/og-image.png",
        "telephone": SITE["phone_tel"],
        "email": SITE["email"],
        "address": {"@type": "PostalAddress", "streetAddress": SITE["address_lines"][0], "addressLocality": "Sucy-en-Brie", "addressRegion": "Île-de-France", "postalCode": "94370", "addressCountry": "FR"},
        "legalName": SITE["legal"]["raison_sociale"].split(" (")[0], "vatID": SITE["legal"]["tva"].replace(" ", ""),
        "areaServed": [{"@type": "AdministrativeArea", "name": "Île-de-France"}, {"@type": "City", "name": "Paris"}],
        "priceRange": "$$$",
        "contactPoint": [{"@type": "ContactPoint", "telephone": SITE["phone_tel"], "contactType": "sales", "availableLanguage": ["fr", "en"], "areaServed": "FR"}],
        "description": strip_tags(ui["org_desc"]),
    }
    if SITE["linkedin"]:
        org["sameAs"] = [SITE["linkedin"]]
    graph = [org, {
        "@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/", "name": SITE["name"],
        "inLanguage": ["fr-FR", "en"], "publisher": {"@id": SITE["url"] + "/#org"},
    }, {
        "@type": "WebPage", "@id": abs_url(lang, page["slug"]) + "#webpage", "url": abs_url(lang, page["slug"]),
        "name": strip_tags(page["title"]), "description": strip_tags(page["desc"]), "inLanguage": "fr-FR" if lang == "fr" else "en",
        "isPartOf": {"@id": SITE["url"] + "/#website"}, "about": {"@id": SITE["url"] + "/#org"},
    }]
    if page["slug"] != "":
        items = [{"@type": "ListItem", "position": 1, "name": ui["home"], "item": abs_url(lang, "")}]
        pos = 2
        if page.get("parent"):
            par = find_page(lang, page["parent"])
            items.append({"@type": "ListItem", "position": pos, "name": strip_tags(par["nav"]), "item": abs_url(lang, par["slug"])}); pos += 1
        items.append({"@type": "ListItem", "position": pos, "name": strip_tags(page["nav"]), "item": abs_url(lang, page["slug"])})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    faqs = [s for s in page.get("sections", []) if s["type"] == "faq"]
    if faqs and page.get("faq_schema", True):
        ents = []
        for s in faqs:
            for it in s["items"]:
                ents.append({"@type": "Question", "name": strip_tags(it["q"]), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(it["a"])}})
        graph.append({"@type": "FAQPage", "mainEntity": ents})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

# ─────────────────────────────────────────────────────────────────────────────
# DOCUMENT
# ─────────────────────────────────────────────────────────────────────────────
def asset_v(name):
    """Empreinte courte du fichier, ajoutée en ?v= pour forcer le rechargement après chaque modification."""
    return hashlib.md5((ROOT / "assets" / name).read_bytes()).hexdigest()[:8]

def render_page(page, lang):
    ui = LANGS[lang]["ui"]
    css_v, js_v = asset_v("style.css"), asset_v("main.js")
    other = "en" if lang == "fr" else "fr"
    canonical = abs_url(lang, page["slug"])
    alt_url = abs_url(other, page["alt"])
    fr_url, en_url = (canonical, alt_url) if lang == "fr" else (alt_url, canonical)
    body = r_hero(page, lang) if page.get("hero") else r_pagehead(page, lang)
    body += render_sections(page, lang).replace('<section class="sec', '<section data-reveal class="sec')
    if page.get("cta", False):
        body += r_cta(ui["cta_default"], lang)
    if page["key"] != "contact":
        csec = next(sec for sec in find_page(lang, "contact")["sections"] if sec["type"] == "contact")
        body += r_contact(csec, lang, page).replace('<section class="sec', '<section data-reveal class="sec')
    noindex = '<meta name="robots" content="noindex,follow">' if page.get("noindex") else '<meta name="robots" content="index,follow,max-image-preview:large">'
    ga = SITE["analytics_id"]
    return f'''<!DOCTYPE html>
<html lang="{"fr" if lang=="fr" else "en"}" data-ga="{ga}" data-lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page["title"]}</title>
<meta name="description" content="{esc(strip_tags(page["desc"]))}">
{noindex}
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="fr" href="{fr_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE["name"]}">
<meta property="og:locale" content="{"fr_FR" if lang=="fr" else "en_US"}">
<meta property="og:locale:alternate" content="{"en_US" if lang=="fr" else "fr_FR"}">
<meta property="og:title" content="{esc(strip_tags(page["title"]))}">
<meta property="og:description" content="{esc(strip_tags(page["desc"]))}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE["url"]}/assets/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1E4B3A">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/newsreader-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/instrument-sans-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css?v={css_v}">
<script type="application/ld+json">{jsonld(page, lang)}</script>
</head>
<body class="{"home" if page.get("hero") else "inner"}">
{r_header(page, lang)}
<main id="main">
{body}
</main>
{r_footer(page, lang)}
<div class="consent" id="consent" hidden>
  <p>{ui["consent_text"]} <a href="{url_for(lang, find_page(lang,"privacy")["slug"])}">{ui["consent_more"]}</a></p>
  <p class="btn-row"><button class="btn btn-ghost" data-consent="deny">{ui["consent_deny"]}</button><button class="btn btn-primary" data-consent="allow">{ui["consent_allow"]}</button></p>
</div>
<script src="/assets/main.js?v={js_v}" defer></script>
</body>
</html>'''

# ─────────────────────────────────────────────────────────────────────────────
# SITE FILES
# ─────────────────────────────────────────────────────────────────────────────
def sitemap():
    urls = []
    for lang, cfg in LANGS.items():
        other = "en" if lang == "fr" else "fr"
        for p in cfg["pages"]:
            if p.get("noindex"):
                continue
            loc = abs_url(lang, p["slug"]); alt = abs_url(other, p["alt"])
            fr_u, en_u = (loc, alt) if lang == "fr" else (alt, loc)
            prio = "1.0" if p["slug"] == "" else ("0.8" if p.get("priority") == "high" else ("0.3" if p.get("priority") == "low" else "0.6"))
            urls.append(f'''  <url><loc>{loc}</loc><lastmod>{SITE["lastmod"]}</lastmod><priority>{prio}</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_u}"/><xhtml:link rel="alternate" hreflang="en" href="{en_u}"/><xhtml:link rel="alternate" hreflang="x-default" href="{en_u}"/>
  </url>''')
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n"

ROBOTS = """User-agent: *
Allow: /
Sitemap: {url}/sitemap.xml
"""

HTACCESS = """# Eden Corporate Mobility — Apache (Hostinger)
Options -Indexes
DirectoryIndex index.html index.php
AddDefaultCharset UTF-8
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
RewriteEngine On
# HTTPS obligatoire
RewriteCond %{HTTPS} !=on
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
# Choisir UNE version : sans www (actif) ou avec www (décommenter le bloc suivant et commenter celui-ci)
RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
RewriteRule ^ https://%1%{REQUEST_URI} [L,R=301]
# RewriteCond %{HTTP_HOST} !^www\\. [NC]
# RewriteRule ^ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
# Slash final sur les dossiers (URL propres)
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^(.+[^/])$ /$1/ [L,R=301]
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json image/svg+xml text/xml
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 1 month"
ExpiresByType application/javascript "access plus 1 month"
ExpiresByType image/svg+xml "access plus 1 year"
ExpiresByType image/png "access plus 1 year"
ExpiresByType font/woff2 "access plus 1 year"
ExpiresByType text/html "access plus 0 seconds"
</IfModule>

<IfModule mod_headers.c>
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
</IfModule>
"""

GENERATED_FILES = ["sitemap.xml", "robots.txt", "favicon.svg", "404.html", "README.md", "CNAME", ".nojekyll"]

def build():
    # Nettoyage prudent : on ne supprime que ce que le générateur produit (jamais .git, _generator, blog, .github…)
    for lang, cfg in LANGS.items():
        for p in cfg["pages"]:
            folder = DIST / cfg["prefix"] / p["slug"] if p["slug"] else DIST / cfg["prefix"]
            if p["slug"] and folder.is_dir():
                shutil.rmtree(folder)
    if (DIST / "en").is_dir():
        shutil.rmtree(DIST / "en")
    if (DIST / "assets").is_dir():
        shutil.rmtree(DIST / "assets")
    for name in GENERATED_FILES + ["index.html", ".htaccess"]:
        if (DIST / name).exists():
            (DIST / name).unlink()
    shutil.copytree(ROOT / "assets", DIST / "assets")
    for extra in GENERATED_FILES:
        src = ROOT / extra
        if src.exists():
            shutil.copy(src, DIST / extra)
    for lang, cfg in LANGS.items():
        for p in cfg["pages"]:
            out = DIST / cfg["prefix"] / p["slug"] / "index.html" if p["slug"] else DIST / cfg["prefix"] / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fill(render_page(p, lang), lang), encoding="utf-8")
    (DIST / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (DIST / "robots.txt").write_text(ROBOTS.format(url=SITE["url"]), encoding="utf-8")
    n = sum(len(c["pages"]) for c in LANGS.values())
    print(f"OK — {n} pages générées dans {DIST}")

if __name__ == "__main__":
    build()
