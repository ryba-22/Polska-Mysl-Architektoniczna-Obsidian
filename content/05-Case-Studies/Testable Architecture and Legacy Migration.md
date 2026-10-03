---
id: PMA-CASE-TESTABLE-ARCH-001
type: case-study
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["legacy","migration","architecture-tests","acl"]
source_ids: ["PILLOPL"]
---

# Testable Architecture and Legacy Migration

Z repozytoriów pilloPl wyłania się praktyczny model migracji legacy:

legacy
→ black-box behavioral characterization
→ desired boundary
→ anti-corruption layer
→ parallel model
→ reconciliation
→ feature switch
→ cut-over.

## Heurystyka

Przed refaktorem utrwal zachowanie obserwowalne. Inaczej nowy model może być elegantszy, ale semantycznie inny.

Architecture test powinien pilnować granicy, a reconciliation test sprawdzać zgodność danych podczas okresu przejściowego.
