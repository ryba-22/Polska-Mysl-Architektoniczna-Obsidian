---
id: PMA-H-BEHAVIOR-PRESERVATION-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["refactoring","behavior","contract","verification"]
source_ids: ["DOMAIN-DRIVERS-DD-AI"]
---

# Behavior Preservation Contract

Refaktor lub zmiana idiomu implementacyjnego powinny zaczynać się od jawnego kontraktu zachowania.

## Kontrakt

Przed zmianą ustal:
- observable outcomes;
- public surface;
- consistency boundary;
- istniejące testy;
- coverage gaps;
- side effects i failure semantics.

Następnie zamroź minimalny zestaw executable tests, który reprezentuje zachowanie wymagające zachowania.

## Gate

Nie oceniaj refaktoru przez "kod wygląda lepiej". Zmiana przechodzi dopiero, gdy kontrakt zachowania jest nadal spełniony, a deklarowana właściwość została poprawiona.

## Powiązania

[[Scenario Before Aggregate]], [[Architecture Code Gap]], [[Evolutionary Strict Pass Rate]].
