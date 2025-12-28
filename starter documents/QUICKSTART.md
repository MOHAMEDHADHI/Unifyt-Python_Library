# Unifyt Quick Start Guide

Get up and running with Unifyt in 5 minutes!

## Installation

```bash
pip install unifyt
```

## Your First Quantity

```python
from unifyt import Quantity

# Create a quantity
distance = Quantity(100, 'meters')
print(distance)  # 100 meters
```

## Basic Operations

```python
from unifyt import Quantity

# Create quantities
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')

# Calculate speed
speed = distance / time
print(speed)  # 10.0 meter / second

# Convert units
speed_kmh = speed.to('kilometer/hour')
print(speed_kmh)  # 36.0 kilometer / hour
```

## Unit Conversions

```python
# Length conversions
distance_m = Quantity(5, 'kilometer')
distance_mi = distance_m.to('mile')
print(distance_mi)  # 3.106855... mile

# Time conversions
time_s = Quantity(120, 'second')
time_min = time_s.to('minute')
print(time_min)  # 2.0 minute
```

## Arithmetic

```python
# Addition (requires compatible units)
d1 = Quantity(100, 'meter')
d2 = Quantity(50, 'meter')
total = d1 + d2
print(total)  # 150 meter

# Multiplication
length = Quantity(10, 'meter')
width = Quantity(5, 'meter')
area = length * width
print(area)  # 50 meter * meter

# Powers
side = Quantity(3, 'meter')
volume = side ** 3
print(volume)  # 27 meter^3
```

## Working with Arrays

```python
import numpy as np
from unifyt import Quantity

# Create array quantity
distances = Quantity(np.array([100, 200, 300]), 'meter')
times = Quantity(np.array([10, 20, 30]), 'second')

# Calculate speeds
speeds = distances / times
print(speeds)  # [10. 10. 10.] meter / second

# Convert all at once
speeds_kmh = speeds.to('kilometer/hour')
print(speeds_kmh)  # [36. 36. 36.] kilometer / hour
```

## Common Patterns

### Physics Calculation

```python
# Kinetic energy: E = 1/2 * m * v^2
mass = Quantity(1000, 'kilogram')
velocity = Quantity(20, 'meter/second')
energy = 0.5 * mass * velocity ** 2
print(energy)  # 200000.0 kilogram * meter^2 / second^2
```

### Engineering Application

```python
# Flow rate
volume = Quantity(1000, 'liter')
time = Quantity(5, 'minute')
flow_rate = volume / time
print(flow_rate.to('liter/second'))  # 3.333... liter / second
```

### Data Analysis

```python
import numpy as np

# Temperature measurements
temps = Quantity(np.array([20, 25, 30, 35]), 'celsius')
mean_temp = Quantity(np.mean(temps.magnitude), 'celsius')
print(f"Mean temperature: {mean_temp}")
```

## Next Steps

- Read the [User Guide](docs/user_guide.md) for detailed information
- Check out [Examples](examples/) for more use cases
- Browse the [API Reference](docs/api_reference.md) for complete documentation

## Common Units

### Length
`meter`, `kilometer`, `centimeter`, `millimeter`, `mile`, `yard`, `foot`, `inch`

### Mass
`kilogram`, `gram`, `milligram`, `pound`, `ounce`, `ton`

### Time
`second`, `minute`, `hour`, `day`, `week`, `year`

### Temperature
`kelvin`, `celsius`, `fahrenheit`

## Tips

1. Always specify units - it makes your code self-documenting
2. Use `.to()` for explicit conversions
3. Let Unifyt catch unit errors early in development
4. Use NumPy arrays for bulk operations
5. Check the examples directory for inspiration

Happy calculating! 🚀
