---
id: PMA-H-AGGREGATE-SIZING-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["ddd","aggregate","consistency","concurrency"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DDD-CREW","DEVSTYLE-DDD-EMAIL-CORPUS","BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-ARTICLES"]
---

# Aggregate Sizing

Aggregate jest najmniejszą jednostką, która musi pozostać spójna atomowo. Nie jest grafem obiektów potrzebnych przez ekran.

## Sygnały do analizy

- liczba i siła invariantów;
- command rate;
- liczba konkurujących klientów/aktorów;
- lifetime agregatu;
- tempo przyrostu eventów/stanu;
- contention i częstotliwość optimistic-lock conflicts;
- liczba corrective policies wymaganych poza granicą.

## Trade-off

Większy aggregate upraszcza część invariantów, ale zwiększa contention i koszt ładowania. Mniejszy aggregate zwiększa autonomię, ale może wymagać eventual consistency, reconciliation i corrective policies.

## Gate

Granica powinna wynikać z [[Unit of Change]] i [[Consistency Boundary]], a następnie przejść scenariusze współbieżności i failure modes.
