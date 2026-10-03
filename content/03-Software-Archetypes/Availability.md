---
id: PMA-ARCHETYPE-AVAILABILITY-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["availability","reservation","resource-contention"]
source_ids: ["SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA","DOMAIN-DRIVERS-DD-JAVA"]
---

# Availability

Archetyp Availability odpowiada na pytanie: czy określony zasób może zostać użyty przez danego właściciela w określonym czasie i na jakich warunkach.

## Recognition questions

- czy istnieje zasób o ograniczonej dostępności?
- czy kilka stron może chcieć go jednocześnie?
- czy dostępność zależy od przedziału czasu?
- czy zasób może być niedostępny z wielu przyczyn?
- czy lock ma właściciela albo czas wygaśnięcia?
- czy występują pule zasobów zamiast konkretnych egzemplarzy?

## Typowe warianty

individual, pooled, temporal, grouped.

## Ryzyka

- double booking;
- stale state;
- zbyt duży aggregate;
- mieszanie opisowych danych zasobu z logiką dostępności.

Powiązania: [[Unit of Change]], [[Concurrency and Stale State]], [[Waitlist]].
