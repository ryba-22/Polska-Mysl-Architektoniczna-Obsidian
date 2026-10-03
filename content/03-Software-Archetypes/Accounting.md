---
id: PMA-ARCHETYPE-ACCOUNTING-001
type: software-archetype
publication_status: public
knowledge_status: synthesis
lifecycle: candidate
peos_usable: true
tags: ["accounting","transactions","ledger"]
source_ids: ["SOFTWARE-ARCHETYPES","ARCHETYPY-OPROGRAMOWANIA"]
---

# Accounting

Accounting reprezentuje transfer wartości jako transakcje i wpisy na kontach, zamiast mutowania pojedynczego pola balance bez historii.

## Recognition questions

- czy trzeba wyjaśnić skąd wzięło się saldo?
- czy operacja powinna być odwracalna przez reversal zamiast edycji historii?
- czy jedna transakcja wpływa na kilka kont lub kategorii?
- czy potrzebny jest audit trail i rekonstrukcja?

## Heurystyka

Jeżeli najważniejsze pytanie brzmi nie tylko ile mamy, ale dlaczego mamy właśnie tyle, model wpisów i transakcji może być lepszy niż mutable balance.

Nie oznacza to automatycznie Event Sourcing.
