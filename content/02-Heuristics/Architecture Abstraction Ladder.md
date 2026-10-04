---
id: PMA-H-ARCH-ABSTRACTION-LADDER-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["architecture","ddd","bounded-context","module","abstraction","decision"]
source_ids: ["BOTTEGA-DDD-CATALOG"]
---

# Architecture Abstraction Ladder

Decyzje architektoniczne łatwo psują się, gdy problem i rozwiązanie znajdują się na różnych poziomach abstrakcji.

Przydatna drabina:

**business process → capability → Bounded Context → module → component → class**

## Sens

Każdy poziom odpowiada na inne pytanie. Proces opisuje przepływ wartości. Capability opisuje zdolność. Bounded Context chroni spójność modelu i języka. Moduł organizuje odpowiedzialność w systemie. Komponent i klasa są już bliżej implementacji.

## Ważne rozróżnienie

**Bounded Context ≠ module**

Jeden Bounded Context może zawierać kilka modułów, a decyzja o deployment unit jest jeszcze innym wymiarem. Nie wolno wywnioskować granicy domenowej tylko z katalogów w repozytorium.

## Heurystyka

Gdy dyskusja utknie, sprawdź:
- na jakim poziomie znajduje się obserwowany problem;
- na jakim poziomie próbujemy go naprawić;
- czy decyzja niższego poziomu nie maskuje błędu wyższego poziomu.

code smell → może być symptomem → złej modularizacji → może być symptomem → błędnej analizy granic

Powiązania: [[DDD jako proces decyzyjny]], [[Architecture Drivers]], [[Linguistic Boundary]], [[Capability vs Product]].
