#1. Create a dictionary of usernames and passwords, extract all the usernames from the dictionary 
# and input username from the user and check if the username is present in the extracted list of usernames:
"""
users = {
    "inez" : "inez123",
    "jihyaa" : "jihyaa123",
    "hermez" : "hermez123",
    "eden" : "eden123"
}

usernames = users.keys()

users_input = input("Enter a username: ")

if users_input in usernames:
    print("Username Found")
else:
    print("Username Not Found")
"""

#2. Write a program to check if a number is positive or negative.
"""
num = float(input("Enter a number: "))

# Use IF-ELSE to check the number
if num > 0:
    print(f"{num} is positive.") #if num = 5, f"{num} is positive." becomes "5 is positive."
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

"""

#3. Write a program to check whether a number is even or odd.

"""num= float(input("Enter a number: "))

# check if the num is divisible by 2
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")"""

#4. Write a program to check whether a person is eligible to vote (age ≥ 18).
"""
age= int(input("Enter your age: "))

if age >= 18:
    print("Eligible to VOTE")
else:
    print("Not Eligible to VOTE")
    """

#5. Write a program to compare two numbers and print the larger one.
"""num1= int(input("Enter a number: "))
num2= int(input("Enter another number: "))

if num1 > num2:
    print(f"The larger number is {num1}")
elif num2 > num1:
    print(f"The larger number is {num2}")
else:
    print("Both numbers are equal")"""

#6. Write a program to check if a number is divisible by 5.
"""num = int(input("Enter a number: "))

if num % 5 == 0:
    print(f"{num} is divisible by 5 ")
else:
    print(f"{num} is not divisible by 5 ")"""

#7. Write a program to check whether a number is positive, negative, or zero
"""
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("The number is Zero")"""

#8. Write a program to assign grades (A, B, C, D, F) based on marks entered by the user
"""num= float(input("Enter a number: "))

if num >= 80:
    print("A grade")
elif num >=70 and num < 80:
    print("B grade")
elif num >=60 and num < 70:
    print("C grade")
elif num >=50 and num < 60:
    print("D grade")
elif num >=40 and num < 50:
    print("E grade")
else:
    print("F grade")"""

#9. Write a program to check whether a character entered is a vowel or consonant.
"""character = input("Enter a character: ")

if character in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")"""

#10. Write a program to find the largest among three numbers.
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the largest
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

if num1 == num2 == num3:
    print("All three numbers are equal")
else:
    print(f"The largest among three numbers is {largest}")"""

#11. Write a program to check whether a number is divisible by both 3 and 5.
"""
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by both 3 and 5")"""

#12. Write a program to check whether a given number is a two-digit number.
"""
num = int(input("Enter a number: "))

if num >= 10 and num<=99: 
    print(f"{num} is a two-digit number")
else:
    print(f"{num} is not a two-digit number")"""

#13. Write a program to check whether a character is uppercase, lowercase, digit, or special character.
"""
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")"""

#14. Write a program to determine if a person can donate blood (age ≥ 18 and weight ≥ 50).
"""
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

if age >= 18 and weight >= 50:
    print("You can donate the blood")
else:
    print("Sorry ! You can't donate the blood")"""

#15. Write a program to check whether a triangle is equilateral, isosceles, or scalene.





#16. Write a program to calculate electricity bill based on units:
# up to 100 units → Rs. 5/unit
# 101–200 units → Rs. 7/unit
# above 200 units → Rs. 10/unit
"""
units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print(f"Total Electricity Bill = Rs. {bill}")
"""


#17. Write a program to check whether a student passed or failed (marks ≥ 40 = pass).
# Program to check pass or fail
"""
marks = float(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")"""

#18. Write a program to determine ticket price:
"""age < 12 → Rs. 100

age 12–18 → Rs. 150

age > 18 → Rs. 200"""

#Write a program to check whether a person is eligible for a driving license (age ≥ 18).
# Write a program to check whether a number is prime or not using if-else.


#0925.1 Calculator using function, loop and match
"""
def calculator():   # it define a function called calculator
    while True:   # Loop will keep running until user exits
        num1 = int(input("Enter first number: "))   
        num2 = int(input("Enter second number: ")) 

        # Show menu
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = int(input("Enter your choice: "))   # Ask user what operation they want i.e add,sub,etc

        # Use match-case for different choices
        match choice:
            case 1:   # If user entered 1
                print("Result =", num1 + num2)   # Perform addition
            case 2:  
                print("Result =", num1 - num2)  
            case 3:   
                print("Result =", num1 * num2)  
            case 4:   
                if num2 != 0:   # Prevent division by zero error
                    print("Result =", num1 / num2)   # Perform division
                else:
                    print("Error: Division by zero!")   # Show error if num2 = 0
            case 5:   # If user entered 5
                print("Exiting Calculator...")   # Exit message
                break   # Break the while loop and program ends
            case _:   # If user enters something else
                print("Invalid choice! Try again.")   # Show invalid message

calculator() # Call the function to run the calculator
"""



#0925.2 Accounting System with functions and loop
"""
# Dictionary to store username and their balance
accounts = {
    "inez": 100000, 
    "jihyaa": 500000,
    "hermez": 90000,
    "eden": 80000
}

# Function to check balance
def check_balance(username):
    print("Your balance is:", accounts[username])

# Function to deposit
def deposit(username):
    amount = int(input("Enter deposit amount: "))
    accounts[username] += amount   # add amount to balance
    print("Deposit successful!")

# Function to withdraw 
def withdraw(username):
    amount = int(input("Enter withdraw amount: "))
    if amount <= accounts[username]:   # only allow if balance is enough
        accounts[username] -= amount   # subtract from balance
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

while True:   # outer loop for login ()
    username = input("Enter username (or 'exit' to quit): ")

    if username == "exit":
        print("Goodbye!")
        break   # stop the program

    if username in accounts:   # if username exists (login success)
        print(f"Welcome {username}!")

        while True:   # inner loop for menu
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                check_balance(username)   # call balance function
            elif choice == "2":
                deposit(username)        
            elif choice == "3":
                withdraw(username)        
            elif choice == "4":
                print("Logged out!")
                break   # back to login screen
            else:
                print("Invalid choice! Try again.")
    else:
        print("Login failed! Username not found.")
"""


#1006.01 Make a calculator program using Python functions and loop
"""
# Function to add two numbers
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error"

# Main calculator loop
while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting Calculator...")
        break

    # Ask for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform operation based on choice
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Try again.")
"""

#1006.02 Print a multiplication table of the number that is input by the user

"""
num = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication Table of {num}:")
# Loop from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
"""

#1006.03 Check if the given number is even or odd
"""
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
"""

#1006.04 Check if a given number is palindrome or not
"""
num = input("Enter atleast three number: ")

# Check if the number is same forwards and backwards
if num == num[::-1]:  #num[::-1] reverse the num (:: <= python slicing)
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
"""

#1006.05 Make a simple login system without registration using functions
"""
# Dictionary to store predefined usernames and their passwords
users = {
    "inez": "inez123",
    "jihyaa": "jihyaa123",
    "hermez": "hermez123",
    "eden": "eden123"
}

# Function to check login validity
def login(username, password):
    if username in users:  # Check if the entered username exists 
        return users[username] == password # Compare entered password with stored password, return True if it matches
    return False  # If username not found, return False


# Main program loop that runs continuously until user types exit
while True:
    print("---- Login System ----")
    
    # Ask user for their username
    username = input("Enter username (or 'exit' to quit): ")

    # If user types 'exit', end the program
    if username == "exit":
        print("Goodbye!")
        break   # Breaks out of the while loop to stop the program

    # Check if the entered username exists in the 'users' dictionary
    if username not in users:
        print("Username not found!") 
        continue   # Skip the rest of this loop and go back to ask username again
                   #continue instead of break as break stop the program

    # Ask for password only if username exists
    password = input("Enter password: ")

    # Call the login function to verify credentials
    if login(username, password):
        print("Login successful! Welcome,", username)  # If function returns True
    else:
        print("Login failed!")  # If function returns False (wrong password)
"""

#1006.06 Make a login system using registration using function
"""
# Dictionary to store predefined usernames and their passwords
users = {
    "inez": "inez123",
    "jihyaa": "jihyaa123",
    "hermez": "hermez123",
    "eden": "eden123"
}

# Function to check login validity
def login(username, password):
    if username in users:  # Check if the entered username exists 
        return users[username] == password  # Compare entered password with stored one
    return False  # If username not found, return False

# Function to register new users
def register():
    username = input("Enter new username: ")

    if username in users:  # Check if username already exists
        print("Username already exists! Try another one..")
        return  # Stop registration process

    password = input("Enter new password: ")
    users[username] = password  # Add new username and password to dictionary
    print("Registration successful! You can now log in.")

# Main program loop that runs continuously until user types exit
while True:
    print("---- Login System ----")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  # Login option
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Call the login function to verify credentials
        if login(username, password):
            print("Login successful! Welcome,", username)
        else:
            print("Login failed! Invalid username or password.")

    elif choice == "2":  # Register option
        register()  # Call the registration function

    elif choice == "3":  # Exit option
        print("Goodbye!")
        break  # Stop the loop and end program

    else:
        print("Invalid choice! Try again.")  # For invalid inputs
"""

#1006.07 Print all the even numbers in a list of numbers
"""
numbers = [2, 5, 8, 11, 14, 17, 20]

# Loop through each number in the list
for num in numbers:
    if num % 2 == 0:   # Check if number is even
        print(num)
"""

