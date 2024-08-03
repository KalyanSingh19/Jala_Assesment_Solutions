#Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C
print("Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C")

class A():
    def display(self):
        print("This is  Class A")
    def show(self):
        print("Now Iam inside class A")

class B(A):
    print("Welcome to B'S worls")
    def dis(self):
        print("This is class B")
    def show(self):
        print("Now i am inside B class")
    

class C(B):
    def show(self):
        super().show()
        print("Now i am inside class C")

obj1 = C()
obj2 = B()
obj1.show() # Overriding Method of class A
obj2.dis()
obj2.show() # calling Method of class B

print("-"*50)
#Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance.
print("Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance.")

class Main():
    def main(self):
        a = A()
        b = B()
        c = C()

        a.display()
        a.show()
        b.dis()
        c.show()

Main().main()

print("-"*50)

# Call an overridden method with super class reference to B and C class’s objects
print("Call an overridden method with super class reference to B and C class's objects")
obj1 = C()
obj2 = B()
obj1.show() # Overriding Method of class A
obj2.dis()
obj2.show() # calling Method of class B

print("-"*50)

#Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members
print("Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members")
class Vehicle():
    def wheels(self):
        print("Vehicle has wheels")
class Car(Vehicle):
    def wheels(self):
        print("Car has Fpur wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has two wheels")

def vehicle_wheels(vehicle):
    vehicle.wheels()

bike = Bike()
car = Car()

vehicle_wheels(bike)
vehicle_wheels(car)




