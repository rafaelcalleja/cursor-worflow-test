# Makefile for common project tasks

# Variables
PYTHON_INTERPRETER = .venv/bin/python
PYTEST = .venv/bin/pytest

# Default target (optional)
.DEFAULT_GOAL := help

# Targets
.PHONY: test
test:
	@echo "Running Python tests..."
	@$(PYTEST)

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  test    - Run the Python test suite using pytest" 