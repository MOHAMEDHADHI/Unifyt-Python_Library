# Unifyt Quick Reference

## 🚀 Installation

```bash
pip install unifyt
```

## 📦 Basic Import

```python
from unifyt import Quantity, Unit, constants, utils
```

## 🎯 Creating Quantities

```python
# With scalar
q = Quantity(100, 'meter')

# With array
import numpy as np
q = Quantity(np.array([1, 2, 3]), 'meter')

# With Unit object
u = Unit('meter')
q = Quantity(100, u)
```

## 🔄 Unit Conversions

```python
# Convert to another unit
q_km = q.to('kilometer')

# Convert to base units
q_base = q.to_base_units()
```

## ➕ Arithmetic Operations

```python
# Addition/Subtraction (compatible units)
result = q1 + q2
result = q1 - q2

# Multiplication/Division
result = q1 * q2
result = q1 / q2

# Power
result = q ** 2

# Scalar operations
result = q * 5
result = q / 2
```

## 🔍 Comparisons

```python
# Equality
q1 == q2

# Ordering
q1 < q2
q1 > q2
q1 <= q2
q1 >= q2
```

## 📊 Array Operations

```python
import numpy as np
from unifyt import utils

# Create arrays
temps = utils.linspace(Quantity(0, 'C'), Quantity(100, 'C'), 11)
zeros = utils.zeros(10, 'meter')
ones = utils.ones((3, 3), 'kilogram')

# Statistics
mean = utils.mean(data)
std = utils.std(data)
total = utils.sum(data)
minimum = utils.min(data)
maximum = utils.max(data)

# Math
sqrt_val = utils.sqrt(quantity)
clipped = utils.clip(data, min_val, max_val)

# Array manipulation
combined = utils.concatenate([q1, q2])
stacked = utils.stack([q1, q2])
```

## 🌟 Physical Constants

```python
from unifyt import constants

# Fundamental
constants.c          # Speed of light
constants.h          # Planck constant
constants.G          # Gravitational constant
constants.k_B        # Boltzmann constant
constants.N_A        # Avogadro number
constants.e_charge   # Elementary charge
constants.g          # Standard gravity

# Astronomical
constants.AU         # Astronomical unit
constants.ly         # Light year
constants.pc         # Parsec
constants.M_sun      # Solar mass
constants.M_earth    # Earth mass
constants.R_earth    # Earth radius

# Atomic
constants.m_e        # Electron mass
constants.m_p        # Proton mass
constants.m_n        # Neutron mass
constants.a_0        # Bohr radius
constants.u          # Atomic mass unit

# Use in calculations
energy = mass * constants.c ** 2  # E = mc²
```

## 🎨 Custom Units

```python
from unifyt import UnitRegistry

registry = UnitRegistry()

# Define new unit
registry.define('furlong', '220 yard')

# Create alias
registry.alias('m', 'meter')

# Use custom unit
distance = Quantity(1, 'furlong')
```

## 💾 Serialization

```python
from unifyt.serialization import (
    save_quantity, load_quantity,
    quantity_to_json, json_to_quantity
)

# Save/load to file
save_quantity(q, 'data.json')
loaded = load_quantity('data.json')

# JSON string
json_str = quantity_to_json(q)
restored = json_to_quantity(json_str)
```

## ⚠️ Exception Handling

```python
from unifyt.exceptions import (
    UnifytException,      # Base exception
    UnitError,            # Unit errors
    DimensionalityError,  # Incompatible dimensions
    ConversionError,      # Cannot convert
    QuantityError,        # Quantity errors
)

try:
    result = distance.to('second')
except ConversionError as e:
    print(f"Cannot convert: {e}")
```

## 📏 Common Units

### Length
```python
'meter', 'm', 'kilometer', 'km', 'centimeter', 'cm', 'millimeter', 'mm'
'mile', 'mi', 'yard', 'yd', 'foot', 'ft', 'inch', 'in'
'nanometer', 'nm', 'angstrom', 'Å'
'light_year', 'ly', 'parsec', 'pc', 'astronomical_unit', 'AU'
```

### Mass
```python
'kilogram', 'kg', 'gram', 'g', 'milligram', 'mg'
'pound', 'lb', 'ounce', 'oz', 'ton', 'tonne'
'atomic_mass_unit', 'amu', 'u', 'dalton', 'Da'
'solar_mass', 'M_sun', 'earth_mass', 'M_earth'
```

### Time
```python
'second', 's', 'millisecond', 'ms', 'microsecond', 'us', 'nanosecond', 'ns'
'minute', 'min', 'hour', 'h', 'hr', 'day', 'd', 'week', 'year', 'yr'
'picosecond', 'ps', 'femtosecond', 'fs', 'attosecond', 'as'
```

### Temperature
```python
'kelvin', 'K', 'celsius', 'C', 'degC', 'fahrenheit', 'F', 'degF'
```

### Energy
```python
'joule', 'J', 'kilojoule', 'kJ', 'megajoule', 'MJ'
'calorie', 'cal', 'kilocalorie', 'kcal', 'Calorie'
'electronvolt', 'eV', 'megaelectronvolt', 'MeV'
'watt_hour', 'Wh', 'kilowatt_hour', 'kWh'
'british_thermal_unit', 'BTU'
```

### Power
```python
'watt', 'W', 'kilowatt', 'kW', 'megawatt', 'MW', 'gigawatt', 'GW'
'horsepower', 'hp', 'metric_horsepower', 'PS'
```

### Pressure
```python
'pascal', 'Pa', 'kilopascal', 'kPa', 'megapascal', 'MPa', 'gigapascal', 'GPa'
'bar', 'atmosphere', 'atm', 'psi', 'torr', 'mmHg', 'inHg'
```

### Force
```python
'newton', 'N', 'kilonewton', 'kN', 'meganewton', 'MN'
'dyne', 'kilogram_force', 'kgf', 'pound_force', 'lbf'
```

### Frequency
```python
'hertz', 'Hz', 'kilohertz', 'kHz', 'megahertz', 'MHz', 'gigahertz', 'GHz'
'terahertz', 'THz', 'rpm', 'rps'
```

### Voltage
```python
'volt', 'V', 'millivolt', 'mV', 'microvolt', 'uV'
'kilovolt', 'kV', 'megavolt', 'MV'
```

### Current
```python
'ampere', 'A', 'milliampere', 'mA', 'microampere', 'uA'
'kiloampere', 'kA'
```

### Volume
```python
'liter', 'L', 'milliliter', 'mL'
'gallon', 'gal', 'quart', 'qt', 'pint', 'pt', 'cup', 'fluid_ounce', 'fl_oz'
```

### Angle
```python
'radian', 'rad', 'degree', 'deg', 'arcminute', 'arcsecond', 'gradian', 'grad'
```

### Data
```python
'bit', 'b', 'byte', 'B'
'kilobyte', 'kB', 'megabyte', 'MB', 'gigabyte', 'GB', 'terabyte', 'TB'
'kibibyte', 'KiB', 'mebibyte', 'MiB', 'gibibyte', 'GiB', 'tebibyte', 'TiB'
```

### Electromagnetic
```python
'farad', 'F', 'microfarad', 'uF', 'nanofarad', 'nF', 'picofarad', 'pF'
'henry', 'H', 'millihenry', 'mH', 'microhenry', 'uH'
'tesla', 'T', 'gauss', 'G', 'weber', 'Wb', 'maxwell', 'Mx'
```

### Radioactivity
```python
'becquerel', 'Bq', 'curie', 'Ci', 'rutherford', 'Rd'
'gray', 'Gy', 'sievert', 'Sv', 'rad', 'rem'
```

## 🎓 Common Patterns

### Physics Calculation
```python
# Kinetic energy: E = ½mv²
mass = Quantity(1000, 'kilogram')
velocity = Quantity(20, 'meter/second')
energy = 0.5 * mass * velocity ** 2
```

### Unit Conversion Pipeline
```python
# Convert and combine
d1 = Quantity(100, 'meter')
d2 = Quantity(0.5, 'kilometer')
total = d1 + d2.to('meter')
```

### Array Processing
```python
# Process array data
distances = Quantity(np.array([100, 200, 300]), 'meter')
times = Quantity(np.array([10, 20, 30]), 'second')
speeds = distances / times
mean_speed = utils.mean(speeds)
```

### Error Handling
```python
from unifyt.exceptions import ConversionError

try:
    result = distance.to('second')
except ConversionError:
    print("Cannot convert length to time")
```

## 💡 Tips & Tricks

### Tip 1: Use Type Hints
```python
from unifyt import Quantity

def calculate_speed(distance: Quantity, time: Quantity) -> Quantity:
    return distance / time
```

### Tip 2: Check Compatibility
```python
if unit1.is_compatible_with(unit2):
    result = q1 + q2
```

### Tip 3: Use Constants
```python
# Instead of hardcoding
energy = mass * constants.c ** 2  # ✅

# Don't do this
c = 299792458  # ❌
energy = mass * c ** 2
```

### Tip 4: Batch Conversions
```python
# Convert array all at once
data_km = data_m.to('kilometer')  # ✅

# Don't loop
# for val in data_m: ...  # ❌
```

### Tip 5: Use Utilities
```python
# Use built-in utilities
mean = utils.mean(data)  # ✅

# Don't reinvent
# mean = Quantity(np.mean(data.magnitude), data.unit)  # ❌
```

## 📚 Documentation Links

- **Complete Guide**: [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)
- **Getting Started**: [GETTING_STARTED.md](GETTING_STARTED.md)
- **Units Catalog**: [UNITS_CATALOG.md](starter documents/UNITS_CATALOG.md)
- **Exceptions Guide**: [EXCEPTIONS_GUIDE.md](EXCEPTIONS_GUIDE.md)
- **API Reference**: [docs/api_reference.md](docs/api_reference.md)
- **Examples**: [examples/](examples/)

## 🆘 Getting Help

```python
# Get help on any object
help(Quantity)
help(constants)
help(utils)

# List available constants
constants.list_constants()

# Check unit compatibility
unit1.is_compatible_with(unit2)
```

## 🎯 Common Use Cases

### Scientific Computing
```python
# E = mc²
energy = mass * constants.c ** 2

# F = ma
force = mass * acceleration

# PV = nRT
pressure * volume == n * constants.R * temperature
```

### Engineering
```python
# Power = Voltage × Current
power = voltage * current

# Flow rate
flow = volume / time

# Stress = Force / Area
stress = force / area
```

### Data Analysis
```python
# Temperature analysis
temps = Quantity(data, 'celsius')
mean_temp = utils.mean(temps)
std_temp = utils.std(temps)
```

---

**Unifyt v0.2.0** - Quick Reference  
**For detailed information, see [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)**

**Happy calculating!** 🚀
