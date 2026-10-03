PYTHON ?= python3

.PHONY: build validate

build:
	$(PYTHON) scripts/build_peos_registry.py

validate: build
	$(PYTHON) scripts/validate_publication.py
	$(PYTHON) scripts/validate_links.py
	git diff --exit-code -- dist/peos
