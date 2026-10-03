---
id: PMA-H-ALGORITHM-RECOGNITION-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["algorithm","structural-recognition","deep-model","ddd"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA"]
---

# Algorithm Recognition

Język biznesowy może ukrywać klasyczny problem informatyczny. Zanim rozbudujesz model domenowy, sprawdź strukturę problemu.

## Sygnały

- zależności kroków → graf i porządek topologiczny;
- wybór najlepszego zestawu przy ograniczeniach → optymalizacja / knapsack;
- dopasowanie kandydatów do zasobów → matching / assignment;
- konfiguracja zgodna z wieloma warunkami → SAT / constraint solving;
- ścieżki i wpływ → analiza grafowa;
- harmonogramowanie zależnych prac → scheduling.

## Zasada

Rozpoznany algorytm nie zastępuje języka domenowego. Jest mechanizmem rozwiązania ukrytym pod modelem biznesowym.
