---
id: PMA-H-DEEP-MODEL-QUALITY-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["ddd","deep-model","model-quality","evaluation"]
source_ids: ["DOMAIN-DRIVERS-COURSE","EVANS-DDD","DEVSTYLE-DDD-EMAIL-CORPUS"]
---

# Deep Model Quality

Deep Model nie jest modelem z dużą liczbą klas. Powinien lepiej wyjaśniać problem i redukować przypadkową złożoność.

## Rubryka

Oceniaj model przez:
- explanatory power — czy wyjaśnia, dlaczego domena zachowuje się tak, a nie inaczej;
- compression — czy kilka pozornie osobnych reguł staje się jednym konceptem;
- simplicity — czy maleje liczba specjalnych przypadków;
- predictive power — czy model pomaga przewidzieć zachowanie nowego przypadku;
- language fit — czy pojęcia pasują do języka ekspertów;
- change locality — czy prawdopodobna zmiana zostaje lokalna;
- autonomy — czy model może podejmować własne decyzje na podstawie swojej wiedzy;
- counterexample resistance — czy trudne przykłady rozwijają model zamiast mnożyć wyjątki.

## Zasada

Porównuj modele na tych samych scenariuszach i kontrprzykładach. "Bardziej elegancki kod" nie jest samodzielnym kryterium jakości modelu.
