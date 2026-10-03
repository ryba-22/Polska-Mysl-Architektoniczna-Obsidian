---
id: PMA-H-MODEL-ALTERNATIVES-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: verified
peos_usable: true
tags: ["ddd","modeling","alternatives","decision"]
source_ids: ["DEVSTYLE-DDD-EMAIL-CORPUS","DOMAIN-DRIVERS-COURSE"]
---

# Model Alternatives

Nie zamykaj modelowania na pierwszej sensownej reprezentacji problemu.

## Heurystyka

Dla decyzji modelarskiej o dużym koszcie zmiany wygeneruj kilka realnie różnych modeli. Materiał Domain Drivers z 2023-12-07 wskazuje praktykę tworzenia czterech alternatywnych modeli dla tego samego problemu.

Porównuj je przez:
- invariants i consistency;
- złożoność scenariuszy;
- change propagation;
- skalowalność;
- język;
- koszt implementacji;
- zachowanie pod przyszłą zmianą.

## Cel

Alternatywy służą ujawnieniu ukrytych założeń. Liczba cztery jest praktyką ze źródła, nie uniwersalnym wymogiem PEOS.
