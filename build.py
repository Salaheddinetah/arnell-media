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
    title="Arnell Company – Automatisering, AI & lokal AI för företag",
    desc="Automatisering, AI-agenter och lokal AI för företag. Vi bygger även webbplatser och systemintegrationer. Boka en kostnadsfri konsultation.",
    og_title="Arnell Company – Automatisering, AI & lokal AI för företag",
    skip="Hoppa till innehållet",
    nav=[("services","Tjänster"),("local-ai","Lokal AI"),("process","Process"),("faq","Vanliga frågor")],
    nav_cta="Kontakta oss", menu="Meny", lang_label="Språk",
    hero_eyebrow="Automation · AI · Lokal AI · Webb",
    hero_h1="Automatisering och AI som tar bort det <em>repetitiva arbetet.</em>",
    hero_lead="Vi hjälper små och medelstora företag att automatisera administration, koppla ihop sina system och införa AI som fungerar i vardagen – även lokalt och privat. Vi bygger också webbplatser och egen mjukvara.",
    hero_cta1="Boka en kostnadsfri konsultation", hero_cta2="Utforska våra tjänster",
    hero_notes=["Svar inom en arbetsdag","Fast omfattning – inga överraskande fakturor"],
    term_title="Exempel på arbetsflöde", term_status="körs",
    term_lines=[("09:02","Ny förfrågan kommer in via e-post"),("09:02","AI läser och sammanfattar innehållet"),("09:02","Kontakten skapas i CRM"),("09:03","Förslag på svar väntar på granskning"),("09:03","Tid bokas i kalendern")],
    term_foot="Illustration. Varje arbetsflöde utformas efter ert företag.",
    value_eyebrow="Varför Arnell Company",
    value_h2="Ett litet team som bygger det ni faktiskt behöver.",
    value_lead="Ni arbetar direkt med dem som gör jobbet – inga mellanled och ingen underleverantör. Vi utgår från ert problem, inte från tekniken, och föreslår den enklaste lösning som räcker.",
    value_items=[
        ("Tydlig kommunikation","Ni vet vad som händer, och varför, från första samtalet till leverans."),
        ("Fast omfattning","Projekt med tydlig omfattning och pris i förväg – inga överraskande fakturor."),
        ("Baserade i Sverige","Vi finns i er tidszon och talar både svenska och engelska."),
        ("Snabb leverans, god kvalitet","Vi arbetar effektivt utan att kapa hörn. Lösningar som går att underhålla och bygga vidare på."),
    ],
    svc_eyebrow="Det här gör vi",
    svc_h2="Fem sätt att få företaget att arbeta smartare.",
    svc_more="Läs mer",
    svc=[
        ("automation","Affärsautomation","Slipp manuell administration. Vi automatiserar e-post, leads, bokningar, rapporter och dataflöden mellan era system, bland annat med n8n."),
        ("ai","AI-automation & AI-agenter","Praktiska AI-assistenter som hanterar mejl, dokument och kundfrågor, med en människa som granskar där det behövs."),
        ("local-ai","Lokal & privat AI","Kör AI-modeller i er egen miljö för större kontroll över data och infrastruktur."),
        ("web","Webb & egen mjukvara","Webbplatser, webbapplikationer, interna portaler och API:er som byggs från grunden efter era mål."),
        ("web","IT-konsulting & integrationer","Vi analyserar era processer och kopplar ihop systemen så att information flödar utan manuellt arbete."),
    ],
    a_tag="01 · Affärsautomation",
    a_h2="Automatisering handlar om att ge tiden tillbaka.",
    a_p=["Affärsautomation innebär att system utför återkommande uppgifter åt er: flyttar data mellan program, skickar bekräftelser, tar fram underlag och påminner. Det frigör tid, minskar manuella fel och gör att inget faller mellan stolarna.",
         "n8n är ett verktyg för arbetsflöden där en händelse – ett nytt mejl, en bokning, en betalning – startar en kedja av steg mellan era system. Det kan drivas i er egen miljö (self-hosted) eller som molntjänst, och passar bra när färdiga integrationer inte räcker."],
    a_signs_h="Tecken på att det är dags att automatisera",
    a_signs=["Ni för över samma uppgifter mellan system för hand.","Förfrågningar och mejl blir liggande för att ingen hinner.","Rapporter och fakturaunderlag tar timmar att sammanställa varje månad.","Kunddata finns på flera ställen och stämmer inte överens."],
    a_ex_h="Det här kan vi automatisera",
    a_ex=["Arbetsflöden i n8n","Hantering av inkommande e-post","Insamling och kvalificering av leads","CRM-automation","Onboarding av nya kunder","Bokningar och påminnelser","Datasynkronisering mellan plattformar","Automatiska rapporter","Fakturor och dokument","API-integrationer","Interna arbetsflöden"],
    flow_t="Exempel: från förfrågan till bokad tid",
    flow=[("IN","Förfrågan kommer in","Via formulär, e-post eller bokningssystem"),("n8n","Arbetsflödet startar","Uppgifterna kontrolleras och struktureras"),("CRM","Kunden registreras","Utan manuell inmatning"),("CAL","Tid bokas","Kalendern uppdateras automatiskt"),("OUT","Bekräftelse skickas","Kunden får svar direkt, ni får en notis")],
    a_benefit="Resultatet: mindre manuellt arbete, färre fel och snabbare svar till era kunder.",
    b_tag="02 · AI-automation & AI-agenter",
    b_h2="AI som gör nytta i vardagen, inte bara i demos.",
    b_lead="En AI-agent är mjukvara som utifrån ett mål kan läsa information, ta enklare beslut och utföra steg i era system. Vi bygger agenter för avgränsade uppgifter där nyttan är tydlig och där en människa fortfarande har sista ordet.",
    b_items=[
        ("AI-assistent för kundsupport","Svarar på vanliga frågor utifrån er egen information och lämnar över till en människa när det behövs."),
        ("E-post och meddelanden","Sorterar, sammanfattar och förbereder svarsutkast som ni granskar innan de skickas."),
        ("Dokumenthantering","Läser av fakturor, avtal och formulär och för över uppgifterna till rätt system."),
        ("Kunskapsassistent","Gör era manualer, rutiner och policyer sökbara med vanliga frågor och svar."),
        ("Kvalificering av leads","Bedömer inkommande förfrågningar så att ni hör av er till rätt personer först."),
        ("Administrativt stöd","Sammanställer underlag, mötesanteckningar och rapporter."),
        ("Egna AI-agenter","Skräddarsydda för en specifik uppgift i just er verksamhet."),
        ("Koppling till befintliga system","AI som arbetar i de verktyg ni redan använder, utan att ni behöver byta."),
    ],
    b_note="AI gör ibland fel. Därför bygger vi in granskning, loggning och tydliga gränser för vad en agent får göra, och vi börjar smått där risken är låg.",
    c_tag="03 · Lokal & privat AI",
    c_h2="AI som körs i er egen miljö.",
    c_lead="Många AI-tjänster skickar er data till en extern leverantör. Med lokal eller privat AI körs modellen på er egen server, i en kontrollerad miljö eller på hårdvara ni äger. Då avgör ni själva var informationen hamnar.",
    infra_env="Er miljö", infra_in=("Dokument & data","era filer, e-post, ärenden"), infra_core=("Lokal AI-modell","t.ex. via Ollama"), infra_out=("Era verktyg","CRM, e-post, system"),
    infra_ext_s="Valfritt", infra_ext_b="Extern AI-molntjänst", infra_ext_t="Används bara om ni väljer det",
    c_adv_h="Fördelar med lokal AI",
    c_adv=["Större kontroll över data","Mer integritetsmedvetna arbetssätt","Mindre beroende av externa leverantörer","Kontroll över infrastrukturen","Kan drivas inom er befintliga IT-miljö"],
    c_srv_h="Det här kan vi hjälpa till med",
    c_srv=["Installation av lokala språkmodeller (LLM)","Privata AI-miljöer","Självhostade AI-lösningar","Lokala AI-assistenter","Privat dokumentanalys","Interna kunskapsassistenter","Uppsättning av AI-infrastruktur","Koppling av modeller till affärsverktyg","Ollama och andra lokala AI-tekniker"],
    cmp_cap="Molnbaserad AI jämfört med lokal AI", cmp_head=("","Molnbaserad AI","Lokal AI"),
    cmp_rows=[("Var körs modellen?","Hos leverantören","På er server eller i er miljö"),
              ("Datakontroll","Styrs av leverantörens villkor","Ni bestämmer själva"),
              ("Kapacitet","Ofta de mest avancerade modellerna","Öppna modeller, kan vara mindre kapabla beroende på hårdvara"),
              ("Kostnad","Löpande användningsavgifter","Investering i hårdvara och drift"),
              ("Underhåll","Sköts av leverantören","Sköts av er eller av oss")],
    c_note="Lokal AI är inte automatiskt säker eller i linje med GDPR. Vad som gäller för er kräver en teknisk och juridisk bedömning av just er situation.",
    d_tag="04 · Webb, integrationer & IT-konsulting",
    d_h2="Webbplatser och system som hänger ihop.",
    d_lead="Vi bygger webbplatser och egen mjukvara, och vi kopplar ihop de system ni redan har. När bokning, kundregister, fakturering och e-post pratar med varandra försvinner dubbelarbetet, eftersom information bara behöver registreras en gång.",
    d_col1=("Webb & utveckling",["Moderna företagswebbplatser","Anpassade webbapplikationer","Interna portaler","API-utveckling och integrationer","Optimering och prestanda","Responsiv UI/UX-utveckling","Egna affärsverktyg","Support och underhåll"]),
    d_col2=("IT-konsulting",["Teknisk rådgivning","Analys av affärsprocesser","Systemintegration","Systemarkitektur","Digitalisering","Optimering av arbetsflöden","Teknisk problemlösning"]),
    p_eyebrow="Så arbetar vi", p_h2="Från första samtal till fungerande lösning.",
    p_steps=[("Kartläggning","Vi lyssnar och förstår ert företag, era mål och vad som tar tid idag."),("Analys","Vi går igenom processerna och bedömer vad som faktiskt är värt att automatisera."),("Lösningsdesign","Vi föreslår en tydlig lösning med omfattning, tidsplan och pris."),("Genomförande","Vi bygger lösningen och kopplar ihop era system."),("Test","Vi testar med verkliga scenarier innan något tas i bruk."),("Fortlöpande förbättring","Vi följer upp, justerar och utvecklar vidare när behoven förändras.")],
    u_eyebrow="Branscher & användningsområden", u_h2="Vilka företag hjälper vi?",
    u_lead="Vi är inte begränsade till en bransch. Här är några exempel på hur olika verksamheter kan använda automation och AI.",
    u_items=[("Skönhet & hälsa","Bokningsbekräftelser, påminnelser, uppföljning och förfrågningar som hanteras utan manuellt arbete."),("Handel & e-handel","Order, kundmejl och fakturaunderlag som flyttas mellan system automatiskt."),("Professionella tjänster","Offerter, dokumenthantering, tidrapportering och kunduppföljning."),("Lokala företag","En webbplats som tar emot förfrågningar och rutiner som svarar på vanliga frågor."),("Övriga små och medelstora företag","Rapporter, dataflöden och interna arbetsflöden anpassade efter er verksamhet.")],
    k_eyebrow="Räkna på det", k_h2="Hur mycket tid går åt till återkommande uppgifter?",
    k_lead="Fyll i en uppgift som ni gör om och om igen. Resultatet är en enkel uppskattning baserad på era egna siffror.",
    k_n="Antal gånger per vecka", k_m="Minuter per gång", k_r="Timkostnad (kr)", k_p="Andel som går att automatisera",
    k_rl1="Möjlig tid att frigöra", k_rl2="Motsvarande kostnad", k_h="timmar / månad", k_k="kr / månad",
    k_fine="Förenklad uppskattning (4,33 veckor per månad). Verklig besparing varierar och bedöms i ett första samtal. Det är inget löfte.",
    k_cta="Diskutera ett automationsprojekt",
    k_msg="Hej! Jag vill diskutera att automatisera en återkommande uppgift. Den utförs ca {n} gånger i veckan och tar ca {min} minuter varje gång. Enligt kalkylatorn motsvarar det ca {h} timmar i månaden som kan frigöras.",
    f_eyebrow="Vanliga frågor", f_h2="Svar på det de flesta undrar över.",
    faq=[
        ("Vad är affärsautomation?","Affärsautomation betyder att återkommande arbetsmoment utförs av system i stället för för hand, till exempel att flytta data mellan program, skicka bekräftelser, skapa rapporter eller sortera inkommande mejl. Målet är att spara tid, minska fel och låta personalen fokusera på arbete som kräver människor."),
        ("När bör ett företag automatisera?","När samma uppgift görs ofta, följer samma regler och tar märkbar tid, eller när information måste skrivas in på flera ställen. Uppgifter som sällan utförs eller kräver mycket omdöme är oftast inte värda att automatisera först."),
        ("Vad är en AI-agent och vad kan den göra?","En AI-agent är mjukvara som utifrån ett mål kan läsa information, ta enklare beslut och utföra steg i era system, till exempel sortera inkommande mejl, sammanfatta dokument eller besvara vanliga kundfrågor. Vi bygger in granskning och gränser så att en människa har sista ordet där det behövs."),
        ("Vad är lokal AI och hur skiljer den sig från molnbaserad AI?","Lokal AI innebär att AI-modellen körs på en server ni kontrollerar, i stället för hos en extern leverantör. Det ger större kontroll över var data hanteras. Avvägningen är att lokala modeller kan vara mindre kapabla än de största molnmodellerna och att hårdvara och drift behöver tas med i beräkningen."),
        ("Är lokal AI säker och GDPR-anpassad?","Lokal AI kan ge bättre kontroll över data, men det är inte automatiskt säkert eller GDPR-anpassat. Det beror på hur lösningen sätts upp, vilken data som hanteras och hur den drivs. Vi lovar därför inga absoluta garantier. Det behöver bedömas tekniskt och juridiskt för er situation."),
        ("Hur fungerar n8n?","n8n är ett verktyg för arbetsflöden. En händelse, som ett nytt mejl eller en bokning, startar en kedja av steg som kopplar ihop era system. n8n har många färdiga integrationer och kan även kopplas mot egna API:er. Det kan drivas i er egen miljö eller som molntjänst."),
        ("Behöver vi byta system för att automatisera?","Oftast inte. Vi kopplar ihop de verktyg ni redan använder, via deras integrationer eller API:er. Om ett system saknar möjlighet att kopplas ihop säger vi det och föreslår alternativ."),
        ("Vad kostar det?","Det beror på omfattningen. Vi arbetar med fast omfattning och lämnar ett tydligt förslag med pris efter ett första samtal, så att ni vet vad som ingår innan vi börjar. Första samtalet är kostnadsfritt."),
        ("Hur lång tid tar ett projekt?","Det beror på hur många system och steg som ingår. Ett avgränsat arbetsflöde går snabbare än en större integration eller en egen applikation. Vi ger en tidsplan efter den första analysen."),
        ("Kan ni bygga och underhålla vår webbplats?","Ja. Vi designar och utvecklar webbplatser från grunden och erbjuder fortlöpande support och underhåll så att sajten fungerar, är säker och uppdaterad."),
    ],
    t_eyebrow="Kontakt", t_h2="Berätta vad ni vill uppnå.",
    t_lead="Beskriv kort er situation så återkommer vi inom en arbetsdag. Första samtalet är kostnadsfritt och förpliktar till ingenting.",
    t_cta_mail="Eller mejla oss direkt:",
    form=dict(name="Namn",email="E-post",company="Företag",optional="valfritt",topic="Vad gäller det?",msg="Meddelande",msg_ph="Vad vill ni uppnå eller förbättra?",
              topics=[("automation","Affärsautomation"),("ai","AI-automation / AI-agenter"),("local-ai","Lokal eller privat AI"),("web","Webbplats eller webbapplikation"),("integration","Integration / IT-konsulting"),("other","Något annat / vet inte än")],
              consent="Jag godkänner att Arnell Company behandlar mina uppgifter för att besvara min förfrågan. Läs mer under",consent_link="Integritet",send="Skicka förfrågan",sending="Skickar …",
              ok="Tack! Vi har tagit emot din förfrågan och återkommer inom en arbetsdag.",err="Något gick fel. Skriv gärna direkt till"),
    foot_tag="Automatisering, AI och webb för företag.", foot_nav="Navigering", foot_contact="Kontakt", foot_lang="Språk",
    foot_links=[("services","Tjänster"),("automation","Affärsautomation"),("ai","AI-agenter"),("local-ai","Lokal AI"),("web","Webb & integrationer"),("faq","Vanliga frågor")],
    priv_h="Integritet", priv_p="Uppgifterna du skickar via kontaktformuläret används bara för att besvara din förfrågan och för att kunna följa upp kontakten. Vi säljer inte uppgifterna och delar dem inte med tredje part för marknadsföring. Formuläret levereras till oss som e-post via tjänsten FormSubmit. Vill du att vi raderar dina uppgifter kan du mejla oss. Webbplatsen använder inga marknadsföringscookies.",
    rights="Alla rättigheter förbehållna.", to_top="Till toppen",
    subject="Ny förfrågan från arnellcompany.se (sv)",
    schema_desc="Arnell Company hjälper små och medelstora företag med affärsautomation, AI-agenter, lokal och privat AI, webbutveckling och systemintegrationer.",
),
"en": dict(
    lang="en", locale="en-GB", og_locale="en_GB", og_alt="sv_SE", path="/en/",
    title="Arnell Company – Business Automation, AI & Local AI",
    desc="Business automation, AI agents and local AI for companies. We also build websites and system integrations. Book a free consultation.",
    og_title="Arnell Company – Business Automation, AI & Local AI",
    skip="Skip to content",
    nav=[("services","Services"),("local-ai","Local AI"),("process","Process"),("faq","FAQ")],
    nav_cta="Get in touch", menu="Menu", lang_label="Language",
    hero_eyebrow="Automation · AI · Local AI · Web",
    hero_h1="Automation and AI that removes the <em>repetitive work.</em>",
    hero_lead="We help small and medium-sized businesses automate administration, connect their systems and put AI to work in everyday operations, including locally and privately. We also build websites and custom software.",
    hero_cta1="Book a free consultation", hero_cta2="Explore our services",
    hero_notes=["Reply within one business day","Fixed scope – no surprise invoices"],
    term_title="Example workflow", term_status="running",
    term_lines=[("09:02","New enquiry arrives by email"),("09:02","AI reads and summarises the message"),("09:02","Contact is created in the CRM"),("09:03","Draft reply waits for review"),("09:03","Meeting is booked in the calendar")],
    term_foot="Illustration. Every workflow is designed around your business.",
    value_eyebrow="Why Arnell Company",
    value_h2="A small team that builds what you actually need.",
    value_lead="You work directly with the people doing the work – no account managers, no outsourcing. We start from your problem, not from the technology, and propose the simplest solution that will do the job.",
    value_items=[
        ("Clear communication","You know what is happening, and why, from the first call to delivery."),
        ("Fixed scope","Projects with a clear scope and price up front – no surprise invoices."),
        ("Based in Sweden","We work in your time zone and speak both Swedish and English."),
        ("Fast delivery, solid quality","We work efficiently without cutting corners, and build things that can be maintained and extended."),
    ],
    svc_eyebrow="What we do",
    svc_h2="Five ways to help your business work smarter.",
    svc_more="Read more",
    svc=[
        ("automation","Business automation","Cut manual administration. We automate email, leads, bookings, reports and data flows between your systems, using tools such as n8n."),
        ("ai","AI automation & AI agents","Practical AI assistants that handle email, documents and customer questions, with a person reviewing where it matters."),
        ("local-ai","Local & private AI","Run AI models in your own environment for greater control over your data and infrastructure."),
        ("web","Web & custom software","Websites, web applications, internal portals and APIs built from scratch around your goals."),
        ("web","IT consulting & integrations","We analyse your processes and connect your systems so information flows without manual work."),
    ],
    a_tag="01 · Business automation",
    a_h2="Automation is about giving time back.",
    a_p=["Business automation means systems carry out recurring tasks for you: moving data between programs, sending confirmations, preparing documents and sending reminders. It frees up time, reduces manual errors and stops things falling through the cracks.",
         "n8n is a workflow tool where an event – a new email, a booking, a payment – triggers a chain of steps across your systems. It can be self-hosted in your own environment or used as a cloud service, and works well when ready-made integrations are not enough."],
    a_signs_h="Signs it is time to automate",
    a_signs=["You copy the same information between systems by hand.","Enquiries and emails sit unanswered because nobody has time.","Reports and invoice data take hours to compile each month.","Customer data lives in several places and does not match."],
    a_ex_h="What we can automate",
    a_ex=["n8n workflows","Incoming email handling","Lead capture and qualification","CRM automation","Customer onboarding","Bookings and reminders","Data synchronisation between platforms","Automated reporting","Invoice and document processing","API integrations","Internal business workflows"],
    flow_t="Example: from enquiry to booked meeting",
    flow=[("IN","Enquiry arrives","Via form, email or booking system"),("n8n","Workflow starts","Details are checked and structured"),("CRM","Customer is registered","No manual data entry"),("CAL","Meeting is booked","The calendar updates automatically"),("OUT","Confirmation is sent","The customer gets a reply, you get a notification")],
    a_benefit="The result: less manual work, fewer mistakes and faster replies to your customers.",
    b_tag="02 · AI automation & AI agents",
    b_h2="AI that is useful day to day, not just in demos.",
    b_lead="An AI agent is software that can read information, make simple decisions and carry out steps in your systems to reach a goal. We build agents for well-defined tasks where the benefit is clear and a person still has the final say.",
    b_items=[
        ("AI customer support assistant","Answers common questions from your own information and hands over to a person when needed."),
        ("Email and message handling","Sorts, summarises and prepares draft replies that you review before they are sent."),
        ("Document processing","Reads invoices, contracts and forms and passes the data to the right system."),
        ("Knowledge assistant","Makes your manuals, procedures and policies searchable through plain questions and answers."),
        ("Lead qualification","Assesses incoming enquiries so you contact the right people first."),
        ("Administrative support","Compiles documents, meeting notes and reports."),
        ("Custom AI agents","Tailored to one specific task in your business."),
        ("Connected to existing systems","AI that works inside the tools you already use, without switching."),
    ],
    b_note="AI sometimes gets things wrong. That is why we build in review, logging and clear limits on what an agent may do, and we start small where the risk is low.",
    c_tag="03 · Local & private AI",
    c_h2="AI that runs in your own environment.",
    c_lead="Many AI services send your data to an external provider. With local or private AI, the model runs on your own server, in a controlled environment or on hardware you own, so you decide where the information goes.",
    infra_env="Your environment", infra_in=("Documents & data","your files, email, cases"), infra_core=("Local AI model","e.g. via Ollama"), infra_out=("Your tools","CRM, email, systems"),
    infra_ext_s="Optional", infra_ext_b="External cloud AI", infra_ext_t="Only used if you choose to",
    c_adv_h="Advantages of local AI",
    c_adv=["Greater control over your data","More privacy-conscious ways of working","Less dependence on external providers","Control over the infrastructure","Can run inside your existing IT environment"],
    c_srv_h="How we can help",
    c_srv=["Local large language model (LLM) deployment","Private AI environments","Self-hosted AI solutions","Local AI assistants","Private document analysis","Internal knowledge assistants","AI infrastructure setup","Connecting models to business tools","Ollama and other local AI technologies"],
    cmp_cap="Cloud AI compared with local AI", cmp_head=("","Cloud AI","Local AI"),
    cmp_rows=[("Where does the model run?","With the provider","On your server or in your environment"),
              ("Data control","Governed by the provider's terms","You decide"),
              ("Capability","Often the most advanced models","Open models, which can be less capable depending on hardware"),
              ("Cost","Ongoing usage fees","Investment in hardware and operations"),
              ("Maintenance","Handled by the provider","Handled by you or by us")],
    c_note="Local AI is not automatically secure or GDPR-compliant. What applies to you needs a technical and legal assessment of your specific situation.",
    d_tag="04 · Web, integrations & IT consulting",
    d_h2="Websites and systems that work together.",
    d_lead="We build websites and custom software, and we connect the systems you already have. When bookings, customer records, invoicing and email talk to each other, double entry disappears because information only has to be registered once.",
    d_col1=("Web & development",["Modern business websites","Custom web applications","Internal portals","API development and integrations","Optimisation and performance","Responsive UI/UX development","Custom business tools","Support and maintenance"]),
    d_col2=("IT consulting",["Technical consulting","Business process analysis","Software integration","System architecture","Digital transformation","Workflow optimisation","Technical problem-solving"]),
    p_eyebrow="How we work", p_h2="From first conversation to working solution.",
    p_steps=[("Discovery","We listen and learn about your business, your goals and what takes time today."),("Analysis","We review your processes and assess what is actually worth automating."),("Solution design","We propose a clear solution with scope, timeline and price."),("Implementation","We build the solution and connect your systems."),("Testing","We test with real scenarios before anything goes live."),("Ongoing improvement","We follow up, adjust and develop further as your needs change.")],
    u_eyebrow="Industries & use cases", u_h2="Which businesses do we help?",
    u_lead="We are not limited to one industry. Here are a few examples of how different businesses can use automation and AI.",
    u_items=[("Beauty & wellness","Booking confirmations, reminders, follow-ups and enquiries handled without manual work."),("Retail & e-commerce","Orders, customer emails and invoice data moved between systems automatically."),("Professional services","Quotes, document handling, time reporting and client follow-up."),("Local businesses","A website that captures enquiries, and routines that answer common questions."),("Other small and medium-sized businesses","Reports, data flows and internal workflows tailored to your operations.")],
    k_eyebrow="Do the maths", k_h2="How much time goes into recurring tasks?",
    k_lead="Enter one task you do over and over. The result is a simple estimate based on your own numbers.",
    k_n="Times per week", k_m="Minutes each time", k_r="Hourly cost (SEK)", k_p="Share that can be automated",
    k_rl1="Time that could be freed up", k_rl2="Equivalent cost", k_h="hours / month", k_k="SEK / month",
    k_fine="Simplified estimate (4.33 weeks per month). Actual savings vary and are assessed in a first conversation. It is not a promise.",
    k_cta="Discuss an automation project",
    k_msg="Hi! I would like to discuss automating a recurring task. It is done about {n} times a week and takes about {min} minutes each time. According to the calculator, that is roughly {h} hours a month that could be freed up.",
    f_eyebrow="FAQ", f_h2="Answers to what most people ask.",
    faq=[
        ("What is business automation?","Business automation means recurring tasks are carried out by systems instead of by hand, for example moving data between programs, sending confirmations, producing reports or sorting incoming email. The aim is to save time, reduce errors and let staff focus on work that needs people."),
        ("When should a company automate?","When the same task is done often, follows the same rules and takes noticeable time, or when information has to be entered in several places. Tasks that are rare or need a lot of judgement are usually not worth automating first."),
        ("What is an AI agent and what can it do?","An AI agent is software that can read information, make simple decisions and carry out steps in your systems to reach a goal, for example sorting incoming email, summarising documents or answering common customer questions. We build in review and limits so a person has the final say where it matters."),
        ("What is local AI and how does it differ from cloud AI?","Local AI means the AI model runs on a server you control instead of with an external provider. That gives you more control over where data is processed. The trade-off is that local models can be less capable than the largest cloud models, and hardware and operations need to be factored in."),
        ("Is local AI secure and GDPR-compliant?","Local AI can give you better control over data, but it is not automatically secure or GDPR-compliant. That depends on how the solution is set up, what data is handled and how it is operated. We therefore make no absolute guarantees. It needs a technical and legal assessment for your situation."),
        ("How does n8n work?","n8n is a workflow tool. An event, such as a new email or booking, starts a chain of steps that connect your systems. n8n has many ready-made integrations and can also connect to custom APIs. It can run in your own environment or as a cloud service."),
        ("Do we need to replace our systems to automate?","Usually not. We connect the tools you already use through their integrations or APIs. If a system cannot be connected, we will tell you and suggest alternatives."),
        ("What does it cost?","It depends on the scope. We work with a fixed scope and give you a clear proposal with a price after a first conversation, so you know what is included before we start. The first conversation is free."),
        ("How long does a project take?","It depends on how many systems and steps are involved. A well-defined workflow is quicker than a larger integration or a custom application. We provide a timeline after the initial analysis."),
        ("Can you build and maintain our website?","Yes. We design and develop websites from scratch and offer ongoing support and maintenance so the site stays working, secure and up to date."),
    ],
    t_eyebrow="Contact", t_h2="Tell us what you want to achieve.",
    t_lead="Describe your situation briefly and we will get back to you within one business day. The first conversation is free and carries no obligation.",
    t_cta_mail="Or email us directly:",
    form=dict(name="Name",email="Email",company="Company",optional="optional",topic="What is it about?",msg="Message",msg_ph="What would you like to achieve or improve?",
              topics=[("automation","Business automation"),("ai","AI automation / AI agents"),("local-ai","Local or private AI"),("web","Website or web application"),("integration","Integration / IT consulting"),("other","Something else / not sure yet")],
              consent="I agree that Arnell Company processes my details to respond to my enquiry. Read more under",consent_link="Privacy",send="Send enquiry",sending="Sending …",
              ok="Thank you! We have received your enquiry and will reply within one business day.",err="Something went wrong. Please write directly to"),
    foot_tag="Automation, AI and web for businesses.", foot_nav="Navigation", foot_contact="Contact", foot_lang="Language",
    foot_links=[("services","Services"),("automation","Business automation"),("ai","AI agents"),("local-ai","Local AI"),("web","Web & integrations"),("faq","FAQ")],
    priv_h="Privacy", priv_p="The details you send through the contact form are used only to respond to your enquiry and to follow up on the contact. We do not sell them or share them with third parties for marketing. The form is delivered to us as an email via the FormSubmit service. If you would like your details deleted, email us. This website does not use marketing cookies.",
    rights="All rights reserved.", to_top="Back to top",
    subject="New enquiry from arnellcompany.se (en)",
    schema_desc="Arnell Company helps small and medium-sized businesses with business automation, AI agents, local and private AI, web development and system integrations.",
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

<section class="sec alt" id="automation">
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

<section class="sec" id="ai">
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

<section class="sec dark" id="local-ai">
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

<section class="sec" id="web">
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
