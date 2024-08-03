# Question 1:  Different ways of creating strings
print("Different ways of Creating strings")

name = 'Kalyan singh'
name = "Kalyan Singh"
name = '''kalyan singh'''
name = str("Kalyan")

print('-'*50)

# Question 2: Concatenating two strings using + operator
print("Concatenating two strings using + operator")
print("kalyan"+"Singh")

# Question 3: Finding length of String
print("Finding length of String")
print(len(name))
count = 0
for x in 'kalyansingh':
    count+=1
print(count)
print("-"*50)

#Question 4: Extract a string from sub string 
print("Extract a string from sub string ")
name = 'PYTHON WORLD'
print(name[1:3])
print("-"*50)

#Question 5 : Searching in strings using index()
print("Searching in strings using index()")
print(name.index("W"))
print("-"*50)

#Question 6 : Matching a String Against a Regular Expression With matches()
print("Matching a String Against a Regular Expression With matches()")
import re
str1 = "You flee my dream come the morning "
str2 = 'You'
mat=re.match(str1,str2)
print(mat)
print("-"*50)

# Question 7 : Comparing strings
print("Comparing strings")
str1 = "Kalyan Singh"
str2 = "Rajput"
print(str1==str2)
print("-"*50)

# Question 8 : startsWith(), endsWith() and compareTo()
print("startsWith(), endsWith() and compareTo()")
name = "Kalyan Singh"
print(name.startswith('Kalyan'))
print(name.endswith("Singh"))
print("-"*50)

#Trimming strings with strip()
print("Trimming strings with strip()")
name = "Hello world!This is kalyan"
print(name.strip('Hellow world!'))
print("-"*50)

#Replacing characters in strings with replace()
print("Replacing characters in strings with replace()")
print(name.replace('This','I am'))
print("-"*50)

#Splitting strings with split()
print("Splitting strings with split()")
print(name.split("!"))
print("-"*50)

#Converting integer objects to Strings
print("Converting integer objects to Strings")
number = str(1234)
print(number)
print(type(number))
print("-"*50)

#Converting to uppercase and lowercase
print("Converting to uppercase and lowercase")
result = ''
for char in name:
    if 'A' <= char <= 'Z':
        result+=chr(ord(char)+32)
    else:
        result+=char

print(result)

