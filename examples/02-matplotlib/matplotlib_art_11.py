import matplotlib.pyplot as plt
import math

width = 400
height = 400
grid = []

for row in range(height):
    line = []
    for col in range(width):
        x = col / width * 4 * math.pi
        y = row / height * 4 * math.pi
        value = math.sin(x) * math.cos(y) + math.sin(x * 0.5 + y * 0.5)
        line.append(value)
    grid.append(line)

plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap="twilight", interpolation="bilinear")
plt.axis("off")
plt.show()