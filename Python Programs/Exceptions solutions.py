#Write a program to generate Arithmetic Exception without exception handling
print("Write a program to generate Arithmetic Exception without exception handling")
#result = 10/0
#print(result)
print("-"*50)
#Handle the Arithmetic exception using try-catch block
print("Handle the Arithmetic exception using try-catch block")
try:
    result = 10/0
except ZeroDivisionError:
    print("Error: Division by Zero")

#Write a method which throws exception, Call that method in main class without try block
print("Write a method which throws exception, Call that method in main class without try block")
def divide(a,b):
    result = a/b
    return result
#divide(10,0)

#Write a program with multiple catch blocks
print("Write a program with multiple catch blocks")
def division(a,b):
    try:
        result = a/b
        print(f"The result is {result}")
    except ZeroDivisionError:
        print("Error: Divison by Zero")
    except TypeError:
        #Write a program to throw exception with your own message
        print("Error:Enter only numbers")

#Write a program to create your own exception
print("-"*50)
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

def my_function(value):
    if value < 0:
        raise MyCustomException("Value cannot be negative")
    else:
        print("Value is positive:", value)

try:
    my_function(-5)
except MyCustomException as e:
    print("Caught custom exception:", e)
print("-"*50)

#Write a program with finally block
print("Write a program with finally block")
def div(x, y):
  try:
    result = x / y
    print("Result:", result)
  except ZeroDivisionError:
    print("Error: Division by zero!")
  finally:
    print("This block always executes")

div(10,0)
print("-"*50)
#Write a program to generate FileNotFoundException
print("Write a program to generate FileNotFoundException")
try:
    file = open("newfile.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("No file is found")

print("-"*50)

#Write a program to generate IOException
print("Write a program to generate IOException")
def write_to_readonly_file(file_path):
  try:
    with open('text.txt', 'r') as file:
      file.write("This is some content")
  except IOError as e:
    print("Error:", e)
write_to_readonly_file("/etc/passwd")  

#




