---
id: PMA-CONCEPT-DDD-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","reasoning"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DEVMOUNTJOB","DDD-BY-EXAMPLES-LIBRARY","DEVSTYLE-DDD-EMAIL-CORPUS","DEVSTYLE-FULL-CORPUS-2026-10-03","BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-ARTICLES"]
---

# DDD jako proces decyzyjny

DDD jest przede wszystkim sposobem dochodzenia od problemu biznesowego do modelu i decyzji technicznych.

Przydatna sekwencja:
purpose / outcome → observation → question → evidence → problem → problem class → behavior / capability → candidate models → source of truth / ownership → drivers → alternatives → temporal / scale / volatility lens → change and failure simulation → socio-technical effects → consequences / cost / risk → decision metric → decision → verification → feedback → revisit.

[[PMA Mental Loop]] opisuje operacyjny przebieg tego procesu, a [[Język polskiej myśli architektonicznej]] — charakterystyczny rejestr pytań i sformułowań używany do utrzymania go w stanie falsyfikowalnym.

## Heurystyka

Jeżeli rozmowa o DDD zaczyna się od Aggregate, Repository, Event Sourcing lub mikroserwisów, proces prawdopodobnie rozpoczął się za późno.

[[Heuristic Engineering]] opisuje nadrzędną zasadę: nie istnieje jeden idealny proces ani jedna architektura; kompetencją jest dobór heurystyki do klasy problemu i evidence.

## Warstwa discovery

[[Information Gathering]] pomaga zebrać wiedzę.
[[Main Question]], [[Alternative Process Flow]], [[Pivotal Event]], [[Linguistic Boundary]] i [[Distillation]] pomagają odkrywać granice.
[[Purpose Before Structure]] i [[Behavior Before Nouns]] pilnują, aby struktura wynikała z celu i zachowania, a nie tylko z rzeczowników.
[[Deep Model Quality]] i [[Model Alternatives]] pomagają porównywać reprezentacje problemu.
[[Problem Classification]] określa rodzaj problemu.
[[Unit of Change]] i [[Aggregate Sizing]] prowadzą do consistency boundary.
[[Temporal Scale and Volatility Lens]] oraz [[Socio-Technical Boundary]] sprawdzają model w czasie, skali i strukturze odpowiedzialności.
[[Dynamic Validation]] sprawdza granice w rzeczywistym przepływie.
[[Feedback and Metrics Loop]] domyka decyzję przez pomiar i production evidence.

## Antywzorce

- projektowanie od ekranów i tabel;
- używanie całego katalogu DDD niezależnie od złożoności;
- traktowanie bounded context jako synonimu mikroserwisu;
- identyczna architektura lokalna we wszystkich kontekstach;
- ocenianie modelu wyłącznie na podstawie elegancji struktury, bez miary efektu.
