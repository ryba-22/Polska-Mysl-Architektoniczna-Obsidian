---
id: PMA-ARCHETYPE-CONFIGURATOR-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["configuration","constraints","sat","algorithm"]
source_ids: ["SOFTWARE-ARCHETYPES"]
---

# Configurator

Configurator pojawia się, gdy użytkownik wybiera kombinację opcji, a reguły określają, które zestawy są dopuszczalne i czego brakuje do poprawnej konfiguracji.

## Recognition questions

- czy reguły dotyczą kombinacji cech, a nie pojedynczej cechy?
- czy trzeba odpowiedzieć czy konfiguracja jest satisfiable?
- czy system ma wskazać brakujące opcje lub konflikt?
- czy liczba kombinacji rośnie wykładniczo?

## Heurystyka

Jeżeli opis biznesowy ukrywa problem satisfiability, rozważ formalizację constraints i znany algorytm zamiast kaskady if/else.

To przykład połączenia [[Pattern vs Archetype vs Algorithm|archetypu i algorytmu]].
