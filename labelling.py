from PIL import Image
from random import Image

def in_range(a,r):
    return  a[0] >= 0 and a[0] < r[0] and a[1] >= 0 and a[1] < r[1]

def blackAndWhite(image):
    size = image.size
    new_image = Image.new("RGB",(size[0],size[1]),(0,0,0))
    for i in range(size[0]):
        for j in range(size[1]):
            p = image.getpixel(i,j)
            m = (p[0] + p[1] + p[2])/3
            if m > 127:
                new_image.putpixel((i,j),(255,255,255))
            else:
                new_image.putpixel((i,j),(0,0,0))
    return new_image

def labelling(image):
    size = image.size
    binary_image = blackAndWhite(image)
    new_image = Image.new("RGB",(size[0],size[1]),(0,0,0))
    for i in range(size[0]):
        for j in range(size[1]):
            p = binary_image.getpixel(i,j)
            if p = (255,255,255):
                if (p[0]-1,p[1]) = (255,255,255) and (p[0],p[1]-1) = (255,255,255):
                    r = new_image.getpixel(i-1,j)
                    s = new_image.getpixel(i,j-1)
                    if r = s:
                        new_image.putpixel((i,j),(r[0],r[1],r[2]))
                    else:
                        new_image.putpixel((i,j),(r[0],r[1],r[2]))
                        new_image.putpixel((i,j-1),(r[0],r[1],r[2]))
                elif (p[0]-1,p[1]) = (255,255,255):
                    r = new_image.getpixel(i-1,j)
                    new_image.putpixel((i,j),(r[0],r[1],r[2]))
                elif (p[0],p[1]-1) = (255,255,255):
                    s = new_image.getpixel(i,j-1)
                    new_image.putpixel( (i,j),(s[0],s[1],s[2]) )
                else:
                    r = random.randint(0,255)
                    g = random.randint(0,255)
                    b = random.randint(0,255)
                    new_image.putpixel((i,j),(r,g,b))



if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Faltando path/to/image.png")
        exit()

    
