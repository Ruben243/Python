class Persona:
    __nombre = ""
    __apellido = ""
    __dni = ""

    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        print("Se a creado una persona", {self.__nombre}, {self.__apellido}, " y ", {self.__dni})

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevonombre):
        self.__nombre = nuevonombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevoapellido):
        self.__apellido = nuevoapellido

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevodni):
        self.__dni = nuevodni

    def __str__(self):
        return "Me llamo " + self.nombre + " con apellido " + self.apellido + " y mi dni es " + self.dni
