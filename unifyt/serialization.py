"""Serialization support for Unifyt quantities."""

import json
import pickle
from typing import Any, Dict, Union
import numpy as np
from unifyt.quantity import Quantity
from unifyt.unit import Unit


__version__ = "1.0"


def quantity_to_dict(quantity: Quantity) -> Dict[str, Any]:
    """
    Convert a Quantity to a dictionary.
    
    Args:
        quantity: Quantity to convert
        
    Returns:
        Dictionary representation
        
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> d = quantity_to_dict(q)
        >>> d['value']
        100
    """
    value = quantity.magnitude
    
    # Convert numpy arrays to lists for JSON compatibility
    if isinstance(value, np.ndarray):
        value = value.tolist()
    
    return {
        'type': 'Quantity',
        'value': value,
        'unit': str(quantity.unit),
        'version': __version__
    }


def dict_to_quantity(data: Dict[str, Any]) -> Quantity:
    """
    Convert a dictionary to a Quantity.
    
    Args:
        data: Dictionary with 'value' and 'unit' keys
        
    Returns:
        Quantity object
        
    Examples:
        >>> d = {'value': 100, 'unit': 'meter', 'type': 'Quantity'}
        >>> q = dict_to_quantity(d)
        >>> q.magnitude
        100
    """
    if data.get('type') != 'Quantity':
        raise ValueError("Dictionary does not represent a Quantity")
    
    value = data['value']
    unit = data['unit']
    
    # Convert lists back to numpy arrays
    if isinstance(value, list):
        value = np.array(value)
    
    return Quantity(value, unit)


def quantity_to_json(quantity: Quantity, **kwargs) -> str:
    """
    Convert a Quantity to a JSON string.
    
    Args:
        quantity: Quantity to convert
        **kwargs: Additional arguments for json.dumps
        
    Returns:
        JSON string
        
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> json_str = quantity_to_json(q)
        >>> 'meter' in json_str
        True
    """
    data = quantity_to_dict(quantity)
    return json.dumps(data, **kwargs)


def json_to_quantity(json_str: str) -> Quantity:
    """
    Convert a JSON string to a Quantity.
    
    Args:
        json_str: JSON string
        
    Returns:
        Quantity object
        
    Examples:
        >>> json_str = '{"value": 100, "unit": "meter", "type": "Quantity", "version": "1.0"}'
        >>> q = json_to_quantity(json_str)
        >>> q.magnitude
        100
    """
    data = json.loads(json_str)
    return dict_to_quantity(data)


def save_quantity(quantity: Quantity, filename: str, format: str = 'json') -> None:
    """
    Save a Quantity to a file.
    
    Args:
        quantity: Quantity to save
        filename: File path
        format: Format ('json' or 'pickle')
        
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> save_quantity(q, 'distance.json')
    """
    if format == 'json':
        with open(filename, 'w') as f:
            json.dump(quantity_to_dict(quantity), f)
    elif format == 'pickle':
        with open(filename, 'wb') as f:
            pickle.dump(quantity, f)
    else:
        raise ValueError(f"Unsupported format: {format}")


def load_quantity(filename: str, format: str = 'json') -> Quantity:
    """
    Load a Quantity from a file.
    
    Args:
        filename: File path
        format: Format ('json' or 'pickle')
        
    Returns:
        Quantity object
        
    Examples:
        >>> q = load_quantity('distance.json')
    """
    if format == 'json':
        with open(filename, 'r') as f:
            data = json.load(f)
        return dict_to_quantity(data)
    elif format == 'pickle':
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError(f"Unsupported format: {format}")


class QuantityEncoder(json.JSONEncoder):
    """
    JSON encoder for Quantity objects.
    
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> json.dumps({'distance': q}, cls=QuantityEncoder)
    """
    
    def default(self, obj):
        """Encode Quantity objects."""
        if isinstance(obj, Quantity):
            return quantity_to_dict(obj)
        return super().default(obj)


def quantity_decoder(dct: Dict[str, Any]) -> Union[Quantity, Dict[str, Any]]:
    """
    JSON decoder hook for Quantity objects.
    
    Args:
        dct: Dictionary from JSON
        
    Returns:
        Quantity if dict represents one, otherwise the dict itself
        
    Examples:
        >>> json_str = '{"value": 100, "unit": "meter", "type": "Quantity", "version": "1.0"}'
        >>> json.loads(json_str, object_hook=quantity_decoder)
    """
    if dct.get('type') == 'Quantity':
        return dict_to_quantity(dct)
    return dct


__all__ = [
    'quantity_to_dict',
    'dict_to_quantity',
    'quantity_to_json',
    'json_to_quantity',
    'save_quantity',
    'load_quantity',
    'QuantityEncoder',
    'quantity_decoder',
]
