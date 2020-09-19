# Class Library
# Layers of abstraction => display the available book, to lend a book, to add a book

# Class Students
# Layers of abstraction => request book, return book


class Library:
    
    def __init__(self,listOfBooks):
        self.availableBooks=listOfBooks

    def displayAvailableBook(self):
        print()
        print("Available Books: -")
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book") 
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry book is not available :(")

    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned a book, Thank you :)")


class Student:
    def requestBook(self):
        print("Enter the name of the book you want to like borrow:")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning:")
        self.book=input()
        return self.book

library = Library(['OS', 'DBMS', 'JS', 'Web Tech'])
student = Student()

while True:
    print()
    print("Enter 1: Diplay Available Books")
    print("Enter 2: Borrow a Book")
    print("Enter 3: Return a Book")
    print("Enter 4: Exit")

    userChoice=int(input())
    if userChoice is 1:
        library.displayAvailableBook()
    elif userChoice is 2:
        requestedBook=student.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook=student.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()
