# Per creare classi astratte:

from abc import ABC, abstractmethod

# Exercise 1: Creating an Abstract Class with Abstract Methods

# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

class Shape(ABC):  # per creare una classe astratta devo fare così 

    @abstractmethod # per creare un metodo astratto devo fare così
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, raggio: float):
        self.raggio = raggio

    def area(self) -> float:
        area = 3.14 * (self.raggio ** 2)
        return area
    
    def perimeter(self) -> float:
        perimeter = 3.14 * self.raggio * 2
        return perimeter

class Rectangle(Shape):
    def __init__(self, base: float, altezza: float) -> float:
        self.base = base
        self.altezza = altezza

    def area(self) -> float:
        area = self.base * self.altezza
        return area
    
    def perimeter(self) -> float:
        perimeter = (self.base + self.altezza) * 2
        return perimeter


# Exercise 2: Implementing Static Methods

# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.

# STATIC METHOD

class MathOperations:

    @staticmethod
    def add( num1: int, num2: int) -> int:
        return num1 + num2
    
    @staticmethod
    def multiply (num1: int, num2: int) -> int:
        return num1 * num2
    
somma = staticmethod(MathOperations.add)
moltiplicazione = staticmethod(MathOperations.multiply)
#print(somma(2,5))
#print(moltiplicazione(2,5))


# Exercise 3: Library Management System 

# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:

#    - __str__ method to return a string representation of the book.

#    - @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
#     It means that you must use the class reference cls to create a new object of the Book class using a string.

# Example: 

# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 

# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:

#     borrow_book(book) to add a book to the borrowed_books list.

#     return_book(book) to remove a book from the borrowed_books list.

#     __str__ method to return a string representation of the member.

#     @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

# Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
# The library class must contain the following methods:

#     add_book(book) to add a book to the library and increment total_books.

#     remove_book(book) to remove a book from the library and decrement total_books.

#     register_member(member) to add a member to the library.

#     lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

#     __str__ method to return a string representation of the library with the list of books and members.

#     @classmethod library_statistics(cls) to print the total number of books.

# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. Register members and add books to the library. Lend books to members 
# and display the state of the library before and after lending.

class Book:
    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"{self.title}, {self.author}, {self.isbn}"

    @classmethod
    def from_string(cls, book_string: str) -> object:
        title, author, isbn=book_string.split(', ')
        return Book(title, author, int(isbn))

book = Book("La Divina Commedia", "D. Alighieri", 999000666)
divina_commedia: Book = Book.from_string(book)
