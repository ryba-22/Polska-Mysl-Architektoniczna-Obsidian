---
id: PMA-H-ECQ-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","integration","event","command","query"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DOMAIN-DRIVERS-DD-AI","BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-ARTICLES"]
---

# Event Command Query

Event, Command i Query opisują semantykę komunikacji, a nie wybrany transport.

## Event

Fakt, który już zaszedł. Nadawca publikuje informację i nie wskazuje jednego odbiorcy, który ma wykonać konkretną czynność.

## Command

Intencja wykonania operacji. Ma jednego logicznego adresata odpowiedzialnego za decyzję lub zmianę stanu.

## Query

Pytanie o informację. Nie powinno zmieniać Source of Truth i oczekuje odpowiedzi.

## Heurystyka

Przed wyborem brokera, RPC lub HTTP nazwij intencję komunikatu. Zmiana transportu nie zmienia Command w Event.

Zobacz [[Transactional Outbox Atomicity]] i [[Sync to Async Migration]].
