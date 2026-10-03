---
id: PMA-H-MODEL-BREAKING-CHANGE-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: candidate
peos_usable: true
tags: ["ddd","model-evolution","change","refactoring"]
source_ids: ["DEVSTYLE-DDD-EMAIL-CORPUS","DOMAIN-DRIVERS-COURSE"]
---

# Model Breaking Change

Dobrze działający model może przestać być właściwy po zmianie wymagań. To nie zawsze oznacza, że poprzedni model był błędny.

## Sygnały

- nowe wymaganie wymusza wiele wyjątków;
- pojęcia przestają mieć jednoznaczne znaczenie;
- invariant zaczyna przecinać dotychczasową granicę;
- zmiana wymaga koordynacji wielu wcześniej autonomicznych modeli;
- koszt kolejnych zmian rośnie skokowo.

## Reakcja

Wróć do scenariuszy, [[Main Question]], [[Deep Model Quality]] i [[Model Alternatives]]. Zamiast maskować problem kolejnymi flagami, sprawdź, czy zmieniła się sama struktura problemu.

## PEOS

Ewolucja modelu powinna być mierzona przez [[Evolutionary Strict Pass Rate]] oraz architecture/change drift.
