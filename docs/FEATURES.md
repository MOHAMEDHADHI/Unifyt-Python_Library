# Unifyt Features

## Core Features

### 1. Intuitive Quantity System

Create physical quantities with ease:

```python
distance = Quantity(100, 'meters')
time = Quantity(10, 'seconds')
speed = distance / time
```

### 2. Automatic Unit Conversion

Units are automatically converted when needed:

```python
d1 = Quantity(1, 'kilometer')
d2 = Quantity(500, 'meter')
total = d1 + d2  # Automatically converts to common unit
```

### 3. Dimensionality Checking

Prevents invalid operations:

```python
# This will raise an error
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
invalid = distance + time  # ValueError: incompatible dimensions
```

### 4. Comprehensive Unit Support

#### Length Units
- SI: meter, kilometer, centimeter, millimeter
- Imperial: mile, yard, foot, inch

#### Mass Units
- SI: kilogram, gram, milligram
- Imperial: pound, ounce, ton

#### Time Units
- second, minute, hour, day, week, year

#### Temperature Units
- kelvin, celsius, fahrenheit

#### And more...
- Electric current (ampere)
- Amount of substance (mole)
- Luminous intensity (candela)

### 5. NumPy Integration

Seamless array operations:

```python
import numpy as np

distances = Quantity(np.array([100, 200, 300]), 'meter')
times = Quantity(np.array([10, 20, 30]), 'second')
speeds = distances / times
```

### 6. Custom Unit Definitions

Define domain-specific units:

```python
registry = UnitRegistry()
registry.define('furlong', '220 yard')
registry.define('parsec', '3.086e16 meter')
```

### 7. Unit System Contexts

Switch between unit systems:

```python
with UnitContext('imperial'):
    # Use imperial units
    distance = Quantity(100, 'foot')
```

### 8. Type Safety

Full type hints for IDE support:

```python
from unifyt import Quantity, Unit

def calculate_speed(distance: Quantity, time: Quantity) -> Quantity:
    return distance / time
```

## Advanced Features

### Compound Units

Create complex units:

```python
# Velocity
velocity = Unit('meter/second')

# Acceleration
acceleration = Unit('meter/second/second')

# Force (derived)
force = Unit('kilogram * meter / second / second')
```

### Power Operations

Raise quantities to powers:

```python
length = Quantity(5, 'meter')
area = length ** 2  # 25 meter^2
volume = length ** 3  # 125 meter^3
```

### Comparison Operations

Compare quantities with automatic conversion:

```python
d1 = Quantity(1, 'kilometer')
d2 = Quantity(1000, 'meter')
print(d1 == d2)  # True
print(d1 > Quantity(500, 'meter'))  # True
```

### Array Broadcasting

NumPy-style broadcasting:

```python
velocities = Quantity(np.array([10, 20, 30]), 'meter/second')
scaled = velocities * 2  # Element-wise multiplication
```

### Statistical Operations

Work with statistical functions:

```python
data = Quantity(np.array([10, 20, 30, 40, 50]), 'meter')
mean = Quantity(np.mean(data.magnitude), 'meter')
std = Quantity(np.std(data.magnitude), 'meter')
```

## Performance Features

### Optimized Conversions

Conversion factors are calculated efficiently:

```python
# Fast conversion
distance_km = Quantity(1000, 'meter').to('kilometer')
```

### Array Operations

Vectorized operations for speed:

```python
# Fast array operations
large_array = Quantity(np.random.rand(10000), 'meter')
converted = large_array.to('kilometer')  # Vectorized
```

### Minimal Overhead

Lightweight implementation:

- No unnecessary conversions
- Efficient dimension tracking
- Optimized arithmetic operations

## Usability Features

### Clear Error Messages

Helpful error messages:

```python
try:
    result = Quantity(100, 'meter') + Quantity(10, 'second')
except ValueError as e:
    print(e)  # "Cannot add meter and second"
```

### Flexible Input

Multiple ways to specify units:

```python
# Full names
d1 = Quantity(100, 'meter')

# Abbreviations
d2 = Quantity(100, 'm')

# Compound units
v = Quantity(10, 'meter/second')
v = Quantity(10, 'm/s')
```

### Pretty Printing

Human-readable output:

```python
q = Quantity(100, 'meter')
print(q)  # "100 meter"
print(f"{q:.2f}")  # "100.00 meter"
```

## Integration Features

### Works with Standard Library

Compatible with Python's math operations:

```python
import math

angle = Quantity(45, 'degree')
# Can be used in calculations
```

### NumPy Compatible

Full NumPy integration:

```python
import numpy as np

data = Quantity(np.array([1, 2, 3]), 'meter')
result = np.sum(data.magnitude)
```

### Type Checking

Works with mypy and other type checkers:

```python
def process(q: Quantity) -> Quantity:
    return q.to('meter')
```

## Extensibility Features

### Custom Units

Easy to add new units:

```python
registry.define('smoot', '1.7018 meter')
```

### Unit Aliases

Create convenient shortcuts:

```python
registry.alias('m', 'meter')
registry.alias('km', 'kilometer')
```

### Plugin System

Extend functionality (future feature):

```python
# Coming soon: plugin support for custom conversions
```

## Documentation Features

### Comprehensive Docs

- User guide with examples
- Complete API reference
- Example scripts
- Quick start guide

### Inline Documentation

Full docstrings:

```python
help(Quantity)  # Shows detailed documentation
```

### Type Hints

Better IDE support:

```python
# IDE will show type information
q = Quantity(100, 'meter')
q.to('kilometer')  # IDE knows return type
```

## Testing Features

### Comprehensive Test Suite

- Unit tests for all features
- Integration tests
- Edge case coverage
- Array operation tests

### High Code Coverage

Maintained test coverage for reliability.

### Continuous Testing

Easy to run tests:

```bash
pytest tests/
```

## Future Features (Roadmap)

- Temperature offset conversions (Celsius/Fahrenheit)
- Currency units with exchange rates
- More unit systems (CGS, atomic units)
- Performance optimizations
- Plugin architecture
- Serialization support (JSON, pickle)
- Database integration helpers
- Plotting integration (matplotlib)
