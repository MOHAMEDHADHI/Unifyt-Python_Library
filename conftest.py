"""Root conftest.py to configure pytest for the entire project."""

import sys
import os

# Disable langsmith plugin before pytest loads it
os.environ['PYTEST_DISABLE_PLUGIN_AUTOLOAD'] = '1'

# This file is in the root directory and will be loaded first by pytest
