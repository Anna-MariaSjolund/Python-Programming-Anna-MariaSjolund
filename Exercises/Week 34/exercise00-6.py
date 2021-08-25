from math import sqrt

def eucl_dist (x1, x2, y1, y2, z1, z2):
    '''Takes the coordinates (x, y) of the two points as input.
    Method returns the euclidean distance.'''
    distance = sqrt((x2 - x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance

#Count the euclidean distance of a point
eucL_distance = eucl_dist(2, 3, 1, 1, 4, 0)
print(eucL_distance)