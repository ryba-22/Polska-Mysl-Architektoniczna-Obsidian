---
id: PMA-CONCEPT-CONNASCENCE-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["coupling","boundaries","architecture"]
source_ids: ["DOMAIN-DRIVERS-DD-AI"]
---

# Connascence

Dwa elementy są connascent, gdy zmiana jednego wymaga odpowiadającej zmiany drugiego, aby system pozostał poprawny.

Przydatna gradacja od słabszej do silniejszej:
Name → Type → Meaning → Position → Algorithm → Execution → Timing → Value → Identity.

## Reguła granicy

Maksymalizuj potrzebne sprzężenie wewnątrz modułu. Minimalizuj sprzężenie przekraczające granicę. To, co musi przekraczać granicę, powinno być możliwie słabe i mieć niski degree.

## Sygnał złej granicy

Strong + high-degree connascence przekraczające boundary oznacza, że granica jest nieszczelna albo fikcyjna.
