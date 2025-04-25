import matplotlib.pyplot as plt
from random import randint
from math import sqrt

points : list[tuple] = []

def generate_points( amount : int ):
    return ([randint(0,360) for _ in range(amount)], [randint(0,360) for _ in range(amount)])


def get_nearest_points( x_points : list = None, y_points : list = None, compressed = None ):
    median_index = 0
    points = list(zip(x_points, y_points)) if not compressed else compressed
    points.sort()

    n = len(points)

    if n <= 30:
        return brute_force( x_points , y_points )
    
    else:
        median_index = n//2
        print(n, median_index, points)
        left, right = points[::median_index], points[median_index::]
        d1 = get_nearest_points(compressed= left)
        d2 = get_nearest_points(compressed= right)
        d = d1 if d1 < d2 else d2

    return d


def brute_force( x_points : list, y_points : list ):
    minn = 99999
    lbl = ""
    for idx in range(len(x_points) - 1):
        for ins in range(len(x_points)):
            if ins == idx:
                continue

            dist = get_distance(
                x_points[idx],
                y_points[idx],
                x_points[ins],
                y_points[ins]
            )

            if dist <= minn:
               lbl = f"{idx,ins}"
               minn = dist
             
    print(lbl)
    return dist

def get_distance( point1_x : int , point1_y : int , point2_x : int , point2_y : int ):
    return sqrt( (point1_x - point2_x)**2 + (point1_y - point2_y)**2 )

def display( x_points : list, y_points : list ):
    plt.figure(figsize=(100, 6))
    plt.scatter (
        x= x_points, 
        y= y_points,
        c= "c"
    )
    [plt.text(x[i] * (1 + 0.01), y[i] * (1 + 0.01) , i, fontsize=8) for i in range(len(x_points))]

    plt.show()


if __name__ == "__main__":
    x, y = generate_points(50)
    print(get_nearest_points(x_points=x, y_points=y))
    print(brute_force(x,y))
    

    display(x,y)