---
id: PMA-EVAL-STRICT-001
type: eval
publication_status: public
knowledge_status: synthesis
lifecycle: active
peos_usable: true
tags: ["evals","strict-pass","agents","maintainability"]
source_ids: ["AI-THAT-WORKS"]
---

# Evolutionary Strict Pass Rate

## Metryka

Isolated pass: agent rozwiązał aktualny checkpoint.

Strict pass: agent rozwiązał aktualny checkpoint i zachował poprawność wszystkich wcześniejszych checkpointów.

## Protokół PEOS

1. zamroź sekwencję zmian;
2. wykonuj je kolejno na tym samym codebase;
3. po każdym kroku uruchamiaj pełny zbiór wcześniejszych kontraktów;
4. rejestruj regressions, complexity drift, dependency drift i architecture violations;
5. porównuj modele/harnessy na tej samej sekwencji.

## Wartość

Ta metryka przybliża pytanie: czy Brain potrafi rozwijać system, a nie tylko jednorazowo rozwiązać ticket.
