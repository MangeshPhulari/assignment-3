#Task 1: Calculate Factorial Using a Function 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
number = int(input("Enter a number: ")) 

print(f"The factorial of {number} is {factorial(number)}.")

#Task 2: Using the Math Module for Calculations

import math

number = int(input("Enter a number: "))

print(f"Square root: {math.sqrt(number)}")
print(f"Logarithm: {math.log(number)}")
print(f"Sine: {math.sin(number)}")








