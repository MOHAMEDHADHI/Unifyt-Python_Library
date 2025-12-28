"""Advanced features demonstration for Unifyt."""

import numpy as np
from unifyt import Quantity, constants, utils
from unifyt.serialization import save_quantity, load_quantity, quantity_to_json

print("=== Physical Constants ===")
print(f"Speed of light: {constants.c}")
print(f"Planck constant: {constants.h}")
print(f"Gravitational constant: {constants.G}")
print(f"Avogadro number: {constants.N_A}")
print(f"Standard gravity: {constants.g}")

print("\n=== Using Constants in Calculations ===")
# Calculate energy from mass (E = mc²)
mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2
print(f"Energy from 1 kg: {energy}")
print(f"Energy in kWh: {energy.to('kilowatt_hour')}")

# Calculate gravitational force
m1 = Quantity(1000, 'kilogram')
m2 = Quantity(500, 'kilogram')
r = Quantity(10, 'meter')
force = constants.G * m1 * m2 / (r ** 2)
print(f"\nGravitational force: {force}")

print("\n=== Utility Functions ===")
# Create evenly spaced quantities
temps = utils.linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
print(f"Temperature range: {temps}")

# Create range with step
distances = utils.arange(Quantity(0, 'meter'), Quantity(100, 'meter'), 
                         Quantity(10, 'meter'))
print(f"Distance range: {distances}")

# Statistical functions
data = Quantity(np.array([10, 20, 30, 40, 50]), 'meter')
print(f"\nData: {data}")
print(f"Mean: {utils.mean(data)}")
print(f"Std: {utils.std(data)}")
print(f"Min: {utils.min(data)}")
print(f"Max: {utils.max(data)}")
print(f"Sum: {utils.sum(data)}")

print("\n=== Array Creation ===")
zeros = utils.zeros(5, 'kilogram')
print(f"Zeros: {zeros}")

ones = utils.ones((2, 3), 'second')
print(f"Ones:\n{ones}")

filled = utils.full(4, Quantity(9.81, 'meter/second^2'))
print(f"Filled: {filled}")

print("\n=== Array Operations ===")
q1 = Quantity(np.array([1, 2, 3]), 'meter')
q2 = Quantity(np.array([4, 5, 6]), 'meter')
concatenated = utils.concatenate([q1, q2])
print(f"Concatenated: {concatenated}")

stacked = utils.stack([q1, q2])
print(f"Stacked:\n{stacked}")

print("\n=== Clipping ===")
values = Quantity(np.array([1, 5, 10, 15, 20]), 'meter')
clipped = utils.clip(values, Quantity(5, 'meter'), Quantity(15, 'meter'))
print(f"Original: {values}")
print(f"Clipped: {clipped}")

print("\n=== Comparison with Tolerance ===")
q1 = Quantity(1.0, 'meter')
q2 = Quantity(1.0000001, 'meter')
print(f"q1: {q1}")
print(f"q2: {q2}")
print(f"Are close: {utils.isclose(q1, q2)}")

print("\n=== Serialization ===")
# Convert to JSON
distance = Quantity(100, 'kilometer')
json_str = quantity_to_json(distance)
print(f"JSON: {json_str}")

# Save and load
save_quantity(distance, '/tmp/distance.json', format='json')
loaded = load_quantity('/tmp/distance.json', format='json')
print(f"Loaded: {loaded}")

print("\n=== More Units ===")
# Energy units
energy = Quantity(1000, 'joule')
print(f"Energy: {energy}")
print(f"In kWh: {energy.to('kilowatt_hour')}")
print(f"In calories: {energy.to('calorie')}")

# Power units
power = Quantity(1, 'horsepower')
print(f"\nPower: {power}")
print(f"In watts: {power.to('watt')}")
print(f"In kilowatts: {power.to('kilowatt')}")

# Pressure units
pressure = Quantity(1, 'atmosphere')
print(f"\nPressure: {pressure}")
print(f"In pascals: {pressure.to('pascal')}")
print(f"In psi: {pressure.to('psi')}")
print(f"In bar: {pressure.to('bar')}")

# Volume units
volume = Quantity(1, 'gallon')
print(f"\nVolume: {volume}")
print(f"In liters: {volume.to('liter')}")
print(f"In milliliters: {volume.to('milliliter')}")

print("\n=== Frequency ===")
freq = Quantity(2.4, 'gigahertz')
print(f"Frequency: {freq}")
print(f"In hertz: {freq.to('hertz')}")
print(f"In megahertz: {freq.to('megahertz')}")

print("\n=== Angle Conversions ===")
angle_deg = Quantity(180, 'degree')
angle_rad = angle_deg.to('radian')
print(f"Angle: {angle_deg}")
print(f"In radians: {angle_rad}")
print(f"Pi radians: {constants.pi}")
