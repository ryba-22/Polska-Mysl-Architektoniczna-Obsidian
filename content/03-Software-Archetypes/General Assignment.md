---
id: PMA-ARCHETYPE-ASSIGNMENT-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["software-archetypes","assignment","optimization","knapsack"]
source_ids: ["SOFTWARE-ARCHETYPES","DOMAIN-DRIVERS-DD-JAVA"]
---

# General Assignment

General Assignment opisuje wybór lub przydział elementów do ograniczonych zasobów przy wielu wymiarach pojemności i wartości.

## Pytania rozpoznawcze

- Czy istnieje pula kandydatów i ograniczona pojemność?
- Czy jeden wybór zużywa kilka rodzajów capacity?
- Czy celem jest maksymalizacja wartości, pokrycia lub wykorzystania?
- Czy heurystyczne if-y zaczynają odtwarzać problem optymalizacyjny?

## Formalizacja

Jednym z możliwych modeli jest multidimensional knapsack; w innych domenach może to być matching lub assignment optimization.
