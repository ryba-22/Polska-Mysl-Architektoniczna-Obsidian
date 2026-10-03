---
id: PMA-H-ARCH-SANDBOX-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["sandbox","experiment","architecture","validation","risk"]
source_ids: ["FINTECH-POLAND-ECOSYSTEM"]
---

# Architecture Sandbox

## Teza

Ryzykownej decyzji architektonicznej nie trzeba rozstrzygać wyłącznie dyskusją. Można zbudować kontrolowane środowisko do sprawdzenia hipotezy przed migracją produkcyjną.

## Przepływ

**hypothesis → isolated implementation → production-like scenarios → metrics → failure injection → observation → decision**

## Przed eksperymentem

- Jaką hipotezę testujemy?
- Jakiego efektu oczekujemy?
- Co może ją obalić?
- Jakie scenariusze produkcyjne trzeba odwzorować?
- Jaką metrykę porównamy?

## Sandbox powinien umożliwiać

- reprezentatywne dane lub bezpieczny odpowiednik;
- symulowanie skali;
- partial failure i retry;
- concurrency;
- replay;
- porównanie starego i nowego modelu;
- obserwację skutków bez wpływania na source of truth.

## Exit criteria

Eksperyment kończy się decyzją, nie samym działającym prototypem.

Zapisz wynik, evidence, konsekwencje, decyzję i revisit trigger.

## Powiązania

- [[Feedback and Metrics Loop]]
- [[Decision Gate]]
- [[Dynamic Validation]]
- [[PMA Mental Loop]]
