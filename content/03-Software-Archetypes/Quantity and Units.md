---
id: PMA-ARCHETYPE-QUANTITY-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["software-archetypes","quantity","units","value-object"]
source_ids: ["SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA"]
---

# Quantity and Units

Quantity oddziela wartość liczbową od jej jednostki i semantyki biznesowej.

## Heurystyka

Jeżeli 10 może oznaczać 10 PLN, 10 godzin, 10 sztuk albo 10 kg, sama liczba jest zbyt słabym typem.

## Korzyści

- wymuszenie zgodności jednostek;
- bezpieczne konwersje;
- mniej ukrytych konwencji;
- ograniczenie [[Connascence]] typu Meaning.
