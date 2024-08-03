#Define a static variable and access that through a class
print("Define a static variable and access that through a class")

class StaticVar():
    staticvariable = 100

print(StaticVar.staticvariable)
print("-"*50)

# Define a static variable and access that through a instance
print("Define a static variable and access that through a instance")

class Python():
    value1 = 56560348
    value2 = 5653854380

example = Python()
print(example.value1) 
print(example.value2)

print("-"*50)

#Define a static variable and change within the instance
print("Define a static variable and change within the instance")
example.value1 = 200
print(example.value1)
print("-"*50)

# Define a static variable and change within the class
class Jython:
    val = 89
    

    def change_value():
        Jython.val += 100
        return Jython.val
    
obj = Jython()
new_ob = Jython.change_value()
print(new_ob)
