#Procedural programming






#DRY: Don't Repeat Yourself

#Code reusability: increase
#Code optimization: increase

#def keyword is used to define a function
#SYntax:
"""def function_name (parameters):
    code to be executed"""

#only by defining the functions, the func doesnt works
#we should call a function
#to call function, we use function_name(arguments)

#example:
"""a= 19
b= 11
def addition():   #programmer defined functions
    print(a+b)

addition()"""  

"""print()
input()
int()
float()"""   #build-in functions


#return keywords return the values
#when return keywords returns something, we need variable to store the returned value
"""a= 19
b= 11
def addition():  
    return (a+b)

sum = addition()
print(sum)

"""

#Global variable:
"""the variable that is defined outside the function"""
#example: a and b is global variable
"""a = 10   
   b = 11
   def function ():
      print(a+b)"""

#Local variable:
"""the variable that is defined inside the function"""
#example: c is local variable
"""a = 10   
   b = 11
   def function ():
      print(a+b)
      c= 22
      print(c)"""


#Arguments: 
"""the values that pass to a function during the function call"""
#Parameters:
"""the varaiable that is used to store arguments"""

#example:
"""def greet(name):   # 'name' is an parameter , parameters are always local variable
    print(f"Hello, {name}!")

greet("Inez")  #"inez" is an arguments
"""

#Arguments: there are two types of arguments:
#Positional Arguments (args): single value arguments
#example:
"""def display(name, age):
    print(f"Name: {name}, age:{age}")

display("inez", 29)

"""

#Keyword Arguments (kwargs): arguments those are in key-value pair
#example:



#Lambda functions:
"""mini function that you write in one line"""
"""lambda keyword is used to define a lambda function"""
#normal operation:
"""x= 10
y= 2
def add(x,y):
    print(x+y)
add()
"""

#lambda example:
"""add= lambda x,y: x+y
print(add(10,2))"""


#MAP:
"""function that takes a function and group data type
as an argument and perform our condition to each
element of the group data"""
#example:
"""list1= [1,2,3,4]
square= list(map(lambda x: x**2,list1))
print(square)"""

#Filter function:
"""filter elements based on a condition"""
#example:
"""number= [1,2,3,4]
even_num = list(filter(lambda x: x % 2 ==0, number))
print(even_num)
"""

#Reduce:
"""combines all element of a list into a single value
it also takes function and group data type as an argument 
and reduces the group data type elements into a single value
according to our condition"""
#example:
"""from functools import reduce
numbers = [5, 6, 7, 8]
sum= reduce(lambda x,y : x+y, numbers)
print(sum)"""   #cant type-cast in list as its combines into single value


#ZIP Function:
"""combines multiple lists element-wise"""
#example:
"""names= ['inez', 'jihya']
age= [23, 25]
combined= list(zip(names,age))
print(combined)  #output [('inez', 23), ('jihya', 25)]
"""



