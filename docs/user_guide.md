# Unifyt User Guide

## Introduction

Unifyt is a powerful Python library for working with physical quantities and units. It combines the best features of Pint and Unyt to provide an intuitive, high-performance solution for unit conversion and calculations.

## Installation

```bash
pip install unifyt
```

## Basic Concepts

### Quantities

A `Quantity` represents a numerical value with a physical unit:

```python
from unifyt import Quantity

distance = Quantity(100, 'meters')
time = Quantity(9.58, 'seconds')
```

### Units

Units can be simple (like 'meter') or compound (like 'meter/second'):

```python
from unifyt import Unit

length_unit = Unit('meter')
velocity_unit = Unit('meter/second')
area_unit = Unit('meter * meter')
```

## Working with Quantities

### Creating Quantities

```python
# With string units
mass = Quantity(75, 'kilogram')
distance = Quantity(42.195, 'kilometer')

# With arrays
import numpy as np
temperatures = Quantity(np.array([20, 25, 30]), 'celsius')
```

### Unit Conversions

```python
# Simple conversion
distance_m = Quantity(5, 'kilometer')
distance_mi = distance_m.to('mile')
print(distance_mi)  # 3.106855... mile

# Automatic conversion in operations
d1 = Quantity(1, 'kilometer')
d2 = Quantity(500, 'meter')
total = d1 + d2  # Result in kilometers
```

### Arithmetic Operations

```python
# Addition and subtraction (requires compatible units)
d1 = Quantity(100, 'meter')
d2 = Quantity(50, 'meter')
total = d1 + d2  # 150 meter

# Multiplication and division
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
speed = distance / time  # 10 meter/second

# Powers
area = Quantity(5, 'meter') ** 2  # 25 meter^2
```

### Comparisons

```python
d1 = Quantity(1, 'kilometer')
d2 = Quantity(1000, 'meter')

print(d1 == d2)  # True
print(d1 > Quantity(500, 'meter'))  # True
```

## Advanced Features

### Custom Units

```python
from unifyt import UnitRegistry

registry = UnitRegistry()
registry.define('furlong', '220 yard')
registry.define('fortnight', '14 day')

# Use custom units
distance = Quantity(1, 'furlong')
```

### Unit Systems

```python
from unifyt import UnitContext

# Use context manager for unit systems
with UnitContext('imperial'):
    distance = Quantity(100, 'foot')
    # Operations use imperial units
```

### Array Operations

```python
import numpy as np

# Create array quantities
distances = Quantity(np.array([100, 200, 300]), 'meter')
times = Quantity(np.array([10, 20, 30]), 'second')

# Perform operations
speeds = distances / times
print(speeds)  # [10, 10, 10] meter/second

# Convert arrays
speeds_kmh = speeds.to('kilometer/hour')
```

## Common Use Cases

### Physics Calculations

```python
# Kinetic energy: E = 1/2 * m * v^2
mass = Quantity(1000, 'kilogram')
velocity = Quantity(20, 'meter/second')
energy = 0.5 * mass * velocity ** 2
print(energy)  # 200000 kilogram * meter^2 / second^2 (Joules)
```

### Engineering Applications

```python
# Flow rate calculation
volume = Quantity(1000, 'liter')
time = Quantity(5, 'minute')
flow_rate = volume / time
print(flow_rate.to('liter/second'))
```

### Scientific Data Analysis

```python
import numpy as np

# Temperature data
temps_celsius = Quantity(np.array([20, 25, 30, 35]), 'celsius')

# Pressure data
pressures = Quantity(np.array([101.3, 102.1, 100.8, 99.5]), 'kilopascal')

# Perform analysis
mean_temp = Quantity(np.mean(temps_celsius.magnitude), 'celsius')
```

## Best Practices

1. **Always specify units**: Make your code self-documenting
2. **Use appropriate precision**: Consider floating-point limitations
3. **Check dimensionality**: Let Unifyt catch unit errors early
4. **Leverage array operations**: Use NumPy for efficient calculations
5. **Define custom units**: Create domain-specific units for clarity

## Error Handling

```python
# Incompatible unit operations raise errors
try:
    result = Quantity(100, 'meter') + Quantity(10, 'second')
except ValueError as e:
    print(f"Error: {e}")

# Incompatible conversions
try:
    result = Quantity(100, 'meter').to('second')
except ValueError as e:
    print(f"Error: {e}")
```

## Performance Tips

1. Use NumPy arrays for bulk operations
2. Minimize unit conversions in loops
3. Cache frequently used unit objects
4. Use base units for intensive calculations

## Next Steps

- Check out the [API Reference](api_reference.md) for detailed documentation
- Explore [Examples](../examples/) for more use cases
- Read about [Contributing](../CONTRIBUTING.md) to help improve Unifyt
