# PMA — Operational Runbook

PMA is the reusable reasoning and synthesis layer for DDD, architecture, domain modeling, and product-engineering heuristics.

The model is a hypothesis. The repository should help test it, not make it sound authoritative.

## WHEN

Use PMA when:

- a software/domain problem needs to be understood before choosing a pattern or implementation;
- evidence from several sources needs reusable synthesis;
- competing models, architecture drivers, ownership, temporal semantics, or failure modes need to be compared;
- a reusable heuristic or distinction may be worth publishing.

Do not use PMA as the canonical home for raw books, project-specific decisions, or an archetype lookup table.

## INPUT

Bring:

- the problem or desired outcome;
- observable evidence from code, data, UI, APIs, documents, or domain experts;
- known constraints and architecture drivers;
- current assumptions and open questions;
- relevant PMA notes or upstream evidence when already known.

Separate at minimum:

`FACT ≠ HYPOTHESIS ≠ ASSUMPTION ≠ DECISION ≠ OPEN QUESTION`.

## FLOW

1. State the real problem and outcome; distinguish the problem from its symptoms.
2. Gather evidence and mark what is observed versus inferred.
3. Identify the main question, pivotal behavior, ownership, and source-of-truth boundaries.
4. Generate at least one competing model when the decision is material.
5. Test models against invariants, temporal semantics, architecture drivers, coupling, failure modes, and cost of change.
6. Stress them with scenarios, counterexamples, retries, recovery, and expected future change.
7. Choose the smallest justified model or reversible experiment; record why alternatives lost.
8. Define falsifiers, verification evidence, and the condition that should reopen the decision.

Use `content/00-Start/Mapa PMA.md` and the linked deep notes when a step needs more depth.

## OUTPUT

A useful PMA result should contain:

- the problem/outcome;
- evidence and uncertainty classification;
- important distinctions and drivers;
- candidate models or hypotheses;
- chosen model/decision and rejected alternatives;
- consequences and failure modes;
- verification/falsification criteria;
- reusable synthesis only when the insight survives the specific case.

## EVIDENCE

A conclusion is supported when:

- claims retain provenance or a traceable reasoning path;
- observations are not silently promoted into universal rules;
- important alternatives and disconfirming evidence were considered;
- the decision can be connected to scenarios, constraints, or project evidence;
- publication boundaries are respected.

Run `make validate` for repository-level publication and link checks.

## STOP

Stop when additional analysis is unlikely to change the decision, or when the remaining uncertainty is better resolved by a concrete experiment or production evidence.

Do not add abstraction merely because another pattern can be named.

## HANDOFF

- recurring conceptual/domain ambiguity → **Domain Archetype Atlas**;
- repeatable product-engineering workflow or gate → **Product Engineering OS**;
- book-level evidence → **Book Knowledge Corpus**;
- UI/UX evidence or reusable interaction model → **UI/UX Knowledge Corpus**;
- project-specific decision, ADR/UDR, tests, or implementation → **project repository**;
- reusable project learning → return to PMA only after provenance and scope review.
