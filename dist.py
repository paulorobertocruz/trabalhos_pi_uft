from math import sqrt

def euclidian(a, b):
    return sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

def d4():
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def d8():
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
