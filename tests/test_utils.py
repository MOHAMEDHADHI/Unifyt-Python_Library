"""Tests for utility functions."""

import pytest
import numpy as np
from unifyt import Quantity, utils


class TestArrayCreation:
    """Test array creation utilities."""
    
    def test_linspace(self):
        """Test linspace function."""
        result = utils.linspace(Quantity(0, 'meter'), Quantity(10, 'meter'), 11)
        assert len(result.magnitude) == 11
        assert result.magnitude[0] == 0
        assert result.magnitude[-1] == 10
    
    def test_arange(self):
        """Test arange function."""
        result = utils.arange(Quantity(0, 'meter'), Quantity(10, 'meter'), 
                             Quantity(2, 'meter'))
        expected = np.array([0, 2, 4, 6, 8])
        assert np.allclose(result.magnitude, expected)
    
    def test_zeros(self):
        """Test zeros function."""
        result = utils.zeros(5, 'meter')
        assert len(result.magnitude) == 5
        assert np.all(result.magnitude == 0)
    
    def test_ones(self):
        """Test ones function."""
        result = utils.ones((2, 3), 'meter')
        assert result.magnitude.shape == (2, 3)
        assert np.all(result.magnitude == 1)
    
    def test_full(self):
        """Test full function."""
        result = utils.full(4, Quantity(5, 'meter'))
        assert len(result.magnitude) == 4
        assert np.all(result.magnitude == 5)


class TestArrayOperations:
    """Test array operations."""
    
    def test_concatenate(self):
        """Test concatenate function."""
        q1 = Quantity(np.array([1, 2]), 'meter')
        q2 = Quantity(np.array([3, 4]), 'meter')
        result = utils.concatenate([q1, q2])
        expected = np.array([1, 2, 3, 4])
        assert np.allclose(result.magnitude, expected)
    
    def test_stack(self):
        """Test stack function."""
        q1 = Quantity(np.array([1, 2]), 'meter')
        q2 = Quantity(np.array([3, 4]), 'meter')
        result = utils.stack([q1, q2])
        assert result.magnitude.shape == (2, 2)


class TestStatisticalFunctions:
    """Test statistical functions."""
    
    def test_sum(self):
        """Test sum function."""
        q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        result = utils.sum(q)
        assert result.magnitude == 10
    
    def test_mean(self):
        """Test mean function."""
        q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        result = utils.mean(q)
        assert result.magnitude == 2.5
    
    def test_std(self):
        """Test std function."""
        q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        result = utils.std(q)
        assert result.magnitude > 0
    
    def test_min(self):
        """Test min function."""
        q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        result = utils.min(q)
        assert result.magnitude == 1
    
    def test_max(self):
        """Test max function."""
        q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        result = utils.max(q)
        assert result.magnitude == 4


class TestMathFunctions:
    """Test mathematical functions."""
    
    def test_sqrt(self):
        """Test sqrt function."""
        q = Quantity(25, 'meter^2')
        result = utils.sqrt(q)
        assert abs(result.magnitude - 5) < 1e-10
    
    def test_clip(self):
        """Test clip function."""
        q = Quantity(np.array([1, 5, 10]), 'meter')
        result = utils.clip(q, Quantity(2, 'meter'), Quantity(8, 'meter'))
        expected = np.array([2, 5, 8])
        assert np.allclose(result.magnitude, expected)
    
    def test_isclose(self):
        """Test isclose function."""
        q1 = Quantity(1.0, 'meter')
        q2 = Quantity(1.0000001, 'meter')
        assert utils.isclose(q1, q2)
        
        q3 = Quantity(2.0, 'meter')
        assert not utils.isclose(q1, q3)
