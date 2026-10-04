---
id: PMA-H-ARCHETYPE-FUNNEL-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["archetypes","ddd","problem-classification","modeling","falsification"]
source_ids: ["BOTTEGA-DDD-CATALOG","BOTTEGA-DDD-MATERIALS","SOFTWARE-ARCHETYPES"]
---

# Archetype Discovery Funnel

Archetyp nie powinien być wybierany przez podobieństwo nazwy. Najpierw trzeba rozpoznać klasę problemu.

## Funnel

evidence
→ problem i główne pytanie
→ destylacja części generycznej
→ candidate archetype
→ kontrast z sąsiednimi archetypami
→ disconfirming evidence
→ wybór tylko potrzebnych elementów
→ kompozycja z wiedzą specyficzną dla domeny
→ test na scenariuszach i kontrprzykładach.

## Heurystyka

Jeżeli po znalezieniu archetypu przestajesz pytać, archetyp stał się dogmatem.

Dobry archetyp:
- kompresuje kilka pozornie osobnych przypadków;
- ujawnia znane invariants i failure modes;
- daje nowe pytania do eksperta;
- nie usuwa wiedzy specyficznej dla domeny;
- można go odrzucić, gdy scenariusze nie pasują.

## Antywzorzec

**mamy Product → wdrażamy cały model Product**

Archetyp jest hipotezą o strukturze problemu, nie paczką klas do skopiowania.

Repo referencyjne: Domain Archetype Atlas (wyspecjalizowany katalog archetypów i kontrastów).

Powiązania: [[Distillation]], [[Problem Classification]], [[Model Alternatives]], [[Deep Model Quality]].
