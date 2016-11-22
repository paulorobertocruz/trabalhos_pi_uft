from PIL import Image
import math

def euclidian(o,d):
    return math.sqrt( (o[0]-d[0])**2 + (o[1]-d[1])**2 )

def cityblock(o,d):
    return abs(o[0]-d[0]) + abs(o[1]-d[1])

def chessboard(o,d):
    return max(abs(o[0]-d[0]),abs(o[1]-d[1]))
