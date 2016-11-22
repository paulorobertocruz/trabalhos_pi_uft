from PIL import Image

def n_interpolacao(img, s):
    size = img.size

    nwidth = int(size[0] * s)
    nheight = int(size[1] * s)

    n_img = Image.new("RGB",(nwidth, nheight), (0,0,0))

    for i in range(nwidth):
        for j in range(nheight):
            p = (int(i/s), int(j/s))
            n_img.putpixel((i,j), img.getpixel(p))

    return n_img

def b_interpolacao(img, s):
    size = img.size
    nwidth = int(size[0] * s)
    nheight = int(size[1] * s)

    n_img = Image.new("RGB", (nwidth, nheight), (0,0,0))

    for i in range(nwidth-1):
        for j in range(nheight-1):

            p = (int(i/s), int(j/s))
            if p == (0,0):
                print("0,0")

            b, c, d = (p[0], p[1]+1), (p[0]+1, p[1]), (p[0]+1, p[1]+1)

            a = img.getpixel(p)
            b = img.getpixel(b)
            c = img.getpixel(c)
            d = img.getpixel(d)

            rr = int((a[0] + b[0] + c[0] + d[0] )/ 4)
            gg = int((a[1] + b[1] + c[1] + d[1] )/ 4)
            bb = int((a[2] + b[2] + c[2] + d[2] )/ 4)

            n_img.putpixel((i, j), (rr, gg, bb))


    return n_img

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Faltando path/to/image.png")
        exit()

    img = Image.open(sys.argv[1])
    img.show()

    a = n_interpolacao(img, 1.3)
    a.show()

    b = b_interpolacao(img, 1.3)
    b.show()
