"""Dimension class for tracking physical dimensions."""

from __future__ import annotations
from typing import Dict


class Dimension:
    """
    Represents physical dimensions (length, mass, time, etc.).
    
    Examples:
        >>> length = Dimension(length=1)
        >>> time = Dimension(time=1)
        >>> velocity = Dimension(length=1, time=-1)
    """
    
    def __init__(
        self,
        length: float = 0,
        mass: float = 0,
        time: float = 0,
        current: float = 0,
        temperature: float = 0,
        amount: float = 0,
        luminosity: float = 0,
    ):
        """Initialize a Dimension with base SI dimensions."""
        self._dims: Dict[str, float] = {
            'length': length,
            'mass': mass,
            'time': time,
            'current': current,
            'temperature': temperature,
            'amount': amount,
            'luminosity': luminosity,
        }
        # Remove zero dimensions for cleaner representation
        self._dims = {k: v for k, v in self._dims.items() if v != 0}
    
    @property
    def length(self) -> float:
        """Length dimension exponent."""
        return self._dims.get('length', 0)
    
    @property
    def mass(self) -> float:
        """Mass dimension exponent."""
        return self._dims.get('mass', 0)
    
    @property
    def time(self) -> float:
        """Time dimension exponent."""
        return self._dims.get('time', 0)
    
    @property
    def current(self) -> float:
        """Electric current dimension exponent."""
        return self._dims.get('current', 0)
    
    @property
    def temperature(self) -> float:
        """Temperature dimension exponent."""
        return self._dims.get('temperature', 0)
    
    @property
    def amount(self) -> float:
        """Amount of substance dimension exponent."""
        return self._dims.get('amount', 0)
    
    @property
    def luminosity(self) -> float:
        """Luminous intensity dimension exponent."""
        return self._dims.get('luminosity', 0)
    
    def __add__(self, other: Dimension) -> Dimension:
        """Add dimensions (for multiplication of quantities)."""
        new_dims = self._dims.copy()
        for dim, value in other._dims.items():
            new_dims[dim] = new_dims.get(dim, 0) + value
        
        return Dimension(
            length=new_dims.get('length', 0),
            mass=new_dims.get('mass', 0),
            time=new_dims.get('time', 0),
            current=new_dims.get('current', 0),
            temperature=new_dims.get('temperature', 0),
            amount=new_dims.get('amount', 0),
            luminosity=new_dims.get('luminosity', 0),
        )
    
    def __sub__(self, other: Dimension) -> Dimension:
        """Subtract dimensions (for division of quantities)."""
        new_dims = self._dims.copy()
        for dim, value in other._dims.items():
            new_dims[dim] = new_dims.get(dim, 0) - value
        
        return Dimension(
            length=new_dims.get('length', 0),
            mass=new_dims.get('mass', 0),
            time=new_dims.get('time', 0),
            current=new_dims.get('current', 0),
            temperature=new_dims.get('temperature', 0),
            amount=new_dims.get('amount', 0),
            luminosity=new_dims.get('luminosity', 0),
        )
    
    def __mul__(self, scalar: float) -> Dimension:
        """Multiply dimension by scalar (for powers)."""
        return Dimension(
            length=self.length * scalar,
            mass=self.mass * scalar,
            time=self.time * scalar,
            current=self.current * scalar,
            temperature=self.temperature * scalar,
            amount=self.amount * scalar,
            luminosity=self.luminosity * scalar,
        )
    
    def __eq__(self, other: object) -> bool:
        """Check if dimensions are equal."""
        if not isinstance(other, Dimension):
            return False
        return self._dims == other._dims
    
    def __repr__(self) -> str:
        """String representation."""
        if not self._dims:
            return "Dimension(dimensionless)"
        parts = [f"{k}={v}" for k, v in self._dims.items()]
        return f"Dimension({', '.join(parts)})"
    
    def __str__(self) -> str:
        """Human-readable string."""
        if not self._dims:
            return "dimensionless"
        parts = []
        for dim, power in self._dims.items():
            if power == 1:
                parts.append(dim)
            else:
                parts.append(f"{dim}^{power}")
        return " * ".join(parts)
