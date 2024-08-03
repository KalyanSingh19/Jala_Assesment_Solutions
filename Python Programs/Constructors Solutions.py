#Write a class with a default constructor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class
class A:
    def __init__(self):
        print("Default constructor")
class B:
    def __init__(self,name):
        self.name = name
        print(f"My name is {self.name}")
    
class C:
    def __init__(self,name,age):
        self.name=name
        self.age = age
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")

class Main():
    obj1 = A()
    obj2 = B("Kalyan")
    obj3 = C("kalyan",23)

ob = Main()

print("-"*50)

#Call the constructors(both default and argument constructors) of super class from a child class
print("Call the constructors(both default and argument constructors) of super class from a child class")
class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Child(Student):
    def __init__(self, name):
        super().__init__(name)


objx = Child("Kalyan")
print(objx.get_name())  
print("-"*50)

#Apply private, public, protected and default access modifiers to the constructor

print("Apply private, public, protected and default access modifiers to the constructor")
class Emp():
    def __init__(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary
    def get_details(self):
        print(f"This is public dataset: {self.name} ")
        print(f"This is protected dataset: {self._age} ")
        print(f"This is private dataset: {self.__salary} ")

obj1 = Emp("kalyan",23,500000)
obj1.get_details()

print(""*50)

#Write a program which illustrates the concept of attributes of a constructor
print("program which illustrates the concept of attributes of a constructor")
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand  # Attributes
        self.color = color
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")

# Creating objects with different attributes
car1 = Car("Toyota", "Red", 2023)
car2 = Car("BMW", "Black", 2022)

# Accessing attributes and using methods
car1.display_info()
car2.display_info()
