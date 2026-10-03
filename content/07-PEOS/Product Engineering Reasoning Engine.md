---
id: PMA-PEOS-REASONING-001
type: peos-model
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["peos","reasoning-engine","ddd","ai"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DOMAIN-DRIVERS-DD-AI","SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA","AI-THAT-WORKS","DEVSTYLE-DDD-EMAIL-CORPUS"]
---

# Product Engineering Reasoning Engine

Docelowy przepływ PEOS:

[[Evidence Contract|Evidence]]
→ [[PMA Language Contract|Language Contract]] / [[Kanoniczne pytania PMA|Canonical Questions]]
→ [[Workflow Preflight|Preflight]]
→ Strategic Questions
→ Domain Discovery
→ Scenarios and Counterexamples
→ Boundary Discovery
→ [[Problem Classification]]
→ Structural Recognition
→ [[Model Alternatives]]
→ [[Unit of Change]]
→ Consistency Design
→ Context and Coupling Design
→ [[Dynamic Validation]]
→ Failure-Mode Analysis
→ [[Architecture Drivers]]
→ [[Decision Gate]]
→ Execution
→ Verifiers
→ [[Evolutionary Strict Pass Rate|Evolutionary Eval]]
→ Production Traces
→ Learning
→ Evidence.

## Structural Recognition

Structural Recognition ma trzy ścieżki:
1. [[Algorithm Recognition|Algorithm Matcher]];
2. [[Software Archetypes|Software Archetype Matcher]];
3. [[Deep Model Quality|Deep Model discovery]].

## Language layer

[[PMA Language Contract]] i [[Kanoniczne pytania PMA]] są warstwą wejściową Reasoning Engine. AI Brain ma prowadzić analizę językiem problemów, driverów, alternatyw, symulacji zmian i konsekwencji, a nie językiem katalogu wzorców.

## Invariants

AI Brain nie dobiera rozwiązania technicznego bez wcześniejszego wskazania dowodów, klasy problemu, istotnych drivers, failure modes i warunków weryfikacji.

Refaktor wymagający zachowania semantics powinien mieć [[Behavior Preservation Contract]]. Zmiana komunikacji powinna przejść [[Event Command Query]] i, gdy dotyczy, [[Sync to Async Migration]].

## Execution

PMA dostarcza wiedzę i heurystyki. PEOS odpowiada za routing, gates, decyzje, wykonanie i evidence of completion.
