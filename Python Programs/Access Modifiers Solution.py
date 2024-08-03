#Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method.
print("Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method.")
class Myclass:
    def __init__(self):
        self.__name = "Kalyan Singh"
        self.__Age = 23
        self._education = "B.Sc"
    def private_details(self):
        print("These are private details")
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__Age
    def get_edu(self):
        return self._education

    def main(self):
        print(self.get_name)
        print(self.get_age)
        self.private_details()

class Subclass(Myclass):
    def acess_private(self):
        print(self.get_name())
        print(self.get_age())

if __name__ == "__main__":
    obj = Myclass()
    obj.main()
print("Create a sub class and try to access the private fields and methods from sub class.")
obj1 = Subclass()
obj1.acess_private()

print("-"*50)

#Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.
print("Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.")
class Employee():
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary
    def get_name(self):
        print(self._name)
    def get_sal(self):
        print(self._salary)

class SubEmployee(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def acess_protected(self):
        self.get_name()
        self.get_sal()

obj4 = SubEmployee("kalyan",5000)
print(obj4.acess_protected())

print("-"*50)

#Create a class with PUBLIC fields and methods
print("Create a class with PUBLIC fields and methods")
class NewClass:
    public_field = "This is a public field"

    # Public method
    def public_method(self):
        print("This is a public method")
print("-"*50)
print()
print("Access the public methods and fields from any class in the same package")
class AnotherClass:
    def access_public_members(self):
        obj = NewClass()
        print(obj.public_field)
        obj.public_method()

obj2 = AnotherClass()
obj2.access_public_members()

