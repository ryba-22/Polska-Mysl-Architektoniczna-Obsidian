---
id: PMA-H-LOCAL-ARCH-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["architecture","bounded-context","complexity","local-architecture"]
source_ids: ["DDD-BY-EXAMPLES-LIBRARY","DOMAIN-DRIVERS-COURSE"]
---

# Local Architecture by Problem Complexity

Architektura powinna być dobierana lokalnie do złożoności modelu, a nie raz dla całej aplikacji.

## Heurystyka

- kontekst z bogatymi invariantami i zachowaniem może uzasadniać model domenowy i porty/adapters;
- prosty kontekst informacyjny może pozostać CRUD-em;
- read model może być projekcją bez bogatego modelu zapisu;
- integration context może potrzebować przede wszystkim kontraktów, idempotencji i recovery.

## Invariant PEOS

Bounded Context nie implikuje automatycznie Aggregate + Repository + CQRS + Hexagonal Architecture.

Dobór rozwiązania następuje po [[Problem Classification]] i [[Architecture Drivers]].
