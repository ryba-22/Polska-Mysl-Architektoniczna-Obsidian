---
id: PMA-AI-FACTORY-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ai","software-factory","agents","feedback-loop"]
source_ids: ["AI-THAT-WORKS"]
---

# Software Factory

Agentic software factory nie jest jednym agentem. Składa się z warstw: compute, dev environment, harness i orchestration.

## Najważniejsza pętla

agent wykonuje zadanie
→ trace runu
→ drugi agent analizuje failure
→ findings są deduplikowane
→ issue
→ human gate
→ implementation/PR
→ verifiers
→ wynik wraca do procesu.

## Heurystyka

Nie optymalizuj wyłącznie orchestratora. Największe ograniczenia często leżą w dev environment, dostępności zależności, verifierach i jakości wejściowego designu.

## Human role

Człowiek powinien decydować, co liczy się jako poprawny wynik i jaką zmianę procesu zaakceptować. Kod może być generowany automatycznie, odpowiedzialność za decyzję nie.
