from turtle import *  # Importa todas las funciones de la biblioteca de gráficos Turtle.
from math import *  # Importa todas las funciones de la biblioteca de matemáticas.

speed(0)  # Establece la velocidad de dibujo al máximo.
bgcolor("black")  # Establece el color de fondo en negro.
goto(0, -40)  # Mueve la tortuga a la posición inicial.
# dibuja una serie de círculos interconectados con radios y colores variables. Esto crea el patrón principal del #espirografo.
for i in range(16):
    # dibuja círculos más pequeños dentro de cada círculo principal.
    for j in range(18):
        color("#FF007F")  # establece el color del lápiz en una tonalidad de naranja.
        rt(90)  # rota la tortuga 90 grados para comenzar a dibujar el círculo.
        circle(150 - j * 6, 90)  # dibuja un cuarto de círculo con un radio decreciente.
        lt(
            90
        )  # rota la tortuga 90 grados para dibujar el siguiente cuarto en la dirección opuesta
        circle(150 - j * 6, 90)  # dibuja el segundo cuarto del círculo.
        rt(
            180
        )  # rota la tortuga 180 grados para posicionarla para la próxima iteración.
    circle(
        40, 24
    )  # dibuja un círculo más pequeño entre los círculos principales del espirografo.

# La segunda parte del código utiliza la biblioteca de gráficos Turtle para dibujar una serie de círculos en un patrón. #Los círculos se dibujan utilizando coordenadas polares.
# establecen el color del lápiz, la forma, el tamaño y el color de relleno para los círculos.
color("black")
shape("circle")
shapesize(0.5)
fillcolor("#8B4513")
golden_angle = 137.508  # Define el ángulo áureo en grados.
phi = golden_angle * (pi / 180)  # Convierte el ángulo áureo a radianes.
# itera a través de un rango para dibujar círculos con radios variables.
for i in range(110):
    r = 4 * sqrt(
        i
    )  # calcula el radio de cada círculo según la variable de iteración i.
    theta = i * phi
    x = r * cos(theta)  # calcula el ángulo en radianes para cada círculo.
    y = r * sin(theta)  # calculan las coordenadas cartesianas para cada círculo.
    # La tortuga se mueve a las coordenadas calculadas usando
    penup()
    goto(x, y)
    setheading(
        i * golden_angle
    )  # establece la dirección de la tortuga según el ángulo áureo.
    pendown()  # baja el lápiz para comenzar a dibujar.
    stamp()  # estampa el círculo en la pantalla.
done()  # Completa el proceso de dibujo.
