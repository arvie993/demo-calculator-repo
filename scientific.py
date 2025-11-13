import math

# Trigonometric functions
def sin(x):
    """Calculate the sine of x (x in radians)"""
    return math.sin(x)

def cos(x):
    """Calculate the cosine of x (x in radians)"""
    return math.cos(x)

def tan(x):
    """Calculate the tangent of x (x in radians)"""
    return math.tan(x)

def asin(x):
    """Calculate the arc sine of x (result in radians)"""
    return math.asin(x)

def acos(x):
    """Calculate the arc cosine of x (result in radians)"""
    return math.acos(x)

def atan(x):
    """Calculate the arc tangent of x (result in radians)"""
    return math.atan(x)

# Logarithmic functions
def log(x, base=math.e):
    """Calculate the logarithm of x to the given base (default is natural log)"""
    return math.log(x, base)

def log10(x):
    """Calculate the base-10 logarithm of x"""
    return math.log10(x)

def log2(x):
    """Calculate the base-2 logarithm of x"""
    return math.log2(x)

# Exponential functions
def exp(x):
    """Calculate e raised to the power of x"""
    return math.exp(x)

def power(x, y):
    """Calculate x raised to the power of y"""
    return math.pow(x, y)

# Square root function
def sqrt(x):
    """Calculate the square root of x"""
    return math.sqrt(x)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Scientific Calculator - Logarithmic Functions")
        print("Usage:")
        print("  python scientific.py log <number> [base]     # Natural log or log with base")
        print("  python scientific.py log10 <number>          # Base-10 logarithm")
        print("  python scientific.py log2 <number>           # Base-2 logarithm")
        print("  python scientific.py exp <number>            # e^x")
        print("  python scientific.py sqrt <number>           # Square root")
        print("  python scientific.py power <x> <y>           # x^y")
        print("\nExamples:")
        print("  python scientific.py log 2.718281828459045   # Natural log of e = 1.0")
        print("  python scientific.py log 8 2                 # log base 2 of 8 = 3.0")
        print("  python scientific.py log10 100               # log10(100) = 2.0")
        print("  python scientific.py log2 8                  # log2(8) = 3.0")
        sys.exit(1)

    operation = sys.argv[1].lower()

    try:
        if operation == "log":
            if len(sys.argv) < 3:
                print("Error: 'log' requires at least one number")
                sys.exit(1)
            x = float(sys.argv[2])
            if len(sys.argv) == 4:
                base = float(sys.argv[3])
                result = log(x, base)
            else:
                result = log(x)
            print(result)

        elif operation == "log10":
            if len(sys.argv) != 3:
                print("Error: 'log10' requires exactly one number")
                sys.exit(1)
            x = float(sys.argv[2])
            result = log10(x)
            print(result)

        elif operation == "log2":
            if len(sys.argv) != 3:
                print("Error: 'log2' requires exactly one number")
                sys.exit(1)
            x = float(sys.argv[2])
            result = log2(x)
            print(result)

        elif operation == "exp":
            if len(sys.argv) != 3:
                print("Error: 'exp' requires exactly one number")
                sys.exit(1)
            x = float(sys.argv[2])
            result = exp(x)
            print(result)

        elif operation == "sqrt":
            if len(sys.argv) != 3:
                print("Error: 'sqrt' requires exactly one number")
                sys.exit(1)
            x = float(sys.argv[2])
            result = sqrt(x)
            print(result)

        elif operation == "power":
            if len(sys.argv) != 4:
                print("Error: 'power' requires exactly two numbers")
                sys.exit(1)
            x = float(sys.argv[2])
            y = float(sys.argv[3])
            result = power(x, y)
            print(result)

        else:
            print(f"Error: Unknown operation '{operation}'")
            print("Run 'python scientific.py' without arguments to see available operations")
            sys.exit(1)

    except ValueError as e:
        error_msg = str(e)
        if "could not convert" in error_msg:
            print("Error: Invalid number format. Please provide valid numeric arguments.")
        elif "math domain error" in error_msg:
            print("Error: Invalid mathematical operation (e.g., log of negative number or zero).")
        else:
            print(f"Error: {e}")
        sys.exit(1)
    except TypeError as e:
        print(f"Error: {e}")
        sys.exit(1)