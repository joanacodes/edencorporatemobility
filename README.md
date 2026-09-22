# Eden Corporate Mobility — site web

Site statique bilingue (FR à la racine, EN sous `/en/`), publié par GitHub Pages directement depuis ce dépôt : **ce qui est dans le dépôt est le site**. Aucune étape de build côté GitHub.

## Modifier le site

Deux façons :

1. **Éditer les fichiers HTML directement** (`index.html`, `logement/index.html`, `en/housing/index.html`…), puis `git add . ; git commit -m "…" ; git push`. Le site est à jour une minute plus tard.
2. **Utiliser le générateur** (`_generator/`), pratique pour changer un texte présent sur toutes les pages (menu, pied de page, formulaire, coordonnées) ou les contenus dans `content_fr.py` / `content_en.py` / `services_*.py` :

```powershell
cd _generator
py build.py
cd ..
git add . ; git commit -m "Mise à jour" ; git push
```

Attention : le générateur réécrit toutes les pages HTML. Si vous avez modifié un HTML à la main, reportez la modification dans `_generator/` avant de relancer `build.py`, sinon elle sera perdue.

## Voir le site en local

```powershell
py -m http.server 8001
```

puis http://localhost:8001 (Ctrl+C pour arrêter). Vous devez être à la racine du dépôt.

## Images

Les images provisoires sont dans `assets/img/` (et `_generator/assets/img/` pour le générateur). Remplacez-les par vos photos **en gardant le même nom de fichier**. Les prompts de génération sont dans `_generator/IMAGES-PROMPTS.md`.

## À compléter (dans `_generator/build.py`, bloc `SITE`)

- Email de contact (`email` et `form_endpoint`, FormSubmit) — puis envoyer un premier message depuis le site pour activer FormSubmit (un email d'activation arrive, cliquer une fois).
- Horaires d'appel, WhatsApp, LinkedIn.
- Mentions légales : numéro de carte professionnelle (loi Hoguet), garantie financière, directeur de la publication à confirmer.
- CGV : validité du devis, acompte, délais de paiement, annulation, assurance. À faire relire par un avocat.
- Chiffres pour les compteurs (`stats`) quand vous en avez.

## Domaine

Le fichier `CNAME` contient `edencorporatemobility.com`. Chez le registrar : 4 enregistrements A vers 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153, un CNAME `www` → `joanacodes.github.io`, sans toucher aux MX (email). Puis GitHub → Settings → Pages → Custom domain → « Enforce HTTPS ».

## Blog (Hugo, plus tard)

Générer le blog dans un dossier `blog/` à la racine (`hugo -d ../blog --baseURL https://edencorporatemobility.com/blog/`), le commiter, le pousser. Le générateur ne touche pas à ce dossier.

## Après la mise en ligne (SEO)

Google Search Console (sitemap : `https://edencorporatemobility.com/sitemap.xml`), fiche Google Business Profile, page LinkedIn avec l'URL du site, redirections des anciennes URL Squarespace si possible (GitHub Pages ne fait pas de redirections serveur : créer une page HTML avec une balise `<meta http-equiv="refresh">` à l'ancienne adresse si nécessaire).
