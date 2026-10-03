---
id: PMA-H-ARCH-CODE-GAP-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["architecture","boundaries","verification","ci"]
source_ids: ["DDD-BY-EXAMPLES-LIBRARY","DOMAIN-DRIVERS-DD-JAVA","PILLOPL"]
---

# Architecture Code Gap

Diagram granic, którego kod nie potrafi egzekwować, jest tylko deklaracją.

## Heurystyka

Dla każdej istotnej granicy ustal:
- publiczne API;
- dozwolone zależności;
- zabronione zależności;
- właściciela danych;
- publikowane i konsumowane komunikaty.

Następnie skompiluj decyzję do automatycznej kontroli zależnej od stacku.

## Przykładowe mechanizmy

ArchUnit, Nx module boundaries, dependency-cruiser, ESLint boundaries, NetArchTest lub własne testy AST.

## PEOS

Context Map powinien mieć executable counterpart w CI.
