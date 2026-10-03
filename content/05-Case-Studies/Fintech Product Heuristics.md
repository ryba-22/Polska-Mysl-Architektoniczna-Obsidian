---
id: PMA-CASE-FINTECH-PRODUCT-001
type: case-study
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["fintech","product-engineering","explainability","sandbox","policy"]
source_ids: ["FINTECH-POLAND-ECOSYSTEM","MONETEO-FINTECH-RANKING-2026"]
---

# Fintech Product Heuristics

## Teza

Najbardziej przenośna lekcja z fintechu nie brzmi „kopiuj funkcje bankowe”, tylko: projektuj wokół decyzji użytkownika, jawnego kosztu, wyjaśnialnego stanu i kontrolowanego ryzyka.

## Wzorce przenośne

### Capability-first
Najpierw ustal job użytkownika i granicę capability. Użyj [[Capability Card]].

### Explainable state
Wartość, saldo lub status powinny mieć provenance. Użyj [[Explainable State and Provenance]].

### Correction instead of historical mutation
Jeżeli fakt został użyty do decyzji lub rozliczenia, preferuj [[Corrections Over Historical Mutation]].

### Actionable state
Status powinien prowadzić do następnej decyzji, nie kończyć się etykietą. Użyj [[Actionable State]].

### Architecture sandbox
Ryzykowne zmiany sprawdzaj przed migracją przez [[Architecture Sandbox]].

### Policy as explicit artifact
Reguły wpływające na decyzję powinny być jawne, wersjonowane i mieć ownera. Użyj [[Policy as Domain Artifact]].

## Antywzorzec

Nie przenoś do innej domeny powierzchniowych elementów fintechu tylko dlatego, że wyglądają dojrzale: dashboardów, kart, wykresów, nazw stanów czy technologii.

Pytanie brzmi: **jaki problem i jaki mechanizm stoją za tym rozwiązaniem?**

## Powiązania

- [[PMA Mental Loop]]
- [[Purpose Before Structure]]
- [[Feedback and Metrics Loop]]
