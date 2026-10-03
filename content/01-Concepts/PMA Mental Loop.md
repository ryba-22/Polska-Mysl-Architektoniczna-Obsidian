---
id: PMA-CONCEPT-MENTAL-LOOP-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["pma","reasoning","mental-model","ddd","architecture","product-engineering"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03","PMA-LANGUAGE-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE"]
---

# PMA Mental Loop

## Teza

Dojrzałe myślenie architektoniczne nie jest linią problem → pattern.

Jest pętlą:

**intencja → evidence → problem → klasa problemu → zachowanie → modele → drivery → stress test → decyzja → pomiar → feedback → ponowne otwarcie decyzji**

Pełny korpus DevStyle pokazał, że pierwsza wersja PMA Mental Loop była zbyt skupiona na samym modelu i architekturze. Brakowało jej trzech perspektyw: **celu**, **systemu społeczno-technicznego** i **pętli uczenia**.

## Faza A — Orientuj się

### 1. Ustal intencję i wartość

- Dla kogo ten problem istnieje?
- Po co w ogóle istnieje ten proces lub moduł?
- Jaki efekt biznesowy lub operacyjny ma się zmienić?
- Czy optymalizujemy to, co ma wartość, czy to, co łatwo mierzyć?

### 2. Oddziel obserwację od interpretacji

- Co rzeczywiście widzę?
- Co jest faktem, a co już diagnozą?
- Jakie evidence potwierdza obserwację?
- Czego nadal nie wiemy?

### 3. Nazwij problem i jego klasę

- Jaki problem próbujemy rozwiązać?
- Czy to CRUD, transformacja, prezentacja, integracja, rywalizacja o zasób czy kombinacja klas?
- Co w wymaganiu jest tylko formą UI, a co zmienia semantykę decyzji?

## Faza B — Modeluj zachowanie

### 4. Zacznij od zachowań, nie rzeczowników

- Jakie decyzje i operacje są wykonywane?
- Jakimi czasownikami nazywa je domena?
- Która operacja wpływa na możliwość wykonania innej?
- Co jest capability, a co tylko wspólnym rzeczownikiem lub tabelą?

### 5. Zbuduj co najmniej dwa modele

- Jaki jest pierwszy sensowny model?
- Jak wygląda alternatywny model tego samego problemu?
- Co każdy model upraszcza?
- Co każdy model ukrywa lub komplikuje?

### 6. Ustal ownership i source of truth

- Kto jest właścicielem decyzji?
- Który model jest autorytatywny dla danego faktu?
- Czy dane są źródłem prawdy, kopią, projekcją czy cache?
- Czy ten stan można odtworzyć bez utraty informacji?

## Faza C — Stresuj model

### 7. Nazwij drivery

- Co naprawdę wymusza tę decyzję?
- Które atrybuty jakościowe są materialne?
- Jakie ryzyko redukujemy?
- Czy dodatkowa złożoność kupuje coś konkretnego?

### 8. Nałóż soczewkę czasu, skali i zmienności

- Co zmienia się często, a co pozostaje stabilne?
- Co się stanie przy x10 ruchu lub x10 danych?
- Czy kolejność i czas mają znaczenie biznesowe?
- Czy istnieje punkt, po którym operacji nie da się sensownie odwrócić?

### 9. Sprawdź granice społeczno-techniczne

- Czy granica software'u daje jasną odpowiedzialność?
- Czy zmiana jednego zespołu wymaga zgody albo czekania na drugi?
- Gdzie pojawia się handoff?
- Czy architektura skraca, czy wydłuża pętlę feedbacku?

### 10. Zasymuluj zmianę i awarię

- Co się stanie, jeśli reguła zmieni się jutro?
- Jak daleko pójdzie fala zmian?
- Co się stanie przy partial failure?
- Kiedy retry ma sens?
- Kiedy system powinien eskalować problem do człowieka?

### 11. Policz koszt i ryzyko

- Jaki jest koszt zależności?
- Jaki jest blast radius błędnej decyzji?
- Co kosztuje nas utrzymanie tej granicy?
- Czy koszt rozwiązania jest proporcjonalny do wartości problemu?

## Faza D — Podejmij falsyfikowalną decyzję

### 12. Ustal miarę jakości

- Po czym poznamy, że granica lub model działa?
- Jaka metryka jest związana z celem, a nie tylko łatwa do policzenia?
- Co zmierzymy przed i po zmianie?
- Jakie production evidence będzie istotne?

### 13. Spróbuj obalić model

- Jaki przypadek jest dla niego najtrudniejszy?
- Co może go sfalsyfikować?
- Czy model nadal działa przy innym ownership, skali lub czasie?
- Czy druga alternatywa radzi sobie lepiej z tym samym kontrprzykładem?

### 14. Podejmij decyzję wraz z warunkami ważności

- Co wybieramy?
- Dlaczego teraz?
- Jakie konsekwencje świadomie akceptujemy?
- Które założenie może unieważnić decyzję?
- Jaki jest revisit trigger?

## Faza E — Ucz się

### 15. Skróć pętlę feedbacku

- Jaki najmniejszy eksperyment pozwala sprawdzić decyzję?
- Jak szybko zobaczymy efekt?
- Czy test, metryka i telemetryka mierzą właściwy problem?
- Co nowego wiemy po wdrożeniu?
- Czy evidence zmieniło model albo drivery?

## Skrócona wersja do codziennego użycia

1. **Po co i dla kogo?**
2. **Jaki problem i jaka klasa problemu?**
3. **Jakie zachowanie jest naprawdę istotne?**
4. **Od czego zależy decyzja?**
5. **Co się stanie przy zmianie, skali lub awarii?**
6. **Co może obalić ten model?**
7. **Jak zmierzymy, że decyzja działa?**

## Invariant

Jeżeli znamy nazwę rozwiązania, ale nie potrafimy odpowiedzieć na pytania **po co, dla kogo, jaka klasa problemu, jakie zachowanie i jak zweryfikujemy efekt**, jesteśmy zbyt głęboko w solution space.

## Powiązania

- [[Język polskiej myśli architektonicznej]]
- [[Kanoniczne pytania PMA]]
- [[PMA Language Contract]]
- [[Problem Classification]]
- [[Purpose Before Structure]]
- [[Behavior Before Nouns]]
- [[Temporal Scale and Volatility Lens]]
- [[Socio-Technical Boundary]]
- [[Feedback and Metrics Loop]]
- [[Recovery and Human Escalation]]
