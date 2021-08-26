from math import sqrt

def eucl_dist (x1, x2, y1, y2, z1, z2):
    '''Takes the coordinates (x, y) of the two points as input.
    Method returns the euclidean distance.'''
    return sqrt((x2 - x1)**2 + (y2-y1)**2 + (z2-z1)**2)

#Count the euclidean distance of a point
print(eucl_dist(2, 3, 1, 1, 4, 0))