#Conditional statements works under the condition
#If the condition is true, then only the statement under conditional statements execute
#If the condition is false, then conditional statements is skipped.

#IF-ELSE:
"""Syntax:
if condition:
    #lines of codes
else:
    #lines of codes"""

#example:
"""a = 10
b = 20
if a > b:
    print("TRUE")
else:
    print("FALSE")"""

#ELIF:
"""marks= 77

if marks >= 90:
    print("A+")

elif marks >= 80 and marks <90:
    print("A")

elif marks >= 70 and marks <80:
    print("B")

elif marks >= 60 and marks <70:
    print("C")
else:
    print("FAIL")"""

#TASK1: create a list of usernames:
"""usernames = ["Inez", "Hermez", "Jihyaa", "Eden"]
username = input("Enter your username: ")

if username in usernames:
    print("Username is found")

else:
    print("Username not found")"""


#Task2: create a dict of usernames and passwords 

"""users = {
    "inez": "inez123",
    "jihyaa": "jihyaa123",
    "hermez": "hermez123"
}

# to extract all usernames i.e keys
username = users.keys()
password = users.values()
print(username)
print(password)

username = input("Enter your username: ")

if username in users:
    print("Username is found")

else:
    print("Username not found")"""


#LOOPS:
"""loops are used when we need to repeat a same block of code multiple times"""
#types:
"""for loop and while loop"""
#for loop:
"""used when we already know the start and stop condition
   For keyword is used in for loop"""

#SYNTAX:
#for loop:
"""for iterator in iterable:  # iterable means group data type 
    #code to be executed"""   #iterator means a variable used to count the iteration
#iteration is a single round that is executed when a loop is encountered.

#example:
"""users = {
    "inez": "inez123",
    "jihyaa": "jihyaa123",
    "hermez": "hermez123"
    }
print(users)
for i in users:
    print(users.get(i))"""


#Example:
"""list1 =["Inez","Rai",2,4,6,7]
for i in list:
    print(i)
"""

#Range: Generates the value, it takes three values: start, end and step
"""
for i in range(5,20,2):
    print(i)"""

# Print even numbers from 0 to 100
"""
for i in range(0, 101, 2):  # start=0, end=100, step=2
    print(i)

#for odd numbers:
for i in range(1, 101, 2):  # start=1, end=100, step=2
    print(i)"""

#use fo list comprehension
#we use loop inside the list
"""list= [i for i in range(1,101)]  #prints 1 to 100 
print(list)"""

"""list= [i**2 for i in range(1,101)]    #for power
print(list)"""

"""list= ["inez" for i in range(1,101)]  #prints inez 100 times
print(list)"""


#WHILE LOOP:
"""used when we don't know the start and stop condition
   While keyword is used in while loop"""
#Syntax
"""while condition:
    code to be executed"""
#example:
"""a = 10
while a >= 0:
    print(a)
    a -= 1"""


#break: can be used only in loop. When break encounters, it completely exists the loop.
#continue: When continue encounters it skips the current iteration but continues the loop.
"""
list = [i for i in range(1,11)]
for i in list:
    if i ==6:
        print("Breaking...")
        break  #if break was not included it would have printed #1 2 3 4 5 breaking 7 8 9 10
    else:
        print(i)"""

#continue: When continue encounters it skips the current iteration but continues the loop.

"""list = [i for i in range(1,11)]
for i in list:
    if i ==6:
        print("Continuing...")
        continue
    else:
        print(i)"""

#using BREAK in calculator:
"""while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    choice =int(input("Enter 1 for add, 2 for sub, 3 for mul and 4 for div, 5 for exist: "))
    match choice:
        case 1:      #we can do "case 1|2|3" as well it means OR
            print(num1+num2)
        case 2:
            print(num1 - num2)
        case 3:
            print(num1*num2)
        case 4:
            print(num1/num2)
        case 5:
            break
        case _:
            print("Invalid")
"""

#Nested if-else: means if else inside if else
"""
a =1
b =9
c=11

if a > b:
    if a > c:
        print("A IS GREATEST")
    else:
        print("C IS GREATEST")
else:
    if b>c:
        print("B IS GREATEST")
    else:
        print("C IS GREATEST")
"""

#NESTED LOOP:
"""
for i in range(1,6):
    for j in range(6,11):
        print(str(i)+","+str(j)) #In Python, you can only concatenate (+) strings with strings.
        """

# Task: Ask username from user, append the username in list, ask username from user, check if username present in list, if yes=> print("Login successful") else print login failed

# task: Updated version of previous task. 1 for register 2 for login. 1 ask username and append in list. 2 ask username and check if username is present or not.

# Task: Update this program sing loop
"""
users = []   # empty list to store registered usernames

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:   # Register
            username = input("Enter username to register: ")
            users.append(username)
            print("User registered successfully!")

        case 2:   # Login
            username = input("Enter username to login: ")
            if username in users:
                print("Login successful!")
            else:
                print("Login failed! Username not found.")

        case 3:   # Exit loop
            print("Goodbye!")
            break

        case _:   # Invalid choice
            print("Invalid choice, try again.")"""


#Task :  Make a accounting system where a user logins and he should be able to check the balance, 
# add balance and withdraw balance. Use dictionary, IF…ELSE and loop if needed.




#LOOP in DICT
"""
dict1 = {
    "name" : "Inez",
    "age" : 23,
    "position": "BI Analyst"
}

for i in dict1:
    print(i)   #this will print keys i.e name,age,position
    print(dict1.get(i))""" #this will print values of keys

"""values = dict1.values()   
for i in values:
    print(i) """ #this is another way to get values of keys

