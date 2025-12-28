"""Utility functions for Unifyt."""

from typing import Union, List, Tuple
import numpy as np
from unifyt.quantity import Quantity
from unifyt.unit import Unit


def linspace(start: Quantity, stop: Quantity, num: int = 50) -> Quantity:
    """
    Create evenly spaced quantities over a specified interval.
    
    Args:
        start: Starting quantity
        stop: Ending quantity (will be converted to start's units)
        num: Number of samples
        
    Returns:
        Quantity with array of evenly spaced values
        
    Examples:
        >>> temps = linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
    """
    stop_converted = stop.to(start.unit)
    values = np.linspace(start.magnitude, stop_converted.magnitude, num)
    return Quantity(values, start.unit)


def arange(start: Quantity, stop: Quantity, step: Quantity) -> Quantity:
    """
    Create quantities with evenly spaced values within a given interval.
    
    Args:
        start: Starting quantity
        stop: Ending quantity
        step: Step size
        
    Returns:
        Quantity with array of values
        
    Examples:
        >>> distances = arange(Quantity(0, 'meter'), Quantity(100, 'meter'), 
        ...                    Quantity(10, 'meter'))
    """
    stop_converted = stop.to(start.unit)
    step_converted = step.to(start.unit)
    values = np.arange(start.magnitude, stop_converted.magnitude, step_converted.magnitude)
    return Quantity(values, start.unit)


def zeros(shape: Union[int, Tuple[int, ...]], unit: Union[str, Unit]) -> Quantity:
    """
    Create a quantity array of zeros.
    
    Args:
        shape: Shape of the array
        unit: Unit for the quantity
        
    Returns:
        Quantity with zeros
        
    Examples:
        >>> z = zeros(10, 'meter')
        >>> z2d = zeros((3, 4), 'kilogram')
    """
    return Quantity(np.zeros(shape), unit)


def ones(shape: Union[int, Tuple[int, ...]], unit: Union[str, Unit]) -> Quantity:
    """
    Create a quantity array of ones.
    
    Args:
        shape: Shape of the array
        unit: Unit for the quantity
        
    Returns:
        Quantity with ones
        
    Examples:
        >>> o = ones(5, 'second')
    """
    return Quantity(np.ones(shape), unit)


def full(shape: Union[int, Tuple[int, ...]], fill_value: Quantity) -> Quantity:
    """
    Create a quantity array filled with a specific value.
    
    Args:
        shape: Shape of the array
        fill_value: Quantity to fill with
        
    Returns:
        Quantity filled with the value
        
    Examples:
        >>> f = full(10, Quantity(5, 'meter'))
    """
    arr = np.full(shape, fill_value.magnitude)
    return Quantity(arr, fill_value.unit)


def concatenate(quantities: List[Quantity], axis: int = 0) -> Quantity:
    """
    Concatenate quantities along an axis.
    
    Args:
        quantities: List of quantities to concatenate
        axis: Axis along which to concatenate
        
    Returns:
        Concatenated quantity
        
    Examples:
        >>> q1 = Quantity(np.array([1, 2]), 'meter')
        >>> q2 = Quantity(np.array([3, 4]), 'meter')
        >>> result = concatenate([q1, q2])
    """
    if not quantities:
        raise ValueError("Need at least one quantity to concatenate")
    
    # Convert all to first quantity's units
    base_unit = quantities[0].unit
    arrays = [q.to(base_unit).value for q in quantities]
    result = np.concatenate(arrays, axis=axis)
    return Quantity(result, base_unit)


def stack(quantities: List[Quantity], axis: int = 0) -> Quantity:
    """
    Stack quantities along a new axis.
    
    Args:
        quantities: List of quantities to stack
        axis: Axis along which to stack
        
    Returns:
        Stacked quantity
        
    Examples:
        >>> q1 = Quantity(np.array([1, 2]), 'meter')
        >>> q2 = Quantity(np.array([3, 4]), 'meter')
        >>> result = stack([q1, q2])
    """
    if not quantities:
        raise ValueError("Need at least one quantity to stack")
    
    base_unit = quantities[0].unit
    arrays = [q.to(base_unit).value for q in quantities]
    result = np.stack(arrays, axis=axis)
    return Quantity(result, base_unit)


def sum(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Sum of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to sum
        
    Returns:
        Sum as a quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        >>> total = sum(q)
    """
    result = np.sum(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def mean(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Mean of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to compute mean
        
    Returns:
        Mean as a quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        >>> avg = mean(q)
    """
    result = np.mean(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def std(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Standard deviation of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to compute std
        
    Returns:
        Standard deviation as a quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        >>> s = std(q)
    """
    result = np.std(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def min(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Minimum of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to find minimum
        
    Returns:
        Minimum as a quantity
    """
    result = np.min(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def max(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Maximum of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to find maximum
        
    Returns:
        Maximum as a quantity
    """
    result = np.max(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def sqrt(quantity: Quantity) -> Quantity:
    """
    Square root of a quantity.
    
    Args:
        quantity: Input quantity
        
    Returns:
        Square root as a quantity
        
    Examples:
        >>> area = Quantity(25, 'meter^2')
        >>> side = sqrt(area)
    """
    return quantity ** 0.5


def clip(quantity: Quantity, min_val: Quantity, max_val: Quantity) -> Quantity:
    """
    Clip quantity values to a range.
    
    Args:
        quantity: Input quantity
        min_val: Minimum value
        max_val: Maximum value
        
    Returns:
        Clipped quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 5, 10]), 'meter')
        >>> clipped = clip(q, Quantity(2, 'meter'), Quantity(8, 'meter'))
    """
    min_converted = min_val.to(quantity.unit).magnitude
    max_converted = max_val.to(quantity.unit).magnitude
    result = np.clip(quantity.value, min_converted, max_converted)
    return Quantity(result, quantity.unit)


def isclose(q1: Quantity, q2: Quantity, rtol: float = 1e-5, atol: float = 1e-8) -> bool:
    """
    Check if two quantities are close in value.
    
    Args:
        q1: First quantity
        q2: Second quantity
        rtol: Relative tolerance
        atol: Absolute tolerance
        
    Returns:
        True if quantities are close
        
    Examples:
        >>> q1 = Quantity(1.0, 'meter')
        >>> q2 = Quantity(1.0000001, 'meter')
        >>> isclose(q1, q2)
    """
    if not q1.unit.is_compatible_with(q2.unit):
        return False
    q2_converted = q2.to(q1.unit)
    return np.allclose(q1.value, q2_converted.value, rtol=rtol, atol=atol)
