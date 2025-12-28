# Getting Started with Unifyt

Welcome to Unifyt! This guide will help you get up and running in minutes.

## Installation

### From PyPI (when published)
```bash
pip install unifyt
```

### From Source (Development)
```bash
# Clone the repository
git clone https://github.com/yourusername/unifyt.git
cd unifyt

# Install in development mode
pip install -e .

# Or use the setup script
./setup_dev.sh
```

## Your First Unifyt Program

Create a file called `first_unifyt.py`:

```python
from unifyt import Quantity

# Create a quantity
distance = Quantity(100, 'meter')
print(f"Distance: {distance}")

# Convert units
distance_km = distance.to('kilometer')
print(f"Distance in km: {distance_km}")

# Do calculations
time = Quantity(10, 'second')
speed = distance / time
print(f"Speed: {speed}")
print(f"Speed in km/h: {speed.to('kilometer/hour')}")
```

Run it:
```bash
python first_unifyt.py
```

Output:
```
Distance: 100 meter
Distance in km: 0.1 kilometer
Speed: 10.0 meter / second
Speed in km/h: 36.0 kilometer / hour
```

## Core Concepts

### 1. Quantities

A `Quantity` is a value with a unit:

```python
from unifyt import Quantity

# Create quantities
length = Quantity(5, 'meter')
mass = Quantity(10, 'kilogram')
time = Quantity(2, 'second')

# Access value and unit
print(length.magnitude)  # 5
print(length.unit)       # meter
```

### 2. Unit Conversions

Convert between compatible units:

```python
# Length conversions
distance_m = Quantity(1000, 'meter')
distance_km = distance_m.to('kilometer')  # 1.0 km
distance_mi = distance_m.to('mile')       # 0.621... miles

# Time conversions
time_s = Quantity(3600, 'second')
time_h = time_s.to('hour')  # 1.0 hour
time_d = time_s.to('day')   # 0.0416... day
```

### 3. Arithmetic Operations

Perform calculations with units:

```python
# Addition (requires compatible units)
d1 = Quantity(100, 'meter')
d2 = Quantity(50, 'meter')
total = d1 + d2  # 150 meter

# Multiplication
length = Quantity(10, 'meter')
width = Quantity(5, 'meter')
area = length * width  # 50 meter^2

# Division
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
speed = distance / time  # 10 meter/second

# Powers
side = Quantity(3, 'meter')
volume = side ** 3  # 27 meter^3
```

### 4. Arrays

Work with NumPy arrays:

```python
import numpy as np
from unifyt import Quantity

# Create array quantity
distances = Quantity(np.array([100, 200, 300]), 'meter')

# Convert all at once
distances_km = distances.to('kilometer')
# [0.1, 0.2, 0.3] kilometer

# Arithmetic with arrays
times = Quantity(np.array([10, 20, 30]), 'second')
speeds = distances / times
# [10, 10, 10] meter/second
```

### 5. Physical Constants

Use built-in constants:

```python
from unifyt import constants

# Access constants
print(constants.c)    # Speed of light
print(constants.g)    # Standard gravity
print(constants.N_A)  # Avogadro number

# Use in calculations
mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2  # E = mc²
```

### 6. Utility Functions

Helpful utilities for common tasks:

```python
from unifyt import utils

# Create ranges
temps = utils.linspace(
    Quantity(0, 'celsius'),
    Quantity(100, 'celsius'),
    11
)

# Statistics
data = Quantity(np.array([10, 20, 30, 40, 50]), 'meter')
mean = utils.mean(data)
std = utils.std(data)
```

## Common Use Cases

### Physics Calculations

```python
from unifyt import Quantity, constants

# Kinetic energy: E = 1/2 * m * v²
mass = Quantity(1000, 'kilogram')
velocity = Quantity(20, 'meter/second')
energy = 0.5 * mass * velocity ** 2
print(f"Kinetic energy: {energy}")

# Gravitational force: F = G * m1 * m2 / r²
m1 = Quantity(1000, 'kilogram')
m2 = Quantity(500, 'kilogram')
r = Quantity(10, 'meter')
force = constants.G * m1 * m2 / (r ** 2)
print(f"Gravitational force: {force}")
```

### Engineering Applications

```python
# Flow rate calculation
volume = Quantity(1000, 'liter')
time = Quantity(5, 'minute')
flow_rate = volume / time
print(f"Flow rate: {flow_rate.to('liter/second')}")

# Power calculation
voltage = Quantity(120, 'volt')
current = Quantity(10, 'ampere')
power = voltage * current
print(f"Power: {power.to('watt')}")
```

### Data Analysis

```python
import numpy as np
from unifyt import Quantity, utils

# Temperature measurements
temps = Quantity(
    np.array([20, 22, 25, 23, 21, 24, 26]),
    'celsius'
)

# Analyze
print(f"Mean: {utils.mean(temps)}")
print(f"Std: {utils.std(temps)}")
print(f"Min: {utils.min(temps)}")
print(f"Max: {utils.max(temps)}")
```

### Custom Units

```python
from unifyt import Quantity, UnitRegistry

# Create registry
registry = UnitRegistry()

# Define custom units
registry.define('furlong', '220 yard')
registry.define('fortnight', '14 day')

# Use them
distance = Quantity(1, 'furlong')
print(f"1 furlong = {distance.to('meter')}")

time = Quantity(1, 'fortnight')
print(f"1 fortnight = {time.to('hour')}")
```

## Next Steps

### Run the Examples

```bash
# Run all examples
./run_examples.sh

# Or run individually
python examples/basic_usage.py
python examples/scientific_calculations.py
python examples/advanced_features.py
python examples/complete_demo.py
```

### Read the Documentation

- [User Guide](docs/user_guide.md) - Comprehensive guide
- [API Reference](docs/api_reference.md) - Complete API docs
- [Quick Start](QUICKSTART.md) - 5-minute guide
- [Features](docs/FEATURES.md) - Feature list
- [Performance](docs/PERFORMANCE.md) - Optimization tips

### Explore Features

1. **100+ Units**: length, mass, time, energy, power, pressure, etc.
2. **30+ Constants**: physical and astronomical constants
3. **Array Support**: NumPy integration
4. **Utilities**: linspace, arange, statistics, etc.
5. **Serialization**: JSON and pickle support
6. **Custom Units**: Define your own units
7. **Type Hints**: Full IDE support

## Tips for Success

### 1. Always Specify Units

```python
# Good
distance = Quantity(100, 'meter')

# Avoid bare numbers when units matter
# distance = 100  # What unit?
```

### 2. Use Appropriate Units

```python
# Use the right unit for your domain
distance = Quantity(5, 'kilometer')  # Not 5000 meters
time = Quantity(2, 'hour')           # Not 7200 seconds
```

### 3. Let Unifyt Check Dimensions

```python
# Unifyt will catch errors
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')

# This will raise an error (good!)
# result = distance + time  # Can't add length and time
```

### 4. Use Arrays for Bulk Data

```python
# Efficient
data = Quantity(np.arange(1000), 'meter')

# Less efficient
# data = [Quantity(i, 'meter') for i in range(1000)]
```

### 5. Leverage Constants

```python
# Use built-in constants
from unifyt import constants

# Don't hardcode
# c = 299792458  # m/s

# Use constant
c = constants.c
```

## Common Pitfalls

### 1. Incompatible Units

```python
# This will error
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
# result = distance + time  # Error!

# Solution: only add compatible units
d1 = Quantity(100, 'meter')
d2 = Quantity(50, 'meter')
result = d1 + d2  # OK
```

### 2. Forgetting to Convert

```python
# Remember to convert when needed
d1 = Quantity(1, 'kilometer')
d2 = Quantity(500, 'meter')

# Automatic conversion in operations
total = d1 + d2  # Unifyt handles this

# But explicit is better
total = d1.to('meter') + d2  # Clear intent
```

### 3. Unit String Typos

```python
# Typo in unit name
# distance = Quantity(100, 'metres')  # Error!

# Correct
distance = Quantity(100, 'meter')  # or 'meters'
```

## Getting Help

### Documentation
- Check `docs/` directory
- Read examples in `examples/`
- Review API reference

### Community
- Open an issue on GitHub
- Check existing issues
- Read CONTRIBUTING.md

### Debugging

```python
# Check unit
q = Quantity(100, 'meter')
print(q.unit)           # meter
print(q.dimensionality) # Dimension(length=1)

# Check value
print(q.magnitude)      # 100
print(q.value)          # array([100])

# Test conversions
print(q.to('kilometer')) # 0.1 kilometer
```

## Quick Reference

### Creating Quantities
```python
q = Quantity(value, 'unit')
q = Quantity(np.array([...]), 'unit')
```

### Converting Units
```python
q_new = q.to('new_unit')
q_base = q.to_base_units()
```

### Arithmetic
```python
q1 + q2  # Addition
q1 - q2  # Subtraction
q1 * q2  # Multiplication
q1 / q2  # Division
q ** n   # Power
```

### Comparisons
```python
q1 == q2  # Equality
q1 < q2   # Less than
q1 > q2   # Greater than
```

### Arrays
```python
utils.linspace(start, stop, num)
utils.arange(start, stop, step)
utils.mean(q)
utils.std(q)
```

### Constants
```python
constants.c    # Speed of light
constants.g    # Gravity
constants.N_A  # Avogadro
```

## What's Next?

1. **Try the examples**: Run `./run_examples.sh`
2. **Read the user guide**: `docs/user_guide.md`
3. **Build something**: Apply Unifyt to your project
4. **Contribute**: Help improve Unifyt

Welcome to the Unifyt community! 🚀
