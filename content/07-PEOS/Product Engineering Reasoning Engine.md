---
id: PMA-PEOS-REASONING-001
type: peos-model
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["peos","reasoning-engine","ddd","ai"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DOMAIN-DRIVERS-DD-AI","SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA","AI-THAT-WORKS","DEVSTYLE-DDD-EMAIL-CORPUS","DEVSTYLE-FULL-CORPUS-2026-10-03"]
---

# Product Engineering Reasoning Engine

Docelowy przepływ PEOS:

Purpose / Outcome
→ [[Evidence Contract|Evidence]]
→ [[PMA Language Contract|Language Contract]] / [[Kanoniczne pytania PMA|Canonical Questions]]
→ [[Workflow Preflight|Preflight]]
→ Strategic Questions
→ Domain Discovery
→ [[Main Question|Main Questions]] / [[Pivotal Event|Pivotal Events]] / [[Distillation]]
→ [[Problem Classification]]
→ [[Behavior Before Nouns|Behavioral Decomposition]]
→ Structural Recognition
→ [[Model Alternatives|Candidate Models]]
→ Source-of-Truth / Ownership
→ [[Architecture Drivers]]
→ [[Temporal Scale and Volatility Lens|Temporal / Scale / Volatility Lens]]
→ [[Unit of Change]]
→ [[Socio-Technical Boundary|Socio-Technical Analysis]]
→ Context and Coupling Design
→ [[Dynamic Validation]]
→ Scenarios and Counterexamples
→ Failure-Mode / [[Recovery and Human Escalation|Recovery Analysis]]
→ Cost and Risk
→ Decision Metric
→ [[Decision Gate]]
→ Execution / Experiment
→ Verifiers
→ [[Evolutionary Strict Pass Rate|Evolutionary Eval]]
→ Production Traces
→ [[Feedback and Metrics Loop|Feedback]]
→ Revisit or Learning
→ Evidence.

## Structural Recognition

Structural Recognition ma trzy ścieżki:
1. [[Algorithm Recognition|Algorithm Matcher]];
2. [[Software Archetypes|Software Archetype Matcher]];
3. [[Deep Model Quality|Deep Model discovery]].

## Language layer

[[PMA Mental Loop]], [[PMA Language Contract]] i [[Kanoniczne pytania PMA]] są warstwą wejściową Reasoning Engine. AI Brain ma prowadzić analizę językiem celu, problemu, klasy problemu, zachowań, driverów, alternatyw, symulacji zmian, kosztu i feedbacku — a nie językiem katalogu wzorców.

## Invariants

AI Brain nie dobiera rozwiązania technicznego bez wcześniejszego wskazania:
- celu / outcome;
- dowodów;
- klasy problemu;
- istotnych zachowań;
- istotnych drivers;
- failure modes;
- sposobu pomiaru i warunków weryfikacji.

Refaktor wymagający zachowania semantics powinien mieć [[Behavior Preservation Contract]].

Zmiana komunikacji powinna przejść [[Event Command Query]] i, gdy dotyczy, [[Sync to Async Migration]].

Zmiana modelu, która narusza wcześniejsze założenia, powinna uruchomić [[Model Breaking Change]] zamiast być automatycznie dopisywana do istniejącej struktury.

## Execution

PMA dostarcza wiedzę i heurystyki. PEOS odpowiada za routing, gates, decyzje, wykonanie i evidence of completion.
