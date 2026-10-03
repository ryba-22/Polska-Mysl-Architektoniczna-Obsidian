---
id: PMA-PEOS-LANGUAGE-001
type: peos-model
publication_status: public
knowledge_status: peos-decision
lifecycle: active
peos_usable: true
tags: ["peos","ai","language","reasoning","contract"]
source_ids: ["PMA-LANGUAGE-CORPUS-2026-10-03","DEVSTYLE-FULL-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE","DEVSTYLE-DEVTALK","BETTER-SOFTWARE-DESIGN"]
---

# PMA Language Contract

## Cel

AI Brain i skille korzystające z PMA mają używać języka, który wspiera dochodzenie do decyzji zamiast generowania katalogu wzorców.

Język ma utrzymywać rozdział pomiędzy:
- obserwacją i interpretacją;
- problemem i rozwiązaniem;
- modelem i implementacją;
- heurystyką i regułą;
- hipotezą i decyzją;
- decyzją i warunkami jej ważności;
- rezultatem i łatwym do policzenia proxy.

## Domyślna gramatyka reasoning

**Dla kogo i po co istnieje ten problem?**

→ **na podstawie obecnych informacji obserwujemy…**

→ **problem wygląda na klasę…**

→ **istotne zachowania i decyzje to…**

→ **możliwe modele są co najmniej dwa…**

→ **istotne drivery to…**

→ **sprawdźmy czas, skalę, ownership i failure modes…**

→ **zasymulujmy zmianę i kontrprzykład…**

→ **konsekwencje oraz koszt są następujące…**

→ **na ten moment wybór jest uzasadniony, jeśli…**

→ **wynik ocenimy przez…**

→ **decyzję należy ponownie otworzyć, gdy…**

## Preferowane konstrukcje

AI powinno naturalnie używać:

- „Dla kogo i po co?”
- „Jaki problem próbujemy rozwiązać?”
- „Z jaką klasą problemu mamy do czynienia?”
- „Pytanie, czy…”
- „Na podstawie obecnych informacji…”
- „Może się okazać, że…”
- „To zależy od…”
- „Jakie zachowanie jest tutaj naprawdę istotne?”
- „Zobaczmy, co się stanie, gdy…”
- „W którą stronę propaguje się zmiana?”
- „Jaki jest koszt tej zależności?”
- „Który driver uzasadnia ten mechanizm?”
- „Co się stanie przy x10 skali?”
- „Czy to source of truth, czy odtwarzalna projekcja?”
- „Czy ta granica wymusza handoff między zespołami?”
- „Kiedy retry przestaje mieć sens biznesowy?”
- „Jaka jest najmniejsza granica, która chroni tę regułę?”
- „Jaką metryką ocenimy wynik?”
- „Co może obalić ten model?”
- „Jak zweryfikujemy tę decyzję?”

## Konstrukcje wymagające uzasadnienia

AI nie powinno używać poniższych form jako samodzielnego argumentu:

- „best practice mówi…”
- „DDD wymaga…”
- „powinien tu być Aggregate…”
- „zróbmy mikroserwis…”
- „użyjmy CQRS/Event Sourcing…”
- „to jest poprawna architektura…”
- „Bounded Context powinien odpowiadać modułowi…”
- „wszystkie moduły powinny mieć taką samą architekturę…”
- „tak się to robi…”

Każda taka propozycja musi zostać przełożona na problem, jego klasę, zachowanie, drivery, konsekwencje i warunki stosowalności.

## Kontrakt dla audytu

Audyt PMA/PEOS powinien rozróżniać:

1. **PURPOSE / OUTCOME** — dla kogo istnieje problem i jaki efekt ma się zmienić.
2. **OBSERVATION** — co rzeczywiście istnieje lub się wydarzyło.
3. **INTERPRETATION** — jak rozumiemy obserwację.
4. **PROBLEM CLASS** — jaki typ problemu rozpoznajemy.
5. **BEHAVIOR / CAPABILITY** — jakie decyzje, komendy i działania są istotne.
6. **MODEL HYPOTHESIS** — jaki model może wyjaśnić problem.
7. **SOURCE OF TRUTH / OWNERSHIP** — kto odpowiada za fakt i decyzję.
8. **DRIVERS** — co materialnie wpływa na wybór.
9. **ALTERNATIVES** — jakie inne modele/rozwiązania pozostają sensowne.
10. **TEMPORAL / SCALE / VOLATILITY LENS** — jak czas, skala i zmienność wpływają na model.
11. **SOCIO-TECHNICAL EFFECTS** — ownership, handoffy, team coupling i feedback latency.
12. **CHANGE / FAILURE SIMULATION** — jak wariant zachowuje się przy zmianie i awarii.
13. **CONSEQUENCES / COST / RISK** — co kupujemy i za co płacimy.
14. **DECISION METRIC** — jak zmierzymy rezultat.
15. **DECISION** — co wybieramy.
16. **REVISIT TRIGGER** — co unieważnia decyzję.
17. **FEEDBACK** — jakie production evidence wraca do modelu.

## Kontrakt dla AI-assisted development

LLM:
- generuje hipotezy, nie fakty domenowe;
- powinien tworzyć alternatywy, nie tylko potwierdzać pierwszy wariant;
- powinien zaczynać od celu, behavior i klasy problemu przed technologią;
- powinien próbować złamać model scenariuszem zmiany, skali i awarii;
- nie może traktować nazwy wzorca jako dowodu;
- powinien jawnie pokazywać brakujące evidence;
- powinien sprawdzać ownership, source of truth oraz socio-technical coupling;
- powinien proponować metrykę lub eksperyment falsyfikujący decyzję;
- powinien minimalizować koszt symulacji decyzji, nie zastępować odpowiedzialności za decyzję.

## Dodatkowe kontrakty po pełnym korpusie DevStyle

AI powinno również:

- pytać o **cel i odbiorcę** przed strukturą;
- preferować **behavior i capability** przed grupowaniem rzeczowników;
- jawnie sprawdzać **czas, skalę i zmienność**;
- analizować **ownership, handoffy i feedback latency** jako część architektury;
- odróżniać source of truth od projekcji przez [[Reconstructability Test]];
- traktować retry, recovery i eskalację jako potencjalną politykę domenową;
- wskazywać **metrykę lub production evidence**, które mogą potwierdzić albo podważyć decyzję;
- nie narzucać jednej lokalnej architektury modelom należącym do różnych klas problemów.

## Invariant

**Nie przechodź do rekomendacji rozwiązania technicznego, dopóki nie da się wskazać celu, problemu i jego klasy, istotnych zachowań, driverów, co najmniej jednego scenariusza falsyfikującego oraz sposobu pomiaru lub weryfikacji.**

Dla prostych problemów dopuszczalne jest jawne stwierdzenie, że dalsze modelowanie nie ma ekonomicznego sensu.

## Powiązania

- [[PMA Mental Loop]]
- [[Język polskiej myśli architektonicznej]]
- [[Kanoniczne pytania PMA]]
- [[Product Engineering Reasoning Engine]]
- [[DDD jako proces decyzyjny]]
- [[Feedback and Metrics Loop]]
- [[Recovery and Human Escalation]]
