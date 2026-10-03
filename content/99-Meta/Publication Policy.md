---
id: PMA-META-PUBLICATION-001
type: governance
publication_status: public
knowledge_status: peos-decision
lifecycle: active
peos_usable: true
tags: ["governance","licensing","publication"]
source_ids: []
---

# Polityka publikacji PMA

## Zasada nadrzędna

PMA publikuje wiedzę, nie kopie źródeł.

Raw source pozostaje lokalnie w private/. GitHub otrzymuje tylko jawnie publiczne syntezy, metadane źródłowe, własne diagramy, własne heurystyki i linki do materiałów pierwotnych.

## Public by explicit opt-in

Notatka jest publikowalna tylko wtedy, gdy ma publication_status: public.

Brak statusu, status private albo review oznacza brak publikacji.

## Co pozostaje lokalnie

- pełne transkrypcje i napisy;
- screenshots i slajdy kursów;
- PDF-y i książki;
- długie cytaty;
- kopie repozytoriów do analizy;
- close reading i research dumps;
- materiały o niejasnym statusie licencyjnym.

## Co może być publiczne

- autorskie syntezy;
- własne heurystyki;
- własne modele i diagramy;
- bibliografia i source registry;
- porównania i wnioski;
- PEOS decision records;
- krótkie cytaty tylko wtedy, gdy są naprawdę potrzebne i prawidłowo przypisane.

## Bramka publikacji

CI musi odrzucić:
1. pliki śledzone pod private/ lub assets-private/;
2. notatki publiczne bez publication_status: public;
3. sekrety i credentiale;
4. niedozwolone raw attachments w warstwie publicznej;
5. niespójny maszynowy registry dla PEOS.

[[PMA-PEOS Bridge]] korzysta wyłącznie z warstwy publicznej.
