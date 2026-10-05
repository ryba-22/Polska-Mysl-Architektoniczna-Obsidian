---
id: PMA-H-BOUNDARY-COUPLING-EVIDENCE-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["architecture","ddd","boundaries","coupling","connascence","ai","evidence"]
source_ids: ["DEVSTYLE-DOMAIN-DRIVERS-CONNASCENCE-DEMO-2026-10-05"]
---

# Boundary Coupling Evidence

## Teza

Granica modułu nie jest linią na diagramie. Jest zbiorem zależności, które tę granicę przekraczają.

Dlatego:

`module boundary ≠ model autonomy`

Osobne pakiety, fasada i jednokierunkowy graf importów mogą współistnieć z silnym couplingiem temporalnym, transakcyjnym, tożsamościowym albo spójnościowym. Jakość granicy warto oceniać przez rzeczywiste crossingi i ich konsekwencje, a nie tylko przez strukturę kodu.

## Problem, który rozwiązujemy

W strategicznym modelowaniu często potrafimy wskazać kandydacką granicę, ale trudniej odpowiedzieć:

- co faktycznie przez nią przechodzi;
- które zależności są przypadkowe, a które wynikają z rzeczywistego invariantu;
- czy dwa moduły są autonomiczne, czy tylko wyglądają na osobne;
- która alternatywna granica lepiej lokalizuje koszt zmiany i poprawność;
- jakie miejsca wymagają wspólnej transakcji, kolejności, identity albo synchronizacji.

Samo `A → B` w dependency graph jest zbyt ubogim opisem.

## Model analizy

Praktyczny przebieg:

```text
candidate boundary
    ↓
membership A/B
    ↓
source evidence
    ↓
ambiguous ownership/shared concepts
    ↓
human semantic gate
    ↓
inventory every crossing
    ↓
classify + locate + count
    ↓
strength / degree / cost
    ↓
Boundary Coupling Profile
    ↓
ranked offenders
    ↓
correctness risks
    ↓
compare alternative boundary
```

Najpierw trzeba ustalić ownership i znaczenie. Dopiero potem wolno liczyć.

## Crossing taxonomy użyta w analizowanym demo

W materiale pokazano praktyczną inwentaryzację obejmującą między innymi:

- **OP** — umowy operacyjne/API i semantyka rezultatów;
- **TY** — typy i przenoszona przez nie semantyka;
- **OR** — ordering, transaction protocol i wymagana kolejność;
- **IN** — invariant rozpięty pomiędzy stronami granicy;
- **WI** — wiring / injection;
- **CV** — konwencja bez pojedynczego nośnika;
- **ST** — współdzielony store/tabela;
- **SI** — współdzielona żywa instancja / mutable runtime state.

Brak wpisu w kategorii też jest evidence. Przykładowo brak shared table nie usuwa problemu, jeśli dwa osobne store'y muszą utrzymywać wspólny invariant.

## Strength, degree i cost

W demo koszt jednostki liczony jest jako:

```text
cost = strength_rank × log₂(1 + degree)
```

gdzie:

- `strength_rank` opisuje siłę rodzaju zależności;
- `degree` opisuje, jak szeroko dana zależność jest rozlana po systemie.

Zależności pogrupowano w pasma:

| pasmo | przykładowe rodzaje |
| --- | --- |
| static-weak | Name, Type |
| static-semantic | Meaning, Position, Algorithm |
| dynamic | Execution, Timing, Value, Identity |

To jest **heurystyczny model kosztu**, nie uniwersalna jednostka jakości architektury.

## Evidence z analizowanego przypadku

Demo analizuje granicę:

```text
Allocation → Availability
```

Strukturalnie granica wygląda relatywnie dobrze:
- zależność jest jednokierunkowa;
- istnieje `AvailabilityFacade`;
- nie ma wspólnej tabeli;
- nie ma współdzielonej mutable live instance;
- mapowanie części typów jest lokalizowane w mapperach.

Głębsza analiza wykrywa jednak 12 crossingów. Profil:

| pasmo | crossing count | total cost |
| --- | ---: | ---: |
| static-weak | 5 | 10.75 |
| static-semantic | 4 | 20.42 |
| dynamic | 3 | 29.51 |
| **total** | **12** | **60.68** |

Trzy dynamiczne crossingi odpowiadają za około 49% całego kosztu.

Najdroższe offenders:
1. jedna transakcja obejmująca oba moduły — 12.00;
2. register-before-use / sequencing — 9.51;
3. współdzielony UUID utrzymywany konwencją — 8.42;
4. cross-store invariant — 8.00.

Wniosek nie brzmi „wynik 60.68 oznacza złą architekturę”. Wniosek brzmi: **ciężar granicy leży głównie w coupling temporalnym i spójnościowym, mimo relatywnie czystej struktury statycznej.**

## Correctness ponad estetykę

W analizowanym przypadku obowiązuje relacja w rodzaju:

```text
Allocation exists
⇔
Availability resource is blocked
```

Stan leży w dwóch store'ach. Ścieżka `block` jest spinana transakcyjnie, ale przy `release` wynik operacji po stronie Availability może zostać zignorowany przez Allocation.

To tworzy możliwość:

```text
local release succeeds
remote/domain-side release fails
→ stores drift
```

Analiza coupling ujawnia więc potencjalny **correctness hole**, nie tylko „brzydką zależność”.

## Kluczowe rozróżnienia

- `module boundary ≠ model autonomy`
- `dependency graph ≠ boundary semantics`
- `shared representation ≠ shared meaning`
- `shared UUID ≠ shared ownership`
- `separate stores ≠ independent consistency`
- `clean facade ≠ weak temporal coupling`
- `score ≠ truth`
- `AI classification ≠ domain decision`

## Rola AI

LLM jest użyteczne jako wykonawca kosztownej analizy:

- code search;
- inventory crossingów;
- source references;
- proposal klasyfikacji;
- liczenie degree;
- wyliczenie kosztu;
- ranking offenders;
- wyszukiwanie potencjalnych correctness holes.

Nie powinno samodzielnie rozstrzygać:

- ownershipu pojęć;
- czy typ jest Shared Kernel;
- czy zależność odzwierciedla prawdziwy invariant biznesowy;
- czy coupling jest akceptowalny;
- czy granicę należy przesunąć.

Dlatego potrzebny jest **human semantic gate przed scoringiem**.

## Heurystyki

1. Najpierw zdefiniuj membership obu stron. Bez tego „crossing” nie ma stabilnego znaczenia.
2. Każdy crossing musi mieć source-ref do kodu, schematu, danych, runtime albo kontraktu.
3. Oddziel static coupling od temporal/consistency coupling.
4. Szukaj nie tylko importów, ale transakcji, kolejności, identity, wspólnych invariants, store'ów i live state.
5. Lokalizacja coupling jest równie ważna jak jego istnienie. Mapper/fasada mogą ograniczać blast radius bez usuwania zależności.
6. Najpierw ranking offenders, dopiero potem total score.
7. Wysoki koszt nie oznacza automatycznie „rozłącz”. Może wskazywać, że dwa elementy rzeczywiście współdzielą invariant i granica jest postawiona za wcześnie.
8. Porównuj głównie alternatywne modele w tym samym systemie albo before/after przy tej samej metodzie.
9. Nie porównuj surowych total scores pomiędzy przypadkowymi systemami.
10. Granica jest hipotezą. Pytanie brzmi: jaki scenariusz lub evidence ją obali?

## Boundary Evidence Card

Minimalny artefakt dla materialnej granicy:

```text
Boundary:
A → B

Ownership:
A = ...
B = ...

Evidence:
code / data / schema / runtime / docs / domain expert

Membership ambiguities:
...

Human gate:
what was accepted/excluded and why

Crossings:
OP / TY / OR / IN / WI / CV / ST / SI

Strongest dependencies:
...

Transaction coupling:
...

Temporal coupling:
...

Identity coupling:
...

Cross-boundary invariants:
...

Shared storage/state:
...

Correctness risks:
...

Boundary Coupling Profile:
static-weak     ...
static-semantic ...
dynamic         ...

Counter-hypothesis:
merge / redraw / translate / accept

Decision:
...

Falsifiers / revisit triggers:
...

Source refs:
...
```

## Kontrprzykłady i granice stosowalności

- Ranking strength jest modelem, nie prawem natury.
- Formuła kosztu też jest decyzją projektową.
- Frequency nie oznacza business criticality.
- Jednorazowy invariant może być ważniejszy od wielu prostych type dependencies.
- Kod może nie zawierać intencji, której źródłem jest umowa, polityka, proces lub wiedza domenowa.
- LLM może dobrze znaleźć pattern i źle zinterpretować jego znaczenie.
- Score bez jawnej klasyfikacji i evidence daje fałszywą precyzję.

## Powiązania

- [[Architecture Code Gap]]
- [[Model Alternatives]]
- [[Deep Model Quality]]
- [[Evidence Contract]]
- [[Unit of Change]]
- [[Reconstructability Test]]
- [[Architecture Drivers]]

## Źródła

- DevStyle / Domain Drivers, „Czy MÓJ MODEL jest lepszy niż Twój? AI jako arbiter jakości | Domain Drivers DEMO”, 2026-10-05, https://youtu.be/Bbk-M96Rghc
- Connascence jest w tym materiale użyte jako taksonomia analizy zależności; PMA traktuje przedstawione scoring i rankingi jako heurystyczny model do falsyfikacji, nie uniwersalną metrykę jakości.
