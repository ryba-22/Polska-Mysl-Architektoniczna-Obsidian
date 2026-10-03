---
id: PMA-FAIL-RECOVERY-ESCALATION-001
type: failure-pattern
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["failure","recovery","retry","human-escalation","integration"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE"]
---

# Recovery and Human Escalation

## Problem

Retry, timeout i eskalacja bywają traktowane jak czysto techniczne ustawienia. W wielu procesach określają jednak zachowanie biznesowe.

Pytanie „ile razy ponowić?” może być równocześnie pytaniem: jak długo biznes akceptuje niespójność, kiedy operacja przestaje mieć wartość, kiedy potrzebna jest ręczna interwencja i kto odpowiada za stan po częściowej awarii.

## Pytania

- Czy wszystkie kroki naprawdę muszą zakończyć się sukcesem razem?
- Co biznesowo oznacza „razem”?
- Czy kolejność ma znaczenie?
- Czy retry jest bezpieczny i idempotentny?
- Ile czasu możemy tolerować niespójność?
- Kiedy przestajemy automatycznie próbować?
- Komu i z jaką informacją eskalujemy problem?
- Jak człowiek może bezpiecznie wznowić lub skorygować proces?
- Jak odróżniamy transient failure od stanu wymagającego decyzji biznesowej?

## Failure pattern

Automatyczny retry bez jawnej polityki może powielać efekt, przedłużać niespójność, ukrywać problem operacyjny albo wykonywać po czasie operację, która utraciła sens biznesowy.

## Powiązania

- [[Event Driven Failure Patterns]]
- [[Transactional Outbox Atomicity]]
- [[Problem Classification]]
- [[PMA Mental Loop]]
