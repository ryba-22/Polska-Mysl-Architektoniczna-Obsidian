---
id: PMA-CONCEPT-LANGUAGE-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["language","reasoning","ddd","architecture","pma"]
source_ids: ["PMA-LANGUAGE-CORPUS-2026-10-03","DEVSTYLE-FULL-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE","DEVSTYLE-DEVTALK","BETTER-SOFTWARE-DESIGN","DDD-WAW-VIDEOS"]
---

# Język polskiej myśli architektonicznej

## Teza

W polskiej praktyce DDD i architektury powtarza się nie tylko zestaw pojęć, ale charakterystyczny sposób prowadzenia rozumowania.

Nie zaczyna się od wzorca. Zaczyna się od obserwacji, pytania i problemu, a następnie przechodzi przez model, drivery, alternatywy, konsekwencje i weryfikację.

Przydatny szkielet:

**obserwacja → pytanie → problem → klasa problemu → możliwe modele → drivery i ograniczenia → heurystyki → warianty → symulacja zmian → konsekwencje i koszt → decyzja → weryfikacja → rozwiązanie techniczne**

To jest język decyzji, nie katalogu wzorców.

## Rejestr językowy

Poniższe konstrukcje są autorską normalizacją sposobu mówienia obecnego w publicznym korpusie PMA. Nie są transkrypcją ani zbiorem cytatów.

### 1. Rozpoznanie problemu

- Jaki problem właściwie próbujemy rozwiązać?
- Z jaką klasą problemu mamy tutaj do czynienia?
- Co jest istotą problemu, a co tylko jego obecnym przejawem?
- Czy rozwiązujemy problem biznesowy, techniczny czy organizacyjny?
- Czy ten problem rzeczywiście wymaga bogatego modelu?
- Co sprawia, że ten przypadek jest trudny?

### 2. Problem i rozwiązanie

- Najpierw rozpoznajmy klasę problemu, potem dobierzmy klasę rozwiązania.
- Nie zaczynajmy od narzędzia.
- Jaki mechanizm odpowiada naturze tego problemu?
- Czy używane narzędzie pasuje do klasy problemu?
- Czy istnieje prostsze rozwiązanie tego samego problemu?
- Czy nie sprowadzamy problemu nietechnicznego do problemu technicznego?

### 3. Evidence i niepewność

- Co wiemy, a co tylko zakładamy?
- Na podstawie jakiej informacji wyciągamy ten wniosek?
- Czy mamy obserwację, czy interpretację obserwacji?
- Jakiej informacji brakuje do podjęcia decyzji?
- Co musielibyśmy zobaczyć, żeby zmienić zdanie?
- Czy to wynika z domeny, czy z obecnej implementacji?

### 4. Model

- Jaki model problemu właśnie budujemy?
- Co ten model upraszcza?
- Co świadomie pomijamy?
- Czy model pomaga podejmować decyzje?
- Czy model jest zrozumiały dla źródła wiedzy?
- Czy możemy zbudować drugi sensowny model tego samego problemu?
- Czy model opisuje zachowanie, czy tylko strukturę danych?

### 5. Alternatywy

- Jak wyglądałby drugi sensowny wariant?
- Jakie mamy alternatywne sposoby podziału?
- Co zyskujemy, a co tracimy w każdym wariancie?
- Które założenie powoduje, że ten wariant ma sens?
- Które decyzje możemy jeszcze odroczyć?
- Który wariant zachowuje większą swobodę przyszłej zmiany?

### 6. Heurystyki

- Potraktujmy to jako heurystykę, nie regułę absolutną.
- Ta heurystyka ma zawęzić przestrzeń możliwych rozwiązań.
- Najpierw użyjmy heurystyki zgrubnej, potem precyzyjnej.
- Co ta heurystyka pozwala nam wyeliminować?
- W jakich warunkach przestaje działać?
- Czy potrzebujemy reguły, czy wystarczy dobra heurystyka?

### 7. Drivery

- Jakie drivery biznesowe wpływają na tę decyzję?
- Jakie drivery techniczne są tutaj materialne?
- Który driver jest dominujący?
- Co właściwie optymalizujemy?
- Za co klient rzeczywiście płaci?
- Jaki atrybut jakościowy uzasadnia dodatkową złożoność?
- Jaki koszt poniesiemy, jeśli ten driver zignorujemy?

### 8. Koszt i wartość

- Gdzie ta decyzja generuje koszt?
- Jaki jest koszt przyszłej zmiany?
- Jaki jest koszt tej zależności?
- Czy koszt rozwiązania jest proporcjonalny do wartości problemu?
- Gdzie warto inwestować czas najlepszych ludzi?
- Czy płacimy za złożoność domenową, czy za złożoność przypadkową?

### 9. Granice modeli

- Gdzie zmienia się język?
- Gdzie zmieniają się reguły?
- Gdzie zmienia się odpowiedzialność za decyzję?
- Co może ewoluować niezależnie?
- Co musi zmieniać się razem?
- Czy granica wynika z zachowania, czy tylko z rzeczownika?
- Czy mamy jeden model, czy dwa modele używające podobnych nazw?

### 10. Autonomia

- Jaką decyzję ten model może podjąć autonomicznie?
- Czy ten obszar może działać, gdy sąsiedni jest niedostępny?
- Czy do działania musimy synchronicznie pytać inny model?
- Kto jest właścicielem decyzji?
- Kto jest właścicielem źródła prawdy?
- Czy autonomia jest rzeczywista, czy tylko deklarowana?

### 11. Zależności

- Kto od kogo zależy?
- W którą stronę propagują się zmiany?
- Czy zależność jest konieczna, czy przypadkowa?
- Która strona narzuca kontrakt?
- Co stanie się z konsumentem, jeśli dostawca zmieni model?
- Czy zależność jest semantyczna, czasowa czy techniczna?

### 12. Symulowanie zmian

- Co się stanie, jeśli ta reguła zmieni się jutro?
- Co się stanie, jeśli dodamy drugi wariant procesu?
- Co się stanie, jeśli model będzie musiał działać niezależnie?
- Które moduły będziemy musieli zmienić?
- Jak daleko propaguje się zmiana?
- Czy mała zmiana biznesowa powoduje dużą zmianę techniczną?
- Zasymulujmy zmianę i zobaczmy, gdzie pójdzie fala zmian.

### 13. Język domeny

- Czy to słowo oznacza tutaj dokładnie to samo?
- Czy dwa obszary używają tej samej nazwy w innym znaczeniu?
- Jak ekspert dziedzinowy nazywa tę czynność?
- Czy nazwa opisuje intencję biznesową, czy implementację?
- Czy język kodu odpowiada językowi rozmowy?
- Czy termin ma sens tylko w jednym kontekście?

### 14. Event Storming

- Co się wydarzyło?
- Co spowodowało to zdarzenie?
- Kto chciał, żeby to się wydarzyło?
- Jaką decyzję trzeba było podjąć?
- Jakiej informacji potrzebowano do tej decyzji?
- Jaka reguła zadecydowała o wyniku?
- Kogo interesuje fakt, że to się wydarzyło?

### 15. Reguły i spójność

- Jaka reguła musi być zawsze prawdziwa?
- Kiedy ta reguła musi zostać sprawdzona?
- Czy wymaga natychmiastowej spójności?
- Czy naruszenie można naprawić później?
- Jaki stan jest potrzebny do podjęcia decyzji?
- Kto jest właścicielem tej reguły?

### 16. Aggregate i concurrency

- Jaki invariant uzasadnia tę granicę?
- Jaka jest najmniejsza granica, która potrafi ochronić tę regułę?
- Czy agregat wynika z zachowania, czy z relacji między tabelami?
- Czy wszystko wewnątrz naprawdę musi być atomowe?
- Co się stanie, gdy dwie poprawne komendy wykonają się równocześnie?
- O jaki zasób konkurują te operacje?
- Jaka jest jednostka konkurencji?

### 17. Legacy

- Obecny kod jest źródłem informacji, nie definicją domeny.
- Co w legacy jest regułą biznesową, a co historycznym skutkiem implementacji?
- Które zachowanie jest przypadkowe, a które stało się kontraktem?
- Jaką wiedzę domenową ukrywa ten fragment kodu?
- Jakie założenie musiało być prawdziwe, żeby kod powstał w ten sposób?
- Jaki model mentalny ujawnia obecna implementacja?

### 18. Modularyzacja i architektura

- Najpierw znajdźmy logiczne podproblemy, nie katalogi w kodzie.
- Co zmienia się z tego samego powodu?
- Czy moduł ma własne zachowanie i odpowiedzialność?
- Czy podział jest stabilny wobec przewidywanych zmian?
- Który problem uzasadnia ten element architektury?
- Jakie drivery wymusiły tę decyzję?
- Jaki trade-off świadomie akceptujemy?
- Co się stanie, jeśli usuniemy ten mechanizm?

### 19. Wzorce i technologia

- Nie utożsamiajmy wzorca z konkretną technologią.
- Co konkretnie kupujemy dzięki temu wzorcowi?
- Czy mechanizm jest wymaganiem, czy preferencją implementacyjną?
- Czy potrzebujemy rozproszenia, czy tylko separacji modelu?
- Czy potrzebujemy kolejki, czy wystarczy lokalny mechanizm?
- Czy dokładamy mechanizm dlatego, że rozwiązuje problem, czy dlatego, że jest znany?

### 20. Decyzja i weryfikacja

- Jaką decyzję właściwie podejmujemy?
- Na podstawie jakich driverów?
- Jakie alternatywy odrzuciliśmy?
- Jakie konsekwencje świadomie akceptujemy?
- Które założenie może unieważnić tę decyzję?
- Kiedy powinniśmy do niej wrócić?
- Co może obalić ten model?
- Jaki najmniejszy eksperyment pozwoli go zweryfikować?

## Charakterystyczne konstrukcje rozmowy

W publicznym korpusie często wraca styl, który utrzymuje decyzje w stanie falsyfikowalnym:

- „Pytanie, czy…”
- „Może się okazać, że…”
- „To zależy od…”
- „Zobaczmy, co się stanie, gdy…”
- „Jeżeli przyjmiemy X, konsekwencją będzie Y…”
- „Na podstawie obecnych informacji…”
- „Nie wiadomo jeszcze, czy…”
- „Być może problem leży gdzie indziej…”
- „Co to właściwie znaczy?”
- „Po co nam to?”
- „Kto od kogo zależy?”
- „Co by się stało, gdyby…?”

Ta forma jest ważna: model pozostaje hipotezą, a decyzja pozostaje jawnie związana z warunkami, w których została podjęta.

## Profile sposobu rozumowania

To profile syntetyczne, nie przypisanie pojedynczych cytatów.

**Sławomir Sobótka** — klasa problemu, model, heurystyka, autonomia, złożoność przypadkowa, konsekwencje zmian i przejście od problem space do solution space.

**Jakub Pilimon** — drivery, zawężanie przestrzeni decyzji, jakość rozwiązania względem celu, trade-offy oraz legacy jako źródło wiedzy o decyzjach i modelu.

**Bartek Słota** — koszt zależności, granice odpowiedzialności, autonomia modeli, Context Mapping i ukryte konsekwencje pozornie lokalnych decyzji.

**Łukasz Szydło** — symulowanie zmian, testowanie granic niezależnie od etykiet DDD, zmienność, modularność i właściwości jakościowe.

**Marcin Markowski** — rozdzielanie modelu i modułu od deploymentu, archetypy modeli, autononomiczne konteksty i wydobywanie granic z legacy.

**Oskar Dudycz** — pragmatyzm implementacyjny, rozdzielanie wzorca od technologii, odchudzanie agregatów, jawne koszty CQRS/Event Sourcing i unikanie architektury ceremonialnej.

**Mariusz Gil** — prowadzenie rozmowy przez pytania, kontrasty i przykłady oraz wydobywanie warunków, w których model ma sens.

**Maciej Aniserowicz / DevTalk** — uczenie przez różnicowanie, prowokacyjne pytania, testowanie „czy to w ogóle ma sens?” i konfrontowanie deklaracji z praktyczną konsekwencją.

## Rozszerzenie po pełnym korpusie DevStyle

Analiza wszystkich 89 materiałów z kanału DevStyle ujawniła grupy sformułowań słabo reprezentowane w pierwszej wersji PMA.

### Cel, klient i efekt

- Dla kogo to właściwie istnieje?
- Po co potrzebujemy tego modelu?
- Co dzięki temu ma stać się możliwe?
- Jaki efekt chcemy zmienić?
- Czy optymalizujemy rezultat, czy tylko łatwą do policzenia aktywność?

### Zachowanie przed strukturą

- Jakie czasowniki opisują ten problem?
- Co użytkownik lub system próbuje zrobić?
- Która operacja wpływa na możliwość wykonania innej?
- Czy wspólny rzeczownik nie ukrywa kilku różnych modeli?
- Czy ta granica wynika z behavior, czy ze schematu danych?

### Odtwarzalność i source of truth

- Czy mogę skasować ten model i odtworzyć go bez utraty informacji?
- Który model jest właścicielem faktu?
- Czy to stan biznesowy, czy projekcja?
- Czy kolejność pojawienia się danych wpływa na wynik?

### Czas, skala i zmienność

- Co się stanie przy dziesięciokrotnie większej skali?
- Co zmienia się często, a co pozostaje stabilne?
- Czy kolejność ma znaczenie biznesowe?
- Jak długo ta decyzja pozostaje ważna?
- Czy przekroczyliśmy punkt, po którym cofnięcie jest bardzo drogie?

### System społeczno-techniczny

- Czy zmiana jednego zespołu wymaga czekania na drugi?
- Gdzie znajduje się handoff?
- Czy ownership jest wystarczająco jasny?
- Czy zakres odpowiedzialności mieści się poznawczo w głowie zespołu?
- Czy granica skraca, czy wydłuża pętlę feedbacku?

### Pomiar i uczenie

- Jaką metryką ocenimy jakość modelu?
- Co mierzymy przed zmianą?
- Jakie production evidence może podważyć decyzję?
- Jak szybko dostaniemy feedback?
- Czy metryka jest związana z celem, czy jest tylko łatwym proxy?

### Recovery i eskalacja

- Co dokładnie oznacza, że operacja ma zakończyć się sukcesem?
- Czy wszystkie kroki naprawdę muszą zakończyć się razem?
- Ile razy i jak długo warto próbować ponownie?
- Kiedy retry przestaje mieć sens biznesowy?
- Kiedy potrzebny jest człowiek i jaką decyzję ma podjąć?

Pełna operacyjna pętla znajduje się w [[PMA Mental Loop]].

## Meta-reguły PMA

1. Nie nazywaj rozwiązania, zanim nie potrafisz nazwać problemu i sił wpływających na decyzję.
2. Model traktuj jako hipotezę do testowania scenariuszami zmian, nie diagram do zatwierdzenia.
3. Heurystyka zawęża przestrzeń rozwiązań; nie udaje prawa natury.
4. Granica jest wartościowa, jeśli ogranicza propagację zmian i odpowiedzialności, nie dlatego, że ma nazwę z DDD.
5. Decyzja architektoniczna jest ważna razem ze swoimi driverami, alternatywami, kosztem i warunkiem ponownego otwarcia.

## Powiązania

- [[DDD jako proces decyzyjny]]
- [[Problem Classification]]
- [[Architecture Drivers]]
- [[Unit of Change]]
- [[Linguistic Boundary]]
- [[Scenario Before Aggregate]]
- [[Product Engineering Reasoning Engine]]
- [[PMA Language Contract]]
- [[Metodyka korpusu językowego PMA]]
