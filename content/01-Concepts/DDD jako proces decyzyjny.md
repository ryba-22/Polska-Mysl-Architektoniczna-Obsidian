---
id: PMA-CONCEPT-DDD-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","reasoning"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DEVMOUNTJOB","DDD-BY-EXAMPLES-LIBRARY"]
---

# DDD jako proces decyzyjny

DDD jest przede wszystkim sposobem dochodzenia od problemu biznesowego do modelu i decyzji technicznych.

Przydatna sekwencja:
requirements → information gathering → strategic heuristics → contextual models → problem class → consistency and integration rules → technical solution.

## Heurystyka

Jeżeli rozmowa o DDD zaczyna się od Aggregate, Repository, Event Sourcing lub mikroserwisów, proces prawdopodobnie rozpoczął się za późno.

## Warstwa discovery

[[Information Gathering]] pomaga zebrać wiedzę.
[[Linguistic Boundary]] i scenariusze pomagają znaleźć granice.
[[Problem Classification]] określa rodzaj problemu.
[[Unit of Change]] prowadzi do consistency boundary.

## Antywzorce

- projektowanie od ekranów i tabel;
- używanie całego katalogu DDD niezależnie od złożoności;
- traktowanie bounded context jako synonimu mikroserwisu;
- identyczna architektura lokalna we wszystkich kontekstach.
