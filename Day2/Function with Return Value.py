def multiply(a,b) :
    return a * b
result = multiply(5, 6)
print("Result :", result)

# Practice:

# 1. Create a function to calculate square of a number.

def calculateSq(number) :
    return number * number

result = calculateSq(5)
print("Square is ", result)

# 2. Create a function to calculate factorial of a number.


def factorial(number) :
    result = 1
    for i in range(1,number +1) :
        result *= i
    return result
num = int(input("Enter The Number "))
print("Factorial of", num, "is", factorial(num))