"""Tests for serialization functionality."""

import pytest
import json
import tempfile
import os
import numpy as np
from unifyt import Quantity
from unifyt.serialization import (
    quantity_to_dict,
    dict_to_quantity,
    quantity_to_json,
    json_to_quantity,
    save_quantity,
    load_quantity,
    QuantityEncoder,
    quantity_decoder,
)


class TestDictSerialization:
    """Test dictionary serialization."""
    
    def test_quantity_to_dict(self):
        """Test converting quantity to dict."""
        q = Quantity(100, 'meter')
        d = quantity_to_dict(q)
        assert d['value'] == 100
        assert d['unit'] == 'meter'
        assert d['type'] == 'Quantity'
    
    def test_dict_to_quantity(self):
        """Test converting dict to quantity."""
        d = {'value': 100, 'unit': 'meter', 'type': 'Quantity'}
        q = dict_to_quantity(d)
        assert q.magnitude == 100
        assert str(q.unit) == 'meter'
    
    def test_array_to_dict(self):
        """Test converting array quantity to dict."""
        q = Quantity(np.array([1, 2, 3]), 'meter')
        d = quantity_to_dict(q)
        assert d['value'] == [1, 2, 3]
    
    def test_dict_to_array(self):
        """Test converting dict to array quantity."""
        d = {'value': [1, 2, 3], 'unit': 'meter', 'type': 'Quantity'}
        q = dict_to_quantity(d)
        assert np.array_equal(q.magnitude, np.array([1, 2, 3]))


class TestJSONSerialization:
    """Test JSON serialization."""
    
    def test_quantity_to_json(self):
        """Test converting quantity to JSON."""
        q = Quantity(100, 'meter')
        json_str = quantity_to_json(q)
        assert isinstance(json_str, str)
        assert 'meter' in json_str
    
    def test_json_to_quantity(self):
        """Test converting JSON to quantity."""
        json_str = '{"value": 100, "unit": "meter", "type": "Quantity", "version": "1.0"}'
        q = json_to_quantity(json_str)
        assert q.magnitude == 100
        assert str(q.unit) == 'meter'
    
    def test_roundtrip(self):
        """Test JSON roundtrip."""
        q1 = Quantity(42.5, 'kilometer')
        json_str = quantity_to_json(q1)
        q2 = json_to_quantity(json_str)
        assert q1.magnitude == q2.magnitude
        assert str(q1.unit) == str(q2.unit)


class TestFileSerialization:
    """Test file serialization."""
    
    def test_save_load_json(self):
        """Test saving and loading JSON."""
        q1 = Quantity(100, 'meter')
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            filename = f.name
        
        try:
            save_quantity(q1, filename, format='json')
            q2 = load_quantity(filename, format='json')
            assert q1.magnitude == q2.magnitude
            assert str(q1.unit) == str(q2.unit)
        finally:
            os.unlink(filename)
    
    def test_save_load_pickle(self):
        """Test saving and loading pickle."""
        q1 = Quantity(np.array([1, 2, 3]), 'meter')
        
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.pkl') as f:
            filename = f.name
        
        try:
            save_quantity(q1, filename, format='pickle')
            q2 = load_quantity(filename, format='pickle')
            assert np.array_equal(q1.magnitude, q2.magnitude)
            assert str(q1.unit) == str(q2.unit)
        finally:
            os.unlink(filename)


class TestJSONEncoder:
    """Test JSON encoder."""
    
    def test_encoder(self):
        """Test QuantityEncoder."""
        q = Quantity(100, 'meter')
        data = {'distance': q}
        json_str = json.dumps(data, cls=QuantityEncoder)
        assert 'meter' in json_str
    
    def test_decoder(self):
        """Test quantity_decoder."""
        json_str = '{"value": 100, "unit": "meter", "type": "Quantity", "version": "1.0"}'
        q = json.loads(json_str, object_hook=quantity_decoder)
        assert isinstance(q, Quantity)
        assert q.magnitude == 100
