"""
Manager biblioteca de libros - Permite prestar, devolver, buscar y listar libros en la biblioteca.
"""

import book
from library import Library

book_1 = book.PaperBook(
    "Cien Años de Soledad", "Gabriel García Márquez", 1967, "978-3-16-148410-0", True
)
book_2 = book.PaperBook("1984", "George Orwell", 1949, "978-0-452-28423-4", False)
book_3 = book.PaperBook(
    "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "978-84-376-0494-7", True
)


library = Library("Biblioteca Central")

library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)

print(library.list_books_available())
