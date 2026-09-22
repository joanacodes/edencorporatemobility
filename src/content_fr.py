# -*- coding: utf-8 -*-
# Contenu FR — Eden Corporate Mobility
# Les jetons {{...}} sont remplacés au build (voir SITE dans build.py).

UI = {
    "nav": [("housing", "Logement"), ("transport", "Transports"), ("wellbeing", "Bien-être"), ("whowe", "Pour qui"), ("about", "À propos")],
    "footer_cols": [
        ("Services", ["housing", "transport", "wellbeing", "owners"]),
        ("Pour qui", ["consulting", "construction", "ngo", "sme", "intl"]),
        ("Eden", ["about", "faq", "contact", "legal", "terms", "privacy"]),
    ],
    "hours": "{{hours}}",
    "call": "Appeler",
    "call_number": "Appeler le {{phone}}",
    "describe": "Décrire votre besoin",
    "write": "Écrire",
    "switch": "EN",
    "switch_long": "This page in English",
    "skip": "Aller au contenu",
    "menu": "Menu",
    "nav_label": "Navigation principale",
    "home": "Accueil",
    "breadcrumb": "Fil d'Ariane",
    "rights": "Tous droits réservés.",
    "footer_tagline": "Logement, transports et services pour les collaborateurs des entreprises en mission à Paris et en Île-de-France.",
    "consent_text": "Nous utilisons un outil de mesure d'audience. Vous pouvez l'accepter ou le refuser ; le site fonctionne dans les deux cas.",
    "consent_more": "En savoir plus",
    "consent_deny": "Refuser",
    "consent_allow": "Accepter",
    "org_desc": "Eden Corporate Mobility loge, transporte et accompagne les collaborateurs des entreprises en mission à Paris et en Île-de-France : appartements meublés, aparthotels, hôtels, transferts et services bien-être. Interlocuteur unique, en français et en anglais.",
    "cta_default": {
        "heading": "Un besoin à Paris ? Appelez-nous.",
        "text": "En dix minutes, nous cadrons votre demande et vous disons ce que nous pouvons faire. En français ou en anglais, sans engagement.",
    },
}

CLIENTS = ["Mecno Service", "Anschu Security", "Meule de Montélimar", "AvePoint Deutschland", "Kodemade", "MCP Sp. z o.o.", "OPCET", "Bee-U Partners"]

SEGMENTS = [
    {"title": "Cabinets de conseil", "text": "Un consultant en mission de six mois a besoin d'un vrai appartement près du client, pas d'une chambre d'hôtel.", "href": "/cabinets-de-conseil/"},
    {"title": "Entreprises du BTP", "text": "En grand déplacement, l'hébergement de vos équipes relève de votre responsabilité. Nous le prenons en charge, près du chantier.", "href": "/entreprises-btp/"},
    {"title": "ONG et organisations", "text": "Des arrivées rapides, des budgets serrés, des durées qui bougent : nous gérons l'imprévu et les justificatifs.", "href": "/ong/"},
    {"title": "PME et ETI", "text": "Pas de travel manager en interne ? Nous jouons ce rôle pour vous, avec un seul interlocuteur et un seul devis.", "href": "/pme-eti/"},
    {"title": "Groupes internationaux", "text": "Vous détachez des cadres ou ouvrez un bureau à Paris : logement, transferts, installation des familles, en anglais.", "href": "/groupes-internationaux/"},
]

TEAM = {
    "type": "team", "heading": "L'équipe qui répond quand vous appelez",
    "intro": "Trois personnes, des expertises complémentaires, un objectif : que chaque collaborateur soit bien installé et que vous n'ayez rien à gérer.",
    "members": [
        {"name": "Flore Hountondji", "role": "Fondatrice, property manager et mobility manager", "text": "Flore sélectionne chaque logement et coordonne les mobilités des collaborateurs, de la recherche à l'installation."},
        {"name": "Tom Rurik", "role": "Business developer", "text": "Tom accompagne les entreprises clientes et identifie les solutions de logement adaptées à chaque mission, avec une approche fiable et sur mesure."},
        {"name": "Anna Prevost", "role": "Responsable des services premium", "text": "Anna construit les services personnalisés qui rendent le séjour plus simple et plus agréable : accueil, conciergerie, activités."},
    ],
}

QUOTE = {"type": "quote", "text": "Un service sérieux et fiable du début à la fin. Je recommande vivement cette agence.", "author": "Aneta Salek", "meta": "cliente"}

PAGES = [
# ───────────────────────────── ACCUEIL
{
    "key": "home", "slug": "", "alt": "", "nav": "Accueil",
    "title": "Corporate housing & mobilité à Paris | Eden Corporate Mobility",
    "desc": "Logement meublé, transports et services pour vos collaborateurs en mission à Paris et en Île-de-France. Un interlocuteur unique, en français et en anglais.",
    "h1": "Logement, transports et services pour vos collaborateurs en mission à Paris",
    "hero": {
        "lead": "Vous envoyez une équipe pour trois semaines ou un cadre pour un an ? Nous trouvons le logement, organisons les déplacements et prenons soin de vos collaborateurs sur place. Un seul interlocuteur, un seul devis.",
        "note": "Cabinets de conseil, entreprises du BTP, ONG, PME et groupes internationaux nous confient leurs équipes en Île-de-France.",
        "card_title": "Parlez à un humain, aujourd'hui.",
        "card_points": ["Réponse en français et en anglais", "Devis clair, sans engagement", "Séjours de quelques nuits à plusieurs mois"],
    },
    "sections": [
        {"type": "logos", "heading": "Ils nous font confiance", "names": CLIENTS},
        {"type": "features", "heading": "Ce que nous prenons en charge", "intro": "Tout ce qui se passe entre le départ de votre collaborateur et son retour, coordonné par une seule équipe.",
         "items": [
            {"icon": "housing", "title": "Logement", "text": "Appartements meublés, aparthotels ou hôtels selon la mission. Sélectionnés pour être proches du lieu de travail, calmes et prêts à vivre.", "href": "/logement/", "link": "Voir les solutions de logement"},
            {"icon": "transport", "title": "Transports", "text": "Transferts depuis les aéroports et les gares, trajets quotidiens vers le lieu de mission : personne n'a à chercher son chemin en arrivant.", "href": "/transports/", "link": "Voir les transports"},
            {"icon": "wellbeing", "title": "Services bien-être", "text": "Accueil, conciergerie, activités : tout ce qui rend un séjour loin de chez soi plus simple, plus agréable, et vos équipes plus efficaces.", "href": "/services-bien-etre/", "link": "Voir les services"},
         ]},
        {"type": "segments", "id": "pour-qui", "heading": "Pour qui nous travaillons", "intro": "Le logement d'un consultant, d'une équipe de chantier ou d'un cadre expatrié ne se gère pas de la même façon.", "items": SEGMENTS},
        {"type": "steps", "heading": "Comment ça se passe", "items": [
            {"title": "Vous nous appelez", "text": "Dates, nombre de personnes, lieu de mission, budget : dix minutes suffisent pour cadrer le besoin, en français ou en anglais."},
            {"title": "Nous vous proposons une sélection", "text": "Logements adaptés, transports et services, réunis dans un devis unique. Vous validez, nous réservons."},
            {"title": "Vos collaborateurs arrivent, tout est prêt", "text": "Clés, transferts, services en place. Nous restons joignables pendant tout le séjour et nous gérons les imprévus."},
        ]},
        {"type": "twocol", "heading": "Pourquoi les entreprises nous choisissent", "aside": "<p class=\"muted\">Bien loger ses collaborateurs, c'est gagner en productivité. C'est la conviction qui a fondé Eden.</p>",
         "html": """<dl class="reasons">
<dt>Un seul interlocuteur</dt><dd>Plus de dix mails entre l'hôtel, l'agence et le chauffeur : vous nous appelez, nous coordonnons tout.</dd>
<dt>Des logements choisis, pas des listings</dt><dd>Chaque logement est sélectionné pour sa localisation, son calme et son équipement, en fonction de la mission.</dd>
<dt>Flexible, de quelques nuits à plusieurs mois</dt><dd>Une mission qui s'allonge, un collaborateur qui change : nous ajustons sans rupture.</dd>
<dt>Le bien-être comme levier de performance</dt><dd>Un collaborateur bien installé dort mieux, travaille mieux et reste plus volontiers.</dd>
</dl>"""},
        QUOTE,
        TEAM,
        {"type": "faq", "heading": "Questions fréquentes", "more": "Toutes les questions fréquentes", "more_href": "/faq/", "items": [
            {"q": "Dans quelles zones intervenez-vous ?", "a": "<p>À Paris et dans toute l'Île-de-France. Pour une mission ailleurs en France, appelez-nous : nous vous dirons rapidement si nous pouvons vous aider.</p>"},
            {"q": "Quels types de logements proposez-vous ?", "a": "<p>Des appartements meublés pour les séjours d'un mois et plus, des aparthotels pour les séjours intermédiaires et des hôtels pour les séjours courts ou les arrivées en urgence. Le format dépend de la durée, du lieu de mission et de votre budget.</p>"},
            {"q": "Pouvez-vous gérer plusieurs collaborateurs ou projets en même temps ?", "a": "<p>Oui. Nous logeons des équipes entières et suivons plusieurs missions en parallèle, avec un interlocuteur unique pour votre entreprise.</p>"},
            {"q": "Comment fonctionne la facturation ?", "a": "<p>Vous recevez un devis par demande, qui détaille logement, transports et services. Après validation, nous réservons et vous facturons votre entreprise selon les modalités du devis. Vos collaborateurs n'ont rien à avancer.</p>"},
        ]},
    ],
},
# ───────────────────────────── LOGEMENT
{
    "key": "housing", "slug": "logement", "alt": "housing", "nav": "Logement", "priority": "high",
    "title": "Logement pour collaborateurs en mission à Paris | Eden Corporate Mobility",
    "desc": "Appartements meublés, aparthotels et hôtels pour vos salariés en déplacement à Paris et en Île-de-France. De quelques nuits à plusieurs mois, près du lieu de mission.",
    "h1": "Un logement prêt à vivre pour chaque collaborateur, à Paris et en Île-de-France",
    "lead": "Nous sélectionnons et réservons le logement qui correspond à la mission : sa durée, son lieu, le nombre de personnes et votre budget.",
    "sections": [
        {"type": "features", "heading": "Trois formats, selon la durée et le rythme de la mission", "items": [
            {"title": "Appartement meublé", "text": "Pour les séjours d'un mois et plus. Un vrai chez-soi avec cuisine, espace de travail et calme. Le format des consultants, des cadres en mutation et des expatriés."},
            {"title": "Aparthotel", "text": "Pour les séjours de quelques semaines. Le confort d'un appartement avec les services d'un hôtel : ménage, réception, linge."},
            {"title": "Hôtel", "text": "Pour les séjours courts et les arrivées en urgence. Nous réservons auprès d'établissements que nous connaissons, près de votre lieu de mission."},
        ]},
        {"type": "twocol", "heading": "Ce que nous vérifions avant de vous proposer un logement", "aside": "<p class=\"muted\">Un logement n'est pas un listing. Nous le choisissons comme si c'était pour un membre de notre équipe.</p>",
         "html": """<dl class="reasons">
<dt>La localisation</dt><dd>Le temps de trajet réel vers le lieu de mission, en transports en commun ou en voiture, aux heures où votre collaborateur se déplace.</dd>
<dt>Le calme et le confort</dt><dd>Literie, isolation, lumière, espace pour travailler. Ce qui fait la différence entre un séjour subi et un séjour agréable.</dd>
<dt>L'équipement</dt><dd>Cuisine complète, lave-linge, wifi fiable, télévision. Tout ce qu'il faut pour vivre, pas seulement pour dormir.</dd>
<dt>Les conditions</dt><dd>Durée, flexibilité, ménage inclus ou non, dépôt de garantie : tout est écrit noir sur blanc avant la réservation.</dd>
</dl>"""},
        {"type": "prose", "heading": "Pour les groupes et les équipes", "html": "<p>Plusieurs personnes sur un même projet ou un même chantier ? Nous logeons les équipes dans un même immeuble ou un même quartier, avec des trajets équivalents vers le site. Chambres individuelles, appartements partagés ou hôtel : nous vous proposons ce qui tient le budget et respecte les règles d'hébergement de votre secteur.</p><p>Plus vous nous prévenez tôt, plus nous avons de choix. Mais nous savons aussi gérer une arrivée imprévue.</p>"},
        {"type": "faq", "heading": "Questions sur le logement", "items": [
            {"q": "Qui signe : l'entreprise ou le collaborateur ?", "a": "<p>Dans la plupart des cas, la réservation est établie au nom de votre entreprise, qui reste notre interlocuteur contractuel et le destinataire des factures. Votre collaborateur n'a rien à avancer et rien à signer sur place, sauf l'état des lieux.</p>"},
            {"q": "Que se passe-t-il si la mission s'allonge ?", "a": "<p>Vous nous prévenez, nous prolongeons le séjour ou organisons une solution de relais, sans rupture pour le collaborateur.</p>"},
            {"q": "Pouvez-vous loger une famille ?", "a": "<p>Oui. Pour une expatriation ou une mutation, nous cherchons un logement adapté à la famille : nombre de chambres, quartier, proximité des écoles.</p>"},
        ]},
    ],
},
# ───────────────────────────── TRANSPORTS
{
    "key": "transport", "slug": "transports", "alt": "transport", "nav": "Transports", "priority": "high",
    "title": "Transports pour collaborateurs en déplacement à Paris | Eden Corporate Mobility",
    "desc": "Transferts aéroport et gare, trajets quotidiens et déplacements d'équipes à Paris et en Île-de-France, coordonnés avec le logement de vos collaborateurs.",
    "h1": "Des collaborateurs qui arrivent à l'heure, sans chercher leur chemin",
    "lead": "Nous organisons les déplacements de vos équipes à Paris et en Île-de-France, coordonnés avec leur logement et leur planning de mission.",
    "sections": [
        {"type": "features", "heading": "Ce que nous organisons", "items": [
            {"title": "Transferts aéroport et gare", "text": "Un chauffeur attend votre collaborateur à Roissy, Orly ou en gare et l'accompagne jusqu'à son logement. Pas de file d'attente aux taxis, pas d'application à installer à l'arrivée."},
            {"title": "Trajets quotidiens", "text": "Titres de transport, courses récurrentes ou navette vers le site de mission, selon les horaires de l'équipe."},
            {"title": "Déplacements d'équipe", "text": "Visites de chantier, séminaires, rendez-vous clients : un véhicule et un chauffeur pour toute l'équipe, à la demande."},
        ]},
        {"type": "prose", "heading": "Pourquoi coordonner transport et logement", "html": "<p>Un logement à quinze minutes du lieu de mission vaut mieux qu'un logement plus beau à une heure de trajet. C'est pour cela que nous choisissons d'abord le logement en fonction des déplacements, puis organisons les trajets qui restent. Le résultat : des collaborateurs reposés, ponctuels et disponibles pour ce qu'ils sont venus faire.</p><p>Tout est réuni dans le même devis et suivi par la même personne que le logement.</p>"},
    ],
},
# ───────────────────────────── BIEN-ÊTRE
{
    "key": "wellbeing", "slug": "services-bien-etre", "alt": "wellbeing-services", "nav": "Bien-être", "priority": "high",
    "title": "Services bien-être pour salariés en mission à Paris | Eden Corporate Mobility",
    "desc": "Accueil, conciergerie, activités et accompagnement des familles pour vos collaborateurs en mission à Paris. Une équipe bien installée travaille mieux.",
    "h1": "Le bien-être de vos collaborateurs, pris en charge sur place",
    "lead": "Loin de chez soi, les petites choses comptent : un frigo rempli à l'arrivée, un abonnement sportif, un rendez-vous pris. Nous nous en occupons.",
    "sections": [
        {"type": "features", "heading": "Des services à la carte ou en programme complet", "items": [
            {"title": "Accueil et installation", "text": "Courses d'arrivée, présentation du quartier, aide aux démarches du quotidien. Votre collaborateur se sent attendu dès le premier soir."},
            {"title": "Conciergerie pendant le séjour", "text": "Ménage, pressing, réservations, livraisons, petits imprévus : un numéro à appeler pour tout ce qui n'est pas la mission."},
            {"title": "Sport et activités", "text": "Accès à une salle de sport, découverte de Paris, sorties d'équipe : de quoi garder l'équilibre et la motivation sur les missions longues."},
            {"title": "Accompagnement des familles", "text": "Pour les expatriations et les mutations : écoles, garde d'enfants, installation du conjoint. Une famille bien installée, c'est un collaborateur serein."},
        ]},
        {"type": "prose", "heading": "Un programme sur mesure", "html": "<p>Chaque entreprise et chaque collaborateur sont différents. Anna, responsable des services premium, construit avec vous un programme adapté : quelques services à la carte pour une mission courte, un accompagnement complet pour une expatriation. Vous décidez ce qui est inclus, nous nous chargeons du reste.</p>"},
    ],
},
# ───────────────────────────── POUR QUI (hub)
{
    "key": "whowe", "slug": "pour-qui", "alt": "who-we-serve", "nav": "Pour qui",
    "title": "Conseil, BTP, ONG, PME, groupes internationaux | Eden Corporate Mobility",
    "desc": "Des solutions de logement et de mobilité adaptées à votre secteur : cabinets de conseil, entreprises du BTP, ONG, PME, ETI et groupes internationaux, à Paris.",
    "h1": "Des solutions pensées pour votre secteur",
    "lead": "Le logement d'un consultant, d'une équipe de chantier ou d'un cadre expatrié ne se gère pas de la même façon. Voici comment nous travaillons avec chacun.",
    "sections": [{"type": "segments", "items": SEGMENTS}],
},
# ───────────────────────────── SEGMENTS
{
    "key": "consulting", "slug": "cabinets-de-conseil", "alt": "consulting-firms", "nav": "Cabinets de conseil", "parent": "whowe", "priority": "high",
    "title": "Logement pour consultants en mission à Paris | Eden Corporate Mobility",
    "desc": "Appartements meublés et services pour vos consultants en mission à Paris : proches du client, flexibles, avec un devis par mission pour faciliter la refacturation.",
    "h1": "Logement et services pour vos consultants en mission à Paris",
    "lead": "Une mission de trois à douze mois chez un client parisien mérite mieux qu'une chambre d'hôtel. Vos consultants aussi.",
    "sections": [
        {"type": "twocol", "heading": "Ce que nous faisons pour les cabinets de conseil", "aside": "<p class=\"muted\">Le confort d'un consultant se voit dans son travail. Et dans sa fidélité au cabinet.</p>",
         "html": """<dl class="reasons">
<dt>Un appartement près du client</dt><dd>Nous partons de l'adresse de la mission et cherchons à moins de trente minutes, avec un espace de travail et un wifi fiable.</dd>
<dt>De la flexibilité</dt><dd>La mission se prolonge, se termine plus tôt, change de site : nous ajustons le logement sans pénaliser votre consultant.</dd>
<dt>Un devis par mission</dt><dd>Logement, transports et services sur un seul document, ce qui simplifie la refacturation à votre client.</dd>
<dt>Des services qui gardent vos équipes en forme</dt><dd>Sport, conciergerie, accueil : sur une mission longue, c'est ce qui évite l'usure.</dd>
</dl>"""},
        {"type": "faq", "heading": "Questions des cabinets de conseil", "items": [
            {"q": "Pouvez-vous loger un consultant qui rentre chez lui le week-end ?", "a": "<p>Oui. Nous proposons des formats adaptés aux présences du lundi au jeudi, avec un logement conservé pendant toute la mission ou une solution hôtelière selon le rythme.</p>"},
            {"q": "Pouvez-vous suivre plusieurs missions pour le même cabinet ?", "a": "<p>C'est notre quotidien. Vous avez un interlocuteur unique pour toutes vos missions en Île-de-France, et une vue claire sur ce qui est réservé pour qui.</p>"},
        ]},
    ],
},
{
    "key": "construction", "slug": "entreprises-btp", "alt": "construction-companies", "nav": "Entreprises du BTP", "parent": "whowe", "priority": "high",
    "title": "Hébergement d'équipes de chantier en Île-de-France | Eden Corporate Mobility",
    "desc": "Logement de vos ouvriers en grand déplacement sur vos chantiers en Île-de-France : hébergements groupés près du site, décents et conformes, transport inclus.",
    "h1": "Hébergement de vos équipes de chantier en Île-de-France",
    "lead": "Vos salariés en grand déplacement doivent être logés correctement, près du chantier, dans les temps. Nous prenons ce sujet en charge pour que vos conducteurs de travaux restent sur le chantier.",
    "sections": [
        {"type": "twocol", "heading": "Ce que nous faisons pour les entreprises du BTP", "aside": "<p class=\"muted\">Une équipe bien logée et bien reposée, c'est moins d'absences, moins de turnover et un chantier qui avance.</p>",
         "html": """<dl class="reasons">
<dt>Des hébergements groupés, près du site</dt><dd>Appartements partagés, résidences ou hôtels dans un même secteur, avec des trajets courts vers le chantier.</dd>
<dt>Des logements décents et conformes</dt><dd>Propres, chauffés, avec cuisine et sanitaires : nous vérifions que les conditions d'hébergement respectent vos obligations d'employeur.</dd>
<dt>Le transport vers le chantier</dt><dd>Navette, véhicules ou titres de transport, selon les horaires de l'équipe et l'accès au site.</dd>
<dt>La gestion des rotations</dt><dd>Arrivées, départs, remplacements : nous suivons les mouvements d'équipe pendant toute la durée du chantier.</dd>
<dt>Une facturation lisible</dt><dd>Un devis par chantier ou par période, des factures claires pour vos frais de grand déplacement.</dd>
</dl>"""},
        {"type": "prose", "heading": "Grand déplacement : ce que dit la règle", "html": "<p>Lorsqu'un ouvrier travaille sur un chantier trop éloigné pour rentrer chaque soir chez lui (en pratique, au-delà d'une cinquantaine de kilomètres ou d'une heure trente de trajet, selon les conventions du secteur), il est en grand déplacement. L'employeur doit alors s'assurer qu'il dispose d'un hébergement convenable : propre, chauffé, aéré, avec douche, lavabo et toilettes. Nous connaissons ces exigences et nous sélectionnons les hébergements en conséquence. Vérifiez les conditions précises dans votre convention collective.</p>"},
        {"type": "faq", "heading": "Questions des entreprises du BTP", "items": [
            {"q": "Pouvez-vous loger vingt personnes en même temps ?", "a": "<p>Oui, c'est précisément le type de demande que nous traitons pour le BTP. Plus vous nous prévenez tôt, plus nous avons de choix. Nous logeons les équipes dans un même secteur, avec des trajets équivalents vers le chantier.</p>"},
            {"q": "Et si le chantier prend du retard ?", "a": "<p>Nous prolongeons les hébergements ou organisons une solution de relais. Vous nous prévenez, nous gérons.</p>"},
        ]},
    ],
},
{
    "key": "ngo", "slug": "ong", "alt": "ngos", "nav": "ONG et organisations", "parent": "whowe", "priority": "high",
    "title": "Hébergement d'équipes d'ONG en mission à Paris | Eden Corporate Mobility",
    "desc": "Logement et transport pour les équipes d'ONG et d'organisations internationales en mission à Paris : réactivité, budgets maîtrisés, justificatifs clairs.",
    "h1": "Loger vos équipes en mission à Paris, vite et dans le budget",
    "lead": "Des arrivées à court préavis, des budgets serrés, des durées qui bougent : nous connaissons les contraintes des organisations à but non lucratif.",
    "sections": [
        {"type": "twocol", "heading": "Ce que nous faisons pour les ONG et les organisations", "aside": "<p class=\"muted\">Votre équipe est venue pour une mission, pas pour chercher un logement. Nous nous en chargeons.</p>",
         "html": """<dl class="reasons">
<dt>Des solutions rapides</dt><dd>Une équipe qui arrive la semaine prochaine pour une conférence, une formation ou une mission d'urgence : nous trouvons et réservons dans les délais.</dd>
<dt>Le bon rapport qualité-prix</dt><dd>Des hébergements corrects et bien situés, au niveau de budget que vous nous indiquez. Sans surprise à la facture.</dd>
<dt>Des groupes bien organisés</dt><dd>Plusieurs personnes, un même quartier, des trajets simples vers votre lieu de réunion. Nous gérons les arrivées échelonnées.</dd>
<dt>Des justificatifs clairs</dt><dd>Devis et factures détaillés par personne et par période, utilisables pour vos rapports aux bailleurs de fonds.</dd>
</dl>"""},
    ],
},
{
    "key": "sme", "slug": "pme-eti", "alt": "smes", "nav": "PME et ETI", "parent": "whowe", "priority": "high",
    "title": "Déplacements professionnels des PME et ETI à Paris | Eden Corporate Mobility",
    "desc": "Pas de travel manager ? Nous gérons logement, transports et services de vos collaborateurs en déplacement à Paris, avec un interlocuteur unique et un seul devis.",
    "h1": "Votre travel manager externalisé pour Paris",
    "lead": "Dans une PME, c'est souvent l'assistante de direction ou le dirigeant qui réserve les hôtels le soir. Confiez-nous ce sujet.",
    "sections": [
        {"type": "twocol", "heading": "Ce que nous faisons pour les PME et les ETI", "aside": "<p class=\"muted\">Vous gagnez du temps, vos collaborateurs gagnent en confort, et vous gardez la maîtrise du budget.</p>",
         "html": """<dl class="reasons">
<dt>Un interlocuteur, un devis, des factures centralisées</dt><dd>Fini les notes de frais éparpillées : tout passe par nous, avec une vue claire sur les dépenses.</dd>
<dt>Des solutions adaptées à votre budget</dt><dd>Nous vous proposons des options à plusieurs niveaux de prix et vous choisissez en connaissance de cause.</dd>
<dt>De la disponibilité quand ça bouge</dt><dd>Une mission qui change de date, un collaborateur qui en remplace un autre : vous nous appelez, nous ajustons.</dd>
<dt>Un service que vos équipes apprécient</dt><dd>Un bon logement et un accueil soigné pèsent dans la fidélité de vos collaborateurs, surtout quand ils se déplacent souvent.</dd>
</dl>"""},
    ],
},
{
    "key": "intl", "slug": "groupes-internationaux", "alt": "international-groups", "nav": "Groupes internationaux", "parent": "whowe", "priority": "high",
    "title": "Relocation de collaborateurs internationaux à Paris | Eden Corporate Mobility",
    "desc": "Vous détachez des cadres ou ouvrez un bureau à Paris ? Logement, transferts, installation et accompagnement de vos expatriés, en anglais et en français.",
    "h1": "Installer vos collaborateurs internationaux à Paris",
    "lead": "Une mutation, un détachement, un nouveau bureau : nous accueillons vos collaborateurs et leurs familles, et nous parlons leur langue, en anglais comme en français.",
    "sections": [
        {"type": "twocol", "heading": "Ce que nous faisons pour les groupes internationaux", "aside": "<p class=\"muted\">Votre siège parle anglais, le propriétaire parisien parle français. Nous faisons le lien.</p>",
         "html": """<dl class="reasons">
<dt>Un logement temporaire, puis durable</dt><dd>Un aparthotel ou un meublé pour les premières semaines, puis un appartement adapté à la durée du détachement.</dd>
<dt>Un accueil à l'arrivée</dt><dd>Transfert depuis l'aéroport, remise des clés, présentation du quartier, premières courses. Votre collaborateur n'est pas seul le premier soir.</dd>
<dt>L'accompagnement des familles</dt><dd>Écoles, garde d'enfants, installation du conjoint : nous préparons l'arrivée de toute la famille.</dd>
<dt>Un interlocuteur pour votre siège, un pour le terrain</dt><dd>En anglais avec vos équipes RH et mobilité, en français avec les propriétaires et les prestataires à Paris.</dd>
</dl>"""},
        {"type": "faq", "heading": "Questions des groupes internationaux", "items": [
            {"q": "Travaillez-vous avec des entreprises basées hors de France ?", "a": "<p>Oui, une partie de nos clients sont des entreprises allemandes, polonaises et d'autres pays européens qui envoient des collaborateurs en Île-de-France. Nous échangeons en anglais et nous gérons les particularités françaises pour vous.</p>"},
            {"q": "Pouvez-vous nous aider à ouvrir un bureau à Paris ?", "a": "<p>Nous logeons et installons l'équipe qui ouvre le bureau, et nous restons son point de contact local pendant les premiers mois.</p>"},
        ]},
    ],
},
# ───────────────────────────── À PROPOS
{
    "key": "about", "slug": "a-propos", "alt": "about", "nav": "À propos",
    "title": "À propos d'Eden Corporate Mobility, agence de mobilité à Paris",
    "desc": "Fondée par Flore Hountondji, Eden Corporate Mobility loge et accompagne les collaborateurs d'entreprises en mission à Paris. Équipe à taille humaine, bilingue.",
    "h1": "Une équipe à taille humaine, dédiée à la mobilité de vos talents",
    "lead": "Nous ne sommes pas une plateforme. Quand vous appelez, vous parlez à la personne qui choisira le logement de votre collaborateur.",
    "sections": [
        {"type": "prose", "heading": "Notre conviction", "html": "<p>Bien loger ses collaborateurs, c'est gagner en productivité. Un salarié qui dort bien, qui n'a pas une heure de trajet le matin et qui sait à qui s'adresser quand quelque chose ne va pas travaille mieux. Et il garde un bon souvenir de l'entreprise qui l'a envoyé.</p><p>Eden Corporate Mobility est née de ce constat. Notre mission : simplifier vos opérations et offrir une expérience premium à chaque collaborateur, du départ au retour.</p>"},
        TEAM,
        {"type": "twocol", "heading": "Comment nous travaillons", "aside": "<p class=\"muted\">Basés à Paris, nous travaillons en français et en anglais avec des entreprises françaises et européennes.</p>",
         "html": """<dl class="reasons">
<dt>Nous sélectionnons</dt><dd>Nous ne transmettons pas des listes de logements. Nous choisissons ceux qui conviennent à la mission et nous répondons de ce choix.</dd>
<dt>Nous répondons vite</dt><dd>Un appel, une réponse. Nous savons que derrière chaque demande il y a une date d'arrivée qui approche.</dd>
<dt>Nous disons ce que nous faisons</dt><dd>Un devis clair, des conditions écrites, pas de frais cachés. Si nous ne pouvons pas, nous le disons.</dd>
</dl>"""},
        {"type": "logos", "heading": "Ils nous ont choisis", "names": CLIENTS},
    ],
},
# ───────────────────────────── PROPRIÉTAIRES
{
    "key": "owners", "slug": "proprietaires", "alt": "property-owners", "nav": "Propriétaires",
    "title": "Louez votre meublé à des entreprises à Paris | Eden Corporate Mobility",
    "desc": "Un appartement meublé à Paris ou en Île-de-France ? Louez-le à des collaborateurs d'entreprises, avec des séjours encadrés et un interlocuteur professionnel.",
    "h1": "Louez votre logement meublé à des entreprises",
    "lead": "Des locataires professionnels, des séjours convenus à l'avance et un interlocuteur unique : rejoignez le réseau de logements d'Eden Corporate Mobility.",
    "sections": [
        {"type": "twocol", "heading": "Ce que nous recherchons", "aside": "<p class=\"muted\">Nous visitons et sélectionnons chaque logement avant de le proposer à nos clients.</p>",
         "html": """<dl class="reasons">
<dt>Des meublés prêts à vivre</dt><dd>Studios, deux-pièces et plus grands, entièrement équipés, à Paris et en petite couronne, proches des transports.</dd>
<dt>Des disponibilités de quelques semaines à plusieurs mois</dt><dd>Nos clients ont des besoins de durée moyenne : idéal si votre logement est libre entre deux locations ou une partie de l'année.</dd>
<dt>Des propriétaires réactifs</dt><dd>Un état des lieux soigné, un logement entretenu et une réponse rapide quand nous vous sollicitons.</dd>
</dl>"""},
        {"type": "prose", "heading": "Ce que vous y gagnez", "html": "<p>Des occupants identifiés, salariés d'entreprises clientes, avec des dates de séjour convenues à l'avance. Un interlocuteur professionnel pour toute la durée du séjour, qui gère les arrivées, les départs et les questions du quotidien. Et un logement occupé par des personnes qui viennent travailler, pas faire la fête.</p><p>Appelez-nous ou décrivez votre logement via le formulaire : nous vous répondons rapidement et nous vous expliquons comment nous travaillons.</p>"},
    ],
},
# ───────────────────────────── FAQ
{
    "key": "faq", "slug": "faq", "alt": "faq", "nav": "Questions fréquentes",
    "title": "Questions fréquentes sur nos services | Eden Corporate Mobility",
    "desc": "Facturation, types de logements, zones couvertes, délais, propriétaires : les réponses aux questions des entreprises avant de nous confier leurs collaborateurs.",
    "h1": "Questions fréquentes",
    "lead": "Si votre question n'est pas ici, appelez-nous : c'est encore plus rapide.",
    "sections": [
        {"type": "faq", "items": [
            {"q": "Comment fonctionne votre système de facturation ?", "a": "<p>Vous recevez un devis par demande, qui détaille le logement, les transports et les services. Après validation, nous réservons et facturons votre entreprise selon les modalités indiquées au devis. Vos collaborateurs n'ont rien à avancer et vous n'avez pas de notes de frais à traiter.</p>"},
            {"q": "Pourquoi choisir une solution de corporate housing plutôt qu'une location classique ?", "a": "<p>Parce qu'une location classique est faite pour durer des années : bail long, dépôt de garantie élevé, dossier lourd, logement vide. Le corporate housing est fait pour les missions : logement meublé et équipé, durée adaptée, réservation au nom de l'entreprise, un interlocuteur unique. Vous gagnez des semaines et vous ne gérez rien sur place.</p>"},
            {"q": "Proposez-vous des services premium pour les collaborateurs ?", "a": "<p>Oui : accueil et installation, conciergerie pendant le séjour, sport et activités, accompagnement des familles. À la carte ou en programme complet. <a href=\"/services-bien-etre/\">Voir les services bien-être</a>.</p>"},
            {"q": "Pouvez-vous gérer plusieurs collaborateurs ou projets simultanément ?", "a": "<p>Oui. Nous logeons des équipes entières et suivons plusieurs missions en parallèle. Vous gardez un seul interlocuteur et une vue claire sur ce qui est réservé, pour qui et jusqu'à quand.</p>"},
            {"q": "Je suis propriétaire : comment intégrer votre réseau ?", "a": "<p>Appelez-nous ou décrivez votre logement via le formulaire de contact. Nous vous expliquons nos critères et, si votre logement correspond, nous convenons d'une visite. <a href=\"/proprietaires/\">En savoir plus pour les propriétaires</a>.</p>"},
            {"q": "Quels types de logements professionnels proposez-vous ?", "a": "<p>Des appartements meublés pour les séjours d'un mois et plus, des aparthotels pour les séjours de quelques semaines et des hôtels pour les séjours courts ou les arrivées en urgence. <a href=\"/logement/\">Voir les solutions de logement</a>.</p>"},
            {"q": "À qui s'adressent vos solutions de logement corporate ?", "a": "<p>Aux entreprises et organisations qui envoient des collaborateurs en mission à Paris et en Île-de-France : cabinets de conseil, entreprises du BTP, ONG, PME, ETI et groupes internationaux. <a href=\"/pour-qui/\">Voir comment nous travaillons avec chaque secteur</a>.</p>"},
            {"q": "Dans quelles zones géographiques intervenez-vous ?", "a": "<p>À Paris et dans toute l'Île-de-France. Pour une mission ailleurs en France, appelez-nous : nous vous dirons rapidement si nous pouvons vous aider.</p>"},
            {"q": "Quels sont les délais pour trouver un logement pour un collaborateur ?", "a": "<p>Cela dépend de la durée, du lieu et du nombre de personnes. Pour une demande individuelle, nous revenons rapidement vers vous avec des options. Pour une équipe, prévenez-nous le plus tôt possible : nous aurons plus de choix. Dans l'urgence, nous savons aussi trouver une solution hôtelière pour les premières nuits.</p>"},
            {"q": "Proposez-vous un service complet de mobilité professionnelle ?", "a": "<p>Oui : logement, transports et services bien-être, coordonnés par la même équipe et réunis dans le même devis. Vous pouvez aussi ne nous confier qu'une partie, par exemple le logement seul.</p>"},
        ]},
    ],
},
# ───────────────────────────── CONTACT
{
    "key": "contact", "slug": "contact", "alt": "contact", "nav": "Contact", "cta": False, "priority": "high",
    "title": "Contact : appelez le {{phone}} | Eden Corporate Mobility",
    "desc": "Parlez à notre équipe, en français ou en anglais, pour loger et accompagner vos collaborateurs à Paris. Par téléphone ou via le formulaire.",
    "h1": "Parlons de votre prochaine mission à Paris",
    "sections": [
        {"type": "contact", "heading": "Le plus simple : nous appeler", "intro": "En dix minutes, nous cadrons votre besoin et nous vous disons ce que nous pouvons faire. En français ou en anglais.",
         "aside": "<p class=\"muted\">Vous êtes propriétaire d'un logement ? Utilisez le même formulaire et décrivez-le.</p>",
         "form": {"heading": "Ou décrivez votre besoin", "intro": "Dates, nombre de personnes, lieu de mission, budget : nous vous rappelons.",
                  "success": "Merci, votre demande est bien envoyée. Nous vous rappelons rapidement.",
                  "privacy": "Vos données servent uniquement à traiter votre demande. <a href=\"/politique-de-confidentialite/\">Politique de confidentialité</a>.",
                  "submit": "Envoyer ma demande", "subject": "[Site web] Nouvelle demande de contact",
                  "fields": [
                      {"name": "name", "label": "Nom et prénom", "type": "text", "req": True, "ac": "name"},
                      {"name": "company", "label": "Entreprise", "type": "text", "req": True, "ac": "organization"},
                      {"name": "role", "label": "Fonction", "type": "text", "ac": "organization-title"},
                      {"name": "email", "label": "Email", "type": "email", "req": True, "ac": "email"},
                      {"name": "phone", "label": "Téléphone", "type": "tel", "ac": "tel"},
                      {"name": "message", "label": "Votre besoin (dates, personnes, lieu, budget)", "type": "textarea", "req": True},
                  ]}},
    ],
},
# ───────────────────────────── LÉGAL
{
    "key": "legal", "slug": "mentions-legales", "alt": "legal-notice", "nav": "Mentions légales", "cta": False, "priority": "low",
    "title": "Mentions légales | Eden Corporate Mobility",
    "desc": "Mentions légales du site edencorporatemobility.com : éditeur, directeur de la publication, hébergeur.",
    "h1": "Mentions légales",
    "sections": [{"type": "prose", "html": """
<h2>Éditeur du site</h2>
<p>{{raison_sociale}}, {{forme}}<br>Siège social : {{address}}<br>SIREN : {{siren}} — {{rcs}}<br>N° de TVA intracommunautaire : {{tva}}<br>Téléphone : {{phone}} — Email : {{email}}<br>{{immatriculation}}</p>
<h2>Directeur de la publication</h2>
<p>{{directeur}}</p>
<h2>Hébergement</h2>
<p>{{host}}</p>
<h2>Propriété intellectuelle</h2>
<p>L'ensemble du site (textes, structure, marques, logos, visuels) est protégé par le droit de la propriété intellectuelle. Toute reproduction ou représentation, totale ou partielle, sans autorisation écrite d'{{name}} est interdite.</p>
<h2>Données personnelles et cookies</h2>
<p>Les informations relatives au traitement de vos données et à l'utilisation des cookies figurent dans notre <a href="/politique-de-confidentialite/">politique de confidentialité</a>.</p>
<h2>Responsabilité</h2>
<p>{{name}} s'efforce de maintenir des informations exactes et à jour sur ce site, sans pouvoir en garantir l'exhaustivité. Les liens vers des sites tiers n'engagent pas la responsabilité de l'éditeur.</p>
"""}],
},
{
    "key": "terms", "slug": "cgv", "alt": "terms", "nav": "Conditions générales de vente", "cta": False, "priority": "low",
    "title": "Conditions générales de vente | Eden Corporate Mobility",
    "desc": "Conditions générales de vente des prestations de logement, de transport et de services d'Eden Corporate Mobility pour les entreprises et organisations.",
    "h1": "Conditions générales de vente",
    "lead": "En vigueur à compter du {{lastmod}}. Ces conditions s'appliquent aux prestations fournies aux professionnels.",
    "sections": [{"type": "prose", "html": """
<h2>1. Objet et champ d'application</h2>
<p>Les présentes conditions générales de vente (« CGV ») régissent les relations entre {{raison_sociale}} ({{forme}}, SIREN {{siren}}), ci-après « Eden », et tout client professionnel (entreprise, organisation, association) ci-après « le Client », pour les prestations suivantes : recherche, sélection et réservation d'hébergements (appartements meublés, aparthotels, hôtels), organisation de transports, services d'accueil, de conciergerie et de bien-être, et toute prestation associée (les « Prestations »). Toute commande implique l'acceptation sans réserve des présentes CGV, qui prévalent sur tout document du Client, sauf accord écrit particulier. Les Prestations destinées à des consommateurs font l'objet de conditions spécifiques communiquées sur demande.</p>
<h2>2. Nature des Prestations</h2>
<p>Eden agit en qualité d'intermédiaire et de coordinateur entre le Client et les prestataires (propriétaires, exploitants d'hébergements, transporteurs, prestataires de services). Les Prestations sont détaillées dans le devis. Sauf mention contraire au devis, le Client demeure responsable des personnes qu'il héberge (les « Occupants »), du respect par celles-ci des règles d'usage des hébergements et des éventuels dommages qu'elles causent.</p>
<h2>3. Devis et commande</h2>
<p>Chaque demande donne lieu à un devis précisant les Prestations, les dates, le nombre d'Occupants, les prix et les conditions particulières. Le devis est valable {{devis_validite}} à compter de son émission. La commande est ferme à réception du devis accepté (signature, bon de commande ou acceptation écrite) et, le cas échéant, du paiement de l'acompte indiqué. Eden confirme alors les réservations. Toute modification ultérieure (dates, Occupants, lieu) donne lieu à un devis complémentaire.</p>
<h2>4. Prix</h2>
<p>Les prix sont exprimés en euros, hors taxes, TVA en sus au taux en vigueur. Ils comprennent les frais de service d'Eden et, selon le devis, le coût des hébergements, transports et services refacturés. Les prix des prestataires tiers peuvent varier en fonction des dates et des disponibilités jusqu'à la confirmation de la commande. Le barème des frais de service d'Eden est communiqué sur demande.</p>
<h2>5. Conditions de paiement</h2>
<p>Sauf conditions particulières au devis, un acompte de {{acompte}} du montant total est dû à la commande, le solde étant payable à {{delai_paiement}} jours à compter de la date d'émission de la facture, par virement bancaire. Aucun escompte n'est accordé pour paiement anticipé. Conformément aux articles L. 441-10 et D. 441-5 du Code de commerce, tout retard de paiement entraîne de plein droit l'application de pénalités de retard calculées au taux d'intérêt appliqué par la Banque centrale européenne à son opération de refinancement la plus récente majoré de 10 points de pourcentage, ainsi que d'une indemnité forfaitaire pour frais de recouvrement de 40 euros, sans préjudice d'une indemnisation complémentaire sur justificatifs. Eden se réserve le droit de suspendre les Prestations en cours en cas de défaut de paiement.</p>
<h2>6. Modification et annulation</h2>
<p>Toute demande de modification ou d'annulation doit être adressée par écrit. Les conditions d'annulation des hébergements, transports et services tiers, telles que communiquées au devis, s'appliquent au Client. Les frais de service d'Eden correspondant au travail déjà réalisé restent dus. En cas d'annulation moins de {{annulation_delai}} avant la date de début des Prestations, {{annulation_frais}} du montant de la commande reste dû, sauf conditions plus favorables au devis.</p>
<h2>7. Obligations du Client</h2>
<p>Le Client s'engage à communiquer des informations exactes et complètes (identité et nombre des Occupants, dates, besoins particuliers), à faire respecter par les Occupants les règles d'occupation des hébergements et les règlements intérieurs, à signaler sans délai tout incident et à régler les éventuels dépôts de garantie, frais de dégradation ou prestations supplémentaires consommées par les Occupants.</p>
<h2>8. Obligations d'Eden</h2>
<p>Eden s'engage à sélectionner avec soin les hébergements et prestataires proposés, à exécuter les Prestations avec diligence, à rester joignable pendant la durée du séjour et, en cas d'indisponibilité d'un hébergement confirmé, à proposer une solution de remplacement de niveau équivalent. Eden est tenue d'une obligation de moyens.</p>
<h2>9. Responsabilité</h2>
<p>La responsabilité d'Eden ne peut être engagée en cas d'inexécution ou de mauvaise exécution imputable au Client, aux Occupants, à un prestataire tiers ou à un cas de force majeure. En toute hypothèse, la responsabilité d'Eden est limitée au montant hors taxes des frais de service perçus au titre de la commande concernée, à l'exclusion de tout dommage indirect (perte d'exploitation, perte de chance, préjudice d'image).</p>
<h2>10. Assurances</h2>
<p>Eden est titulaire d'une assurance responsabilité civile professionnelle {{assurance}}. Le Client fait son affaire de l'assurance des Occupants et de leurs biens.</p>
<h2>11. Données personnelles</h2>
<p>Les données personnelles des interlocuteurs du Client et des Occupants sont traitées conformément à la <a href="/politique-de-confidentialite/">politique de confidentialité</a> d'Eden, pour les besoins de l'exécution des Prestations.</p>
<h2>12. Confidentialité et propriété intellectuelle</h2>
<p>Les parties s'engagent à garder confidentielles les informations échangées dans le cadre de la relation commerciale. Les documents, méthodes et contenus produits par Eden restent sa propriété.</p>
<h2>13. Durée et résiliation</h2>
<p>Les présentes s'appliquent pendant toute la durée des Prestations. En cas de manquement grave de l'une des parties non réparé dans un délai de quinze jours après mise en demeure écrite, l'autre partie peut résilier la commande de plein droit, sans préjudice des sommes dues.</p>
<h2>14. Droit applicable et juridiction</h2>
<p>Les présentes CGV sont soumises au droit français. Tout litige relatif à leur interprétation ou à leur exécution sera soumis, à défaut d'accord amiable, au Tribunal de commerce de Paris, y compris en cas de référé, d'appel en garantie ou de pluralité de défendeurs. En cas de divergence entre la version française et une traduction, la version française fait foi.</p>
<p class="muted small">Document à faire valider par votre conseil avant publication.</p>
"""}],
},
{
    "key": "privacy", "slug": "politique-de-confidentialite", "alt": "privacy-policy", "nav": "Politique de confidentialité", "cta": False, "priority": "low",
    "title": "Politique de confidentialité et cookies | Eden Corporate Mobility",
    "desc": "Comment Eden Corporate Mobility collecte, utilise et protège vos données personnelles, et comment gérer les cookies sur ce site.",
    "h1": "Politique de confidentialité",
    "lead": "Dernière mise à jour : {{lastmod}}.",
    "sections": [{"type": "prose", "html": """
<h2>1. Responsable du traitement</h2>
<p>{{raison_sociale}} ({{name}}), {{address}} — {{email}} — {{phone}}.</p>
<h2>2. Données que nous collectons</h2>
<p><strong>Via le formulaire de contact :</strong> nom et prénom, entreprise, fonction, adresse email, numéro de téléphone, contenu de votre message.<br><strong>Dans le cadre d'une prestation :</strong> identité et coordonnées des interlocuteurs du client et des personnes hébergées, dates de séjour, besoins particuliers utiles à l'organisation du séjour, données de facturation.<br><strong>Lors de la navigation :</strong> données techniques (adresse IP, type de navigateur, pages consultées) traitées par notre hébergeur pour la sécurité et le bon fonctionnement du site, et, si vous l'acceptez, données de mesure d'audience.</p>
<h2>3. Finalités et bases légales</h2>
<p>Répondre à vos demandes et établir des devis (mesures précontractuelles) ; exécuter et facturer les prestations (exécution du contrat) ; respecter nos obligations comptables et fiscales (obligation légale) ; entretenir la relation commerciale avec nos clients professionnels et vous informer de nos services (intérêt légitime, avec possibilité de vous y opposer à tout moment) ; mesurer l'audience du site (consentement).</p>
<h2>4. Destinataires</h2>
<p>Vos données sont traitées par l'équipe d'Eden et, dans la mesure nécessaire à l'exécution des prestations, transmises aux prestataires concernés (propriétaires et exploitants d'hébergements, transporteurs, prestataires de services), ainsi qu'à nos sous-traitants techniques (hébergement du site, acheminement du formulaire de contact par FormSubmit, messagerie, outils de gestion et de facturation). Nous ne vendons pas vos données.</p>
<h2>5. Transferts hors Union européenne</h2>
<p>Nos données sont hébergées dans l'Union européenne. Si l'un de nos outils implique un transfert hors UE, il est encadré par des garanties appropriées (clauses contractuelles types de la Commission européenne ou décision d'adéquation).</p>
<h2>6. Durées de conservation</h2>
<p>Demandes de contact sans suite : 3 ans à compter du dernier échange. Données clients et personnes hébergées : durée de la relation commerciale, puis archivage pendant les délais de prescription applicables. Documents comptables et factures : 10 ans. Données de mesure d'audience : 25 mois maximum. Choix relatif aux cookies : 6 mois.</p>
<h2>7. Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité de vos données, ainsi que du droit de définir des directives relatives à leur sort après votre décès. Pour l'exercer, écrivez à {{email}} ou à l'adresse postale ci-dessus, en justifiant de votre identité. Vous pouvez également introduire une réclamation auprès de la CNIL (cnil.fr).</p>
<h2>8. Cookies</h2>
<p>Ce site n'utilise que des cookies strictement nécessaires à son fonctionnement, qui ne requièrent pas votre consentement. Si un outil de mesure d'audience est activé, un bandeau vous permet d'accepter ou de refuser les cookies correspondants ; votre choix est conservé six mois et peut être modifié à tout moment en supprimant les cookies de votre navigateur. Aucun cookie publicitaire n'est déposé.</p>
<h2>9. Sécurité</h2>
<p>Nous mettons en œuvre des mesures techniques et organisationnelles adaptées pour protéger vos données : connexion chiffrée (HTTPS), accès restreint aux données, sauvegardes, sensibilisation de l'équipe.</p>
<h2>10. Mise à jour</h2>
<p>Cette politique peut être modifiée pour tenir compte de l'évolution de nos services ou de la réglementation. La version en vigueur est celle publiée sur cette page.</p>
"""}],
},
]
