
import re
import math
from PIL import Image
image_cat = Image.open('cat.jpg')
image_forest = Image.open('forest.jpg')

pixels_cat = image_cat.load()
pixels_forest = image_forest.load()
c_width, c_height = image_cat.size
print(image_cat.size)
print(image_forest.size)

perc = 0

for y in range(0, c_height):
    for x in range(0, c_width):
        perc += 1;
        # perc_left = f'{((perc / (c_height * c_width)) * 100):.2f}'
        perc_left = (perc / (c_height * c_width)) * 100
        (r, g, b) = pixels_cat[x, y]
        (r, g, b) = pixels_forest[x, y]
        # print(r, g, b, pixels_cat[x, y], f'\% remaining {perc_left}%\r', end = '')
        # print(f'forest RGB: %-3s, %-3s, %-3s; cat RGB: %-15s; \% remaining: %-6s\%.\r'(r, g, b, f'{pixels_cat[x, y]}',f'{perc_left:.2f}'), end = '')
        # print(f'forest RGB: %-3s, %-3s, %-3s; \% remaining: %-6s\%.\r'(r, g, b,perc_left), end = '')
        print(f'forest RGB: {r:>3}, {g:>3}, {b:>3}; % remaining: {perc_left:>6.2f}%.\r', end = '') #Percentage complete of transfer
        """
        r - range 0, 100
        g - range 200, 255
        b - range 0, 80
        
        """
        # a = int(0, 100)
        # b2 = int (200, 255)
        # c = int (0, 80)
        # if (pixels_cat[x, y] != (a, b2, c)):
        # if (pixels_cat[x, y] != (67, 229, 24)) and (pixels_cat[x, y] != (66, 229, 24)) and (pixels_cat[x, y] != (65, 229, 24)) and (pixels_cat[x, y] != (68, 229, 24)) and (pixels_cat[x, y] != (69, 229, 24)) and (pixels_cat[x, y] != (70, 229, 24)) and (pixels_cat[x, y] != (64, 229, 24)) and (pixels_cat[x, y] != (63, 229, 24)) and (pixels_cat[x, y] != (62, 229, 24)) and (pixels_cat[x, y] != (61, 229, 24)) and (pixels_cat[x, y] != (60, 229, 24)):
        # if re.search(r'(6*, 229, 24)', pixels_cat[x, y]):
        # if (re.search('^(?!\d{1,2}|?!100)',pixels_cat[x,y][0])) and (re.search('^(?!2[0-4]\d|?!25[0-5])',pixels_cat[x,y][1])) and (re.search('^(?!\d{1,2})',pixels_cat[x,y][2])):
        if (not (re.search(r"^6\d$",f"{pixels_cat[x,y][0]}" ))) and (not re.search(r"^2[2-3]\d$",f"{pixels_cat[x,y][1]}")) and (not re.search(r"^2\d$",f"{pixels_cat[x,y][2]}")):
            pixels_forest[x, y] = pixels_cat[x, y]
print('\ntranspose complete.\n')
image_forest.show()
# image_forest.save('forest_cat.jpg')
# image_fc = Image.open('forest_cat.jpg')
# image_fc.show()
# print(image_original.size)
# pixels_original = image_cat.load()
# for y in range (0, 600):
#     for x in range(0, 800):
#         (r, g, b) = pixels_original [x, y]
#         pixels_original[x, y] = (r, g, 255)

# pixels_original[100, 200] = (200, 0, 200)

# r, g, b = pixels_original[100, 200]

# print (r, g, b)

# image_cat.show()

# image_original.save('forest_cat.jpg')