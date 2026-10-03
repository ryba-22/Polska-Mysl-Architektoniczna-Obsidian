---
id: PMA-H-SOCIOTECH-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["socio-technical","team-topology","boundaries","ownership","feedback"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03"]
---

# Socio-Technical Boundary

## Teza

Granica modelu nie kończy się na kodzie. Jej konsekwencje pojawiają się w ownership, komunikacji, handoffach i czasie oczekiwania między zespołami.

Silna zależność organizacyjna może zostać odwzorowana w software, a źle dobrana granica software może wymusić silną zależność organizacyjną.

## Pytania

- Kto odpowiada end-to-end za ten strumień wartości?
- Czy zmiana jednego modelu wymaga uzgodnienia z innym zespołem?
- Czy jeden zespół musi rozumieć implementację drugiego, aby dostarczyć własną zmianę?
- Gdzie ludzie czekają na decyzję, review, deployment lub dane innego zespołu?
- Czy ownership mieści się poznawczo w głowie zespołu?
- Czy zależność techniczna tworzy paraliż decyzyjny?
- Czy rozdzielenie modeli skraca pętlę feedbacku?

## Heurystyka

Dobra granica ogranicza jednocześnie propagację zmian w kodzie, konieczność synchronizacji zespołów oraz zakres wiedzy potrzebnej do podjęcia lokalnej decyzji.

Nie oznacza to mechanicznego kopiowania struktury organizacyjnej do kodu. Obie strony należy analizować jako jeden system społeczno-techniczny.

## Powiązania

- [[Unit of Change]]
- [[Connascence]]
- [[Feedback and Metrics Loop]]
- [[Behavior Before Nouns]]
