---
id: PMA-H-EXPLAINABLE-STATE-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["explainability","provenance","state","finance","read-model"]
source_ids: ["FINTECH-POLAND-ECOSYSTEM","MONETEO-FINTECH-RANKING-2026"]
---

# Explainable State and Provenance

## Teza

W systemach, w których użytkownik podejmuje decyzję na podstawie liczby lub statusu, sam wynik jest niewystarczający.

**Stan powinien być wyjaśnialny przez fakty, które go utworzyły.**

## Kontrakt

Dla każdej istotnej wartości lub statusu system powinien potrafić odpowiedzieć:

- z jakich faktów wynik powstał?
- według jakiej reguły został policzony?
- na jaki moment obowiązuje?
- które źródło jest source of truth?
- co zmieni wynik?
- czy użytkownik może przejść od agregatu do faktów źródłowych?

## Przykład ogólny

Zamiast samego „saldo = 120” preferuj model: należności 720 minus przypisane wpłaty 480 minus korekty 120 = 120 do zapłaty.

Każdy składnik ma własne provenance i drill-down.

## Invariant

Read model może upraszczać prezentację, ale nie może ukrywać semantyki w sposób uniemożliwiający odtworzenie wyniku.

## Powiązania

- [[Reconstructability Test]]
- [[Feedback and Metrics Loop]]
