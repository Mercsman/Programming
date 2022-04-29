from PIL import Image
image_cat = Image.open('cat.jpg')
# image_forest = Image.open('forest.jpeg')

pixels_cat = image_cat.load()
# pixels_forest = image_forest.load()

# print (pixels_cat[100, 200])
for y in range(100, 110):
    for x in range(100, 105):
        (r, g, b) = pixels_cat [x, y]
        pixels_cat[x, y] = (r, g, 255)
        print(r, g, b)
image_cat.show()

# width, height = image_cat.size
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
