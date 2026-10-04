---
id: PMA-H-PIVOTAL-EVENT-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","event-storming","boundary","lifecycle"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DEVSTYLE-DDD-EMAIL-CORPUS","BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-PUBLIC-TALKS"]
---

# Pivotal Event

Pivotal Event to zdarzenie, po którym historia biznesowa zaczyna działać według innego zestawu reguł lub znaczeń.

## Sygnały

Po zdarzeniu może zmienić się:
- znaczenie pojęcia;
- odpowiedzialny aktor;
- owner decyzji;
- lifecycle;
- zestaw dozwolonych operacji;
- grupa procesów reagujących na fakt.

## Heurystyka

Nie pytaj tylko "czy event jest ważny?". Pytaj "czy po nim zmienia się model potrzebny do rozumienia następnej części procesu?".

Pivotal event jest kandydatem na granicę, którą trzeba zweryfikować scenariuszami i [[Linguistic Boundary]].
