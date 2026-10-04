---
id: PMA-H-BACKWARD-NARRATION-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","event-storming","model-discovery","temporal-reasoning"]
source_ids: ["DOMAIN-DRIVERS-COURSE"]
---

# Backward Narration

## Teza

Aby odkryć brakujący model, policy albo event, opowiadaj proces od ważnej
operacji **wstecz**.

Nie pytaj tylko:

> co wydarzy się potem?

Pytaj:

> co musiało już stać się prawdą, żeby ta operacja była legalnie możliwa?

## Problem, który rozwiązuje

W analizie strategicznej łatwo przejść od:

obiekt istnieje

bezpośrednio do:

obiekt można użyć

i zgubić decyzję, która zmieniła jego znaczenie, kwalifikowalność lub zestaw
dozwolonych operacji.

To właśnie w tej luce często ukrywa się:

- policy;
- lifecycle transition;
- [[Pivotal Event]];
- mapping model;
- brakujące źródło prawdy.

## Procedura

Dla ważnej komendy lub zdarzenia:

1. Nazwij fakt końcowy.
2. Zapytaj: co musiało być prawdą chwilę wcześniej?
3. Dla każdego warunku zapytaj ponownie: skąd system to wie?
4. Oddziel:
   - fakt;
   - decyzję;
   - policy;
   - projekcję;
   - zdarzenie zmieniające stan.
5. Zatrzymaj się, gdy dotrzesz do jawnego source of truth albo znanego
   pivotal event.

## Przykład

Resource Allocated

← resource był allocatable
← powstały jednostki dostępności
← właściwości zasobu zostały zmapowane na availability units
← resource został zarejestrowany

Jeżeli krok „właściwości zostały zmapowane” nie ma ownera ani nazwy, mamy
hotspot modelowania.

## Rozróżnienie

Backward narration nie jest odtwarzaniem implementacyjnego call stacka.

Interesuje nas:

**co musiało stać się prawdą biznesowo**

a nie:

**jakie funkcje wywołał kod**.

## Falsyfikacja

Nie każda luka oznacza nowy model. Może to być:

- derived fact;
- zwykła walidacja;
- techniczna translacja;
- read-model composition;
- reguła należąca już do istniejącego modelu.

Nowy model jest hipotezą, którą trzeba sprawdzić przez [[Model Alternatives]].

## Powiązania

- [[Pivotal Event]]
- [[Mapping Model Discovery]]
- [[Main Question]]
- [[Event Command Query]]
- [[Behavior Before Nouns]]
