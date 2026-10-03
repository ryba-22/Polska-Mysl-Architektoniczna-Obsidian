---
id: PMA-H-ALTERNATIVE-FLOW-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","process","boundary","event-storming"]
source_ids: ["DOMAIN-DRIVERS-COURSE"]
---

# Alternative Process Flow

Rozgałęzienie procesu jest sygnałem do zbadania źródła różnicy, nie automatyczną granicą modelu.

## Pytania

Gdy proces rozdziela się na alternatywne ścieżki, sprawdź czy różnią się:
- regułami;
- językiem;
- potrzebnymi informacjami;
- właścicielem decyzji;
- cyklem życia;
- wymaganiami dotyczącymi spójności.

Jeżeli kilka z tych różnic występuje razem, alternatywny flow może wskazywać osobny model lub capability.

## Antyheurystyka

Sama instrukcja warunkowa albo inny ekran nie uzasadnia osobnego bounded contextu.

Zobacz [[Pivotal Event]] i [[Main Question]].
