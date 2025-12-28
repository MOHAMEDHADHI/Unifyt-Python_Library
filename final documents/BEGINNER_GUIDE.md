# Unifyt Beginner's Guide

## 👋 Welcome!

This guide is designed for absolute beginners. No prior knowledge of unit conversion libraries required!

## 📚 Table of Contents

1. [What is Unifyt?](#what-is-unifyt)
2. [Why Do I Need It?](#why-do-i-need-it)
3. [Installation](#installation)
4. [Your First Steps](#your-first-steps)
5. [Core Concepts](#core-concepts)
6. [Common Tasks](#common-tasks)
7. [Practical Examples](#practical-examples)
8. [Common Mistakes](#common-mistakes)
9. [Next Steps](#next-steps)

---

## What is Unifyt?

**Unifyt** is a Python library that helps you work with measurements and units.

### Think of it like this:

Instead of writing:
```python
distance = 100  # Is this meters? kilometers? miles? 🤔
```

You write:
```python
from unifyt import Quantity
distance = Quantity(100, 'meter')  # Crystal clear! ✨
```

### What can it do?

✅ **Track units automatically** - Never forget what unit you're using  
✅ **Convert between units** - meters to miles in one line  
✅ **Prevent errors** - Can't accidentally add meters to seconds  
✅ **Make code clear** - Anyone can understand your measurements  

---

## Why Do I Need It?

### Problem 1: Unit Confusion

**Without Unifyt:**
```python
# What units are these?
speed = 60  # mph? km/h? m/s? 😕
time = 2    # hours? minutes? seconds? 🤷
```

**With Unifyt:**
```python
from unifyt import Quantity

speed = Quantity(60, 'mile/hour')  # Clear! 😊
time = Quantity(2, 'hour')          # Obvious! 👍
```

### Problem 2: Manual Conversions

**Without Unifyt:**
```python
# Tedious and error-prone
miles = 100
kilometers = miles * 1.60934  # Did I get this right? 😰
```

**With Unifyt:**
```python
miles = Quantity(100, 'mile')
kilometers = miles.to('kilometer')  # Always correct! ✅
```

### Problem 3: Calculation Errors

**Without Unifyt:**
```python
# Easy to make mistakes
distance = 100  # meters
time = 10       # seconds
speed = distance + time  # WRONG! But no error 😱
```

**With Unifyt:**
```python
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
# speed = distance + time  # ERROR! Can't add length and time ✅
speed = distance / time     # Correct! 10 m/s 🎯
```

---

## Installation

### Step 1: Make sure you have Python

Open your terminal/command prompt and type:
```bash
python --version
```

You should see something like `Python 3.8.0` or higher.

### Step 2: Install Unifyt

```bash
pip install unifyt
```

That's it! You're ready to go! 🎉

---

## Your First Steps

### Step 1: Import Unifyt

```python
from unifyt import Quantity
```

This gives you access to the main tool you'll use.

### Step 2: Create Your First Quantity

```python
distance = Quantity(100, 'meter')
print(distance)  # Output: 100 meter
```

**What just happened?**
- You created a "quantity" with a value (100) and a unit (meter)
- Unifyt now tracks both the number AND the unit

### Step 3: Convert Units

```python
distance_km = distance.to('kilometer')
print(distance_km)  # Output: 0.1 kilometer
```

**What just happened?**
- You converted 100 meters to kilometers
- Unifyt did the math for you (100 meters = 0.1 kilometers)

### Step 4: Do Math

```python
time = Quantity(10, 'second')
speed = distance / time
print(speed)  # Output: 10.0 meter / second
```

**What just happened?**
- You divided distance by time
- Unifyt automatically figured out the result unit (meter/second)

---

## Core Concepts

### Concept 1: Quantities

A **Quantity** is a number with a unit.

```python
# These are all quantities:
length = Quantity(5, 'meter')
mass = Quantity(10, 'kilogram')
time = Quantity(30, 'second')
temperature = Quantity(25, 'celsius')
```

**Think of it as:** A labeled number. The label is the unit.

### Concept 2: Units

A **unit** is the measurement type.

```python
# Common units:
'meter'      # length
'kilogram'   # mass
'second'     # time
'celsius'    # temperature
```

**Think of it as:** The "type" of measurement.

### Concept 3: Conversion

**Conversion** means changing from one unit to another.

```python
distance = Quantity(1000, 'meter')
distance_km = distance.to('kilometer')  # 1 kilometer
distance_mi = distance.to('mile')       # 0.621 mile
```

**Think of it as:** Translating between languages, but for measurements.

### Concept 4: Compatible Units

Some units can be converted, some can't.

```python
# ✅ These CAN be converted (both are length):
meters = Quantity(100, 'meter')
miles = meters.to('mile')

# ❌ These CANNOT be converted (different types):
distance = Quantity(100, 'meter')
# time = distance.to('second')  # ERROR!
```

**Think of it as:** You can translate English to Spanish, but not English to Music.

---

## Common Tasks

### Task 1: Create a Measurement

```python
from unifyt import Quantity

# Pattern: Quantity(number, 'unit')
height = Quantity(180, 'centimeter')
weight = Quantity(70, 'kilogram')
age = Quantity(25, 'year')
```

### Task 2: Convert Units

```python
# Pattern: quantity.to('new_unit')
height_m = height.to('meter')      # 1.8 meter
height_ft = height.to('foot')      # 5.9 foot
weight_lb = weight.to('pound')     # 154.3 pound
```

### Task 3: Do Calculations

```python
# Addition (same type of unit)
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
```

### Task 4: Compare Measurements

```python
d1 = Quantity(1, 'kilometer')
d2 = Quantity(1000, 'meter')

print(d1 == d2)  # True (they're equal!)
print(d1 > Quantity(500, 'meter'))  # True
```

---

## Practical Examples

### Example 1: Cooking

```python
from unifyt import Quantity

# Recipe calls for 500 grams of flour
flour = Quantity(500, 'gram')

# But your scale shows pounds
flour_lb = flour.to('pound')
print(f"You need {flour_lb.magnitude:.2f} pounds of flour")
# Output: You need 1.10 pounds of flour
```

### Example 2: Travel

```python
# Your car shows speed in mph
speed = Quantity(60, 'mile/hour')

# But the speed limit is in km/h
speed_kmh = speed.to('kilometer/hour')
print(f"You're going {speed_kmh.magnitude:.0f} km/h")
# Output: You're going 97 km/h
```

### Example 3: Fitness

```python
# You ran 5 kilometers
distance = Quantity(5, 'kilometer')

# How many miles is that?
distance_mi = distance.to('mile')
print(f"You ran {distance_mi.magnitude:.2f} miles")
# Output: You ran 3.11 miles

# You ran it in 30 minutes
time = Quantity(30, 'minute')

# What was your pace?
pace = distance / time
print(f"Your pace: {pace}")
# Output: Your pace: 0.166... kilometer/minute

# Convert to km/h
pace_kmh = pace.to('kilometer/hour')
print(f"Your pace: {pace_kmh.magnitude:.1f} km/h")
# Output: Your pace: 10.0 km/h
```

### Example 4: Science Class

```python
# Calculate kinetic energy: E = ½mv²
mass = Quantity(2, 'kilogram')
velocity = Quantity(10, 'meter/second')

energy = 0.5 * mass * velocity ** 2
print(f"Kinetic energy: {energy}")
# Output: Kinetic energy: 100.0 kilogram * meter^2 / second^2

# That's Joules!
print(f"Energy: {energy.magnitude} Joules")
```

### Example 5: Home Project

```python
# You need to paint a room
length = Quantity(5, 'meter')
width = Quantity(4, 'meter')
height = Quantity(2.5, 'meter')

# Calculate wall area (4 walls)
wall_area = 2 * (length * height) + 2 * (width * height)
print(f"Wall area: {wall_area}")

# Paint covers 10 square meters per liter
coverage = Quantity(10, 'meter^2')
paint_needed = wall_area / coverage
print(f"Paint needed: {paint_needed.magnitude:.1f} liters")
```

---

## Common Mistakes

### Mistake 1: Forgetting Units

❌ **Wrong:**
```python
distance = 100  # What unit?
```

✅ **Right:**
```python
distance = Quantity(100, 'meter')  # Clear!
```

### Mistake 2: Adding Incompatible Units

❌ **Wrong:**
```python
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
result = distance + time  # ERROR!
```

✅ **Right:**
```python
distance = Quantity(100, 'meter')
time = Quantity(10, 'second')
speed = distance / time  # Correct!
```

### Mistake 3: Typos in Unit Names

❌ **Wrong:**
```python
distance = Quantity(100, 'metrs')  # Typo!
```

✅ **Right:**
```python
distance = Quantity(100, 'meter')  # Correct spelling
# or
distance = Quantity(100, 'meters')  # Also works!
```

### Mistake 4: Converting to Wrong Unit

❌ **Wrong:**
```python
distance = Quantity(100, 'meter')
time = distance.to('second')  # Can't convert length to time!
```

✅ **Right:**
```python
distance = Quantity(100, 'meter')
distance_km = distance.to('kilometer')  # Both are length!
```

### Mistake 5: Not Using .magnitude

❌ **Wrong:**
```python
distance = Quantity(100, 'meter')
print(distance + 50)  # Might not work as expected
```

✅ **Right:**
```python
distance = Quantity(100, 'meter')
# If you need just the number:
number = distance.magnitude  # 100
# Or create a new quantity:
new_distance = distance + Quantity(50, 'meter')
```

---

## Next Steps

### Level 1: Basics (You are here! ✅)
- ✅ Create quantities
- ✅ Convert units
- ✅ Do simple math
- ✅ Understand errors

### Level 2: Intermediate
**Next, learn about:**
- Arrays and bulk data ([examples/array_operations.py](examples/array_operations.py))
- Physical constants ([COMPLETE_GUIDE.md](COMPLETE_GUIDE.md#physical-constants))
- More unit types ([UNITS_CATALOG.md](starter documents/UNITS_CATALOG.md))

**Read:**
- [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) - Everything in detail
- [examples/scientific_calculations.py](examples/scientific_calculations.py) - Real-world examples

### Level 3: Advanced
**Eventually, explore:**
- Custom units ([examples/custom_units.py](examples/custom_units.py))
- Performance optimization ([docs/PERFORMANCE.md](docs/PERFORMANCE.md))
- Error handling ([EXCEPTIONS_GUIDE.md](EXCEPTIONS_GUIDE.md))

---

## Quick Reference Card

### Create
```python
q = Quantity(value, 'unit')
```

### Convert
```python
q_new = q.to('new_unit')
```

### Math
```python
q1 + q2  # Add (same unit type)
q1 - q2  # Subtract
q1 * q2  # Multiply
q1 / q2  # Divide
q ** 2   # Square
```

### Compare
```python
q1 == q2  # Equal
q1 < q2   # Less than
q1 > q2   # Greater than
```

### Get Number
```python
number = q.magnitude
```

---

## Practice Exercises

### Exercise 1: Temperature Conversion
Convert 25 degrees Celsius to Fahrenheit.

<details>
<summary>Click to see solution</summary>

```python
from unifyt import Quantity

temp_c = Quantity(25, 'celsius')
# Note: Temperature offset conversions coming in v0.3.0
# For now, use for temperature differences only
```
</details>

### Exercise 2: Speed Calculation
Calculate speed if you travel 150 kilometers in 2 hours.

<details>
<summary>Click to see solution</summary>

```python
from unifyt import Quantity

distance = Quantity(150, 'kilometer')
time = Quantity(2, 'hour')
speed = distance / time
print(speed)  # 75.0 kilometer / hour
```
</details>

### Exercise 3: Area Calculation
Calculate the area of a rectangle that is 5 meters by 3 meters.

<details>
<summary>Click to see solution</summary>

```python
from unifyt import Quantity

length = Quantity(5, 'meter')
width = Quantity(3, 'meter')
area = length * width
print(area)  # 15 meter^2
```
</details>

### Exercise 4: Unit Conversion Chain
Convert 1 mile to meters, then to centimeters.

<details>
<summary>Click to see solution</summary>

```python
from unifyt import Quantity

distance = Quantity(1, 'mile')
distance_m = distance.to('meter')
distance_cm = distance_m.to('centimeter')
print(distance_cm)  # 160934.4 centimeter

# Or in one step:
distance_cm = distance.to('centimeter')
print(distance_cm)  # 160934.4 centimeter
```
</details>

---

## Getting Help

### If You're Stuck

1. **Check the error message** - It usually tells you what's wrong
2. **Look at examples** - [examples/](examples/) folder has working code
3. **Read the guide** - [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) has everything
4. **Use quick reference** - [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for syntax

### Common Questions

**Q: What units are available?**  
A: See [UNITS_CATALOG.md](starter documents/UNITS_CATALOG.md) for all 300+ units

**Q: How do I handle errors?**  
A: See [EXCEPTIONS_GUIDE.md](EXCEPTIONS_GUIDE.md)

**Q: Can I use arrays?**  
A: Yes! See [examples/array_operations.py](examples/array_operations.py)

**Q: How do I make custom units?**  
A: See [examples/custom_units.py](examples/custom_units.py)

---

## Summary

### What You Learned

✅ What Unifyt is and why it's useful  
✅ How to install Unifyt  
✅ How to create quantities  
✅ How to convert between units  
✅ How to do calculations  
✅ Common mistakes to avoid  

### Key Takeaways

1. **Always use Quantity** - Don't use bare numbers for measurements
2. **Units must be compatible** - Can't add meters to seconds
3. **Conversions are easy** - Just use `.to('unit')`
4. **Math works naturally** - Unifyt handles the units automatically

### You're Ready!

You now know enough to start using Unifyt in your projects! 🎉

**Next steps:**
- Try it in your own code
- Explore [examples/](examples/)
- Read [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) when you're ready for more

---

**Welcome to the Unifyt community!** 🚀

**Questions?** Check [INDEX.md](INDEX.md) for all documentation.  
**Need more?** Read [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md).  
**Quick lookup?** Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md).

**Happy calculating!** ✨
