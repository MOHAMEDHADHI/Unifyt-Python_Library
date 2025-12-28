"""Context manager for unit systems."""

from typing import Optional
from contextlib import contextmanager


class UnitContext:
    """
    Context manager for switching between unit systems.
    
    Examples:
        >>> with UnitContext('imperial'):
        ...     distance = Quantity(100, 'feet')
        ...     print(distance)
    """
    
    _current_system: Optional[str] = None
    
    def __init__(self, system: str):
        """
        Initialize context with a unit system.
        
        Args:
            system: Unit system name ('SI', 'imperial', 'CGS', etc.)
        """
        self.system = system
        self._previous_system: Optional[str] = None
    
    def __enter__(self) -> 'UnitContext':
        """Enter the context."""
        self._previous_system = UnitContext._current_system
        UnitContext._current_system = self.system
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit the context."""
        UnitContext._current_system = self._previous_system
    
    @classmethod
    def get_current_system(cls) -> Optional[str]:
        """Get the current unit system."""
        return cls._current_system


@contextmanager
def unit_system(system: str):
    """
    Context manager for temporarily switching unit systems.
    
    Args:
        system: Unit system name
        
    Examples:
        >>> with unit_system('imperial'):
        ...     # Use imperial units
        ...     pass
    """
    ctx = UnitContext(system)
    with ctx:
        yield ctx
