#1006.01 Prepare a simple login and register system using File and function only of usernames

# Simple Login and Register System using File and Function

# Function to register new user
"""def register():
    username = input("Enter new username: ")

    # Read all usernames from file
    file = open("file1.txt", "r")
    content = file.read()
    file.close()

    usernames = content.split(",") if content else []  # convert to list

    if username in usernames:
        print("Username already exists! Try another one..")
    else:
        file = open("file1.txt", "a")  # append mode
        if content:  # if file not empty, add comma before new name
            file.write("," + username)
        else:
            file.write(username)
        file.close()
        print("Registration successful!")

# Function to login
def login():
    username = input("Enter username: ")

    file = open("file1.txt", "r")
    content = file.read()
    file.close()

    usernames = content.split(",") if content else []

    if username in usernames:
        print("Login successful! Welcome,", username)
    else:
        print("Login failed!")

# Main Program
while True:
    print("\n---- Simple Login System ----")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
"""

#Login and registration system using both username and password
""""
import json

#For Registration 
def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    dict_credential = {username: password}
    json_credential = json.dumps(dict_credential)  # convert dictionary to JSON string

    file = open("login.txt", "a")  # open file in append mode
    file.write(json_credential + "-")  # store data with a separator
    file.close()  # close file

    print("Registration successful!")


# For Login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file = open("login.txt", "r")  # open file in read mode
    content = file.read()
    file.close()

    credentials = content.split("-")  # split all stored users

    for i in credentials:
        if i != "":  # ignore empty parts
            dict_credential = json.loads(i)  # convert JSON to dictionary
            if username in dict_credential and dict_credential[username] == password:
                print("Login successful! Welcome,", username)
                break
    else:
        print("Login failed! Invalid username or password.")


# Main Menu 
while True:
    print("--- Login & Registration System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")

"""

#for else: same as if else
#the else part is executed if the break is not encountered in for block 
"""
    for i in credentials:
        if i !="":
            dict_credential=json.loads(i)  #loads is opposite to dumbs
            if username in dict_credential and dict_credential.get(username)== password:
                print("Login Successful!")
                break
        else:
            print("Login Failed!")
            continue
        break
"""

import json  # to convert dict to JSON string

# Function to add product 
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    # store data in dict
    product = {"name": name, "price": price, "quantity": quantity}

    try:
        file = open("products.txt", "a") # open file in append mode (add new data)
        file.write(json.dumps(product) + "-") # convert dict to JSON and add "-" as separator
        print("Product added successfully!")
    except Exception as e: # if any error happens during file writing
        print("Error while saving product!")
    finally:
        file.close()  # close file safely


# Function to view all products
def view_products():
    try:
        file = open("products.txt", "r") # open file in read mode
        data = file.read()
    except FileNotFoundError: #if the file doesn't exist 
        print("No products found yet!")
        return #exit the function
    finally:
        try:
            file.close()
        except:
            pass #ignore error if file not open

    products = data.split("-")  # separate each product
    found = False #to check if product exist

    print("--- All Products ---")
    for item in products: # loop through each product record
        if item.strip() != "": # ignore empty strings
            product = json.loads(item)  # convert string to dictionary
            print(f"Name: {product['name']}, Price: Rs.{product['price']}, Quantity: {product['quantity']}") # show details of each product
            found = True # means at least one product is found

    if not found:
        print("No products to show yet!")


# Function to search product 
def search_product():
    search_name = input("Enter product name to search: ")

    try:
        file = open("products.txt", "r")
        data = file.read()
    except FileNotFoundError:
        print("No product data found!")
        return
    finally:
        try:
            file.close()
        except:
            pass

    products = data.split("-") # seperate each product
    found = False  # to check if product found

    for item in products: # go through each product in the lis
        if item.strip() != "": 
            product = json.loads(item) 
            if product["name"].lower() == search_name.lower():  # compare names in lowercase
                # show the product details (name, price, and quantity) from the dictionary
                print(f"Found: {product['name']} | Price: Rs.{product['price']} | Quantity: {product['quantity']}")
                found = True # means that the product has been found
                break #stop searching once found

    if not found:
        print("Product not found !")


# Function to remove product
def remove_product():
    remove_name = input("Enter product name to remove: ")

    try:
        file = open("products.txt", "r")
        data = file.read()
    except FileNotFoundError:
        print("No product data found!")
        return  # stop the function here
    finally:
        try:
            file.close()
        except:
            pass

    products = data.split("-") # split all product records using "-" separator
    updated_products = [] # create an empty list to store remaining products
    removed = False # start by assuming no product is removed

    for item in products:   # check each product one by one
        if item.strip() != "": #ignore empty strings
            product = json.loads(item) 
            if product["name"].lower() != remove_name.lower():  # if this product name is not the one we want to delete
                updated_products.append(product) # keep it by adding to the new list
            else:
                removed = True  # mark that we found and removed the matching product

    if removed: # check if any product was actually removed
        try:
            file = open("products.txt", "w")  # overwrite file with updated data
            for p in updated_products:
                file.write(json.dumps(p) + "-")
            print("Product removed successfully!")
        except Exception as e:
            print("Error while updating file!")
        finally:
            file.close()
    else:
        print("Product not found!")


# Main Menu 
while True:
    print("--- E-Commerce Product Management ---")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Remove Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        remove_product()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
