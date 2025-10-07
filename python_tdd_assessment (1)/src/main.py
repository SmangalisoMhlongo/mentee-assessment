# Implement the following functions so all tests pass

def add_numbers(a, b):
    total = a + b
    return total

def is_even(num):
    if num%2 == 0:
        return True
    else: 
        return False
    

def reverse_string(text):
    re_text = text[::-1]
    return re_text


def factorial(n):
    """
    Return the factorial of n using recursion or a loop.
    Raise ValueError if n is negative.
    """
    if n < 0:
        raise ValueError
    results = 1
    for i in range(1,n+1):
        results = results * i
    return results

def calculate_discount(price, percentage):
    """
    Returns the discounted price (price - percentage%)
    Raise ValueError for negatives
    Cap discount at 90%
    """
    if price < 0 or percentage < 0:
        raise ValueError
    if percentage > 90 :
        percentage = 90

    proper_disc = ((price * percentage)/100) 
    discount = (price - proper_disc) 
    return discount

print(calculate_discount(100,95))
