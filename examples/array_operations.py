"""Examples of array operations with Unifyt."""

import numpy as np
from unifyt import Quantity

print("=== Creating Array Quantities ===")
# Temperature measurements
temperatures = Quantity(np.array([20, 22, 25, 23, 21]), 'celsius')
print(f"Temperatures: {temperatures}")

# Distance measurements
distances = Quantity(np.array([100, 200, 300, 400, 500]), 'meter')
print(f"Distances: {distances}")

print("\n=== Array Conversions ===")
distances_km = distances.to('kilometer')
print(f"Distances in km: {distances_km}")

distances_miles = distances.to('mile')
print(f"Distances in miles: {distances_miles}")

print("\n=== Array Arithmetic ===")
# Add arrays
d1 = Quantity(np.array([100, 200, 300]), 'meter')
d2 = Quantity(np.array([50, 100, 150]), 'meter')
total = d1 + d2
print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"d1 + d2: {total}")

# Multiply arrays
times = Quantity(np.array([10, 20, 30]), 'second')
speeds = distances[:3] / times
print(f"\nDistances: {distances[:3]}")
print(f"Times: {times}")
print(f"Speeds: {speeds}")

print("\n=== Statistical Operations ===")
# Calculate statistics
data = Quantity(np.array([10, 20, 30, 40, 50]), 'meter')
print(f"Data: {data}")
print(f"Mean: {Quantity(np.mean(data.magnitude), 'meter')}")
print(f"Std Dev: {Quantity(np.std(data.magnitude), 'meter')}")
print(f"Min: {Quantity(np.min(data.magnitude), 'meter')}")
print(f"Max: {Quantity(np.max(data.magnitude), 'meter')}")

print("\n=== Element-wise Operations ===")
# Square each element
lengths = Quantity(np.array([1, 2, 3, 4, 5]), 'meter')
areas = lengths ** 2
print(f"Lengths: {lengths}")
print(f"Areas: {areas}")

print("\n=== Broadcasting ===")
# Multiply array by scalar
velocities = Quantity(np.array([10, 20, 30]), 'meter/second')
scaled = velocities * 2
print(f"Original velocities: {velocities}")
print(f"Scaled velocities: {scaled}")

print("\n=== Filtering and Indexing ===")
# Filter values
all_distances = Quantity(np.array([50, 150, 250, 350, 450]), 'meter')
print(f"All distances: {all_distances}")

# Get distances greater than 200m
mask = all_distances.magnitude > 200
filtered = Quantity(all_distances.magnitude[mask], 'meter')
print(f"Distances > 200m: {filtered}")

print("\n=== Matrix Operations ===")
# 2D array
matrix = Quantity(np.array([[1, 2, 3], [4, 5, 6]]), 'meter')
print(f"Matrix:\n{matrix}")
print(f"Shape: {matrix.magnitude.shape}")
print(f"Transposed:\n{Quantity(matrix.magnitude.T, 'meter')}")
