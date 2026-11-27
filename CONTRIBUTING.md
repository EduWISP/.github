# Contribuire a EduWISP

🇬🇧 *English summary at the end of this page.*

Grazie per l'interesse! In questa fase EduWISP è dedicato alla **progettazione e alla documentazione**: non sono ancora aperti contributi di codice applicativo.

## ⚠️ Regola fondamentale: nessun dato reale

EduWISP riguarda **minori**. Non inserire **mai** in issue, discussioni, pull request, screenshot o allegati dati personali reali di studenti, famiglie o personale scolastico (nomi, classi, foto, numeri di serie associati a persone, segnalazioni reali). Usa solo esempi fittizi. I contenuti che violano questa regola vengono rimossi.

## Da dove iniziare

Cerca le [buone prime issue](https://github.com/search?q=org%3AEduWISP+label%3A%22good+first+issue%22+state%3Aopen&type=issues) (etichetta `good first issue`) in tutti i repository: sono compiti piccoli, ben descritti e adatti alla fase di progettazione. Commenta la issue per fartela assegnare.

## Dove contribuire

| Cosa | Dove |
|---|---|
| Idee, domande, confronto aperto | [Discussions](https://github.com/EduWISP/docs/discussions) |
| Nuovo requisito o modifica | Issue con modello **Requisito** |
| Verifica di una funzione Android | Issue con modello **Verifica Android** |
| Rischio privacy, legale o di sicurezza | Issue con modello **Privacy e sicurezza** |
| Errori o miglioramenti della documentazione | Issue con modello **Documentazione** o direttamente una pull request |
| Decisione progettuale | Pull request con un nuovo ADR in `docs/decisioni/` |
| Vulnerabilità | **Non** in pubblico: vedi [SECURITY.md](SECURITY.md) |

## Come scrivere un buon contributo

1. Indica il contesto: scuola, famiglia, studente, amministrazione o infrastruttura.
2. Distingui **fatti verificati** (con fonte), **ipotesi** e **opinioni**.
3. Per temi privacy o sicurezza descrivi rischi e possibili mitigazioni, citando le norme pertinenti.
4. Una proposta per issue o pull request.

## Pull request sulla documentazione

- Repository: [EduWISP/docs](https://github.com/EduWISP/docs), cartella `docs/`.
- L'**italiano** è la versione di riferimento. Se modifichi una pagina italiana in modo sostanziale, aggiorna anche la pagina in `docs/_en/` oppure segnalalo nella PR (etichetta `traduzione`).
- Mantieni gli identificativi dei requisiti (`RF-`, `RNF-`, `RC-`): non riutilizzare un ID eliminato.
- Gli ADR accettati non si modificano: si sostituiscono con un nuovo ADR.

## DCO

Ogni commit deve avere il **Developer Certificate of Origin** ([DCO](https://developercertificate.org/)): con la riga `Signed-off-by` dichiari di avere il diritto di inviare il contributo con la licenza del progetto. Basta usare:

```bash
git commit -s -m "Descrizione della modifica"
```

Un controllo automatico verifica il DCO in ogni pull request.

## Licenze

- **Codice:** AGPL-3.0-or-later con termini aggiuntivi di attribuzione e tutela del nome (vedi `NOTICE.md` in ogni repository).
- **Documentazione e testi:** CC BY-SA 4.0.
- **Nome e logo EduWISP:** esclusi dalle licenze aperte ([politica del marchio](https://eduwisp.org/docs/progetto/marchio/)).

Inviando un contributo accetti che venga distribuito con queste licenze. Il copyright resta tuo.

## Lingue

Puoi scrivere in italiano o in inglese.

---

### English summary

EduWISP is in the design phase; code contributions are not open yet. **Never share real personal data** of students, families or staff — use fictional examples only. Use Discussions for ideas, the issue templates for requirements, Android checks, privacy/security concerns and documentation. Italian is the authoritative documentation language; please update or flag the English version (`docs/_en/`) when changing Italian pages. Every commit needs a DCO sign-off (`git commit -s`). Code is AGPL-3.0-or-later with additional attribution and trademark terms; docs are CC BY-SA 4.0; the EduWISP name and logo are not openly licensed. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). You may write in Italian or English.
