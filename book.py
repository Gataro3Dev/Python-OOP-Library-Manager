"""
Módulo que define clases para representar libros en una biblioteca.
"""

from typing import Protocol


class bookProtocol(Protocol):
    def lend_book(self) -> str:
        """
        Método para prestar un libro.

        :param self: Description
        :return: Mensaje de confirmación del préstamo
        :rtype: str
        """
        ...

    def return_it_book(self) -> str:
        """
        Método para devolver un libro.

        :param self: Description
        :return: Mensaje de confirmación de la devolución
        :rtype: str
        """
        ...

    def popular_book(self) -> bool:
        """
        Método para verificar si un libro es popular.

        :param self: Description
        :return: True si el libro es popular, False en caso contrario
        :rtype: bool
        """
        ...


class Book:
    """
    Clase que representa un libro en la biblioteca.
    """

    def __init__(self, titulo, autor, anio, isbn, available):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.isbn = isbn
        self.available = available
        self.__lended = 0

    def __str__(self):
        return f"{self.titulo} by {self.autor} ({self.anio}) - ISBN: {self.isbn} - {'Disponible' if self.available else 'No disponible'}"

    def lend_book(self):
        if self.available:
            self.available = False
            self.__lended += 1
            return f"Has prestado '{self.titulo}' exitosamente."
        else:
            return f"Lo siento, '{self.titulo}' no está disponible en este momento."

    def return_it_book(self):
        if not self.available:
            self.available = True
            return f"Has devuelto '{self.titulo}' exitosamente."

    def popular_book(self):
        return self.__lended > 5

    def getter_lended(self):
        return self.__lended

    def setter_lended(self, value: int):
        if value >= 0:
            self.__lended = value
        else:
            raise ValueError("El número debe ser mayor a 0.")


class PaperBook(Book):  # type: ignore
    """
    Clase que representa un libro físico en la biblioteca.
    """

    def loan_duration(self):
        return "7 días"  # Días de préstamo para libros físicos


class EBook(Book):  # type: ignore
    """
    Clase que representa un libro electrónico en la biblioteca.
    """

    def loan_duration(self):
        return "14 días"  # Días de préstamo para libros electrónicos
