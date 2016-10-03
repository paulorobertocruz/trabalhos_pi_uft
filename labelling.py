from PIL import Image
from random import randint

def blackAndWhite(image):
    new_image = Image.new("RGB",image.size,(0,0,0))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel( (i,j) )
            m = (p[0] + p[1] + p[2])/3
            if m > 127:
                new_image.putpixel((i,j),(255,255,255))
            else:
                new_image.putpixel((i,j),(0,0,0))
    return new_image

def labelling(image):
    binary_image = blackAndWhite(image)
    new_image = Image.new("RGB", image.size, (255,255,255))
    labels = [(100, 100, 100), (0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 200, 100)]
    next_label = 0
    similar_labels = [i for i in range(len(labels))]
    image_labels = [ [-1 for _ in range(image.size[1])] for _ in range(image.size[0])]
    #in_range
    def inr(x, y):
        if x >= 0 and x < image.size[0] and y >= 0 and y < image.size[1]:
            return True
        return False

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = binary_image.getpixel( (i,j) )
            if p == (0,0,0):
                r = binary_image.getpixel( (i-1,j) )
                s = binary_image.getpixel( (i,j-1) )
                if r == (255,255,255) and s == (255,255,255):
                    image_labels[i][j] = next_label
                    next_label += 1
                elif r == (0, 0, 0) and s != (0, 0, 0):
                    image_labels[i][j] = image_labels[i-1][j]
                elif s == (0, 0, 0) and r != (0, 0, 0):
                    image_labels[i][j] = image_labels[i][j-1]
                elif s == (0, 0, 0) and r == (0, 0, 0) and image_labels[i][j-1] == image_labels[i-1][j]:
                    image_labels[i][j] = image_labels[i][j-1]
                elif s == (0, 0, 0) and r == (0, 0, 0) and image_labels[i][j-1] != image_labels[i-1][j]:
                    image_labels[i][j] = image_labels[i][j-1]
                    similar_labels[image_labels[i][j-1]] = image_labels[i-1][j]

    #junta labels similar_labels
    for i in range(len(similar_labels)):
        if similar_labels[i] != i:
            for j in range(len(similar_labels)):
                if similar_labels[j] == i:
                    similar_labels[j] = similar_labels[i]

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            new_image.putpixel((i,j), labels[ similar_labels[image_labels[i][j]] ])
    #preenche a imagem de labels
    return new_image



if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Faltando path/to/image.png")
        exit()
    print("tretas")
    image_path = sys.argv[1]
    image = Image.open(image_path)
    image.save("labelling/"+image.filename.split('/')[-1])
    labelling(image).save("labelling/resultado.png")
