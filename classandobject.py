# define a class
class Bike:
    name = "Road Bike"  # class attribute
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 5
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

bike2 = Bike()
# access attributes and assign new values


print(f"Name: {bike2.name}, Gears: {bike2.gear} ")

class Employee:
    id = 0  # class attribute
    name = ""  # class attribute
    
    #constructor method
    def __init__(self, name, id):
        self.name = name  # instance attribute
        self.id = id    # instance attribute

    #class Method
    def display_info(self):
        print(f"Inside Class Employee ID: {self.id}")  # instance method to display employee ID  



emp1 = Employee("Ram",  101)  # creating an instance of Employee
#emp1.id = 101  # instance attribute
emp1.display_info()  # calling the instance method
print(f"Employee ID: {emp1.id}")
emp2 = Employee("Sarath",  102)  # creating another instance of Employee#emp2.id = 102  # instance attribute
emp2.display_info()  # calling the instance method
print(f"Employee ID: {emp2.id}")
