# 🚀 Start Here - Unifyt in 60 Seconds

## What is Unifyt?

**Unifyt** makes working with physical units **simple**, **safe**, and **automatic**.

## Install (5 seconds)

```bash
pip install unifyt
```

## Your First Calculation (10 seconds)

```python
from unifyt import Quantity

distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
speed = distance / time

print(speed)  # 10.0 meter / second
```

## Convert Units (5 seconds)

```python
print(speed.to('kilometer/hour'))  # 36.0 kilometer / hour
print(speed.to('mile/hour'))       # 22.37 mile / hour
```

## Use Constants (10 seconds)

```python
from unifyt import constants

mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2  # E = mc²
print(energy)  # 8.987551787e+16 kg⋅m²/s²
```

## Work with Arrays (10 seconds)

```python
import numpy as np

distances = Quantity(np.array([100, 200, 300]), 'meter')
times = Quantity(np.array([10, 20, 30]), 'second')
speeds = distances / times

print(speeds)  # [10. 10. 10.] meter / second
```

## Use Utilities (10 seconds)

```python
from unifyt import utils

temps = utils.linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
mean_temp = utils.mean(temps)
print(mean_temp)  # 50.0 celsius
```

## That's It! 🎉

You now know the basics of Unifyt!

## What's Next?

### Learn More (Choose Your Path)

**Want the full story?**
→ Read [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) - Everything you need to know

**Want to understand the value?**
→ Read [WHY_UNIFYT.md](WHY_UNIFYT.md) - Why Unifyt is useful

**Want a quick tutorial?**
→ Read [QUICKSTART.md](QUICKSTART.md) - 5-minute introduction

**Want comprehensive learning?**
→ Read [GETTING_STARTED.md](GETTING_STARTED.md) - Full tutorial

**Want to see examples?**
→ Browse [examples/](examples/) - Real-world code

**Want API details?**
→ Check [docs/api_reference.md](docs/api_reference.md) - Complete reference

### Try Examples

```bash
# Run all examples
./run_examples.sh

# Or run individually
python examples/basic_usage.py
python examples/scientific_calculations.py
python examples/complete_demo.py
```

### Common Tasks

```python
# Length conversions
distance = Quantity(5, 'kilometer')
print(distance.to('mile'))  # 3.106... mile

# Mass conversions
mass = Quantity(1, 'kilogram')
print(mass.to('pound'))  # 2.204... pound

# Energy conversions
energy = Quantity(1000, 'joule')
print(energy.to('kilowatt_hour'))  # 0.000277... kWh

# Temperature (coming soon: offset conversions)
temp = Quantity(25, 'celsius')
# print(temp.to('fahrenheit'))  # Future feature

# Pressure conversions
pressure = Quantity(1, 'atmosphere')
print(pressure.to('psi'))  # 14.696 psi
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
```

### Arithmetic
```python
q1 + q2  # Addition (compatible units)
q1 - q2  # Subtraction
q1 * q2  # Multiplication
q1 / q2  # Division
q ** n   # Power
```

### Constants
```python
constants.c      # Speed of light
constants.g      # Standard gravity
constants.N_A    # Avogadro number
```

### Utilities
```python
utils.mean(q)    # Mean
utils.std(q)     # Standard deviation
utils.sum(q)     # Sum
utils.min(q)     # Minimum
utils.max(q)     # Maximum
```

## Need Help?

- **Quick lookup**: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **Navigation**: [INDEX.md](INDEX.md)
- **Full guide**: [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)
- **Examples**: [examples/](examples/)

## Why Unifyt?

✅ **Prevents errors** - Automatic unit checking  
✅ **Saves time** - No manual conversions  
✅ **Clear code** - Self-documenting  
✅ **Fast** - Optimized performance  
✅ **Complete** - 100+ units, 30+ constants  

## Get Started Now!

```python
from unifyt import Quantity

# Your code here!
distance = Quantity(100, 'meter')
print(distance.to('kilometer'))
```

**Happy calculating!** 🎉

---

**Next**: Read [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) for the full story!
