---
id: PMA-META-HOSTING-001
type: governance
publication_status: public
knowledge_status: peos-decision
lifecycle: active
peos_usable: false
tags: ["obsidian","github","hosting"]
source_ids: []
---

# Hosting i Obsidian

## Lokalny model

Katalog główny repozytorium jest vaultem Obsidiana.

content/ — publiczne syntezy.
private/ — lokalny research i materiały źródłowe, ignorowane przez Git.
dist/peos/ — publiczny machine-readable registry dla PEOS.

## GitHub

GitHub jest canonical source dla publicznej części PMA i jej historii.

Nie używamy Git jako live-syncu Obsidiana. Commit jest świadomą publikacją wersji wiedzy.

## Publiczny serwis

Docelowo publiczna warstwa może być renderowana jako digital garden przez Quartz/GitHub Pages. Warstwa prywatna nie uczestniczy w buildzie strony.

## Reguła

Publikacja ma być jawna i odwracalna: private by default, public by explicit opt-in.
