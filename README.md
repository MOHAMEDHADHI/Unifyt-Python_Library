# Unifyt v0.2.0

A powerful and easy-to-use Python library for unit conversion and calculations, combining the best features of Pint and Unyt.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.2.0-green.svg)](https://github.com/MEERAN2314/unifyt)

## 🌟 Why Unifyt?

Unifyt solves the universal problem of working with physical units in scientific computing, engineering, and data analysis. It prevents errors, saves time, and makes your code clear and maintainable.

**Before Unifyt:**
```python
distance = 100  # meters? kilometers? 🤔
speed = distance / 10  # What unit is this? 😕
```

**With Unifyt:**
```python
from unifyt import Quantity
distance = Quantity(100, 'meter')
speed = distance / Quantity(10, 'second')  # Automatically: 10 m/s ✨
print(speed.to('kilometer/hour'))  # 36.0 km/h 🎯
```

## Features

- **Intuitive API**: Simple and Pythonic interface for working with physical quantities
- **Extensive Unit Support**: **300+ units** including SI, imperial, astronomical, atomic, electromagnetic, and more
- **High Performance**: Optimized for speed with caching and NumPy integration
- **Type Safety**: Full type hints for better IDE support
- **Flexible Conversions**: Easy unit conversions with automatic dimensionality checking
- **Array Support**: Seamless integration with NumPy arrays
- **Custom Units**: Define your own units and unit systems
- **Context Management**: Switch between unit systems easily
- **Physical Constants**: Built-in library of **80+ physical and astronomical constants**
- **Utility Functions**: Array creation, statistical operations, and more
- **Serialization**: Save and load quantities in JSON or pickle format

## 🎉 What's New in v0.2.0

- **300+ units** (3x increase from v0.1.0!)
- **80+ constants** (2.7x increase!)
- **25+ exception types** for precise error handling
- **15+ new categories**: Electromagnetic, radioactivity, data storage, viscosity, and more
- **Comprehensive documentation**: 10+ new guides including WHY_UNIFYT.md, EXCEPTIONS_GUIDE.md
- **Fully backward compatible** - All existing code works
- See [CHANGELOG.md](CHANGELOG.md) for complete details
- **Custom Units**: Define your own units and unit systems
- **Context Management**: Switch between unit systems easily
- **Physical Constants**: Built-in library of physical and astronomical constants
- **Utility Functions**: Array creation, statistical operations, and more
- **Serialization**: Save and load quantities in JSON or pickle format

## Installation

```bash
pip install unifyt
```

## 🚀 Quick Start

**New to Unifyt?** Choose your path:

- **60 seconds**: [START_HERE.md](starter documents/START_HERE.md) - Lightning fast intro
- **5 minutes**: [QUICKSTART.md](QUICKSTART.md) - Quick tutorial  
- **Complete**: [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) - Everything you need
- **Why use it**: [WHY_UNIFYT.md](WHY_UNIFYT.md) - Value proposition

```bash
pip install unifyt
```

```python
from unifyt import Quantity, constants, utils
import numpy as np

# Create quantities with units
distance = Quantity(100, 'meters')
time = Quantity(9.58, 'seconds')

# Perform calculations
speed = distance / time
print(speed)  # 10.438413361169102 meter / second

# Convert units
speed_mph = speed.to('miles/hour')
print(speed_mph)  # 23.350065963060686 mile / hour

# Work with arrays
distances = Quantity(np.array([100, 200, 300]), 'meters')
print(distances.to('kilometers'))  # [0.1 0.2 0.3] kilometer

# Use physical constants
mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2  # E = mc²
print(energy.to('kilowatt_hour'))

# Utility functions
temps = utils.linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
mean_temp = utils.mean(temps)
```

**Want more?** → [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) - **The ultimate guide!**  
**Need help?** → [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - **Quick lookup!**

## 📚 Documentation

### 🌟 Essential Guides (Start Here!)
- **[WHY_UNIFYT.md](WHY_UNIFYT.md)** ⭐ - **Why you need this library**
- **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** ⭐ - **The ultimate guide**
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** ⭐ - **Quick lookup**
- **[EXCEPTIONS_GUIDE.md](EXCEPTIONS_GUIDE.md)** ⭐ - **Error handling**

### 📚 Getting Started
- **[START_HERE.md](starter documents/START_HERE.md)** - 60-second intro
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute tutorial
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Comprehensive tutorial
- **[INDEX.md](INDEX.md)** - Complete navigation hub

### 📖 Reference Documentation
- **[UNITS_CATALOG.md](starter documents/UNITS_CATALOG.md)** - All 300+ units
- **[docs/api_reference.md](docs/api_reference.md)** - Full API reference
- **[docs/user_guide.md](docs/user_guide.md)** - Complete usage guide
- **[docs/FEATURES.md](docs/FEATURES.md)** - Detailed feature list
- **[examples/](examples/)** - Practical examples

### 🔧 Advanced Topics
- **[docs/PERFORMANCE.md](docs/PERFORMANCE.md)** - Optimization guide
- **[docs/MIGRATION.md](docs/MIGRATION.md)** - Migrating from Pint/Unyt

### 📋 Project Information
- **[FINAL_SUMMARY.md](starter documents/FINAL_SUMMARY.md)** - Project summary
- **[STRUCTURE.md](STRUCTURE.md)** - Project structure
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute

## Examples

Check out the `examples/` directory for more usage examples:

- **basic_usage.py** - Basic unit conversions and operations
- **scientific_calculations.py** - Physics, chemistry, and engineering examples
- **custom_units.py** - Define your own units
- **array_operations.py** - NumPy array integration
- **advanced_features.py** - Constants, utilities, and serialization

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/MOHAMEDHADHI/unifyt.git
cd unifyt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Run linting
flake8 unifyt/

# Run type checking
mypy unifyt/

# Format code
black unifyt/ tests/
```

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Supported Units (300+)

### Core Units
- **Length**: meter, kilometer, mile, foot, inch, nanometer, angstrom, parsec, light_year, etc.
- **Mass**: kilogram, gram, pound, ounce, ton, atomic_mass_unit, solar_mass, earth_mass, etc.
- **Time**: second, minute, hour, day, week, year, femtosecond, attosecond, millennium, etc.
- **Temperature**: kelvin, celsius, fahrenheit

### Derived Units
- **Energy**: joule, calorie, kilowatt_hour, electronvolt, BTU, erg, rydberg, hartree, etc.
- **Power**: watt, kilowatt, horsepower, gigawatt, terawatt, etc.
- **Pressure**: pascal, bar, atmosphere, psi, torr, gigapascal, etc.
- **Force**: newton, dyne, kilogram_force, pound_force, kip, etc.
- **Frequency**: hertz, kilohertz, megahertz, gigahertz, terahertz, rpm, etc.
- **Voltage**: volt, millivolt, kilovolt, megavolt, etc.
- **Current**: ampere, milliampere, microampere, kiloampere, etc.
- **Capacitance**: farad, microfarad, nanofarad, picofarad, etc.
- **Inductance**: henry, millihenry, microhenry, etc.
- **Magnetic Field**: tesla, gauss, millitesla, etc.
- **Radioactivity**: becquerel, curie, rutherford, etc.
- **Radiation Dose**: gray, sievert, rad, rem, etc.
- **Data**: bit, byte, kilobyte, megabyte, gigabyte, terabyte, etc.
- **Volume**: liter, gallon, milliliter, cup, etc.
- **Angle**: radian, degree, arcminute, arcsecond, etc.
- **Viscosity**: poise, stokes, pascal_second, etc.
- **Concentration**: molar, millimolar, micromolar, etc.
- And many more!

## Physical Constants (80+)

Access fundamental constants with proper units:

```python
from unifyt import constants

# Fundamental
print(constants.c)          # Speed of light
print(constants.h)          # Planck constant
print(constants.G)          # Gravitational constant
print(constants.N_A)        # Avogadro number
print(constants.g)          # Standard gravity

# Astronomical
print(constants.AU)         # Astronomical unit
print(constants.M_sun)      # Solar mass
print(constants.L_sun)      # Solar luminosity
print(constants.H_0)        # Hubble constant

# Atomic & Particle
print(constants.m_e)        # Electron mass
print(constants.m_p)        # Proton mass
print(constants.mu_B)       # Bohr magneton
print(constants.lambda_C)   # Compton wavelength

# Planck Units
print(constants.l_P)        # Planck length
print(constants.t_P)        # Planck time
print(constants.E_P)        # Planck energy

# Electromagnetic
print(constants.Z_0)        # Vacuum impedance
print(constants.Phi_0)      # Magnetic flux quantum

# Cosmological
print(constants.T_CMB)      # CMB temperature
print(constants.universe_age)  # Age of universe
```

## 🎯 Real-World Applications

- **Physics**: Kinetic energy, gravitational force, E=mc²
- **Engineering**: Flow rates, power calculations, pressure conversions
- **Chemistry**: Concentration calculations, ideal gas law
- **Data Analysis**: Sensor data, environmental monitoring
- **Astronomy**: Light-year distances, escape velocity
- **Education**: Teaching physics, chemistry labs

See [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) for detailed examples!

## Acknowledgments

This library is inspired by and builds upon the excellent work of:
- [Pint](https://github.com/hgrecco/pint) - Python units library
- [Unyt](https://github.com/yt-project/unyt) - Handle, manipulate, and convert data with units

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

