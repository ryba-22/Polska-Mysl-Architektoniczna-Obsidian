---
id: PMA-CONCEPT-COMPOSITION-001
type: concept
publication_status: public
knowledge_status: source-derived
lifecycle: candidate
peos_usable: true
tags: ["architecture","composition","dependency-inversion","testability"]
source_ids: ["SOFTWARE-ESSENTIALIST-EMAIL-2025-11-25"]
---

# Intentional Composition

Każda aplikacja gdzieś tworzy obiekty, wiąże zależności i wybiera wariant środowiska. Pytanie brzmi, czy robi to świadomie.

## Composition Root

Jedno jawne miejsce bootstrapu upraszcza kontrolę zależności i pozwala składać różne boot modes: development, test, integration, production, CLI lub worker.

## Sygnały problemu

Rozproszona konstrukcja zależności utrudnia:
- testowanie;
- podmianę infrastruktury;
- uruchamianie różnych środowisk;
- refaktor;
- izolowanie modułów.

## Heurystyka

Zacznij od pojedynczego bootstrap location i dependency inversion. Rozbudowany DI container jest opcją, nie warunkiem.

## Zastrzeżenie

To synteza jednego źródła praktycznego, a nie uniwersalny wymóg dla każdego systemu.
