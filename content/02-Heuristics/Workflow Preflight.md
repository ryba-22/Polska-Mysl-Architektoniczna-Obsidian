---
id: PMA-H-WORKFLOW-PREFLIGHT-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: active
peos_usable: true
tags: ["preflight","workflow","scope","overengineering"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","DOMAIN-DRIVERS-COURSE"]
---

# Workflow Preflight

Przed kosztownym workflow sprawdź, czy dana technika jest właściwa dla problemu.

## Pytania bazowe

- Czy istnieje problem wystarczająco ważny, by go rozwiązywać?
- Czy mamy wystarczające evidence do rozpoczęcia?
- Czy wybrany typ analizy pasuje do klasy problemu?
- Czy decyzja jest odwracalna?
- Czy istnieje tańsza technika lub eksperyment?
- Czy potrzebna jest jawna decyzja człowieka?

## Warianty

Ten sam kontrakt można stosować jako discovery-preflight, architecture-preflight, refactor-preflight, migration-preflight, integration-preflight i deployment-preflight.

## PEOS

Preflight ma zapobiegać AI overengineering oraz uruchamianiu ciężkiego procesu tylko dlatego, że dana technika jest dostępna.
