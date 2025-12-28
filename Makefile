# Makefile for Unifyt development

.PHONY: help install install-dev test test-cov clean format lint check examples docs validate all

help:
	@echo "Unifyt Development Commands:"
	@echo ""
	@echo "  make install      - Install package"
	@echo "  make install-dev  - Install with development dependencies"
	@echo "  make test         - Run tests"
	@echo "  make test-cov     - Run tests with coverage"
	@echo "  make clean        - Remove temporary files"
	@echo "  make format       - Format code with black and isort"
	@echo "  make lint         - Run linters (flake8, mypy)"
	@echo "  make check        - Run all code quality checks"
	@echo "  make examples     - Run all examples"
	@echo "  make validate     - Validate project structure"
	@echo "  make all          - Run format, lint, test"
	@echo ""

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=unifyt --cov-report=html --cov-report=term

clean:
	@echo "Cleaning temporary files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name "*.pyd" -delete 2>/dev/null || true
	@rm -rf .pytest_cache .coverage htmlcov 2>/dev/null || true
	@rm -rf build dist *.egg-info .eggs 2>/dev/null || true
	@rm -rf .mypy_cache 2>/dev/null || true
	@find . -type f -name "*~" -delete 2>/dev/null || true
	@find . -type f -name "*.swp" -delete 2>/dev/null || true
	@find . -type f -name ".DS_Store" -delete 2>/dev/null || true
	@echo "Cleanup complete!"

format:
	@echo "Formatting code..."
	black unifyt/ tests/ examples/
	isort unifyt/ tests/ examples/
	@echo "Formatting complete!"

lint:
	@echo "Running linters..."
	flake8 unifyt/ --max-line-length=100 --extend-ignore=E203,W503
	mypy unifyt/ --ignore-missing-imports
	@echo "Linting complete!"

check: format lint test
	@echo "All checks passed!"

examples:
	@echo "Running examples..."
	@python examples/basic_usage.py
	@python examples/scientific_calculations.py
	@python examples/custom_units.py
	@python examples/array_operations.py
	@python examples/advanced_features.py
	@python examples/complete_demo.py
	@echo "Examples complete!"

validate:
	@bash validate.sh

all: format lint test
	@echo "All tasks complete!"

.DEFAULT_GOAL := help
