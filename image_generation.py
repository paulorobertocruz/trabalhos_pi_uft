from PIL import Image
from random import randint
image_size = 512
image = Image.new("RGB", (image_size, image_size), (255, 255, 255))
tamanho_max = 100
quantidade = randint(3, 10)

def quad(image, start, tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            image.putpixel((start[0]+i, start[1]+j),(0,0,0))
    return image

for i in range(quantidade):
    tamanho = randint(3, tamanho_max)
    startpos = ( randint(0, image_size-tamanho_max), randint(0, image_size-tamanho_max))
    image = quad(image, startpos, tamanho)


image.save("labelling/input.png")
