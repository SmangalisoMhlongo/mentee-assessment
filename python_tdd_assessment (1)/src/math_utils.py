# src/math_utils.py

# TODO: Implement the following functions with basic math operations.
# Each should handle invalid input gracefully.

def add(a, b):
    # TODO: Return the sum of a and b
    ints = [1,2,3,4,5,6,7,8,9,0]

    try:
        if a not in ints or b not in ints:
            raise ValueError
        else:
            total = a + b
            return int(total)
        
    except ValueError:
        print("Enter a integer.")
            


def subtract(a, b):
    # TODO: Return the difference between a and b
    ints = [1,2,3,4,5,6,7,8,9,0]
    try:
        if a not in ints or b not in ints:
            raise ValueError
        else:
            total = a - b
            return int(total)
        
    except ValueError:
        print("Enter a integer.")

def multiply(a, b):
    # TODO: Return the product of a and b
    total = a * b
    return int(total)

def divide(a, b):
    # TODO: Return the quotient of a / b, handle division by zero with ValueError
    if b == 0:
        raise ValueError
    
    total = a/b
    return int(total)


