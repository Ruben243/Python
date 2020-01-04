# Funcion que solicita nombre y apellidos y los escribe en un archivo txt
def user():
    nombre = input("Introduzca su nombre ")
    apellido = input("Introduzca su apellido ")
    try:
        f = open("/home/ruben-gfp/log.txt", "a")
        f.write("El nombre de usuario es " + nombre + " y su apellido es " + apellido + '\n')
    except:
        try:
            f = open('/home/ruben-gfp/log.txt', 'a')
            f.write('algo a ido mal')
        finally:
            f.close()


# Funcion que recibe un string y retorna un int,1 si es true o 2 si es false
def acess(x):
    if x == "1234":

        return True
    else:
        return False


# variable de control
dato = " "

# bucle que solicita tu contraseña mientras el usuario no introduzca quit
while dato != "quit":
    passs = input("Introduzca su contraseña ")
    i = acess(passs)
    # si es aceptado permite la introduzcion de datos
    if i:
        print("Aceptado")
        while dato != "quit":
            user()
            dato = input("¿Desea introducir otro usuario Yes/ quit ")
    # si es falso te indica si la contrseña es incorrecta y te pregunta si deseas volver a intentarlo
    else:
        print("rechazado")
        dato = input("¿Quiere volver a intertarlo Yes/Quit ")

print("FIN DEL PROGRAMA")
