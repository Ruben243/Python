def imprimir_rombos(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


imprimir_rombos(5)

print("\n************************************************************\n")


def cuadrado(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * rows)
        else:
            print("*" + " " * (rows - 2) + "*")


cuadrado(5)

print("\n************************************************************\n")


def triangulo_invertido(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

triangulo_invertido(5)