"""Scientific calculation examples using Unifyt."""

from unifyt import Quantity
import numpy as np

print("=== Physics: Kinetic Energy ===")
# E = 1/2 * m * v^2
mass = Quantity(1000, 'kilogram')
velocity = Quantity(20, 'meter/second')
kinetic_energy = 0.5 * mass * velocity ** 2
print(f"Mass: {mass}")
print(f"Velocity: {velocity}")
print(f"Kinetic Energy: {kinetic_energy}")

print("\n=== Physics: Gravitational Potential Energy ===")
# E = m * g * h
mass = Quantity(50, 'kilogram')
g = Quantity(9.81, 'meter/second/second')
height = Quantity(10, 'meter')
potential_energy = mass * g * height
print(f"Mass: {mass}")
print(f"Height: {height}")
print(f"Potential Energy: {potential_energy}")

print("\n=== Chemistry: Ideal Gas Law ===")
# PV = nRT (simplified example)
pressure = Quantity(101.325, 'kilopascal')  # 1 atm
volume = Quantity(22.4, 'liter')
print(f"Pressure: {pressure}")
print(f"Volume: {volume}")
print(f"PV: {pressure * volume}")

print("\n=== Engineering: Flow Rate ===")
volume = Quantity(1000, 'liter')
time = Quantity(5, 'minute')
flow_rate = volume / time
print(f"Volume: {volume}")
print(f"Time: {time}")
print(f"Flow Rate: {flow_rate}")
print(f"Flow Rate (L/s): {flow_rate.to('liter/second')}")

print("\n=== Astronomy: Distance Calculation ===")
# Distance = velocity * time
velocity = Quantity(299792458, 'meter/second')  # Speed of light
time = Quantity(1, 'year')
distance = velocity * time
print(f"Speed of light: {velocity}")
print(f"Time: {time}")
print(f"Distance (light-year): {distance}")
print(f"Distance (km): {distance.to('kilometer')}")

print("\n=== Array Operations ===")
# Multiple measurements
distances = Quantity(np.array([100, 200, 300, 400, 500]), 'meter')
times = Quantity(np.array([10, 20, 30, 40, 50]), 'second')
speeds = distances / times
print(f"Distances: {distances}")
print(f"Times: {times}")
print(f"Speeds: {speeds}")
print(f"Average speed: {Quantity(np.mean(speeds.magnitude), 'meter/second')}")
