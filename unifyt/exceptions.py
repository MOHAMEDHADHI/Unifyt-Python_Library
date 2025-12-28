"""Custom exceptions for Unifyt library.

This module provides a comprehensive exception hierarchy for the Unifyt library,
allowing users to catch specific errors or broad categories of errors.

Exception Hierarchy:
    UnifytException (base)
    ├── UnitError
    │   ├── DimensionalityError
    │   ├── UnitNotFoundError
    │   ├── UnitParseError
    │   └── ConversionError
    ├── QuantityError
    │   ├── InvalidValueError
    │   ├── OperationError
    │   ├── ComparisonError
    │   ├── ArrayError
    │   └── OverflowError
    ├── RegistryError
    │   ├── UnitDefinitionError
    │   └── UnitAlreadyExistsError
    ├── SerializationError
    │   ├── SerializationFormatError
    │   └── DeserializationError
    ├── ContextError
    │   └── InvalidUnitSystemError
    ├── ConstantError
    └── UtilityError

Usage:
    >>> from unifyt import Quantity
    >>> from unifyt.exceptions import ConversionError, UnitError
    >>> 
    >>> try:
    ...     q = Quantity(100, 'meter')
    ...     q.to('second')  # Invalid conversion
    ... except ConversionError as e:
    ...     print(f"Conversion failed: {e}")
    ... except UnitError as e:
    ...     print(f"Unit error: {e}")
"""

from typing import Any, List, Optional


class UnifytException(Exception):
    """Base exception for all Unifyt errors.
    
    All custom exceptions in Unifyt inherit from this class,
    allowing users to catch all library-specific errors with a single except clause.
    
    Attributes:
        message: Human-readable error message
    """
    
    def __init__(self, message: str):
        """Initialize exception with message.
        
        Args:
            message: Error message describing what went wrong
        """
        self.message = message
        super().__init__(self.message)
    
    def __repr__(self) -> str:
        """Return detailed representation of the exception."""
        return f"{self.__class__.__name__}('{self.message}')"


class UnitError(UnifytException):
    """Base exception for unit-related errors.
    
    This includes parsing errors, conversion errors, and dimensionality mismatches.
    """
    pass


class DimensionalityError(UnitError):
    """Raised when operations involve incompatible dimensions.
    
    This occurs when trying to add meters to seconds, compare kilograms with joules, etc.
    
    Attributes:
        unit1: First unit involved in the operation
        unit2: Second unit involved in the operation
        operation: The operation that was attempted
    
    Examples:
        >>> from unifyt import Quantity
        >>> distance = Quantity(100, 'meter')
        >>> time = Quantity(10, 'second')
        >>> distance + time  # Raises DimensionalityError
    """
    
    def __init__(self, unit1: str, unit2: str, operation: str = "operation"):
        """Initialize dimensionality error.
        
        Args:
            unit1: First unit
            unit2: Second unit
            operation: Operation being attempted (e.g., 'addition', 'comparison')
        """
        message = (
            f"Cannot perform {operation} with incompatible dimensions: "
            f"'{unit1}' and '{unit2}'"
        )
        super().__init__(message)
        self.unit1 = unit1
        self.unit2 = unit2
        self.operation = operation


class UnitNotFoundError(UnitError):
    """Raised when a unit is not recognized.
    
    This can occur when using a typo or an unsupported unit name.
    
    Attributes:
        unit_name: The unit that was not found
        suggestions: List of similar unit names that might have been intended
    
    Examples:
        >>> from unifyt import Quantity
        >>> q = Quantity(100, 'metrs')  # Typo - raises UnitNotFoundError
    """
    
    def __init__(self, unit_name: str, suggestions: Optional[List[str]] = None):
        """Initialize unit not found error.
        
        Args:
            unit_name: The unit that was not found
            suggestions: List of similar unit names (for helpful error messages)
        """
        message = f"Unit '{unit_name}' not recognized."
        if suggestions:
            message += f" Did you mean: {', '.join(suggestions)}?"
        super().__init__(message)
        self.unit_name = unit_name
        self.suggestions = suggestions or []


class UnitParseError(UnitError):
    """Raised when a unit string cannot be parsed.
    
    This occurs when the unit string has invalid syntax or structure.
    
    Attributes:
        unit_string: The string that failed to parse
        reason: Optional reason for the parsing failure
        position: Optional position in the string where parsing failed
    
    Examples:
        >>> from unifyt import Unit
        >>> u = Unit('meter//second')  # Invalid syntax - raises UnitParseError
    """
    
    def __init__(self, unit_string: str, reason: Optional[str] = None, position: Optional[int] = None):
        """Initialize unit parse error.
        
        Args:
            unit_string: The string that failed to parse
            reason: Optional reason for failure
            position: Optional character position where parsing failed
        """
        message = f"Cannot parse unit string: '{unit_string}'"
        if position is not None:
            message += f" at position {position}"
        if reason:
            message += f". Reason: {reason}"
        super().__init__(message)
        self.unit_string = unit_string
        self.reason = reason
        self.position = position


class ConversionError(UnitError):
    """Raised when unit conversion fails.
    
    This typically occurs when trying to convert between incompatible units.
    
    Attributes:
        from_unit: Source unit
        to_unit: Target unit
        reason: Optional reason for the conversion failure
    
    Examples:
        >>> from unifyt import Quantity
        >>> distance = Quantity(100, 'meter')
        >>> distance.to('second')  # Raises ConversionError
    """
    
    def __init__(self, from_unit: str, to_unit: str, reason: Optional[str] = None):
        """Initialize conversion error.
        
        Args:
            from_unit: Source unit
            to_unit: Target unit
            reason: Optional reason for failure
        """
        message = f"Cannot convert from '{from_unit}' to '{to_unit}'"
        if reason:
            message += f": {reason}"
        else:
            message += ". Units have incompatible dimensions."
        super().__init__(message)
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.reason = reason


class QuantityError(UnifytException):
    """Base exception for quantity-related errors.
    
    This includes invalid values, failed operations, and comparison errors.
    """
    pass


class InvalidValueError(QuantityError):
    """Raised when a quantity value is invalid.
    
    This can occur with NaN, infinity, or values outside valid ranges.
    
    Attributes:
        value: The invalid value
        reason: Optional reason for invalidity
        constraint: Optional constraint that was violated
    
    Examples:
        >>> from unifyt import Quantity
        >>> import numpy as np
        >>> q = Quantity(np.nan, 'meter')  # May raise InvalidValueError
    """
    
    def __init__(self, value: Any, reason: Optional[str] = None, constraint: Optional[str] = None):
        """Initialize invalid value error.
        
        Args:
            value: The invalid value
            reason: Optional reason for invalidity
            constraint: Optional constraint that was violated (e.g., 'must be positive')
        """
        message = f"Invalid value: {value}"
        if constraint:
            message += f" ({constraint})"
        if reason:
            message += f". Reason: {reason}"
        super().__init__(message)
        self.value = value
        self.reason = reason
        self.constraint = constraint


class OperationError(QuantityError):
    """Raised when an operation cannot be performed.
    
    This includes arithmetic operations on incompatible quantities.
    
    Attributes:
        operation: The operation being attempted
        operand1: First operand
        operand2: Second operand
        reason: Optional reason for failure
    
    Examples:
        >>> from unifyt import Quantity
        >>> distance = Quantity(100, 'meter')
        >>> distance + 50  # Raises OperationError (can't add scalar to dimensioned quantity)
    """
    
    def __init__(self, operation: str, operand1: Any, operand2: Any, reason: Optional[str] = None):
        """Initialize operation error.
        
        Args:
            operation: The operation being attempted (e.g., 'addition', 'multiplication')
            operand1: First operand
            operand2: Second operand
            reason: Optional reason for failure
        """
        message = f"Cannot perform {operation} on {operand1} and {operand2}"
        if reason:
            message += f": {reason}"
        super().__init__(message)
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.reason = reason


class ComparisonError(QuantityError):
    """Raised when quantities cannot be compared.
    
    This occurs when comparing quantities with incompatible dimensions or types.
    
    Attributes:
        quantity1: First quantity
        quantity2: Second quantity
        reason: Optional reason for failure
    
    Examples:
        >>> from unifyt import Quantity
        >>> distance = Quantity(100, 'meter')
        >>> time = Quantity(10, 'second')
        >>> distance < time  # Raises ComparisonError
    """
    
    def __init__(self, quantity1: Any, quantity2: Any, reason: Optional[str] = None):
        """Initialize comparison error.
        
        Args:
            quantity1: First quantity
            quantity2: Second quantity
            reason: Optional reason for failure
        """
        message = f"Cannot compare {quantity1} with {quantity2}"
        if reason:
            message += f": {reason}"
        super().__init__(message)
        self.quantity1 = quantity1
        self.quantity2 = quantity2
        self.reason = reason


class ArrayError(QuantityError):
    """Raised when array operations fail.
    
    This includes concatenation, stacking, and reshaping errors.
    
    Attributes:
        operation: The array operation that failed
        reason: Optional reason for failure
        shape_info: Optional information about array shapes
    
    Examples:
        >>> from unifyt import Quantity, utils
        >>> q1 = Quantity([1, 2], 'meter')
        >>> q2 = Quantity([3, 4, 5], 'second')
        >>> utils.concatenate([q1, q2])  # Raises ArrayError (incompatible units)
    """
    
    def __init__(self, operation: str, reason: Optional[str] = None, shape_info: Optional[str] = None):
        """Initialize array error.
        
        Args:
            operation: The array operation that failed
            reason: Optional reason for failure
            shape_info: Optional information about array shapes
        """
        message = f"Array operation '{operation}' failed"
        if shape_info:
            message += f" (shapes: {shape_info})"
        if reason:
            message += f": {reason}"
        super().__init__(message)
        self.operation = operation
        self.reason = reason
        self.shape_info = shape_info


class QuantityOverflowError(QuantityError):
    """Raised when a quantity operation results in overflow.
    
    This occurs when calculations produce values too large to represent.
    
    Attributes:
        operation: The operation that caused overflow
        operands: The operands involved
    
    Examples:
        >>> from unifyt import Quantity
        >>> import sys
        >>> huge = Quantity(sys.float_info.max, 'meter')
        >>> huge * huge  # May raise QuantityOverflowError
    """
    
    def __init__(self, operation: str, operands: Optional[List[Any]] = None):
        """Initialize quantity overflow error.
        
        Args:
            operation: The operation that caused overflow
            operands: Optional list of operands involved
        """
        message = f"Overflow in {operation}"
        if operands:
            message += f" with operands: {operands}"
        super().__init__(message)
        self.operation = operation
        self.operands = operands or []


class RegistryError(UnifytException):
    """Base exception for unit registry errors.
    
    This includes errors when defining, modifying, or accessing custom units.
    """
    pass


class UnitDefinitionError(RegistryError):
    """Raised when a unit definition is invalid.
    
    This occurs when trying to define a unit with invalid syntax or circular dependencies.
    
    Attributes:
        unit_name: Name of the unit being defined
        definition: The invalid definition
        reason: Optional reason for failure
    
    Examples:
        >>> from unifyt import UnitRegistry
        >>> registry = UnitRegistry()
        >>> registry.define('bad_unit', 'invalid syntax')  # Raises UnitDefinitionError
    """
    
    def __init__(self, unit_name: str, definition: str, reason: Optional[str] = None):
        """Initialize unit definition error.
        
        Args:
            unit_name: Name of the unit being defined
            definition: The invalid definition
            reason: Optional reason for failure
        """
        message = f"Invalid unit definition for '{unit_name}': '{definition}'"
        if reason:
            message += f". Reason: {reason}"
        super().__init__(message)
        self.unit_name = unit_name
        self.definition = definition
        self.reason = reason


class UnitAlreadyExistsError(RegistryError):
    """Raised when trying to define a unit that already exists.
    
    This prevents accidental overwriting of existing unit definitions.
    
    Attributes:
        unit_name: Name of the existing unit
    
    Examples:
        >>> from unifyt import UnitRegistry
        >>> registry = UnitRegistry()
        >>> registry.define('my_unit', 'meter')
        >>> registry.define('my_unit', 'kilometer')  # Raises UnitAlreadyExistsError
    """
    
    def __init__(self, unit_name: str):
        """Initialize unit already exists error.
        
        Args:
            unit_name: Name of the existing unit
        """
        message = (
            f"Unit '{unit_name}' already exists. "
            f"Use a different name or remove the existing unit first."
        )
        super().__init__(message)
        self.unit_name = unit_name


class UnitSystemError(RegistryError):
    """Raised when there are issues with unit system definitions.
    
    This occurs when a unit system is misconfigured or has conflicts.
    
    Attributes:
        system_name: Name of the unit system
        reason: Reason for the error
    
    Examples:
        >>> from unifyt import UnitRegistry
        >>> registry = UnitRegistry()
        >>> registry.add_system('bad_system', {})  # May raise UnitSystemError
    """
    
    def __init__(self, system_name: str, reason: str):
        """Initialize unit system error.
        
        Args:
            system_name: Name of the unit system
            reason: Reason for the error
        """
        message = f"Unit system '{system_name}' error: {reason}"
        super().__init__(message)
        self.system_name = system_name
        self.reason = reason


class SerializationError(UnifytException):
    """Base exception for serialization errors.
    
    This includes errors during saving, loading, and format conversion.
    """
    pass


class SerializationFormatError(SerializationError):
    """Raised when serialization format is not supported.
    
    This occurs when trying to use an unsupported file format.
    
    Attributes:
        format_name: The unsupported format
        supported_formats: List of supported formats
    
    Examples:
        >>> from unifyt import Quantity
        >>> from unifyt.serialization import save_quantity
        >>> q = Quantity(100, 'meter')
        >>> save_quantity(q, 'data.xml', format='xml')  # Raises SerializationFormatError
    """
    
    def __init__(self, format_name: str, supported_formats: Optional[List[str]] = None):
        """Initialize serialization format error.
        
        Args:
            format_name: The unsupported format
            supported_formats: List of supported formats
        """
        message = f"Unsupported serialization format: '{format_name}'"
        if supported_formats:
            message += f". Supported formats: {', '.join(supported_formats)}"
        super().__init__(message)
        self.format_name = format_name
        self.supported_formats = supported_formats or []


class DeserializationError(SerializationError):
    """Raised when deserialization fails.
    
    This occurs when loading data from a file or string fails.
    
    Attributes:
        data: The data that failed to deserialize (or filename)
        reason: Optional reason for failure
        format_hint: Optional hint about expected format
    
    Examples:
        >>> from unifyt.serialization import load_quantity
        >>> q = load_quantity('corrupted.json')  # Raises DeserializationError
    """
    
    def __init__(self, data: Any, reason: Optional[str] = None, format_hint: Optional[str] = None):
        """Initialize deserialization error.
        
        Args:
            data: The data that failed to deserialize
            reason: Optional reason for failure
            format_hint: Optional hint about expected format
        """
        message = "Failed to deserialize data"
        if format_hint:
            message += f" (expected format: {format_hint})"
        if reason:
            message += f": {reason}"
        super().__init__(message)
        self.data = data
        self.reason = reason
        self.format_hint = format_hint


class SerializationVersionError(SerializationError):
    """Raised when serialized data version is incompatible.
    
    This occurs when loading data saved with a different library version.
    
    Attributes:
        data_version: Version of the serialized data
        library_version: Current library version
    
    Examples:
        >>> from unifyt.serialization import load_quantity
        >>> q = load_quantity('old_format.json')  # May raise SerializationVersionError
    """
    
    def __init__(self, data_version: str, library_version: str):
        """Initialize serialization version error.
        
        Args:
            data_version: Version of the serialized data
            library_version: Current library version
        """
        message = (
            f"Incompatible data version: {data_version} "
            f"(library version: {library_version})"
        )
        super().__init__(message)
        self.data_version = data_version
        self.library_version = library_version


class ContextError(UnifytException):
    """Base exception for context-related errors.
    
    This includes errors with unit system contexts and preferences.
    """
    pass


class InvalidUnitSystemError(ContextError):
    """Raised when an invalid unit system is specified.
    
    This occurs when trying to use a unit system that doesn't exist.
    
    Attributes:
        system_name: The invalid system name
        available_systems: List of available systems
    
    Examples:
        >>> from unifyt import UnitContext
        >>> with UnitContext('invalid_system'):  # Raises InvalidUnitSystemError
        ...     pass
    """
    
    def __init__(self, system_name: str, available_systems: Optional[List[str]] = None):
        """Initialize invalid unit system error.
        
        Args:
            system_name: The invalid system name
            available_systems: List of available systems
        """
        message = f"Invalid unit system: '{system_name}'"
        if available_systems:
            message += f". Available systems: {', '.join(available_systems)}"
        super().__init__(message)
        self.system_name = system_name
        self.available_systems = available_systems or []


class ContextStateError(ContextError):
    """Raised when context state is invalid.
    
    This occurs when trying to exit a context that wasn't entered.
    
    Attributes:
        reason: Reason for the state error
    
    Examples:
        >>> from unifyt import UnitContext
        >>> ctx = UnitContext('SI')
        >>> ctx.__exit__(None, None, None)  # May raise ContextStateError
    """
    
    def __init__(self, reason: str):
        """Initialize context state error.
        
        Args:
            reason: Reason for the state error
        """
        message = f"Invalid context state: {reason}"
        super().__init__(message)
        self.reason = reason


class ConstantError(UnifytException):
    """Raised when accessing constants fails.
    
    This occurs when requesting a constant that doesn't exist.
    
    Attributes:
        constant_name: Name of the constant
        available_constants: List of available constants
    
    Examples:
        >>> from unifyt import constants
        >>> c = constants.get_constant('invalid_constant')  # Raises ConstantError
    """
    
    def __init__(self, constant_name: str, available_constants: Optional[List[str]] = None):
        """Initialize constant error.
        
        Args:
            constant_name: Name of the constant
            available_constants: List of available constants
        """
        message = f"Constant '{constant_name}' not found"
        if available_constants:
            # Show first 10 constants to avoid overwhelming error messages
            shown = available_constants[:10]
            message += f". Available constants: {', '.join(shown)}"
            if len(available_constants) > 10:
                message += f" and {len(available_constants) - 10} more"
        super().__init__(message)
        self.constant_name = constant_name
        self.available_constants = available_constants or []


class UtilityError(UnifytException):
    """Raised when utility functions fail.
    
    This is a general error for utility function failures.
    
    Attributes:
        function_name: Name of the utility function
        reason: Reason for failure
    
    Examples:
        >>> from unifyt import utils
        >>> utils.some_utility([])  # May raise UtilityError
    """
    
    def __init__(self, function_name: str, reason: str):
        """Initialize utility error.
        
        Args:
            function_name: Name of the utility function
            reason: Reason for failure
        """
        message = f"Utility function '{function_name}' failed: {reason}"
        super().__init__(message)
        self.function_name = function_name
        self.reason = reason


class ValidationError(UnifytException):
    """Raised when validation fails.
    
    This occurs when input validation fails for any operation.
    
    Attributes:
        parameter: Name of the parameter that failed validation
        value: The invalid value
        constraint: The constraint that was violated
    
    Examples:
        >>> from unifyt import Quantity
        >>> q = Quantity(-1, 'meter')
        >>> # Some operation requiring positive values
        >>> # May raise ValidationError
    """
    
    def __init__(self, parameter: str, value: Any, constraint: str):
        """Initialize validation error.
        
        Args:
            parameter: Name of the parameter that failed validation
            value: The invalid value
            constraint: The constraint that was violated
        """
        message = f"Validation failed for parameter '{parameter}': {constraint} (got: {value})"
        super().__init__(message)
        self.parameter = parameter
        self.value = value
        self.constraint = constraint


class PrecisionError(UnifytException):
    """Raised when precision or rounding issues occur.
    
    This occurs when operations result in significant precision loss.
    
    Attributes:
        operation: The operation that caused precision issues
        precision_loss: Estimated precision loss
    
    Examples:
        >>> from unifyt import Quantity
        >>> # Very large and very small numbers
        >>> huge = Quantity(1e308, 'meter')
        >>> tiny = Quantity(1e-308, 'meter')
        >>> huge + tiny  # May raise PrecisionError
    """
    
    def __init__(self, operation: str, precision_loss: Optional[float] = None):
        """Initialize precision error.
        
        Args:
            operation: The operation that caused precision issues
            precision_loss: Optional estimated precision loss
        """
        message = f"Precision error in {operation}"
        if precision_loss is not None:
            message += f" (estimated loss: {precision_loss:.2e})"
        super().__init__(message)
        self.operation = operation
        self.precision_loss = precision_loss


class ConfigurationError(UnifytException):
    """Raised when configuration is invalid.
    
    This occurs when library configuration settings are invalid.
    
    Attributes:
        setting: Name of the configuration setting
        value: The invalid value
        reason: Reason for invalidity
    
    Examples:
        >>> from unifyt import configure
        >>> configure(invalid_setting='value')  # May raise ConfigurationError
    """
    
    def __init__(self, setting: str, value: Any, reason: str):
        """Initialize configuration error.
        
        Args:
            setting: Name of the configuration setting
            value: The invalid value
            reason: Reason for invalidity
        """
        message = f"Invalid configuration for '{setting}': {reason} (value: {value})"
        super().__init__(message)
        self.setting = setting
        self.value = value
        self.reason = reason


# Exception hierarchy for easy catching and comprehensive error handling
__all__ = [
    # Base exception
    'UnifytException',
    
    # Unit errors
    'UnitError',
    'DimensionalityError',
    'UnitNotFoundError',
    'UnitParseError',
    'ConversionError',
    
    # Quantity errors
    'QuantityError',
    'InvalidValueError',
    'OperationError',
    'ComparisonError',
    'ArrayError',
    'QuantityOverflowError',
    
    # Registry errors
    'RegistryError',
    'UnitDefinitionError',
    'UnitAlreadyExistsError',
    'UnitSystemError',
    
    # Serialization errors
    'SerializationError',
    'SerializationFormatError',
    'DeserializationError',
    'SerializationVersionError',
    
    # Context errors
    'ContextError',
    'InvalidUnitSystemError',
    'ContextStateError',
    
    # Other errors
    'ConstantError',
    'UtilityError',
    'ValidationError',
    'PrecisionError',
    'ConfigurationError',
]


# Convenience function for creating custom exceptions
def create_exception(
    exception_class: type,
    message: str,
    **kwargs
) -> UnifytException:
    """Create a custom exception with additional context.
    
    This is a helper function for creating exceptions with custom attributes.
    
    Args:
        exception_class: The exception class to instantiate
        message: Error message
        **kwargs: Additional attributes to set on the exception
    
    Returns:
        An instance of the specified exception class
    
    Examples:
        >>> exc = create_exception(
        ...     UnitError,
        ...     "Custom error",
        ...     custom_attr="value"
        ... )
    """
    exc = exception_class(message)
    for key, value in kwargs.items():
        setattr(exc, key, value)
    return exc


# Error context manager for better error messages
class ErrorContext:
    """Context manager for adding context to exceptions.
    
    This allows wrapping code blocks and adding additional context
    to any exceptions that occur.
    
    Examples:
        >>> from unifyt import Quantity
        >>> from unifyt.exceptions import ErrorContext
        >>> 
        >>> with ErrorContext("calculating velocity"):
        ...     distance = Quantity(100, 'meter')
        ...     time = Quantity(10, 'second')
        ...     velocity = distance / time
    """
    
    def __init__(self, context: str):
        """Initialize error context.
        
        Args:
            context: Description of what's being done
        """
        self.context = context
    
    def __enter__(self):
        """Enter the context."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context and enhance any exceptions.
        
        Args:
            exc_type: Exception type
            exc_val: Exception value
            exc_tb: Exception traceback
        
        Returns:
            False to propagate the exception
        """
        if exc_type is not None and issubclass(exc_type, UnifytException):
            # Add context to the exception message
            if hasattr(exc_val, 'message'):
                exc_val.message = f"{exc_val.message} (context: {self.context})"
                exc_val.args = (exc_val.message,)
        return False  # Don't suppress the exception

