def count_slope(x1, y1, x2, y2):
    """Takes the coordinates (x, y) of the two points as input.
    Method returns the k-value/slope."""
    return (y2-y1)/(x2-x1)

#Computes and prints the slope of the line. 
print(f"The k-value is: {count_slope(4, 4, 0, 1)}.")

def count_m(x1, y1, x2, y2):
    """Takes the coordinates (x, y) of the two points as input.
    Method returns the m-value."""
    slope = (y2-y1)/(x2-x1) #Counts the slope.
    return y1 - (slope*x1) #Uses slope to count the m-value.

#Computes and prints the m-value of the line.
print(f"The m-value is: {count_m(4, 4, 0, 1)}.")