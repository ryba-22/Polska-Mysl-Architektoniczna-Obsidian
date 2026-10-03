---
id: PMA-ARCHETYPE-PRICING-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["pricing","calculation","rules"]
source_ids: ["SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA","BSLOTA"]
---

# Pricing

Pricing modeluje sposób wyznaczania wartości pieniężnej na podstawie parametrów, reguł i kontekstu.

## Recognition questions

- czy cena jest funkcją zestawu parametrów?
- czy istnieją niezależne strategie, progi lub funkcje schodkowe?
- czy reguły ceny mają zmieniać się częściej niż lifecycle produktu?
- czy pricing powinien być wyjaśnialny jako breakdown?

## Heurystyka

Jeżeli obliczenie nie zmienia Source of Truth, sama kalkulacja należy zwykle do Transformation/Calculation. Nie umieszczaj jej w agregacie tylko dlatego, że wynik później wpływa na komendę.

## Sygnał deep model

Banking, logistics i telecom mogą używać podobnej struktury Pricing mimo zupełnie innego języka domenowego.
