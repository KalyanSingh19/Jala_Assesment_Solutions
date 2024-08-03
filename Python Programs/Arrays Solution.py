# Question 1 : function to add integer values of an array
print("to add integer values of an array")
sum = 0
num = [10,20,30,40,50]
for i in range(0,len(num)):
    sum = sum + num[i]
print(sum)
print("-"*50)

# Question 2 : to calculate the average value of an array of integers
print("to calculate the average value of an array of integers")
list1 = [10,20,30,40,50,60,70,80,90]
sum = 0
for x in list1:
    sum+=x
avg = sum / len(list1)
print(f"The average of the list is {avg}")
print("-"*50)

#Question3 : to find the index of an array element
print("to find the index of an array element")
list2 = [10,20,30,40,50]
print(list2.index(30))
print(list2.index(50))
print("- "*50)

# Question 4 : to test if array contains a specific value
print("to test if array contains a specific value:")

list3 = [10,20,30,5,40,1000]
def check_for_array(num):
    if num in list3:
        print("Element exists")
check_for_array(5)

print("-"*50)

#Question 5 : to test if array contains a specific value
print("to test if array contains a specific value:")
list4 = [10,20,30,40,50]
list4.remove(30)
print(list4)
print("-"*50)

# Question 6 : to copy an array to another array
print("to copy an array to another array:")
list5  = [100,200,300,400,500]
list6 = list5.copy()
print(list6)

print("-"*50)

# Question 7 : to insert an element at a specific position in the array
print("to insert an element at a specific position in the array")
list7 = [100,300,400,500,600,700,800]
list7.insert(1,200)
print(list7)

print("-"*50)

# Question 9 : to find the minimum and maximum value of an array
print("to find the minimum and maximum value of an array")
list8 = [100,200,3004,5000,2858,6784,85767,82834]
min_value =list8.index( min(list8))
max_value = list8.index(max(list8))
print(f"Max value is at {max_value}")
print(f"Min value is at {min_value}")

print("-"*50)

# Question 10 : function to reverse an array of integer values
print("function to reverse an array of integer values")
list9 = [10,20,30,40,50,60,70,80]
list9.reverse()
print(list9)
print("-"*50)

# Question 11 : to find the duplicate values of an array
list10 = [10,20,30,40,50,50,60,70,70,80]
for x in range(0,len(list10)):
    for k in range(x+1, len(list10)):
        if list10[x] == list10[k]:
            print("Duplicate element is present")

print("-"*50)

# QUestion: 12to find the common values between two arrays
print("to find the common values between two arrays")
lista = [10,20,3,4,5,6,7]
listb = [10,5,6,78,2,3,10]
common_elements = [x for x in lista if x in listb]
print(common_elements)

print("-"*50)

# Question 13 : a method to remove duplicate elements from an array
print("a method to remove duplicate elements from an array")
def remove_duplicates(lis):
    return list(set(lis))
listc = [10,10,20,30,40,50,60,60,60,60,60,60,70,90]
newlist = remove_duplicates(listc)
print(newlist)

print("-"*50)

#Question 14 : a method to find the second largest number in an array
print("a method to find the second largest number in an array")
arr1 = [10,50,60,90,20,40,453,976,7794,9284]
arr1.sort()
print(arr1[-2])

print("-"*50)

#Question 15 : a method to find number of even number and odd numbers in an array
print("a method to find number of even number and odd numbers in an array")
arr2 = [12,3,4,5,6,7,89,32,45,34,54,6,77,556,5,7576,8,867375,75,32,43]
even_number = []
odd_number = []
for x in arr2:
    if x%2==0:
        even_number.append(x)
    else:
        odd_number.append(x)
print(f"Total even numbers : {even_number}")
print(f"Total Odd numbers : {odd_number}")
print("-"*50)

# Question 16 : function to get the difference of largest and smallest value
print("function to get the difference of largest and smallest value")
def find_difference(lis):
    lis.sort()
    a= lis[-1]
    b = lis[0]
    result = b-a
    print(f"The difference is {result}")
listt = [6987,4827,3575,8437,9494,3475,3875,8475,8794,7565,8467]
find_difference(listt)
print("-"*50)

# Question 17 : a method to verify if the array contains two specified elements(12,23
print("a method to verify if the array contains two specified elements(12,23)")
arra = [12,45,36,78,92,14,57,89]
for x in arra:
    if x == 12:
        print ("Array exists")
    if x == 23:
        print("Array exists")
print("-"*50)

#Question 18 : a program to remove the duplicate elements and return the new array
print("a program to remove the duplicate elements and return the new array")
new_list = set()
def remove_duplicates(ar):
    lis= [x for x in ar if x not in new_list and not new_list.add(x) ]
    print(lis)
arr3 = [12,12,12,12,3,4,5,3,2,2342,432,323,432,432,43,432]
remove_duplicates(arr3)