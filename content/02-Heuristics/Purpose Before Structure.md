---
id: PMA-H-PURPOSE-001
type: heuristic
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["purpose","value","customer","discovery","architecture"]
source_ids: ["DEVSTYLE-FULL-CORPUS-2026-10-03"]
---

# Purpose Before Structure

## Teza

Pytanie o strukturę powinno być poprzedzone pytaniem o **cel istnienia** modelu, modułu, procesu lub capability.

„Co to jest?” zwykle prowadzi do rzeczowników. „Po co to istnieje i co dzięki temu możemy osiągnąć?” częściej prowadzi do zachowań, odpowiedzialności i wartości.

## Pytania

- Dla kogo istnieje ten model?
- Jaką potrzebę obsługuje?
- Jaki efekt ma umożliwić?
- Jaką wartość dostarcza bezpośrednio lub pośrednio?
- Co przestanie być możliwe, gdy ten element zniknie?
- Czy nazwa modułu opisuje capability, czy tylko zbiór podobnych danych?

## Sygnał ostrzegawczy

Jeżeli granice wynikają głównie z rzeczowników typu User, Product, Document, Vehicle, ale trudno wskazać niezależny cel i zachowanie każdej części, podział może odzwierciedlać strukturę danych zamiast struktury problemu.

## Powiązania

- [[Behavior Before Nouns]]
- [[Problem Classification]]
- [[PMA Mental Loop]]
