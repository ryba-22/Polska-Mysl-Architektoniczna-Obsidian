---
id: PMA-AI-BACKPRESSURE-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["ai","agents","verification","backpressure"]
source_ids: ["AI-THAT-WORKS"]
---

# Agentic Backpressure

Agent powinien dostawać możliwie szybkie, tanie i deterministyczne sygnały, które ograniczają dryf zanim błąd urośnie.

## Przykłady

typecheck, lint, unit tests, architecture tests, schema validation, contract tests, mutation tests, static analyzers.

## Zasada

Im krótsza pętla feedbacku, tym mniejszy koszt błędnej trajektorii agenta.

Nie wszystko da się zweryfikować automatycznie. To, czego nie obejmują verifiers, pozostaje zakresem review człowieka.
