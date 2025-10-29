

#class is a blueprint that create object
"""name = "Inez"
print(type(name))"""

#class keyword is used to define a class.
#Syntax:
"""class class_name:
    Attributes and Methods
"""

#Attributes:
"""the variables defined inside the class"""

#Methods:
"""the functions defined inside the class(lower), (upper)"""

#Object:
"""When creating an object from a class, we need to call a class"""

#example:
"""
#Creating Class
class Dog:
    eyes = 2   #these are attributes
    legs = 4
    def eat(self):  #this is method
        print("Dog is eating")

#Creating object from class
Tommy = Dog()
print(Tommy.eyes)

Pinky = Dog()
print(Pinky.legs)

Leo = Dog()
Leo.eat()
"""

"""class Car:
    wheel = 4
    steering = 1
    doors = 4

    def change_info(self, color, brand, name):
        self.color = color
        self.brand = brand
        self.name = name

Toyota = Car()
Toyota.change_info("Red", "Toyota", "TY!08")
print(Toyota.brand)
print(Toyota.color)
"""

#Object Attributes:
"""The attributes that varies depending to the object"""

#Class Attributes:
"""That doesn't varies according to the object"""

"""
class Student:
    college_name = "Mindrisers Institution"

    def set_info(self,name, id, gender, address):
        self.name = name
        self.id = id
        self.gender = gender
        self.address = address
    def display(self):
        print(self.name,self.id,self.gender,self.address)

Inez = Student()
Inez.set_info("Inez", "7", "Female", "KTM-05")
Inez.display()
print(Inez.college_name)
"""

#OOP pillars:
"""1. ENCAPSULATION 
  Wrap variables(parameters)and methods(functions or behaviour)into single class. Utilities it using objects of specific classes.

Example:
class BankAccount:
    def _init_(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Controlled access

Inez = BankAccount(1000)
Inez.deposit(800)
print(Inez.get_balance())



Functions are made to return value.

2. ABSTRACTION :
Hides complex implementation details from end users...

3. INHERITANCE
child class(sub class) inherit both attributes and behaviors from parent class(super class). 





4. POLYMORPHISM 
i. METHOD OVERRIDING:
    Same function name, same parameters but different behaviour.

ii. METHOD OVERLOADING:
    Same function name, same behaviour but different parameter.

"""


#INHERITANCE:
#example:
"""
class Grandparent:
    name = "Grandparent"
    def gp(self):
        print("This is from Grandparent class")

class Parent(Grandparent):
    name = "Parent"
    def show(self):
        print("This is from Parent class")

class Child(Parent):
    name = "Child"
    def abc(self):
        print("this is from child class")

eden = Child()
eden.show()
eden.abc()
eden.gp()
"""

#MRO stands for Method Resolution Order.
"""It is the order in which Python looks for a method or attribute in a hierarchy of classes during inheritance.

When you call a method on an object, Python doesn't just check that class
it looks through the entire inheritance chain in a specific order.
This order is decided by the MRO."""

#MRO:
"""
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B,C):
    def show(self):
        super().show()
        print("D")

print(D.mro())
obj = D()
obj.show()
"""
#Explanation:
"""
Step 1 — The MRO of class D

Let’s check:

print(D.mro())


You’ll get:

[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


That means the order in which Python will search for methods is:
👉 D → B → C → A → object

🧩 Step 2 — What happens when you call obj.show()?

Let’s trace it step by step:

You called:

obj.show()


So, it first looks inside class D.

In class D, the method is:

def show(self):
    super().show()
    print("D")


First, it calls super().show() → which means go to the next class in MRO after D, which is B.

Then after that call finishes, it prints "D".

🪜 Step 3 — Now inside class B

B.show() runs:

def show(self):
    super().show()
    print("B")


Again, super().show() means go to the next class in MRO after B, which is C.

Then it prints "B".

🪜 Step 4 — Now inside class C

C.show() runs:

def show(self):
    super().show()
    print("C")


Again, super().show() means go to next in MRO after C, which is A.

Then it prints "C".

🪜 Step 5 — Now inside class A

A.show() runs:

def show(self):
    print("A")


Just prints "A", no more super() here.

🧠 Step 6 — Now all methods finish in reverse order

After A.show() finishes, the control goes back up:

Back to C.show() → prints "C"

Then to B.show() → prints "B"

Finally to D.show() → prints "D"

✅ Final Output:
A
C
B
D

💡 Why this order?

Because of MRO (D → B → C → A)
And because super() follows that same order to move to the next class in MRO, not necessarily the “parent” class in the diagram.

✨ In short:

super() doesn’t always mean “call the parent class”.

It means “call the next class in the MRO chain”.

MRO ensures methods are called in a consistent left-to-right order even in multiple inheritance."""


#CONSTRUCTION:
"""The special method in OOP in python that call authomatically when an object is created.
There's only one constructor and i.e. __init__
Constructor always starts and ends with double underscore(__)"""

#example:
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

obj = Student("Inez", 23)
print(obj.name,obj.age)
"""

#Decorators:
"""Decorators are the special function that takes function as an argument and
help to modify the original function w/o changing the og function.
It simply returns the modified version of the function w/o changing the og functions.
Use @ as a prefix in a decorator."""

#Example:
"""
def my_decorator(abc):
    #the decorator always contains a nested function
    def modify_function():
        print("JIHYAA")
        print("25")
        abc()

    return modify_function

@my_decorator
def efg():
    for i in range(5):
        print(i)
efg()  #output: JIHYAA 25 0 1 2 3 4 cause of @my_decorator
"""

#example:
"""class Student:
    def __init__(self,name):
        self.name = name
    
    @staticmethod 
    def display():
        print("Displaying the result....")

obj = Student("Eden")
print(obj.name)
obj.display()
"""

#ENCAPSULATION:
"""the main concept of encapsulation is data(attributes and methods) hiding
we use __(double underscore) before the attribute name to hide the data
the encapsulation data is hidden from outside the class even its own object cannot access
but the hidden data can be accessed from inside the class"""

"""if we need to access the hidden data, we should create a new not hidden attribute/method"""
#example: Attributes
"""class Credential:
    username = "Inez"
    __password = "Inez123"

    password_changed = __password + "***"

c1 = Credential()
print(c1.__password)
print(c1.password_changed)
"""

#example: Method
"""class Credential:
    username = "Inez"
    __password = "Inez123"

    #hidden method aka private
    def __reset_password(self, new_password):
        self.__password = new_password
        return self.__password
    
    #public method
    def abc(self, new_password):
        password = self.__reset_password(new_password)
        print(password)

c1 = Credential()
print(c1.abc("inez222"))"""

#ABSTRACTION:
"""Show only what is needed and hide the implementation details"""

#example:
"""credentials = ["Jitenwa"]

def register():
    username = input("Enter your username: ")
    credentials.append(username)
    print("Register successful !")

def login():
    username = input("Enter your username: ")
    if username in credentials:
        print("Login successful !")
    else:
        print("Invalid Credential !")

choice =int(input("Enter 1 for register, 2 for login: "))

match choice:
    case 1:
        register()
    case 2:
        login()
    case 3:
        exit()
"""

#ABSTRACT METHOD DECORATOR:
"""it tells us that every child class which inherits the abstract class
needs to have same method as of abstract method.
ABC class is always inherited by parent class.
if child class inherits the parent class, the child class must have abstract method."""

"""from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def course(self):
        print("Student chosed course...")

class Ram(Student):
    name = "Ram"

#s1 = Student()
#s1.course()

r1 = Ram()
print(r1.name)
"""

#POLYMORPHISM:
"""One action multiple forms"""
#example:
"""
a = 11
b = 10
print(a+b)

a = "10"
b = "11"
print(a+b)
"""
#same attribute/method but behaves differently according to class

class Bird:
    name = "Bird"

    @staticmethod
    def sound():
        print("Chirping")

class Dog:
    name = "Dog"
    def sound(self):
        print("Barking")

class Cat:
    name = "Cat"
    def sound(self):
        print("Meowing")

obj1 = Bird()
obj2 = Dog()
obj3 = Cat()



