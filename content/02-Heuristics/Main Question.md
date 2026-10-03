---
id: PMA-H-MAIN-QUESTION-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","model-boundaries","strategic-design"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DEVSTYLE-DDD-EMAIL-CORPUS"]
---

# Main Question

Model powinien mieć jasny cel decyzyjny: na jakie główne pytanie biznesowe odpowiada?

## Heurystyka

Dla kandydata na model zapytaj:
- jakie pytanie ma rozstrzygać;
- jakich faktów potrzebuje do odpowiedzi;
- kto jest właścicielem tych faktów;
- jakie reguły wpływają na odpowiedź;
- czy może odpowiedzieć bez zaglądania do wielu obcych modeli.

Jeżeli dwa fragmenty systemu odpowiadają na różne główne pytania, mogą wymagać różnych modeli nawet wtedy, gdy operują na podobnych danych.

## Przykład strukturalny

"czy zasób jest dostępny?" i "jak najlepiej wykorzystać dostępne zasoby?" dotyczą tych samych zasobów, ale prowadzą odpowiednio w stronę [[Availability]] i optymalizacji.

## PEOS

Main Question jest jednym z wejść do [[Problem Classification]] i boundary discovery.
