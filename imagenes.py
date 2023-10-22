import math

from PIL import Image
import numpy as np

img = Image.new("RGB", (1024, 1024))  # 1024 = 2^10

for x in range(1024):
    for y in range(1024):
        y_factor = math.sin(y * 2 * math.pi / 256)
        # x_factor = math.sin(x * 2 * math.pi / 256)
        intensity = int((255 / 2) * (y_factor + 1))

        r = 0
        g = 0
        b = 0

        if y <= 341:
            r = intensity
        elif y <= 500:
            g = intensity
        else:
            b = intensity

        img.putpixel((x, y), (r, g, b))

img.save("example.png")
