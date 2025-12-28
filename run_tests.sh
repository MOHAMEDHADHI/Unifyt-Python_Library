#!/bin/bash
# Run tests with langsmith plugin disabled

# Disable langsmith plugin via environment variable
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1

# Run pytest with explicit plugin disabling
python -m pytest tests/ -v -p no:langsmith -p no:pytest_langsmith "$@"
