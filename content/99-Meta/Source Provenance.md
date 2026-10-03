---
id: PMA-META-PROVENANCE-001
type: governance
publication_status: public
knowledge_status: peos-decision
lifecycle: active
peos_usable: true
tags: ["provenance","evidence","governance"]
source_ids: []
---

# Pochodzenie wiedzy

Każda istotna notatka PMA powinna rozróżniać, czy dana treść jest:
- source-derived — bezpośrednio wyprowadzona ze źródła;
- synthesis — autorską syntezą wielu źródeł;
- inference — wnioskiem wymagającym ostrożności;
- peos-decision — decyzją operacyjną Product Engineering OS;
- validated — heurystyką lub zasadą z dodatkowym potwierdzeniem w evalach albo praktyce.

Pole source_ids wskazuje rekordy z source-registry/sources.json.

PMA nie traktuje pochodzenia jako przypisu dekoracyjnego. Provenance decyduje, jak mocno AI Brain może oprzeć na danej notatce decyzję.
