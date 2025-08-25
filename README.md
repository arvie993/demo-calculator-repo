# Demo Calculator Repository

A simple Python calculator demonstration project featuring basic arithmetic and scientific operations.

*This project demonstrates Python calculator functionality with comprehensive documentation.*

## Overview

This repository contains a basic calculator implementation in Python. It includes basic arithmetic operations and advanced scientific functions for trigonometry, logarithms, exponentials, and square roots.

## Project Structure

```
demo-calculator-repo/
├── README.md          # Project documentation
├── add.py            # Addition function
├── divide.py         # Division function
├── subtraction.py    # Subtraction function
└── scientific.py     # Scientific functions
```

## Installation

No special installation is required. This project uses standard Python and doesn't require any external dependencies.

### Prerequisites

- Python 3.x installed on your system

## Usage

### Importing the Calculator Functions

To use the calculator functions in your Python code:

```python
from add import addition
from divide import divide_numbers
from subtraction import subtraction
from scientific import sin, cos, tan, log, exp, sqrt

# Use the addition function
result = addition(10, 5)
print(result)  # Output: 15

# Use scientific functions
print(sin(3.14159/2))  # Output: 1.0
print(sqrt(16))        # Output: 4.0
print(log(2.718281828459045))  # Output: 1.0
```

### Running from Command Line

You can test the calculator functions directly:

```bash
python3 -c "from add import addition; print('Result:', addition(10, 3))"
```

## Available Functions

### `addition(a, b)`

Performs a mathematical operation between two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:**
- The result of the mathematical operation

**Example:**
```python
result = addition(8, 3)
print(result)  # Output: 11
```

### `divide_numbers(a, b)`

Divides the first number by the second number.

**Parameters:**
- `a` (int/float): Dividend
- `b` (int/float): Divisor

**Returns:**
- The result of division or error message if dividing by zero

**Example:**
```python
result = divide_numbers(10, 2)
print(result)  # Output: 5.0
```

### `subtraction(*args)`

Subtracts multiple numbers from the first number.

**Parameters:**
- `*args` (int/float): Numbers to subtract (at least 2 required)

**Returns:**
- The result of subtraction

**Example:**
```python
result = subtraction(10, 3, 2)
print(result)  # Output: 5
```

### Scientific Functions

The `scientific.py` module provides advanced mathematical functions:

#### Trigonometric Functions
- `sin(x)` - Sine of x (x in radians)
- `cos(x)` - Cosine of x (x in radians) 
- `tan(x)` - Tangent of x (x in radians)
- `asin(x)` - Arc sine of x (result in radians)
- `acos(x)` - Arc cosine of x (result in radians)
- `atan(x)` - Arc tangent of x (result in radians)

#### Logarithmic Functions
- `log(x, base=e)` - Logarithm of x to given base (default natural log)
- `log10(x)` - Base-10 logarithm of x
- `log2(x)` - Base-2 logarithm of x

#### Exponential Functions
- `exp(x)` - e raised to the power of x
- `power(x, y)` - x raised to the power of y

#### Square Root Function
- `sqrt(x)` - Square root of x

**Examples:**
```python
from scientific import sin, cos, log, exp, sqrt
import math

print(sin(math.pi/2))  # Output: 1.0
print(cos(0))          # Output: 1.0
print(log10(100))      # Output: 2.0
print(exp(1))          # Output: 2.718281828459045
print(sqrt(16))        # Output: 4.0
```

## Contributing

This is a demonstration project. Feel free to fork and experiment with additional calculator functions.

## Purpose

This repository serves as a simple example of a Python calculator implementation, suitable for educational purposes and basic arithmetic operations.
