---
id: PMA-H-EVIDENCE-CONTRACT-001
type: heuristic
publication_status: public
knowledge_status: peos-decision
lifecycle: active
peos_usable: true
tags: ["evidence","reasoning","decision","ai"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","AI-THAT-WORKS"]
---

# Evidence Contract

Istotna decyzja nie powinna istnieć wyłącznie jako konkluzja modelu. Musi mieć ślad prowadzący od twierdzenia do dowodów i ograniczeń.

## Minimalny kontrakt

- claim / statement;
- evidence refs;
- strength lub confidence rubric;
- scope;
- assumptions;
- contradictions;
- limitations;
- decision owner;
- lifecycle/status;
- verification lub falsification condition.

## Zasada

Brak dowodu nie jest dowodem negatywnym. Konflikt źródeł pozostaje jawny, dopóki scenariusz lub właściciel decyzji go nie rozstrzygnie.

## PEOS

To rozszerza Evidence Ledger: evidence służy nie tylko audytowi po fakcie, lecz steruje tym, czy [[Workflow Preflight]] i gate mogą przepuścić decyzję.
