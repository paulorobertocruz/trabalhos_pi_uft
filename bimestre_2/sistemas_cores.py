from PIL import Image
from math import pow
def pixel_hsl_rgb(p):
    """ Retorna matriz cmy de uma imagem rgb """
    
    C = (1 - abs(2 * p[2] - 1) ) * p[1]
    X = C * (1 - abs( (p[0] / 60) % 2 - 1) )
    m = p[2] - C/2

    if p[0] >= 0 and p[0] < 60:
        Rl, Gl, Bl = C, X, 0
    elif p[0] >= 60 and p[0] < 120:
        Rl, Gl, Bl = X, C, 0
    elif p[0] >= 120 and p[0] < 180:
        Rl, Gl, Bl = 0, C, X
    elif p[0] >= 180 and p[0] < 240:
        Rl, Gl, Bl = 0, X, C
    elif p[0] >= 240 and p[0] < 300:
        Rl, Gl, Bl = X, 0, C
    elif p[0] >= 300 and p[0] < 360:
        Rl, Gl, Bl = C, 0, X
    
    R, G, B = (Rl+m)*255, (Gl+m)*255, (Bl+m)*255

    return (int(R), int(G), int(B))


def rgb_to_xyz(image):
    
    xyz = [[0 for __ in range(image.size[1])] for _ in range(image.size[0])]

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            
            pixel = image.getpixel((i, j))

            var_R = ( pixel[0] / 255 )
            var_G = ( pixel[1] / 255 )
            var_B = ( pixel[2] / 255 )

            if var_R > 0.04045 :
                var_R = ( ( var_R + 0.055 ) / 1.055 ) ** 2.4                
            else:
                var_R = var_R / 12.92

            if var_G > 0.04045:
                var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
            else:
                var_G = var_G / 12.92
            
            if var_B > 0.04045:
                var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
            else:
                var_B = var_B / 12.92

            var_R = var_R * 100
            var_G = var_G * 100
            var_B = var_B * 100

            X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
            Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
            Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

            xyz[i][j] = (X, Y, Z)
    return xyz

    


def rgb_to_cmy(image):
    """ Retorna matriz cmy de uma imagem rgb """

    cmy = [[0 for __ in range(image.size[1])] for _ in range(image.size[0])]

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = image.getpixel((i, j))
            cmy[i][j] = (1 - pixel[0]/255, 1 - pixel[1]/255, 1 - pixel[2]/255)
    return cmy


def rgb_to_hsl(image):
    """ Retorna pixel hsl de uma pixel rgb"""
    hsl = [[0 for __ in range(image.size[1])] for _ in range(image.size[0])]

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = image.getpixel((i,j))
            red_l = pixel[0]/255
            green_l = pixel[1]/255
            blue_l = pixel[2]/255
            
            cmax = max([red_l, green_l, blue_l])
            cmin = min([red_l, green_l, blue_l])

            delta = cmax - cmin
            
            h = 0
            
            if delta == 0:
                h = 0
            
            elif cmax == red_l:
                h = 60 * (((green_l - blue_l) / delta) % 6)
            
            elif cmax == green_l:
                h = 60 * (( (blue_l - red_l) / delta) + 2)
            
            elif cmax == blue_l:            
                h = 60 * (( (red_l - green_l) / delta) + 4)
            
            l = (cmax + cmin) / 2
            s = delta / 1 - abs(2*l-1)
            if delta == 0:
                s = 0

            hsl[i][j] = (h, s, l)

    return hsl

def pixel_rgb_to_hsl(pixel):
    """ Retorna pixel hsl de uma pixel rgb"""

    red_l = pixel[0]/255
    green_l = pixel[1]/255
    blue_l = pixel[2]/255
    
    cmax = max([red_l, green_l, blue_l])
    cmin = min([red_l, green_l, blue_l])

    delta = cmax - cmin
    
    h = 0
    
    if delta == 0:
        h = 0
    
    elif cmax == red_l:
        h = 60 * (((green_l - blue_l) / delta) % 6)
    
    elif cmax == green_l:
        h = 60 * (( (blue_l - red_l) / delta) + 2)
    
    elif cmax == blue_l:            
        h = 60 * (( (red_l - green_l) / delta) + 4)
    
    l = (cmax + cmin) / 2
    s = delta / 1 - abs(2*l-1)
    if delta == 0:
        s = 0

    return (h, s, l)            

def pixel_rgb_to_xyz(pixel):

    var_R = ( pixel[0] / 255 )
    var_G = ( pixel[1] / 255 )
    var_B = ( pixel[2] / 255 )

    if var_R > 0.04045 :
        var_R = ( ( var_R + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_R = var_R / 12.92

    if var_G > 0.04045:
        var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_G = var_G / 12.92
    
    if var_B > 0.04045:
        var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
    Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
    Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

    return  (X, Y, Z)    

    


def pixel_rgb_to_cmy(pixel):
    """ Retorna pixel cmy de um pixel rgb """    
    return (1 - pixel[0]/255, 1 - pixel[1]/255, 1 - pixel[2]/255)




def teste_hsl(image):
    
    hsl = rgb_to_hsl(image)

    for i in range(image.size[0]):
        for j in range(image.size[1]):

            tt = (hsl[i][j][0], hsl[i][j][1], hsl[i][j][2]+0.15)            

            p = pixel_hsl_rgb(tt)

            image.putpixel((i, j), p)
    
    return image

def image_from_rgb(rgb):
    img = Image.new("RGB", (128, 128), rgb)
    return img

import sys
if __name__ == "__main__":
    print("MAIN")
    cor = sys.argv[1]
    cor = cor.split(",")
    rgb = (int(cor[0]), int(cor[1]), int(cor[2]))
    print("RGB:", rgb)
    print("CMY:", pixel_rgb_to_cmy(rgb))
    print("HSL:", pixel_rgb_to_hsl(rgb))
    print("XYZ:", pixel_rgb_to_xyz(rgb))
    image_from_rgb(rgb).show()

    if len(sys.argv) > 2:
        img = Image.open("img.jpg")
        img = teste_hsl(img)
        img.show()

