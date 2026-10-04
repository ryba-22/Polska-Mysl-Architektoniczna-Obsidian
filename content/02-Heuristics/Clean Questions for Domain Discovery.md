---
id: PMA-H-CLEAN-QUESTIONS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["event-storming","facilitation","discovery","questions","language"]
source_ids: ["BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-MATERIALS"]
---

# Clean Questions for Domain Discovery

Pytanie discovery powinno wydobywać model rozmówcy, a nie przemycać model pytającego.

## Transformacja pytań

Zamiast:
- "czy to powinien być osobny mikroserwis?"
- "czy zrobimy to asynchronicznie?"
- "czy to jest agregat?"

pytaj:
- kto posiada wiedzę potrzebną do tej decyzji?
- co musi pozostać prawdziwe, gdy operacja się kończy?
- co może wydarzyć się później i czy biznes to akceptuje?
- co jeśli ta sama prośba przyjdzie dwa razy?
- kiedy to pojęcie zaczyna znaczyć coś innego?
- co robicie dzisiaj, gdy ten przypadek zawodzi?

## Zasada

**technical question → business consequence**

Facylitator nie powinien wymuszać technicznego słownictwa na ekspercie domenowym. Jego zadaniem jest tak przeformułować pytanie, aby odpowiedź dostarczyła evidence potrzebnego później do decyzji technicznej.

## Failure mode

Pytanie sugerujące rozwiązanie daje pozornie szybki rezultat, ale zamienia warsztat discovery w sesję potwierdzania hipotezy architekta.

Powiązania: [[Information Gathering]], [[Kanoniczne pytania PMA]], [[Linguistic Boundary]], [[Evidence Contract]].
