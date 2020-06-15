from OBjetos.Persona import Persona


class Alumno(Persona):
    __notas = ""
    __curso = ""

    def __init__(self, nombre, apellido, dni, notas, curso):
        self.curso = curso
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.__notas = notas
        Persona(nombre, apellido, dni)

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, nuevanota):
        self.__notas = nuevanota

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, nuevocurso):
        self.__curso = nuevocurso

    def __str__(self):
        return Persona.__str__(self) + " con las nota " + self.notas + " y estoy en el curso " + self.curso
