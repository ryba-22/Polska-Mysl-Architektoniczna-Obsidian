---
id: PMA-CONCEPT-CONSISTENCY-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ddd","aggregate","consistency","concurrency"]
source_ids: ["DOMAIN-DRIVERS-COURSE","DOMAIN-DRIVERS-DD-JAVA","BSLOTA"]
---

# Consistency Boundary

Consistency boundary to najmniejsza jednostka stanu, która musi pozostać poprawna atomowo dla konkretnego zestawu invariantów.

Nie należy jej wyznaczać na podstawie podobieństwa danych albo relacji encji.

## Pytania

- jakie reguły muszą być prawdziwe po każdej komendzie?
- które komendy mogą wystąpić równocześnie?
- jaki stan jest potrzebny, aby odpowiedzieć czy operacja jest dozwolona?
- co musi zmienić się w jednej transakcji?
- czy rozdzielenie zmiany wymaga corrective policy?

[[Unit of Change]] jest heurystyką prowadzącą do tej granicy.

Aggregate jest jednym z możliwych sposobów implementacji tej granicy, a nie punktem startowym modelowania.
