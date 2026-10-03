---
id: PMA-AI-STATE-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ai","agents","state","resumability"]
source_ids: ["AI-THAT-WORKS","DOMAIN-DRIVERS-DD-AI"]
---

# Structured Agent State

Długotrwały workflow nie powinien polegać wyłącznie na historii rozmowy.

## Minimalny stan

workflow id, goal, current stage, completed stages, evidence refs, decisions, assumptions, open questions, gates, artifacts, verification status i next action.

## Właściwości

- resumability;
- retry;
- auditability;
- możliwość forkingu;
- deterministyczne przekazanie pracy innemu agentowi.

## Zasada

Context window jest pamięcią roboczą, nie systemem zapisu procesu.
