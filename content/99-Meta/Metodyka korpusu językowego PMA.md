---
id: PMA-META-LANGUAGE-CORPUS-001
type: governance
publication_status: public
knowledge_status: synthesis
lifecycle: active
peos_usable: false
tags: ["provenance","language","corpus","methodology"]
source_ids: ["PMA-LANGUAGE-CORPUS-2026-10-03","DOMAIN-DRIVERS-COURSE","DEVSTYLE-DEVTALK","BETTER-SOFTWARE-DESIGN","DDD-WAW-VIDEOS"]
---

# Metodyka korpusu językowego PMA

## Cel

Korpus służy do badania sposobu formułowania problemów, pytań, hipotez i decyzji w polskiej praktyce DDD oraz architektury oprogramowania.

Nie służy do publikowania transkrypcji.

## Stan 2026-10-03

Pierwszy public-source run objął 35 unikalnych nagrań z dostępnymi napisami, około 328 tys. słów i około 2 mln znaków tekstu.

W korpusie znalazły się m.in. materiały i rozmowy z udziałem:
- Sławomira Sobótki;
- Jakuba Pilimona;
- Bartka Słoty;
- Łukasza Szydły;
- Marcina Markowskiego;
- Oskara Dudycza;
- Mariusza Gila;
- Macieja Aniserowicza;
- Macieja Jędrzejewskiego.

Źródła obejmowały publiczne nagrania Domain Drivers / DevStyle / DevTalk, Better Software Design, DDD WAW oraz konferencje i meetupy.

## Pipeline

1. Znalezienie publicznego nagrania.
2. Sprawdzenie dostępności napisów.
3. Pobranie napisów wyłącznie do lokalnej warstwy research.
4. Usunięcie timestampów, duplikatów rolling captions i znaczników technicznych.
5. Analiza częstości pojęć i konstrukcji językowych.
6. Close reading wybranych fragmentów.
7. Normalizacja do autorskich pytań i sformułowań PMA.
8. Publikacja wyłącznie syntezy.

## Ograniczenia

- napisy automatyczne mogą zawierać błędy;
- częstotliwość słowa nie jest sama w sobie dowodem znaczenia;
- mówcy zmieniają sposób wypowiedzi zależnie od formatu;
- wypowiedzi z LIVE, wykładu i podcastu nie są bezpośrednio porównywalne;
- konstrukcje publikowane w PMA są parafrazą i normalizacją, nie cytatem.

## Bramka licencyjna

Pełne VTT/SRT, research dumpy i close reading pozostają poza repozytorium publicznym zgodnie z [[Publication Policy|Polityka publikacji PMA]].

Publiczne są:
- statystyki zagregowane;
- autorskie syntezy;
- autorskie heurystyki;
- bibliografia i identyfikacja źródeł.

## Powiązania

- [[Język polskiej myśli architektonicznej]]
- [[PMA Language Contract]]
- [[Source Provenance|Pochodzenie wiedzy]]
- [[Publication Policy|Polityka publikacji PMA]]
