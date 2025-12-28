"""Pytest configuration and fixtures."""

import pytest
import numpy as np


@pytest.fixture
def sample_array():
    """Provide a sample numpy array for testing."""
    return np.array([1, 2, 3, 4, 5])


@pytest.fixture
def tolerance():
    """Provide default tolerance for floating point comparisons."""
    return 1e-10
