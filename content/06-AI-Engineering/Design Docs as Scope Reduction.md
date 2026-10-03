---
id: PMA-AI-DESIGN-DOCS-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["ai","design-doc","planning","execution"]
source_ids: ["AI-THAT-WORKS"]
---

# Design Docs as Scope Reduction

Dobry design doc redukuje przestrzeń decyzji podczas implementacji.

## Heurystyka

Dla złożonej zmiany najpierw zamroź:
- problem i oczekiwany stan końcowy;
- invariants;
- kontrakty;
- failure modes;
- decyzje i trade-offs;
- plan weryfikacji.

Następnie podziel implementację na małe części, z których każda ma jednoznaczny DoD.

## PEOS

Design artifact jest wejściem do execution, nie dekoracją po implementacji.
