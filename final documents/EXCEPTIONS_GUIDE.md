# Unifyt Exception Handling Guide

This guide provides comprehensive documentation for all exceptions in the Unifyt library, including when they're raised, how to handle them, and best practices.

## Table of Contents

1. [Exception Hierarchy](#exception-hierarchy)
2. [Unit Errors](#unit-errors)
3. [Quantity Errors](#quantity-errors)
4. [Registry Errors](#registry-errors)
5. [Serialization Errors](#serialization-errors)
6. [Context Errors](#context-errors)
7. [Other Errors](#other-errors)
8. [Best Practices](#best-practices)
9. [Error Context Manager](#error-context-manager)

## Exception Hierarchy

All Unifyt exceptions inherit from `UnifytException`, allowing you to catch all library-specific errors:

```
UnifytException (base)
├── UnitError
│   ├── DimensionalityError
│   ├── UnitNotFoundError
│   ├── UnitParseError
│   └── ConversionError
├── QuantityError
│   ├── InvalidValueError
│   ├── OperationError
│   ├── ComparisonError
│   ├── ArrayError
│   └── QuantityOverflowError
├── RegistryError
│   ├── UnitDefinitionError
│   ├── UnitAlreadyExistsError
│   └── UnitSystemError
├── SerializationError
│   ├── SerializationFormatError
│   ├── DeserializationError
│   └── SerializationVersionError
├── ContextError
│   ├── InvalidUnitSystemError
│   └── ContextStateError
├── ConstantError
├── UtilityError
├── ValidationError
├── PrecisionError
└── ConfigurationError
```

## Unit Errors

### DimensionalityError

**When raised:** Operations involving incompatible dimensions (e.g., adding meters to seconds).

**Attributes:**
- `unit1`: First unit
- `unit2`: Second unit
- `operation`: Operation attempted

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import DimensionalityError

try:
    distance = Quantity(100, 'meter')
    time = Quantity(10, 'second')
    result = distance + time  # Incompatible!
except DimensionalityError as e:
    print(f"Cannot {e.operation}: {e.unit1} and {e.unit2}")
```

### UnitNotFoundError

**When raised:** Using an unrecognized unit name.

**Attributes:**
- `unit_name`: The unit that wasn't found
- `suggestions`: List of similar unit names

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import UnitNotFoundError

try:
    q = Quantity(100, 'metrs')  # Typo!
except UnitNotFoundError as e:
    print(f"Unit '{e.unit_name}' not found")
    if e.suggestions:
        print(f"Did you mean: {', '.join(e.suggestions)}")
```

### UnitParseError

**When raised:** Invalid unit string syntax.

**Attributes:**
- `unit_string`: The string that failed to parse
- `reason`: Why parsing failed
- `position`: Character position of error (if available)

**Example:**
```python
from unifyt import Unit
from unifyt.exceptions import UnitParseError

try:
    u = Unit('meter//second')  # Invalid syntax
except UnitParseError as e:
    print(f"Parse error at position {e.position}: {e.reason}")
```

### ConversionError

**When raised:** Converting between incompatible units.

**Attributes:**
- `from_unit`: Source unit
- `to_unit`: Target unit
- `reason`: Why conversion failed

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import ConversionError

try:
    distance = Quantity(100, 'meter')
    distance.to('second')  # Can't convert length to time!
except ConversionError as e:
    print(f"Cannot convert {e.from_unit} to {e.to_unit}: {e.reason}")
```

## Quantity Errors

### InvalidValueError

**When raised:** Quantity value is invalid (NaN, infinity, out of range).

**Attributes:**
- `value`: The invalid value
- `reason`: Why it's invalid
- `constraint`: Constraint that was violated

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import InvalidValueError
import numpy as np

try:
    q = Quantity(np.nan, 'meter')
    # Some operation requiring valid values
except InvalidValueError as e:
    print(f"Invalid value {e.value}: {e.constraint}")
```

### OperationError

**When raised:** Arithmetic operation cannot be performed.

**Attributes:**
- `operation`: The operation (e.g., 'addition', 'multiplication')
- `operand1`: First operand
- `operand2`: Second operand
- `reason`: Why operation failed

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import OperationError

try:
    distance = Quantity(100, 'meter')
    result = distance + 50  # Can't add scalar to dimensioned quantity
except OperationError as e:
    print(f"Cannot perform {e.operation}: {e.reason}")
```

### ComparisonError

**When raised:** Quantities cannot be compared.

**Attributes:**
- `quantity1`: First quantity
- `quantity2`: Second quantity
- `reason`: Why comparison failed

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import ComparisonError

try:
    distance = Quantity(100, 'meter')
    time = Quantity(10, 'second')
    result = distance < time  # Can't compare different dimensions
except ComparisonError as e:
    print(f"Cannot compare: {e.reason}")
```

### ArrayError

**When raised:** Array operations fail (concatenation, stacking, reshaping).

**Attributes:**
- `operation`: The array operation
- `reason`: Why it failed
- `shape_info`: Information about array shapes

**Example:**
```python
from unifyt import Quantity, utils
from unifyt.exceptions import ArrayError

try:
    q1 = Quantity([1, 2], 'meter')
    q2 = Quantity([3, 4], 'second')
    result = utils.concatenate([q1, q2])  # Incompatible units
except ArrayError as e:
    print(f"Array operation '{e.operation}' failed: {e.reason}")
```

### QuantityOverflowError

**When raised:** Calculation produces values too large to represent.

**Attributes:**
- `operation`: The operation that caused overflow
- `operands`: The operands involved

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import QuantityOverflowError
import sys

try:
    huge = Quantity(sys.float_info.max, 'meter')
    result = huge * huge  # Overflow!
except QuantityOverflowError as e:
    print(f"Overflow in {e.operation}")
```

## Registry Errors

### UnitDefinitionError

**When raised:** Invalid unit definition in registry.

**Attributes:**
- `unit_name`: Name of unit being defined
- `definition`: The invalid definition
- `reason`: Why definition is invalid

**Example:**
```python
from unifyt import UnitRegistry
from unifyt.exceptions import UnitDefinitionError

try:
    registry = UnitRegistry()
    registry.define('bad_unit', 'invalid syntax')
except UnitDefinitionError as e:
    print(f"Cannot define '{e.unit_name}': {e.reason}")
```

### UnitAlreadyExistsError

**When raised:** Trying to define a unit that already exists.

**Attributes:**
- `unit_name`: Name of existing unit

**Example:**
```python
from unifyt import UnitRegistry
from unifyt.exceptions import UnitAlreadyExistsError

registry = UnitRegistry()
registry.define('my_unit', 'meter')

try:
    registry.define('my_unit', 'kilometer')  # Already exists!
except UnitAlreadyExistsError as e:
    print(f"Unit '{e.unit_name}' already exists")
```

### UnitSystemError

**When raised:** Issues with unit system definitions.

**Attributes:**
- `system_name`: Name of the unit system
- `reason`: What's wrong with the system

**Example:**
```python
from unifyt import UnitRegistry
from unifyt.exceptions import UnitSystemError

try:
    registry = UnitRegistry()
    registry.add_system('bad_system', {})  # Invalid system
except UnitSystemError as e:
    print(f"System '{e.system_name}' error: {e.reason}")
```

## Serialization Errors

### SerializationFormatError

**When raised:** Unsupported serialization format.

**Attributes:**
- `format_name`: The unsupported format
- `supported_formats`: List of supported formats

**Example:**
```python
from unifyt import Quantity
from unifyt.serialization import save_quantity
from unifyt.exceptions import SerializationFormatError

try:
    q = Quantity(100, 'meter')
    save_quantity(q, 'data.xml', format='xml')  # XML not supported
except SerializationFormatError as e:
    print(f"Format '{e.format_name}' not supported")
    print(f"Use: {', '.join(e.supported_formats)}")
```

### DeserializationError

**When raised:** Loading data fails.

**Attributes:**
- `data`: The data that failed (or filename)
- `reason`: Why deserialization failed
- `format_hint`: Expected format

**Example:**
```python
from unifyt.serialization import load_quantity
from unifyt.exceptions import DeserializationError

try:
    q = load_quantity('corrupted.json')
except DeserializationError as e:
    print(f"Failed to load: {e.reason}")
```

### SerializationVersionError

**When raised:** Data version incompatible with library version.

**Attributes:**
- `data_version`: Version of serialized data
- `library_version`: Current library version

**Example:**
```python
from unifyt.serialization import load_quantity
from unifyt.exceptions import SerializationVersionError

try:
    q = load_quantity('old_format.json')
except SerializationVersionError as e:
    print(f"Data version {e.data_version} incompatible with {e.library_version}")
```

## Context Errors

### InvalidUnitSystemError

**When raised:** Invalid unit system specified.

**Attributes:**
- `system_name`: The invalid system name
- `available_systems`: List of available systems

**Example:**
```python
from unifyt import UnitContext
from unifyt.exceptions import InvalidUnitSystemError

try:
    with UnitContext('invalid_system'):
        pass
except InvalidUnitSystemError as e:
    print(f"System '{e.system_name}' not available")
    print(f"Available: {', '.join(e.available_systems)}")
```

### ContextStateError

**When raised:** Context state is invalid.

**Attributes:**
- `reason`: Why state is invalid

**Example:**
```python
from unifyt import UnitContext
from unifyt.exceptions import ContextStateError

try:
    ctx = UnitContext('SI')
    ctx.__exit__(None, None, None)  # Exit without enter
except ContextStateError as e:
    print(f"Invalid state: {e.reason}")
```

## Other Errors

### ConstantError

**When raised:** Accessing non-existent constant.

**Attributes:**
- `constant_name`: Name of constant
- `available_constants`: List of available constants

**Example:**
```python
from unifyt import constants
from unifyt.exceptions import ConstantError

try:
    c = constants.get_constant('invalid_constant')
except ConstantError as e:
    print(f"Constant '{e.constant_name}' not found")
    print(f"Available: {', '.join(e.available_constants[:5])}")
```

### ValidationError

**When raised:** Input validation fails.

**Attributes:**
- `parameter`: Parameter name
- `value`: Invalid value
- `constraint`: Constraint violated

**Example:**
```python
from unifyt.exceptions import ValidationError

try:
    # Some function requiring positive values
    validate_positive(-5)
except ValidationError as e:
    print(f"Parameter '{e.parameter}' failed: {e.constraint}")
```

### PrecisionError

**When raised:** Significant precision loss occurs.

**Attributes:**
- `operation`: Operation causing precision issues
- `precision_loss`: Estimated precision loss

**Example:**
```python
from unifyt import Quantity
from unifyt.exceptions import PrecisionError

try:
    huge = Quantity(1e308, 'meter')
    tiny = Quantity(1e-308, 'meter')
    result = huge + tiny  # Precision loss
except PrecisionError as e:
    print(f"Precision error in {e.operation}: {e.precision_loss}")
```

### ConfigurationError

**When raised:** Invalid configuration settings.

**Attributes:**
- `setting`: Configuration setting name
- `value`: Invalid value
- `reason`: Why it's invalid

**Example:**
```python
from unifyt.exceptions import ConfigurationError

try:
    configure(invalid_setting='value')
except ConfigurationError as e:
    print(f"Invalid config '{e.setting}': {e.reason}")
```

## Best Practices

### 1. Catch Specific Exceptions

Catch the most specific exception possible:

```python
from unifyt import Quantity
from unifyt.exceptions import ConversionError, UnitError

try:
    q = Quantity(100, 'meter')
    q.to('second')
except ConversionError as e:
    # Handle conversion errors specifically
    print(f"Conversion failed: {e}")
except UnitError as e:
    # Handle other unit errors
    print(f"Unit error: {e}")
```

### 2. Use Exception Attributes

Access exception attributes for detailed error handling:

```python
from unifyt import Quantity
from unifyt.exceptions import UnitNotFoundError

try:
    q = Quantity(100, 'metrs')
except UnitNotFoundError as e:
    if e.suggestions:
        print(f"Did you mean: {e.suggestions[0]}?")
        # Auto-correct or prompt user
```

### 3. Catch All Unifyt Errors

Use `UnifytException` to catch all library errors:

```python
from unifyt import Quantity
from unifyt.exceptions import UnifytException

try:
    # Complex operations
    result = perform_calculation()
except UnifytException as e:
    # Handle any Unifyt error
    log_error(e)
    raise
except Exception as e:
    # Handle non-Unifyt errors
    log_unexpected_error(e)
```

### 4. Provide Context

Add context to make debugging easier:

```python
from unifyt import Quantity
from unifyt.exceptions import UnifytException

def calculate_velocity(distance, time):
    try:
        return distance / time
    except UnifytException as e:
        raise type(e)(f"Error calculating velocity: {e.message}") from e
```

### 5. Validate Early

Validate inputs early to provide better error messages:

```python
from unifyt import Quantity
from unifyt.exceptions import InvalidValueError

def process_distance(value, unit):
    if value < 0:
        raise InvalidValueError(
            value,
            reason="distance cannot be negative",
            constraint="must be >= 0"
        )
    return Quantity(value, unit)
```

## Error Context Manager

Use the `ErrorContext` manager to add context to exceptions:

```python
from unifyt import Quantity
from unifyt.exceptions import ErrorContext

with ErrorContext("calculating average velocity"):
    distances = [Quantity(100, 'meter'), Quantity(200, 'meter')]
    times = [Quantity(10, 'second'), Quantity(20, 'second')]
    
    velocities = [d / t for d, t in zip(distances, times)]
    average = sum(velocities) / len(velocities)
```

If an error occurs, it will include the context:
```
ConversionError: Cannot convert from 'meter' to 'second' (context: calculating average velocity)
```

## Creating Custom Exceptions

For advanced use cases, you can create custom exceptions:

```python
from unifyt.exceptions import UnifytException, create_exception

# Using the helper function
exc = create_exception(
    UnifytException,
    "Custom error message",
    custom_attribute="value",
    error_code=42
)

# Or subclass directly
class MyCustomError(UnifytException):
    def __init__(self, message, custom_data):
        super().__init__(message)
        self.custom_data = custom_data
```

## Summary

The Unifyt exception system provides:

- **Clear hierarchy** for catching errors at different levels
- **Rich attributes** for detailed error handling
- **Helpful messages** with suggestions and context
- **Type safety** for better IDE support
- **Extensibility** for custom error handling

Always catch the most specific exception you can handle, and let unexpected errors propagate with their full context.
