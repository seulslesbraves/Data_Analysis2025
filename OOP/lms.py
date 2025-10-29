#LMS: Library Management System
#1. Add books,update,remove, and delete, search
#2. Types of books: Physical and E-book

"""class LMS:
    books = []

    def add_book(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        self.books.append(self.name)

    def update_book(self, name, new_name):
        if name in self.books:
            index = self.books.index(name)
            self.books.pop(index)
            self.books.insert(index, new_name)
            print(f"{name} Book name updated to {new_name}")
        else:
            print("Book Not Found !!")
    def remove_book(self, name):
        if name in self.books:
            index = self.books.index(name)
            self.books.pop(index)
            print(f"{name} book has been removed !!")
        else:
            print("Book not found !!")
    def view_book(self):
        for book in self.books:
            print(book)

while True:
    choice = int(input("Enter 1 for adding book, 2 for updating book, 3 for removing book, 4 for viewing book,5 for exit: "))

    library1 = LMS()
    match choice:
        case 1:
         name = input("Enter book name: ")
         author = input("Enter author name: ")
         pages = input("Enter book pages: ")         
         library1.add_book(name, author, pages)
         print("Book added successfully !!")

        case 2:
          name = input("Enter book name that you want to update: ")
          new_name = input("Enter new book name to update: ")
          library1.update_book(name, new_name)
        case 3:
            name = input("Enter a book name to remove: ")
            library1.remove_book(name)
        case 4:
            library1.view_book()
        case 5:
            print("Goodbye !!")
            break
        case _:
            print("Invalid input !!")
 """

