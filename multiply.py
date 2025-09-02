def multiply_numbers(a, b):
    """Multiply two numbers and return the product."""
    return a * b


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python multiply.py <a> <b>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Error: Both <a> and <b> must be numbers.")
        sys.exit(1)

    result = multiply_numbers(a, b)
    # If both inputs look like integers, show an int result for cleanliness
    if a.is_integer() and b.is_integer():
        result = int(result)
    print(result)
