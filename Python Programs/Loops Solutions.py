#Question 1 : Print Bright IT career 10 times using for loop
print("Print Bright IT Caereer 10 times :")
for x in range(10):
    print("Bright IT Career")

print("-"*50)

#Question 2 : print 1 to 20 numbers using while loop
print("print 1 to 20 numbers using while loop:")
i = 1
while i <=20:
    print(i,end=' ')
    i+=1
print('')
print('-'*50)
#Question 3 : to print equal and not equal operator
print("to print equal and not equal operator:")
a = 10
b = 20
if a==b:
   print("Equal")
else:
    print("Not equal")

print('-'*50)
#Question 4 : to print even and odd numbers:
print("to print even and odd numbers:")
print("Even Numbers:")
for x in range(1,51):
    if x %2 == 0:
        print(x,end=' ')
print("\n Odd Nubers:")
for x in range(50):
    if x %2 !=0:
        print(x,end=' ')

print('')
print('-'*50 )

# Question 5 : To Print Largest number among three numbers:
print("To Print Largest number among three numbers:")
x = 100
y = 110
z = 80 

if (x > y) and (x>z):
    print(f"\n The largest number is {x}")
elif (y>x) and (y>z):
    print(f"\n The largest number is {y}")
elif (z>x) and (z>y):
    print(f"\n The largest number is {z}")

print('-'*50)

# Question 6 : print even numbers between 10 and 20 using while loop 
print("print even numbers between 10 and 20 using while loop:")
variable = 10
while variable <= 20:
    if variable %2 == 0 :
        print(f" Even Numbers are {variable}")
    variable+=1
print('-'*50)

# Question : 7 print 1 to 10 using the do-while loop statement.
print("print 1 to 10 using the do-while loop statement:")
c = 1
while True:
    print(c,end=' ')
    c+=1
    if c > 10:
        break
print()
print("="*50)

# Question 8 : Write a program to find Armstrong number or not
print("to find Armstrong number or not")
num = int(input("Enter number Check Armstrong number"))
original = num
power = len(str(num))
store = 0
while num > 0 :
    digit = num%10
    store += digit**power
    num= num//10

if original == store:
    print("It is Arm Strong number")
else:
    print("It is not Arm Strong number")

print("-"* 50 )

# Question 9 : program to find the prime or not
print("to program to find the prime or not :")
def primeNumber(num):
    if num == 1:
        print("The number is not prime number")
    if num > 1:
        for i in range(2,num):
            if num% i == 0:
                print("The number is not prime number")
                break
        else:
            print("The number is Prime number")

primeNumber(original)

print("-"*50)

# Question 10 : Write a program to palindrome or not.
print("program to check a number is  palindrome or not ")
n = int(input("Enter number to check if number is pallindrome or not : "))
original_num = n
reverse_num = 0
while (n>0):
    digit = n % 10
    reverse_num = reverse_num*10 + digit
    n = n//10
if reverse_num == original_num:
    print("The number is pallindrome")
else:
    print("The number is not pallindrome ")

print("-"*50)

# Question 11: to check whether a number is EVEN or ODD using switch, python doesnt support switch
print("to check whether a number is EVEN or ODD")
if original % 2 == 0:
    print("Even")
else:
    print("Odd")

# Question 12 : Print gender (Male/Female) program according to given M/F using match case
print("Print gender (Male/Female) program according to given M/F using match case")
gender = input("Mention your gender")
match gender:
    case "Male":
        print("Your gender is Male")
    case "Female":
        print("Your gender is female")
    case _ :
        print("Invalid input")





    




    

    


