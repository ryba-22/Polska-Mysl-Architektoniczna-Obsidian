---
id: PMA-H-PROBLEM-CLASS-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["problem-classification","ddd","architecture"]
source_ids: ["DOMAIN-DRIVERS-DD-AI","DOMAIN-DRIVERS-COURSE","DDD-BY-EXAMPLES-LIBRARY"]
---

# Problem Classification

Pattern selection bez wcześniejszej klasyfikacji problemu jest błędem procesu.

## Podstawowe klasy

### CRUD
Operacja zapisuje lub odczytuje dane, a reguły nie zależą od współbieżnie zmieniającego się stanu.

Sygnał: Command i Event są często tym samym czasownikiem w trybie rozkazującym i czasie przeszłym, a reguł biznesowych jest niewiele.

### Transformation and Presentation
Operacja nie zmienia Source of Truth. Czyta, oblicza, grupuje albo projektuje.

Test: gdyby skasować ten model i odbudować go z innych danych, czy utracilibyśmy informację? Jeżeli nie, prawdopodobnie jest projekcją.

### Integration
Problem dotyczy współpracy autonomicznych modeli lub systemów: kontraktów, kolejności, partial failure, retry i tłumaczenia znaczeń.

### Resource Contention
Decyzja czy można wykonać operację zależy od mutable state, który inna komenda może zmienić w tym samym czasie.

## Następny krok

Po klasyfikacji uruchom [[Pattern vs Archetype vs Algorithm]] i dopiero potem dobieraj architekturę.
