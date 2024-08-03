student_list = {101:'Kalyan',102:'Karan',103:'Rohit',104:'Rahul',105:'Siddhu'}
print(student_list)
print("-"*50)
print("Adding a value to Dictionary")
print("-"*50)
student_list[106] = "Teena"
print(student_list)
print("-"*50)
print("Updating a Value to Dictionary")
student_list.update({101:'Kalyan Singh'})
print(student_list)
print("-"*50)
print("Accessing the value in dictionary")
print(student_list.get(102))
print("-"*50)
print("Create a nested loop dictionary")
student = {
    101:{
        'name': "Kalyan","Age":23,'grades':{
            'maths':80,'science':98,'English':91}
    },102:{
        'name': "Karan","Age":25,'grades':{
            'maths':88,'science':94,'English':90}
    },103:{
        'name': "Rahul","Age":20,'grades':{
            'maths':75,'science':87,'English':91}
    },104:{
        'name': "Teena","Age":18,'grades':{
            'maths':88,'science':93,'English':76}
    },105:{
        'name': "Guna","Age":14,'grades':{
            'maths':98,'science':100,'English':100}
    }
}

print(student)


print("-"*50)


#Access the values of nested loop dictionary
print("Access the values of nested loop dictionary")
print(student.get(102,{}).get('name'))
print(student.get(104,{}).get('grades',{}).get("maths"))

print("-"*50)


#Print the keys present in a particular dictionary
print("Print the keys present in a particular dictionary")
print(student.keys())
print(student[101].keys())
print(student[102]["grades"].keys())

print("-"*50)


#Delete a value from a dictionary
print("Delete a value from a dictionary")
del student[103]
print(student)




