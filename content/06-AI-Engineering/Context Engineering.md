---
id: PMA-AI-CONTEXT-001
type: concept
publication_status: public
knowledge_status: synthesis
lifecycle: verified
peos_usable: true
tags: ["ai","context-engineering","memory"]
source_ids: ["AI-THAT-WORKS","BOTTEGA-DDD-CATALOG"]
---

# Context Engineering

Prompt, RAG, pamięć, historia i wyniki narzędzi są jednym problemem: jak złożyć właściwy kontekst wejściowy dla modelu.

## Zasady

- nie każ agentowi pamiętać wszystkiego;
- dane zawsze potrzebne pobieraj deterministycznie;
- state i memory mogą żyć w wyspecjalizowanych narzędziach;
- deterministyczne problemy rozwiązuj kodem, nie promptem;
- projekt memory zaczyna się od konkretnego user experience, nie od wyboru vector database.

## Decaying Resolution Memory

Świeże informacje mogą pozostać szczegółowe, a starsze być kompresowane do wyższego poziomu abstrakcji.

Dla PEOS oznacza to oddzielenie trwałej wiedzy PMA od krótkotrwałego run state.
