---
id: PMA-H-TEMPORAL-SCALE-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["time","scale","volatility","architecture-drivers","change"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE"]
---

# Temporal Scale and Volatility Lens

## Teza

Model, który wygląda dobrze przy dzisiejszym stanie, może być błędny po zmianie **czasu, skali lub częstości zmian**.

## Czas

- Czy kolejność operacji ma znaczenie biznesowe?
- Jak długo decyzja pozostaje ważna?
- Czy istnieje deadline, okno czasowe lub expiration?
- Czy późniejszy fakt może zmienić interpretację wcześniejszego?
- Czy istnieje punkt, po którym operacja jest ekonomicznie lub fizycznie nieodwracalna?

## Skala

- Co dzieje się przy x10 operacji?
- Czy proporcja odczytów do zapisów się zmienia?
- Czy ruch jest równomierny, czy sezonowy?
- Czy wzrost liczby zespołów zwiększa liczbę zależności szybciej niż liniowo?

## Zmienność

- Co zmienia się często?
- Co jest stabilnym rdzeniem?
- Czy jeden model łączy elementy o bardzo różnej zmienności?
- Czy częsta zmiana jednego elementu wymusza deployment lub uzgodnienia w niezależnym obszarze?

## Powiązania

- [[Architecture Drivers]]
- [[Unit of Change]]
- [[Scenario Before Aggregate]]
- [[PMA Mental Loop]]
