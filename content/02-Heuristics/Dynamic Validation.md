---
id: PMA-H-DYNAMIC-VALIDATION-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: verified
peos_usable: true
tags: ["ddd","boundaries","runtime","validation"]
source_ids: ["DEVSTYLE-DDD-EMAIL-CORPUS","DOMAIN-DRIVERS-COURSE"]
---

# Dynamic Validation

Granica narysowana na mapie jest hipotezą. Trzeba sprawdzić, jak modele współpracują w rzeczywistym przepływie.

## Pytania

- kto inicjuje komunikację;
- w którą stronę płyną zależności;
- czy wymagany jest sync czy async;
- jak często modele muszą rozmawiać;
- czy jedno żądanie wymaga wielu round-tripów;
- czy jeden invariant przecina proponowaną granicę;
- jakie partial failures powstaną po rozdzieleniu.

## Sygnał złej granicy

Jeżeli dwa "autonomiczne" modele stale potrzebują synchronicznego dostępu do wzajemnego state, wspólnej transakcji albo koordynowanej zmiany, granicę należy ponownie zakwestionować.

Zobacz [[Connascence]] i [[Architecture Code Gap]].
