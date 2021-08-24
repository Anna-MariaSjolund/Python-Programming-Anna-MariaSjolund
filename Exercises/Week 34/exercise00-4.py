def count_slope(x1, y1, x2, y2):
    '''Takes the coordinates (x, y) of the two points as input.
    Method returns the k-value/slope.'''
    slope = (y2-y1)/(x2-x1)
    return slope

#Computes and prints the slope of the line. 
slope = count_slope(4, 4, 0, 1)
print(slope)

def count_m(x1, y1, x2, y2):
    '''Takes the coordinates (x, y) of the two points as input.
    Method returns the m-value.'''
    slope = (y2-y1)/(x2-x1) #Counts the slope.
    m = y1 - (slope*x1) #Uses slope to count the m-value.
    return m

#Computes and prints the m-value of the line.
m = count_m(4, 4, 0, 1)
print(m)