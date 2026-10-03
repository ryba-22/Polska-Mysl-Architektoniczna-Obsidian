---
id: PMA-PEOS-REASONING-001
type: peos-model
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["peos","reasoning-engine","ddd","ai"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DOMAIN-DRIVERS-DD-AI","SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA","AI-THAT-WORKS"]
---

# Product Engineering Reasoning Engine

Docelowy przepływ PEOS:

Evidence
→ Strategic Questions
→ Domain Discovery
→ Scenarios and Counterexamples
→ Boundary Discovery
→ Problem Classification
→ Structural Recognition
→ Unit of Change
→ Consistency Design
→ Context and Coupling Design
→ Failure-Mode Analysis
→ Architecture Drivers
→ Decision Record
→ Execution
→ Verifiers
→ Evolutionary Eval
→ Production Traces
→ Learning
→ Evidence.

## Structural Recognition

Structural Recognition ma trzy ścieżki:
1. Algorithm Matcher;
2. Software Archetype Matcher;
3. Deep Model discovery.

## Language layer

[[PMA Language Contract]] i [[Kanoniczne pytania PMA]] są warstwą wejściową Reasoning Engine. AI Brain ma prowadzić analizę językiem problemów, driverów, alternatyw, symulacji zmian i konsekwencji, a nie językiem katalogu wzorców.

## Invariant

AI Brain nie dobiera rozwiązania technicznego bez wcześniejszego wskazania:
- dowodów;
- klasy problemu;
- istotnych drivers;
- failure modes;
- warunków weryfikacji.

## Execution

PMA dostarcza wiedzę i heurystyki. PEOS odpowiada za routing, gates, decyzje, wykonanie i evidence of completion.
