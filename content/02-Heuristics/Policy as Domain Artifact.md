---
id: PMA-H-POLICY-ARTIFACT-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["policy","rules","governance","domain","decision"]
source_ids: ["FINTECH-POLAND-ECOSYSTEM"]
---

# Policy as Domain Artifact

## Teza

Reguła, która wpływa na decyzję biznesową, recovery, retry, rozliczenie lub uprawnienie, nie powinna istnieć wyłącznie jako anonimowy if w kodzie.

## Minimalny kontrakt policy

- Name — jak nazywa ją domena?
- Purpose — jaki problem kontroluje?
- Owner — kto odpowiada za regułę?
- Inputs — jakiej informacji potrzebuje?
- Decision — co rozstrzyga?
- Effective from / to — kiedy obowiązuje?
- Exceptions — jakie ma wyjątki?
- Evidence / source — skąd wynika?
- Version — czy zmiana policy jest śledzona?

## Pytania

- Czy ta reguła jest konfiguracją techniczną, czy decyzją biznesową?
- Kto może ją zmienić?
- Jak zmiana wpływa na historyczne decyzje?
- Czy system potrafi wyjaśnić, według której wersji policy podjął decyzję?

## Powiązania

- [[Evidence Contract]]
- [[Corrections Over Historical Mutation]]
- [[Recovery and Human Escalation]]
- [[Decision Gate]]
