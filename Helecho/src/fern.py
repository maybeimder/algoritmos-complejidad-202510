import matplotlib.pyplot as plt
from math import cos, sin, pi

def draw_fern( x : int , y : int , angle : float , height : int ):
    # Función recursiva para dibujar una parte del helecho.
    # x, y: coordenadas del punto de inicio del tallo/rama actual.
    # angle: ángulo de inclinación del tallo/rama actual en grados.
    # height: longitud del tallo/rama actual.

    rad = angle * pi / 180 # Convertir ángulo a radianes.
    if height < 1:
        return # Caso base: si la altura es menor que 1, no dibujar nada.

    plt.plot(
        [ x , x + height*cos(rad) ], # Coordenadas x de la línea.
        [ y , y + height*sin(rad) ], # Coordenadas y de la línea.
        'g',
    )

    # Calcula las coordenadas del punto final del tallo/rama actual, que será el punto de inicio para las siguientes ramas
    tx, ty = x + height*cos(rad), y + height*sin(rad)

    # Llama recursivamente a la función 'draw_fern' para dibujar tres ramas más pequeñas que parten del punto final actual:
    draw_fern(tx, ty, angle, height * 2/3) # Dibuja una rama principal más pequeña en la misma dirección.
    draw_fern(tx, ty, angle + 90, height * 1/2) # Dibuja una rama lateral más pequeña con un ángulo de +90 grados.
    draw_fern(tx, ty, angle - 90, height * 1/2) # Dibuja otra rama lateral más pequeña con un ángulo de -90 grados.

#Dibujemos el helecho!:
draw_fern(0,0,90,40)
plt.show()


    