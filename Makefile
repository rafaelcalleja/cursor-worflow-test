# Makefile for common project tasks

# Variables
PYTHON_INTERPRETER = .venv/bin/python
PIP = .venv/bin/pip
PYTEST = .venv/bin/pytest

# Default target (optional)
.DEFAULT_GOAL := help

# Targets
.PHONY: install
install:
	@echo "Installing/updating dependencies..."
	@$(PIP) install -r requirements.txt

.PHONY: test
test: install # Ensure dependencies are installed before testing
	@echo "Running Python tests..."
	@$(PYTEST)

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install - Install Python dependencies from requirements.txt"
	@echo "  test    - Run the Python test suite using pytest (installs deps first)" 