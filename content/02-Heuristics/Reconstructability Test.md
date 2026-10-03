---
id: PMA-H-RECONSTRUCT-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["projection","presentation","source-of-truth","problem-classification"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE"]
---

# Reconstructability Test

## Teza

Jednym z najszybszych sposobów odróżnienia modelu prezentacji/projekcji od modelu będącego źródłem prawdy jest pytanie o **odtwarzalność informacji**.

## Test

> Gdyby skasować ten widok, raport, indeks lub read model i odbudować go z innych autorytatywnych modeli, czy utracilibyśmy jakąkolwiek informację biznesową?

Jeżeli **nie**, prawdopodobnie mamy projekcję, cache, indeks lub model prezentacyjny.

Jeżeli **tak**, trzeba ponownie sprawdzić, czy nie przypisaliśmy odpowiedzialności za stan biznesowy do elementu traktowanego jako prezentacja.

## Dalsze pytania

- Które źródła są source of truth?
- Czy projekcja modyfikuje którekolwiek źródło?
- Co jeśli źródła dotrą w innej kolejności?
- Czy projekcja może być chwilowo niekompletna?
- Czy odtworzenie wymaga historii zdarzeń, snapshotu czy aktualnego stanu?

## Powiązania

- [[Problem Classification]]
- [[Consistency Boundary]]
- [[Recovery and Human Escalation]]
