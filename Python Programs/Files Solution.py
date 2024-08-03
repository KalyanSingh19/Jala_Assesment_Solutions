#Write a program to write text to .txt file using InputStream
print("program to write text to .txt file using InputStream")
file = open("New file.txt","w")
add = "First Python file"
file.write(add)
file.close()
#Write a program to read text file
print("Write a program to read text file")
file1 = open("New file.txt","r")
data = file1.read()
print(data)
print("-"*50)
#Write a program to read a file stream supports random access
print("program to read a file stream supports random access")

file3 = open("New file.txt","r")
#Write a program to read a file a just to a particular index using seek()
file3.seek(4)
ch = file3.read(1)
print(ch)

print("-"*50)

#
import os

def check_file_permissions(file_path):
  has_read_permission = os.access(file_path, os.R_OK)
  has_write_permission = os.access(file_path, os.W_OK)
  return has_read_permission, has_write_permission

if __name__ == "__main__":
  file_path = "New file.txt"  

  read_permission, write_permission = check_file_permissions(file_path)

  print(f"File: {file_path}")
  print(f"Read permission: {read_permission}")
  print(f"Write permission: {write_permission}")
