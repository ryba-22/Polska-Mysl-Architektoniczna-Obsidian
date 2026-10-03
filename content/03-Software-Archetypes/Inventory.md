---
id: PMA-ARCHETYPE-INVENTORY-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["software-archetypes","inventory","availability","reservation"]
source_ids: ["ARCHETYPY-OPROGRAMOWANIA"]
---

# Inventory

Inventory reprezentuje posiadane lub dostępne instancje/pule zasobów, ich identyfikację, stan oraz możliwość rezerwacji.

## Pytania rozpoznawcze

- Czy biznes odróżnia definicję produktu od egzemplarza lub partii?
- Czy zasób może być indywidualny, pulowy lub czasowy?
- Czy potrzebujemy blokady, rezerwacji albo listy oczekujących?
- Czy stan magazynowy jest Source of Truth dla dostępności, czy tylko jednym z wejść?

## Powiązania

[[Product]], [[Availability]], [[Waitlist]], [[Concurrency and Stale State]].
