---
id: PMA-ARCHETYPE-RULES-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["software-archetypes","rules","scoring","decision"]
source_ids: ["ARCHETYPY-OPROGRAMOWANIA"]
---

# Rules and Scoring

Archetyp Rules and Scoring pojawia się, gdy wynik jest składany z wielu zmiennych warunków, predykatów, wag lub modyfikatorów.

## Pytania rozpoznawcze

- Czy reguły często zmieniają się niezależnie od głównego modelu?
- Czy wynik powinien być wyjaśnialny jako suma wkładów lub decyzji?
- Czy potrzebne są AND/OR/NOT, progi, przedziały lub fuzzy scoring?
- Czy konfiguracja reguł ma być dynamiczna?

## Ryzyko

Nie zamieniaj każdej reguły domenowej w generic rule engine. Archetyp jest właściwy dopiero, gdy zmienność reguł jest sama w sobie częścią problemu.
