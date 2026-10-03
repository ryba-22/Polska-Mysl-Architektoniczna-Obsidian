---
id: PMA-H-CORRECTIONS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["correction","audit","history","finance","temporal"]
source_ids: ["FINTECH-POLAND-ECOSYSTEM"]
---

# Corrections Over Historical Mutation

## Teza

Jeżeli historyczny fakt ma znaczenie audytowe, finansowe, prawne lub procesowe, korekta jest zwykle bezpieczniejszym modelem niż nadpisanie przeszłości.

## Pytania

- Czy zmieniamy fakt historyczny, czy tworzymy nowy fakt korygujący?
- Czy po zmianie potrafimy wyjaśnić wcześniejszy stan?
- Czy użytkownik zobaczy różnicę między błędem pierwotnym i korektą?
- Czy korekta zachowuje związek z obiektem, który koryguje?
- Czy można odtworzyć stan as-of przed korektą?

## Preferowany model

FactRecorded → CorrectionRecorded → projekcja bieżącego stanu

zamiast nadpisywania historycznego rekordu.

## Granica stosowalności

Nie każdy edytowalny opis wymaga append-only history. Heurystyka jest szczególnie cenna tam, gdzie wcześniejszy stan został wykorzystany do rozliczenia, decyzji, komunikacji lub audytu.

## Powiązania

- [[Temporal Scale and Volatility Lens]]
- [[Explainable State and Provenance]]
- [[Behavior Preservation Contract]]
