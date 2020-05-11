#Write a program to create a file and insert a paragraph and close.
#Creating a file and adding paragraph and closing it
file = open("pyfile1.txt", "w") 
file = open("pyfile1.txt", "a") 
file.write ("We are in a pandemic era \n")
file.write ("We are in new york \n")
file.write ("We are getting news for lock down daily\n")
file.close() 

# Write a program to read the first line of the file.
file = open("pyfile1.txt", "r") 
print(file.readline()) 
print() 
file.close() 

#Write a program to append data into the file created above.

file = open("pyfile1.txt", "a") 
file.write ("We are praying to get over with this terrible era \n")
file.close() 
#Write a program to fetch the file located at the desktop.
# we will be using os methods to find the location directory

import os
file1 = open(os.path.expanduser("~/Desktop/somefile.txt"), 'r')

file_list = file1.readlines()

#using for lope to print line by line from file

for line in file_list:
    print(line)
file1.close()

#Write a program to remove the file located at the
#We will be using the OS module to invoke remove method to delete file from desktop
import os
os.remove(os.path.expanduser("~/Desktop/somefile.txt"))
