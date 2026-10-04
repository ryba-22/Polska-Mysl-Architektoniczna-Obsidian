---
id: PMA-H-BEING-BEHAVING-BECOMING-001
type: heuristic
publication_status: public
knowledge_status: source-derived
lifecycle: candidate
peos_usable: true
tags: ["ddd","modeling","boundary","archetypes","lifecycle"]
source_ids: ["BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-MATERIALS"]
---

# Being, Behaving, Becoming

To trzy soczewki pomagające sprawdzić, **co właściwie próbujemy modelować**.

- **Being** — co istnieje: identity, role, relacje, struktury i rzeczy rozpoznawalne w domenie.
- **Behaving** — co robi i według jakich reguł: operacje, decyzje, invariants, policies i capabilities.
- **Becoming** — jak zmienia się w czasie: lifecycle, przejścia, pivotal events, historia i temporalność.

## Do czego służy

Triada pomaga rozplątać model, w którym jeden rzeczownik przypadkowo miesza strukturę, zachowanie i cykl życia.

Przykład: "uczestnictwo" może oznaczać relację osoby z usługą (**Being**), reguły dołączania i rezygnacji (**Behaving**) albo historię candidate → active → suspended → ended (**Becoming**). Nazwanie wszystkiego jedną encją nie usuwa tych trzech odpowiedzialności.

## Heurystyka

Nie twórz automatycznie trzech klas ani trzech Bounded Contexts. To narzędzie discovery, nie szablon implementacyjny.

Pytaj:
- czy identity pozostaje ta sama, gdy zmienia się zachowanie?
- czy reguła może ewoluować niezależnie od lifecycle?
- czy pivotal event zmienia znaczenie pojęcia?
- czy historia jest faktem domenowym, czy tylko technicznym audytem?

Powiązania: [[Pivotal Event]], [[Linguistic Boundary]], [[Model Alternatives]], [[Deep Model Quality]].
