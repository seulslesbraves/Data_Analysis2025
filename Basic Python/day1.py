"""print("Rabina Dangol")


num1= input("Enter a number: ")
print(num1)"""

#input your name and print it
"""NAME= input("Enter your name:")
print(NAME)"""

#typecasting : changing from one data type to another type
#eg: int, str, float, etc

#input data  type is always str
"""num1= int(input("Enter a number:"))
num2= int(input("Enter another number:"))
print(num1+num2)"""

#task1: Take input of 5 different numbers and print the sum of all numbers
"""num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
sum = num1 + num2 + num3 + num4 + num5
print("Sum of all numbers:", sum)"""

#task2: take input of your name and surname and concatenate them
"""name= input("Enter your first name: ")
surname= input("Enter your surname: ")
full_name = name + " " + surname
print("Full name:", full_name)"""


#naming convention
#PascalCase, camelCase,snake_case, kebab-case

#Data Type
"""int, str, tuple, float, list, dict, set"""
"""list1=[1,2,3.5,"JIhyaa",[1,1,1]] #group data type"""

"""mutable and non-mutable data type"""

#type(): used to find the data type
"""a= 10
print(type(a))"""

#logical operator : AND, OR,  NOT
"""x = True
y = False
print(x and y)  # output: False  (True if both are True)
print(x or y)   # True  ( True if at least one is True)
print(not x)    # False (Inverst the result)"""

#Identity Operators:  is , isnot, in, not in
"""is : checks the memory location while == checks the value"""

#Membership Operators: in, not in
"""in: checks whether the value present in group data type or not"""
#example:
"""name= "Jihyaa Koyee"
check= "J" in name
print(check)
"""

#TASK1: Create a simple calculator 
"""print("Simple Calculator")

# Take inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Show results
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
"""
#TASK2: input two no of user and perform all the airth operation on them

#python method
"""name= "Rabeena Dangol"
print(name)
print(name.lower())

"""


#LIST:
"""list1=[1,2,3.5,"JIhyaa",[1,1,1]] #group data type
list1.append(7) #Adds an element(7) at the end of the list
print(list1)"""

#INDEX:  the position of element and is always unique.

#Indexing: Accessing the single element from the group data type
"""print(list1[5])  #shows result 7 as indexing starts from 0 not 1.
print(list1[-1])  #shows  result 7 as it means last element"""

#Slicing: Accessing multiple elements or creating a new list from group data type
#Syntax:
"""name[start_index: end_index]"""
#example: 
"""print(list1[2:4])"""


#string data type is also a group data type
#we can perform indexing and slicing in string also in the same way

#TASK1: perform indeixing and slicing in stting data type
#INDEXING:
"""text = "Python"

# Positive indexing
print(text[0])  # P
print(text[1])  # y
print(text[5])  # n

# Negative indexing
print(text[-1]) # n
print(text[-2]) # o
print(text[-6]) # P
"""
#SLICING:
"""text = "Python Programming"

print(text[0:6])    # Python
print(text[7:18])   # Programming
print(text[:6])     # Python   (from beginning)
print(text[7:])     # Programming  (till end)
print(text[:])      # Python Programming (whole string)

# With step
print(text[0:18:2]) # Pto rgamn (every 2nd char)"""









#Tuple: same as list that store multiple elements but it wraps with () <---- parenthesis
"""tuple1 = (1,2,2,3,7,"JIHYAA", 9,00.9,90)
print(type(tuple1))"""

#SET: same as list that store multiple elements but it wraps with {}
"""set1 = {17,2,"Inez",3,7,"JIHYAA", 19,8.9,80}
set2 =  {1,2,2,3,7,"JIHYAA", 9,00.9,90}
print(type(set1))
print(set1.intersection(set2))
print(set1.union(set2))"""

#DICT: also a group data type that has element in a key value pair
#we also wrap the elements by {}
#example:
"""dict1= {
    "name": "Jihyaa Koyee",
    "age": 25,
    "position": "AI Engineer"
    }

print(type(dict1))

#keys, values, update, get 
print(dict1.values())
print(dict1.update({"age": 66}))
print(dict1)"""



#TAsk2: JSON --> search and explore bout JSON data type
"""       What is JSON?

JSON stands for JavaScript Object Notation.

It is a lightweight format to store and exchange data.
Very popular for APIs, databases, and config files.
Easy for humans to read and computers to parse.
In JSON, data is written as key value pairs inside { }."""

"""      What is an API?

API stands for Application Programming Interface.
It’s like a messenger that allows two different software or apps to talk to each other."""

#Example:
"""{
  "name": "Alice",
  "age": 21,
  "is_student": true,
  "skills": ["Python", "SQL", "Data Analysis"],
  "address": {
    "city": "Kathmandu",
    "country": "Nepal"
  }
}"""


#TAsk: Create a dict of usernames and password
#extract all the username from dict

# Dictionary of usernames and passwords
users = {
    "inez": "inez123",
    "jihyaa": "jihyaa123",
    "hermez": "hermez123"
}

# to extract all usernames i.e keys
usernames = users.keys()

print("All usernames:", usernames)

