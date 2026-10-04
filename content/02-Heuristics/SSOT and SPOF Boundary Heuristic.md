---
id: PMA-H-SSOT-SPOF-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","boundary","ownership","ssot","spof","autonomy"]
source_ids: ["BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-MATERIALS","DOMAIN-DRIVERS-COURSE"]
---

# SSOT and SPOF Boundary Heuristic

Single Source of Truth i Single Point of Failure odpowiadają na dwa różne pytania.

SSOT pyta: **kto jest autorytatywnym właścicielem faktu lub decyzji?**
SPOF pyta: **od czego zależy zdolność wykonania pracy i co się stanie, gdy ta zależność zniknie?**

## Ważne rozróżnienie

Jedno źródło prawdy nie oznacza jednej fizycznej bazy danych. Informacja może mieć wiele kopii, projekcji i cache'y, jeśli istnieje jeden owner jej znaczenia oraz jawny mechanizm propagacji i uzgadniania.

Autonomia nie oznacza także braku integracji. Moduł jest autonomiczny w zakresie decyzji wtedy, gdy posiada wiedzę potrzebną do podjęcia tej decyzji albo ma jawnie zaakceptowaną zależność od innego właściciela.

## Pytania graniczne

- kto może zaakceptować albo odrzucić zmianę?
- gdzie wymuszany jest invariant?
- czy dwa moduły mogą modyfikować ten sam fakt biznesowy?
- która kopia wygrywa po rozjechaniu danych?
- co dzieje się, gdy upstream jest niedostępny?
- czy synchroniczna zależność tworzy SPOF dla krytycznego flow?
- kto odpowiada za retry, reconciliation i korektę?

## Heurystyka

**shared data ≠ shared ownership**

Jeżeli dwa moduły muszą wspólnie decydować o tym samym fakcie, prawdopodobnie granica jest błędna albo brakuje nadrzędnego modelu odpowiedzialności. Jeżeli jeden moduł jest ownerem, drugi powinien konsumować kontrakt, projekcję albo fakt, zamiast współdzielić prawo mutacji.

Powiązania: [[Architecture Drivers]], [[Unit of Change]], [[Consistency Boundary]], [[Event Command Query]].
