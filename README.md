# Demo Calculator Repository

A simple Python calculator demonstration project featuring basic arithmetic operations and logarithmic functions.

## Overview

This repository contains a basic calculator implementation in Python. It includes arithmetic operations and logarithmic functions for mathematical calculations.

## Project Structure

```
demo-calculator-repo/
├── README.md          # Project documentation
├── add.py            # Addition functions
├── divide.py         # Division functions
├── subtraction.py    # Subtraction functions
└── logarithm.py      # Logarithmic functions
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
from logarithm import natural_log, log_base_10, log_custom_base

# Use the addition function
result = addition(10, 5)
print(result)  # Output: 5

# Use logarithm functions
ln_result = natural_log(2.718)
log10_result = log_base_10(100)
custom_log_result = log_custom_base(8, 2)
```

### Running from Command Line

You can test the calculator functions directly:

```bash
python3 -c "from add import addition; print('Result:', addition(10, 3))"
python3 -c "from logarithm import natural_log; print('Natural log of 10:', natural_log(10))"
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
print(result)  # Output: 5
```

### `divide_numbers(a, b)`

Divides the first number by the second number.

**Parameters:**
- `a` (int/float): Dividend
- `b` (int/float): Divisor

**Returns:**
- The result of division or error message for division by zero

**Example:**
```python
result = divide_numbers(10, 2)
print(result)  # Output: 5.0
```

### `subtraction(*args)`

Subtracts multiple numbers from the first number.

**Parameters:**
- `*args`: Variable number of arguments (at least 2 required)

**Returns:**
- The result of subtraction

**Example:**
```python
result = subtraction(10, 3, 2)
print(result)  # Output: 5
```

### `natural_log(x)`

Calculates the natural logarithm (base e) of a number.

**Parameters:**
- `x` (int/float): The number to calculate the natural log of

**Returns:**
- The natural logarithm of x or error message for invalid input

**Example:**
```python
result = natural_log(10)
print(result)  # Output: 2.302585092994046
```

### `log_base_10(x)`

Calculates the base 10 logarithm of a number.

**Parameters:**
- `x` (int/float): The number to calculate the base 10 log of

**Returns:**
- The base 10 logarithm of x or error message for invalid input

**Example:**
```python
result = log_base_10(100)
print(result)  # Output: 2.0
```

### `log_custom_base(x, base)`

Calculates the logarithm of a number with a custom base.

**Parameters:**
- `x` (int/float): The number to calculate the log of
- `base` (int/float): The base for the logarithm

**Returns:**
- The logarithm of x with the specified base or error message for invalid input

**Example:**
```python
result = log_custom_base(8, 2)
print(result)  # Output: 3.0
```

## Contributing

This is a demonstration project. Feel free to fork and experiment with additional calculator functions.

## Purpose

This repository serves as a simple example of a Python calculator implementation with arithmetic and logarithmic operations, suitable for educational purposes and mathematical calculations.
