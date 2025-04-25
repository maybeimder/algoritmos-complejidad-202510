import matplotlib.pyplot as plt
from math import cos, sin, pi


# John Ferrer
# Diana Garcia
# Carlos Morales
# Sebastian Santos

def draw_fern( x : int , y : int , angle : float , height : int ):
    rad = angle * pi / 180
    if height < 1:
        return

    plt.plot(
        [ x , x + height*cos(rad) ],
        [ y , y + height*sin(rad) ],
        'lg',
    )

    tx, ty = x + height*cos(rad), y + height*sin(rad)
    draw_fern(tx, ty, angle, height * 2/3)
    draw_fern(tx, ty, angle + 90, height * 1/2)
    draw_fern(tx, ty, angle - 90, height * 1/2)

draw_fern(0,0,90,40)
plt.show()


    