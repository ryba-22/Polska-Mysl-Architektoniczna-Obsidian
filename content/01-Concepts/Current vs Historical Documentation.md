---
id: PMA-CONCEPT-DOCS-CURRENT-HISTORY-001
type: concept
publication_status: public
knowledge_status: source-derived
lifecycle: verified
peos_usable: true
tags: ["documentation","adr","architecture","knowledge"]
source_ids: ["PROJECT-FRONTEND-EMAIL-2024-08-01"]
---

# Current vs Historical Documentation

Dokumentacja systemu odpowiada na dwa różne pytania: jak system działa teraz oraz dlaczego wygląda właśnie tak.

## Current documentation

Powinna być aktualna i pomagać wejść w projekt: cel systemu, uruchomienie, architektura, kontrakty, zależności i aktualne zachowanie.

## Historical documentation

Przechowuje decyzje i ich kontekst. ADR powinien opisywać decyzję, powód, rozważone alternatywy i konsekwencje. Gdy decyzja się zmienia, nowy ADR zastępuje poprzedni zamiast przepisywać historię.

## Widoki

Dla większych systemów modele C4 mogą uzupełniać current documentation, ale nie zastępują decision history.

## PEOS

Generated/current artifacts i immutable decision records powinny mieć różne lifecycle.
