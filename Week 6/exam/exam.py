# Python Basics

# Data Types

# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple
# d) Set
#_________________________
#   Answer: Tuple
#_________________________
# Lists and Loops

# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.
#_________________________
answer =[number **2 for number in range(1,11) if number %2==0]
print(answer)
#_________________________
# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.
#_________________________
answer2 =[number for number in range(1,11) if number %2==0 and number %3==0]
print(answer2)
#_________________________

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
    print(f" {student['name']}, {student['age']} years")

# Function Behavior with *args and **kwargs

# Write a function combine_words that accepts any number of positional arguments and key-value arguments. The function should return a single sentence combining all the words provided.
# Example:
# print(combine_words("Hello", "world", second="is", third="great!", first="Python"))
# Expected Output:

# "Hello world. Python is great!"

def combine_words(*args, **kwargs):
    
    words = list(args)   
    part1 = ' '.join(words) 
    #print(part1)
    part2 = ". "+' '.join(kwargs[key] for key in sorted(kwargs))
    # print(part2)
    sentence = part1  + part2
    return(sentence)
    

print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

# Object-Oriented Programming (OOP)

# Create a class Vehicle with string attributes type, brand, and integer attribute year. Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.


class Vehicle:
    def __init__(self, type: str, brand: str, year:int):
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Type: {self.type}, Brand: {self.brand}, Year: {self.year}"


# OOP Inheritance and Decorators

# Create a class Car with string attributes brand, model, and integer attribute mileage. Implement a method to return the car’s details.

class Car:
    def __init__(self, brand: str, model: str, mileage:int):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Mileage: {self.mileage}"


# Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.

class ElectricCar(Car):
    def __init__(self, brand: str, model: str, mileage: int, battery_capacity: float):
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    def car_details(self):
        return super().car_details() + f", Battery Capacity: {self.__battery_capacity}"

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value: float):
        if value > 0:
            self.__battery_capacity = value

# Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created and a static method for a bank policy message. Ensure the balance is non-negative.
