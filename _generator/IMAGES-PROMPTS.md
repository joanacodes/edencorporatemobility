# Eden Corporate Mobility — images du site : prompts de génération

Chaque emplacement d'image du site a un nom de fichier fixe. Le site est livré avec des images provisoires (dégradés aux couleurs de la marque) ; pour mettre la vraie image, il suffit de **déposer un fichier du même nom dans `dist/assets/img/`** (et dans `src/assets/img/` pour les prochains builds).

## Règles pour une série cohérente

- Style commun à tous les prompts (déjà inclus dans chacun) : *Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché*.
- Générer en 16:10, 4:3 ou 3:2 selon l'emplacement (le ratio est dans chaque prompt), puis exporter à la taille indiquée. Poids visé : moins de 200 Ko par image (JPG qualité 75–80 ou WebP ; si vous utilisez WebP, changez l'extension dans `src/images.py` et relancez `build.py`).
- Pas de texte, pas de logos, pas de marques visibles. Pas de visages trop « stock ». Lumière naturelle, tons neutres, touches de vert et de laiton.
- **Photos réelles recommandées** pour l'équipe (`about-team.jpg`) et, dès que possible, pour les logements que vous proposez vraiment : une vraie photo d'appartement convainc plus qu'une image générée, et Google valorise les visuels authentiques.
- Les textes alternatifs (alt) sont déjà dans le code, en FR et en EN ; ils décrivent ce que l'image doit montrer. Si votre image montre autre chose, adaptez l'alt dans `src/images.py`.
- Outils : Midjourney (v6+), Flux, Ideogram ou Firefly fonctionnent avec ces prompts. Le suffixe `--ar` est celui de Midjourney ; ailleurs, choisissez le ratio dans l'interface.

## Liste des images

### 1. `hero-1.jpg` — Accueil — diapositive 1 (logement)

- Taille : 1600 × 1000 px (ratio 1.60)
- Alt FR : Salon lumineux d'un appartement meublé à Paris, vue sur des immeubles haussmanniens
- Alt EN : Bright living room of a furnished apartment in Paris with a view of Haussmann buildings
- Prompt :

```
Bright living room of a furnished corporate apartment in Paris, tall window with a view of Haussmann facades, sofa, small desk with a laptop, morning light. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 16:10
```

### 2. `hero-2.jpg` — Accueil — diapositive 2 (transports)

- Taille : 1600 × 1000 px (ratio 1.60)
- Alt FR : Chauffeur accueillant une voyageuse d'affaires avec sa valise devant un immeuble parisien
- Alt EN : Driver welcoming a business traveller with her suitcase in front of a Paris building
- Prompt :

```
A driver in a dark suit holding the rear door of a black sedan open for a business traveller with a cabin suitcase, quiet Paris street with Haussmann facades, early morning. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 16:10
```

### 3. `hero-3.jpg` — Accueil — diapositive 3 (équipes)

- Taille : 1600 × 1000 px (ratio 1.60)
- Alt FR : Trois collaborateurs avec bagages arrivant devant une résidence en Île-de-France
- Alt EN : Three colleagues with luggage arriving at a residence in the Paris region
- Prompt :

```
Three colleagues with rolling suitcases and work bags arriving together at the entrance of a modern residence in the Paris suburbs, one holding keys, late afternoon light. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 16:10
```

### 4. `hero-4.jpg` — Accueil — diapositive 4 (bien-être)

- Taille : 1600 × 1000 px (ratio 1.60)
- Alt FR : Table de petit-déjeuner dressée avec un panier de bienvenue dans un appartement meublé
- Alt EN : Breakfast table set with a welcome basket in a furnished apartment
- Prompt :

```
Welcome basket with fresh bread, fruit and a handwritten card on the kitchen table of a furnished Paris apartment, soft window light, Paris rooftops visible through the window. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 16:10
```

### 5. `service-logement.jpg` — Accueil — bloc Logement

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Chambre d'un appartement meublé avec literie de qualité et lumière naturelle
- Alt EN : Bedroom of a furnished apartment with quality bedding and natural light
- Prompt :

```
Calm bedroom of a furnished apartment in Paris, crisp white bedding, wooden headboard, tall window with linen curtains, a suitcase on a luggage rack. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 6. `service-transports.jpg` — Accueil — bloc Transports

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Vue depuis la banquette arrière d'une voiture avec chauffeur traversant Paris
- Alt EN : View from the back seat of a chauffeured car driving through Paris
- Prompt :

```
View from the back seat of a chauffeured car driving along the Seine in Paris, driver's hands on the wheel, soft bokeh city lights at dusk. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 7. `service-bien-etre.jpg` — Accueil — bloc Bien-être

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Personne en tenue de sport buvant un café sur un balcon parisien le matin
- Alt EN : Person in sportswear drinking coffee on a Paris balcony in the morning
- Prompt :

```
A person in running clothes holding a coffee on a small Paris balcony at sunrise, zinc rooftops, relaxed. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 8. `home-why.jpg` — Accueil — Pourquoi nous choisir

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Conseillère de l'agence remettant des clés à un collaborateur dans un appartement
- Alt EN : Agency adviser handing keys to an employee inside an apartment
- Prompt :

```
A friendly relocation adviser handing apartment keys to a newly arrived employee in a bright Paris apartment, both smiling, natural light. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 9. `seg-conseil.jpg` — Segment Cabinets de conseil (vignette + bannière)

- Taille : 900 × 600 px (ratio 1.50)
- Alt FR : Consultant travaillant sur un ordinateur portable près d'une fenêtre d'appartement parisien
- Alt EN : Consultant working on a laptop by the window of a Paris apartment
- Prompt :

```
A consultant working on a laptop at a small desk by a tall window in a Paris apartment, notebook and coffee, focused, morning light. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 3:2
```

### 10. `seg-btp.jpg` — Segment BTP (vignette + bannière)

- Taille : 900 × 600 px (ratio 1.50)
- Alt FR : Équipe de chantier en gilets de sécurité quittant un chantier en Île-de-France en fin de journée
- Alt EN : Construction crew in safety vests leaving a site in the Paris region at the end of the day
- Prompt :

```
Construction workers in hi-vis vests and helmets walking out of a building site gate at the end of the day, Paris suburb, cranes in the background, golden hour. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 3:2
```

### 11. `seg-ong.jpg` — Segment ONG (vignette + bannière)

- Taille : 900 × 600 px (ratio 1.50)
- Alt FR : Petite équipe en réunion autour d'une table avec ordinateurs et documents
- Alt EN : Small team meeting around a table with laptops and documents
- Prompt :

```
A small international team in a meeting around a wooden table with laptops and printed documents, bright room in Paris, engaged conversation. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 3:2
```

### 12. `seg-pme.jpg` — Segment PME / ETI (vignette + bannière)

- Taille : 900 × 600 px (ratio 1.50)
- Alt FR : Dirigeante de PME au téléphone dans un bureau, agenda ouvert
- Alt EN : SME manager on the phone in an office with an open diary
- Prompt :

```
An SME manager on the phone at her desk, open planner and laptop, small modern office, warm daylight, relieved expression. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 3:2
```

### 13. `seg-intl.jpg` — Segment Groupes internationaux (vignette + bannière)

- Taille : 900 × 600 px (ratio 1.50)
- Alt FR : Famille avec valises arrivant à l'aéroport de Paris-Charles-de-Gaulle
- Alt EN : Family with suitcases arriving at Paris-Charles de Gaulle airport
- Prompt :

```
A family with suitcases walking through an airport arrivals hall, looking hopeful, soft daylight through large windows, blurred crowd. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 3:2
```

### 14. `banner-logement.jpg` — Logement — bannière

- Taille : 1600 × 1000 px (ratio 1.60)
- Alt FR : Appartement meublé parisien avec parquet, cuisine ouverte et grandes fenêtres
- Alt EN : Furnished Paris apartment with parquet floor, open kitchen and large windows
- Prompt :

```
Wide view of a furnished Paris apartment: herringbone parquet, open kitchen, dining table, tall windows, plants, tidy and welcoming. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 16:10
```

### 15. `format-appartement.jpg` — Logement — Appartement meublé

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Salon et coin bureau d'un appartement meublé à Paris
- Alt EN : Living room and work corner of a furnished apartment in Paris
- Prompt :

```
Living room of a furnished apartment in Paris with a dedicated work corner, desk lamp, bookshelf, tall window. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 16. `format-aparthotel.jpg` — Logement — Aparthotel

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Studio d'aparthotel avec kitchenette et lit fait
- Alt EN : Aparthotel studio with kitchenette and made bed
- Prompt :

```
Modern aparthotel studio: made bed, compact kitchenette, folded towels, large window over a Paris street, hotel-clean. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 17. `format-hotel.jpg` — Logement — Hôtel

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Réception d'un hôtel parisien avec un voyageur d'affaires
- Alt EN : Reception desk of a Paris hotel with a business traveller
- Prompt :

```
A business traveller checking in at the reception desk of a boutique hotel in Paris, warm lighting, wood and brass details. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 18. `logement-quartier.jpg` — Logement — Où loger en Île-de-France

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Rue parisienne avec station de métro et immeubles haussmanniens
- Alt EN : Paris street with a metro station and Haussmann buildings
- Prompt :

```
A Paris street corner with a metro entrance, Haussmann buildings, a café terrace, people commuting, morning. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 19. `logement-groupe.jpg` — Logement — Groupes et équipes

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Façade d'une résidence moderne avec plusieurs appartements en Île-de-France
- Alt EN : Facade of a modern residence with several apartments in the Paris region
- Prompt :

```
Facade of a modern mid-rise residence with balconies in a green Paris suburb, clear sky, people at the entrance. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 20. `banner-transports.jpg` — Transports — bannière

- Taille : 1600 × 1000 px (ratio 1.60)
- Alt FR : Voiture avec chauffeur attendant devant le terminal d'un aéroport parisien
- Alt EN : Chauffeured car waiting outside a Paris airport terminal
- Prompt :

```
A black sedan waiting at the curb of an airport terminal at dawn, driver standing beside it with a small name sign (blank), glass facade reflections. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 16:10
```

### 21. `transport-aeroport.jpg` — Transports — Transferts aéroport et gare

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Voyageur avec valise sortant d'une gare parisienne
- Alt EN : Traveller with a suitcase leaving a Paris railway station
- Prompt :

```
A traveller with a cabin suitcase walking out of Gare de Lyon-style station hall into daylight, arches and clock, blurred crowd. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 22. `transport-quotidien.jpg` — Transports — Trajets quotidiens

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Quai de RER avec des voyageurs le matin en Île-de-France
- Alt EN : RER platform with commuters in the morning in the Paris region
- Prompt :

```
Commuters on a bright suburban train platform in the Paris region in the morning, a train arriving, calm and orderly. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 23. `transport-equipe.jpg` — Transports — Déplacements d'équipe

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Minibus déposant une équipe devant un bâtiment de bureaux
- Alt EN : Minibus dropping off a team in front of an office building
- Prompt :

```
A small team stepping out of a clean white minivan in front of a glass office building in La Défense-style district, morning. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 24. `transport-coordination.jpg` — Transports — Coordination avec le logement

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Plan de Paris et carte de transport posés sur une table avec un carnet
- Alt EN : Paris map and travel pass on a table with a notebook
- Prompt :

```
Top-down view of a paper map of Paris, a transit pass, keys and a notebook with a handwritten schedule on a wooden table. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 25. `banner-bien-etre.jpg` — Bien-être — bannière

- Taille : 1600 × 1000 px (ratio 1.60)
- Alt FR : Collaboratrice détendue lisant sur un canapé dans un appartement lumineux
- Alt EN : Relaxed employee reading on a sofa in a bright apartment
- Prompt :

```
A person relaxing on a sofa with a book in a bright furnished apartment after work, plants, warm evening light through tall windows. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 16:10
```

### 26. `bienetre-accueil.jpg` — Bien-être — Accueil et installation

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Réfrigérateur rempli de produits frais dans un appartement prêt pour l'arrivée
- Alt EN : Fridge stocked with fresh food in an apartment ready for arrival
- Prompt :

```
An open fridge freshly stocked with fruit, vegetables, yoghurt and juice in a clean apartment kitchen, a welcome note on the counter. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 27. `bienetre-conciergerie.jpg` — Bien-être — Conciergerie

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Concierge remettant un sac de pressing et des courses à la porte d'un appartement
- Alt EN : Concierge handing dry cleaning and groceries at an apartment door
- Prompt :

```
A concierge handing a garment bag and a grocery tote to a resident at the door of a Paris apartment, hallway with parquet, friendly. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 28. `bienetre-sport.jpg` — Bien-être — Sport et activités

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Personne courant le long de la Seine tôt le matin
- Alt EN : Person running along the Seine early in the morning
- Prompt :

```
A runner on the quays of the Seine at sunrise, bridges and Haussmann buildings in soft light, empty path. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 29. `bienetre-famille.jpg` — Bien-être — Familles

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Parent et enfant devant la grille d'une école parisienne
- Alt EN : Parent and child at the gate of a Paris school
- Prompt :

```
A parent walking a child with a small backpack to the gate of a Paris school in the morning, tree-lined street. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 30. `bienetre-programme.jpg` — Bien-être — Programme sur mesure

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Responsable des services prenant des notes lors d'un appel avec une cliente
- Alt EN : Services manager taking notes during a call with a client
- Prompt :

```
A services manager taking notes in a paper planner during a phone call, bright office, plants, calm. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 31. `about-team.jpg` — À propos — Comment nous travaillons (remplacer par une vraie photo d'équipe)

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : L'équipe d'Eden Corporate Mobility en réunion dans ses bureaux
- Alt EN : The Eden Corporate Mobility team in a meeting at its office
- Prompt :

```
REAL TEAM PHOTO RECOMMENDED. Otherwise: three colleagues discussing around a table with apartment plans and a laptop, bright office. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### 32. `owners-appartement.jpg` — Propriétaires — Ce que nous recherchons

- Taille : 1200 × 900 px (ratio 1.33)
- Alt FR : Propriétaire ouvrant les volets d'un appartement meublé à Paris
- Alt EN : Owner opening the shutters of a furnished apartment in Paris
- Prompt :

```
A property owner opening tall wooden shutters in a furnished Paris apartment, light flooding in, parquet floor. diverse professionals aged 25–55, candid, not looking at the camera. Editorial lifestyle photograph, natural daylight, realistic, 35 mm lens, shallow depth of field, calm premium mood, muted neutral tones with soft green and warm brass accents, Parisian context (Haussmann facades, zinc roofs, tall windows, herringbone parquet), no text, no logos, no brand names, no watermark, not oversaturated, not a luxury cliché --ar 4:3
```

### Image de partage (réseaux sociaux)

`assets/og-image.png` (1200 × 630) est générée automatiquement avec le titre du site. Pour la remplacer par une photo, gardez le même nom et la même taille, et laissez de la marge pour le texte si vous en ajoutez.
