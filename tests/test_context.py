"""Tests for UnitContext class."""

import pytest
from unifyt.context import UnitContext, unit_system


class TestUnitContext:
    """Test unit context manager."""
    
    def test_context_creation(self):
        """Test creating context."""
        ctx = UnitContext('SI')
        assert ctx.system == 'SI'
    
    def test_context_enter_exit(self):
        """Test entering and exiting context."""
        assert UnitContext.get_current_system() is None
        
        with UnitContext('imperial'):
            assert UnitContext.get_current_system() == 'imperial'
        
        assert UnitContext.get_current_system() is None
    
    def test_nested_contexts(self):
        """Test nested contexts."""
        with UnitContext('SI'):
            assert UnitContext.get_current_system() == 'SI'
            
            with UnitContext('imperial'):
                assert UnitContext.get_current_system() == 'imperial'
            
            assert UnitContext.get_current_system() == 'SI'
    
    def test_unit_system_function(self):
        """Test unit_system context manager function."""
        with unit_system('CGS'):
            assert UnitContext.get_current_system() == 'CGS'
