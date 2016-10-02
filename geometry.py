from PIL import Image

def translation(image,new_x,new_y):
    new = Image.new("RGB",(image.size[0],image.size[1]),(0,0,0))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel(i,j)
            new.putpixel((i+new_x,j+new_y),(p[0],p[1],p[2]))
    return new


def reflexao(image, eixo):
    if image.mode is not "RGB":
        return None

    x = lambda x: x
    y = lambda y: y

    if "x" in eixo:
        x = lambda x: image.size[0] -1 -x
    if "y" in eixo:
        y = lambda y: image.size[1] -1 -y

    nimage = Image.new("RGB", image.size, (0,0,0))

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            nimage.putpixel( (x(i), y(j) ), image.getpixel( (i,j) ) )

    return nimage
