from math import sqrt

def eucl_dist (x1, x2, y1, y2, z1, z2):
    """Takes the coordinates (x, y, z) of the two 3D-points as input.
    Method returns the euclidean distance."""
    return sqrt((x2 - x1)**2 + (y2-y1)**2 + (z2-z1)**2)

#Count the euclidean distance of the two 3D-points (2, 1, 4) and (3, 1, 0)
print(f"The euclidean distance in 3D is: {eucl_dist(2, 3, 1, 1, 4, 0):.2f} length units.")