from PIL import Image, ImageOps
# Open images
input_img=Image.open("before1.jpg")
shirt = Image.open("shirt.png")
input_img = ImageOps.fit(input_img, shirt.size)
input_img.paste(shirt, shirt)
input_img.save("output.jpg")