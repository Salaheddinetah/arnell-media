#!/usr/bin/env python3
"""Builds the bilingual single-page site.

  python3 build.py   ->  dist/index.html (Swedish, default)
                         dist/en/index.html (English)

Both files are complete, static, single-page HTML documents (CSS + JS inlined),
so search engines see fully rendered content in each language.
Edit copy in the CONTENT dict below, design in src/style.css, behaviour in src/script.js.
"""
import json, html, pathlib

ROOT = pathlib.Path(__file__).parent
DOMAIN = "https://arnellcompany.se"
EMAIL = "contact@arnellcompany.se"
FORM_ENDPOINT = "https://formsubmit.co/ajax/" + EMAIL   # works after first-submission email confirmation
YEAR = 2026

e = html.escape

CONTENT = {
"sv": dict(
    lang="sv", locale="sv-SE", og_locale="sv_SE", og_alt="en_GB", path="/",
    title="Arnell Company – Integrationer och automation för små företag",
    desc="Jag kopplar ihop de system ert företag redan använder – Fortnox, e-handel, lager, bokning och rekrytering – och automatiserar det som görs för hand. Fast pris per flöde.",
    og_title="Arnell Company – Integrationer och automation för små företag",
    skip="Hoppa till innehållet",
    nav=[("services","Branscher"),("flows","Exempel"),("pricing","Pris"),("faq","Vanliga frågor")],
    nav_cta="Kontakta mig", menu="Meny", lang_label="Språk",
    hero_eyebrow="Integrationer · Automation · n8n · Fortnox",
    hero_h1="Era system ska prata med varandra. <em>Inte genom er.</em>",
    hero_lead="Jag bygger integrationer och automatiska flöden mellan de system ni redan betalar för – bokföring, webbshop, lager, bokning och rekrytering. Det som i dag kopieras, jagas eller stäms av för hand sköts av ett flöde som övervakas.",
    hero_cta1="Boka ett kostnadsfritt samtal (30 min)", hero_cta2="Se branscher och exempel",
    hero_notes=["Svar inom en arbetsdag","Fast pris per flöde"],
    term_title="Exempel: underlagsjakt för redovisningsbyrå", term_status="körs",
    term_lines=[("06:00","Kontroll mot Fortnox: 14 klienter"),("06:00","3 klienter saknar underlag för oktober"),("06:01","Påminnelse skickad till 3 klienter"),("06:01","Avvikelse loggad – handläggare notifierad"),("06:02","Veckorapport uppdaterad")],
    term_foot="Illustration. Varje flöde byggs efter era system och regler.",
    value_eyebrow="Varför Arnell Company",
    value_h2="En utvecklare, ett flöde i taget.",
    value_lead="Du pratar direkt med mig som bygger lösningen. Jag börjar med det som kostar mest tid, bygger ett flöde till fast pris och tar hand om det efteråt. Finns det redan en färdig app som löser problemet säger jag det.",
    value_items=[
        ("Ett flöde i taget","Vi börjar avgränsat. När det första flödet fungerar tar vi nästa."),
        ("Fast pris","Omfattning och pris bestäms innan jag börjar – inga överraskande fakturor."),
        ("Era system, er data","Varje kund får en egen n8n-installation. Flödena tillhör er."),
        ("Övervakat","Varje flöde loggar fel och larmar mig, så att problem upptäcks tidigt."),
    ],
    svc_eyebrow="Branscher",
    svc_h2="Fem typer av företag jag bygger för.",
    svc_more="Se exempel",
    svc=[
        ("flows","Redovisningsbyråer","Underlag som jagas automatiskt inför moms och AGI, och en översikt över tid och lönsamhet per klient."),
        ("flows","E-handel med extern lagerpartner","Lager-, order- och returvakt mellan webbshop, Ongoing WMS och Fortnox, plus marginal per order."),
        ("flows","Estetiska kliniker","Från förfrågan till konsultation och återbesök – utan att journal- eller hälsouppgifter lämnar ert system."),
        ("flows","Installatörer – sol, batteri, laddbox","Grön teknik-underlag kontrollerade inför Skatteverket, och förfrågningar från offertportaler till signerad order."),
        ("flows","Bemanning & rekrytering","Från tillsatt kandidat i Teamtailor till fakturautkast i Fortnox, med rapporter per kund."),
    ],
    a_tag="01 · Så fungerar det",
    a_h2="Ni behåller era system. Jag bygger det som saknas mellan dem.",
    a_p=["De flesta företag har redan bra system för bokföring, försäljning och bokning. Problemet är det som händer mellan dem: uppgifter som förs över för hand, avstämningar i Excel och påminnelser som någon måste komma ihåg.",
         "Jag bygger flödena i n8n, ett verktyg för arbetsflöden där en händelse – en betald faktura, en ny order, en tillsatt kandidat – startar en kedja av kontroller och steg. Varje kund får en egen n8n-installation, och jag övervakar flödena löpande."],
    a_signs_h="Tecken på att ni behöver ett flöde",
    a_signs=["Samma uppgifter skrivs in i två eller fler system.","Någon stämmer av siffror mellan system varje vecka eller månad.","Ni jagar kunder, klienter eller kollegor på samma uppgifter om och om igen.","Rapporten ni vill ha kräver data från flera system."],
    a_ex_h="Det här brukar flödena göra",
    a_ex=["Kontrollera och flagga avvikelser","Påminna inför deadlines","Skapa utkast i Fortnox","Synka status mellan system","Sammanställa rapporter från flera källor","Larma när något fastnar","Flytta data vid systembyte","Koppla system som saknar färdig integration"],
    flow_t="Exempel: returvakt för e-handel",
    flow=[("IN","Retur registreras","I lagersystemet (Ongoing WMS)"),("n8n","Flödet startar","Ordern matchas och kontrolleras"),("SHOP","Återbetalning förbereds","Utkast i webbshopen för godkännande"),("FTX","Kreditfaktura","Utkast skapas i Fortnox"),("OUT","Avvikelser larmas","Ni får en notis om något inte stämmer")],
    a_benefit="Resultatet: färre manuella steg, färre missade fel och siffror ni kan lita på.",
    b_tag="02 · Exempel på flöden",
    b_h2="Konkreta flöden, inte allmän automation.",
    b_lead="Några exempel på vad jag bygger. Varje flöde avgränsas och prissätts för sig, och byggs efter era system och regler.",
    b_items=[
        ("Underlagsjakten · redovisningsbyrå","Kontrollerar varje natt vilka klienter som saknar underlag i Fortnox och skickar påminnelser inför moms- och AGI-deadlines."),
        ("Klientöversikt · redovisningsbyrå","Tid, ofakturerat arbete och intäkt per klient i en veckorapport, med flagga när marginalen är för låg."),
        ("Lager- och returvakt · e-handel","Larm vid lågt lager, fastnade ordrar och returer, med utkast till återbetalning och kreditfaktura."),
        ("Marginal per order · e-handel","Försäljning, inköpspris, frakt och avgifter samlade till marginal per order, produkt och kanal."),
        ("Förfrågan till konsultation · klinik","Förfrågningar från annonser och webbplats följs upp tills de bokat konsultation. Bara kontaktuppgifter och tider hanteras."),
        ("Grön teknik-underlag · installatör","Betalda fakturor kontrolleras mot det Skatteverket kräver, saknade uppgifter listas och underlaget är klart i god tid före 31 januari."),
        ("Förfrågan till order · installatör","Förfrågningar från offertportaler samlas, följs upp och blir kund och projekt i Fortnox när offerten är signerad."),
        ("Tillsättning till faktura · bemanning","När en kandidat markeras som anställd i Teamtailor skapas kund och fakturautkast i Fortnox."),
    ],
    b_note="Flöden för kliniker hanterar aldrig journaluppgifter, bilder eller behandlingsdetaljer – bara kontaktuppgifter, tider, belopp och samtycke.",
    c_tag="03 · Det här bygger jag inte",
    c_h2="Finns det redan en färdig app säger jag det.",
    c_lead="Många vanliga kopplingar löses redan av färdiga appar för några hundra kronor i månaden. Då är det bättre att ni använder dem. Jag bygger det som ligger mellan systemen och som ingen app gör åt er.",
    infra_env="Er egen miljö", infra_in=("Era system","Fortnox, webbshop, lager, ATS"), infra_core=("Egen n8n-installation","en per kund"), infra_out=("Kontroller & rapporter","larm, utkast, översikter"),
    infra_ext_s="Hålls utanför", infra_ext_b="Känsliga uppgifter", infra_ext_t="Journaler och hälsodata flyttas aldrig",
    c_adv_h="Det här köper ni hellre färdigt",
    c_adv=["Standardkoppling mellan webbshop och Fortnox","Avstämning av Swish, Klarna och Stripe","Kundkännedom (KYC) för redovisningsbyråer","Bokningspåminnelser och förskottsbetalning","Fakturering direkt från arbetsorder-appen"],
    c_srv_h="Så hanteras er data",
    c_srv=["En separat n8n-installation per kund","Drift inom EU","Personuppgiftsbiträdesavtal med varje kund","Bara de uppgifter flödet behöver","Ni äger flödena och kan ta dem vidare"],
    cmp_cap="Färdig app jämfört med eget flöde", cmp_head=("","Färdig app","Eget flöde"),
    cmp_rows=[("Passar när","Behovet är standard","Behovet är specifikt för er"),
              ("Kostnad","Månadsavgift, ofta låg","Fast pris för bygget och en månadsavgift för drift"),
              ("Anpassning","Begränsad till appens inställningar","Era regler och undantag"),
              ("Antal system","Oftast två","Så många som behövs"),
              ("Ansvar","Leverantören","Jag, enligt avtal")],
    c_note="En egen installation ger bättre kontroll, men är inte automatiskt säker eller GDPR-anpassad. Hur data hanteras bedöms för varje flöde.",
    d_tag="04 · Pris",
    d_h2="Så prissätter jag.",
    d_lead="Inget timpris som tickar. Ni får ett fast pris för varje flöde innan jag börjar, och en månadsavgift som täcker drift, övervakning och mindre justeringar. Exakt pris lämnas efter det första samtalet.",
    d_col1=("Det här betalar ni för",["Kostnadsfritt första samtal, 30 minuter","Förstudie för större uppdrag – avräknas mot bygget","Fast pris per flöde","Månadsavgift för drift och övervakning","Servrar och licenser till självkostnad"]),
    d_col2=("Det här ingår alltid",["Felloggning och larm","Dokumentation av varje flöde","Test med verkliga data innan start","Justeringar när ett system ändras","Ni äger flödena"]),
    p_eyebrow="Så arbetar jag", p_h2="Fyra steg, ett flöde i taget.",
    p_steps=[("Samtal","30 minuter om vad som tar tid och vilka system ni har. Kostnadsfritt."),("Förslag","Ett avgränsat flöde med fast pris och tidsplan. Jag kontrollerar först om en färdig app räcker."),("Bygge och test","Jag bygger flödet i er egen n8n-miljö och testar med verkliga data."),("Drift","Flödet övervakas löpande. När det fungerar tar vi nästa.")],
    u_eyebrow="Passar bäst för", u_h2="Företag som har systemen men saknar kopplingen.",
    u_lead="Mina kunder har oftast 2–50 anställda och använder flera system som inte pratar med varandra.",
    u_items=[("Ni använder Fortnox eller Bokio","Och minst ett system till – webbshop, lager, rekryteringssystem eller bokning."),("Någon gör samma sak varje vecka","Avstämningar, påminnelser eller rapporter som tar timmar."),("Fel kostar pengar","Missade deadlines, fel lagersaldo eller fakturor som aldrig skickas."),("Ni vill äga lösningen","Flödena dokumenteras och tillhör er, även om ni byter leverantör."),("Mindre bra passform","Om en färdig app löser problemet, eller om ni bara behöver en enstaka export.")],
    k_eyebrow="Räkna på det", k_h2="Hur mycket tid går åt till manuellt arbete mellan systemen?",
    k_lead="Fyll i en uppgift som görs om och om igen. Resultatet är en enkel uppskattning baserad på era egna siffror.",
    k_n="Antal gånger per vecka", k_m="Minuter per gång", k_r="Timkostnad (kr)", k_p="Andel som går att automatisera",
    k_rl1="Möjlig tid att frigöra", k_rl2="Motsvarande kostnad", k_h="timmar / månad", k_k="kr / månad",
    k_fine="Grov uppskattning (4,33 veckor per månad). Verklig besparing varierar och bedöms i ett första samtal. Det är inget löfte.",
    k_cta="Diskutera ett flöde",
    k_msg="Hej! Jag vill diskutera ett flöde för en återkommande uppgift. Den utförs ca {n} gånger i veckan och tar ca {min} minuter varje gång. Enligt kalkylatorn motsvarar det ca {h} timmar i månaden.",
    f_eyebrow="Vanliga frågor", f_h2="Svar på det de flesta undrar över.",
    faq=[
        ("Vad gör du, kort?","Jag kopplar ihop de system ett företag redan använder och automatiserar återkommande arbete mellan dem, till exempel påminnelser, avstämningar, utkast i Fortnox och rapporter. Jag bygger i n8n och tar hand om flödena efteråt."),
        ("Bygger du AI-chattbotar?","Nej, det är inte mitt fokus. Jag bygger integrationer och automatiska flöden. Där AI gör nytta, till exempel för att läsa av ett dokument, kan det ingå som ett steg i ett flöde."),
        ("Varför inte Zapier eller en färdig app?","Om en färdig app löser ert behov rekommenderar jag den. Ett eget flöde lönar sig när ni har egna regler, flera system eller system som saknar färdiga kopplingar."),
        ("Behöver vi Fortnox integrationslicens?","Ja, integrationer mot Fortnox kräver Fortnox integrationslicens. Den ingår i vissa av Fortnox paket och kan annars läggas till. Jag hjälper er att kontrollera vad som gäller för er."),
        ("Vem äger flödena?","Ni. Varje kund får en egen n8n-installation och flödena dokumenteras. Om vi slutar samarbeta kan ni ta över dem själva eller lämna dem till någon annan."),
        ("Vad händer om ett system ändras?","Flödena loggar fel och larmar mig. Mindre justeringar när ett system ändras ingår i månadsavgiften."),
        ("Hur hanteras personuppgifter?","Jag är personuppgiftsbiträde och tecknar ett avtal med varje kund. Flödena hanterar bara de uppgifter som behövs och driften sker inom EU. Det gör inte en lösning automatiskt GDPR-anpassad – det bedöms för varje flöde."),
        ("Hur lång tid tar det?","Det beror främst på hur snabbt vi får åtkomst till era system. Ett avgränsat flöde går fort när åtkomsten är på plats. Ni får en tidsplan i förslaget."),
        ("Vad kostar det?","Fast pris per flöde och en månadsavgift för drift. Exakt pris lämnas efter första samtalet, när jag vet vilka system som ingår. Samtalet är kostnadsfritt."),
        ("Bygger du fortfarande webbplatser?","Ja, men mitt fokus är integrationer och automation. Hör av dig om du behöver båda."),
    ],
    t_eyebrow="Kontakt", t_h2="Berätta vad som tar tid i dag.",
    t_lead="Skriv kort vilka system ni använder och vad som görs för hand. Jag svarar inom en arbetsdag. Första samtalet är kostnadsfritt och förpliktar till ingenting.",
    t_cta_mail="Eller mejla direkt:",
    form=dict(name="Namn",email="E-post",company="Företag",optional="valfritt",topic="Vilken bransch?",msg="Meddelande",msg_ph="Vilka system använder ni och vad görs för hand i dag?",
              topics=[("accounting","Redovisningsbyrå"),("ecommerce","E-handel / lager"),("clinic","Klinik"),("installer","Installatör (sol, batteri, laddbox, värmepump)"),("staffing","Bemanning / rekrytering"),("other","Annat / vet inte än")],
              consent="Jag godkänner att Arnell Company behandlar mina uppgifter för att besvara min förfrågan. Läs mer under",consent_link="Integritet",send="Skicka förfrågan",sending="Skickar …",
              ok="Tack! Jag har fått din förfrågan och svarar inom en arbetsdag.",err="Något gick fel. Skriv gärna direkt till"),
    foot_tag="Integrationer och automation för små företag.", foot_nav="Navigering", foot_contact="Kontakt", foot_lang="Språk",
    foot_links=[("services","Branscher"),("how","Så fungerar det"),("flows","Exempel på flöden"),("scope","Det här bygger jag inte"),("pricing","Pris"),("faq","Vanliga frågor")],
    priv_h="Integritet", priv_p="Uppgifterna du skickar via kontaktformuläret används bara för att besvara din förfrågan och följa upp kontakten. Jag säljer inte uppgifterna och delar dem inte med tredje part för marknadsföring. Formuläret levereras som e-post via tjänsten FormSubmit. Vill du att jag raderar dina uppgifter kan du mejla mig. Webbplatsen använder inga marknadsföringscookies.",
    rights="Alla rättigheter förbehållna.", to_top="Till toppen",
    subject="Ny förfrågan från arnellcompany.se (sv)",
    schema_desc="Arnell Company bygger integrationer och automatiska flöden i n8n för små företag i Sverige: redovisningsbyråer, e-handel, kliniker, installatörer och bemanningsföretag.",
),
"en": dict(
    lang="en", locale="en-GB", og_locale="en_GB", og_alt="sv_SE", path="/en/",
    title="Arnell Company – Integrations and Automation for Small Businesses",
    desc="I connect the systems your business already uses – Fortnox, e-commerce, warehouse, booking and recruitment – and automate the work done by hand. Fixed price per workflow.",
    og_title="Arnell Company – Integrations and Automation for Small Businesses",
    skip="Skip to content",
    nav=[("services","Industries"),("flows","Examples"),("pricing","Pricing"),("faq","FAQ")],
    nav_cta="Get in touch", menu="Menu", lang_label="Language",
    hero_eyebrow="Integrations · Automation · n8n · Fortnox",
    hero_h1="Your systems should talk to each other. <em>Not through you.</em>",
    hero_lead="I build integrations and automated workflows between the systems you already pay for – accounting, web shop, warehouse, booking and recruitment. What is copied, chased or reconciled by hand today is handled by a monitored workflow.",
    hero_cta1="Book a free 30-minute call", hero_cta2="See industries and examples",
    hero_notes=["Reply within one business day","Fixed price per workflow"],
    term_title="Example: missing-documents check for an accounting firm", term_status="running",
    term_lines=[("06:00","Check against Fortnox: 14 clients"),("06:00","3 clients missing October documents"),("06:01","Reminder sent to 3 clients"),("06:01","Exception logged – accountant notified"),("06:02","Weekly report updated")],
    term_foot="Illustration. Every workflow is built around your systems and rules.",
    value_eyebrow="Why Arnell Company",
    value_h2="One developer, one workflow at a time.",
    value_lead="You talk directly to me, the person building the solution. I start with what costs you the most time, build one workflow at a fixed price and look after it afterwards. If a ready-made app already solves the problem, I will tell you.",
    value_items=[
        ("One workflow at a time","We start small. Once the first workflow works, we take the next."),
        ("Fixed price","Scope and price are agreed before I start – no surprise invoices."),
        ("Your systems, your data","Every client gets their own n8n installation. The workflows are yours."),
        ("Monitored","Every workflow logs errors and alerts me, so problems are caught early."),
    ],
    svc_eyebrow="Industries",
    svc_h2="Five kinds of business I build for.",
    svc_more="See examples",
    svc=[
        ("flows","Accounting firms","Automatic chasing of missing client documents before VAT and payroll deadlines, plus an overview of hours and profitability per client."),
        ("flows","E-commerce with a 3PL warehouse","Stock, order and returns monitoring between web shop, Ongoing WMS and Fortnox, plus margin per order."),
        ("flows","Aesthetic clinics","From enquiry to consultation and follow-up visit – without patient records or health data leaving your system."),
        ("flows","Installers – solar, battery, EV chargers","Green-technology tax deduction data checked before it goes to Skatteverket, and leads from quote portals to signed orders."),
        ("flows","Staffing & recruitment","From a hired candidate in Teamtailor to a draft invoice in Fortnox, with reports per client."),
    ],
    a_tag="01 · How it works",
    a_h2="You keep your systems. I build what is missing between them.",
    a_p=["Most businesses already have good systems for accounting, sales and booking. The problem is what happens between them: data copied by hand, reconciliations in Excel and reminders someone has to remember.",
         "I build the workflows in n8n, a workflow tool where an event – a paid invoice, a new order, a hired candidate – starts a chain of checks and steps. Every client gets their own n8n installation, and I monitor the workflows continuously."],
    a_signs_h="Signs you need a workflow",
    a_signs=["The same data is entered into two or more systems.","Someone reconciles figures between systems every week or month.","You chase customers, clients or colleagues for the same information again and again.","The report you want needs data from several systems."],
    a_ex_h="What the workflows typically do",
    a_ex=["Check and flag exceptions","Send reminders before deadlines","Create drafts in Fortnox","Sync status between systems","Compile reports from several sources","Alert when something gets stuck","Move data when you switch systems","Connect systems without a ready-made integration"],
    flow_t="Example: returns monitoring for e-commerce",
    flow=[("IN","Return registered","In the warehouse system (Ongoing WMS)"),("n8n","Workflow starts","The order is matched and checked"),("SHOP","Refund prepared","Draft in the web shop for approval"),("FTX","Credit note","Draft created in Fortnox"),("OUT","Exceptions flagged","You are notified if something does not match")],
    a_benefit="The result: fewer manual steps, fewer missed errors and figures you can trust.",
    b_tag="02 · Example workflows",
    b_h2="Specific workflows, not general automation.",
    b_lead="A few examples of what I build. Each workflow is scoped and priced on its own, and built around your systems and rules.",
    b_items=[
        ("Missing-documents chaser · accounting firm","Checks every night which clients are missing documents in Fortnox and sends reminders before VAT and payroll deadlines."),
        ("Client overview · accounting firm","Hours, unbilled work and revenue per client in a weekly report, flagged when the margin is too low."),
        ("Stock and returns monitor · e-commerce","Alerts for low stock, stuck orders and returns, with draft refunds and credit notes."),
        ("Margin per order · e-commerce","Sales, purchase cost, shipping and fees combined into margin per order, product and channel."),
        ("Enquiry to consultation · clinic","Enquiries from ads and the website are followed up until a consultation is booked. Only contact details and times are handled."),
        ("Green-tech deduction data · installer","Paid invoices are checked against what Skatteverket requires, missing details are listed and the data is ready well before 31 January."),
        ("Enquiry to order · installer","Enquiries from quote portals are collected, followed up and become a customer and project in Fortnox when the quote is signed."),
        ("Placement to invoice · staffing","When a candidate is marked as hired in Teamtailor, a customer and draft invoice are created in Fortnox."),
    ],
    b_note="Clinic workflows never handle patient records, photos or treatment details – only contact details, times, amounts and consent.",
    c_tag="03 · What I do not build",
    c_h2="If a ready-made app exists, I will tell you.",
    c_lead="Many common connections are already solved by ready-made apps for a few hundred kronor a month. Then you are better off using them. I build what sits between your systems and that no app does for you.",
    infra_env="Your own environment", infra_in=("Your systems","Fortnox, web shop, warehouse, ATS"), infra_core=("Own n8n installation","one per client"), infra_out=("Checks & reports","alerts, drafts, overviews"),
    infra_ext_s="Kept out", infra_ext_b="Sensitive data", infra_ext_t="Patient records and health data never move",
    c_adv_h="Better bought ready-made",
    c_adv=["Standard web shop to Fortnox sync","Swish, Klarna and Stripe payout reconciliation","Customer due diligence (KYC) for accounting firms","Booking reminders and deposits","Invoicing straight from the work-order app"],
    c_srv_h="How your data is handled",
    c_srv=["A separate n8n installation per client","Hosted within the EU","A data processing agreement with every client","Only the data the workflow needs","You own the workflows and can take them elsewhere"],
    cmp_cap="Ready-made app compared with your own workflow", cmp_head=("","Ready-made app","Own workflow"),
    cmp_rows=[("Fits when","The need is standard","The need is specific to you"),
              ("Cost","Monthly fee, often low","Fixed build price plus a monthly fee for operation"),
              ("Customisation","Limited to the app's settings","Your rules and exceptions"),
              ("Number of systems","Usually two","As many as needed"),
              ("Responsibility","The vendor","Me, as agreed")],
    c_note="Your own installation gives you more control, but it is not automatically secure or GDPR-compliant. How data is handled is assessed for each workflow.",
    d_tag="04 · Pricing",
    d_h2="How I price.",
    d_lead="No ticking hourly rate. You get a fixed price for each workflow before I start, and a monthly fee that covers operation, monitoring and minor adjustments. The exact price is given after the first call.",
    d_col1=("What you pay for",["Free first call, 30 minutes","Scoping for larger projects – credited against the build","Fixed price per workflow","Monthly fee for operation and monitoring","Servers and licences at cost"]),
    d_col2=("Always included",["Error logging and alerts","Documentation of every workflow","Testing with real data before go-live","Adjustments when a system changes","You own the workflows"]),
    p_eyebrow="How I work", p_h2="Four steps, one workflow at a time.",
    p_steps=[("Call","30 minutes on what takes time and which systems you use. Free of charge."),("Proposal","One scoped workflow with a fixed price and timeline. I first check whether a ready-made app would do."),("Build and test","I build the workflow in your own n8n environment and test it with real data."),("Operation","The workflow is monitored continuously. Once it works, we take the next.")],
    u_eyebrow="Best fit", u_h2="Businesses that have the systems but lack the connection.",
    u_lead="My clients usually have 2–50 employees and use several systems that do not talk to each other.",
    u_items=[("You use Fortnox or Bokio","And at least one other system – web shop, warehouse, recruitment system or booking."),("Someone does the same thing every week","Reconciliations, reminders or reports that take hours."),("Mistakes cost money","Missed deadlines, wrong stock levels or invoices that never go out."),("You want to own the solution","The workflows are documented and yours, even if you change supplier."),("Not a good fit","If a ready-made app solves the problem, or you only need a one-off export.")],
    k_eyebrow="Do the maths", k_h2="How much time goes into manual work between your systems?",
    k_lead="Enter a task that is done over and over. The result is a simple estimate based on your own figures.",
    k_n="Times per week", k_m="Minutes each time", k_r="Hourly cost (SEK)", k_p="Share that can be automated",
    k_rl1="Time that could be freed", k_rl2="Equivalent cost", k_h="hours / month", k_k="SEK / month",
    k_fine="Rough estimate (4.33 weeks per month). Actual savings vary and are assessed in a first call. This is not a promise.",
    k_cta="Discuss a workflow",
    k_msg="Hi! I would like to discuss a workflow for a recurring task. It is done about {n} times a week and takes about {min} minutes each time. According to the calculator that is about {h} hours a month.",
    f_eyebrow="FAQ", f_h2="Answers to the most common questions.",
    faq=[
        ("What do you do, in short?","I connect the systems a business already uses and automate recurring work between them, such as reminders, reconciliations, drafts in Fortnox and reports. I build in n8n and look after the workflows afterwards."),
        ("Do you build AI chatbots?","No, that is not my focus. I build integrations and automated workflows. Where AI is useful, for example to read a document, it can be one step in a workflow."),
        ("Why not Zapier or a ready-made app?","If a ready-made app covers your needs, I will recommend it. Your own workflow pays off when you have your own rules, several systems or systems without ready-made connections."),
        ("Do we need a Fortnox integration licence?","Yes, integrations with Fortnox require Fortnox's integration licence. It is included in some Fortnox packages and can otherwise be added. I will help you check what applies to you."),
        ("Who owns the workflows?","You do. Every client gets their own n8n installation and the workflows are documented. If we stop working together, you can take them over or hand them to someone else."),
        ("What happens if a system changes?","The workflows log errors and alert me. Minor adjustments when a system changes are included in the monthly fee."),
        ("How is personal data handled?","I act as a data processor and sign an agreement with every client. The workflows only handle the data they need, and hosting is within the EU. That does not make a solution automatically GDPR-compliant – it is assessed for each workflow."),
        ("How long does it take?","Mostly it depends on how quickly we get access to your systems. A scoped workflow moves fast once access is in place. You get a timeline in the proposal."),
        ("What does it cost?","A fixed price per workflow and a monthly fee for operation. The exact price is given after the first call, once I know which systems are involved. The call is free."),
        ("Do you still build websites?","Yes, but my focus is integrations and automation. Get in touch if you need both."),
    ],
    t_eyebrow="Contact", t_h2="Tell me what takes time today.",
    t_lead="Briefly describe which systems you use and what is done by hand. I reply within one business day. The first call is free and carries no obligation.",
    t_cta_mail="Or email directly:",
    form=dict(name="Name",email="Email",company="Company",optional="optional",topic="Which industry?",msg="Message",msg_ph="Which systems do you use and what is done by hand today?",
              topics=[("accounting","Accounting firm"),("ecommerce","E-commerce / warehouse"),("clinic","Clinic"),("installer","Installer (solar, battery, EV charger, heat pump)"),("staffing","Staffing / recruitment"),("other","Other / not sure yet")],
              consent="I agree that Arnell Company processes my details to respond to my enquiry. Read more under",consent_link="Privacy",send="Send enquiry",sending="Sending …",
              ok="Thank you! I have received your enquiry and will reply within one business day.",err="Something went wrong. Please write directly to"),
    foot_tag="Integrations and automation for small businesses.", foot_nav="Navigation", foot_contact="Contact", foot_lang="Language",
    foot_links=[("services","Industries"),("how","How it works"),("flows","Example workflows"),("scope","What I do not build"),("pricing","Pricing"),("faq","FAQ")],
    priv_h="Privacy", priv_p="The details you send through the contact form are used only to respond to your enquiry and follow up on the contact. I do not sell them or share them with third parties for marketing. The form is delivered as an email via the FormSubmit service. If you would like your details deleted, email me. This website does not use marketing cookies.",
    rights="All rights reserved.", to_top="Back to top",
    subject="New enquiry from arnellcompany.se (en)",
    schema_desc="Arnell Company builds integrations and automated workflows in n8n for small businesses in Sweden: accounting firms, e-commerce, clinics, installers and staffing companies.",
),
}

def sv_en_urls(c):
    return DOMAIN + "/", DOMAIN + "/en/"

def build_schema(c, lang):
    sv_url, en_url = sv_en_urls(c)
    url = sv_url if lang == "sv" else en_url
    org = {"@type": ["Organization", "ProfessionalService"], "@id": sv_url + "#org",
           "name": "Arnell Company", "url": sv_url, "logo": DOMAIN + "/logo.png", "image": DOMAIN + "/og-image.png",
           "email": EMAIL, "description": c["schema_desc"],
           "areaServed": [{"@type": "Country", "name": "Sweden"}], "knowsLanguage": ["sv", "en"],
           "availableLanguage": ["Swedish", "English"]}
    services = []
    for i, (sid, name, d) in enumerate(c["svc"]):
        services.append({"@type": "Service", "@id": f"{url}#service-{i+1}", "name": name, "description": d,
                         "url": f"{url}#{sid}", "provider": {"@id": sv_url + "#org"}, "areaServed": "SE",
                         "inLanguage": lang})
    faq = {"@type": "FAQPage", "@id": url + "#faq-schema", "inLanguage": lang,
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
    site = {"@type": "WebSite", "@id": sv_url + "#website", "url": sv_url, "name": "Arnell Company",
            "inLanguage": ["sv", "en"], "publisher": {"@id": sv_url + "#org"}}
    page = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": c["title"], "description": c["desc"],
            "inLanguage": lang, "isPartOf": {"@id": sv_url + "#website"}, "about": {"@id": sv_url + "#org"}}
    return json.dumps({"@context": "https://schema.org", "@graph": [org, site, page] + services + [faq]}, ensure_ascii=False, indent=2)

def render(lang):
    c = CONTENT[lang]
    css = (ROOT / "src/style.css").read_text(encoding="utf-8")
    js = (ROOT / "src/script.js").read_text(encoding="utf-8")
    sv_url, en_url = sv_en_urls(c)
    canon = sv_url if lang == "sv" else en_url
    f = c["form"]
    i18n = {"lang": lang, "locale": c["locale"], "email": EMAIL, "subject": c["subject"], "sending": f["sending"],
            "ok": f["ok"], "err": f["err"], "calcMsg": c["k_msg"]}

    nav_items = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in c["nav"])
    if lang == "sv":
        sw = (f'<a href="/" hreflang="sv" lang="sv" aria-current="true">SV</a>'
              f'<a href="/en/" hreflang="en" lang="en" data-lang-link>EN</a>')
    else:
        sw = (f'<a href="/" hreflang="sv" lang="sv" data-lang-link>SV</a>'
              f'<a href="/en/" hreflang="en" lang="en" aria-current="true">EN</a>')

    term = "".join(f'<li class="ok"><time>{t}</time><span>{e(s)}</span></li>' for t, s in c["term_lines"])
    value = "".join(f'<li><div><h3>{e(h)}</h3><p>{e(p)}</p></div></li>' for h, p in c["value_items"])
    svc = "".join(f'<li><a href="#{sid}"><span class="n">0{i+1}</span><h3>{e(n)}</h3><p>{e(d)}</p><span class="arr" aria-hidden="true">→</span></a></li>'
                  for i, (sid, n, d) in enumerate(c["svc"]))
    checks = lambda items, cls="": f'<ul class="checks {cls}">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"
    flow = "".join(f'<li><span class="dot">{k}</span><div><strong>{e(t)}</strong><span>{e(s)}</span></div></li>' for k, t, s in c["flow"])
    ai = "".join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in c["b_items"])
    steps = "".join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in c["p_steps"])
    uc = "".join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in c["u_items"])
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in c["faq"])
    ch = c["cmp_head"]
    cmp_rows = "".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td><td>{e(d)}</td></tr>' for a, b, d in c["cmp_rows"])
    topics = "".join(f'<option value="{v}">{e(t)}</option>' for v, t in f["topics"])
    foot_links = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in c["foot_links"])
    d1h, d1 = c["d_col1"]; d2h, d2 = c["d_col2"]

    page = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c["title"])}</title>
<meta name="description" content="{e(c["desc"])}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="sv" href="{sv_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{sv_url}">
<meta name="theme-color" content="#F6F4EE">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Arnell Company">
<meta property="og:title" content="{e(c["og_title"])}">
<meta property="og:description" content="{e(c["desc"])}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{c["og_locale"]}">
<meta property="og:locale:alternate" content="{c["og_alt"]}">
<meta property="og:image" content="{DOMAIN}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(c["og_title"])}">
<meta name="twitter:description" content="{e(c["desc"])}">
<meta name="twitter:image" content="{DOMAIN}/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..800&family=Hanken+Grotesk:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script type="application/ld+json">
{build_schema(c, lang)}
</script>
<!-- Analytics: add your Plausible / GA4 / Search Console snippet here. Events (cta_click, generate_lead, language_switch,
     calculator_use, email_click) are already pushed to window.dataLayer and forwarded to gtag()/plausible() if present. -->
<style>
{css}
</style>
</head>
<body id="top">
<a class="skip" href="#main">{e(c["skip"])}</a>

<header class="nav">
  <div class="wrap nav-in">
    <a class="logo" href="{c["path"]}#top" aria-label="Arnell Company"><img src="/logo.png" width="160" height="30" alt="Arnell Company"></a>
    <button class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="nav-links" aria-label="{e(c["menu"])}"><span></span><span></span><span></span></button>
    <nav aria-label="{e(c["menu"])}" style="display:contents">
    <ul class="nav-links" id="nav-links">
      {nav_items}
      <li><a class="btn btn-primary btn-sm" href="#contact">{e(c["nav_cta"])}</a></li>
      <li class="lang-li"><span class="lang" role="group" aria-label="{e(c["lang_label"])}">{sw}</span></li>
    </ul>
    </nav>
  </div>
</header>

<main id="main">

<section class="hero" id="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">{e(c["hero_eyebrow"])}</p>
      <h1>{c["hero_h1"]}</h1>
      <p class="lead">{e(c["hero_lead"])}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#contact">{e(c["hero_cta1"])}</a>
        <a class="btn btn-ghost" href="#services">{e(c["hero_cta2"])}</a>
      </div>
      <p class="hero-note">{"".join(f"<span>{e(n)}</span>" for n in c["hero_notes"])}</p>
    </div>
    <figure class="term" aria-label="{e(c["term_title"])}">
      <div class="term-bar"><i></i><i></i><i></i><span>{e(c["term_title"])}</span><b>● {e(c["term_status"])}</b></div>
      <ol>{term}</ol>
      <figcaption class="term-foot">{e(c["term_foot"])}</figcaption>
    </figure>
  </div>
</section>

<section class="sec value dark" id="why">
  <div class="wrap value-grid">
    <div class="rv">
      <p class="eyebrow">{e(c["value_eyebrow"])}</p>
      <h2>{e(c["value_h2"])}</h2>
      <p class="lead">{e(c["value_lead"])}</p>
    </div>
    <ol class="rv">{value}</ol>
  </div>
</section>

<section class="sec" id="services">
  <div class="wrap">
    <div class="rv">
      <p class="eyebrow">{e(c["svc_eyebrow"])}</p>
      <h2>{e(c["svc_h2"])}</h2>
    </div>
    <ul class="svc-list rv">{svc}</ul>
  </div>
</section>

<section class="sec alt" id="how">
  <div class="wrap split">
    <div class="rv">
      <span class="tag">{e(c["a_tag"])}</span>
      <h2>{e(c["a_h2"])}</h2>
      <div class="prose">{"".join(f"<p>{e(p)}</p>" for p in c["a_p"])}</div>
      <p class="sub-h">{e(c["a_signs_h"])}</p>
      {checks(c["a_signs"], "one")}
      <p class="sub-h">{e(c["a_ex_h"])}</p>
      {checks(c["a_ex"])}
    </div>
    <div class="rv">
      <div class="flow">
        <p class="flow-t">{e(c["flow_t"])}</p>
        <ol>{flow}</ol>
      </div>
      <p class="note">{e(c["a_benefit"])}</p>
      <p style="margin-top:1.5rem"><a class="btn btn-primary" href="#contact">{e(c["k_cta"])}</a></p>
    </div>
  </div>
</section>

<section class="sec" id="flows">
  <div class="wrap">
    <div class="rv">
      <span class="tag">{e(c["b_tag"])}</span>
      <h2>{e(c["b_h2"])}</h2>
      <p class="lead">{e(c["b_lead"])}</p>
    </div>
    <ul class="ai-list rv">{ai}</ul>
    <p class="note rv">{e(c["b_note"])}</p>
  </div>
</section>

<section class="sec dark" id="scope">
  <div class="wrap">
    <div class="rv">
      <span class="tag">{e(c["c_tag"])}</span>
      <h2>{e(c["c_h2"])}</h2>
      <p class="lead">{e(c["c_lead"])}</p>
    </div>
    <div class="infra rv" role="img" aria-label="{e(c["infra_env"])}: {e(c["infra_in"][0])} → {e(c["infra_core"][0])} → {e(c["infra_out"][0])}. {e(c["infra_ext_b"])}: {e(c["infra_ext_t"])}.">
      <div class="env" aria-hidden="true">
        <span class="env-l">{e(c["infra_env"])}</span>
        <div class="row">
          <div class="n">{e(c["infra_in"][0])}<small>{e(c["infra_in"][1])}</small></div><span class="ar">→</span>
          <div class="n core">{e(c["infra_core"][0])}<small>{e(c["infra_core"][1])}</small></div><span class="ar">→</span>
          <div class="n">{e(c["infra_out"][0])}<small>{e(c["infra_out"][1])}</small></div>
        </div>
      </div>
      <div class="out" aria-hidden="true"><small>{e(c["infra_ext_s"])}</small><b>{e(c["infra_ext_b"])}</b><span>{e(c["infra_ext_t"])}</span></div>
    </div>
    <div class="split rv">
      <div>
        <p class="sub-h" style="margin-top:0">{e(c["c_adv_h"])}</p>
        {checks(c["c_adv"], "one")}
        <p class="sub-h">{e(c["c_srv_h"])}</p>
        {checks(c["c_srv"], "one")}
      </div>
      <div>
        <table class="cmp">
          <caption>{e(c["cmp_cap"])}</caption>
          <thead><tr><th scope="col"><span class="vh">{e(c["cmp_cap"])}</span></th><th scope="col">{e(ch[1])}</th><th scope="col">{e(ch[2])}</th></tr></thead>
          <tbody>{cmp_rows}</tbody>
        </table>
        <p class="note">{e(c["c_note"])}</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="pricing">
  <div class="wrap">
    <div class="rv">
      <span class="tag">{e(c["d_tag"])}</span>
      <h2>{e(c["d_h2"])}</h2>
      <p class="lead">{e(c["d_lead"])}</p>
    </div>
    <div class="cols2 rv">
      <div><h3>{e(d1h)}</h3>{checks(d1)}</div>
      <div><h3>{e(d2h)}</h3>{checks(d2)}</div>
    </div>
  </div>
</section>

<section class="sec alt" id="process">
  <div class="wrap">
    <div class="rv">
      <p class="eyebrow">{e(c["p_eyebrow"])}</p>
      <h2>{e(c["p_h2"])}</h2>
    </div>
    <ol class="steps rv">{steps}</ol>
  </div>
</section>

<section class="sec" id="use-cases">
  <div class="wrap">
    <div class="rv">
      <p class="eyebrow">{e(c["u_eyebrow"])}</p>
      <h2>{e(c["u_h2"])}</h2>
      <p class="lead">{e(c["u_lead"])}</p>
    </div>
    <ul class="uc rv">{uc}</ul>
  </div>
</section>

<section class="sec alt" id="calculator">
  <div class="wrap">
    <div class="rv">
      <p class="eyebrow">{e(c["k_eyebrow"])}</p>
      <h2>{e(c["k_h2"])}</h2>
      <p class="lead">{e(c["k_lead"])}</p>
    </div>
    <div class="calc rv" id="calc">
      <form onsubmit="return false" aria-label="{e(c["k_h2"])}">
        <div class="field"><label for="c-n">{e(c["k_n"])}</label><input id="c-n" type="number" inputmode="numeric" min="0" max="10000" value="20"></div>
        <div class="field"><label for="c-m">{e(c["k_m"])}</label><input id="c-m" type="number" inputmode="numeric" min="0" max="1440" value="10"></div>
        <div class="field"><label for="c-r">{e(c["k_r"])}</label><input id="c-r" type="number" inputmode="numeric" min="0" max="10000" value="500"></div>
        <div class="field"><label for="c-p">{e(c["k_p"])} <output id="c-p-out" for="c-p">60 %</output></label><input id="c-p" type="range" min="10" max="90" step="5" value="60"></div>
      </form>
      <div class="result" aria-live="polite">
        <div>
          <p class="rl">{e(c["k_rl1"])}</p>
          <p class="big"><span id="r-h">0</span><small>{e(c["k_h"])}</small></p>
        </div>
        <div>
          <p class="rl">{e(c["k_rl2"])}</p>
          <p class="big"><span id="r-m">0</span><small>{e(c["k_k"])}</small></p>
        </div>
        <p class="fine">{e(c["k_fine"])}</p>
        <a class="btn btn-signal" id="calc-cta" href="#contact">{e(c["k_cta"])}</a>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="faq">
  <div class="wrap">
    <div class="rv">
      <p class="eyebrow">{e(c["f_eyebrow"])}</p>
      <h2>{e(c["f_h2"])}</h2>
    </div>
    <div class="faq rv">{faq}</div>
  </div>
</section>

<section class="sec contact" id="contact">
  <div class="wrap contact-grid">
    <div class="rv">
      <p class="eyebrow">{e(c["t_eyebrow"])}</p>
      <h2>{e(c["t_h2"])}</h2>
      <p class="lead">{e(c["t_lead"])}</p>
      <p style="margin-top:1.75rem" class="muted">{e(c["t_cta_mail"])}</p>
      <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    <form class="cform rv" id="contact-form" data-endpoint="{FORM_ENDPOINT}" novalidate>
      <div class="two">
        <div><label for="f-name">{e(f["name"])}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
        <div><label for="f-email">{e(f["email"])}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div><label for="f-company">{e(f["company"])} <span class="opt">({e(f["optional"])})</span></label><input id="f-company" name="company" type="text" autocomplete="organization"></div>
      <div><label for="f-topic">{e(f["topic"])}</label><select id="f-topic" name="topic">{topics}</select></div>
      <div><label for="f-msg">{e(f["msg"])}</label><textarea id="f-msg" name="message" placeholder="{e(f["msg_ph"])}" required></textarea></div>
      <div class="hp" aria-hidden="true"><label>Leave empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
      <label class="consent"><input type="checkbox" name="consent" required><span>{e(f["consent"])} <a href="#privacy">{e(f["consent_link"])}</a>.</span></label>
      <button class="btn btn-primary" type="submit">{e(f["send"])}</button>
      <p class="status" id="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <img src="/logo.png" width="160" height="30" alt="Arnell Company" loading="lazy">
        <p class="muted">{e(c["foot_tag"])}</p>
      </div>
      <nav aria-label="{e(c["foot_nav"])}">
        <p class="fh">{e(c["foot_nav"])}</p>
        <ul>{foot_links}</ul>
      </nav>
      <div>
        <p class="fh">{e(c["foot_contact"])}</p>
        <ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
        <p class="fh" style="margin-top:1.5rem">{e(c["foot_lang"])}</p>
        <span class="lang" role="group" aria-label="{e(c["lang_label"])}">{sw}</span>
      </div>
    </div>
    <div id="privacy"><p class="fh">{e(c["priv_h"])}</p><p>{e(c["priv_p"])}</p></div>
    <div class="legal"><span>© {YEAR} Arnell Company. {e(c["rights"])}</span><a href="#top">{e(c["to_top"])} ↑</a></div>
  </div>
</footer>

<script>window.I18N={json.dumps(i18n, ensure_ascii=False)};</script>
<script>
{js}
</script>
</body>
</html>
'''
    return page

if __name__ == "__main__":
    out = ROOT / "dist"
    (out / "en").mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(render("sv"), encoding="utf-8")
    (out / "en" / "index.html").write_text(render("en"), encoding="utf-8")
    print("built", out / "index.html", out / "en/index.html")
