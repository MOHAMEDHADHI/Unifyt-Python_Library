#!/usr/bin/env python3
"""Quick test to verify all exceptions work correctly."""

import sys
sys.path.insert(0, '.')

# Import directly from exceptions module to avoid dependency issues
from unifyt.exceptions import (
    UnifytException,
    UnitError,
    DimensionalityError,
    UnitNotFoundError,
    UnitParseError,
    ConversionError,
    QuantityError,
    InvalidValueError,
    OperationError,
    ComparisonError,
    ArrayError,
    QuantityOverflowError,
    RegistryError,
    UnitDefinitionError,
    UnitAlreadyExistsError,
    UnitSystemError,
    SerializationError,
    SerializationFormatError,
    DeserializationError,
    SerializationVersionError,
    ContextError,
    InvalidUnitSystemError,
    ContextStateError,
    ConstantError,
    UtilityError,
    ValidationError,
    PrecisionError,
    ConfigurationError,
    ErrorContext,
    create_exception,
)


def test_basic_exceptions():
    """Test that all exceptions can be instantiated."""
    print("Testing exception instantiation...")
    
    # Test base exception
    exc = UnifytException("test message")
    assert exc.message == "test message"
    assert str(exc) == "test message"
    print("✓ UnifytException")
    
    # Test unit errors
    exc = DimensionalityError("meter", "second", "addition")
    assert exc.unit1 == "meter"
    assert exc.unit2 == "second"
    print("✓ DimensionalityError")
    
    exc = UnitNotFoundError("metrs", ["meter", "meters"])
    assert exc.unit_name == "metrs"
    assert len(exc.suggestions) == 2
    print("✓ UnitNotFoundError")
    
    exc = UnitParseError("meter//second", "invalid syntax", 6)
    assert exc.unit_string == "meter//second"
    assert exc.position == 6
    print("✓ UnitParseError")
    
    exc = ConversionError("meter", "second", "incompatible")
    assert exc.from_unit == "meter"
    assert exc.to_unit == "second"
    print("✓ ConversionError")
    
    # Test quantity errors
    exc = InvalidValueError(float('nan'), "not a number", "must be finite")
    assert exc.constraint == "must be finite"
    print("✓ InvalidValueError")
    
    exc = OperationError("addition", "meter", "second", "incompatible")
    assert exc.operation == "addition"
    print("✓ OperationError")
    
    exc = ComparisonError("100 meter", "10 second", "incompatible")
    print("✓ ComparisonError")
    
    exc = ArrayError("concatenate", "incompatible units", "shapes: (2,) (3,)")
    assert exc.operation == "concatenate"
    print("✓ ArrayError")
    
    exc = QuantityOverflowError("multiplication", ["huge", "huge"])
    assert exc.operation == "multiplication"
    print("✓ QuantityOverflowError")
    
    # Test registry errors
    exc = UnitDefinitionError("bad_unit", "invalid", "syntax error")
    assert exc.unit_name == "bad_unit"
    print("✓ UnitDefinitionError")
    
    exc = UnitAlreadyExistsError("meter")
    assert exc.unit_name == "meter"
    print("✓ UnitAlreadyExistsError")
    
    exc = UnitSystemError("bad_system", "invalid config")
    assert exc.system_name == "bad_system"
    print("✓ UnitSystemError")
    
    # Test serialization errors
    exc = SerializationFormatError("xml", ["json", "pickle"])
    assert exc.format_name == "xml"
    assert len(exc.supported_formats) == 2
    print("✓ SerializationFormatError")
    
    exc = DeserializationError("corrupted data", "invalid json", "json")
    assert exc.format_hint == "json"
    print("✓ DeserializationError")
    
    exc = SerializationVersionError("0.1.0", "0.2.0")
    assert exc.data_version == "0.1.0"
    print("✓ SerializationVersionError")
    
    # Test context errors
    exc = InvalidUnitSystemError("bad", ["SI", "imperial"])
    assert exc.system_name == "bad"
    print("✓ InvalidUnitSystemError")
    
    exc = ContextStateError("not entered")
    assert exc.reason == "not entered"
    print("✓ ContextStateError")
    
    # Test other errors
    exc = ConstantError("bad_constant", ["c", "h", "G"])
    assert exc.constant_name == "bad_constant"
    print("✓ ConstantError")
    
    exc = UtilityError("concatenate", "empty list")
    assert exc.function_name == "concatenate"
    print("✓ UtilityError")
    
    exc = ValidationError("distance", -1, "must be positive")
    assert exc.parameter == "distance"
    print("✓ ValidationError")
    
    exc = PrecisionError("addition", 1e-15)
    assert exc.operation == "addition"
    print("✓ PrecisionError")
    
    exc = ConfigurationError("max_precision", 1000, "too large")
    assert exc.setting == "max_precision"
    print("✓ ConfigurationError")


def test_exception_hierarchy():
    """Test exception inheritance."""
    print("\nTesting exception hierarchy...")
    
    # All exceptions should inherit from UnifytException
    assert issubclass(UnitError, UnifytException)
    assert issubclass(DimensionalityError, UnitError)
    assert issubclass(QuantityError, UnifytException)
    assert issubclass(OperationError, QuantityError)
    print("✓ Exception hierarchy correct")


def test_error_context():
    """Test ErrorContext manager."""
    print("\nTesting ErrorContext...")
    
    try:
        with ErrorContext("test operation"):
            raise UnifytException("test error")
    except UnifytException as e:
        assert "context: test operation" in str(e)
        print("✓ ErrorContext adds context to exceptions")


def test_create_exception():
    """Test create_exception helper."""
    print("\nTesting create_exception...")
    
    exc = create_exception(
        UnitError,
        "custom error",
        custom_attr="value",
        another_attr=42
    )
    assert exc.message == "custom error"
    assert exc.custom_attr == "value"
    assert exc.another_attr == 42
    print("✓ create_exception works correctly")


def test_exception_repr():
    """Test exception repr."""
    print("\nTesting exception repr...")
    
    exc = ConversionError("meter", "second")
    repr_str = repr(exc)
    assert "ConversionError" in repr_str
    print(f"✓ Exception repr: {repr_str}")


if __name__ == "__main__":
    print("=" * 60)
    print("Unifyt Exception System - Basic Tests")
    print("=" * 60)
    
    test_basic_exceptions()
    test_exception_hierarchy()
    test_error_context()
    test_create_exception()
    test_exception_repr()
    
    print("\n" + "=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)
