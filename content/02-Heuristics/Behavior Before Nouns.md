---
id: PMA-H-BEHAVIOR-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["behavior","modularity","boundaries","ddd"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE"]
---

# Behavior Before Nouns

## Teza

Rzeczowniki są słabym domyślnym kryterium modularyzacji. Ten sam „obiekt” może uczestniczyć w kilku modelach, bo w różnych kontekstach interesują nas inne zachowania, reguły i dane.

Przed pytaniem „gdzie należy encja?” zapytaj „jakie decyzje i operacje wykonujemy?”.

## Pytania

- Jakie czasowniki opisują użycie tego pojęcia?
- Które operacje mają własne reguły?
- Czy wykonanie jednej operacji wpływa na możliwość wykonania innej?
- Czy dwa use case'y używają tego samego rzeczownika, ale wymagają innego modelu?
- Czy zmiany zachowania propagują się razem?
- Czy podział według behavior zmniejsza liczbę zależności?

## Przykład heurystyczny

„Pojazd” może oznaczać inny model dla katalogowania floty, sprawdzania dostępności, planowania transportu i zgodności certyfikatów.

Wspólny rzeczownik nie implikuje wspólnego modelu.

## Powiązania

- [[Purpose Before Structure]]
- [[Linguistic Boundary]]
- [[Unit of Change]]
- [[Socio-Technical Boundary]]
