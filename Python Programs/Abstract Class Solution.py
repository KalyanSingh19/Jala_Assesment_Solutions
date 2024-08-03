#Create an abstract class with abstract and non-abstract methods.
print("Create an abstract class with abstract and non-abstract methods.")
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    def love(self): #Non abstract method
        print("Protect the animals")

class Cow(Animal):
    def eat(self):
        print("Cows eat grass")
#"Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods")
class Tiger(Animal):
    def eat(self):
        print("Tiger eats meat")
print("Create an instance for the child class in child class and call abstract methods")
obj1 = Tiger()
obj1.eat()
print("-"*50)

obj1.love()
print("Create an instance for the child class in child class and call non abstract methods")
obj1.love()

print("-"*50)

#