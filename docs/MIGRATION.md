# Migration Guide

## Migrating from Pint

If you're coming from Pint, here's how to adapt your code:

### Basic Usage

**Pint:**
```python
import pint
ureg = pint.UnitRegistry()
distance = 100 * ureg.meter
```

**Unifyt:**
```python
from unifyt import Quantity
distance = Quantity(100, 'meter')
```

### Unit Conversions

**Pint:**
```python
distance_km = distance.to(ureg.kilometer)
```

**Unifyt:**
```python
distance_km = distance.to('kilometer')
```

### Arithmetic

Both libraries work similarly:
```python
# Both Pint and Unifyt
speed = distance / time
```

### Custom Units

**Pint:**
```python
ureg.define('furlong = 220 * yard')
```

**Unifyt:**
```python
from unifyt import UnitRegistry
registry = UnitRegistry()
registry.define('furlong', '220 yard')
```

### Key Differences

1. **No global registry required** - Unifyt works without explicit registry
2. **Simpler API** - Direct Quantity creation
3. **Better array support** - Optimized for NumPy
4. **Built-in constants** - Physical constants included

## Migrating from Unyt

### Basic Usage

**Unyt:**
```python
import unyt
distance = unyt.unyt_quantity(100, 'meter')
```

**Unifyt:**
```python
from unifyt import Quantity
distance = Quantity(100, 'meter')
```

### Arrays

**Unyt:**
```python
import numpy as np
distances = unyt.unyt_array([100, 200, 300], 'meter')
```

**Unifyt:**
```python
import numpy as np
from unifyt import Quantity
distances = Quantity(np.array([100, 200, 300]), 'meter')
```

### Unit Systems

**Unyt:**
```python
distance.to('cgs')
```

**Unifyt:**
```python
from unifyt import UnitContext
with UnitContext('cgs'):
    # Use CGS units
    pass
```

### Key Differences

1. **Unified Quantity class** - No separate array class
2. **More utility functions** - Built-in statistical operations
3. **Physical constants** - Included in library
4. **Better serialization** - JSON and pickle support

## Common Patterns

### Pattern 1: Creating Quantities

```python
# Old (Pint/Unyt)
q = 100 * ureg.meter
q = unyt.unyt_quantity(100, 'meter')

# New (Unifyt)
q = Quantity(100, 'meter')
```

### Pattern 2: Unit Conversions

```python
# Old (Pint/Unyt)
q_km = q.to(ureg.kilometer)
q_km = q.to('kilometer')

# New (Unifyt)
q_km = q.to('kilometer')
```

### Pattern 3: Array Operations

```python
# Old (Pint)
values = [100, 200, 300] * ureg.meter

# Old (Unyt)
values = unyt.unyt_array([100, 200, 300], 'meter')

# New (Unifyt)
values = Quantity(np.array([100, 200, 300]), 'meter')
```

### Pattern 4: Physical Constants

```python
# Old (Pint)
from scipy import constants
c = constants.c * ureg.meter / ureg.second

# Old (Unyt)
from unyt import physical_constants
c = physical_constants.speed_of_light

# New (Unifyt)
from unifyt import constants
c = constants.c  # Already has units!
```

## Feature Comparison

| Feature | Pint | Unyt | Unifyt |
|---------|------|------|-------|
| Basic units | ✓ | ✓ | ✓ |
| Custom units | ✓ | ✓ | ✓ |
| Array support | ✓ | ✓✓ | ✓✓ |
| Physical constants | - | ✓ | ✓✓ |
| Utility functions | - | - | ✓✓ |
| Serialization | ✓ | ✓ | ✓✓ |
| Type hints | ✓ | ✓ | ✓✓ |
| Performance | ✓ | ✓✓ | ✓✓ |
| Documentation | ✓✓ | ✓ | ✓✓ |

Legend: ✓ = Supported, ✓✓ = Well supported, - = Not supported

## Tips for Migration

1. **Start with imports**: Replace your import statements first
2. **Update quantity creation**: Change to Unifyt's Quantity syntax
3. **Test conversions**: Verify unit conversions work as expected
4. **Use new features**: Take advantage of constants and utilities
5. **Update tests**: Ensure your test suite passes

## Compatibility Notes

### What Works the Same

- Basic arithmetic operations
- Unit conversions
- Comparison operations
- NumPy integration
- Most common units

### What's Different

- No global registry needed
- Simpler API
- Different constant names
- Enhanced array support
- Additional utility functions

### What's New

- Built-in physical constants
- Utility functions (linspace, arange, etc.)
- Better serialization
- Performance optimizations
- More comprehensive documentation

## Getting Help

If you encounter issues during migration:

1. Check the [User Guide](user_guide.md)
2. Review [Examples](../examples/)
3. Read the [API Reference](api_reference.md)
4. Open an issue on GitHub
