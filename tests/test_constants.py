"""Tests for physical constants."""

import pytest
from unifyt import constants, Quantity


class TestPhysicalConstants:
    """Test physical constants."""
    
    def test_speed_of_light(self):
        """Test speed of light constant."""
        assert isinstance(constants.c, Quantity)
        assert constants.c.magnitude == 299792458
    
    def test_planck_constant(self):
        """Test Planck constant."""
        assert isinstance(constants.h, Quantity)
        assert constants.h.magnitude > 0
    
    def test_gravitational_constant(self):
        """Test gravitational constant."""
        assert isinstance(constants.G, Quantity)
        assert constants.G.magnitude > 0
    
    def test_avogadro(self):
        """Test Avogadro constant."""
        assert isinstance(constants.N_A, Quantity)
        assert constants.N_A.magnitude > 6e23
    
    def test_standard_gravity(self):
        """Test standard gravity."""
        assert isinstance(constants.g, Quantity)
        assert abs(constants.g.magnitude - 9.80665) < 1e-5


class TestAstronomicalConstants:
    """Test astronomical constants."""
    
    def test_astronomical_unit(self):
        """Test astronomical unit."""
        assert isinstance(constants.AU, Quantity)
        assert constants.AU.magnitude > 1e11
    
    def test_light_year(self):
        """Test light year."""
        assert isinstance(constants.ly, Quantity)
        assert constants.ly.magnitude > 9e15
    
    def test_solar_mass(self):
        """Test solar mass."""
        assert isinstance(constants.M_sun, Quantity)
        assert constants.M_sun.magnitude > 1e30


class TestConstantAccess:
    """Test constant access functions."""
    
    def test_get_constant(self):
        """Test getting constant by name."""
        c = constants.get_constant('c')
        assert isinstance(c, Quantity)
    
    def test_get_constant_not_found(self):
        """Test getting non-existent constant."""
        with pytest.raises(KeyError):
            constants.get_constant('nonexistent')
    
    def test_list_constants(self):
        """Test listing all constants."""
        const_list = constants.list_constants()
        assert isinstance(const_list, list)
        assert len(const_list) > 0
        assert 'c' in const_list
        assert 'G' in const_list
