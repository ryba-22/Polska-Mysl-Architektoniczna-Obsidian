---
id: PMA-AI-FACTORY-LAYERS-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["ai","software-factory","agents","orchestration"]
source_ids: ["AI-THAT-WORKS"]
---

# Software Factory Layers

Agentic software factory można rozdzielić na cztery niezależne warstwy:

1. compute — gdzie agent działa;
2. development environment — czego potrzebuje do budowania i testowania;
3. harness — interfejs modelu, narzędzia i lifecycle;
4. orchestration — routing pracy, stan, feedback i sterowanie runami.

## Zasada

Nie wiąż PEOS z jednym harness-em. Wiedza, workflow i verifiers powinny pozostać przenośne między narzędziami wykonawczymi.
