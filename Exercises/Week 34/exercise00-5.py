from math import sqrt

def eucl_dist (x1, x2, y1, y2):
    """Takes the coordinates (x, y) of the two points as input.
    Method returns the euclidean distance."""
    return sqrt((x2 - x1)**2 + (y2-y1)**2)

#Count the euclidean distance between the points (3, 5) and (-2, 4)
print(f"The euclidean distance is: {eucl_dist(-2, 3, 4, 5):.2f} length units.")
