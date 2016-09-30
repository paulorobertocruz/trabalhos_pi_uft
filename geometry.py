from PIL import Image

def translation(image,new_x,new_y):
    new = Image.new("RGB",(image.size[0],image.size[1]),(0,0,0))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel(i,j)
            new.putpixel((i+new_x,j+new_y),(p[0],p[1],p[2]))
    return new
