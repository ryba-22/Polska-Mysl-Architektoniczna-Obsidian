---
id: PMA-COMPARE-STRUCTURE-001
type: comparison
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["pattern","archetype","algorithm","modeling"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA"]
---

# Pattern vs Archetype vs Algorithm

## Algorithm

Odpowiada na formalny problem obliczeniowy.

Przykłady: topological sort, matching, knapsack, SAT, graph traversal.

## Software Archetype

Odpowiada na powtarzalny kształt modelu biznesowego.

Przykłady: Availability, Pricing, Accounting, Waitlist, Configurator, Plan vs Execution.

## Pattern

Odpowiada na powtarzalny problem projektowy lub implementacyjny w określonym kontekście.

Przykłady: Aggregate, Saga, Outbox, Repository.

## Reguła kolejności

Najpierw rozpoznaj problem i strukturę. Dopiero potem wybieraj pattern.

Business language
→ problem structure
→ algorithm/archetype/deep model
→ architecture drivers
→ implementation pattern.

## Ryzyko

Pattern-first design łatwo zamienia system w katalog wzorców bez związku z realną złożonością.
