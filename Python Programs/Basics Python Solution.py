#  Question : 1
# To print your name 
print('Kalyan Singh')

print("-"*50) # to separate each output in console


#Question 2:
# Single line and Multi Line Commands
#This is 
# Multi Line 
#Commenting
print("Single Line  and  MultiLine Commenting")


print("-"*50) # to separate each output in console



# Question 3: 
a = 50
print(f"The type of a is {type(a)}")
b = False
print(f"The type of a is {type(b)}")
c = 5.0
print(f"The type of a is {type(c)}")
charector = 'My program'
print(f"The type of a is {type(charector)}")

print("-"*50)# to separate each output in console

# Question 4 :
x = 10
def glob():
    # takes global variable as local variable isnt defined
    print(x)

def local():
    #local variable is defined
    x = 20
    print(x)

def both():
    # precedence of local variable over global variable 
    global a
    a = 60
    print(a)

glob()
local()
both()

print("-"*50) # to separate each output in console