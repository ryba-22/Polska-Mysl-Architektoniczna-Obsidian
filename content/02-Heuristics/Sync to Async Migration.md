---
id: PMA-H-SYNC-ASYNC-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["integration","async","migration","outbox","workflow"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","DEVSTYLE-DDD-EMAIL-CORPUS"]
---

# Sync to Async Migration

Przejście z wywołania synchronicznego na asynchroniczne jest zmianą semantyki czasu i awarii, nie prostą podmianą transportu.

## Discovery

Najpierw ustal producer, consumer, obecny styl komunikacji, kto czyta efekt jako następny, storage producenta, transaction span, wymagania ordering, istniejący outbox i test pokrywający cross-model effect.

## Klasyfikacja

Jeżeli caller używa wartości zwrotnej albo następny krok musi natychmiast zobaczyć efekt, migracja może zmieniać zachowanie biznesowe. Najpierw rozstrzygnij [[Event Command Query]].

## Workflow

discover → classify → define atomicity → design outbox → relay → consumer → idempotency/retry → contract tests → integration verification.

## Gate

Stan domenowy i wpis outbox muszą mieć udowodnioną [[Transactional Outbox Atomicity]]. Partial failure, duplicate delivery i read-after-write muszą mieć jawne zachowanie.
