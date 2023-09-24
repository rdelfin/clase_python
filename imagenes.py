import math

from PIL import Image
import numpy as np

pixeles = np.ones((500, 500))

for x in range(500):
    for y in range(500):
        pixeles[y][x] = (255/2)*math.tan(x*2*math.pi/100)+255/2


print(pixeles)

img = Image.fromarray(pixeles)
img.show()