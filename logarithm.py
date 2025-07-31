import math

def natural_log(x):
    """
    Calculate the natural logarithm (base e) of a number.
    
    Args:
        x (int/float): The number to calculate the natural log of
        
    Returns:
        float: The natural logarithm of x
        str: Error message if input is invalid
    """
    try:
        if x <= 0:
            return "Error: Cannot calculate log of zero or negative number."
        return math.log(x)
    except (TypeError, ValueError):
        return "Error: Invalid input type."

def log_base_10(x):
    """
    Calculate the base 10 logarithm of a number.
    
    Args:
        x (int/float): The number to calculate the base 10 log of
        
    Returns:
        float: The base 10 logarithm of x
        str: Error message if input is invalid
    """
    try:
        if x <= 0:
            return "Error: Cannot calculate log of zero or negative number."
        return math.log10(x)
    except (TypeError, ValueError):
        return "Error: Invalid input type."

def log_custom_base(x, base):
    """
    Calculate the logarithm of a number with a custom base.
    
    Args:
        x (int/float): The number to calculate the log of
        base (int/float): The base for the logarithm
        
    Returns:
        float: The logarithm of x with the specified base
        str: Error message if input is invalid
    """
    try:
        if x <= 0:
            return "Error: Cannot calculate log of zero or negative number."
        if base <= 0 or base == 1:
            return "Error: Base must be positive and not equal to 1."
        return math.log(x, base)
    except (TypeError, ValueError):
        return "Error: Invalid input type."