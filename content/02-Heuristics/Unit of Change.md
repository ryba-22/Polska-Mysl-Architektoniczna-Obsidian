---
id: PMA-H-CONSISTENCY-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: verified
peos_usable: true
tags: ["consistency","concurrency","aggregate","ddd"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DOMAIN-DRIVERS-DD-JAVA","BSLOTA"]
---

# Unit of Change

## Główne pytania

- które eventy zmieniają stan wpływający na Single Source of Truth?
- czy komendy dotyczące tego samego stanu mogą być przetwarzane równolegle?
- jaki stan musi zmienić się atomowo?
- jakie są konsekwencje braku wspólnej transakcji?
- czy event może zostać powtórzony?
- czy zamiast niego może zajść inny event?
- czy inny event może być jego konsekwencją?

## Heurystyka

Jeżeli odpowiedź na pytanie czy operacja jest dozwolona zależy od stanu, który może zmienić inna równoległa komenda, uruchom analizę concurrency i consistency boundary.

## Zakaz przedwczesnej implementacji

No Aggregate before Unit-of-Change evidence.

Najpierw zachowania, reguły, scenariusze i konflikty. Dopiero potem [[Consistency Boundary]] i mechanizm implementacyjny.
