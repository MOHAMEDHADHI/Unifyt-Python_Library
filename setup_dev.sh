#!/bin/bash
# Development environment setup script

echo "=== Setting up Unifyt Development Environment ==="
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install package in editable mode with dev dependencies
echo "Installing Unifyt in development mode..."
pip install -e ".[dev]"

echo ""
echo "=== Setup Complete ==="
echo "Virtual environment created and activated."
echo "To activate in the future, run: source venv/bin/activate"
echo ""
echo "Available commands:"
echo "  ./run_tests.sh       - Run test suite"
echo "  ./run_examples.sh    - Run all examples"
echo "  ./check_code.sh      - Run code quality checks"
