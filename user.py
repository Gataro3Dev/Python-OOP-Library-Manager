"""
Clase usuario para el sistema de gestión de biblioteca.
"""

from typing import Protocol


class requestProtocol(Protocol):
    def book_loaned(self, titulo: str) -> str:
        """
        Método para solicitar el préstamo de un libro.

        :param self: Description
        :param titulo: Título del libro a solicitar
        :type titulo: str
        :return: Mensaje de confirmación del préstamo
        :rtype: str
        """
        ...


class User:
    def __init__(self, name, id_user):
        self.name = name
        self.id_user = id_user
        self.book_lended = []

    def __str__(self):
        return f"Usuario: {self.name}, ID: {self.id_user}."

    def book_loaned(self, titulo):
        return f"Se ha solicitado el libro '{titulo}'."


class Student(User):
    def __init__(self, name, id_user, career):
        super().__init__(name, id_user)
        self.career = career
        self.Limit_book_lended = 5

    def __str__(self):
        return f"Estudiante: {self.name}, ID: {self.id_user}, Carrera: {self.career}."

    def book_loaned(self, titulo):
        if len(self.book_lended) < self.Limit_book_lended:
            self.book_lended.append(titulo)
            return (
                f"Se autorizo el prestamo de '{titulo}' para el estudiante {self.name}."
            )
        else:
            return (
                f"El estudiante {self.name} ha alcanzado el límite de libros prestados."
            )

    def return_book(self, titulo):
        if titulo in self.book_lended:
            self.book_lended.remove(titulo)
            return f"El estudiante {self.name} ha devuelto el libro '{titulo}'."
        else:
            return f"El estudiante {self.name} no tiene prestado el libro '{titulo}'."


class Teacher(User):
    def __init__(self, name, id_user):
        super().__init__(name, id_user)
        self.Limit_book_lended = None

    def __str__(self):
        return f"Profesor: {self.name}, ID: {self.id_user}."

    def book_loaned(self, titulo):
        self.book_lended.append(titulo)
        return f"Se autorizo el prestamo de '{titulo}' para el profesor {self.name}."

    def return_book(self, titulo):
        if titulo in self.book_lended:
            self.book_lended.remove(titulo)
            return f"El profesor {self.name} ha devuelto el libro '{titulo}'."
        else:
            return f"El profesor {self.name} no tiene prestado el libro '{titulo}'."
