# Unifyt Quick Reference Card

## 🚀 Installation

```bash
pip install unifyt
```

## 📦 Import

```python
from unifyt import Quantity, Unit, constants, utils
```

## 🎯 Basic Usage

### Create Quantities
```python
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
mass = Quantity(5, 'kilogram')
```

### Convert Units
```python
distance_km = distance.to('kilometer')  # 0.1 km
time_min = time.to('minute')            # 0.166... min
```

### Arithmetic
```python
speed = distance / time                 # 10 m/s
area = Quantity(5, 'm') ** 2           # 25 m²
total = Quantity(1, 'km') + Quantity(500, 'm')  # 1.5 km
```

## 📐 Common Units

### Length
```python
'meter', 'm', 'kilometer', 'km', 'centimeter', 'cm'
'mile', 'mi', 'foot', 'ft', 'inch', 'in'
'nanometer', 'nm', 'angstrom'
```

### Mass
```python
'kilogram', 'kg', 'gram', 'g', 'milligram', 'mg'
'pound', 'lb', 'ounce', 'oz', 'ton'
```

### Time
```python
'second', 's', 'minute', 'min', 'hour', 'h'
'day', 'd', 'week', 'year', 'yr'
'millisecond', 'ms', 'microsecond', 'us'
```

### Energy
```python
'joule', 'J', 'kilojoule', 'kJ'
'calorie', 'cal', 'kilocalorie', 'kcal'
'kilowatt_hour', 'kWh', 'electronvolt', 'eV'
```

### Power
```python
'watt', 'W', 'kilowatt', 'kW', 'megawatt', 'MW'
'horsepower', 'hp'
```

### Pressure
```python
'pascal', 'Pa', 'kilopascal', 'kPa'
'bar', 'atmosphere', 'atm', 'psi', 'torr'
```

### Volume
```python
'liter', 'L', 'milliliter', 'mL'
'gallon', 'gal', 'quart', 'qt', 'pint', 'pt'
```

### Frequency
```python
'hertz', 'Hz', 'kilohertz', 'kHz'
'megahertz', 'MHz', 'gigahertz', 'GHz'
```

### Angle
```python
'radian', 'rad', 'degree', 'deg'
```

## 🔬 Physical Constants

```python
constants.c          # Speed of light
constants.h          # Planck constant
constants.G          # Gravitational constant
constants.N_A        # Avogadro number
constants.k_B        # Boltzmann constant
constants.g          # Standard gravity
constants.e_charge   # Elementary charge
constants.m_e        # Electron mass
constants.m_p        # Proton mass
constants.AU         # Astronomical unit
constants.ly         # Light year
constants.M_sun      # Solar mass
```

## 🛠️ Utility Functions

### Array Creation
```python
utils.linspace(start, stop, num)    # Evenly spaced
utils.arange(start, stop, step)     # Range with step
utils.zeros(shape, unit)            # Array of zeros
utils.ones(shape, unit)             # Array of ones
utils.full(shape, fill_value)       # Filled array
```

### Statistics
```python
utils.sum(quantity)                 # Sum
utils.mean(quantity)                # Mean
utils.std(quantity)                 # Standard deviation
utils.min(quantity)                 # Minimum
utils.max(quantity)                 # Maximum
```

### Math
```python
utils.sqrt(quantity)                # Square root
utils.clip(q, min_val, max_val)    # Clip values
utils.isclose(q1, q2)               # Compare with tolerance
```

### Array Operations
```python
utils.concatenate([q1, q2])         # Join arrays
utils.stack([q1, q2])               # Stack arrays
```

## 📊 Array Operations

```python
import numpy as np

# Create array quantity
distances = Quantity(np.array([100, 200, 300]), 'meter')

# Convert all at once
distances_km = distances.to('kilometer')

# Arithmetic with arrays
times = Quantity(np.array([10, 20, 30]), 'second')
speeds = distances / times

# Statistics
mean_speed = utils.mean(speeds)
```

## 💾 Serialization

```python
from unifyt.serialization import save_quantity, load_quantity

# Save to file
save_quantity(distance, 'distance.json')

# Load from file
loaded = load_quantity('distance.json')

# JSON string
json_str = quantity_to_json(distance)
q = json_to_quantity(json_str)
```

## 🎨 Custom Units

```python
from unifyt import UnitRegistry

registry = UnitRegistry()
registry.define('furlong', '220 yard')
registry.define('fortnight', '14 day')

distance = Quantity(1, 'furlong')
print(distance.to('meter'))
```

## 🔄 Unit Contexts

```python
from unifyt import UnitContext

with UnitContext('imperial'):
    # Use imperial units
    distance = Quantity(100, 'foot')
```

## 📈 Common Patterns

### Physics Calculation
```python
# Kinetic energy: E = 1/2 * m * v²
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

### Array Analysis
```python
# Temperature data
temps = Quantity(np.array([20, 25, 30, 35]), 'celsius')
mean_temp = utils.mean(temps)
std_temp = utils.std(temps)
```

### Using Constants
```python
# E = mc²
mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2
print(energy.to('kilowatt_hour'))
```

## 🎯 Quick Commands

### Development
```bash
make test          # Run tests
make format        # Format code
make lint          # Run linters
make examples      # Run examples
make clean         # Clean temp files
```

### Scripts
```bash
./run_tests.sh     # Run test suite
./run_examples.sh  # Run all examples
./check_code.sh    # Check code quality
./clean.sh         # Clean project
```

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Project overview |
| [GETTING_STARTED.md](GETTING_STARTED.md) | Tutorial |
| [QUICKSTART.md](QUICKSTART.md) | 5-min intro |
| [INDEX.md](INDEX.md) | Navigation |
| [docs/user_guide.md](docs/user_guide.md) | Complete guide |
| [docs/api_reference.md](docs/api_reference.md) | API docs |

## 🐛 Common Issues

### Incompatible Units
```python
# Error: Can't add length and time
# distance + time  # ❌

# Solution: Only add compatible units
distance1 + distance2  # ✅
```

### Unit Not Found
```python
# Check spelling
Quantity(100, 'meter')  # ✅ not 'metres'

# Or define custom unit
registry.define('myunit', '10 meter')
```

### Import Error
```bash
# Install unifyt
pip install unifyt
```

## 💡 Tips

1. **Always specify units** - Makes code self-documenting
2. **Use arrays for bulk data** - More efficient
3. **Leverage constants** - Don't hardcode values
4. **Check dimensions** - Let Unifyt catch errors
5. **Use utilities** - Built-in functions are optimized

## 🔗 Quick Links

- **Examples**: [examples/](examples/)
- **Tests**: [tests/](tests/)
- **Source**: [unifyt/](unifyt/)
- **Docs**: [docs/](docs/)

---

**Version**: 0.1.0  
**License**: MIT  
**More Info**: See [INDEX.md](INDEX.md)
