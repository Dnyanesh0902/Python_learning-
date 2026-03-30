# Python Data Structures.
# 1️⃣ Lists
# 2️⃣ Dictionaries

# 🐍 1️⃣ Python Lists
# A list stores multiple values in one variable.

nums = [10, 20, 30, 40, 50]
print(nums)

# Access List Elements
# Index starts from 0.
numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[2])

# Add Elements to List
fruits = ["apple","banana"]
fruits.append("mango")
print(fruits)

# Loop Through List
numbers = [1, 2, 3, 4, 5]

for n in numbers :
    print(n)

# 🐍 2️⃣ Python Dictionaries
# A dictionary stores data in key : value pairs.
student = {
    "name" :"Dnyanesh",
    "age":24,
    "marks" : 85
}

print(student)
# Access Dictionary Values
print(student["name"])
print(student["marks"])
# Add New Data
student["City"] ="Pune"
print(student)

# Loop Through Dictionary
for key, value in student.items():
    print(key, ":", value)

# 🧠 Why Lists & Dictionaries Are Important
# AI and Data Science use them heavily.

students = ["Ram","Shyam","Amit"]

marks = {
    "Ram" :85,
    "Shyam" :78,
    "Amit" :92
}

# 1️⃣ What is List Comprehension?
# It is a short and powerful way to create lists

numbers = [1, 2, 3, 4, 5]

even_numbers = []

for n in numbers :
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)

# ⚡ List Comprehension Version
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [n for n in numbers if n % 2  == 0]
print(even_numbers)

# 2️⃣ Example – Square Numbers
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

# 3️⃣ Example – Convert Names to Uppercase
names = ["ram", "shyam","amit"]
upper_names = [name.upper() for name in names]
print(upper_names)

# 4️⃣ Example – Filter Numbers > 10
numbers = [5, 12, 8, 20, 3]
result = [n for n in numbers if n > 10]
print(result)

# Practice Challenge
# 1️⃣ Square numbers from 1–10 using list comprehension
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squ = [n * n for n in num]
print(squ)

# 2️⃣ From list [10,15,20,25,30] create a new list with numbers divisible by 5.
num1 = [10,15,20,25,30]
newls = [n for n in num1 if n % 5 == 0]
print(newls)

# 3️⃣ Convert this list to uppercase
language =["python","ai","developer"]
upper_name =[lang.upper() for lang in language]
print(upper_name)