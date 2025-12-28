"""Tests for Quantity class."""

import pytest
import numpy as np
from unifyt import Quantity, Unit


class TestQuantityCreation:
    """Test quantity creation."""
    
    def test_create_with_string_unit(self):
        """Test creating quantity with string unit."""
        q = Quantity(100, 'meter')
        assert q.magnitude == 100
        assert str(q.unit) == 'meter'
    
    def test_create_with_unit_object(self):
        """Test creating quantity with Unit object."""
        unit = Unit('meter')
        q = Quantity(100, unit)
        assert q.magnitude == 100
    
    def test_create_with_array(self):
        """Test creating quantity with numpy array."""
        arr = np.array([1, 2, 3])
        q = Quantity(arr, 'meter')
        assert np.array_equal(q.magnitude, arr)


class TestQuantityConversion:
    """Test unit conversions."""
    
    def test_length_conversion(self):
        """Test length unit conversion."""
        q = Quantity(1000, 'meter')
        q_km = q.to('kilometer')
        assert q_km.magnitude == 1.0
    
    def test_time_conversion(self):
        """Test time unit conversion."""
        q = Quantity(60, 'second')
        q_min = q.to('minute')
        assert q_min.magnitude == 1.0
    
    def test_incompatible_conversion(self):
        """Test that incompatible conversions raise error."""
        q = Quantity(100, 'meter')
        with pytest.raises(ValueError):
            q.to('second')


class TestQuantityArithmetic:
    """Test arithmetic operations."""
    
    def test_addition(self):
        """Test adding quantities."""
        q1 = Quantity(100, 'meter')
        q2 = Quantity(50, 'meter')
        result = q1 + q2
        assert result.magnitude == 150
    
    def test_addition_with_conversion(self):
        """Test adding quantities with different units."""
        q1 = Quantity(1, 'kilometer')
        q2 = Quantity(500, 'meter')
        result = q1 + q2
        assert result.magnitude == 1.5
    
    def test_subtraction(self):
        """Test subtracting quantities."""
        q1 = Quantity(100, 'meter')
        q2 = Quantity(30, 'meter')
        result = q1 - q2
        assert result.magnitude == 70
    
    def test_multiplication(self):
        """Test multiplying quantities."""
        q1 = Quantity(10, 'meter')
        q2 = Quantity(5, 'meter')
        result = q1 * q2
        assert result.magnitude == 50
    
    def test_division(self):
        """Test dividing quantities."""
        q1 = Quantity(100, 'meter')
        q2 = Quantity(10, 'second')
        result = q1 / q2
        assert result.magnitude == 10
    
    def test_scalar_multiplication(self):
        """Test multiplying by scalar."""
        q = Quantity(10, 'meter')
        result = q * 5
        assert result.magnitude == 50
    
    def test_power(self):
        """Test raising to power."""
        q = Quantity(10, 'meter')
        result = q ** 2
        assert result.magnitude == 100


class TestQuantityComparison:
    """Test comparison operations."""
    
    def test_equality(self):
        """Test equality comparison."""
        q1 = Quantity(1000, 'meter')
        q2 = Quantity(1, 'kilometer')
        assert q1 == q2
    
    def test_less_than(self):
        """Test less than comparison."""
        q1 = Quantity(100, 'meter')
        q2 = Quantity(200, 'meter')
        assert q1 < q2
    
    def test_greater_than(self):
        """Test greater than comparison."""
        q1 = Quantity(200, 'meter')
        q2 = Quantity(100, 'meter')
        assert q1 > q2


class TestQuantityArray:
    """Test array operations."""
    
    def test_array_creation(self):
        """Test creating quantity with array."""
        arr = np.array([1, 2, 3, 4, 5])
        q = Quantity(arr, 'meter')
        assert len(q.magnitude) == 5
    
    def test_array_conversion(self):
        """Test converting array quantity."""
        arr = np.array([1000, 2000, 3000])
        q = Quantity(arr, 'meter')
        q_km = q.to('kilometer')
        expected = np.array([1, 2, 3])
        assert np.allclose(q_km.magnitude, expected)
    
    def test_array_arithmetic(self):
        """Test arithmetic with array quantities."""
        arr1 = np.array([10, 20, 30])
        arr2 = np.array([5, 10, 15])
        q1 = Quantity(arr1, 'meter')
        q2 = Quantity(arr2, 'meter')
        result = q1 + q2
        expected = np.array([15, 30, 45])
        assert np.allclose(result.magnitude, expected)
