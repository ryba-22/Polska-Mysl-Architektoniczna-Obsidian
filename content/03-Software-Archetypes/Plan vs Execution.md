---
id: PMA-ARCHETYPE-PLANEXEC-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["plan","execution","delta","simulation","tolerance"]
source_ids: ["ARCHETYPY-OPROGRAMOWANIA"]
---

# Plan vs Execution

Archetyp porównuje plan z rzeczywistym wykonaniem i modeluje deltę, tolerancję oraz działania korygujące.

## Recognition questions

- czy istnieje oczekiwany plan i osobny strumień wykonania?
- czy odchylenie ma znaczenie tylko powyżej tolerancji?
- czy matching plan↔execution jest nietrywialny?
- czy system ma symulować konsekwencje lub modyfikować przyszły plan?

## Elementy

plan, actual execution, matching, delta, tolerance, statistics, modification policy, simulation.

## Heurystyka

Nie próbuj modelować wykonania jako mutacji planu, jeśli biznes potrzebuje widzieć różnicę między tym, co miało się wydarzyć, a tym, co się wydarzyło.
