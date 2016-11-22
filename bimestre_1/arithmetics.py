from PIL import Image
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

def multiplicacao(image_a, image_b):
    for i in range(image_a.size[0]):
        for j in range(image_a.size[1]):
            p = image_a.getpixel((i,j))
            b = image_b.getpixel((i,j))
            pr = max(0, min(int(p[0] * b[0]), 255))
            pg = max(0, min(int(p[1] * b[1]), 255))
            pb = max(0, min(int(p[2] * b[2]), 255))
            image_a.putpixel((i,j), (pr, pg, pb))
    return image

def escala(image, fator):
    fator = float(fator)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            pr = max(0, min(int(p[0] * fator), 255))
            pg = max(0, min(int(p[1] * fator), 255))
            pb = max(0, min(int(p[2] * fator), 255))
            image.putpixel((i,j), (pr, pg, pb))
    return image

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
            else:
                n_img.putpixel((i,j),(int((p1[0]+p2[0])/2),int((p1[1]*p2[1])/2),int((p1[2]*p2[2])/2)))

    return n_img

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("faltando argumentos")
        exit()

    operation = sys.argv[1]
    options = sys.argv[2]
    image_path = sys.argv[3]

    image = Image.open(image_path)
    image.show()

    if operation == "escala":
        escala(image, options).show()
    elif operation == "soma":
        image_b = Image.open(options)
        soma(image, image_b).show()
    elif operation == "multiplicacao":
        image_b = Image.open(options)
        multiplicacao(image, image_b).show()
