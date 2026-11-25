# EduWISP

**Open-source platform for managing school-owned Android devices**

EduWISP è un progetto open source che nasce con l'obiettivo di offrire alle scuole uno strumento completo, modulare e indipendente per la gestione dei tablet Android utilizzati nelle attività didattiche.

Ispirato alla filosofia di [OpenWISP](https://openwisp.org/), EduWISP intende portare nel mondo dell'istruzione un modello di gestione centralizzata, basato su componenti modulari, standard aperti, automazione e controllo dei dispositivi.

Il progetto prevede anche un sistema integrato di **Family Control**, pensato per consentire una collaborazione regolamentata tra istituto scolastico e famiglia nella gestione dell'utilizzo dei dispositivi.

> **Stato del progetto: fase di progettazione**
>
> In questa fase stiamo definendo visione, requisiti, architettura, funzionalità, sicurezza, privacy e modello di governance. Non è ancora iniziata la fase di sviluppo software.

---

## Indice

- [Visione](#visione)
- [Obiettivi](#obiettivi)
- [Caratteristiche principali](#caratteristiche-principali)
- [Gestione dei dispositivi Android](#gestione-dei-dispositivi-android)
- [Gestione scolastica](#gestione-scolastica)
- [Family Control](#family-control)
- [Motore delle policy](#motore-delle-policy)
- [Architettura concettuale](#architettura-concettuale)
- [Sicurezza e privacy](#sicurezza-e-privacy)
- [Modello di distribuzione](#modello-di-distribuzione)
- [Principi del progetto](#principi-del-progetto)
- [Roadmap progettuale](#roadmap-progettuale)
- [Documentazione](#documentazione)
- [Contributi](#contributi)
- [Licenza](#licenza)

## Visione

EduWISP vuole diventare una piattaforma aperta per la gestione dei dispositivi digitali scolastici.

L'obiettivo non è soltanto installare applicazioni o applicare restrizioni ai tablet, ma definire un sistema nel quale:

- La scuola possa gestire centralmente i dispositivi di sua proprietà.
- Docenti e personale autorizzato possano applicare configurazioni coerenti con le attività didattiche.
- Le famiglie possano partecipare alla gestione dell'utilizzo dei dispositivi, secondo responsabilità e permessi definiti.
- Le regole siano applicate in modo coerente, verificabile e trasparente.
- Gli istituti possano scegliere se utilizzare un'infrastruttura cloud oppure installare EduWISP sui propri server.

## Obiettivi

1. Centralizzare la gestione dei tablet Android scolastici.
2. Semplificare la distribuzione e l'aggiornamento delle applicazioni.
3. Definire profili e restrizioni in base a scuola, classe, studente e dispositivo.
4. Consentire modalità operative specifiche per lezioni, verifiche e attività didattiche.
5. Integrare un Family Control con ruoli e responsabilità distinti.
6. Proteggere i dati degli studenti e rispettare i principi di privacy by design.
7. Evitare la dipendenza obbligatoria da un unico fornitore cloud.
8. Favorire una comunità open source e lo sviluppo di moduli indipendenti.

## Caratteristiche principali

### Mobile Device Management (MDM)

- Registrazione e provisioning dei dispositivi.
- Associazione a istituto, plesso, classe e studente.
- Inventario centralizzato di hardware e software.
- Installazione e aggiornamento delle applicazioni.
- Catalogo di applicazioni obbligatorie e facoltative.
- Gestione di applicazioni consentite e bloccate.
- Configurazioni gestite delle applicazioni compatibili.
- Gestione delle reti Wi-Fi e dei certificati.
- Restrizioni sulle impostazioni Android.
- Modalità kiosk e dispositivi multi-app.
- Gestione degli aggiornamenti di sistema.
- Blocco e cancellazione remota, nei limiti supportati dalla piattaforma Android.

Le funzionalità effettivamente disponibili dipenderanno dalle API e dalle modalità di gestione Android supportate.

### Gestione scolastica

- Organizzazione multi-istituto.
- Gestione di plessi, classi, docenti e studenti.
- Associazione dei dispositivi agli utenti.
- Profili di configurazione per classe e gruppo.
- Regole specifiche per le attività didattiche.
- Modalità verifica con restrizioni temporanee.
- Distribuzione centralizzata delle applicazioni didattiche.
- Registro delle modifiche e delle operazioni amministrative.

### Family Control

Un modulo integrato per consentire alle famiglie di partecipare alla gestione dell'utilizzo dei dispositivi.

Funzionalità previste:

- Associazione verificata tra genitore, tutore e studente.
- Portale dedicato alle famiglie.
- Fasce orarie di utilizzo.
- Restrizioni aggiuntive durante il tempo extrascolastico.
- Regole sulle applicazioni utilizzabili.
- Profili di utilizzo e limiti configurabili, dove supportati.
- Consultazione delle regole attive sul dispositivo.
- Storico essenziale delle modifiche e delle autorizzazioni.

Il Family Control non sarà una copia di Google Family Link. Dovrà essere integrato nel modello di gestione scolastica, rispettando la titolarità del dispositivo e i diritti degli studenti.

### Policy Engine

Un motore centralizzato per definire, combinare e distribuire le regole.

Le policy potranno essere associate a:

- Intera organizzazione scolastica.
- Singolo istituto o plesso.
- Classe o gruppo.
- Singolo studente.
- Singolo dispositivo.
- Attività didattica o fascia oraria.
- Contesto scolastico o familiare.

La gerarchia e la risoluzione dei conflitti tra policy scolastiche, familiari e di sicurezza saranno definite durante la progettazione.

## Gestione dei dispositivi Android

Il target iniziale è costituito da tablet Android con Google Mobile Services (GMS), di proprietà degli istituti scolastici.

La modalità di gestione primaria da valutare è **Android Enterprise Fully Managed**, adatta ai dispositivi aziendali o scolastici gestiti integralmente dall'organizzazione.

L'integrazione con Android Enterprise e Android Management API dovrà essere verificata rispetto alle condizioni di accesso, ai requisiti Google e alle funzionalità effettivamente disponibili.

EduWISP dovrà mantenere il proprio modello di gestione indipendente dal provider MDM, così da evitare di legare l'intero progetto a una singola tecnologia.

## Gestione scolastica

La scuola rappresenta il soggetto responsabile della gestione istituzionale del dispositivo.

Il sistema dovrà consentire di distinguere i ruoli:

- Amministratore della piattaforma.
- Amministratore dell'istituto.
- Responsabile IT.
- Dirigente o personale autorizzato.
- Docente.
- Studente.
- Genitore o tutore.

Ogni ruolo dovrà disporre esclusivamente delle autorizzazioni necessarie alle proprie attività.

## Family Control

La relazione tra scuola e famiglia è uno degli elementi centrali del progetto.

Il modello di collaborazione e la ripartizione delle responsabilità dovranno essere definiti prima dello sviluppo. Una possibile soluzione prevede due ambiti di gestione coordinati:

- **Ambito scolastico:** gestione istituzionale, didattica e sicurezza del dispositivo.
- **Ambito familiare:** regole aggiuntive per l'utilizzo domestico e il tempo extrascolastico.

Le regole di sicurezza e le esigenze didattiche obbligatorie non dovranno essere aggirabili attraverso le impostazioni familiari.

## Motore delle policy

Il Policy Engine sarà un componente autonomo rispetto alla tecnologia MDM utilizzata.

Dovrà occuparsi di:

- Definizione delle regole.
- Associazione delle regole ai soggetti interessati.
- Priorità e ambiti di applicazione.
- Risoluzione dei conflitti.
- Pianificazione temporale.
- Generazione della configurazione effettiva.
- Tracciamento delle modifiche.
- Gestione dei dispositivi temporaneamente non connessi.

## Architettura concettuale

L'architettura dovrà essere modulare, con componenti logicamente separati e interfacce documentate.

I principali domini funzionali previsti sono:

| Modulo | Responsabilità |
|---|---|
| Core | Organizzazioni, utenti, ruoli e dispositivi |
| MDM | Gestione e configurazione dei dispositivi |
| Android Provider | Integrazione con le tecnologie Android |
| Application Management | Catalogo e distribuzione delle app |
| Policy Engine | Definizione e risoluzione delle regole |
| School Management | Istituti, plessi, classi e docenti |
| Family Control | Gestione delle regole familiari |
| Audit | Tracciamento delle operazioni |
| API | Integrazione con sistemi esterni |
| Web Interface | Interfacce per amministratori, docenti e famiglie |

Come ipotesi iniziale si valuterà un'architettura modulare, evitando di introdurre microservizi non necessari nella prima fase.

## Sicurezza e privacy

La protezione degli studenti e dei loro dati è un requisito fondamentale.

Principi previsti:

- Privacy by design e privacy by default.
- Separazione dei dati tra istituti.
- Controllo degli accessi basato sui ruoli.
- Autenticazione e autorizzazione robuste.
- Cifratura delle comunicazioni.
- Audit delle operazioni amministrative.
- Conservazione limitata dei dati.
- Trasparenza sulle informazioni raccolte.
- Valutazione degli obblighi GDPR e della normativa italiana.
- Valutazione dell'eventuale necessità di una DPIA.

EduWISP non nasce per sorvegliare gli studenti. Funzioni invasive come lettura dei messaggi, accesso a foto e contenuti personali o geolocalizzazione continua non rientrano negli obiettivi del progetto.

## Modello di distribuzione

EduWISP sarà progettato secondo un modello **cloud-first ma self-hostable**.

Sono previsti due scenari:

- **Cloud hosted:** servizio ospitato su infrastruttura cloud, gestibile da un'organizzazione o da un fornitore.
- **Self-hosted:** installazione autonoma presso la scuola, una rete di istituti o un provider scelto dall'organizzazione.

Il sistema server avrà come riferimento **Debian GNU/Linux 13 (Trixie)**.

Il supporto a Debian Trixie dovrà essere considerato un requisito di deployment, da tradurre successivamente in una specifica tecnica.

## Principi del progetto

- Open source.
- Modularità.
- Indipendenza dal cloud proprietario.
- Interoperabilità tramite API.
- Sicurezza e privacy by design.
- Multi-tenancy.
- Documentazione pubblica.
- Comunità e governance trasparenti.
- Nessuna raccolta di dati non necessaria.

## Roadmap progettuale

| Fase | Obiettivo | Stato |
|---|---|---|
| 1 | Visione e obiettivi | In definizione |
| 2 | Requisiti funzionali e non funzionali | Da definire |
| 3 | Modello scuola-famiglia | Da definire |
| 4 | Architettura logica | Da definire |
| 5 | Verifica delle possibilità Android Enterprise | Da verificare |
| 6 | Sicurezza, privacy e conformità | Da definire |
| 7 | Governance e licenza | Da definire |
| 8 | Specifiche tecniche | Non iniziata |
| 9 | Sviluppo | Non iniziato |

## Documentazione

La documentazione completa sarà pubblicata tramite GitHub Pages.

Struttura prevista:

- **Visione e obiettivi**
- Requisiti funzionali e non funzionali
- Architettura generale
- Gestione Android
- Mobile Device Management
- Gestione scolastica
- Family Control
- Policy Engine
- Sicurezza
- Privacy e GDPR
- Deployment e infrastruttura
- Governance e contributi
- Roadmap

## Contributi

EduWISP vuole essere un progetto comunitario.

Nella fase iniziale sono particolarmente importanti:

- Discussioni sui requisiti.
- Proposte architetturali.
- Analisi delle funzionalità Android.
- Valutazioni sulla privacy e sulla sicurezza.
- Contributi alla documentazione.
- Confronto con scuole, docenti e famiglie.

Le modalità di contribuzione e revisione saranno definite nel documento di governance.

## Licenza

La licenza open source dovrà essere scelta prima dell'avvio dello sviluppo.

AGPL-3.0 è una delle opzioni da valutare, soprattutto per la natura server-side della piattaforma, ma non è ancora una decisione definitiva.

---

**EduWISP – Open education device management.**

*Una piattaforma aperta per una gestione consapevole, sicura e condivisa dei dispositivi scolastici.*
