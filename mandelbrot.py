import matplotlib.pyplot as plt
import numpy as np
import math

x_start = -2
x_end = 1
y_start = -1.5
y_end = 1.5
pixel_width = 1000
pixel_height = int(pixel_width*(y_end-y_start)/(x_end-x_start))
n_iterations = 100
points_to_draw = np.zeros((pixel_height, pixel_width))

for x in range(pixel_width):
    for y in range(pixel_height):
        c = (x_end - x_start) * x/pixel_width + x_start + ((y_end - y_start) * -y/pixel_height + y_end)*1j
        z = 0

        for n in range(n_iterations):
            z = z**2 + c

            if abs(z) > 2:
                break

        points_to_draw[y][x] = n

plt.imshow(points_to_draw, cmap='hot', extent=(x_start, x_end, y_start, y_end))
plt.show()