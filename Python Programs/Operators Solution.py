# Question 1:
# to show arthemicatic operations
num1 = input("Enter first Value")
num2 = input("Enter Second Value")
# Addition operation
def add(num1,num2):
    try: # try block is used in error handling which is used before the block of code which might cause execption
        result = float(num1) + float(num2)
        print(f"The sum of {num1} and {num2} is {result}")
    except TypeError: # except block handles the different cases 
        print("Error: Operands must be numbers")
# Subtraction Operation
def subtract(num1,num2):
    try:
        result = float(num1) - float(num2)
        print(f"The subtraction of {num1} and {num2} is {result}")
    except:
        print("Error: Operands must be numbers")
# Multiplication Operation
def multiply(num1,num2):
    try:
        result = float(num1) * float(num2)
        print(f"The Multiplication of {num1} and {num2} is {result}")
    except:
        print("Error: Operands must be numbers")
# Division Operation
def divide(num1,num2):
    try:
        result = float(num1) / float(num2)
        print(f"The Division of {num1} and {num2} is {result}")
    except ZeroDivisionError:
        print("Error: Division by Zero")
    except TypeError:
        print("Error: Operands must be numbers")

add(num1,num2)
subtract(num1,num2)
multiply(num1,num2)
divide(num1,num2)

print('-' * 50)

#Question 2 : For increment and decrement operators
count = 0
for x in range(5):
    count += 1 # increment operator
print(f"The value of Count is {count}")
for y in range(5):
    count-=1 # decrement operator
print(f"The value of count is {count}")

print('-'*50)

# Question 3: Program to find two numbers or equal or not
x = int(input("Enter first number "))
y = int(input("Enter Second number"))
if x == y: # '==' operator is used to check if both data types are equal or not
    print("Numbers are Equal")
else:
    print("Numbers are not equal")

print("-" * 50)

# Question 4 : Program for Relational operators
a = 10
b = 20
print(a<b) # returns True if b is greater than a
print(a<=b) # returns True if b is greater than or equal to a
print(a>b) # returns True if a is greater than b
print(a>=b) # returns True if a is greater than or equal to b
print(a==b) # returns True if both a and b are equal
print(a!=b) # returns True if a and b are not equal

print("-"* 50)

# Question 5: print smaller and larger number
if x > y :
    print(f"The value of {x} is greater than {y}")
else:
    print(f"The value of {x} is smaller than {y}")

