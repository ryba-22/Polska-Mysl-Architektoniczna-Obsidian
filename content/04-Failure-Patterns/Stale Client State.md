---
id: PMA-FP-STALE-CLIENT-001
type: failure-pattern
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["concurrency","api","stale-state","optimistic-locking"]
source_ids: ["BSLOTA","DOMAIN-DRIVERS-DD-JAVA"]
---

# Stale Client State

Konflikt współbieżności może powstać nie tylko pomiędzy dwiema transakcjami w bazie, ale również między odczytem klienta a późniejszą komendą.

## Sygnał

Klient odczytuje mutable state, podejmuje decyzję i po pewnym czasie wysyła zmianę opartą na poprzedniej wersji.

## Konsekwencja

Sam optimistic lock chroni zapis, ale konflikt musi mieć semantykę na granicy systemu.

## Mitigacje

- version token;
- ETag / If-Match;
- jawny conflict result;
- ponowny odczyt i decyzja użytkownika;
- idempotent retry tylko tam, gdzie zachowanie jest bezpieczne.

Zobacz [[Concurrency and Stale State]].
