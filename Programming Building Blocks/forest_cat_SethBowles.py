import re
import math
from PIL import Image
print()
image_cat = Image.open('cat.jpg')
image_forest = Image.open('forest.jpg')

pixels_cat = image_cat.load()
pixels_forest = image_forest.load()
c_width, c_height = image_cat.size
# print(image_cat.size)
# print(image_forest.size)

perc = 0

for y in range(0, c_height):
    for x in range(0, c_width):
        perc += 1;
        perc_left = f'{((perc / (c_height * c_width)) * 100):.2f}'
        perc_left = (perc / (c_height * c_width)) * 100
        (r, g, b) = pixels_cat[x, y]
        # (r, g, b) = pixels_forest[x, y]
        if (r, b, g) >= (r, b, 215):
                # pixels_cat[x, y] = pixels_forest[x, y]
                # r, g, b = pixels_forest
                # pixels_cat[x, y] = pixels_forest[x, y]
                pixels_cat[x, y] = pixels_forest[x, y]
        # (r, g, b) = pixels_forest[x, y]
                print(f'forest RGB: {r:>3}, {g:>3}, {b:>3};                                                    ------------------ loading:{perc_left:>6.2f}% ------------------\r', end = '')

print ()
image_cat.show()
image_cat.save('forest_cat.jpg')