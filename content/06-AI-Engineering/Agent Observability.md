---
id: PMA-AI-OBS-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ai","observability","tracing"]
source_ids: ["AI-THAT-WORKS"]
---

# Agent Observability

W systemach, gdzie agenci generują wiele zmian i zachowanie jest częściowo niedeterministyczne, tracing staje się źródłem dowodów o rzeczywistym wykonaniu.

## Trace trzy poziomy

- design: co agent przewidywał i jaki call stack zakładał;
- code: jakie elementy zostały rzeczywiście użyte;
- runtime: jak system zachował się w produkcji.

## Pętla uczenia

production trace
→ divergence from design
→ missing assumption
→ nowa heurystyka / eval / invariant
→ następny run.

Observability jest najbardziej wartościowe po wystąpieniu nieoczekiwanego problemu, dlatego instrumentacja musi istnieć wcześniej.
