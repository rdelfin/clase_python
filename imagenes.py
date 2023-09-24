import math

from PIL import Image
import numpy as np

pixeles = np.ones((500, 500))

for x in range(500):
    for y in range(500):
        y_factor = math.sin(y * 2 * math.pi / 100)
        x_factor = math.sin(x * 2 * math.pi / 100)
        pixeles[y][x] = (255 / 2) * (y_factor * x_factor + 1)

img = Image.fromarray(pixeles)
img.show()
