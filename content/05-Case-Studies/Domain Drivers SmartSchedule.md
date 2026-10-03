---
id: PMA-CASE-SMARTSCHEDULE-001
type: case-study
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["domain-drivers","ddd","smartschedule","case-study"]
source_ids: ["DOMAIN-DRIVERS-ORG","DOMAIN-DRIVERS-DD-JAVA","DOMAIN-DRIVERS-DD-AI"]
---

# Domain Drivers — SmartSchedule

SmartSchedule jest wielojęzykowym laboratorium pokazującym, że różne części systemu mogą wymagać różnych modeli i klas problemów.

## Obserwowane modele

- planning;
- availability;
- allocation;
- optimization;
- risk;
- simulation;
- resource;
- capability scheduling;
- cashflow.

## Wnioski

Availability chroni mutable state i jest miejscem naturalnej analizy concurrency.

Optimization może być klasycznym problemem algorytmicznym, a nie agregatem.

Risk może wymagać długotrwałej koordynacji procesu.

Granice modułów są egzekwowane testami architektury, więc Context Map nie kończy się jako diagram.

Pięć implementacji językowych pokazuje rozdział modelu domenowego od idiomów frameworka i języka.
