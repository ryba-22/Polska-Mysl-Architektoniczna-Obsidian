---
id: PMA-ARCHETYPE-WAITLIST-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["waitlist","queue","selection-policy"]
source_ids: ["SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA"]
---

# Waitlist

Waitlist przechowuje kandydatów oczekujących na zasób i rozdziela problem oczekiwania od polityki wyboru.

## Recognition questions

- czy popyt przewyższa capacity?
- czy kandydat może czekać bez rezerwacji konkretnego zasobu?
- czy wybór jest FIFO, priority, quota albo criteria-based?
- czy polityka selekcji może się zmieniać niezależnie od kolejki?

## Heurystyka

Nie zaszywaj polityki wyboru w strukturze danych kolejki, jeśli biznes może ją zmieniać. Oddziel membership od selection policy.

Powiązania: [[Availability]], Reservation, Rules.
