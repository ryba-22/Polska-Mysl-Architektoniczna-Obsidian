---
id: PMA-H-FEEDBACK-METRICS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["feedback","metrics","validation","learning","architecture"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03"]
---

# Feedback and Metrics Loop

## Teza

Modelu nie należy oceniać wyłącznie przez elegancję diagramu. Decyzja potrzebuje **miary jakości** oraz możliwie krótkiej pętli feedbacku.

Metryka nie zastępuje modelowania. Pozwala sprawdzić, czy model realizuje driver, dla którego został wybrany.

## Pytania przed decyzją

- Jaki rezultat ma się poprawić?
- Jaką metryką można go obserwować?
- Czy metryka mierzy cel, czy jedynie łatwo policzalny proxy?
- Jaka jest wartość bazowa?
- Jak szybko po zmianie otrzymamy feedback?

## Pytania po decyzji

- Czy wynik zmienił się w oczekiwanym kierunku?
- Czy powstał niezamierzony koszt gdzie indziej?
- Czy skróciliśmy czy wydłużyliśmy lead time i handoffy?
- Czy production evidence potwierdza nasze założenia?
- Czy należy ponownie otworzyć decyzję?

## Antywzorzec

„Mamy 100% coverage”, „mamy dużo commitów”, „mamy mikroserwisy” albo „mamy niskie latency” nie jest automatycznie dowodem dobrej architektury. Miarę trzeba połączyć z konkretnym celem i driverem.

## Powiązania

- [[PMA Mental Loop]]
- [[Architecture Drivers]]
- [[Socio-Technical Boundary]]
- [[Evolutionary Eval]]
