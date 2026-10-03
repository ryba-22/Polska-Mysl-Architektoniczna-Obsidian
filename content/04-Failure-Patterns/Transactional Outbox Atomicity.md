---
id: PMA-FAIL-OUTBOX-001
type: failure-pattern
publication_status: public
knowledge_status: source-derived
lifecycle: verified
peos_usable: true
tags: ["outbox","atomicity","integration"]
source_ids: ["DOMAIN-DRIVERS-DD-AI"]
---

# Transactional Outbox Atomicity

Outbox daje atomowość tylko wtedy, gdy zmiana stanu producenta i wpis outbox uczestniczą w tej samej transakcji na tym samym transactional resource.

## Werdykt

same resource + same transaction → atomic.

same resource + brak transakcji → atomic after fix.

different resources → not atomic.

## Konsekwencja

Dwa magazyny danych nie stają się atomowe tylko dlatego, że obie operacje są wykonywane w jednej funkcji aplikacyjnej.

Gdy nie da się zachować lokalnej atomowości, potrzebna jest jawna decyzja: outbox w store producenta, CDC/derive-from-committed-state, inny reliability mechanism albo świadomy best-effort.
