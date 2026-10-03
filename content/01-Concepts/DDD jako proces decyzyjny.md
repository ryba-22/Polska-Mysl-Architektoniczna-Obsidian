---
id: PMA-CONCEPT-DDD-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","reasoning"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DEVMOUNTJOB","DDD-BY-EXAMPLES-LIBRARY","DEVSTYLE-DDD-EMAIL-CORPUS"]
---

# DDD jako proces decyzyjny

DDD jest przede wszystkim sposobem dochodzenia od problemu biznesowego do modelu i decyzji technicznych.

Przydatna sekwencja:
observation → question → evidence → problem → problem class → candidate models → drivers → heuristics → alternatives → change simulation → consequences and cost → decision → verification → technical solution.

[[Język polskiej myśli architektonicznej]] opisuje charakterystyczny rejestr pytań i sformułowań używany do utrzymania tego procesu w stanie falsyfikowalnym.

## Heurystyka

Jeżeli rozmowa o DDD zaczyna się od Aggregate, Repository, Event Sourcing lub mikroserwisów, proces prawdopodobnie rozpoczął się za późno.

[[Heuristic Engineering]] opisuje nadrzędną zasadę: nie istnieje jeden idealny proces ani jedna architektura; kompetencją jest dobór heurystyki do klasy problemu i evidence.

## Warstwa discovery

[[Information Gathering]] pomaga zebrać wiedzę.
[[Main Question]], [[Alternative Process Flow]], [[Pivotal Event]], [[Linguistic Boundary]] i [[Distillation]] pomagają odkrywać granice.
[[Deep Model Quality]] i [[Model Alternatives]] pomagają porównywać reprezentacje problemu.
[[Problem Classification]] określa rodzaj problemu.
[[Unit of Change]] i [[Aggregate Sizing]] prowadzą do consistency boundary.
[[Dynamic Validation]] sprawdza granice w rzeczywistym przepływie.

## Antywzorce

- projektowanie od ekranów i tabel;
- używanie całego katalogu DDD niezależnie od złożoności;
- traktowanie bounded context jako synonimu mikroserwisu;
- identyczna architektura lokalna we wszystkich kontekstach.
