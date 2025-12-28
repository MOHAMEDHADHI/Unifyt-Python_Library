#!/usr/bin/env python3
"""Run tests with langsmith plugin disabled."""

import sys
import os

# Disable langsmith plugin before importing pytest
os.environ['PYTEST_DISABLE_PLUGIN_AUTOLOAD'] = '1'

# Now import and run pytest
import pytest

if __name__ == '__main__':
    # Run pytest with langsmith disabled
    args = [
        'tests/',
        '-v',
        '-p', 'no:langsmith',
        '--tb=short',
    ] + sys.argv[1:]  # Add any additional arguments
    
    sys.exit(pytest.main(args))
