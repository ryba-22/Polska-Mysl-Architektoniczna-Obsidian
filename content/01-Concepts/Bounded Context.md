---
id: PMA-CONCEPT-BC-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","bounded-context","language"]
source_ids: ["DDD-BY-EXAMPLES-LIBRARY","DOMAIN-DRIVERS-COURSE"]
---

# Bounded Context

Bounded Context jest granicą spójności modelu i języka dla określonego celu, a nie automatycznie granicą procesu, zespołu, repozytorium czy mikroserwisu.

## Sygnały granicy

- ten sam termin ma inne znaczenie;
- reguły i lifecycle zmieniają się po pivotal event;
- różne fragmenty odpowiadają na inne główne pytania biznesowe;
- ownership danych i reguł jest różny;
- zmiany po jednej stronie nie powinny wymagać synchronicznych zmian po drugiej.

## Test

Czy model po jednej stronie granicy da się zmienić bez znajomości wewnętrznych szczegółów drugiej strony?

Jeżeli nie, zbadaj coupling i [[Connascence]].
