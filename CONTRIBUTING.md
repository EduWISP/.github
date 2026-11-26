# Contribuire a EduWISP

🇬🇧 *English summary at the end of this page.*

Grazie per l'interesse! In questa fase EduWISP è dedicato alla **progettazione e alla documentazione**: non sono ancora aperti contributi di codice applicativo.

## ⚠️ Regola fondamentale: nessun dato reale

EduWISP riguarda **minori**. Non inserire **mai** in issue, discussioni, pull request, screenshot o allegati dati personali reali di studenti, famiglie o personale scolastico (nomi, classi, foto, numeri di serie associati a persone, segnalazioni reali). Usa solo esempi fittizi. I contenuti che violano questa regola vengono rimossi.

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

## Lingue

Puoi scrivere in italiano o in inglese.

---

### English summary

EduWISP is in the design phase; code contributions are not open yet. **Never share real personal data** of students, families or staff — use fictional examples only. Use Discussions for ideas, the issue templates for requirements, Android checks, privacy/security concerns and documentation. Italian is the authoritative documentation language; please update or flag the English version (`docs/_en/`) when changing Italian pages. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). You may write in Italian or English.
