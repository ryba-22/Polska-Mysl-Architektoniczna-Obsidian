---
id: PMA-H-MAPPING-MODEL-DISCOVERY-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","model-discovery","mapping","boundaries","strategic-design"]
source_ids: ["DOMAIN-DRIVERS-COURSE"]
---

# Mapping Model Discovery

## Teza

Jeżeli ważne zachowanie potrzebuje faktów z dwóch dobrze wydzielonych modeli,
a żaden z nich nie powinien przejąć całej odpowiedzialności, być może brakuje
modelu opisującego **biznesowe mapowanie między nimi**.

Nie zaczynaj od pytania:

> do którego modułu dopisać tę funkcję?

Najpierw zapytaj:

> jaka decyzja łączy te dwa modele i kto jest jej właścicielem?

## Sens prostym językiem

Dwa modele mogą być poprawne osobno, ale między nimi może brakować pojęcia,
które wyjaśnia, jak jedno staje się znaczące dla drugiego.

Przykład:

- Resource wie, jakie właściwości ma zasób;
- Availability wie, co można zablokować;
- osobna decyzja może określać, jak właściwości zasobu przekładają się na
  jednostki dostępności.

To mapowanie może być ważniejszą częścią domeny niż oba końce relacji.

## Kiedy szukać mapping modelu

Sygnały:

- nowe wymaganie potrzebuje danych z kilku modeli;
- rozszerzenie któregokolwiek z nich zmienia jego główne pytanie;
- pojawia się specyficzne słownictwo wciskane do generycznego modelu;
- punkt wejścia do zachowania staje się koncepcyjnie mylący;
- reguła łączenia zmienia się niezależnie od modeli po obu stronach;
- mapowanie musi być audytowalne lub odtwarzalne;
- istnieją wyjątki, temporalność albo wersje mapowania;
- biznes posiada nazwę na proces przejścia między tymi stanami lub rolami.

## Mapping model ≠ mapper

Nie każde mapowanie jest modelem domenowym.

Zwykłe:

DTO A → DTO B

albo:

odpowiedź z modułu A + odpowiedź z modułu B → ekran

może pozostać translacją lub kompozycją query.

Kandydat na model rośnie w siłę, gdy mapowanie:

- steruje zmianą stanu;
- zawiera policy;
- ma własne wyjątki;
- ma historię;
- wymaga provenance;
- wpływa na pieniądze, uprawnienia, kwalifikowalność lub zobowiązania;
- jest używane w wielu procesach jako stabilne pojęcie.

## Procedura

1. Nazwij [[Main Question]] obu istniejących modeli.
2. Nazwij nowe pytanie wymagania.
3. Sprawdź, czy nowe pytanie jest tylko kompozycją odczytów.
4. Jeżeli nie:
   - wskaż ownera decyzji;
   - wskaż właścicieli faktów wejściowych;
   - znajdź policy i wyjątki;
   - sprawdź temporalność i reconstructability.
5. Użyj [[Backward Narration]], aby znaleźć brakujący krok przed operacją.
6. Poszukaj [[Pivotal Event]], po którym obiekt zaczyna działać według nowych
   reguł.
7. Zasymuluj kolejne wymagania i spróbuj obalić hipotezę o nowym modelu.

## Przykład strukturalny

Resource ≠ Availability ≠ mapping Resource → AvailabilityUnit

Jeżeli jeden zasób może generować wiele jednostek dostępności zależnie od
właściwości lub planu, relacja 1:1 była tylko wcześniejszym założeniem.

## Failure pattern

Typowy błąd:

1. pojawia się nowe wymaganie;
2. zespół wybiera najbliższy nazwą moduł;
3. dopisuje do niego specyficzne dane i operacje;
4. moduł przestaje mieć jedno główne pytanie;
5. kolejne wymagania zwiększają coupling.

To jest sygnał, że problem może znajdować się poziom wyżej niż kod.

## Falsyfikacja

Nie twórz nowego modelu, jeżeli:

- reguła jest stała i trywialna;
- nie ma własnego języka biznesowego;
- nie ma znaczenia dla zmiany stanu;
- nie potrzebuje historii ani audytu;
- kompozycja odczytów jest tańsza i równie czytelna;
- nowy model nie poprawia ownershipu ani locality of change.

## Konsekwencja architektoniczna

Generyczny model może pozostać stabilny, a specyficzny biznes ujawniać się w
sposobie, w jaki generyczne modele są ze sobą mapowane.

**generyki ≠ cała domena**

Część unikalności domeny żyje w relacjach i transformacjach między nimi.

## Powiązania

- [[Main Question]]
- [[Pivotal Event]]
- [[Model Alternatives]]
- [[Backward Narration]]
- [[Linguistic Boundary]]
- [[Socio-Technical Boundary]]
