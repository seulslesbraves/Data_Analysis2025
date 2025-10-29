#Python File Handling:
"""the flow for file handling are:
    Open the file => open(file_path, open_mode)
    Perform the operation
    Close the file"""

#Opening the File Modes:
"""
"r" → Read (default, file must exist)

"w" → Write (creates new or overwrites existing) #we can only write either in string or JSON on file

"a" → Append (add at end of file)

"b" → Binary (images, PDFs, etc.)

"x" → Create (error if file exists)
"""

#example:
#for read:
"""file= open("file1.txt","r")
content= file.read()
file.close()  #we must close the file so that we can reuse unless it will overwrites

print(content)"""

#for write:
"""file= open("file1.txt","w")
file.write("jihyaa")
file.close() 

"""

#for append:
"""file= open("file1.txt","a")
file.write("Inez")
file.close()  
"""

#split(): splits the words from a unique char and retyrns a list of words
#by default, split() method splits the string by space
"""
name= "INez Koyee Rai"
list_of_word = name.split()
print(list_of_word)
"""

#example:
"""username= ["Inez", "Jihyaa", "Hermez", "Eden"]
file= open("file1.txt", "a")
file.write(str(username))
file.close()

file= open("file1.txt", "r")
content= file.read()
file.close()

print(content)
username= content.split(",")
print(username)

if "Eden" in username:
    print("Login Successful")
else:
    print("Login failed")
"""
