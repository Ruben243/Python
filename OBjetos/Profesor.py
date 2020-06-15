from .Persona import Persona


class Profesor(Persona):
    __materia = ""
    __cargo = ""

    def __init__(self, nombre, apellido, dni, materia, cargo):
        self.cargo = cargo
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.__materia = materia
        Persona(nombre, apellido, dni)

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, nuevamateria):
        self.__materia = nuevamateria

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, nuevocargo):
        self.__cargo = nuevocargo

    def __str__(self):
        return Persona.__str__(self) + " imparto la materia " + self.materia + " y tengo el cargo de " + self.cargo
