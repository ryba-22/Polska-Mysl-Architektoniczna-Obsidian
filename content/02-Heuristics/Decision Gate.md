---
id: PMA-H-DECISION-GATE-001
type: heuristic
publication_status: public
knowledge_status: peos-decision
lifecycle: active
peos_usable: true
tags: ["ai","governance","decision","gate"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","AI-THAT-WORKS"]
---

# Decision Gate

Agent może samodzielnie wykonywać odwracalne kroki, ale decyzje o wysokim koszcie zmiany powinny przechodzić jawny gate.

## Przepływ

discover → evidence → propose options → trade-offs → decision gate → execute → verify.

## Typowe gate points

- architecture boundary;
- data model i migration;
- public contract;
- security/permission model;
- integration style;
- destructive operation;
- nieodwracalna zmiana danych;
- decyzja wpływająca na produkt lub użytkownika.

## Zasada

Human gate nie oznacza ręcznego zatwierdzania każdej linijki. Oznacza zachowanie ownership nad decyzją, której konsekwencje wykraczają poza lokalny krok execution.
