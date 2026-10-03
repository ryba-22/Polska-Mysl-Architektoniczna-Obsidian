---
id: PMA-H-DDD-LANGUAGE-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: verified
peos_usable: true
tags: ["ddd","ubiquitous-language","bounded-context"]
source_ids: ["DDD-BY-EXAMPLES-LIBRARY","DOMAIN-DRIVERS-COURSE"]
---

# Linguistic Boundary

Zmiana znaczenia słowa jest jednym z najsilniejszych sygnałów kandydatury na granicę modelu.

## Pytania

- czy ten sam rzeczownik znaczy coś innego dla dwóch procesów?
- czy koncept ma inny lifecycle i inne reguły?
- czy po pivotal event ludzie zaczynają używać innego słownictwa?
- czy jeden zespół stale tłumaczy pojęcia drugiemu?

## Przykład strukturalny

Book w katalogu może oznaczać opis pozycji bibliograficznej, a Book w lending konkretny zasób podlegający regułom dostępności. Wspólna nazwa nie oznacza wspólnego modelu.

## Anti-signal

Różne słowa nie oznaczają automatycznie różnych kontekstów. Najpierw sprawdź znaczenie, reguły i ownership.
