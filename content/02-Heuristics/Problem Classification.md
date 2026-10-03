---
id: PMA-H-PROBLEM-CLASS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["problem-classification","ddd","architecture"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","DOMAIN-DRIVERS-COURSE","DDD-BY-EXAMPLES-LIBRARY","DEVSTYLE-FULL-CORPUS-2026-10-03"]
---

# Problem Classification

Pattern selection bez wcześniejszej klasyfikacji problemu jest błędem procesu.

Nie zakładamy jednej homogenicznej architektury aplikacyjnej dla wszystkich modułów. Lokalny model i mechanizm techniczny powinny być adekwatne do lokalnej klasy problemu.

## Pięć podstawowych klas rozpoznawanych w publicznym korpusie

### CRUD / note-taking

Operacja głównie zapisuje lub odczytuje opisowy stan. Reguły nie zależą istotnie od współbieżnie zmieniającego się zasobu.

Sygnały:
- czasowniki typu zapisz, edytuj, usuń, odczytaj;
- kolejne zapisy zwykle nie zmieniają prawa innego użytkownika do wykonania operacji;
- historia wcześniejszych edycji rzadko zmienia dopuszczalność następnej.

Pytanie rozróżniające:

**Czy zapis tej informacji wpływa na to, co inny aktor może zrobić w tym samym czasie?**

### Resource Contention / consistency problem

Dopuszczalność operacji zależy od mutable state, który może zostać zmieniony przez inną równoległą komendę.

Sygnały:
- ograniczona pula lub limit;
- jedna komenda blokuje lub unieważnia inną;
- równoległe poprawne żądania mogą razem złamać invariant;
- potrzebna jest jawna granica spójności.

Pytanie:

**O jaki zasób konkurują operacje i jaka jest najmniejsza granica chroniąca regułę?**

### Presentation / projection

Model składa, grupuje lub przetwarza dane do odczytu, ale nie jest właścicielem źródłowego faktu biznesowego.

Pytanie:

**Gdyby skasować ten widok, raport lub read model i odbudować go z innych sources of truth, czy utracilibyśmy informację?**

Jeżeli nie, uruchom [[Reconstructability Test]].

### Transformation / calculation

Model pobiera dane ze źródeł i wykonuje nietrywialne obliczenie lub transformację. Jego istotą jest algorytm, nie walka o mutable resource.

Pytania:
- Czy źródła pozostają niezmienione?
- Czy problemem jest poprawność obliczenia?
- Czy wiele transformacji może działać równolegle bez wzajemnego unieważniania?

### Integration

Problem dotyczy współpracy autonomicznych modeli lub systemów i zmiany stanu poza lokalną granicą.

Sygnały:
- kontrakty między modelami;
- partial failure;
- retry;
- kolejność komunikatów;
- tłumaczenie znaczeń;
- potrzeba eskalacji.

Pytania:
- Czy modyfikujemy stan innego autonomicznego modelu?
- Czy wszystkie kroki muszą zakończyć się sukcesem „razem”?
- Co biznesowo oznacza „razem”?
- Czy kolejność ma znaczenie?
- Kiedy automatyczne ponowienie powinno ustąpić [[Recovery and Human Escalation|eskalacji]]?

## Problemy mieszane

Realny use case może łączyć kilka klas. To nie jest argument za jednym wielkim modelem.

Przykład: opis produktu może być prostym CRUD-em, a lifecycle tego samego produktu osobnym modelem stanów i reguł. Wspólny rzeczownik nie wymusza wspólnej granicy.

Uruchom [[Behavior Before Nouns]].

## Lenses dodatkowe

Niezależnie od klasy nałóż:
- [[Temporal Scale and Volatility Lens]];
- [[Architecture Drivers]];
- [[Unit of Change]];
- [[Socio-Technical Boundary]].

## Następny krok

Po klasyfikacji uruchom [[Pattern vs Archetype vs Algorithm]] i dopiero potem dobieraj architekturę.
