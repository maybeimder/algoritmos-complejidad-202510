import matplotlib.pyplot as plt
from random import randint
from math import sqrt, pow

points : list[tuple] = []
stripes = []

def generate_points( amount : int ):
    return ([randint(0,360) for _ in range(amount)], [randint(0,360) for _ in range(amount)])


def get_nearest_points(points : list):
    median_index = 0
    points.sort(key=lambda x: x[0])

    n = len(points)

    if n <= 5:
        return brute_force(points)
    
    else:
        median_index = n//2
        #print(n, median_index, points)
        left, right = points[:median_index], points[median_index:]
        d1, p11, p12 = get_nearest_points(left)
        d2, p21, p22 = get_nearest_points(right)
        
        if d1 == min(d1, d2):
            d = d1
            p1, p2 = p11, p12
        else:
            d = d2
            p1, p2 = p21, p22
        d3, p31, p32 = get_nearest_points_in_middle_stripe(median_index,points, d)
        if d3 == min(d, d3):
            d = d3
            p1, p2 = p31, p32
        print(f"d1: {d1}, d2: {d2}, d3: {d3}, d: {d}")
        return d, p1, p2

def get_nearest_points_in_middle_stripe(median_index,points : list, d : int):
    middle = (points[median_index-1][0] + points[median_index][0]) / 2
    stripe = [point for point in points if abs(point[0] - middle) < d]
    return brute_force(stripe) if len(stripe) > 1 else (d+1, 0, 0)

def brute_force( points : list ):
    minn = 99999
    lbl = []
    distance = 0.0
    for idx in range(len(points) - 1):
        for ins in range(len(points)):
            if ins == idx:
                continue

            distance = get_distance(
                points[idx][0],
                points[idx][1],
                points[ins][0],
                points[ins][1]
            )
            if distance <= minn:
               lbl = [idx,ins]
               minn = distance
             
    #print(lbl)
    return minn, points[lbl[0]], points[lbl[1]]

def get_distance( point1_x : int , point1_y : int , point2_x : int , point2_y : int ):
    d = sqrt(pow(point1_x - point2_x, 2) + pow(point1_y - point2_y, 2))
    return d

def display( x_points : list, y_points : list , p1 : tuple, p2 : tuple, distance : float ):
    plt.figure(figsize=(100, 6))
    plt.scatter (
        x= x_points, 
        y= y_points,
        c= "c"
    )
    [plt.text(x[i] * (1 + 0.01), y[i] * (1 + 0.01) , f"({x[i]},{y[i]})", fontsize=7) for i in range(len(x_points))]
    
    plt.title("Puntos más cercanos")
    plt.plot([p1[0],p2[0]], [p1[1],p2[1]], 'bo-')
    plt.text((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2,
             f"Distancia: {distance:.2f}",
             fontsize=8, ha='center', va='bottom', color='red')
    
    plt.show()


if __name__ == "__main__":
    x, y = generate_points(150)
    points = list(zip(x, y))
    dist, p1, p2 = get_nearest_points(points)
    print(f"Distancia: {dist}")
    print(f"Punto 1 -> {p1}")
    print(f"Punto 2 -> {p2}")
    dist1, p11, p21 = brute_force(points)
    print(f"Distancia: {dist1}")
    print(f"Punto 1 -> {p11}")
    print(f"Punto 2 -> {p21}")
    

    display(x,y, p1, p2, dist)