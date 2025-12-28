"""Complete demonstration of Unifyt capabilities."""

import numpy as np
from unifyt import Quantity, Unit, UnitRegistry, constants, utils
from unifyt.serialization import save_quantity, load_quantity, quantity_to_json
import tempfile
import os

print("=" * 70)
print("UNIFYT - Complete Feature Demonstration")
print("=" * 70)

# ============================================================================
# 1. BASIC OPERATIONS
# ============================================================================
print("\n1. BASIC OPERATIONS")
print("-" * 70)

distance = Quantity(100, 'meter')
time = Quantity(9.58, 'second')
speed = distance / time

print(f"Distance: {distance}")
print(f"Time: {time}")
print(f"Speed: {speed}")
print(f"Speed in km/h: {speed.to('kilometer/hour'):.2f}")
print(f"Speed in mph: {speed.to('mile/hour'):.2f}")

# ============================================================================
# 2. EXTENSIVE UNIT SUPPORT
# ============================================================================
print("\n2. EXTENSIVE UNIT SUPPORT (100+ units)")
print("-" * 70)

# Energy
energy = Quantity(1000, 'joule')
print(f"Energy: {energy}")
print(f"  In kWh: {energy.to('kilowatt_hour'):.6f}")
print(f"  In calories: {energy.to('calorie'):.2f}")
print(f"  In eV: {energy.to('electronvolt'):.2e}")

# Power
power = Quantity(1, 'horsepower')
print(f"\nPower: {power}")
print(f"  In watts: {power.to('watt'):.2f}")
print(f"  In kilowatts: {power.to('kilowatt'):.4f}")

# Pressure
pressure = Quantity(1, 'atmosphere')
print(f"\nPressure: {pressure}")
print(f"  In pascals: {pressure.to('pascal'):.0f}")
print(f"  In psi: {pressure.to('psi'):.2f}")
print(f"  In bar: {pressure.to('bar'):.4f}")

# Volume
volume = Quantity(1, 'gallon')
print(f"\nVolume: {volume}")
print(f"  In liters: {volume.to('liter'):.4f}")
print(f"  In milliliters: {volume.to('milliliter'):.2f}")

# Frequency
freq = Quantity(2.4, 'gigahertz')
print(f"\nFrequency: {freq}")
print(f"  In hertz: {freq.to('hertz'):.0f}")
print(f"  In megahertz: {freq.to('megahertz'):.0f}")

# ============================================================================
# 3. PHYSICAL CONSTANTS
# ============================================================================
print("\n3. PHYSICAL CONSTANTS (30+ constants)")
print("-" * 70)

print(f"Speed of light: {constants.c}")
print(f"Planck constant: {constants.h}")
print(f"Gravitational constant: {constants.G}")
print(f"Avogadro number: {constants.N_A}")
print(f"Boltzmann constant: {constants.k_B}")
print(f"Standard gravity: {constants.g}")
print(f"Astronomical unit: {constants.AU}")
print(f"Solar mass: {constants.M_sun}")

# Use constants in calculations
print("\nCalculation: E = mc²")
mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2
print(f"Energy from 1 kg: {energy}")
print(f"Energy in kWh: {energy.to('kilowatt_hour'):.2e}")

# ============================================================================
# 4. ARRAY OPERATIONS
# ============================================================================
print("\n4. ARRAY OPERATIONS")
print("-" * 70)

# Create arrays
distances = Quantity(np.array([100, 200, 300, 400, 500]), 'meter')
times = Quantity(np.array([10, 20, 30, 40, 50]), 'second')
speeds = distances / times

print(f"Distances: {distances}")
print(f"Times: {times}")
print(f"Speeds: {speeds}")
print(f"Speeds in km/h: {speeds.to('kilometer/hour')}")

# ============================================================================
# 5. UTILITY FUNCTIONS
# ============================================================================
print("\n5. UTILITY FUNCTIONS")
print("-" * 70)

# Array creation
temps = utils.linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
print(f"Temperature range: {temps}")

# Statistical operations
data = Quantity(np.array([10, 20, 30, 40, 50]), 'meter')
print(f"\nData: {data}")
print(f"Mean: {utils.mean(data)}")
print(f"Std: {utils.std(data):.2f}")
print(f"Min: {utils.min(data)}")
print(f"Max: {utils.max(data)}")
print(f"Sum: {utils.sum(data)}")

# Array creation utilities
zeros = utils.zeros(5, 'kilogram')
ones = utils.ones(5, 'second')
print(f"\nZeros: {zeros}")
print(f"Ones: {ones}")

# Clipping
values = Quantity(np.array([1, 5, 10, 15, 20]), 'meter')
clipped = utils.clip(values, Quantity(5, 'meter'), Quantity(15, 'meter'))
print(f"\nOriginal: {values}")
print(f"Clipped [5, 15]: {clipped}")

# ============================================================================
# 6. CUSTOM UNITS
# ============================================================================
print("\n6. CUSTOM UNITS")
print("-" * 70)

registry = UnitRegistry()
registry.define('furlong', '220 yard')
registry.define('fortnight', '14 day')
registry.define('parsec', '3.086e16 meter')

distance_furlong = Quantity(1, 'furlong')
print(f"1 furlong = {distance_furlong.to('meter'):.2f}")
print(f"1 furlong = {distance_furlong.to('foot'):.2f}")

time_fortnight = Quantity(1, 'fortnight')
print(f"1 fortnight = {time_fortnight.to('hour'):.0f}")

distance_parsec = Quantity(1, 'parsec')
print(f"1 parsec = {distance_parsec.to('kilometer'):.2e}")

# ============================================================================
# 7. SERIALIZATION
# ============================================================================
print("\n7. SERIALIZATION")
print("-" * 70)

# JSON serialization
distance = Quantity(100, 'kilometer')
json_str = quantity_to_json(distance)
print(f"JSON: {json_str}")

# File I/O
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
    filename = f.name

save_quantity(distance, filename, format='json')
loaded = load_quantity(filename, format='json')
print(f"Saved and loaded: {loaded}")
os.unlink(filename)

# ============================================================================
# 8. SCIENTIFIC CALCULATIONS
# ============================================================================
print("\n8. SCIENTIFIC CALCULATIONS")
print("-" * 70)

# Kinetic energy
print("Kinetic Energy: E = 1/2 * m * v²")
mass = Quantity(1000, 'kilogram')
velocity = Quantity(20, 'meter/second')
kinetic_energy = 0.5 * mass * velocity ** 2
print(f"Mass: {mass}")
print(f"Velocity: {velocity}")
print(f"Kinetic Energy: {kinetic_energy}")

# Gravitational force
print("\nGravitational Force: F = G * m1 * m2 / r²")
m1 = Quantity(1000, 'kilogram')
m2 = Quantity(500, 'kilogram')
r = Quantity(10, 'meter')
force = constants.G * m1 * m2 / (r ** 2)
print(f"Force: {force}")
print(f"Force in newtons: {force.to('newton'):.6e}")

# ============================================================================
# 9. PERFORMANCE FEATURES
# ============================================================================
print("\n9. PERFORMANCE FEATURES")
print("-" * 70)

# Large array operations
large_array = Quantity(np.random.rand(10000), 'meter')
print(f"Large array: {len(large_array.magnitude)} elements")
converted = large_array.to('kilometer')
print(f"Converted to km: {len(converted.magnitude)} elements")
print(f"Mean: {utils.mean(converted):.6f}")

# Unit caching (automatic)
print("\nUnit caching is automatic - repeated unit creation is fast")
for i in range(5):
    q = Quantity(i, 'meter/second')  # Uses cached unit

# ============================================================================
# 10. COMPARISON AND VALIDATION
# ============================================================================
print("\n10. COMPARISON AND VALIDATION")
print("-" * 70)

d1 = Quantity(1, 'kilometer')
d2 = Quantity(1000, 'meter')
print(f"{d1} == {d2}: {d1 == d2}")
print(f"{d1} > {Quantity(500, 'meter')}: {d1 > Quantity(500, 'meter')}")

# Close comparison
q1 = Quantity(1.0, 'meter')
q2 = Quantity(1.0000001, 'meter')
print(f"\n{q1} ≈ {q2}: {utils.isclose(q1, q2)}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("✓ 100+ units supported (length, mass, time, energy, power, etc.)")
print("✓ 30+ physical constants with proper units")
print("✓ Array operations with NumPy integration")
print("✓ Utility functions for common operations")
print("✓ Custom unit definitions")
print("✓ JSON and pickle serialization")
print("✓ High performance with caching and vectorization")
print("✓ Type hints and comprehensive documentation")
print("✓ Easy to use, powerful, and extensible")
print("=" * 70)
