---
id: PMA-H-ACTIONABLE-STATE-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ux","workflow","notification","decision","state"]
source_ids: ["MONETEO-FINTECH-RANKING-2026"]
---

# Actionable State

## Teza

Dobry system operacyjny nie kończy się na pokazaniu stanu. Powinien pomóc użytkownikowi zrozumieć **co ten stan oznacza i jaka decyzja jest teraz możliwa**.

## Kontrakt stanu

Dla istotnego statusu lub alertu pokaż:

1. Co się stało?
2. Dlaczego?
3. Jaki jest wpływ?
4. Co można zrobić teraz?
5. Co się stanie po wykonaniu akcji?

## Notifications

Notyfikacja powinna reprezentować intention/action, nie tylko channel payload.

Jedno zdarzenie lub potrzeba kontaktu może zasilać widok operatora, e-mail, SMS, portal i kolejkę pracy.

Kanał dostarczenia nie powinien definiować semantyki komunikatu.

## Antywzorzec

„Masz błąd”, „Saldo: 120”, „FAILED” lub „Wymaga uwagi” bez przyczyny i sensownej następnej akcji.

## Powiązania

- [[Recovery and Human Escalation]]
- [[Capability Card]]
- [[Socio-Technical Boundary]]
