"""Tests for UnitRegistry class."""

import pytest
from unifyt import UnitRegistry


class TestUnitRegistry:
    """Test unit registry."""
    
    def test_define_custom_unit(self):
        """Test defining custom unit."""
        registry = UnitRegistry()
        registry.define('furlong', '220 yard')
        unit = registry.get_unit('furlong')
        assert unit is not None
    
    def test_create_alias(self):
        """Test creating unit alias."""
        registry = UnitRegistry()
        registry.alias('m', 'meter')
        unit = registry.get_unit('m')
        assert unit is not None
    
    def test_list_units(self):
        """Test listing custom units."""
        registry = UnitRegistry()
        registry.define('custom1', 'meter')
        registry.define('custom2', 'second')
        units = registry.list_units()
        assert len(units) == 2
    
    def test_list_aliases(self):
        """Test listing aliases."""
        registry = UnitRegistry()
        registry.alias('m', 'meter')
        registry.alias('s', 'second')
        aliases = registry.list_aliases()
        assert len(aliases) == 2
