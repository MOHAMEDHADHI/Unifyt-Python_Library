# Unifyt Units Catalog v0.2.0

## 📋 Complete Reference of All 300+ Units

This document provides a comprehensive catalog of all units supported by Unifyt v0.2.0. - Complete Reference

## 📚 Overview

Unifyt supports **300+ units** across multiple domains. This document categorizes them by use case and provides practical examples.

---

## 🏠 General Use Units (Everyday Applications)

### Length - Distance Measurement
**Common Units**: meter, kilometer, centimeter, millimeter, mile, yard, foot, inch

**Use Cases**:
- Construction and carpentry
- Road distances and navigation
- Height and width measurements
- Sports and athletics

**Examples**:
```python
from unifyt import Quantity

# Construction
room_length = Quantity(5, 'meter')
wall_height = Quantity(8, 'foot')

# Navigation
trip_distance = Quantity(150, 'mile')
print(trip_distance.to('kilometer'))  # 241.4 km

# Sports
sprint_distance = Quantity(100, 'meter')
marathon = Quantity(26.2, 'mile')
```

**Available Units**:
- **Metric**: meter (m), kilometer (km), centimeter (cm), millimeter (mm)
- **Imperial**: mile (mi), yard (yd), foot (ft), inch (in)

---

### Mass - Weight Measurement
**Common Units**: kilogram, gram, pound, ounce, ton

**Use Cases**:
- Cooking and recipes
- Body weight and fitness
- Shipping and logistics
- Grocery shopping

**Examples**:
```python
# Cooking
flour = Quantity(500, 'gram')
sugar = Quantity(2, 'cup')

# Body weight
weight = Quantity(70, 'kilogram')
print(weight.to('pound'))  # 154.3 lb

# Shipping
package = Quantity(5, 'pound')
print(package.to('kilogram'))  # 2.27 kg
```

**Available Units**:
- **Metric**: kilogram (kg), gram (g), milligram (mg), ton, tonne
- **Imperial**: pound (lb), ounce (oz), stone (st)
- **Specialized**: carat (ct), grain (gr)

---

### Time - Duration Measurement
**Common Units**: second, minute, hour, day, week, month, year

**Use Cases**:
- Scheduling and calendars
- Cooking timers
- Project planning
- Age calculation

**Examples**:
```python
# Cooking
bake_time = Quantity(45, 'minute')
print(bake_time.to('second'))  # 2700 s

# Project planning
deadline = Quantity(2, 'week')
print(deadline.to('day'))  # 14 days

# Age
age = Quantity(30, 'year')
print(age.to('day'))  # 10,957 days
```

**Available Units**:
- **Basic**: second (s), minute (min), hour (h), day (d)
- **Extended**: week, fortnight, month, year (yr)
- **Long**: decade, century, millennium

---

### Temperature - Heat Measurement
**Common Units**: celsius, fahrenheit, kelvin

**Use Cases**:
- Weather forecasting
- Cooking temperatures
- HVAC systems
- Medical thermometers

**Examples**:
```python
# Weather
temp = Quantity(25, 'celsius')
# Note: Temperature offset conversions coming in v0.3.0

# Cooking
oven_temp = Quantity(350, 'fahrenheit')

# Science
absolute_zero = Quantity(0, 'kelvin')
```

**Available Units**:
- **Metric**: celsius (C, degC)
- **Imperial**: fahrenheit (F, degF)
- **Scientific**: kelvin (K)

---

### Volume - Capacity Measurement
**Common Units**: liter, milliliter, gallon, cup, pint, quart

**Use Cases**:
- Cooking and baking
- Fuel consumption
- Beverage containers
- Aquariums and pools

**Examples**:
```python
# Cooking
milk = Quantity(2, 'cup')
print(milk.to('milliliter'))  # 473 mL

# Fuel
tank = Quantity(15, 'gallon')
print(tank.to('liter'))  # 56.8 L

# Beverages
bottle = Quantity(500, 'milliliter')
```

**Available Units**:
- **Metric**: liter (L), milliliter (mL)
- **Imperial**: gallon (gal), quart (qt), pint (pt), cup, fluid_ounce (fl_oz)

---

### Area - Surface Measurement
**Common Units**: square meter, square foot, acre, hectare

**Use Cases**:
- Real estate
- Land surveying
- Gardening and farming
- Floor planning

**Examples**:
```python
# Real estate
house_area = Quantity(2000, 'foot') ** 2
print(house_area.to('meter^2'))

# Farming
farm = Quantity(50, 'acre')
print(farm.to('hectare'))  # 20.2 ha

# Gardening
garden = Quantity(100, 'meter^2')
```

**Available Units**:
- **Metric**: square meter (m²), hectare (ha)
- **Imperial**: square foot (ft²), acre

---

### Speed - Velocity Measurement
**Common Units**: kilometer/hour, mile/hour, meter/second

**Use Cases**:
- Vehicle speed
- Running pace
- Wind speed
- Internet speed

**Examples**:
```python
# Driving
speed = Quantity(60, 'mile/hour')
print(speed.to('kilometer/hour'))  # 96.6 km/h

# Running
pace = Quantity(10, 'kilometer/hour')

# Wind
wind_speed = Quantity(20, 'knot')
print(wind_speed.to('meter/second'))
```

**Available Units**:
- **Metric**: meter/second (m/s), kilometer/hour (km/h)
- **Imperial**: mile/hour (mph), foot/second (ft/s)
- **Nautical**: knot (kt, kn)
- **Aviation**: mach

---

### Energy - Power Consumption
**Common Units**: joule, calorie, kilowatt_hour, BTU

**Use Cases**:
- Electricity bills
- Food nutrition
- Heating and cooling
- Battery capacity

**Examples**:
```python
# Electricity
consumption = Quantity(500, 'kilowatt_hour')
print(consumption.to('joule'))

# Nutrition
food_energy = Quantity(2000, 'kilocalorie')
print(food_energy.to('joule'))

# Heating
heater = Quantity(10000, 'BTU')
```

**Available Units**:
- **Metric**: joule (J), kilojoule (kJ)
- **Nutrition**: calorie (cal), kilocalorie (kcal, Calorie)
- **Electrical**: watt_hour (Wh), kilowatt_hour (kWh)
- **HVAC**: british_thermal_unit (BTU)

---

### Power - Rate of Energy
**Common Units**: watt, kilowatt, horsepower

**Use Cases**:
- Appliance ratings
- Engine power
- Solar panels
- Light bulbs

**Examples**:
```python
# Appliances
microwave = Quantity(1000, 'watt')
print(microwave.to('kilowatt'))  # 1 kW

# Engines
car_engine = Quantity(150, 'horsepower')
print(car_engine.to('kilowatt'))  # 111.9 kW

# Solar
panel = Quantity(300, 'watt')
```

**Available Units**:
- **Metric**: watt (W), kilowatt (kW), megawatt (MW)
- **Automotive**: horsepower (hp), metric_horsepower (PS)

---

### Pressure - Force per Area
**Common Units**: pascal, bar, atmosphere, psi

**Use Cases**:
- Tire pressure
- Weather forecasting
- Scuba diving
- Hydraulic systems

**Examples**:
```python
# Tire pressure
tire = Quantity(32, 'psi')
print(tire.to('bar'))  # 2.2 bar

# Weather
atmospheric = Quantity(1, 'atmosphere')
print(atmospheric.to('pascal'))  # 101,325 Pa

# Diving
depth_pressure = Quantity(3, 'bar')
```

**Available Units**:
- **Metric**: pascal (Pa), kilopascal (kPa), bar
- **Imperial**: psi (pound per square inch)
- **Atmospheric**: atmosphere (atm), torr, mmHg, inHg

---

### Angle - Rotation Measurement
**Common Units**: degree, radian

**Use Cases**:
- Navigation and compass
- Geometry and trigonometry
- Camera angles
- Astronomy

**Examples**:
```python
# Navigation
bearing = Quantity(45, 'degree')
print(bearing.to('radian'))

# Geometry
right_angle = Quantity(90, 'degree')

# Astronomy
arc = Quantity(30, 'arcminute')
```

**Available Units**:
- **Common**: degree (deg), radian (rad)
- **Precision**: arcminute, arcsecond
- **Surveying**: gradian (grad)

---

### Data Storage - Digital Information
**Common Units**: byte, kilobyte, megabyte, gigabyte, terabyte

**Use Cases**:
- Computer storage
- File sizes
- Internet data plans
- Memory capacity

**Examples**:
```python
# File size
video = Quantity(4.7, 'gigabyte')
print(video.to('megabyte'))  # 4,700 MB

# Storage
hard_drive = Quantity(1, 'terabyte')
print(hard_drive.to('gigabyte'))  # 1,000 GB

# Memory
ram = Quantity(16, 'gibibyte')
print(ram.to('gigabyte'))  # 17.18 GB
```

**Available Units**:
- **Decimal**: bit (b), byte (B), kilobyte (kB), megabyte (MB), gigabyte (GB), terabyte (TB), petabyte (PB)
- **Binary**: kibibyte (KiB), mebibyte (MiB), gibibyte (GiB), tebibyte (TiB)

---

## 🔬 Scientific Use Units (Research & Engineering)

### Atomic & Nuclear Physics

**Units**: atomic_mass_unit, dalton, electron_mass, proton_mass, neutron_mass, electronvolt, rydberg, hartree, fermi

**Use Cases**:
- Particle physics experiments
- Mass spectrometry
- Nuclear reactions
- Quantum chemistry

**Examples**:
```python
from unifyt import Quantity, constants

# Atomic mass
carbon_12 = Quantity(12, 'atomic_mass_unit')
print(carbon_12.to('kilogram'))

# Particle mass
electron = Quantity(1, 'electron_mass')
proton = Quantity(1, 'proton_mass')

# Nuclear energy
binding_energy = Quantity(8, 'megaelectronvolt')

# Quantum chemistry
energy_level = Quantity(1, 'hartree')
print(energy_level.to('electronvolt'))
```

**Available Units**:
- **Mass**: atomic_mass_unit (amu, u), dalton (Da), electron_mass (m_e), proton_mass (m_p), neutron_mass (m_n), muon_mass, tau_mass
- **Energy**: electronvolt (eV), rydberg (Ry), hartree (Ha)
- **Length**: fermi (fm), angstrom (Å)

---

### Astronomy & Astrophysics

**Units**: astronomical_unit, light_year, parsec, kiloparsec, megaparsec, solar_mass, earth_mass

**Use Cases**:
- Stellar distances
- Galactic measurements
- Cosmological calculations
- Planetary science

**Examples**:
```python
# Stellar distances
distance = Quantity(4.2, 'light_year')  # Proxima Centauri
print(distance.to('parsec'))  # 1.3 pc

# Galactic scale
galaxy_distance = Quantity(2.5, 'megaparsec')  # Andromeda
print(galaxy_distance.to('light_year'))

# Stellar mass
star_mass = Quantity(2, 'solar_mass')
print(star_mass.to('kilogram'))

# Planetary mass
planet = Quantity(1, 'earth_mass')
```

**Available Units**:
- **Distance**: astronomical_unit (au, AU), light_year (ly), parsec (pc), kiloparsec (kpc), megaparsec (Mpc)
- **Mass**: solar_mass (M_sun), earth_mass (M_earth), jupiter_mass (M_jupiter), moon_mass (M_moon)
- **Nautical**: nautical_mile (nmi), fathom, league

---

### Electromagnetic Theory

**Units**: farad, henry, tesla, weber, gauss, maxwell, volt, ampere, ohm, coulomb

**Use Cases**:
- Circuit design
- Magnetic field measurements
- Capacitor and inductor selection
- Electromagnetic compatibility

**Examples**:
```python
# Capacitance
capacitor = Quantity(100, 'microfarad')
print(capacitor.to('picofarad'))

# Inductance
inductor = Quantity(10, 'millihenry')

# Magnetic field
earth_field = Quantity(50, 'microtesla')
print(earth_field.to('gauss'))  # 0.5 G

# Magnetic flux
flux = Quantity(1, 'weber')
print(flux.to('maxwell'))

# RC time constant
R = Quantity(1000, 'ohm')
C = Quantity(100, 'microfarad')
tau = R * C
print(tau.to('millisecond'))
```

**Available Units**:
- **Capacitance**: farad (F), millifarad (mF), microfarad (uF), nanofarad (nF), picofarad (pF)
- **Inductance**: henry (H), millihenry (mH), microhenry (uH), nanohenry (nH)
- **Magnetic Field**: tesla (T), millitesla (mT), microtesla (uT), nanotesla (nT), gauss (G), milligauss (mG)
- **Magnetic Flux**: weber (Wb), milliweber (mWb), maxwell (Mx)
- **Voltage**: volt (V), millivolt (mV), microvolt (uV), nanovolt (nV), kilovolt (kV), megavolt (MV)
- **Current**: ampere (A), milliampere (mA), microampere (uA), nanoampere (nA), picoampere (pA), kiloampere (kA)
- **Resistance**: ohm (Ω), kiloohm (kΩ), megaohm (MΩ)
- **Charge**: coulomb (C)

---

### Radioactivity & Nuclear Medicine

**Units**: becquerel, curie, gray, sievert, rad, rem, rutherford

**Use Cases**:
- Radiation safety
- Nuclear medicine
- Radiotherapy
- Environmental monitoring

**Examples**:
```python
# Activity
source = Quantity(1, 'curie')
print(source.to('becquerel'))  # 3.7×10^10 Bq

# Absorbed dose
dose = Quantity(1, 'gray')
print(dose.to('rad'))  # 100 rad

# Equivalent dose
exposure = Quantity(1, 'sievert')
print(exposure.to('rem'))  # 100 rem

# Medical imaging
scan_dose = Quantity(5, 'millisievert')

# Safety limit
annual_limit = Quantity(20, 'millisievert')
```

**Available Units**:
- **Activity**: becquerel (Bq), kilobecquerel (kBq), megabecquerel (MBq), gigabecquerel (GBq), curie (Ci), millicurie (mCi), microcurie (uCi), rutherford (Rd)
- **Absorbed Dose**: gray (Gy), milligray (mGy), rad
- **Equivalent Dose**: sievert (Sv), millisievert (mSv), microsievert (uSv), rem, millirem (mrem)

---

### High-Precision Time Measurement

**Units**: picosecond, femtosecond, attosecond, shake, nanosecond, microsecond

**Use Cases**:
- Laser physics
- Ultrafast spectroscopy
- Particle physics
- Telecommunications

**Examples**:
```python
# Laser pulse
pulse_duration = Quantity(100, 'femtosecond')
print(pulse_duration.to('second'))  # 1×10^-13 s

# Atomic processes
transition_time = Quantity(1, 'attosecond')

# Nuclear physics
shake_time = Quantity(1, 'shake')  # 10 ns

# Telecommunications
signal_delay = Quantity(50, 'picosecond')
```

**Available Units**:
- **Ultra-fast**: attosecond (as, 10^-18 s), femtosecond (fs, 10^-15 s), picosecond (ps, 10^-12 s)
- **Fast**: nanosecond (ns, 10^-9 s), microsecond (us, 10^-6 s), millisecond (ms, 10^-3 s)
- **Nuclear**: shake (10^-8 s)

---

### Microscopic Length Scales

**Units**: nanometer, picometer, femtometer, angstrom, fermi

**Use Cases**:
- Nanotechnology
- Crystallography
- Molecular biology
- Semiconductor manufacturing

**Examples**:
```python
# Nanotechnology
nanoparticle = Quantity(50, 'nanometer')

# Crystallography
lattice_spacing = Quantity(3.5, 'angstrom')
print(lattice_spacing.to('nanometer'))  # 0.35 nm

# Nuclear physics
nuclear_radius = Quantity(5, 'fermi')
print(nuclear_radius.to('meter'))  # 5×10^-15 m

# DNA
dna_width = Quantity(2, 'nanometer')
```

**Available Units**:
- **Nano**: nanometer (nm, 10^-9 m), picometer (pm, 10^-12 m), femtometer (fm, 10^-15 m)
- **Specialized**: angstrom (Å, 10^-10 m), fermi (fm, 10^-15 m)

---

### High Energy Physics

**Units**: gigaelectronvolt, teraelectronvolt, megajoule, gigajoule, ton_tnt, kiloton_tnt, megaton_tnt

**Use Cases**:
- Particle accelerators
- Nuclear weapons
- Cosmic ray physics
- High-energy astrophysics

**Examples**:
```python
# Particle accelerator
proton_energy = Quantity(7, 'teraelectronvolt')  # LHC
print(proton_energy.to('joule'))

# Nuclear explosion
yield_energy = Quantity(15, 'kiloton_tnt')  # Hiroshima
print(yield_energy.to('joule'))

# Cosmic ray
cosmic_energy = Quantity(100, 'gigaelectronvolt')
```

**Available Units**:
- **Particle Physics**: electronvolt (eV), kiloelectronvolt (keV), megaelectronvolt (MeV), gigaelectronvolt (GeV), teraelectronvolt (TeV)
- **Large Scale**: megajoule (MJ), gigajoule (GJ), erg
- **Explosive**: ton_tnt, kiloton_tnt, megaton_tnt, quad, therm

---

### Fluid Dynamics & Viscosity

**Units**: poise, centipoise, stokes, centistokes, pascal_second

**Use Cases**:
- Oil and lubricant testing
- Paint and coating industry
- Food processing
- Pharmaceutical manufacturing

**Examples**:
```python
# Motor oil
oil_viscosity = Quantity(100, 'centipoise')
print(oil_viscosity.to('pascal_second'))

# Kinematic viscosity
water_visc = Quantity(1, 'centistokes')

# Industrial fluid
hydraulic_oil = Quantity(50, 'poise')
```

**Available Units**:
- **Dynamic Viscosity**: pascal_second (Pa·s), poise (P), centipoise (cP)
- **Kinematic Viscosity**: stokes (St), centistokes (cSt)

---

### Chemistry & Concentration

**Units**: molar, millimolar, micromolar, nanomolar, gram_per_liter

**Use Cases**:
- Solution preparation
- Biochemistry
- Analytical chemistry
- Pharmacology

**Examples**:
```python
# Solution concentration
nacl_solution = Quantity(1, 'molar')  # 1 M NaCl
print(nacl_solution.to('millimolar'))  # 1000 mM

# Biochemistry
enzyme_conc = Quantity(10, 'micromolar')

# Pharmacology
drug_dose = Quantity(50, 'nanomolar')

# Density
solution_density = Quantity(1.2, 'gram_per_liter')
```

**Available Units**:
- **Concentration**: molar (M, mol/L), millimolar (mM), micromolar (uM), nanomolar (nM)
- **Density**: kilogram_per_cubic_meter (kg/m³), gram_per_cubic_centimeter (g/cm³), gram_per_liter (g/L)
- **Molar Mass**: gram_per_mole (g/mol), kilogram_per_mole (kg/mol)

---

### Frequency & Rotation

**Units**: hertz, kilohertz, megahertz, gigahertz, terahertz, rpm, rps

**Use Cases**:
- Radio and telecommunications
- Spectroscopy
- Motor speed
- Signal processing

**Examples**:
```python
# Radio
fm_station = Quantity(100, 'megahertz')

# WiFi
wifi_freq = Quantity(2.4, 'gigahertz')

# Spectroscopy
infrared = Quantity(30, 'terahertz')

# Motor speed
engine_rpm = Quantity(3000, 'rpm')
print(engine_rpm.to('hertz'))  # 50 Hz
```

**Available Units**:
- **Frequency**: hertz (Hz), millihertz (mHz), kilohertz (kHz), megahertz (MHz), gigahertz (GHz), terahertz (THz)
- **Rotation**: rpm (revolutions per minute), rps (revolutions per second)

---

### Force & Acceleration

**Units**: newton, dyne, kilogram_force, pound_force, kip, gal, standard_gravity

**Use Cases**:
- Structural engineering
- Seismology
- Aerospace
- Mechanical testing

**Examples**:
```python
# Structural load
beam_load = Quantity(1000, 'newton')
print(beam_load.to('kilogram_force'))

# Seismology
earthquake_accel = Quantity(100, 'gal')  # Galileo
print(earthquake_accel.to('meter/second^2'))

# Aerospace
thrust = Quantity(10, 'kilonewton')

# Gravity
g_force = Quantity(3, 'standard_gravity')
```

**Available Units**:
- **Force**: newton (N), kilonewton (kN), meganewton (MN), dyne, kilogram_force (kgf), gram_force (gf), ton_force (tf), pound_force (lbf), poundal, kip
- **Acceleration**: gal (Galileo), standard_gravity (g0)

---

### Illumination & Light

**Units**: lux, lumen, foot_candle, phot, candela

**Use Cases**:
- Lighting design
- Photography
- Workplace safety
- Horticulture

**Examples**:
```python
# Indoor lighting
office_light = Quantity(500, 'lux')

# Photography
studio_light = Quantity(1000, 'foot_candle')
print(studio_light.to('lux'))

# Light output
bulb = Quantity(800, 'lumen')

# Luminous intensity
led = Quantity(1, 'candela')
```

**Available Units**:
- **Illuminance**: lux (lx), foot_candle (fc), phot (ph)
- **Luminous Flux**: lumen (lm)
- **Luminous Intensity**: candela (cd)

---

### Flow Rate & Fuel Efficiency

**Units**: cubic_meter_per_second, liter_per_second, gallon_per_minute, mile_per_gallon, kilometer_per_liter

**Use Cases**:
- Hydraulic systems
- HVAC design
- Fuel economy
- Water treatment

**Examples**:
```python
# Water flow
pump_rate = Quantity(10, 'gallon_per_minute')
print(pump_rate.to('liter_per_second'))

# HVAC
air_flow = Quantity(1, 'cubic_meter_per_second')

# Fuel economy
car_efficiency = Quantity(30, 'mile_per_gallon')
print(car_efficiency.to('kilometer_per_liter'))

# Fuel consumption
consumption = Quantity(8, 'liter_per_100km')
```

**Available Units**:
- **Flow Rate**: cubic_meter_per_second (m³/s), liter_per_second (L/s), liter_per_minute (L/min), gallon_per_minute (gpm)
- **Fuel Efficiency**: mile_per_gallon (mpg), kilometer_per_liter (km/L), liter_per_100km (L/100km)

---

### Catalytic Activity & Biochemistry

**Units**: katal, unit (enzyme unit)

**Use Cases**:
- Enzyme kinetics
- Biochemical assays
- Clinical diagnostics
- Biotechnology

**Examples**:
```python
# Enzyme activity
enzyme = Quantity(1, 'katal')  # 1 mol/s

# Clinical test
enzyme_unit = Quantity(100, 'unit')  # 100 U
print(enzyme_unit.to('katal'))
```

**Available Units**:
- **Catalytic Activity**: katal (kat), unit (U, enzyme unit)

---

### Specialized & Historical Units

**Units**: chain, furlong, league, stone, slug, carat, grain

**Use Cases**:
- Land surveying (historical)
- Horse racing
- Gemology
- Ammunition

**Examples**:
```python
# Surveying
property_length = Quantity(10, 'chain')
print(property_length.to('meter'))

# Horse racing
race_distance = Quantity(1, 'furlong')  # 220 yards

# Gemology
diamond = Quantity(1, 'carat')  # 0.2 grams

# Body weight (UK)
weight = Quantity(12, 'stone')
print(weight.to('kilogram'))
```

**Available Units**:
- **Surveying**: chain, furlong, league, fathom
- **Mass**: stone (st), slug, carat (ct), grain (gr)

---

## 📊 Units by Domain Summary

### Engineering Domains

| Domain | Key Units | Count |
|--------|-----------|-------|
| **Mechanical** | newton, pascal, joule, watt | 30+ |
| **Electrical** | volt, ampere, ohm, farad, henry | 40+ |
| **Civil** | meter, kilogram, pascal, newton | 20+ |
| **Chemical** | molar, liter, gram, kelvin | 25+ |
| **Aerospace** | mach, knot, standard_gravity | 15+ |

### Scientific Domains

| Domain | Key Units | Count |
|--------|-----------|-------|
| **Physics** | joule, newton, tesla, hertz | 50+ |
| **Chemistry** | molar, gram, liter, kelvin | 30+ |
| **Astronomy** | parsec, light_year, solar_mass | 15+ |
| **Nuclear** | becquerel, gray, sievert | 20+ |
| **Quantum** | electronvolt, hartree, angstrom | 15+ |

### Everyday Domains

| Domain | Key Units | Count |
|--------|-----------|-------|
| **Cooking** | gram, cup, liter, celsius | 15+ |
| **Fitness** | kilogram, meter, calorie | 10+ |
| **Navigation** | mile, kilometer, knot | 10+ |
| **Computing** | byte, gigabyte, terabyte | 15+ |
| **Home** | watt, kilowatt_hour, liter | 20+ |

---

## 🎯 Quick Reference by Use Case

### For Students
- **Physics**: meter, kilogram, second, joule, newton, watt
- **Chemistry**: gram, liter, molar, celsius, joule
- **Math**: radian, degree, dimensionless

### For Engineers
- **Mechanical**: newton, pascal, joule, watt, meter
- **Electrical**: volt, ampere, ohm, farad, henry, tesla
- **Civil**: meter, kilogram, pascal, newton, cubic_meter

### For Scientists
- **Particle Physics**: electronvolt, femtometer, attosecond
- **Astrophysics**: parsec, light_year, solar_mass
- **Nuclear**: becquerel, gray, sievert, atomic_mass_unit

### For Developers
- **Data**: byte, kilobyte, megabyte, gigabyte, terabyte
- **Performance**: hertz, megahertz, gigahertz
- **Network**: bit, byte, megabyte_per_second

### For Home Use
- **Cooking**: gram, cup, liter, celsius, fahrenheit
- **Shopping**: kilogram, pound, liter, gallon
- **Energy**: kilowatt_hour, watt, BTU

---

## 📖 Complete Alphabetical Index

[See QUICK_REFERENCE.md for complete alphabetical listing]

---

## 🚀 Getting Started

```python
from unifyt import Quantity

# Pick any unit from this catalog
measurement = Quantity(value, 'unit_name')

# Convert to any compatible unit
result = measurement.to('target_unit')

# Perform calculations
combined = measurement1 + measurement2
product = measurement1 * measurement2
```

---

**Total Units**: 300+  
**Categories**: 30+  
**Version**: 0.2.0  
**Last Updated**: December 24, 2024

For more information, see:
- [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) - Full usage guide
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick lookup
- [docs/api_reference.md](docs/api_reference.md) - API documentation
