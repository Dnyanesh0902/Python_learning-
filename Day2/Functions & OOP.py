#Functions
# A function is a reusable block of code that performs a specific task.

def greet(name):
    print("Hello", name)
greet("Dnyanesh")

#Practice:

# 1. Write a function add_numbers(a, b) that returns the sum of two numbers.
def add_number(a, b):
    return a + b

result = add_number(10,16)
print(result)
 
# 2. Write a function is_even(number) that prints if a number is even or odd.

def is_even(number) :
    if number % 2 == 0 :
        return "Even"
    else :
        return "Odd"
    
results = is_even(5)
print(results)
    
