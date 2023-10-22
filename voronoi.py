import math

from PIL import Image
import numpy as np


def distance(point1, point2):
    x = point2[0] - point1[0]
    y = point2[1] - point1[1]
    return math.sqrt((x * x) + (y * y))


img = Image.new("RGB", (1024, 1024))  # 1024 = 2^10

point_1 = (20, 20)  # rojo
point_2 = (500, 200)  # verde
point_3 = (50, 800)  # azul

for x in range(1024):
    for y in range(1024):
        distance_to_point_1 = distance(point_1, (x, y))
        distance_to_point_2 = distance(point_2, (x, y))
        distance_to_point_3 = distance(point_3, (x, y))

        r = 0
        g = 0
        b = 0

        if (
            distance_to_point_1 < distance_to_point_2
            and distance_to_point_1 < distance_to_point_3
        ):
            r = 255
        elif (
            distance_to_point_2 < distance_to_point_1
            and distance_to_point_2 < distance_to_point_3
        ):
            g = 255
        elif (
            distance_to_point_3 < distance_to_point_2
            and distance_to_point_3 < distance_to_point_1
        ):
            b = 255

        img.putpixel((x, y), (r, g, b))


img.save("voronoi.png")
