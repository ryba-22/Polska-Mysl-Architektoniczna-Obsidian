---
id: PMA-FAIL-CONCURRENCY-001
type: failure-pattern
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["concurrency","optimistic-locking","stale-state","api"]
source_ids: ["BSLOTA","DOMAIN-DRIVERS-DD-JAVA","SOFTWARE-ARCHETYPES"]
---

# Concurrency and Stale State

Concurrency nie kończy się na wersji w bazie. Konflikt może powstać pomiędzy wcześniejszym odczytem klienta a późniejszą komendą.

## Failure shape

1. klient odczytuje stan V1;
2. ktoś inny zapisuje V2;
3. pierwszy klient wykonuje decyzję opartą na V1;
4. zapis bez kontroli wersji nadpisuje lub łamie invariant.

## Ochrona

- optimistic locking w consistency boundary;
- jawna wersja zasobu;
- na granicy HTTP możliwe ETag / If-Match;
- semantyczny konflikt zamiast generycznego 500;
- retry tylko wtedy, gdy ponowne wykonanie ma prawidłową semantykę.

## Heurystyka

Jeżeli command jest oparty na wcześniej odczytanym mutable state, analizuj zarówno race w DB, jak i staleness klienta.
