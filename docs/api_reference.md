# Unifyt API Reference

## Core Classes

### Quantity

Represents a physical quantity with a value and unit.

#### Constructor

```python
Quantity(value, unit)
```

**Parameters:**
- `value` (float, int, or np.ndarray): Numerical value
- `unit` (str or Unit): Unit specification

**Example:**
```python
q = Quantity(100, 'meter')
```

#### Properties

- `value`: Get the numerical value as numpy array
- `magnitude`: Get the magnitude (scalar or array)
- `unit`: Get the Unit object
- `dimensionality`: Get the Dimension object

#### Methods

##### to(target_unit)

Convert to a different unit.

**Parameters:**
- `target_unit` (str or Unit): Target unit

**Returns:** New Quantity with converted value

**Raises:** ValueError if units are incompatible

##### to_base_units()

Convert to base SI units.

**Returns:** New Quantity in base units

#### Arithmetic Operations

- `+`, `-`: Addition and subtraction (requires compatible units)
- `*`, `/`: Multiplication and division
- `**`: Power operation
- `-`: Negation
- `abs()`: Absolute value

#### Comparison Operations

- `==`, `!=`: Equality comparison
- `<`, `<=`, `>`, `>=`: Magnitude comparison (requires compatible units)

---

### Unit

Represents a physical unit.

#### Constructor

```python
Unit(unit_str, scale=1.0)
```

**Parameters:**
- `unit_str` (str): String representation of unit
- `scale` (float): Scale factor (default: 1.0)

**Example:**
```python
u = Unit('meter/second')
```

#### Properties

- `dimensionality`: Get the Dimension object

#### Methods

##### is_compatible_with(other)

Check if this unit is compatible with another.

**Parameters:**
- `other` (Unit): Unit to compare with

**Returns:** bool

##### conversion_factor_to(other)

Get conversion factor to another unit.

**Parameters:**
- `other` (Unit): Target unit

**Returns:** float

**Raises:** ValueError if units are incompatible

##### to_base_units()

Convert to base SI units.

**Returns:** Unit in base units

##### is_dimensionless()

Check if unit is dimensionless.

**Returns:** bool

#### Arithmetic Operations

- `*`: Multiply units
- `/`: Divide units
- `**`: Raise to power

---

### Dimension

Represents physical dimensions.

#### Constructor

```python
Dimension(length=0, mass=0, time=0, current=0, 
          temperature=0, amount=0, luminosity=0)
```

**Parameters:** Exponents for each base dimension (default: 0)

**Example:**
```python
velocity_dim = Dimension(length=1, time=-1)
```

#### Properties

- `length`: Length dimension exponent
- `mass`: Mass dimension exponent
- `time`: Time dimension exponent
- `current`: Electric current dimension exponent
- `temperature`: Temperature dimension exponent
- `amount`: Amount of substance dimension exponent
- `luminosity`: Luminous intensity dimension exponent

#### Arithmetic Operations

- `+`: Add dimensions (for multiplication)
- `-`: Subtract dimensions (for division)
- `*`: Multiply by scalar (for powers)

---

### UnitRegistry

Registry for managing custom units.

#### Constructor

```python
UnitRegistry()
```

#### Methods

##### define(name, definition)

Define a custom unit.

**Parameters:**
- `name` (str): Name of the new unit
- `definition` (str): Definition in terms of existing units

**Example:**
```python
registry = UnitRegistry()
registry.define('furlong', '220 yard')
```

##### alias(alias, unit_name)

Create an alias for an existing unit.

**Parameters:**
- `alias` (str): New alias name
- `unit_name` (str): Existing unit name

##### get_unit(name)

Get a unit by name.

**Parameters:**
- `name` (str): Unit name or alias

**Returns:** Unit object or None

##### list_units()

List all custom units.

**Returns:** Dict[str, Unit]

##### list_aliases()

List all aliases.

**Returns:** Dict[str, str]

---

### UnitContext

Context manager for unit systems.

#### Constructor

```python
UnitContext(system)
```

**Parameters:**
- `system` (str): Unit system name ('SI', 'imperial', 'CGS', etc.)

**Example:**
```python
with UnitContext('imperial'):
    distance = Quantity(100, 'foot')
```

#### Class Methods

##### get_current_system()

Get the current unit system.

**Returns:** str or None

---

## Supported Units

### Length
- meter (m), kilometer (km), centimeter (cm), millimeter (mm)
- mile (mi), yard (yd), foot (ft), inch (in)

### Mass
- kilogram (kg), gram (g), milligram (mg)
- pound (lb), ounce (oz), ton

### Time
- second (s), minute (min), hour (h/hr), day (d), week, year (yr)

### Temperature
- kelvin (K), celsius (C), fahrenheit (F)

### Electric Current
- ampere (A)

### Amount of Substance
- mole (mol)

### Luminous Intensity
- candela (cd)

## Constants

### default_registry

Default UnitRegistry instance available at module level.

```python
from unifyt import default_registry
```

## Exceptions

### ValueError

Raised when:
- Attempting operations on incompatible units
- Converting between incompatible units
- Invalid unit specifications

## Type Hints

Unifyt includes full type hints for better IDE support. Import types:

```python
from unifyt import Quantity, Unit, Dimension, UnitRegistry, UnitContext
```
