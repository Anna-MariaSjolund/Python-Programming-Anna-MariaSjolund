class Vector:
    '''A class to represent a euclidean vector with magnitude and direction.'''
    def __init__(self, *numbers:float) -> None: #* so that we do not specify the amount of numbers 
        #print(numbers)
        
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} must be a float or int, not {type(number)}")
        if len(numbers) <= 0:
            raise ValueError("Vectors cannot be empty")
            
        self._numbers = tuple(float(number for number in numbers))

#v1 = (1, 1)
#v2 = (1, 1, 14, 5, 2, 252, 56, 2, 7)
