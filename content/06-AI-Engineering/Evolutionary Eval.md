---
id: PMA-AI-EVAL-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ai","evals","evolution","regression"]
source_ids: ["AI-THAT-WORKS"]
---

# Evolutionary Eval

Jednorazowy pass/fail nie mierzy zdolności agenta do utrzymywania systemu przez kolejne zmiany.

## Model

S1 zostaje zaimplementowane.
S2 jest implementowane na kodzie po S1 i musi zachować S1.
S3 jest implementowane na kodzie po S2 i musi zachować S1 oraz S2.

Mierzymy strict pass, a nie tylko isolated pass.

## Dlaczego

Zła struktura danych albo zły boundary mogą przejść wszystkie aktualne testy, ale zwiększać koszt kolejnych zmian. Eval musi obserwować akumulację długu w czasie.
