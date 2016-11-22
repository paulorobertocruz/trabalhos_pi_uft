from PIL import Image

def negative(image):
    nega = lambda p: ( 255 - p[0], 255 - p[1], 255 - p[2] )
    nimage = Image.new(image.mode, image.size, (0,0,0))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            nimage.putpixel( (i, j), nega(image.getpixel((i,j))) )
    return nimage



if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("faltando argumentos")
        exit()

    image_path = sys.argv[1]

    image = Image.open(image_path)
    image.show()
    negative(image).show()
