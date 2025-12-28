"""Unit registry for managing custom units and unit systems."""

from typing import Dict, Optional
from unifyt.unit import Unit


class UnitRegistry:
    """
    Registry for managing units and unit systems.
    
    Examples:
        >>> registry = UnitRegistry()
        >>> registry.define('furlong', '220 yards')
        >>> registry.define('fortnight', '14 days')
    """
    
    def __init__(self) -> None:
        """Initialize the unit registry."""
        self._custom_units: Dict[str, Unit] = {}
        self._aliases: Dict[str, str] = {}
    
    def define(self, name: str, definition: str) -> None:
        """
        Define a custom unit.
        
        Args:
            name: Name of the new unit
            definition: Definition in terms of existing units
        """
        # Parse definition and create unit
        unit = Unit(definition)
        self._custom_units[name] = unit
    
    def alias(self, alias: str, unit_name: str) -> None:
        """
        Create an alias for an existing unit.
        
        Args:
            alias: New alias name
            unit_name: Existing unit name
        """
        self._aliases[alias] = unit_name
    
    def get_unit(self, name: str) -> Optional[Unit]:
        """
        Get a unit by name.
        
        Args:
            name: Unit name or alias
            
        Returns:
            Unit object or None if not found
        """
        # Check aliases first
        if name in self._aliases:
            name = self._aliases[name]
        
        # Check custom units
        if name in self._custom_units:
            return self._custom_units[name]
        
        # Try to create from built-in units
        try:
            return Unit(name)
        except Exception:
            return None
    
    def list_units(self) -> Dict[str, Unit]:
        """List all custom units."""
        return self._custom_units.copy()
    
    def list_aliases(self) -> Dict[str, str]:
        """List all aliases."""
        return self._aliases.copy()
