from math import sqrt

def count_hypothenuse(cathetus1, cathetus2):
    """Arg 1 takes the length of cathetus 1. Arg 2 takes the length of cathetus 2.
    The method returns the length of the hypothenuse."""
    return sqrt(cathetus1**2 + cathetus2**2)

def count_cathetus(cathetus1, hypothenuse):
    """Arg 1 takes the length of cathetus 1. Arg 2 takes the length of cathetus 1.
    The method returns the length of cathetus 2."""
    return sqrt(hypothenuse**2 - cathetus1**2)

#Count the length of the hypothenuse
print(count_hypothenuse(3, 4))

#Count the length of the cathetus
print(count_cathetus(5, 7))