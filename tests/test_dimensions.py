"""Tests for Dimension class."""

import pytest
from unifyt.dimensions import Dimension


class TestDimensionCreation:
    """Test dimension creation."""
    
    def test_create_length_dimension(self):
        """Test creating length dimension."""
        dim = Dimension(length=1)
        assert dim.length == 1
        assert dim.mass == 0
    
    def test_create_velocity_dimension(self):
        """Test creating velocity dimension."""
        dim = Dimension(length=1, time=-1)
        assert dim.length == 1
        assert dim.time == -1


class TestDimensionArithmetic:
    """Test dimension arithmetic."""
    
    def test_dimension_addition(self):
        """Test adding dimensions."""
        d1 = Dimension(length=1)
        d2 = Dimension(time=-1)
        result = d1 + d2
        assert result.length == 1
        assert result.time == -1
    
    def test_dimension_subtraction(self):
        """Test subtracting dimensions."""
        d1 = Dimension(length=1, time=-1)
        d2 = Dimension(time=-1)
        result = d1 - d2
        assert result.length == 1
        assert result.time == 0
    
    def test_dimension_multiplication(self):
        """Test multiplying dimension by scalar."""
        dim = Dimension(length=1, time=-1)
        result = dim * 2
        assert result.length == 2
        assert result.time == -2


class TestDimensionEquality:
    """Test dimension equality."""
    
    def test_equal_dimensions(self):
        """Test that equal dimensions are recognized."""
        d1 = Dimension(length=1, mass=1)
        d2 = Dimension(length=1, mass=1)
        assert d1 == d2
    
    def test_unequal_dimensions(self):
        """Test that unequal dimensions are recognized."""
        d1 = Dimension(length=1)
        d2 = Dimension(mass=1)
        assert d1 != d2
    
    def test_dimensionless(self):
        """Test dimensionless dimension."""
        d1 = Dimension()
        d2 = Dimension()
        assert d1 == d2
