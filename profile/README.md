<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/EduWISP/.github/main/branding/eduwisp-logo-dark.svg">
    <img src="https://raw.githubusercontent.com/EduWISP/.github/main/branding/eduwisp-logo.svg" alt="EduWISP" height="90">
  </picture>
</p>

<p align="center">
  <b>Piattaforma open source per la gestione dei dispositivi Android scolastici</b><br>
  <i>Open-source platform for managing school-owned Android devices</i>
</p>

EduWISP vuole offrire alle scuole uno strumento aperto, modulare e indipendente per gestire i tablet Android usati nella didattica. Unisce **MDM**, **gestione scolastica**, **Family Control** e strumenti di **prevenzione del cyberbullismo**, ispirandosi alla filosofia di [OpenWISP](https://openwisp.org/).

> 🚧 **Fase di progettazione.** Stiamo definendo visione, requisiti, architettura, sicurezza, privacy e governance. Lo sviluppo software non è ancora iniziato.

### 📖 [Leggi la documentazione](https://eduwisp.github.io/docs/) · 🇬🇧 [English](https://eduwisp.github.io/docs/en/)

## In breve

| | |
|---|---|
| 🏫 **Scuola** | Gestione centralizzata di dispositivi, app e regole per istituto, plesso, classe e studente |
| 👪 **Famiglia** | Regole aggiuntive per l'uso domestico, senza poter scavalcare sicurezza e didattica |
| 🛡️ **Tutela** | Segnalazione e gestione del cyberbullismo, senza sorveglianza degli studenti |
| ⚖️ **Conformità** | GDPR e normativa italiana su privacy e minori come vincolo bloccante |
| 🆓 **Libero** | Solo software open source e gratuito: dove serve un servizio proprietario, costruiamo l'alternativa |
| ☁️ **Hosting** | Cloud-first ma sempre self-hostable, server di riferimento Debian 13 |

## Partecipa

In questa fase servono soprattutto: casi d'uso delle scuole, analisi di Android Enterprise, revisione legale e privacy (DPO, giuristi), revisione della documentazione e traduzioni.

- 🌱 [Buone prime issue](https://github.com/search?q=org%3AEduWISP+label%3A%22good+first+issue%22+state%3Aopen&type=issues): compiti adatti a chi inizia, in tutti i repository
- 💬 [Discussions](https://github.com/EduWISP/docs/discussions): idee e domande
- 📝 [Issue](https://github.com/EduWISP/docs/issues/new/choose): requisiti, verifiche Android, privacy
- 🤝 [Come contribuire](https://github.com/EduWISP/.github/blob/main/CONTRIBUTING.md) · [Codice di condotta](https://github.com/EduWISP/.github/blob/main/CODE_OF_CONDUCT.md)

## Repository

Ogni modulo ha un **proprio repository**, così che chiunque possa prenderne in carico uno in modo indipendente (sul modello di OpenWISP). Il core è **indipendente dalla piattaforma**: Android è il primo agente, altre piattaforme potranno aggiungersi. Tutti i moduli sono in fase di progettazione.

| Area | Repository |
|---|---|
| 📖 Progetto | [docs](https://github.com/EduWISP/docs) · [.github](https://github.com/EduWISP/.github) |
| 🧱 Base | [eduwisp-utils](https://github.com/EduWISP/eduwisp-utils) · [eduwisp-users](https://github.com/EduWISP/eduwisp-users) · [eduwisp-audit](https://github.com/EduWISP/eduwisp-audit) |
| 🏫 Moduli | [eduwisp-school](https://github.com/EduWISP/eduwisp-school) · [eduwisp-devices](https://github.com/EduWISP/eduwisp-devices) · [eduwisp-apps](https://github.com/EduWISP/eduwisp-apps) · [eduwisp-policy](https://github.com/EduWISP/eduwisp-policy) · [eduwisp-family](https://github.com/EduWISP/eduwisp-family) · [eduwisp-wellbeing](https://github.com/EduWISP/eduwisp-wellbeing) |
| 📱 Dispositivi | [eduwisp-protocol](https://github.com/EduWISP/eduwisp-protocol) · [eduwisp-android-dpc](https://github.com/EduWISP/eduwisp-android-dpc) |
| 🚀 Installazione | [ansible-eduwisp](https://github.com/EduWISP/ansible-eduwisp) · [docker-eduwisp](https://github.com/EduWISP/docker-eduwisp) |

Vuoi occuparti di un modulo? [Proponiti in Discussions](https://github.com/EduWISP/docs/discussions).

---|---|
| [docs](https://github.com/EduWISP/docs) | Documentazione di progetto, requisiti e decisioni (ADR) |

Ogni modulo avrà un **proprio repository**, così che chiunque possa prenderne in carico uno in modo indipendente (sul modello di OpenWISP). I repository dei moduli (`eduwisp-users`, `eduwisp-devices`, `eduwisp-policy`, `eduwisp-family`, `eduwisp-android-dpc`, …) verranno creati all'avvio dello sviluppo: vedi la [mappa dei repository](https://eduwisp.github.io/docs/architettura/repository/). Vuoi occuparti di un modulo? [Proponiti in Discussions](https://github.com/EduWISP/docs/discussions).

---

*🇬🇧 EduWISP is an open-source project, currently in the design phase, to manage school-owned Android tablets with MDM, school management, family control and cyberbullying prevention, with full compliance with EU and Italian law on data protection and minors. Documentation is in Italian (default) and English.*
