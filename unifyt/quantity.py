"""Core Quantity class for representing values with units."""

from __future__ import annotations
from typing import Union, Any, Optional
import numpy as np
from unifyt.unit import Unit
from unifyt.dimensions import Dimension


class Quantity:
    """
    Represents a physical quantity with a value and unit.
    
    Examples:
        >>> distance = Quantity(100, 'meters')
        >>> time = Quantity(10, 'seconds')
        >>> speed = distance / time
        >>> print(speed.to('km/h'))
    """
    
    def __init__(self, value: Union[float, int, np.ndarray], unit: Union[str, Unit]):
        """
        Initialize a Quantity.
        
        Args:
            value: Numerical value (scalar or array)
            unit: Unit as string or Unit object
        """
        self._value = np.asarray(value)
        self._unit = Unit(unit) if isinstance(unit, str) else unit
    
    @property
    def value(self) -> np.ndarray:
        """Get the numerical value."""
        return self._value
    
    @property
    def unit(self) -> Unit:
        """Get the unit."""
        return self._unit
    
    @property
    def magnitude(self) -> Union[float, np.ndarray]:
        """Get the magnitude (scalar or array)."""
        return self._value.item() if self._value.shape == () else self._value
    
    @property
    def dimensionality(self) -> Dimension:
        """Get the dimensionality of this quantity."""
        return self._unit.dimensionality
    
    def to(self, target_unit: Union[str, Unit]) -> Quantity:
        """
        Convert to a different unit.
        
        Args:
            target_unit: Target unit for conversion
            
        Returns:
            New Quantity with converted value
            
        Raises:
            ValueError: If units are incompatible
        """
        target = Unit(target_unit) if isinstance(target_unit, str) else target_unit
        
        if not self._unit.is_compatible_with(target):
            raise ValueError(
                f"Cannot convert from {self._unit} to {target}: "
                f"incompatible dimensions"
            )
        
        conversion_factor = self._unit.conversion_factor_to(target)
        new_value = self._value * conversion_factor
        return Quantity(new_value, target)
    
    def to_base_units(self) -> Quantity:
        """Convert to base SI units."""
        return self.to(self._unit.to_base_units())
    
    def __add__(self, other: Union[Quantity, float, int]) -> Quantity:
        """Add two quantities or a quantity and a scalar."""
        if isinstance(other, Quantity):
            if not self._unit.is_compatible_with(other._unit):
                raise ValueError(f"Cannot add {self._unit} and {other._unit}")
            other_converted = other.to(self._unit)
            return Quantity(self._value + other_converted._value, self._unit)
        elif self._unit.is_dimensionless():
            return Quantity(self._value + other, self._unit)
        else:
            raise ValueError("Cannot add dimensioned quantity with scalar")
    
    def __sub__(self, other: Union[Quantity, float, int]) -> Quantity:
        """Subtract two quantities or a quantity and a scalar."""
        if isinstance(other, Quantity):
            if not self._unit.is_compatible_with(other._unit):
                raise ValueError(f"Cannot subtract {other._unit} from {self._unit}")
            other_converted = other.to(self._unit)
            return Quantity(self._value - other_converted._value, self._unit)
        elif self._unit.is_dimensionless():
            return Quantity(self._value - other, self._unit)
        else:
            raise ValueError("Cannot subtract scalar from dimensioned quantity")
    
    def __mul__(self, other: Union[Quantity, float, int]) -> Quantity:
        """Multiply quantities or quantity by scalar."""
        if isinstance(other, Quantity):
            new_value = self._value * other._value
            new_unit = self._unit * other._unit
            return Quantity(new_value, new_unit)
        else:
            return Quantity(self._value * other, self._unit)
    
    def __truediv__(self, other: Union[Quantity, float, int]) -> Quantity:
        """Divide quantities or quantity by scalar."""
        if isinstance(other, Quantity):
            new_value = self._value / other._value
            new_unit = self._unit / other._unit
            return Quantity(new_value, new_unit)
        else:
            return Quantity(self._value / other, self._unit)
    
    def __pow__(self, exponent: Union[int, float]) -> Quantity:
        """Raise quantity to a power."""
        new_value = self._value ** exponent
        new_unit = self._unit ** exponent
        return Quantity(new_value, new_unit)
    
    def __radd__(self, other: Union[float, int]) -> Quantity:
        """Right addition."""
        return self.__add__(other)
    
    def __rsub__(self, other: Union[float, int]) -> Quantity:
        """Right subtraction."""
        return Quantity(other - self._value, self._unit)
    
    def __rmul__(self, other: Union[float, int]) -> Quantity:
        """Right multiplication."""
        return self.__mul__(other)
    
    def __rtruediv__(self, other: Union[float, int]) -> Quantity:
        """Right division."""
        return Quantity(other / self._value, Unit("dimensionless") / self._unit)
    
    def __neg__(self) -> Quantity:
        """Negate quantity."""
        return Quantity(-self._value, self._unit)
    
    def __abs__(self) -> Quantity:
        """Absolute value."""
        return Quantity(np.abs(self._value), self._unit)
    
    def __eq__(self, other: Any) -> bool:
        """Check equality."""
        if not isinstance(other, Quantity):
            return False
        if not self._unit.is_compatible_with(other._unit):
            return False
        other_converted = other.to(self._unit)
        return np.allclose(self._value, other_converted._value)
    
    def __lt__(self, other: Quantity) -> bool:
        """Less than comparison."""
        if not isinstance(other, Quantity):
            raise TypeError("Cannot compare Quantity with non-Quantity")
        if not self._unit.is_compatible_with(other._unit):
            raise ValueError(f"Cannot compare {self._unit} with {other._unit}")
        other_converted = other.to(self._unit)
        return bool(np.all(self._value < other_converted._value))
    
    def __le__(self, other: Quantity) -> bool:
        """Less than or equal comparison."""
        return self == other or self < other
    
    def __gt__(self, other: Quantity) -> bool:
        """Greater than comparison."""
        if not isinstance(other, Quantity):
            raise TypeError("Cannot compare Quantity with non-Quantity")
        return not self <= other
    
    def __ge__(self, other: Quantity) -> bool:
        """Greater than or equal comparison."""
        return not self < other
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Quantity({self.magnitude}, '{self._unit}')"
    
    def __str__(self) -> str:
        """Human-readable string."""
        return f"{self.magnitude} {self._unit}"
    
    def __format__(self, format_spec: str) -> str:
        """Format quantity."""
        if format_spec:
            return f"{self._value.__format__(format_spec)} {self._unit}"
        return str(self)
