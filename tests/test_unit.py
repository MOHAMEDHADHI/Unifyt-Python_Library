"""Tests for Unit class."""

import pytest
from unifyt import Unit
from unifyt.dimensions import Dimension


class TestUnitCreation:
    """Test unit creation."""
    
    def test_create_simple_unit(self):
        """Test creating simple unit."""
        unit = Unit('meter')
        assert str(unit) == 'meter'
    
    def test_create_compound_unit(self):
        """Test creating compound unit."""
        unit = Unit('meter/second')
        assert 'meter' in str(unit)
        assert 'second' in str(unit)


class TestUnitDimensionality:
    """Test unit dimensionality."""
    
    def test_length_dimensionality(self):
        """Test length unit dimensionality."""
        unit = Unit('meter')
        dim = unit.dimensionality
        assert dim.length == 1
        assert dim.mass == 0
    
    def test_velocity_dimensionality(self):
        """Test velocity unit dimensionality."""
        unit = Unit('meter/second')
        dim = unit.dimensionality
        assert dim.length == 1
        assert dim.time == -1


class TestUnitCompatibility:
    """Test unit compatibility."""
    
    def test_compatible_units(self):
        """Test that compatible units are recognized."""
        u1 = Unit('meter')
        u2 = Unit('kilometer')
        assert u1.is_compatible_with(u2)
    
    def test_incompatible_units(self):
        """Test that incompatible units are recognized."""
        u1 = Unit('meter')
        u2 = Unit('second')
        assert not u1.is_compatible_with(u2)


class TestUnitConversion:
    """Test unit conversion factors."""
    
    def test_meter_to_kilometer(self):
        """Test meter to kilometer conversion."""
        u1 = Unit('meter')
        u2 = Unit('kilometer')
        factor = u1.conversion_factor_to(u2)
        assert factor == 0.001
    
    def test_second_to_minute(self):
        """Test second to minute conversion."""
        u1 = Unit('second')
        u2 = Unit('minute')
        factor = u1.conversion_factor_to(u2)
        assert abs(factor - 1/60) < 1e-10


class TestUnitArithmetic:
    """Test unit arithmetic."""
    
    def test_unit_multiplication(self):
        """Test multiplying units."""
        u1 = Unit('meter')
        u2 = Unit('second')
        result = u1 * u2
        assert 'meter' in str(result)
        assert 'second' in str(result)
    
    def test_unit_division(self):
        """Test dividing units."""
        u1 = Unit('meter')
        u2 = Unit('second')
        result = u1 / u2
        dim = result.dimensionality
        assert dim.length == 1
        assert dim.time == -1
    
    def test_unit_power(self):
        """Test raising unit to power."""
        u = Unit('meter')
        result = u ** 2
        dim = result.dimensionality
        assert dim.length == 2
