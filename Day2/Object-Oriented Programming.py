# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(self.brand, self.model, "is starting!")

# #Create Object
# my_car = Car("Tesla", "Model 3")
# my_car.start()


# 2

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(self.brand, self.model, "Is Starting!")

# #creating Multiple Objects

# car1 = Car("Tesla","Model 3")
# car2 = Car("BMW","X5")
# car3 = Car("Audi","A4")
# car4 = Car("Thar","Star Edition")

# car1.start()
# car2.start()
# car3.start()
# car4.start()

#3

# class BankAccount:
#     def __init__(self, Owner, balance):
#         self.owner = Owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited", amount)
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else :
#             self.balance -= amount
#             print("WithDrawn", amount)
    
#     def show_balance(self):
#         print("Current Balance:", self.balance)

# #crate Account Object
# account1 = BankAccount("Dnyanesh", 10000)
# account1.deposit(500)
# account1.withdraw(560)
# account1.show_balance()
# 3️⃣ What You Learned Here
# 1. Class --> blueprint
# 2. Object --> instance of class
# 3. Constructor (__init__) --> initialie object
# 4. Methods --> functions inside class
# 5. Self  --> refers to current object



# 4️⃣ Why Functions & OOP?
# Functions → reusable code
# OOP → structure for large projects
# Both are required for AI projects where you will build models, APIs, and apps

class Student :
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print(self.name, self.marks)

    def is_pass(self):
        if self.marks > 40 :
            print("Pass")
        else :
            print("Fail")

stu1 = Student("Dnyanesh", 85)
stu1.show_details()
stu1.is_pass()
