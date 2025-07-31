def subtraction(*args):
    if len(args) < 2:
        raise ValueError("At least 2 numbers are required for subtraction")
    
    result = args[0]
    for num in args[1:]:
        result -= num
    
    return result