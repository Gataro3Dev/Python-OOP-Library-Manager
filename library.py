"""
Módulo que define la clase Biblioteca y sus funcionalidades.
"""

from book import Book


class Library:
    """
    Clase que representa la biblioteca.
    """

    def __init__(self, name) -> None:
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def list_books_available(self):
        return {book.titulo for book in self.books if book.available}

    def find_book_by_title(self, titulo: str):
        for book in self.books:
            if book.titulo == titulo:
                return book
        return None
