#Exception Handling
#example:
"""
num1 = 9
num2 = 0
div = num1/num2
print(div)   #gives error as cannot be divide by zero.
"""
#Try Except Finally:
#try:
"""In try block, we write the part of code that may raise an error"""
#except:
"""In except block, we write the code that is to be executed if error occurs in try block"""
#finally:
"""The code of finally block runs even if error occurs or not. Basically, it always gets executed"""
#example
"""
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("An error occured as number cannot be divide by zero.")
except ValueError:
    print("An error occured due to insertation of different data tye.")
finally:
    print("This will be printed anyways")
"""

#another way:
"""
except ZeroDivisionError as e:
print(e) """  #print the error that shows durings ZeroDivisionError

#another example:
"""
list = [1,2,3,4,5]
try:
    print(list[5])
except IndexError as e:
    print(e) #shows list index out of range

"""
#another way:
"""
try:
    file = open("abc.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    file = open("abc.txt", "w")
    file.close()
"""



