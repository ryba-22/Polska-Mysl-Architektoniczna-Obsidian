# Polska Myśl Architektoniczna — PMA

PMA jest wersjonowanym grafem wiedzy o projektowaniu oprogramowania, DDD, modelowaniu domenowym, archetypach oprogramowania i AI-assisted product engineering.

## Publiczna wersja

Repozytorium: https://github.com/ryba-22/Polska-Mysl-Architektoniczna-Obsidian

GitHub Pages / Quartz: https://ryba-22.github.io/Polska-Mysl-Architektoniczna-Obsidian/

## Model działania

- Obsidian jest lokalnym IDE wiedzy.
- GitHub przechowuje wyłącznie jawnie publiczną warstwę wiedzy.
- private/ zawiera lokalne materiały źródłowe, transkrypcje, slajdy, research dumps i opracowania wymagające ostrożności licencyjnej. Ten katalog jest ignorowany przez Git.
- content/ zawiera autorskie syntezy PMA przeznaczone do publikacji.
- dist/peos/ jest maszynowym indeksem publicznej wiedzy dla Product Engineering OS / AI Brain.
- Quartz 5 renderuje publiczny digital garden z content/ przez GitHub Actions.

## Zasada publikacji

Raw source private, synthesis public.

Każda publiczna notatka ma publication_status: public. Warstwa prywatna nigdy nie jest publikowana.

## Vault

Otwórz katalog główny repozytorium jako vault Obsidiana. content/ i private/ są wtedy widoczne w jednym środowisku, ale Git śledzi wyłącznie część publiczną.

Start: [[content/00-Start/Start Here]]

## Walidacja

Uruchom:

    make validate

Bramki sprawdzają publication boundary, wikilinki oraz świeżość wygenerowanego registry dla PEOS.
