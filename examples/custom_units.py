"""Examples of defining and using custom units."""

from unifyt import Quantity, UnitRegistry

# Create a unit registry
registry = UnitRegistry()

print("=== Defining Custom Units ===")

# Define some unusual units
registry.define('furlong', '220 yard')
registry.define('fortnight', '14 day')

print("Defined: furlong = 220 yards")
print("Defined: fortnight = 14 days")

# Use custom units
print("\n=== Using Custom Units ===")
distance = Quantity(1, 'furlong')
print(f"Distance: {distance}")
print(f"Distance in meters: {distance.to('meter')}")
print(f"Distance in feet: {distance.to('foot')}")

time_period = Quantity(1, 'fortnight')
print(f"\nTime period: {time_period}")
print(f"Time in hours: {time_period.to('hour')}")
print(f"Time in seconds: {time_period.to('second')}")

# Calculate speed in unusual units
print("\n=== Speed in Furlongs per Fortnight ===")
distance_furlongs = Quantity(10, 'furlong')
time_fortnights = Quantity(2, 'fortnight')
speed = distance_furlongs / time_fortnights
print(f"Speed: {speed}")

# Convert to more common units
speed_ms = speed.to('meter/second')
print(f"Speed in m/s: {speed_ms}")

# Create aliases
print("\n=== Creating Aliases ===")
registry.alias('m', 'meter')
registry.alias('km', 'kilometer')
registry.alias('s', 'second')

print("Created aliases: m, km, s")
print(f"Aliases: {registry.list_aliases()}")

# Domain-specific units
print("\n=== Domain-Specific Units ===")
registry.define('parsec', '3.086e16 meter')  # Astronomical unit
registry.define('angstrom', '1e-10 meter')   # Atomic scale

distance_space = Quantity(1, 'parsec')
print(f"Distance: {distance_space}")
print(f"Distance in km: {distance_space.to('kilometer')}")

wavelength = Quantity(5000, 'angstrom')
print(f"\nWavelength: {wavelength}")
print(f"Wavelength in nm: {wavelength.to('meter') * 1e9} nanometers")
