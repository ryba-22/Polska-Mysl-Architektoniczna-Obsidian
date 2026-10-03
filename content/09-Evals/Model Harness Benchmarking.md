---
id: PMA-EVAL-MODEL-HARNESS-001
type: eval
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ai","evals","model","harness","cost","benchmark"]
source_ids: ["TENXDEVS-EMAIL-2026-08-19","AI-THAT-WORKS"]
---

# Model Harness Benchmarking

Modelu nie oceniaj wyłącznie przez cenę tokena ani publiczny leaderboard. Mierz wynik w swoim workflow i harnessie.

## Minimalny zestaw metryk

- task success / pass rate;
- stabilność między próbami;
- koszt całego przebiegu;
- czas do poprawnego wyniku;
- liczba interwencji/retry;
- strict regression pass dla zadań rozwijających istniejący codebase.

## Cost per Successful Task

Koszt poprawnego zadania = łączny koszt prób / liczba poprawnie zakończonych zadań.

Tani model z niską skutecznością może być droższy operacyjnie niż droższy model z wysoką skutecznością.

## Harness effect

Ten sam model może zachowywać się inaczej zależnie od harnessu, narzędzi, skilli i struktury planu. Benchmarkuj kombinację model + harness + workflow.

## PEOS

Dobre design/planning może obniżyć klasę modelu potrzebną do execution. Porównania muszą używać tej samej zamrożonej sekwencji zadań i budżetu.
