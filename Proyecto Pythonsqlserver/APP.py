import Persona
import pyodbc

persona = Persona.Persona()
op=""
while op != "e":
    print('1.Obtener')
    print('2.Crear')
    print('3.Editar')
    print('4.Eliminar')
    print("e:Salir")

    op = input("Selecciona una opcion: ")
    if op == "1":
        persona.Obtener()
    elif op == "2":
        nombre = input("Cual es su nombre?: ")
        pais = input("Cual es su pais?: ")
        persona.Add(nombre, pais)

    elif op == "3":
        persona.Obtener()
        id = input("¿Cual registro quieres editar?: ")
        nombre = input("Cual es su nombre?: ")
        pais = input("Cual es su pais?: ")
        persona.Edit(nombre, pais, id)

    elif op == "4":
        persona.Obtener()
        id = input("¿Cual registro quieres eliminar?: ")
        persona.Delete(id)

    elif op== "e":
        print("Fin del programa")

    else:
        print("Opcion invalida")
