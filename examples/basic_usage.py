"""Basic usage examples for Unifyt library."""

from unifyt import Quantity

# Create quantities with units
print("=== Creating Quantities ===")
distance = Quantity(100, 'meter')
print(f"Distance: {distance}")

time = Quantity(9.58, 'second')
print(f"Time: {time}")

# Perform calculations
print("\n=== Calculations ===")
speed = distance / time
print(f"Speed: {speed}")
print(f"Speed (formatted): {speed:.2f}")

# Convert units
print("\n=== Unit Conversions ===")
speed_kmh = speed.to('kilometer/hour')
print(f"Speed in km/h: {speed_kmh}")

speed_mph = speed.to('mile/hour')
print(f"Speed in mph: {speed_mph}")

# Addition with automatic conversion
print("\n=== Addition with Conversion ===")
d1 = Quantity(1, 'kilometer')
d2 = Quantity(500, 'meter')
total = d1 + d2
print(f"{d1} + {d2} = {total}")

# Multiplication
print("\n=== Area Calculation ===")
length = Quantity(10, 'meter')
width = Quantity(5, 'meter')
area = length * width
print(f"Area: {area}")

# Powers
print("\n=== Powers ===")
side = Quantity(3, 'meter')
volume = side ** 3
print(f"Volume of cube: {volume}")

# Comparisons
print("\n=== Comparisons ===")
d1 = Quantity(1, 'kilometer')
d2 = Quantity(1000, 'meter')
print(f"{d1} == {d2}: {d1 == d2}")
print(f"{d1} > {Quantity(500, 'meter')}: {d1 > Quantity(500, 'meter')}")
