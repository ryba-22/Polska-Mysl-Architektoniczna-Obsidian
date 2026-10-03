---
id: PMA-H-ARCH-DRIVERS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["architecture","decision","drivers"]
source_ids: ["DOMAIN-DRIVERS-COURSE"]
---

# Architecture Drivers

Technologia i pattern są liściem drzewa decyzyjnego, nie jego korzeniem.

## Drivers

- typ złożoności;
- klasa problemu;
- ownership danych i logiki;
- Single Source of Truth;
- transaction boundary;
- SLA i availability;
- scale i latency;
- privacy i regulacje;
- failure isolation i Single Point of Failure;
- changeability;
- stabilność modelu biznesowego;
- umiejętności i autonomia zespołu.

## Proces

Drivers → constraints → options → trade-offs → decision → verification.

Dopiero tutaj rozważamy sync/async, broker/RPC, local/distributed, optimistic locking, CQRS, outbox, styl programowania i strategię testów.
