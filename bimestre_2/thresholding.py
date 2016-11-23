import sys
import os

# para poder importar bimestre_1
dir_name = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) )
sys.path.append(dir_name)

from PIL import Image
from bimestre_1.histograma import grayscale, histograma

def thresholding(image):
    greyed_image = grayscale(image)
    hist = histograma(greyed_image)
    largest = (0,0)
    second_largest = (0,0)
    # encontrar dois picos no histograma
    largest = (max(hist),hist.index(max(hist)))
    for i in range(len(hist)):
        # print("largest %d minus index %d = %d" % (largest[1],i,abs(largest[1] - i)))
        if(abs(largest[1] - i) > 50):
            if(hist[i] < largest[0] and hist[i] > second_largest[0]):
                second_largest = (hist[i],i)
    # print dos picos encontrados
    print("maior pico %d em %d" % (largest[0], largest[1]))
    print("segundo maior pico %d em %d" % (second_largest[0], second_largest[1]))
    # encontrar o menor ponto do vale entre os dois picos
    if(largest[1] < second_largest[1]):
        x = hist[largest[1]:second_largest[1]]
    else:
        x = hist[second_largest[1]:largest[1]]
    least = min(x)
    threshold = hist.index(least)
    #for i in range(len(hist)):
    #    if(hist[i]==least):
    #        threshold = i
    print("limiar é %d" % threshold)
    # binarizar a partir do threshold
    new = Image.new("RGB",(image.size[0],image.size[1]),(0,0,0))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = greyed_image.getpixel((i,j))
            if(p[0] > threshold):
                new.putpixel((i,j),(255,255,255))
            else:
                new.putpixel((i,j),(0,0,0))
    return new

img = Image.open("img.jpg")
img = thresholding(img)
img.show()
