# 
print('---------------Data Types-----------------')

# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple
# d) Set
# 
print('answer: c) Tuple')


print('-------------Lists and Loops-----------------')

# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.

num_list = range(1, 11)
print(num_list)
for x in num_list:
    if x % 2 == 0 and x % 3 == 0:
        print(x)

# Loop through the provided list of dictionaries and print the names and ages:

student_list = [
    {
    "name": "John", 
    "age": 24
    }, 
    {
    "name": "Anna", 
    "age": 22
    }, 
    {
    "name": "Mike", 
    "age": 25
    }
]

for student in student_list:
    name = student["name"]
    age = student["age"]
    print(f"Name: {name}, Age: {age}")

print('-------------Function Behavior with *args and **kwargs---------------')
# 
# Write a function combine_words that accepts any number of positional arguments and key-value arguments. The function should return a single sentence combining all the words provided.


def combine_words(*args, **kwargs):
    words = list(args) + list(kwargs.values())
    sentence = ' '.join(words)
    return sentence

print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

print('Expected Output: \n "Hello world. Python is great!"')


print('-------------Object-Oriented Programming (OOP)----------------')

class Vehicle:
    def __init__(self, type_, brand, year):
        if not all((type_, brand, year)):
            raise ValueError("not all attributes.")
        self.type = type_
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Type: {self.type}, Brand: {self.brand}, Year: {self.year}"

veh = Vehicle('type', 'brand', 2002)     
print(veh)   

print('-------------OOP Inheritance and Decorators-----------------------')

class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def get_details(self):
        return f"Car info: brand {self.brand}, model {self.model}, mileage {self.mileage}"

car = Car('Honda', 'civic', 100000)   
print(car.get_details())     

class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery_capacity):
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = new_capacity

    def get_details(self):
        car_details = super().get_details()
        return f"{car_details}, Battery Capacity: {self.__battery_capacity}"

elcar = ElectricCar('Tesla', 'X', 10, 2000)   
print(elcar.get_details())     

class BankAccount:
    _total_accounts = 0

    def __init__(self, account_holder, initial_balance=0.0):
        self._account_holder = account_holder
        self._balance = max(0.0, initial_balance)
        BankAccount._total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def view_balance(self):
        return self._balance

    @classmethod
    def total_accounts(cls):
        return cls._total_accounts

    @staticmethod
    def bank_policy_message():
        return "some message"

account1 = BankAccount("Mike", 1000.0)
account2 = BankAccount("Bred", 500.0)

account1.deposit(200)
account2.withdraw(100)

print(f"{account1._account_holder}'s Balance: {account1.view_balance()}")
print(f"{account2._account_holder}'s Balance: {account2.view_balance()}")
print("Total Accounts:", BankAccount.total_accounts())
print(BankAccount.bank_policy_message())


print('-------------Data Science-----------------------')

import numpy as np, pandas as pd, matplotlib.pyplot as plt

array = np.arange(1,10).reshape(3,3)

print(array)

df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})


# 
# 
# Replace non-numeric values in column “A” with the mean of numeric values. Plot a histogram of the “A” column using matplotlib.
# 
# Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.
#


# 
# Django and Django REST
# 
# Create a new Django project called ‘academy’. After that - create a new app (inside the ‘academy’ project) called ‘school’.
# 
# 
# 
# Django Models with Foreign Key
# 
# Define Django models Teacher and Course. Course has course_name (CharField) and course_code (CharField). Teacher has name (CharField). Create a many-to-many relationship between Teacher and Course.
# 
# 
# Views
# 
# Create a Django view course_details to fetch details of a course by its id.
# 
# 
# Use a APIview for Teacher to display all teachers.
# 
# 
# Create a base model SchoolFacility with facility_name (CharField) and usage_purpose (TextField).
# 
# 
# Create a Laboratory model inheriting from SchoolFacility with equipment_list (TextField).
# 
# 
# Create views for all school facilities and another for only laboratories.
# 
# 
# Create a serializer for SchoolFacility and another for Laboratory to convert to JSON. Test using Postman.
# 
# 
# 
# Good Luck !