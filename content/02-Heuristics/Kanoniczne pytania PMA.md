---
id: PMA-HEURISTIC-QUESTIONS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["questions","reasoning","facilitation","ddd","architecture"]
source_ids: ["PMA-LANGUAGE-CORPUS-2026-10-03","DEVSTYLE-FULL-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE","DEVSTYLE-DEVTALK","BETTER-SOFTWARE-DESIGN"]
---

# Kanoniczne pytania PMA

## Teza

Dobra analiza częściej zaczyna się od właściwego pytania niż od właściwego wzorca.

Pełny zestaw pytań jest zsynchronizowany z [[PMA Mental Loop]].

## 1. Intencja i wartość

1. Dla kogo istnieje ten problem?
2. Po co istnieje ten proces, capability albo model?
3. Jaki efekt ma się zmienić?
4. Co ma wartość, a co jest tylko aktywnością?

## 2. Evidence i problem

5. Co dokładnie obserwujemy?
6. Co jest faktem, a co interpretacją?
7. Jaki problem próbujemy rozwiązać?
8. Jakiej informacji nadal brakuje?

## 3. Klasa problemu

9. Z jaką klasą problemu mamy do czynienia?
10. Czy operacja modyfikuje source of truth?
11. Czy zapis jednej operacji wpływa na to, co inni mogą zrobić równolegle?
12. Czy stan można skasować i odtworzyć bez utraty informacji?
13. Czy istotą jest obliczenie, prezentacja, integracja czy walka o zasób?

## 4. Zachowanie i model

14. Jakie czasowniki opisują domenę?
15. Jakie decyzje naprawdę są tutaj podejmowane?
16. Czy wspólny rzeczownik ukrywa kilka modeli?
17. Jaki model przyjmujemy?
18. Co ten model świadomie pomija?
19. Jaki drugi model również pasuje do evidence?

## 5. Ownership i zależności

20. Kto jest właścicielem decyzji?
21. Kto jest właścicielem źródła prawdy?
22. Kto od kogo zależy?
23. W którą stronę propaguje się zmiana?
24. Czy zależność jest semantyczna, czasowa, organizacyjna czy techniczna?

## 6. Czas, skala i zmienność

25. Czy kolejność ma znaczenie biznesowe?
26. Jak długo decyzja pozostaje ważna?
27. Co się stanie przy x10 skali?
28. Co zmienia się często, a co jest stabilne?
29. Czy istnieje punkt, po którym cofnięcie operacji jest bardzo drogie?

## 7. System społeczno-techniczny

30. Czy zmiana jednego zespołu wymaga czekania na drugi?
31. Gdzie pojawia się handoff?
32. Czy odpowiedzialność jest jasna end-to-end?
33. Czy zakres wiedzy potrzebny do zmiany mieści się w granicy zespołu?
34. Czy architektura skraca pętlę feedbacku?

## 8. Failure i recovery

35. Co się stanie przy partial failure?
36. Czy wszystkie kroki naprawdę muszą zakończyć się sukcesem razem?
37. Co biznesowo znaczy „razem”?
38. Kiedy retry nadal ma sens?
39. Kiedy system powinien eskalować do człowieka?
40. Jak człowiek bezpiecznie wznowi lub skoryguje proces?

## 9. Drivery, koszt i ryzyko

41. Co optymalizujemy?
42. Który driver jest dominujący?
43. Jaki koszt ma ta zależność?
44. Jaki jest blast radius błędnej decyzji?
45. Czy dodatkowa złożoność jest proporcjonalna do wartości problemu?

## 10. Falsyfikacja i decyzja

46. Co może obalić ten model?
47. Jaki scenariusz jest dla niego najtrudniejszy?
48. Jakie alternatywy odrzucamy i dlaczego?
49. Jakie konsekwencje świadomie akceptujemy?
50. Jaki warunek powinien ponownie otworzyć decyzję?

## 11. Pomiar i uczenie

51. Jaką metryką ocenimy wynik?
52. Czy metryka mierzy cel czy proxy?
53. Jaki najmniejszy eksperyment daje wartościowe evidence?
54. Jak szybko dostaniemy feedback?
55. Co po wdrożeniu może zmienić nasz model?

## Heurystyka rozmowy

Preferuj sekwencję:

**intencja → pytanie → evidence → problem → klasa → behavior → modele → drivery → stress test → konsekwencje → decyzja → metryka → feedback**

Unikaj:

**nazwa wzorca → uzasadnienie po fakcie → implementacja → sukces mierzony samym wdrożeniem**

## Kontrprzykłady i granice stosowalności

Nie każde zadanie wymaga 55 pytań. Prosty CRUD, lokalna transformacja lub mała poprawka mogą zakończyć pętlę bardzo wcześnie. Celem jest zmniejszenie kosztu błędnej decyzji, nie maksymalizacja ceremonii.

## Powiązania

- [[PMA Mental Loop]]
- [[Język polskiej myśli architektonicznej]]
- [[Problem Classification]]
- [[Architecture Drivers]]
- [[Feedback and Metrics Loop]]
