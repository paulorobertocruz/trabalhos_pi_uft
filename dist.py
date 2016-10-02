from math import sqrt

def euclidian(a, b):
    return sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

def d4(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def d8(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("poucos argumentos: dist.py metodo[euclidian, d4, d8] pixel_a pixel_b")
        print("exemplo: dist.py d4 0,0 10,3")
        exit()
    a = sys.argv[2].split(',')
    b = sys.argv[3].split(',')

    if sys.argv[1] == "d4":
        d = d4((int(a[0]), int(a[1])), (int(b[0]), int(b[1])) )
        print(d)
    elif sys.argv[1] == "d8":
        d = d8((int(a[0]), int(a[1])), (int(b[0]), int(b[1])) )
        print(d)
    elif sys.argv[1] == "euclidian":
        d = euclidian((int(a[0]), int(a[1])), (int(b[0]), int(b[1])) )
        print(d)
