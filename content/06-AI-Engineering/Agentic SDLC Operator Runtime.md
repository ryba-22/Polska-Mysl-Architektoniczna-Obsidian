---
id: PMA-AI-OPERATOR-RUNTIME-001
type: synthesis
publication_status: public
knowledge_status: synthesis
lifecycle: active
peos_usable: true
tags: ["ai","agentic-sdlc","operator-runtime","standards","verification","orchestration"]
source_ids: ["SKILLPANEL-MAISTER","AI-THAT-WORKS"]
---

# Agentic SDLC Operator Runtime

Dojrzały agentic SDLC potrzebuje dwóch odrębnych warstw:

1. **engineering reasoning / governance** — co powinno zostać zrobione, dlaczego, na podstawie jakich dowodów i przy jakim ryzyku;
2. **operator runtime** — jak człowiek uruchamia, obserwuje, wznawia i weryfikuje pracę agentów bez rekonstruowania kontekstu z rozmowy.

Maister jest użytecznym practitioner reference dla drugiej warstwy. Nie jest źródłem prawdy dla domeny ani architektury projektu.

## Wzorce warte przeniesienia

### Project Constitution Discovery

Standard projektu nie powinien być zgadywany z jednej instrukcji. Kandydaci mogą być rekonstruowani z:

- konfiguracji narzędzi;
- powtarzalnych wzorców kodu;
- dokumentacji;
- CI/CD;
- historii review/PR, jeżeli jest dostępna.

Wynik discovery jest **obserwacją**, nie automatycznie obowiązującą regułą.

Przepływ:

`observed convention → evidence/confidence → conflict check → owner approval → intended rule → executable enforcement`

### Task-local Execution Dossier

Długie zadanie powinno mieć trwały pakiet artefaktów pozwalający wznowić pracę bez polegania na pamięci chatu:

`analysis → decisions → implementation → verification`

Dossier przechowuje evidence i artefakty. Nie powinno tworzyć drugiego canonical state.

### Verification Fan-out

Jedno ogólne „review” miesza różne pytania. Weryfikację można rozdzielić na niezależne osie:

- completeness;
- executable tests;
- code/contract review;
- pragmatic / over-engineering review;
- reality check — czy rozwiązano właściwy problem;
- production readiness.

Nie każda oś musi być aktywna dla każdego zadania. Dobór powinien zależeć od ryzyka i rodzaju gwarancji.

### Operator Dashboard as Projection

Dashboard poprawia human observability, ale powinien być **read model**, obliczanym z canonical state, Git i evidence.

`canonical state + repo/Git + evidence → projection/dashboard`

Nigdy odwrotnie.

### Single Front Door

Operator nie powinien znać całej topologii repozytoriów i workflow przed rozpoczęciem pracy.

Punkt wejścia powinien przyjmować problem, a następnie wykonywać:

`outcome → risk → missing evidence → knowledge routing → execution profile → workflow/lane topology`

### Fast Path

Pełny proces dla każdej drobnej zmiany tworzy ceremony debt. Szybka ścieżka ma sens, jeśli jest skutkiem jawnie niskiego ryzyka i odwracalności, a nie osobnym „trybem bez zasad”.

## Kontr-zasady

### State nie jest rzeczywistością

Task state może sterować orkiestracją, ale nie może mieć wyższego autorytetu niż:

`actual behavior → Git SHA/diff → executable evidence → process state → reports → conversation`

### Observed convention ≠ intended standard

Częstotliwość wzorca w kodzie może oznaczać standard, przypadek albo historyczny dług. Discovery tworzy kandydatów, nie konstytucję automatycznie.

### Gate wynika z ryzyka lub decyzji, nie numeru fazy

Stałe approval checkpointy dają kontrolę, ale mogą tworzyć approval fatigue. Gate powinien być obowiązkowy, gdy zmienia się materialny scope, trust boundary, irreversible effect, acceptance authority albo evidence jest niewystarczające.

### Executor ≠ reviewer

Specjalistyczny verification fan-out nie zastępuje niezależności review. Agent wykonujący zmianę nie powinien być jedynym źródłem werdyktu o jej poprawności.

## Kandydaci do PEOS / ChatLOOP

- Project Constitution Discovery jako evidence-gathering przed planowaniem;
- risk-derived execution profiles: fast / standard / evidence-heavy;
- Verification Matrix zamiast jednego uniwersalnego review;
- Execution Dossier przy lane;
- dashboard jako read-time projection;
- jeden operator front door routujący do odpowiedniego workflow.

## Granica zastosowania

Maister jest tutaj źródłem practitioner patterns. Nie traktujemy jego workflow jako dowodu, że konkretna liczba faz, promptów lub approval gates jest optymalna. Wartość źródła polega na pokazaniu sprawdzalnych mechanizmów operator runtime, które można zestawić z silniejszym evidence/governance model PMA i PEOS.
