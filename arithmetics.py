from PIL import image
from interpolation import b_interpolacao

def even(image1, image2):
    new = Image.new("RGB",(image1.size[0],image1.size[1]),(0,0,0))
    proportion = (image1.size * 100)/image2.size
    new = b_interpolacao(image2, proportion)
    return new

def soma(image1, image2):
    if image1.size != image2.size:
        return None, "Tamanhos das imagens sao diferentes"

    nimage = Image.new("RGB", image1.size, (0,0,0))

    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            rgb = tuple(map( lambda x, y: (x + y)/2, image1.getpixel((i, j)), image2.getpixel((i, j)) ))
            nimage.setpixel((i, j), rgb )

    return nimage



def arith(image1,image2,op):
    n_img = Image.new("RGB", (image1.size[0],image1.size[1]), (0,0,0))
    n_two = even(image1,image2)
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            p1 = image1.getpixel(i,j)
            p2 = n_two.getpixel(i,j)
            if op == "+":
                n_img.putpixel((i,j),(p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2]))
            elif op == "-":
                n_img.putpixel((i,j),(p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2]))
            elif op == "*":
                n_img.putpixel((i,j),(p1[0]*p2[0],p1[1]*p2[1],p1[2]*p2[2]))
            elif op == "/":
                n_img.putpixel((i,j),(int(p1[0]/p2[0]),int(p1[1]/p2[1]),int(p1[2]/p2[2])))
            else
                n_img.putpixel((i,j),(int((p1[0]+p2[0])/2),int((p1[1]*p2[1])/2),int((p1[2]*p2[2])/2)))

    return n_img
