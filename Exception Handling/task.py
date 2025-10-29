#1008.01  Update Login and registration system using both username and password
"""
import json  # import json module to convert dict to string and viceversa

#Registration Function 
def register():
    username = input("Enter new username: ")  
    password = input("Enter new password: ") 

    dict_credential = {username: password}  # create a dictionary for this user
    json_credential = json.dumps(dict_credential)  # convert dictionary to JSON string

    try:
        file = open("login.txt", "a")  # open file in append mode to add user
        file.write(json_credential + "-")  # write user data with a separator
    except Exception as e:  # if any error occurs while writing
        print("An error occurred while saving:", e)
    finally:
        file.close()  # make sure the file is always closed

    print("Registration successful!")  


# Login Function
def login():
    username = input("Enter your username: ") 
    password = input("Enter your password: ") 

    try:
        file = open("login.txt", "r")  # open file in read mode to get user data
        content = file.read()  # read all content from file
    except FileNotFoundError:  # if file does not exist
        print("No users registered yet! Please register first.")
        return  # exit the function
    except Exception as e:  # any other error while reading
        print("An error occurred while reading the file:", e)
        return  # exit the function
    finally:
        try:
            file.close()  # ensure file is closed
        except:
            pass  # if file was never opened, ignore

    credentials = content.split("-")  # split all users using "-" as separator

    for i in credentials:  # check each stored user
        if i != "":  # ignore empty strings
            dict_credential = json.loads(i)  # convert JSON string back to dictionary
            if username in dict_credential and dict_credential[username] == password:
                print("Login successful! Welcome,", username)  # successful login
                break  # exit the loop
    else:  # executed only if no break occurred (login failed)
        print("Login failed!")


# Main Menu Loop
while True:  # keep showing menu until user exits
    print("--- Login & Registration System ---")  # menu header
    print("1. Register") 
    print("2. Login")    
    print("3. Exit")     

    choice = input("Enter your choice: ")  

    if choice == "1":
        register()  # call registration function
    elif choice == "2":
        login()  # call login function
    elif choice == "3":
        print("Goodbye!")  # exit message
        break  # stop the menu loop
    else:
        print("Invalid choice! ")  # invalid input
"""

#1008.02 Updated Simple Calculator:
"""
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:  # handle division by zero
        return (e)

# Main calculator loop
while True:
    print("---Simple Calculator---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting Calculator...")
        break

    try:
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

    except ValueError as e:  # handle invalid number input
        print(e)
"""
#1010.01 Prepare a ATM system that includes register and login system and the user is able to add balance, check balance, withdraw balance. Use files.

import json #to convert dict to JSON string and vice versa

#Registration Function:
def registration():
    username = input("Enter new username: ") #get username
    password = input("Enter new password: ") #get password 
    balance = 0  #new users start with 0 balance

    user_credential = {username: {"password":password, "balance":balance}} # dictionary with password and balance
    json_data = json.dumps(user_credential) #convert dict to JSOn string

    try:
        file = open("login.txt", "a")  # open file in append mode
        file.write(json_data + "-")  # write user data with separator
        print("Registration successful!")

    except Exception as e:  # catch any writing error
        print("An error occurred while saving.")
    finally:
        file.close()  # close file safely


#Login Function:
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        file = open("login.txt", "r")  # read file with user data
        content = file.read()
    except FileNotFoundError: #this block runs if the file does not exist yet
        print("No users registered yet! Please register first.")
        return
    except Exception as e: #if any other unexpected errors
        print("An error occurred while reading the file.")
        return  # Exit the function on error
    finally: #runs no matter what
        try:
            file.close()
        except:
            pass #if file was not opened, ignore the error

    users = content.split("-")  # split all stored users
    all_users = {}

    for i in users: #go through each user in the list
        if i != "": #Skip empty strings ("-")
            user_dict = json.loads(i) # convert each JSON string back to dictionary and merge
            all_users.update(user_dict)
    
    # check login credentials
    #check if username and password is correct, both condition must be true
    if username in all_users and all_users[username]["password"] == password:
        print("Login successful! Welcome,", username)
        atm_menu(username, all_users)  # go to ATM menu
    else:
        print("Login failed! Wrong Credential !!")


#ATM MENU:
def atm_menu(username, all_users):
    while True: #loop until user logout
        print("--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Enter choice: ")

        if  choice == "1":  # check balance
            print("Your balance is:", all_users[username]["balance"])  #all_users = dictionary (username is nested dict)

        elif choice == "2":  # deposit money
            try:
                amount = float(input("Enter deposit amount: "))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue # go back to ATM menu
                elif amount == 0:
                    print("Deposit amount can't be ZERO !")
                    continue
            except ValueError:  # runs if user enters a non-number (like text)
                print("Invalid input! Enter a number.")
                continue

            all_users[username]["balance"] += amount # add deposit amount to user’s balance
            print("Deposit successful!")

        elif choice == "3":  # withdraw money
            try:
                amount = float(input("Enter withdraw amount: "))
                if amount <= 0:
                    print("Amount cannot be negative or Zero !")
                    continue
            except ValueError:
                print("Invalid input! Enter a number.")
                continue

            if amount <= all_users[username]["balance"]:  # check if user has enough money
                all_users[username]["balance"] -= amount # subtract the withdrawn amount from balance
                print("Withdrawal successful!")
            else:
                print("Insufficient balance!")

        elif choice == "4":  # logout
            print("Logged out!")
            break
        else:
            print("Invalid choice!")

        # save updated data back to file
        try:
            file = open("login.txt", "w")  # overwrite file with updated data
            for user, data in all_users.items():
                file.write(json.dumps({user: data}) + "-")
        except Exception as e:
            print("Error saving file.")
        finally:
            file.close()


# --- Main Menu ---
while True:
    print("--- Login & Registration System with ATM ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        registration()  # call registration
    elif main_choice == "2":
        login()  # call login
    elif main_choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
