from PIL import Image


def in_range(a, r):
    return  a[0] >= 0 and a[0] < r[0] and a[1] >= 0 and a[1] < r[1]


def te():
    img = Image.open("tocantins.jpg")
    print(img.format, img.size, img.mode)
    p = (100, 100)
    print(img.getpixel(p))

    img.putpixel(p, (0, 0, 0))
    img.show()


def visinhos_4(x, y):
    return (x, y-1), (x, y+1), (x-1, y), (x+1, y)


def visinhos_diagonal(x, y):
    return (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)


def visinhos_8(x, y):
    return visinhos_4(x, y), visinhos_diagonal(x, y)


def n_interpolacao(img, s):
    size = img.size

    nwidth = int(size[0] * s)
    nheight = int(size[1] * s)

    n_img = Image.new("RGB",(nwidth, nheight), (0,0,0))
    # print(n_img.size)
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
    # print(n_img.size)
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


img = Image.open("tocantins.jpg")
img.show()
a = n_interpolacao(img, 1.3)
a.show()

b = b_interpolacao(img, 1.3)
b.show()
