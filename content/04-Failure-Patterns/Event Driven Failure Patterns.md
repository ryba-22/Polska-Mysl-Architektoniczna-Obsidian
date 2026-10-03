---
id: PMA-FAIL-EDA-001
type: failure-pattern
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["event-driven","integration","failure-modes"]
source_ids: ["PILLOPL","DOMAIN-DRIVERS-DD-AI","EMMETT","DDD-BY-EXAMPLES-CQRS"]
---

# Event Driven Failure Patterns

Event-driven architecture wymaga katalogu failure modes, a nie tylko katalogu wzorców.

## Najważniejsze przypadki

- event miss — zmiana stanu wystąpiła, ale integracyjny fakt nie dotarł;
- duplicate delivery — ten sam komunikat jest przetworzony więcej niż raz;
- out-of-order delivery — kolejność obserwowana przez konsumenta różni się od kolejności biznesowej;
- non-idempotent consumer;
- schema versioning;
- behavior versioning — schema pozostaje kompatybilna, ale znaczenie zachowania się zmienia;
- state-transfer event — event staje się kopią całego modelu i rozmywa ownership;
- partial external-call failure;
- read-after-write broken by async;
- non-atomic outbox;
- temporal coupling ukryty pod asynchronicznym transportem.

## Bramka

Każda decyzja o async musi odpowiedzieć na: duplicates, ordering, idempotency, atomicity, retry, recovery, read-after-write i observability.
