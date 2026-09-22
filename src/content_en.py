# -*- coding: utf-8 -*-
# English content — Eden Corporate Mobility. Tokens {{...}} are replaced at build time.

UI = {
    "nav": [("housing", "Housing"), ("transport", "Transport"), ("wellbeing", "Wellbeing"), ("whowe", "Who we serve"), ("about", "About")],
    "footer_cols": [
        ("Services", ["housing", "transport", "wellbeing", "owners"]),
        ("Who we serve", ["consulting", "construction", "ngo", "sme", "intl"]),
        ("Eden", ["about", "faq", "contact", "legal", "terms", "privacy"]),
    ],
    "hours": "{{hours_en}}",
    "call": "Call us",
    "call_number": "Call {{phone}}",
    "describe": "Describe your needs",
    "write": "Write",
    "switch": "FR",
    "switch_long": "Cette page en français",
    "skip": "Skip to content",
    "menu": "Menu",
    "nav_label": "Main navigation",
    "home": "Home",
    "breadcrumb": "Breadcrumb",
    "rights": "All rights reserved.",
    "footer_tagline": "Housing, transport and wellbeing services for employees on assignment in Paris and the Île-de-France region.",
    "consent_text": "We use an audience measurement tool. You can accept or decline it; the site works either way.",
    "consent_more": "Learn more",
    "consent_deny": "Decline",
    "consent_allow": "Accept",
    "org_desc": "Eden Corporate Mobility houses, transports and looks after employees sent to Paris and the Île-de-France region by their companies: furnished apartments, aparthotels, hotels, airport transfers and wellbeing services. One English-speaking contact in Paris.",
    "cta_default": {
        "heading": "Sending people to Paris? Call us.",
        "text": "In ten minutes we will understand your needs and tell you what we can do. In English or French, no commitment.",
    },
}

CLIENTS = ["Mecno Service", "Anschu Security", "Meule de Montélimar", "AvePoint Deutschland", "Kodemade", "MCP Sp. z o.o.", "OPCET", "Bee-U Partners"]

SEGMENTS = [
    {"title": "Consulting firms", "text": "A consultant on a six-month engagement needs a real apartment near the client, not a hotel room.", "href": "/en/consulting-firms/"},
    {"title": "Construction companies", "text": "Crews working far from home must be housed properly, close to the site and on time. We take that off your hands.", "href": "/en/construction-companies/"},
    {"title": "NGOs and organisations", "text": "Short notice, tight budgets, dates that move: we handle the unexpected and give you clean paperwork.", "href": "/en/ngos/"},
    {"title": "SMEs and mid-size companies", "text": "No travel manager in-house? We play that role for your Paris trips, with one contact and one quote.", "href": "/en/smes/"},
    {"title": "International groups", "text": "Seconding executives or opening a Paris office: housing, transfers, family settling-in, all in English.", "href": "/en/international-groups/"},
]

TEAM = {
    "type": "team", "heading": "The people who pick up the phone",
    "intro": "Three people, complementary skills, one goal: every employee well settled, and nothing left for you to manage.",
    "members": [
        {"name": "Flore Hountondji", "role": "Founder, property manager and mobility manager", "text": "Flore selects every property and coordinates each employee's move, from the first search to the day they settle in."},
        {"name": "Tom Rurik", "role": "Business developer", "text": "Tom works with client companies to understand each assignment and identify housing that fits it, with a reliable, tailored approach."},
        {"name": "Anna Prevost", "role": "Head of premium services", "text": "Anna builds the personalised services that make a stay simpler and more pleasant: welcome, concierge, activities."},
    ],
}

QUOTE = {"type": "quote", "text": "Serious and reliable service from start to finish. I highly recommend this agency.", "author": "Aneta Salek", "meta": "client"}

PAGES = [
# ───────────────────────────── HOME
{
    "key": "home", "slug": "", "alt": "", "nav": "Home",
    "title": "Corporate Housing in Paris for Your Employees | Eden Corporate Mobility",
    "desc": "Furnished housing, transport and wellbeing services for employees your company sends to Paris and the Île-de-France region. One English-speaking contact in Paris.",
    "h1": "Housing, transport and care for your employees on assignment in Paris",
    "hero": {
        "lead": "Sending a crew for three weeks or an executive for a year? We find the housing, organise the transport and look after your people once they land. One local contact who speaks your language, one quote.",
        "note": "Consulting firms, construction companies, NGOs, SMEs and international groups trust us with their teams in the Paris region.",
        "card_title": "Talk to a person in Paris, today.",
        "card_points": ["We answer in English and French", "Clear quote, no commitment", "Stays from a few nights to many months"],
    },
    "sections": [
        {"type": "logos", "heading": "Companies that trust us", "names": CLIENTS},
        {"type": "features", "heading": "What we take care of", "intro": "Everything that happens between your employee's departure and return, coordinated by one team on the ground in Paris.",
         "items": [
            {"icon": "housing", "title": "Housing", "text": "Furnished apartments, aparthotels or hotels depending on the assignment. Chosen to be close to the workplace, quiet and ready to live in.", "href": "/en/housing/", "link": "See housing options"},
            {"icon": "transport", "title": "Transport", "text": "Airport and station pick-ups, daily commutes to the assignment site: nobody has to work out the Paris metro on their first evening.", "href": "/en/transport/", "link": "See transport services"},
            {"icon": "wellbeing", "title": "Wellbeing services", "text": "Welcome, concierge, activities: everything that makes a stay far from home simpler and more pleasant, and your team more effective.", "href": "/en/wellbeing-services/", "link": "See wellbeing services"},
         ]},
        {"type": "segments", "id": "who-we-serve", "heading": "Who we work with", "intro": "Housing a consultant, a construction crew or an expatriate executive are three different jobs. We know each one.", "items": SEGMENTS},
        {"type": "steps", "heading": "How it works", "items": [
            {"title": "You call us", "text": "Dates, number of people, where they will work, budget: ten minutes is enough to frame the request, in English or French."},
            {"title": "We send you a selection", "text": "Suitable housing, transport and services, in one quote. You approve, we book."},
            {"title": "Your people arrive, everything is ready", "text": "Keys, transfers, services in place. We stay reachable for the whole stay and handle whatever comes up."},
        ]},
        {"type": "twocol", "heading": "Why companies choose us", "aside": "<p class=\"muted\">Housing employees well is a productivity decision. That conviction is why Eden exists.</p>",
         "html": """<dl class="reasons">
<dt>One contact, on the ground in Paris</dt><dd>No more email chains between a hotel, an agency and a driver in a language you may not speak: you call us, we coordinate everything locally.</dd>
<dt>Housing we have chosen, not listings</dt><dd>Every property is selected for its location, quietness and equipment, for the assignment in question.</dd>
<dt>Flexible, from a few nights to many months</dt><dd>An assignment that runs long, a team member who changes: we adjust without disruption.</dd>
<dt>Wellbeing as a performance lever</dt><dd>A well-settled employee sleeps better, works better and is happier to go again.</dd>
</dl>"""},
        QUOTE,
        TEAM,
        {"type": "faq", "heading": "Frequently asked questions", "more": "All frequently asked questions", "more_href": "/en/faq/", "items": [
            {"q": "Which areas do you cover?", "a": "<p>Paris and the whole Île-de-France region (Greater Paris). For an assignment elsewhere in France, call us and we will quickly tell you whether we can help.</p>"},
            {"q": "Do you work with companies based outside France?", "a": "<p>Yes. Many of our clients are companies in Germany, Poland and other European countries sending staff to the Paris region. We work in English and handle the French specifics for you.</p>"},
            {"q": "What kinds of housing do you offer?", "a": "<p>Furnished apartments for stays of a month or more, aparthotels for stays of a few weeks and hotels for short stays or last-minute arrivals. The format depends on duration, work location and your budget.</p>"},
            {"q": "How does invoicing work?", "a": "<p>You receive one quote per request, itemising housing, transport and services. Once approved, we book and invoice your company on the terms stated in the quote. Your employees pay nothing up front.</p>"},
        ]},
    ],
},
# ───────────────────────────── HOUSING
{
    "key": "housing", "slug": "housing", "alt": "logement", "nav": "Housing", "priority": "high",
    "title": "Furnished Housing for Employees in Paris | Eden Corporate Mobility",
    "desc": "Furnished apartments, aparthotels and hotels for staff on assignment in Paris and the Île-de-France region. A few nights to many months, close to the workplace.",
    "h1": "Ready-to-live-in housing for every employee, in Paris and the surrounding region",
    "lead": "We select and book the housing that fits the assignment: its length, its location, the number of people and your budget.",
    "sections": [
        {"type": "features", "heading": "Three formats, depending on length and rhythm of the assignment", "items": [
            {"title": "Furnished apartment", "text": "For stays of a month or more. A real home with a kitchen, a place to work and peace and quiet. The format for consultants, relocated executives and expatriates."},
            {"title": "Aparthotel", "text": "For stays of a few weeks. The comfort of an apartment with hotel services: cleaning, reception, linen."},
            {"title": "Hotel", "text": "For short stays and last-minute arrivals. We book with establishments we know, near the place of work."},
        ]},
        {"type": "twocol", "heading": "What we check before proposing a property", "aside": "<p class=\"muted\">A property is not a listing. We choose it as if it were for a member of our own team.</p>",
         "html": """<dl class="reasons">
<dt>Location</dt><dd>Real travel time to the workplace, by public transport or car, at the hours your employee will actually commute.</dd>
<dt>Quiet and comfort</dt><dd>Bedding, insulation, light, space to work. The difference between a stay endured and a stay enjoyed.</dd>
<dt>Equipment</dt><dd>Full kitchen, washing machine, reliable wifi, TV. Everything needed to live, not just to sleep.</dd>
<dt>Terms</dt><dd>Duration, flexibility, cleaning included or not, deposit: everything in writing before booking.</dd>
</dl>"""},
        {"type": "prose", "heading": "For groups and teams", "html": "<p>Several people on the same project or site? We house teams in the same building or neighbourhood, with equivalent commutes to the site. Single rooms, shared apartments or hotel: we propose what fits the budget and complies with your sector's accommodation rules.</p><p>The earlier you tell us, the more choice we have. But we also know how to handle an unplanned arrival.</p>"},
        {"type": "faq", "heading": "Housing questions", "items": [
            {"q": "Who signs: the company or the employee?", "a": "<p>In most cases the booking is made in your company's name; the company remains our contractual contact and receives the invoices. Your employee pays nothing up front and signs nothing on site except the check-in inventory.</p>"},
            {"q": "What if the assignment runs longer?", "a": "<p>Tell us, and we extend the stay or arrange a follow-on solution with no disruption for the employee.</p>"},
            {"q": "Can you house a family?", "a": "<p>Yes. For an expatriation or a relocation we look for housing that suits the family: number of bedrooms, neighbourhood, proximity to schools.</p>"},
        ]},
    ],
},
# ───────────────────────────── TRANSPORT
{
    "key": "transport", "slug": "transport", "alt": "transports", "nav": "Transport", "priority": "high",
    "title": "Employee Transport & Airport Transfers, Paris | Eden Corporate Mobility",
    "desc": "Airport and station transfers, daily commutes and team travel in Paris and the Île-de-France region, coordinated with your employees' housing.",
    "h1": "Employees who arrive on time, without working out the way",
    "lead": "We organise your team's travel in Paris and the surrounding region, coordinated with their housing and their work schedule.",
    "sections": [
        {"type": "features", "heading": "What we organise", "items": [
            {"title": "Airport and station transfers", "text": "A driver meets your employee at Charles de Gaulle, Orly or the station and takes them to their door. No taxi queue, no app to install on arrival."},
            {"title": "Daily commutes", "text": "Travel passes, recurring rides or a shuttle to the site, depending on the team's hours."},
            {"title": "Team travel", "text": "Site visits, workshops, client meetings: a vehicle and driver for the whole team, on request."},
        ]},
        {"type": "prose", "heading": "Why housing and transport are decided together", "html": "<p>A place fifteen minutes from the site beats a nicer place an hour away. So we choose the housing around the commute first, then organise the journeys that remain. The result: rested, punctual employees available for what they came to do.</p><p>Everything sits on the same quote and is followed by the same person as the housing.</p>"},
    ],
},
# ───────────────────────────── WELLBEING
{
    "key": "wellbeing", "slug": "wellbeing-services", "alt": "services-bien-etre", "nav": "Wellbeing", "priority": "high",
    "title": "Wellbeing & Concierge Services, Paris | Eden Corporate Mobility",
    "desc": "Welcome, concierge, activities and family support for your employees on assignment in Paris. Because a well-settled team works better.",
    "h1": "Your employees' wellbeing, looked after on the ground",
    "lead": "Far from home, small things matter: a stocked fridge on arrival, a gym membership, an appointment booked. We take care of them.",
    "sections": [
        {"type": "features", "heading": "À la carte or as a full programme", "items": [
            {"title": "Welcome and settling-in", "text": "Arrival groceries, a walk around the neighbourhood, help with everyday admin. Your employee feels expected from the first evening."},
            {"title": "Concierge during the stay", "text": "Cleaning, laundry, bookings, deliveries, small emergencies: one number to call for everything that is not the job."},
            {"title": "Sport and activities", "text": "Gym access, discovering Paris, team outings: what keeps balance and motivation on long assignments."},
            {"title": "Family support", "text": "For expatriations and relocations: schools, childcare, helping the partner settle. A well-settled family means a focused employee."},
        ]},
        {"type": "prose", "heading": "A programme built for you", "html": "<p>Every company and every employee is different. Anna, our head of premium services, builds the programme with you: a few à la carte services for a short assignment, full support for an expatriation. You decide what is included; we take care of the rest.</p>"},
    ],
},
# ───────────────────────────── WHO WE SERVE (hub)
{
    "key": "whowe", "slug": "who-we-serve", "alt": "pour-qui", "nav": "Who we serve",
    "title": "Who We Serve: Consulting, Construction, NGOs, SMEs | Eden Corporate Mobility",
    "desc": "Housing and mobility solutions built for your sector: consulting firms, construction companies, NGOs, SMEs and international groups sending staff to Paris.",
    "h1": "Solutions built for your sector",
    "lead": "Housing a consultant, a construction crew or an expatriate executive are three different jobs. Here is how we work with each.",
    "sections": [{"type": "segments", "items": SEGMENTS}],
},
# ───────────────────────────── SEGMENTS
{
    "key": "consulting", "slug": "consulting-firms", "alt": "cabinets-de-conseil", "nav": "Consulting firms", "parent": "whowe", "priority": "high",
    "title": "Housing for Consultants on Assignment in Paris | Eden Corporate Mobility",
    "desc": "Furnished apartments and services for your consultants on long engagements in Paris: close to the client, flexible, one quote per engagement for easy rebilling.",
    "h1": "Housing and services for your consultants in Paris",
    "lead": "A three- to twelve-month engagement with a Paris client deserves better than a hotel room. So do your consultants.",
    "sections": [
        {"type": "twocol", "heading": "What we do for consulting firms", "aside": "<p class=\"muted\">A consultant's comfort shows in their work. And in how long they stay with the firm.</p>",
         "html": """<dl class="reasons">
<dt>An apartment near the client</dt><dd>We start from the engagement address and search within thirty minutes of it, with a workspace and reliable wifi.</dd>
<dt>Flexibility</dt><dd>The engagement runs long, ends early or moves site: we adjust the housing without penalising your consultant.</dd>
<dt>One quote per engagement</dt><dd>Housing, transport and services on a single document, which makes rebilling to your client straightforward.</dd>
<dt>Services that keep your people fresh</dt><dd>Gym, concierge, welcome: on a long engagement, this is what prevents burnout.</dd>
</dl>"""},
        {"type": "faq", "heading": "Questions from consulting firms", "items": [
            {"q": "Can you house a consultant who flies home at weekends?", "a": "<p>Yes. We propose formats suited to Monday-to-Thursday presence, either keeping the apartment for the whole engagement or a hotel solution, depending on the rhythm.</p>"},
            {"q": "Can you handle several engagements for the same firm?", "a": "<p>That is our daily work. You have one contact for all your engagements in the Paris region and a clear view of what is booked for whom.</p>"},
        ]},
    ],
},
{
    "key": "construction", "slug": "construction-companies", "alt": "entreprises-btp", "nav": "Construction companies", "parent": "whowe", "priority": "high",
    "title": "Construction Crew Accommodation in Paris | Eden Corporate Mobility",
    "desc": "Workforce housing for your crews on construction sites in Paris and the Île-de-France region: grouped accommodation near the site, compliant, with transport.",
    "h1": "Accommodation for your construction crews in the Paris region",
    "lead": "Workers posted far from home must be housed properly, near the site, on time. We take this on so your site managers can stay on site.",
    "sections": [
        {"type": "twocol", "heading": "What we do for construction companies", "aside": "<p class=\"muted\">A well-housed, well-rested crew means fewer absences, less turnover and a site that keeps moving.</p>",
         "html": """<dl class="reasons">
<dt>Grouped accommodation near the site</dt><dd>Shared apartments, residences or hotels in the same area, with short journeys to the site.</dd>
<dt>Decent, compliant housing</dt><dd>Clean, heated, with kitchen and bathroom facilities: we check that conditions meet French employer obligations for workers away from home.</dd>
<dt>Transport to the site</dt><dd>Shuttle, vehicles or travel passes, depending on the crew's hours and site access.</dd>
<dt>Crew rotations</dt><dd>Arrivals, departures, replacements: we track team movements for the whole duration of the project.</dd>
<dt>Clear invoicing</dt><dd>One quote per project or period, and clear invoices for your travel and subsistence accounting.</dd>
</dl>"""},
        {"type": "prose", "heading": "Posting crews to France: what to know", "html": "<p>Under French rules, a worker whose site is too far to return home each night is on \"grand déplacement\". The employer must then make sure the worker has proper accommodation: clean, heated, ventilated, with shower, washbasin and toilet. Companies posting workers from other EU countries face equivalent obligations. We know these requirements and select accommodation accordingly. Check the exact conditions in the applicable collective agreement or with your advisers.</p>"},
        {"type": "faq", "heading": "Questions from construction companies", "items": [
            {"q": "Can you house twenty people at once?", "a": "<p>Yes, this is exactly the kind of request we handle for construction. The earlier you tell us, the more choice we have. We house crews in the same area with equivalent commutes to the site.</p>"},
            {"q": "What if the project is delayed?", "a": "<p>We extend the accommodation or arrange a follow-on solution. You tell us, we handle it.</p>"},
        ]},
    ],
},
{
    "key": "ngo", "slug": "ngos", "alt": "ong", "nav": "NGOs and organisations", "parent": "whowe", "priority": "high",
    "title": "Accommodation for NGO Teams on Mission in Paris | Eden Corporate Mobility",
    "desc": "Housing and transport for NGO and international organisation teams on mission in Paris: fast response, controlled budgets, clean paperwork for donors.",
    "h1": "Housing your teams in Paris, fast and within budget",
    "lead": "Short-notice arrivals, tight budgets, dates that move: we know the constraints of non-profit organisations.",
    "sections": [
        {"type": "twocol", "heading": "What we do for NGOs and organisations", "aside": "<p class=\"muted\">Your team came for a mission, not to hunt for housing. We take care of it.</p>",
         "html": """<dl class="reasons">
<dt>Fast solutions</dt><dd>A team arriving next week for a conference, a training or an emergency mission: we find and book in time.</dd>
<dt>Good value</dt><dd>Decent, well-located accommodation at the budget level you give us. No surprises on the invoice.</dd>
<dt>Well-organised groups</dt><dd>Several people, one neighbourhood, simple journeys to your meeting venue. We manage staggered arrivals.</dd>
<dt>Clean paperwork</dt><dd>Quotes and invoices itemised per person and per period, ready for your donor reporting.</dd>
</dl>"""},
    ],
},
{
    "key": "sme", "slug": "smes", "alt": "pme-eti", "nav": "SMEs and mid-size companies", "parent": "whowe", "priority": "high",
    "title": "Business Travel Housing in Paris for SMEs | Eden Corporate Mobility",
    "desc": "No travel manager? We handle housing, transport and services for your employees travelling to Paris, with one local contact and one quote.",
    "h1": "Your outsourced travel manager for Paris",
    "lead": "In a smaller company it is often the office manager or the CEO booking hotels at night. Hand that job to us.",
    "sections": [
        {"type": "twocol", "heading": "What we do for SMEs and mid-size companies", "aside": "<p class=\"muted\">You save time, your employees gain comfort, and you keep control of the budget.</p>",
         "html": """<dl class="reasons">
<dt>One contact, one quote, centralised invoices</dt><dd>No more scattered expense claims: everything goes through us, with a clear view of spending.</dd>
<dt>Options that fit your budget</dt><dd>We propose options at several price levels and you choose with full information.</dd>
<dt>Availability when things change</dt><dd>An assignment that moves date, an employee replacing another: you call, we adjust.</dd>
<dt>A service your people appreciate</dt><dd>Good housing and a proper welcome count for retention, especially for those who travel often.</dd>
</dl>"""},
    ],
},
{
    "key": "intl", "slug": "international-groups", "alt": "groupes-internationaux", "nav": "International groups", "parent": "whowe", "priority": "high",
    "title": "Relocating International Staff to Paris | Eden Corporate Mobility",
    "desc": "Seconding executives or opening an office in Paris? Housing, airport transfers, settling-in and family support for your expatriates, in English and French.",
    "h1": "Settling your international employees in Paris",
    "lead": "A relocation, a secondment, a new office: we welcome your employees and their families, and we speak their language, in English as well as French.",
    "sections": [
        {"type": "twocol", "heading": "What we do for international groups", "aside": "<p class=\"muted\">Your head office speaks English, the Paris landlord speaks French. We are the bridge.</p>",
         "html": """<dl class="reasons">
<dt>Temporary housing, then long-term</dt><dd>An aparthotel or furnished flat for the first weeks, then an apartment suited to the length of the secondment.</dd>
<dt>A welcome on arrival</dt><dd>Airport transfer, keys, a tour of the neighbourhood, first groceries. Your employee is not alone on the first evening.</dd>
<dt>Family support</dt><dd>Schools, childcare, helping the partner settle: we prepare the arrival of the whole family.</dd>
<dt>One contact for head office, one for the ground</dt><dd>English with your HR and mobility teams, French with landlords and suppliers in Paris.</dd>
</dl>"""},
        {"type": "faq", "heading": "Questions from international groups", "items": [
            {"q": "Do you work with companies based outside France?", "a": "<p>Yes. Many of our clients are German, Polish and other European companies sending staff to the Paris region. We work in English and handle the French specifics for you.</p>"},
            {"q": "Can you help us open an office in Paris?", "a": "<p>We house and settle the team opening the office and remain their local point of contact during the first months.</p>"},
        ]},
    ],
},
# ───────────────────────────── ABOUT
{
    "key": "about", "slug": "about", "alt": "a-propos", "nav": "About",
    "title": "About Eden Corporate Mobility, Corporate Housing Agency in Paris",
    "desc": "Founded by Flore Hountondji, Eden Corporate Mobility houses and supports employees sent to Paris by their companies. A small, bilingual team on the ground.",
    "h1": "A small team on the ground, dedicated to moving your talent",
    "lead": "We are not a platform. When you call, you speak to the person who will choose your employee's housing.",
    "sections": [
        {"type": "prose", "heading": "What we believe", "html": "<p>Housing employees well is a productivity decision. Someone who sleeps well, does not spend an hour commuting each morning and knows who to call when something goes wrong does better work. And keeps a good memory of the company that sent them.</p><p>Eden Corporate Mobility was founded on that observation. Our mission: simplify your operations and give every employee a premium experience, from departure to return.</p>"},
        TEAM,
        {"type": "twocol", "heading": "How we work", "aside": "<p class=\"muted\">Based in Paris, we work in English and French with French and European companies.</p>",
         "html": """<dl class="reasons">
<dt>We select</dt><dd>We do not forward lists of properties. We choose the ones that fit the assignment, and we stand behind that choice.</dd>
<dt>We answer fast</dt><dd>One call, one answer. We know every request has an arrival date getting closer.</dd>
<dt>We say what we do</dt><dd>A clear quote, written terms, no hidden fees. If we cannot do something, we say so.</dd>
</dl>"""},
        {"type": "logos", "heading": "Companies that chose us", "names": CLIENTS},
    ],
},
# ───────────────────────────── PROPERTY OWNERS
{
    "key": "owners", "slug": "property-owners", "alt": "proprietaires", "nav": "Property owners",
    "title": "Rent Your Furnished Flat to Companies in Paris | Eden Corporate Mobility",
    "desc": "Own a furnished apartment in Paris or nearby? Rent it to company employees on assignment, with pre-agreed stays and one professional point of contact.",
    "h1": "Rent your furnished property to companies",
    "lead": "Professional tenants, stays agreed in advance and one point of contact: join Eden Corporate Mobility's housing network.",
    "sections": [
        {"type": "twocol", "heading": "What we look for", "aside": "<p class=\"muted\">We visit and select every property before offering it to our clients.</p>",
         "html": """<dl class="reasons">
<dt>Ready-to-live-in furnished homes</dt><dd>Studios, one-bedrooms and larger, fully equipped, in Paris and the inner suburbs, close to public transport.</dd>
<dt>Availability from a few weeks to several months</dt><dd>Our clients need mid-length stays: ideal if your property is free between tenants or for part of the year.</dd>
<dt>Responsive owners</dt><dd>A careful inventory, a well-maintained property and a quick answer when we reach out.</dd>
</dl>"""},
        {"type": "prose", "heading": "What you gain", "html": "<p>Identified occupants, employees of client companies, with stay dates agreed in advance. A professional contact for the whole stay, handling arrivals, departures and day-to-day questions. And a property occupied by people who are here to work.</p><p>Call us or describe your property through the form: we will get back to you quickly and explain how we work.</p>"},
    ],
},
# ───────────────────────────── FAQ
{
    "key": "faq", "slug": "faq", "alt": "faq", "nav": "FAQ",
    "title": "Frequently Asked Questions | Eden Corporate Mobility",
    "desc": "Invoicing, housing types, areas covered, lead times, property owners: answers to the questions companies ask before trusting us with their employees in Paris.",
    "h1": "Frequently asked questions",
    "lead": "If your question is not here, call us: it is even faster.",
    "sections": [
        {"type": "faq", "items": [
            {"q": "How does your invoicing work?", "a": "<p>You receive one quote per request, itemising housing, transport and services. Once approved, we book and invoice your company on the terms stated in the quote. Your employees pay nothing up front and you have no expense claims to process.</p>"},
            {"q": "Why corporate housing rather than a standard rental?", "a": "<p>Because a standard French rental is designed to last years: long lease, high deposit, heavy paperwork, an empty flat. Corporate housing is designed for assignments: furnished and equipped, the right duration, booked in the company's name, one point of contact. You save weeks and manage nothing on site.</p>"},
            {"q": "Do you offer premium services for employees?", "a": "<p>Yes: welcome and settling-in, concierge during the stay, sport and activities, family support. À la carte or as a full programme. <a href=\"/en/wellbeing-services/\">See wellbeing services</a>.</p>"},
            {"q": "Can you manage several employees or projects at the same time?", "a": "<p>Yes. We house whole teams and follow several assignments in parallel. You keep one contact and a clear view of what is booked, for whom and until when.</p>"},
            {"q": "I own a property: how do I join your network?", "a": "<p>Call us or describe your property through the contact form. We will explain our criteria and, if it fits, arrange a visit. <a href=\"/en/property-owners/\">Learn more for property owners</a>.</p>"},
            {"q": "What types of housing do you offer?", "a": "<p>Furnished apartments for stays of a month or more, aparthotels for stays of a few weeks and hotels for short stays or last-minute arrivals. <a href=\"/en/housing/\">See housing options</a>.</p>"},
            {"q": "Who are your services for?", "a": "<p>Companies and organisations sending employees on assignment to Paris and the Île-de-France region: consulting firms, construction companies, NGOs, SMEs, mid-size companies and international groups. <a href=\"/en/who-we-serve/\">See how we work with each sector</a>.</p>"},
            {"q": "Which areas do you cover?", "a": "<p>Paris and the whole Île-de-France region. For an assignment elsewhere in France, call us and we will quickly tell you whether we can help.</p>"},
            {"q": "How long does it take to find housing for an employee?", "a": "<p>It depends on duration, location and number of people. For an individual request we come back quickly with options. For a team, tell us as early as possible: we will have more choice. In an emergency we can also arrange a hotel for the first nights.</p>"},
            {"q": "Do you offer a complete corporate mobility service?", "a": "<p>Yes: housing, transport and wellbeing services, coordinated by the same team and grouped in the same quote. You can also entrust us with only part of it, for example housing alone.</p>"},
            {"q": "What time zone are you in, and when can we call?", "a": "<p>We are in Paris (Central European Time). {{hours_en}}. Outside those hours, send the form and we will call you back.</p>"},
        ]},
    ],
},
# ───────────────────────────── CONTACT
{
    "key": "contact", "slug": "contact", "alt": "contact", "nav": "Contact", "cta": False, "priority": "high",
    "title": "Contact: call {{phone}} | Eden Corporate Mobility",
    "desc": "Talk to our team in Paris, in English or French, about housing and supporting your employees in Paris. By phone or through the form.",
    "h1": "Let's talk about your next assignment in Paris",
    "sections": [
        {"type": "contact", "heading": "The simplest way: call us", "intro": "In ten minutes we will understand your needs and tell you what we can do. In English or French. We are in Paris, Central European Time.",
         "aside": "<p class=\"muted\">Own a property? Use the same form and describe it.</p>",
         "form": {"heading": "Or describe your needs", "intro": "Dates, number of people, work location, budget: we will call you back.",
                  "success": "Thank you, your request has been sent. We will call you back shortly.",
                  "privacy": "Your details are used only to handle your request. <a href=\"/en/privacy-policy/\">Privacy policy</a>.",
                  "submit": "Send my request", "subject": "[Website] New contact request",
                  "fields": [
                      {"name": "name", "label": "Full name", "type": "text", "req": True, "ac": "name"},
                      {"name": "company", "label": "Company", "type": "text", "req": True, "ac": "organization"},
                      {"name": "role", "label": "Job title", "type": "text", "ac": "organization-title"},
                      {"name": "email", "label": "Email", "type": "email", "req": True, "ac": "email"},
                      {"name": "phone", "label": "Phone (with country code)", "type": "tel", "ac": "tel"},
                      {"name": "message", "label": "Your needs (dates, people, location, budget)", "type": "textarea", "req": True},
                  ]}},
    ],
},
# ───────────────────────────── LEGAL
{
    "key": "legal", "slug": "legal-notice", "alt": "mentions-legales", "nav": "Legal notice", "cta": False, "priority": "low",
    "title": "Legal Notice | Eden Corporate Mobility",
    "desc": "Legal notice for edencorporatemobility.com: publisher, publishing director, hosting provider.",
    "h1": "Legal notice",
    "sections": [{"type": "prose", "html": """
<h2>Website publisher</h2>
<p>{{raison_sociale}}, {{forme}}<br>Registered office: {{address}}<br>SIREN: {{siren}} — {{rcs}}<br>EU VAT number: {{tva}}<br>Phone: {{phone}} — Email: {{email}}<br>{{immatriculation}}</p>
<h2>Publishing director</h2>
<p>{{directeur}}</p>
<h2>Hosting</h2>
<p>{{host}}</p>
<h2>Intellectual property</h2>
<p>The whole of this website (texts, structure, trademarks, logos, visuals) is protected by intellectual property law. Any reproduction or representation, in whole or in part, without the written consent of {{name}} is prohibited.</p>
<h2>Personal data and cookies</h2>
<p>Information on how we process your data and use cookies is set out in our <a href="/en/privacy-policy/">privacy policy</a>.</p>
<h2>Liability</h2>
<p>{{name}} strives to keep the information on this site accurate and up to date but cannot guarantee its completeness. Links to third-party sites do not engage the publisher's liability.</p>
<p class="muted small">This English version is provided for convenience; the <a href="/mentions-legales/">French version</a> prevails.</p>
"""}],
},
{
    "key": "terms", "slug": "terms", "alt": "cgv", "nav": "Terms of service", "cta": False, "priority": "low",
    "title": "Terms of Service | Eden Corporate Mobility",
    "desc": "General terms of sale for Eden Corporate Mobility's housing, transport and wellbeing services for companies and organisations.",
    "h1": "General terms of sale",
    "lead": "Effective from {{lastmod}}. These terms apply to services provided to business customers. This translation is provided for convenience; the <a href=\"/cgv/\">French version</a> is the binding one.",
    "sections": [{"type": "prose", "html": """
<h2>1. Purpose and scope</h2>
<p>These general terms of sale ("Terms") govern the relationship between {{raison_sociale}} ({{forme}}, SIREN {{siren}}), hereafter "Eden", and any business customer (company, organisation, association), hereafter "the Client", for the following services: search, selection and booking of accommodation (furnished apartments, aparthotels, hotels), organisation of transport, welcome, concierge and wellbeing services, and any related service (the "Services"). Any order implies full acceptance of these Terms, which prevail over any document of the Client unless otherwise agreed in writing. Services provided to consumers are subject to specific terms available on request.</p>
<h2>2. Nature of the Services</h2>
<p>Eden acts as an intermediary and coordinator between the Client and the providers (owners, accommodation operators, transport companies, service providers). The Services are described in the quote. Unless stated otherwise in the quote, the Client remains responsible for the persons it houses (the "Occupants"), for their compliance with the rules of use of the accommodation and for any damage they cause.</p>
<h2>3. Quotes and orders</h2>
<p>Each request gives rise to a quote specifying the Services, dates, number of Occupants, prices and special conditions. The quote is valid for {{devis_validite}} from its issue date. The order becomes firm upon receipt of the accepted quote (signature, purchase order or written acceptance) and, where applicable, payment of the deposit stated. Eden then confirms the bookings. Any subsequent change (dates, Occupants, location) gives rise to an additional quote.</p>
<h2>4. Prices</h2>
<p>Prices are stated in euros, excluding VAT, which is added at the applicable rate. They include Eden's service fees and, as stated in the quote, the cost of accommodation, transport and services rebilled to the Client. Third-party prices may vary according to dates and availability until the order is confirmed. Eden's service fee schedule is available on request.</p>
<h2>5. Payment terms</h2>
<p>Unless otherwise stated in the quote, a deposit of {{acompte}} of the total amount is due on order, the balance being payable within {{delai_paiement}} days of the invoice date, by bank transfer. No discount is granted for early payment. In accordance with articles L. 441-10 and D. 441-5 of the French Commercial Code, any late payment automatically incurs late-payment interest at the European Central Bank's most recent refinancing rate plus 10 percentage points, together with a fixed recovery indemnity of 40 euros, without prejudice to additional compensation upon proof. Eden may suspend ongoing Services in the event of non-payment.</p>
<h2>6. Changes and cancellation</h2>
<p>Any request for change or cancellation must be made in writing. The cancellation conditions of third-party accommodation, transport and services, as stated in the quote, apply to the Client. Eden's service fees corresponding to work already performed remain due. In the event of cancellation less than {{annulation_delai}} before the start date of the Services, {{annulation_frais}} of the order amount remains due, unless the quote provides more favourable terms.</p>
<h2>7. Client obligations</h2>
<p>The Client undertakes to provide accurate and complete information (identity and number of Occupants, dates, special needs), to ensure that Occupants comply with the occupancy rules and house rules of the accommodation, to report any incident without delay and to pay any deposits, damage costs or additional services consumed by the Occupants.</p>
<h2>8. Eden's obligations</h2>
<p>Eden undertakes to select accommodation and providers with care, to perform the Services diligently, to remain reachable throughout the stay and, if confirmed accommodation becomes unavailable, to propose a replacement of equivalent standard. Eden is bound by an obligation of means.</p>
<h2>9. Liability</h2>
<p>Eden shall not be liable for non-performance or improper performance attributable to the Client, the Occupants, a third-party provider or force majeure. In any event, Eden's liability is limited to the amount, excluding VAT, of the service fees received for the order concerned, excluding any indirect loss (loss of business, loss of opportunity, reputational harm).</p>
<h2>10. Insurance</h2>
<p>Eden holds professional liability insurance {{assurance}}. The Client is responsible for insuring the Occupants and their belongings.</p>
<h2>11. Personal data</h2>
<p>Personal data of the Client's contacts and of the Occupants are processed in accordance with Eden's <a href="/en/privacy-policy/">privacy policy</a>, for the purposes of performing the Services.</p>
<h2>12. Confidentiality and intellectual property</h2>
<p>The parties undertake to keep confidential the information exchanged in the course of their business relationship. Documents, methods and content produced by Eden remain its property.</p>
<h2>13. Term and termination</h2>
<p>These Terms apply for the duration of the Services. In the event of a serious breach by either party not remedied within fifteen days of written notice, the other party may terminate the order as of right, without prejudice to sums due.</p>
<h2>14. Governing law and jurisdiction</h2>
<p>These Terms are governed by French law. Any dispute relating to their interpretation or performance shall, failing amicable settlement, be submitted to the Commercial Court of Paris, including for summary proceedings, third-party claims or multiple defendants. In the event of any discrepancy between the French version and a translation, the French version prevails.</p>
<p class="muted small">To be reviewed by your legal adviser before publication.</p>
"""}],
},
{
    "key": "privacy", "slug": "privacy-policy", "alt": "politique-de-confidentialite", "nav": "Privacy policy", "cta": False, "priority": "low",
    "title": "Privacy Policy & Cookies | Eden Corporate Mobility",
    "desc": "How Eden Corporate Mobility collects, uses and protects your personal data, and how cookies are managed on this website.",
    "h1": "Privacy policy",
    "lead": "Last updated: {{lastmod}}.",
    "sections": [{"type": "prose", "html": """
<h2>1. Data controller</h2>
<p>{{raison_sociale}} ({{name}}), {{address}} — {{email}} — {{phone}}.</p>
<h2>2. Data we collect</h2>
<p><strong>Through the contact form:</strong> full name, company, job title, email address, phone number, content of your message.<br><strong>In the course of a service:</strong> identity and contact details of the client's contacts and of the persons housed, stay dates, special needs relevant to organising the stay, billing data.<br><strong>When browsing:</strong> technical data (IP address, browser type, pages viewed) processed by our hosting provider for security and site operation, and, if you accept it, audience measurement data.</p>
<h2>3. Purposes and legal bases</h2>
<p>Answering your requests and preparing quotes (pre-contractual measures); performing and invoicing services (performance of a contract); complying with accounting and tax obligations (legal obligation); maintaining the business relationship with our business clients and informing you about our services (legitimate interest, with the right to object at any time); measuring site audience (consent).</p>
<h2>4. Recipients</h2>
<p>Your data are processed by Eden's team and, to the extent necessary to perform the services, shared with the providers concerned (owners and operators of accommodation, transport companies, service providers), as well as with our technical processors (website hosting, contact-form delivery by FormSubmit, email, management and invoicing tools). We do not sell your data.</p>
<h2>5. Transfers outside the European Union</h2>
<p>Our data are hosted in the European Union. Where one of our tools involves a transfer outside the EU, it is covered by appropriate safeguards (European Commission standard contractual clauses or an adequacy decision).</p>
<h2>6. Retention periods</h2>
<p>Contact requests without follow-up: 3 years from the last exchange. Client and occupant data: duration of the business relationship, then archived for the applicable limitation periods. Accounting documents and invoices: 10 years. Audience measurement data: 25 months maximum. Cookie choice: 6 months.</p>
<h2>7. Your rights</h2>
<p>You have the right to access, rectify, erase, restrict and object to the processing of your data, the right to data portability, and the right to give instructions regarding your data after your death. To exercise these rights, write to {{email}} or to the postal address above, with proof of identity. You may also lodge a complaint with the French data protection authority, the CNIL (cnil.fr).</p>
<h2>8. Cookies</h2>
<p>This site uses only cookies strictly necessary for its operation, which do not require your consent. If an audience measurement tool is enabled, a banner lets you accept or decline the corresponding cookies; your choice is kept for six months and can be changed at any time by deleting your browser's cookies. No advertising cookies are set.</p>
<h2>9. Security</h2>
<p>We implement appropriate technical and organisational measures to protect your data: encrypted connection (HTTPS), restricted access, backups, team awareness.</p>
<h2>10. Updates</h2>
<p>This policy may be updated to reflect changes in our services or in regulation. The version in force is the one published on this page.</p>
"""}],
},
]
