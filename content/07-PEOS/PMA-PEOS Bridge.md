---
id: PMA-PEOS-BRIDGE-001
type: integration
publication_status: public
knowledge_status: peos-decision
lifecycle: active
peos_usable: true
tags: ["peos","pma","integration","knowledge"]
source_ids: []
---

# PMA-PEOS Bridge

PMA jest knowledge plane. PEOS jest execution plane.

## Kontrakt

PEOS nie czyta całego vaulta. Konsumuje tylko publiczny, wygenerowany registry z dist/peos/.

Registry zawiera:
- concepts;
- heuristics;
- software archetypes;
- failure patterns;
- case studies;
- AI engineering notes;
- relacje i source IDs.

## Runtime retrieval

Przykład:
stage = domain-design
problem_class = resource-contention

Router może pobrać:
- Unit of Change;
- Consistency Boundary;
- Availability;
- Concurrency and Stale State;
- Transactional Outbox Atomicity, jeśli pojawia się integracja.

## Bezpieczeństwo

private/ nigdy nie jest częścią maszynowego registry. Lokalny PEOS może odwołać się do prywatnego researchu tylko w jawnie uruchomionym research workflow, nigdy przez publiczny artifact.

## Versioning

PEOS powinien rejestrować SHA repo PMA użyty w danym runie, aby decyzje były reprodukowalne.
