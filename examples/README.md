# Unifyt Examples

This directory contains example scripts demonstrating various features of the Unifyt library.

## Running Examples

Make sure Unifyt is installed:

```bash
pip install unifyt
```

Then run any example:

```bash
python examples/basic_usage.py
python examples/scientific_calculations.py
python examples/custom_units.py
python examples/array_operations.py
python examples/advanced_features.py
python examples/complete_demo.py
```

Or run all examples at once:

```bash
./run_examples.sh
```

## Example Files

### basic_usage.py
**Demonstrates fundamental operations:**
- Creating quantities with units
- Unit conversions (length, speed)
- Arithmetic operations (addition, multiplication, division)
- Powers and area calculations
- Comparison operations
- Basic formatting

**Best for:** First-time users learning the basics

### scientific_calculations.py
**Shows scientific and engineering applications:**
- Physics calculations (kinetic energy, potential energy)
- Chemistry examples (ideal gas law)
- Engineering problems (flow rates)
- Astronomy calculations (light-year distances)
- Array-based data analysis
- Real-world problem solving

**Best for:** Scientists and engineers

### custom_units.py
**Illustrates custom unit definitions:**
- Defining new units (furlong, fortnight)
- Creating unit aliases (m, km, s)
- Domain-specific units (parsec, angstrom)
- Using unusual unit combinations
- Unit registry management

**Best for:** Users needing specialized units

### array_operations.py
**Covers NumPy integration:**
- Creating array quantities
- Array conversions
- Element-wise operations
- Statistical calculations (mean, std, min, max)
- Broadcasting
- Filtering and indexing
- Matrix operations
- 2D array handling

**Best for:** Data scientists and analysts

### advanced_features.py
**Demonstrates advanced capabilities:**
- Physical constants (c, h, G, N_A, etc.)
- Using constants in calculations (E=mc²)
- Utility functions (linspace, arange, zeros, ones)
- Statistical operations on arrays
- Array manipulation (concatenate, stack)
- Clipping and comparison with tolerance
- Serialization (JSON, file I/O)
- Extended unit support (energy, power, pressure, volume, frequency)
- Angle conversions

**Best for:** Power users and advanced applications

### complete_demo.py
**Comprehensive showcase of all features:**
1. Basic operations
2. Extensive unit support (100+ units)
3. Physical constants (30+ constants)
4. Array operations
5. Utility functions
6. Custom units
7. Serialization
8. Scientific calculations
9. Performance features
10. Comparison and validation

**Best for:** Understanding the full capabilities of Unifyt

## Learning Path

### Beginner
1. Start with `basic_usage.py` to understand core concepts
2. Try `scientific_calculations.py` for practical applications
3. Explore `array_operations.py` for data handling

### Intermediate
4. Learn `custom_units.py` for extending the library
5. Study `advanced_features.py` for constants and utilities

### Advanced
6. Master `complete_demo.py` to see everything together
7. Read the documentation in `docs/` for deep dives
8. Experiment with your own use cases

## Quick Examples

### Simple Conversion
```python
from unifyt import Quantity

distance = Quantity(100, 'meter')
distance_km = distance.to('kilometer')
print(distance_km)  # 0.1 kilometer
```

### Using Constants
```python
from unifyt import Quantity, constants

mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2
print(energy)  # E = mc²
```

### Array Operations
```python
import numpy as np
from unifyt import Quantity, utils

temps = utils.linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
mean_temp = utils.mean(temps)
print(mean_temp)
```

### Custom Units
```python
from unifyt import Quantity, UnitRegistry

registry = UnitRegistry()
registry.define('furlong', '220 yard')
distance = Quantity(1, 'furlong')
print(distance.to('meter'))
```

## Features Demonstrated

### Units (100+)
- Length: meter, kilometer, mile, foot, inch, nanometer, angstrom
- Mass: kilogram, gram, pound, ounce, ton
- Time: second, minute, hour, day, week, year
- Energy: joule, calorie, kilowatt_hour, electronvolt
- Power: watt, kilowatt, horsepower
- Pressure: pascal, bar, atmosphere, psi, torr
- Force: newton, pound_force
- Frequency: hertz, megahertz, gigahertz
- Voltage: volt, millivolt, kilovolt
- Volume: liter, gallon, milliliter, cup
- Angle: radian, degree
- And more!

### Constants (30+)
- Fundamental: c, h, G, k_B, N_A, e, g
- Astronomical: AU, ly, pc, M_sun, M_earth, R_earth
- Atomic: m_e, m_p, m_n, a_0, u

### Utilities
- Array creation: linspace, arange, zeros, ones, full
- Statistics: sum, mean, std, min, max
- Math: sqrt, clip, isclose
- Array ops: concatenate, stack

### Serialization
- JSON format
- Pickle format
- File save/load
- Custom encoders

## Performance Tips

1. **Use arrays for bulk operations**
   ```python
   # Fast
   values = Quantity(np.arange(1000), 'meter')
   ```

2. **Minimize conversions in loops**
   ```python
   # Convert once, not in loop
   data = Quantity(values, 'meter')
   data_km = data.to('kilometer')
   ```

3. **Leverage utility functions**
   ```python
   # Use built-in utilities
   mean_val = utils.mean(data)
   ```

## Common Patterns

### Pattern 1: Data Analysis
```python
import numpy as np
from unifyt import Quantity, utils

# Load data with units
temperatures = Quantity(np.array([20, 25, 30, 35]), 'celsius')

# Analyze
mean_temp = utils.mean(temperatures)
std_temp = utils.std(temperatures)
```

### Pattern 2: Scientific Computing
```python
from unifyt import Quantity, constants

# Physics calculation
mass = Quantity(1000, 'kilogram')
velocity = Quantity(20, 'meter/second')
energy = 0.5 * mass * velocity ** 2
```

### Pattern 3: Unit Conversion Pipeline
```python
# Input in various units
d1 = Quantity(100, 'meter')
d2 = Quantity(0.5, 'kilometer')
d3 = Quantity(1000, 'foot')

# Normalize to common unit
total = d1 + d2.to('meter') + d3.to('meter')
```

## Troubleshooting

### Import Error
```bash
# Install unifyt
pip install unifyt
```

### Unit Not Found
```python
# Check available units in documentation
# Or define custom unit
from unifyt import UnitRegistry
registry = UnitRegistry()
registry.define('myunit', '10 meter')
```

### Incompatible Units
```python
# This will raise an error
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
# result = distance + time  # Error!

# Use compatible units
speed = distance / time  # OK
```

## Additional Resources

- [User Guide](../docs/user_guide.md) - Comprehensive documentation
- [API Reference](../docs/api_reference.md) - Complete API docs
- [Performance Guide](../docs/PERFORMANCE.md) - Optimization tips
- [Migration Guide](../docs/MIGRATION.md) - From Pint/Unyt
- [Main README](../README.md) - Project overview

## Contributing Examples

Have a great example? Contributions are welcome!

1. Create a new example file
2. Add clear comments and docstrings
3. Include print statements showing output
4. Update this README
5. Submit a pull request

## Questions?

- Check the documentation in `docs/`
- Review other examples
- Open an issue on GitHub
- Read the user guide

Happy calculating! 🚀
