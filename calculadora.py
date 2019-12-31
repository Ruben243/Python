# Funcion que suma dos numeros,muestra el resultado y lo escribe en un archivo
def sumar(x, y):
    try:
        try:
            print(x + y)
            f = open("/home/ruben-gfp/log.txt", "a")
            f.write("La suma de " + str(x) + " y " + str(y) + " es " + str(x + y) + '\n')


        except:
            print("error")
    finally:
        f.close()


# Funcion que resta dos numeros,muestra el resultado y lo escribe en un archivo
def resta(x, y):
    try:
        try:
            print(x - y)
            f = open("/home/ruben-gfp/log.txt", "a")
            f.write("La rest de " + str(x) + " y " + str(y) + " es " + str(x - y) + '\n')


        except:
            print("error")
    finally:
        f.close()


# Funcion que divide dos numeros,muestra el resultado y lo escribe en un archivo
def divide(x, y):
    try:
        print(x / y)
        f = open("/home/ruben-gfp/log.txt", "a")
        f.write("La division de " + str(x) + " y " + str(y) + " es " + str(x / y) + '\n')
    except ZeroDivisionError:
        try:
            f = open('/home/ruben-gfp/log.txt', 'a')
            f.write('error,ningun numero puede ser 0' + '\n')
        finally:
            f.close()


# Funcion que multiplica dos numeros,muestra el resultado y lo escribe en un archivo
def multiplica(x, y):
    try:

        print(x * y)
        f = open("/home/ruben-gfp/log.txt", "a")
        f.write("El producto de " + str(x) + " y " + str(y) + " es " + str(x * y) + '\n')
    except:
        try:
            f = open('/home/ruben-gfp/log.txt', 'a')
            f.write('algo a ido mal')
        finally:
            f.close()


# variable de control del bucle

opcion = ' '

# Bucle while que se ejecuta hasta que el usuario introduce Q
while opcion != 'Q':
    print('Elija una opcion: ')
    print('suma')
    print('resta')
    print('division')
    print('multiplicacion')
    print('Q salir')
    opcion = input(':')

    if opcion == "suma":
        try:
            numero1 = float(input("Primer numero: "))
            numero2 = float(input("segundo  numero: "))
        except:
            print('Error')

        sumar(numero1, numero2)

    elif opcion == 'resta':
        try:
            numero1 = float(input("Primer numero: "))
            numero2 = float(input("segundo  numero: "))
        except:
            print('Error')
        resta(numero1, numero2)

    elif opcion == 'division':
        try:
            numero1 = float(input("Primer numero: "))
            numero2 = float(input("segundo  numero: "))
        except:
            print('Error')
        divide(numero1, numero2)

    elif opcion == 'multiplicacion':
        try:
            numero1 = float(input("Primer numero: "))
            numero2 = float(input("segundo  numero: "))
        except:
            print('Error')
        multiplica(numero1, numero2)

    elif opcion == 'Q':
        break

    else:
        print('Opcion erronea')

print('FIN DEL PROGRAMA')
