# src/factorial.py

# TODO: Implement factorial function recursively
# Must raise ValueError for negative numbers
# Must raise ValueError for negative numbers
# To calculate the factorial of a number, multiply that number by every positive integer less than it, down to 1. 
# For example, 4 factorial (written as 4!) is calculated as 4 x 3 x 2 x 1, which equals 24. 
# The general formula is n! = n × (n-1) × (n-2) × ... × 1.  


def factorial(n):
    if n < 0:
        raise ValueError
    results = 1
    for i in range(1,n+1):
        results = results * i
    return results

print(factorial(5))

