from PIL import Image

def rgbToCmy(image):
    cmy = [ [ 0 for __ in range(image.size[1])] for _ in range(image.size[0])]

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = image.getpixel( (i,j) )
            cmy[i][j] = ( 1 - pixel[0]/255, 1 - pixel[1]/255, 1 - pixel[2]/255 )
    return cmy

def cmyToRgb(image):
    pass

def cmtToHsl(image):
    pass
