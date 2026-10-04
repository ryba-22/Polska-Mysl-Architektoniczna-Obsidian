---
id: PMA-H-FOUR-MODEL-LEVELS-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: candidate
peos_usable: true
tags: ["ddd","modeling","capability","operations","policy","decision-support"]
source_ids: ["BOTTEGA-DDD-CATALOG"]
---

# Four Model Levels

Jedną domenę można oglądać na czterech poziomach odpowiedzialności:

1. **Capability** — jaka zdolność biznesowa istnieje i jaki rezultat potrafi dostarczyć.
2. **Operations** — jakie działania realizują tę zdolność i jak przebiega praca.
3. **Policy** — według jakich zmiennych reguł podejmowane są decyzje.
4. **Decision Support** — jakie obserwacje, miary, prognozy lub rekomendacje wspierają decyzje.

## Po co ten podział

Pomaga wykryć modele, w których bieżące wykonanie procesu, konfigurowalne zasady i analityka zostały sklejone tylko dlatego, że dotyczą tego samego rzeczownika.

## Kontrasty

**capability ≠ moduł**
**operations ≠ application layer**
**policy ≠ tabela konfiguracyjna**
**decision support ≠ read model**

To poziomy analizy odpowiedzialności. Ich odwzorowanie na komponenty techniczne jest osobną decyzją.

## Pytania

- co musi pozostać stabilne, nawet gdy proces wykonania się zmieni?
- które reguły są polityką i powinny ewoluować niezależnie?
- czy wynik analityczny jest źródłem prawdy, czy tylko wsparciem decyzji?
- czy capability ma jednego ownera i jedno znaczenie?

Powiązania: [[Capability vs Product]], [[Architecture Abstraction Ladder]], [[Architecture Drivers]].
