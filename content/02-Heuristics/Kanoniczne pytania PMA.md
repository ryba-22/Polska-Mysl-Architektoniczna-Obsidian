---
id: PMA-HEURISTIC-QUESTIONS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["questions","reasoning","facilitation","ddd","architecture"]
source_ids: ["PMA-LANGUAGE-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE","DEVSTYLE-DEVTALK","BETTER-SOFTWARE-DESIGN"]
---

# Kanoniczne pytania PMA

## Teza

Dobra analiza architektoniczna częściej zaczyna się od właściwego pytania niż od właściwego wzorca.

## Minimalny zestaw pytań

### Problem
1. Jaki problem próbujemy rozwiązać?
2. Z jaką klasą problemu mamy do czynienia?
3. Co jest faktem, a co założeniem?
4. Co jest złożonością domenową, a co przypadkową?

### Model
5. Jaki model przyjmujemy?
6. Co ten model upraszcza lub pomija?
7. Jaki drugi model również pasuje do obecnych informacji?
8. Czy model opisuje zachowanie i decyzje, czy tylko dane?

### Granice
9. Co musi zmieniać się razem?
10. Co może ewoluować niezależnie?
11. Gdzie zmienia się język lub reguła?
12. Kto jest właścicielem decyzji i source of truth?

### Zależności
13. Kto od kogo zależy?
14. W którą stronę propaguje się zmiana?
15. Jaki jest koszt tej zależności?
16. Czy zależność jest semantyczna, czasowa czy techniczna?

### Reguły i concurrency
17. Jaka reguła musi być chroniona natychmiast?
18. Jaka jest najmniejsza granica, która może ją ochronić?
19. Co się stanie przy dwóch równoległych poprawnych żądaniach?
20. O jaki ograniczony zasób konkurują operacje?

### Drivery
21. Co optymalizujemy?
22. Który driver biznesowy lub techniczny jest dominujący?
23. Jaki atrybut jakościowy uzasadnia dodatkowy mechanizm?
24. Czy koszt rozwiązania jest proporcjonalny do wartości problemu?

### Falsyfikacja
25. Co się stanie, jeśli jutro zmieni się reguła?
26. Jak daleko pójdzie fala zmian?
27. Jaki scenariusz najłatwiej złamie proponowaną granicę?
28. Co musiałoby się wydarzyć, żebyśmy zmienili decyzję?

### Decyzja
29. Jakie alternatywy rozważaliśmy?
30. Jakie konsekwencje świadomie akceptujemy?
31. Której decyzji nie musimy jeszcze podejmować?
32. Jak zweryfikujemy, że wybrany wariant faktycznie działa?

## Heurystyka rozmowy

Preferuj sekwencję:

**pytanie → evidence → hipoteza → alternatywa → scenariusz zmiany → konsekwencja → decyzja → warunek weryfikacji**

Unikaj sekwencji:

**nazwa wzorca → uzasadnienie po fakcie → implementacja**

## Kontrprzykłady i granice stosowalności

Nie każde zadanie wymaga pełnego zestawu pytań. Prosty CRUD, transformacja lub lokalna poprawka mogą wymagać tylko kilku z nich. Celem jest zmniejszenie kosztu błędnej decyzji, nie maksymalizacja ceremonii.

## Powiązania

- [[Język polskiej myśli architektonicznej]]
- [[Problem Classification]]
- [[Architecture Drivers]]
- [[Scenario Before Aggregate]]
- [[Unit of Change]]
