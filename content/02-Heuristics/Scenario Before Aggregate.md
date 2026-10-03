---
id: PMA-H-SCENARIO-BEFORE-AGGREGATE-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","design-level","aggregate","example-mapping"]
source_ids: ["DDD-BY-EXAMPLES-LIBRARY","DEVMOUNTJOB","DOMAIN-DRIVERS-COURSE"]
---

# Scenario Before Aggregate

Nie zaczynaj Design Level od wskazywania agregatów. Najpierw zbierz scenariusze, kontrprzykłady, komendy, zdarzenia, read modele i reguły biznesowe.

## Heurystyka

Jeżeli nie potrafimy jeszcze opisać:
- co użytkownik próbuje osiągnąć;
- jakie fakty są potrzebne do decyzji;
- kiedy operacja ma się nie udać;
- jakie konsekwencje biznesowe ma sukces lub porażka;

to wyznaczanie agregatu jest przedwczesne.

## Dlaczego

Wczesne nazwanie Aggregate kotwiczy modelera w rozwiązaniu technicznym. Praca na przykładach pozwala najpierw odkryć zachowanie i odpowiedzialności.

## Następny krok

Po ustabilizowaniu scenariuszy przejdź do [[Unit of Change]] i [[Consistency Boundary]].
