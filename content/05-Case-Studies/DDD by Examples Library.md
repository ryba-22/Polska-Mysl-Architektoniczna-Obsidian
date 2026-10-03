---
id: PMA-CASE-LIBRARY-001
type: case-study
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","event-storming","library","case-study"]
source_ids: ["DDD-BY-EXAMPLES-LIBRARY"]
---

# DDD by Examples — Library

Repozytorium pokazuje przejście od problemu biznesowego do kodu bez rozpoczynania od tactical patterns.

## Ścieżka

Big Picture Event Storming
→ Ubiquitous Language
→ Example Mapping
→ Design Level Event Storming
→ scenarios and business rules
→ bounded contexts
→ local architecture
→ implementation.

## Heurystyki

### Linguistic boundary
Book w catalogue i Book w lending mają inne znaczenie, reguły i lifecycle. To sygnał dwóch modeli.

### CRUD detector
Jeżeli większość eventów jest prostą przeszłą formą odpowiadającej komendy, a business rules są nieliczne, kontekst może być CRUD-em.

### Local architecture
Lending ma istotną złożoność i bogatszy model. Catalogue jest prostszy i nie potrzebuje tej samej architektury.

### Aggregate discovery
Najpierw zachowania i odpowiedzialności. Agregaty nie są oznaczane na początku Design Level.
