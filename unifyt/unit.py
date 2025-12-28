"""Unit class for representing physical units."""

from __future__ import annotations
from typing import Dict, Optional
from unifyt.dimensions import Dimension


class Unit:
    """
    Represents a physical unit.
    
    Examples:
        >>> meter = Unit('meter')
        >>> second = Unit('second')
        >>> speed_unit = meter / second
    """
    
    # Base SI units
    _BASE_UNITS = {
        'meter': Dimension(length=1),
        'kilogram': Dimension(mass=1),
        'second': Dimension(time=1),
        'ampere': Dimension(current=1),
        'kelvin': Dimension(temperature=1),
        'mole': Dimension(amount=1),
        'candela': Dimension(luminosity=1),
        'dimensionless': Dimension(),
    }
    
    # Conversion factors to base units
    _CONVERSIONS = {
        # Length
        'meter': 1.0, 'm': 1.0, 'meters': 1.0,
        'kilometer': 1000.0, 'km': 1000.0, 'kilometers': 1000.0,
        'centimeter': 0.01, 'cm': 0.01, 'centimeters': 0.01,
        'millimeter': 0.001, 'mm': 0.001, 'millimeters': 0.001,
        'micrometer': 1e-6, 'um': 1e-6, 'micrometers': 1e-6,
        'nanometer': 1e-9, 'nm': 1e-9, 'nanometers': 1e-9,
        'angstrom': 1e-10, 'Å': 1e-10,
        'mile': 1609.344, 'mi': 1609.344, 'miles': 1609.344,
        'yard': 0.9144, 'yd': 0.9144, 'yards': 0.9144,
        'foot': 0.3048, 'ft': 0.3048, 'feet': 0.3048,
        'inch': 0.0254, 'in': 0.0254, 'inches': 0.0254,
        
        # Mass
        'kilogram': 1.0, 'kg': 1.0, 'kilograms': 1.0,
        'gram': 0.001, 'g': 0.001, 'grams': 0.001,
        'milligram': 1e-6, 'mg': 1e-6, 'milligrams': 1e-6,
        'microgram': 1e-9, 'ug': 1e-9, 'micrograms': 1e-9,
        'pound': 0.453592, 'lb': 0.453592, 'pounds': 0.453592,
        'ounce': 0.0283495, 'oz': 0.0283495, 'ounces': 0.0283495,
        'ton': 1000.0, 'tons': 1000.0, 'tonne': 1000.0, 'tonnes': 1000.0,
        
        # Time
        'second': 1.0, 's': 1.0, 'seconds': 1.0, 'sec': 1.0,
        'millisecond': 0.001, 'ms': 0.001, 'milliseconds': 0.001,
        'microsecond': 1e-6, 'us': 1e-6, 'microseconds': 1e-6,
        'nanosecond': 1e-9, 'ns': 1e-9, 'nanoseconds': 1e-9,
        'minute': 60.0, 'min': 60.0, 'minutes': 60.0,
        'hour': 3600.0, 'h': 3600.0, 'hr': 3600.0, 'hours': 3600.0,
        'day': 86400.0, 'd': 86400.0, 'days': 86400.0,
        'week': 604800.0, 'weeks': 604800.0,
        'year': 31536000.0, 'yr': 31536000.0, 'years': 31536000.0,
        
        # Temperature (offset handled separately)
        'kelvin': 1.0, 'K': 1.0,
        'celsius': 1.0, 'C': 1.0, 'degC': 1.0,
        'fahrenheit': 5.0/9.0, 'F': 5.0/9.0, 'degF': 5.0/9.0,
        
        # Current
        'ampere': 1.0, 'A': 1.0, 'amperes': 1.0, 'amp': 1.0, 'amps': 1.0,
        'milliampere': 0.001, 'mA': 0.001,
        
        # Amount
        'mole': 1.0, 'mol': 1.0, 'moles': 1.0,
        
        # Luminosity
        'candela': 1.0, 'cd': 1.0,
        
        # Energy
        'joule': 1.0, 'J': 1.0, 'joules': 1.0,
        'kilojoule': 1000.0, 'kJ': 1000.0,
        'calorie': 4.184, 'cal': 4.184, 'calories': 4.184,
        'kilocalorie': 4184.0, 'kcal': 4184.0, 'Calorie': 4184.0,
        'electronvolt': 1.602176634e-19, 'eV': 1.602176634e-19,
        'watt_hour': 3600.0, 'Wh': 3600.0,
        'kilowatt_hour': 3.6e6, 'kWh': 3.6e6,
        
        # Power
        'watt': 1.0, 'W': 1.0, 'watts': 1.0,
        'kilowatt': 1000.0, 'kW': 1000.0, 'kilowatts': 1000.0,
        'megawatt': 1e6, 'MW': 1e6, 'megawatts': 1e6,
        'horsepower': 745.7, 'hp': 745.7,
        
        # Pressure
        'pascal': 1.0, 'Pa': 1.0,
        'kilopascal': 1000.0, 'kPa': 1000.0,
        'megapascal': 1e6, 'MPa': 1e6,
        'bar': 1e5, 'bars': 1e5,
        'atmosphere': 101325.0, 'atm': 101325.0,
        'psi': 6894.76, 'PSI': 6894.76,
        'torr': 133.322, 'Torr': 133.322,
        
        # Force
        'newton': 1.0, 'N': 1.0, 'newtons': 1.0,
        'kilonewton': 1000.0, 'kN': 1000.0,
        'pound_force': 4.44822, 'lbf': 4.44822,
        
        # Frequency
        'hertz': 1.0, 'Hz': 1.0,
        'kilohertz': 1000.0, 'kHz': 1000.0,
        'megahertz': 1e6, 'MHz': 1e6,
        'gigahertz': 1e9, 'GHz': 1e9,
        
        # Voltage
        'volt': 1.0, 'V': 1.0, 'volts': 1.0,
        'millivolt': 0.001, 'mV': 0.001,
        'kilovolt': 1000.0, 'kV': 1000.0,
        
        # Charge
        'coulomb': 1.0, 'C': 1.0, 'coulombs': 1.0,
        
        # Resistance
        'ohm': 1.0, 'Ω': 1.0, 'ohms': 1.0,
        'kiloohm': 1000.0, 'kΩ': 1000.0,
        'megaohm': 1e6, 'MΩ': 1e6,
        
        # Volume
        'liter': 0.001, 'L': 0.001, 'liters': 0.001, 'litre': 0.001, 'litres': 0.001,
        'milliliter': 1e-6, 'mL': 1e-6, 'milliliters': 1e-6,
        'gallon': 0.00378541, 'gal': 0.00378541, 'gallons': 0.00378541,
        'quart': 0.000946353, 'qt': 0.000946353,
        'pint': 0.000473176, 'pt': 0.000473176,
        'cup': 0.000236588, 'cups': 0.000236588,
        'fluid_ounce': 2.95735e-5, 'fl_oz': 2.95735e-5,
        
        # Area (derived but commonly used)
        'hectare': 10000.0, 'ha': 10000.0,
        'acre': 4046.86, 'acres': 4046.86,
        
        # Angle
        'radian': 1.0, 'rad': 1.0, 'radians': 1.0,
        'degree': 0.0174533, 'deg': 0.0174533, 'degrees': 0.0174533,
        'arcminute': 0.000290888, 'arcmin': 0.000290888,
        'arcsecond': 4.84814e-6, 'arcsec': 4.84814e-6,
        'gradian': 0.015708, 'grad': 0.015708,
        
        # Dimensionless
        'dimensionless': 1.0,
        'percent': 0.01, '%': 0.01,
        'ppm': 1e-6,
        'ppb': 1e-9,
        'ppt': 1e-12,
        
        # Advanced Length (Astronomical & Microscopic)
        'astronomical_unit': 1.495978707e11, 'au': 1.495978707e11,
        'light_year': 9.4607304725808e15, 'ly': 9.4607304725808e15,
        'parsec': 3.0856775814913673e16, 'pc': 3.0856775814913673e16,
        'kiloparsec': 3.0856775814913673e19, 'kpc': 3.0856775814913673e19,
        'megaparsec': 3.0856775814913673e22, 'Mpc': 3.0856775814913673e22,
        'picometer': 1e-12, 'pm': 1e-12,
        'femtometer': 1e-15, 'fm': 1e-15,
        'fermi': 1e-15,
        'nautical_mile': 1852.0, 'nmi': 1852.0,
        'fathom': 1.8288,
        'chain': 20.1168,
        'furlong': 201.168,
        'league': 4828.03,
        
        # Advanced Mass (Atomic & Large Scale)
        'atomic_mass_unit': 1.66053906660e-27, 'amu': 1.66053906660e-27, 'u': 1.66053906660e-27,
        'dalton': 1.66053906660e-27, 'Da': 1.66053906660e-27,
        'electron_mass': 9.1093837015e-31, 'm_e': 9.1093837015e-31,
        'proton_mass': 1.67262192369e-27, 'm_p': 1.67262192369e-27,
        'neutron_mass': 1.67492749804e-27, 'm_n': 1.67492749804e-27,
        'solar_mass': 1.98847e30, 'M_sun': 1.98847e30,
        'earth_mass': 5.97217e24, 'M_earth': 5.97217e24,
        'carat': 0.0002, 'ct': 0.0002,
        'grain': 6.479891e-5, 'gr': 6.479891e-5,
        'stone': 6.35029, 'st': 6.35029,
        'slug': 14.5939,
        
        # Advanced Time
        'picosecond': 1e-12, 'ps': 1e-12,
        'femtosecond': 1e-15, 'fs': 1e-15,
        'attosecond': 1e-18, 'as': 1e-18,
        'shake': 1e-8,
        'fortnight': 1209600.0,
        'month': 2629800.0,  # Average month (365.25/12 days)
        'decade': 315576000.0,
        'century': 3155760000.0,
        'millennium': 31557600000.0,
        
        # Advanced Energy
        'megajoule': 1e6, 'MJ': 1e6,
        'gigajoule': 1e9, 'GJ': 1e9,
        'erg': 1e-7,
        'british_thermal_unit': 1055.06, 'BTU': 1055.06, 'btu': 1055.06,
        'therm': 1.05506e8,
        'quad': 1.05506e18,
        'ton_tnt': 4.184e9,
        'kiloton_tnt': 4.184e12,
        'megaton_tnt': 4.184e15,
        'rydberg': 2.1798723611035e-18, 'Ry': 2.1798723611035e-18,
        'hartree': 4.3597447222071e-18, 'Ha': 4.3597447222071e-18,
        
        # Advanced Power
        'gigawatt': 1e9, 'GW': 1e9,
        'terawatt': 1e12, 'TW': 1e12,
        'milliwatt': 0.001, 'mW': 0.001,
        'microwatt': 1e-6, 'uW': 1e-6,
        'nanowatt': 1e-9, 'nW': 1e-9,
        'metric_horsepower': 735.5, 'PS': 735.5,
        'boiler_horsepower': 9809.5,
        
        # Advanced Pressure
        'gigapascal': 1e9, 'GPa': 1e9,
        'millibar': 100.0, 'mbar': 100.0,
        'microbar': 0.1, 'ubar': 0.1,
        'barye': 0.1,
        'technical_atmosphere': 98066.5, 'at': 98066.5,
        'inch_mercury': 3386.39, 'inHg': 3386.39,
        'millimeter_mercury': 133.322, 'mmHg': 133.322,
        'pound_per_square_inch': 6894.76, 'psi': 6894.76,
        
        # Advanced Force
        'meganewton': 1e6, 'MN': 1e6,
        'dyne': 1e-5, 'dyn': 1e-5,
        'kilogram_force': 9.80665, 'kgf': 9.80665,
        'gram_force': 0.00980665, 'gf': 0.00980665,
        'ton_force': 9806.65, 'tf': 9806.65,
        'poundal': 0.138255,
        'kip': 4448.22,
        
        # Advanced Frequency
        'terahertz': 1e12, 'THz': 1e12,
        'millihertz': 0.001, 'mHz': 0.001,
        'rpm': 1/60.0,  # Revolutions per minute
        'rps': 1.0,  # Revolutions per second
        
        # Advanced Voltage
        'megavolt': 1e6, 'MV': 1e6,
        'microvolt': 1e-6, 'uV': 1e-6,
        'nanovolt': 1e-9, 'nV': 1e-9,
        'statvolt': 299.792458,
        
        # Advanced Current
        'microampere': 1e-6, 'uA': 1e-6,
        'nanoampere': 1e-9, 'nA': 1e-9,
        'picoampere': 1e-12, 'pA': 1e-12,
        'kiloampere': 1000.0, 'kA': 1000.0,
        'statampere': 3.33564e-10,
        
        # Capacitance
        'farad': 1.0, 'F': 1.0,
        'millifarad': 0.001, 'mF': 0.001,
        'microfarad': 1e-6, 'uF': 1e-6,
        'nanofarad': 1e-9, 'nF': 1e-9,
        'picofarad': 1e-12, 'pF': 1e-12,
        
        # Inductance
        'henry': 1.0, 'H': 1.0,
        'millihenry': 0.001, 'mH': 0.001,
        'microhenry': 1e-6, 'uH': 1e-6,
        'nanohenry': 1e-9, 'nH': 1e-9,
        
        # Magnetic Field
        'tesla': 1.0, 'T': 1.0,
        'millitesla': 0.001, 'mT': 0.001,
        'microtesla': 1e-6, 'uT': 1e-6,
        'nanotesla': 1e-9, 'nT': 1e-9,
        'gauss': 1e-4, 'G': 1e-4,
        'milligauss': 1e-7, 'mG': 1e-7,
        
        # Magnetic Flux
        'weber': 1.0, 'Wb': 1.0,
        'milliweber': 0.001, 'mWb': 0.001,
        'maxwell': 1e-8, 'Mx': 1e-8,
        
        # Illuminance
        'lux': 1.0, 'lx': 1.0,
        'foot_candle': 10.764, 'fc': 10.764,
        'phot': 10000.0, 'ph': 10000.0,
        
        # Luminous Flux
        'lumen': 1.0, 'lm': 1.0,
        
        # Radioactivity
        'becquerel': 1.0, 'Bq': 1.0,
        'kilobecquerel': 1000.0, 'kBq': 1000.0,
        'megabecquerel': 1e6, 'MBq': 1e6,
        'gigabecquerel': 1e9, 'GBq': 1e9,
        'curie': 3.7e10, 'Ci': 3.7e10,
        'millicurie': 3.7e7, 'mCi': 3.7e7,
        'microcurie': 3.7e4, 'uCi': 3.7e4,
        'rutherford': 1e6, 'Rd': 1e6,
        
        # Absorbed Dose
        'gray': 1.0, 'Gy': 1.0,
        'milligray': 0.001, 'mGy': 0.001,
        'rad': 0.01,
        
        # Equivalent Dose
        'sievert': 1.0, 'Sv': 1.0,
        'millisievert': 0.001, 'mSv': 0.001,
        'microsievert': 1e-6, 'uSv': 1e-6,
        'rem': 0.01,
        'millirem': 1e-5, 'mrem': 1e-5,
        
        # Catalytic Activity
        'katal': 1.0, 'kat': 1.0,
        'unit': 1.66667e-8, 'U': 1.66667e-8,  # Enzyme unit
        
        # Data/Information
        'bit': 1.0, 'b': 1.0,
        'byte': 8.0, 'B': 8.0,
        'kilobyte': 8000.0, 'kB': 8000.0,
        'megabyte': 8e6, 'MB': 8e6,
        'gigabyte': 8e9, 'GB': 8e9,
        'terabyte': 8e12, 'TB': 8e12,
        'petabyte': 8e15, 'PB': 8e15,
        'kibibyte': 8192.0, 'KiB': 8192.0,
        'mebibyte': 8388608.0, 'MiB': 8388608.0,
        'gibibyte': 8589934592.0, 'GiB': 8589934592.0,
        'tebibyte': 8796093022208.0, 'TiB': 8796093022208.0,
        
        # Velocity
        'knot': 0.514444, 'kt': 0.514444, 'kn': 0.514444,
        'mach': 343.0,  # At sea level, 15°C
        
        # Acceleration
        'gal': 0.01,  # Galileo
        'standard_gravity': 9.80665, 'g0': 9.80665,
        
        # Viscosity (Dynamic)
        'pascal_second': 1.0, 'Pa_s': 1.0,
        'poise': 0.1, 'P': 0.1,
        'centipoise': 0.001, 'cP': 0.001,
        
        # Viscosity (Kinematic)
        'stokes': 1e-4, 'St': 1e-4,
        'centistokes': 1e-6, 'cSt': 1e-6,
        
        # Thermal Conductivity
        'watt_per_meter_kelvin': 1.0, 'W_m_K': 1.0,
        
        # Heat Capacity
        'joule_per_kelvin': 1.0, 'J_K': 1.0,
        
        # Specific Heat
        'joule_per_kilogram_kelvin': 1.0, 'J_kg_K': 1.0,
        
        # Molar Mass
        'gram_per_mole': 0.001, 'g_mol': 0.001,
        'kilogram_per_mole': 1.0, 'kg_mol': 1.0,
        
        # Concentration
        'molar': 1000.0, 'M': 1000.0,  # mol/L
        'millimolar': 1.0, 'mM': 1.0,
        'micromolar': 0.001, 'uM': 0.001,
        'nanomolar': 1e-6, 'nM': 1e-6,
        
        # Density
        'kilogram_per_cubic_meter': 1.0, 'kg_m3': 1.0,
        'gram_per_cubic_centimeter': 1000.0, 'g_cm3': 1000.0,
        'gram_per_liter': 1.0, 'g_L': 1.0,
        
        # Flow Rate
        'cubic_meter_per_second': 1.0, 'm3_s': 1.0,
        'liter_per_second': 0.001, 'L_s': 0.001,
        'liter_per_minute': 1.66667e-5, 'L_min': 1.66667e-5,
        'gallon_per_minute': 6.30902e-5, 'gpm': 6.30902e-5,
        
        # Fuel Efficiency
        'mile_per_gallon': 425144.0, 'mpg': 425144.0,  # Inverse meters
        'kilometer_per_liter': 1000.0, 'km_L': 1000.0,
        'liter_per_100km': 0.01, 'L_100km': 0.01,
    }
    
    # Map units to their base unit (auto-generated from conversions)
    _UNIT_TO_BASE = None  # Will be generated dynamically
    
    # Temperature offset units (special handling)
    _TEMPERATURE_OFFSETS = {
        'celsius': 273.15,
        'C': 273.15,
        'degC': 273.15,
        'fahrenheit': 459.67,
        'F': 459.67,
        'degF': 459.67,
    }
    
    # Cache for parsed units
    _unit_cache: Dict[str, 'Unit'] = {}
    
    @classmethod
    def _build_unit_to_base_map(cls) -> Dict[str, str]:
        """Build the unit to base unit mapping."""
        if cls._UNIT_TO_BASE is not None:
            return cls._UNIT_TO_BASE
        
        mapping = {}
        # Length units
        length_units = ['meter', 'm', 'meters', 'kilometer', 'km', 'kilometers', 
                       'centimeter', 'cm', 'centimeters', 'millimeter', 'mm', 'millimeters',
                       'micrometer', 'um', 'micrometers', 'nanometer', 'nm', 'nanometers',
                       'angstrom', 'Å', 'mile', 'mi', 'miles', 'yard', 'yd', 'yards',
                       'foot', 'ft', 'feet', 'inch', 'in', 'inches']
        for u in length_units:
            mapping[u] = 'meter'
        
        # Mass units
        mass_units = ['kilogram', 'kg', 'kilograms', 'gram', 'g', 'grams',
                     'milligram', 'mg', 'milligrams', 'microgram', 'ug', 'micrograms',
                     'pound', 'lb', 'pounds', 'ounce', 'oz', 'ounces',
                     'ton', 'tons', 'tonne', 'tonnes']
        for u in mass_units:
            mapping[u] = 'kilogram'
        
        # Time units
        time_units = ['second', 's', 'seconds', 'sec', 'millisecond', 'ms', 'milliseconds',
                     'microsecond', 'us', 'microseconds', 'nanosecond', 'ns', 'nanoseconds',
                     'minute', 'min', 'minutes', 'hour', 'h', 'hr', 'hours',
                     'day', 'd', 'days', 'week', 'weeks', 'year', 'yr', 'years']
        for u in time_units:
            mapping[u] = 'second'
        
        # Temperature units
        temp_units = ['kelvin', 'K', 'celsius', 'C', 'degC', 'fahrenheit', 'F', 'degF']
        for u in temp_units:
            mapping[u] = 'kelvin'
        
        # Current units
        current_units = ['ampere', 'A', 'amperes', 'amp', 'amps', 'milliampere', 'mA']
        for u in current_units:
            mapping[u] = 'ampere'
        
        # Amount units
        amount_units = ['mole', 'mol', 'moles']
        for u in amount_units:
            mapping[u] = 'mole'
        
        # Luminosity units
        lum_units = ['candela', 'cd']
        for u in lum_units:
            mapping[u] = 'candela'
        
        # Dimensionless
        mapping['dimensionless'] = 'dimensionless'
        mapping['percent'] = 'dimensionless'
        mapping['%'] = 'dimensionless'
        mapping['ppm'] = 'dimensionless'
        mapping['ppb'] = 'dimensionless'
        
        cls._UNIT_TO_BASE = mapping
        return mapping
    
    def __init__(self, unit_str: str, scale: float = 1.0):
        """
        Initialize a Unit.
        
        Args:
            unit_str: String representation of the unit
            scale: Scale factor for the unit
        """
        # Check cache first
        cache_key = f"{unit_str}:{scale}"
        if cache_key in Unit._unit_cache:
            cached = Unit._unit_cache[cache_key]
            self._name = cached._name
            self._components = cached._components
            self._scale = cached._scale
            return
        
        self._parse_unit(unit_str)
        self._scale = scale
        
        # Cache the unit
        if len(Unit._unit_cache) < 1000:  # Limit cache size
            Unit._unit_cache[cache_key] = self
    
    def _parse_unit(self, unit_str: str) -> None:
        """Parse unit string into components."""
        # Simple parsing - handle basic units and compound units
        if '/' in unit_str:
            parts = unit_str.split('/')
            numerator = parts[0].strip()
            denominator = parts[1].strip()
            
            num_unit = Unit(numerator)
            den_unit = Unit(denominator)
            
            self._components = num_unit._components.copy()
            for unit, power in den_unit._components.items():
                self._components[unit] = self._components.get(unit, 0) - power
            self._name = unit_str
        elif '*' in unit_str or ' ' in unit_str:
            # Handle multiplication
            separator = '*' if '*' in unit_str else ' '
            parts = [p.strip() for p in unit_str.split(separator) if p.strip()]
            
            self._components: Dict[str, float] = {}
            for part in parts:
                unit = Unit(part)
                for u, p in unit._components.items():
                    self._components[u] = self._components.get(u, 0) + p
            self._name = unit_str
        else:
            # Single unit
            self._name = unit_str.strip()
            self._components = {self._name: 1.0}
    
    @property
    def dimensionality(self) -> Dimension:
        """Get the dimensionality of this unit."""
        # Build mapping if not done yet
        unit_to_base = self._build_unit_to_base_map()
        
        dim = Dimension()
        for unit, power in self._components.items():
            base_unit = unit_to_base.get(unit, unit)
            if base_unit in self._BASE_UNITS:
                base_dim = self._BASE_UNITS[base_unit]
                dim = dim + (base_dim * power)
        return dim
    
    def is_compatible_with(self, other: Unit) -> bool:
        """Check if this unit is compatible with another."""
        return self.dimensionality == other.dimensionality
    
    def conversion_factor_to(self, other: Unit) -> float:
        """Get conversion factor to another unit."""
        if not self.is_compatible_with(other):
            raise ValueError(f"Incompatible units: {self} and {other}")
        
        # Calculate conversion factor
        self_factor = 1.0
        for unit, power in self._components.items():
            self_factor *= self._CONVERSIONS.get(unit, 1.0) ** power
        
        other_factor = 1.0
        for unit, power in other._components.items():
            other_factor *= other._CONVERSIONS.get(unit, 1.0) ** power
        
        return self_factor / other_factor * self._scale / other._scale
    
    def to_base_units(self) -> Unit:
        """Convert to base SI units."""
        unit_to_base = self._build_unit_to_base_map()
        
        base_components: Dict[str, float] = {}
        for unit, power in self._components.items():
            base_unit = unit_to_base.get(unit, unit)
            base_components[base_unit] = base_components.get(base_unit, 0) + power
        
        # Build base unit string
        numerator = []
        denominator = []
        for unit, power in base_components.items():
            if power > 0:
                if power == 1:
                    numerator.append(unit)
                else:
                    numerator.append(f"{unit}^{power}")
            elif power < 0:
                if power == -1:
                    denominator.append(unit)
                else:
                    denominator.append(f"{unit}^{-power}")
        
        if not numerator and not denominator:
            return Unit("dimensionless")
        elif not denominator:
            return Unit(" * ".join(numerator))
        elif not numerator:
            return Unit("1 / " + " * ".join(denominator))
        else:
            return Unit(" * ".join(numerator) + " / " + " * ".join(denominator))
    
    def is_dimensionless(self) -> bool:
        """Check if unit is dimensionless."""
        return self.dimensionality == Dimension()
    
    def __mul__(self, other: Unit) -> Unit:
        """Multiply units."""
        new_components = self._components.copy()
        for unit, power in other._components.items():
            new_components[unit] = new_components.get(unit, 0) + power
        
        # Build new unit string
        parts = []
        for unit, power in new_components.items():
            if power != 0:
                if power == 1:
                    parts.append(unit)
                else:
                    parts.append(f"{unit}^{power}")
        
        unit_str = " * ".join(parts) if parts else "dimensionless"
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale * other._scale
        return result
    
    def __truediv__(self, other: Unit) -> Unit:
        """Divide units."""
        new_components = self._components.copy()
        for unit, power in other._components.items():
            new_components[unit] = new_components.get(unit, 0) - power
        
        # Build new unit string
        numerator = []
        denominator = []
        for unit, power in new_components.items():
            if power > 0:
                if power == 1:
                    numerator.append(unit)
                else:
                    numerator.append(f"{unit}^{power}")
            elif power < 0:
                if power == -1:
                    denominator.append(unit)
                else:
                    denominator.append(f"{unit}^{abs(power)}")
        
        if not numerator and not denominator:
            unit_str = "dimensionless"
        elif not denominator:
            unit_str = " * ".join(numerator)
        elif not numerator:
            unit_str = "1 / " + " * ".join(denominator)
        else:
            unit_str = " * ".join(numerator) + " / " + " * ".join(denominator)
        
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale / other._scale
        return result
    
    def __pow__(self, exponent: float) -> Unit:
        """Raise unit to a power."""
        new_components = {unit: power * exponent for unit, power in self._components.items()}
        
        parts = []
        for unit, power in new_components.items():
            if power == 1:
                parts.append(unit)
            else:
                parts.append(f"{unit}^{power}")
        
        unit_str = " * ".join(parts) if parts else "dimensionless"
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale ** exponent
        return result
    
    def __eq__(self, other: object) -> bool:
        """Check equality."""
        if not isinstance(other, Unit):
            return False
        return self._components == other._components
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Unit('{self._name}')"
    
    def __str__(self) -> str:
        """Human-readable string."""
        return self._name
