---
id: PMA-H-MODELING-WHIRLPOOL-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: verified
peos_usable: true
tags: ["ddd","modeling","knowledge-crunching","feedback","executable-specification"]
source_ids: ["BOTTEGA-DDD-ARTICLES","BOTTEGA-DDD-MATERIALS"]
---

# Modeling Whirlpool

Modeling Whirlpool opisuje modelowanie jako **iteracyjne dostrajanie języka, reguł, przykładów i kodu**, a nie liniowy hand-off "analiza → dokument → implementacja".

## Iteracja ≠ inkrement

Inkrementacja dzieli rozwiązanie na porcje. Iteracja wraca do tego samego problemu z nową wiedzą i pozwala zmienić wcześniejszy model.

Dlatego wynik sesji modelowania nie jest kontraktem zamrożonym raz na zawsze. Jest hipotezą, którą kolejne scenariusze mogą poprawić albo obalić.

## Pętla

rozmowa z ekspertem
→ przykład / scenariusz
→ słownictwo i reguły
→ model
→ implementacja / executable specification
→ feedback
→ kolejna wersja modelu.

## Konsekwencja

Dokumentacja ma największą wartość wtedy, gdy utrzymuje semantyczne sprzężenie zwrotne z działającym systemem. Specification by Example i scenariusze akceptacyjne mogą pełnić rolę wykonywalnej dokumentacji, ale tylko jeśli opisują zachowanie ważne biznesowo, a nie strukturę implementacji.

Powiązania: [[DDD jako proces decyzyjny]], [[Dynamic Validation]], [[Scenario Before Aggregate]], [[Behavior Preservation Contract]].
