# Eden Corporate Mobility — nouveau site (FR / EN)

Site statique bilingue, 34 pages, prêt pour Hostinger. Aucune dépendance et aucun code serveur : HTML, CSS, JS. Le formulaire de contact passe par FormSubmit (service gratuit, sans compte).

## 1. Contenu du livrable

```
dist/              ← À TÉLÉVERSER TEL QUEL dans public_html (Hostinger)
  index.html       ← accueil FR ; /en/ = accueil EN
  logement/ transports/ services-bien-etre/ pour-qui/ …   (FR)
  en/housing/ en/transport/ en/wellbeing-services/ …       (EN)
  sitemap.xml  robots.txt  .htaccess  404.html  favicon.svg
  assets/          ← style.css, main.js, polices auto-hébergées (RGPD), og-image.png
src/               ← générateur (Python 3) : build.py + content_fr.py + content_en.py
```

Pour modifier le site : éditer `src/content_fr.py` / `src/content_en.py` (textes, SEO) et `src/build.py` (coordonnées, infos légales), puis lancer `python3 build.py` dans `src/`. Le dossier `dist/` est régénéré. On peut aussi éditer les HTML directement.

## 2. À compléter avant la mise en ligne (tout est dans `src/build.py`, bloc `SITE`)

| Élément | Où | Statut |
|---|---|---|
| Email de contact | `SITE.email` et `SITE.form_endpoint` (FormSubmit) | à confirmer |
| Horaires d'appel FR/EN | `SITE.hours_fr`, `SITE.hours_en` | à confirmer |
| Adresse du siège | `SITE.address_lines` | à compléter |
| WhatsApp (recommandé pour les clients étrangers) | `SITE.whatsapp` (ex. `33612345678`) | vide = bouton masqué |
| Page LinkedIn | `SITE.linkedin` | vide = lien masqué |
| Mentions légales : raison sociale, forme, SIREN, RCS, TVA, capital, immatriculation Atout France / carte pro si applicable, hébergeur | `SITE.legal` | à compléter |
| CGV : validité du devis, acompte, délai de paiement, annulation, assurance RC pro | `SITE.terms` | valeurs par défaut prudentes, à valider |
| Mesure d'audience (GA4) | `SITE.analytics_id` | vide = aucun cookie, aucun bandeau |
| www ou non-www | `SITE.url` + bloc correspondant dans `.htaccess` | non-www par défaut |

CGV, mentions légales et politique de confidentialité sont un socle sérieux (Code de commerce L441-10 / D441-5, RGPD, CNIL) mais doivent être relus par un avocat. Point à vérifier avec lui : le statut d'intermédiaire (immatriculation Atout France pour la vente de séjours / carte professionnelle loi Hoguet pour l'intermédiation locative, selon le modèle exact).

## 3. Affirmations à valider dans les textes

Le copywriting est spécifique, donc engageant. Ces points sont formulés à partir du site actuel et des pratiques du secteur ; à vérifier ou ajuster :
- Réservation au nom de l'entreprise, collaborateurs qui n'avancent rien, factures centralisées (pages Logement, FAQ, PME).
- Services listés : transferts avec chauffeur, navettes, courses d'arrivée, conciergerie, sport, accompagnement des familles (pages Transports, Bien-être).
- Capacité à loger des groupes (ex. « vingt personnes ») et clients basés en Allemagne / Pologne (page BTP, Groupes internationaux) — déduit des logos clients.
- Délais de réponse : volontairement non chiffrés. Dès que vous avez un chiffre fiable (« options sous 24 h »), ajoutez-le dans le hero : c'est le meilleur levier de conversion.
- Chiffres à ajouter dès que possible : collaborateurs logés, missions par an, année de création, note Google. Aucun chiffre n'a été inventé.
- Témoignage d'Aneta Salek repris du site actuel ; d'autres témoignages nommés (entreprise + fonction) renforceraient fortement la page d'accueil.

## 4. Déploiement Hostinger

1. hPanel → Gestionnaire de fichiers → `public_html` : supprimer l'ancien contenu, téléverser **le contenu** de `dist/` (y compris `.htaccess`, fichier caché).
2. Activer le formulaire : ouvrir `/contact/` sur le site en ligne, envoyer un premier test. FormSubmit envoie alors un email d'activation à l'adresse de réception : cliquer sur le lien, une seule fois. Les demandes suivantes arrivent directement dans la boîte mail (l'expéditeur est en Reply-To). Facultatif : FormSubmit fournit ensuite un alias `https://formsubmit.co/el/…` à mettre dans `SITE.form_endpoint` pour ne pas exposer l'email dans le code. Si du spam arrive, supprimer la ligne `_captcha` dans `build.py` pour réactiver le captcha de FormSubmit.
3. SSL : activer le certificat (hPanel → Sécurité → SSL). `.htaccess` force déjà HTTPS.
4. Si le domaine actuel est sur Squarespace : pointer le DNS vers Hostinger, puis ajouter des redirections 301 des anciennes URL vers les nouvelles dans `.htaccess` (`Redirect 301 /ancienne-page /logement/`). Lister les anciennes URL avant de couper Squarespace.

## 5. Checklist SEO après mise en ligne

- Google Search Console : ajouter le domaine, soumettre `https://edencorporatemobility.com/sitemap.xml`, demander l'indexation de l'accueil FR et EN. Idem Bing Webmaster Tools.
- Fiche Google Business Profile « Eden Corporate Mobility » (catégorie : agence de logement / service de relocation), adresse, téléphone, horaires, photos. Indispensable pour exister sur le nom de marque face à Edenred / Eden Mobility.
- Page LinkedIn de l'entreprise avec l'URL du site ; les 3 profils de l'équipe doivent renvoyer vers le site.
- Cohérence nom / adresse / téléphone partout (site, Google, LinkedIn, annuaires).
- Backlinks à viser : CCI franco-allemande et franco-polonaise, annuaires du BTP et des ONG, partenaires (hôtels, aparthotels), écoles internationales, pages « ressources » des cabinets de relocation.
- Contenu à publier ensuite (blog, 1 article / mois, FR + EN) : « Loger une équipe de chantier en Île-de-France : obligations et solutions », « Corporate housing vs hôtel longue durée à Paris : coût réel », « Relocating employees to Paris: a checklist for HR », « Bail mobilité, bail société : ce que doit savoir un employeur ».
- Vérifier hreflang et données structurées avec l'outil de test des résultats enrichis de Google ; mesurer Core Web Vitals (PageSpeed Insights) : le site est léger (aucune librairie, polices auto-hébergées).

## 6. Carte des mots-clés (page → requêtes visées)

| Page | FR | EN |
|---|---|---|
| Accueil | corporate housing Paris, logement collaborateurs mission Paris, mobilité professionnelle | corporate housing Paris, employee housing Paris, business travel accommodation Paris |
| Logement | logement meublé entreprise Paris, hébergement salariés en déplacement, aparthotel entreprise | furnished apartments for employees Paris, temporary housing Paris for companies |
| Transports | transfert aéroport entreprise Paris, transport collaborateurs déplacement | airport transfer Paris corporate, employee transport Paris |
| Bien-être | services bien-être salariés en déplacement, conciergerie d'entreprise | employee wellbeing services Paris, corporate concierge Paris |
| BTP | hébergement équipes chantier Île-de-France, logement ouvriers grand déplacement | construction crew accommodation Paris, workforce housing France |
| Conseil | logement consultants en mission Paris | consultant accommodation Paris |
| ONG | hébergement équipes ONG Paris | NGO staff accommodation Paris |
| PME / ETI | gestion déplacements professionnels PME | business travel management SMEs Paris |
| Groupes internationaux | relocation collaborateurs Paris, expatriation logement Paris | relocation services Paris employees, expat housing Paris company |
| Propriétaires | louer son appartement à une entreprise Paris, bail société | rent apartment to company Paris |

## 7. Ce qui a été corrigé par rapport au site actuel

Restes de template anglais supprimés, bande de mots-clés dupliquée retirée (keyword stuffing), faute dans le titre principal corrigée, titres et meta descriptions uniques sur chaque page, balises hreflang FR/EN, données structurées (Organisation, fil d'Ariane, FAQ), sitemap, polices auto-hébergées (RGPD), pages CGV / mentions légales / confidentialité, appel téléphonique accessible partout (bouton en-tête, carte dans le hero, barre fixe sur mobile, bloc de fin de page).

## 8. Recommandations

- Ajouter de vraies photos (logements, équipe) : les blocs sont prêts à les recevoir ; une image par service et une photo d'équipe suffisent.
- Ajouter un numéro WhatsApp Business : pour un DRH allemand ou polonais, c'est souvent le premier réflexe avant un appel international.
- Enregistrer les appels comme conversions (GA4 `call_click` déjà prévu dès que l'ID est renseigné).
