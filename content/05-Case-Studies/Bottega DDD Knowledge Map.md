---
id: PMA-CASE-BOTTEGA-DDD-001
type: case-study
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["bottega","ddd","event-storming","archetypes","source-map"]
source_ids: ["BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-MATERIALS","BOTTEGA-DDD-ARTICLES","BOTTEGA-DDD-PUBLIC-TALKS"]
---

# Bottega DDD Knowledge Map

Research pass: 2026-10-04.

Źródła Bottegi tworzą spójny ciąg od discovery do implementacji, ale nie są jednym poziomem wiedzy. Warto je rozdzielać na siedem warstw.

## 1. Discovery i strategic DDD

Event Storming, subdomains, Core/Supporting/Generic, Bounded Context, Context Map, destylacja, ownership i autonomia.

Nowe lub wzmocnione w PMA: [[SSOT and SPOF Boundary Heuristic]], [[Architecture Abstraction Ladder]], [[Clean Questions for Domain Discovery]].

## 2. Taktyczne modelowanie

Aggregates, invariants, policies, lifecycle, concurrency i granice transakcji.

W PMA istniało już: [[Aggregate Sizing]], [[Unit of Change]], [[Consistency Boundary]].

## 3. Archetypy modeli biznesowych

Party/Role/Relationship, Product/Catalog/Inventory, Availability, dokumenty, reguły/scoring, account/wallet i kolejne powtarzalne struktury.

Najważniejszy wniosek: archetyp jest narzędziem rozpoznania klasy problemu, nie gotowym projektem. Zobacz [[Archetype Discovery Funnel]] i osobny Domain Archetype Atlas.

## 4. Temporalność i proces

Pivotal Events, Saga/Process Manager, reguły zależne od sekwencji zdarzeń, time-varying rules oraz [[Being Behaving Becoming]].

## 5. Architektura i integracja

Command ≠ Event ≠ Query, CQRS, eventual consistency, Outbox/Inbox, idempotency, ordering, Ports & Adapters i failure modes.

W PMA większość tej warstwy była już obecna; Bottega jest dodatkowym provenance, nie powodem do dublowania notatek.

## 6. Modelowanie jako proces uczenia

Starsza seria "DDD krok po kroku" pokazuje [[Modeling Whirlpool]], Ubiquitous Language i wykonywalne specyfikacje. Nowsze materiały przesuwają nacisk z katalogu Building Blocks na heurystyki granic, archetypy, evidence i konsekwencje decyzji.

## 7. AI-assisted engineering i legacy

Nowsze programy łączą modularność z ograniczaniem kontekstu dla LLM oraz refaktoryzację legacy z change vectors, historią Git, hotspotami i Event Storming As-Is/To-Be.

To powinno zasilać proces PEOS dopiero po syntezie i walidacji w PMA, a nie przez kopiowanie materiałów szkoleniowych.

## Granica publikacji

Publiczna PMA przechowuje autorską syntezę i provenance. PDF-y, napisy i robocze ekstrakcje pozostają w prywatnym archiwum źródeł.
