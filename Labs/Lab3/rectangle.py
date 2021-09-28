from geometry import Geometry
from math import sqrt

class Rectangle(Geometry):
    def __init__(self, length:float, width:float, x_coordinate:float=0, y_coordinate:float=0) -> None:
        super().__init__(x_coordinate, y_coordinate)
        self.length = length
        self.width = width

    @property
    def length(self) -> float:
        return self._length
    
    @property
    def width(self) -> float:
        return self._width
   
    @length.setter
    def length(self, length) -> None:
        self._length = Geometry.validation_numerical_above_zero(length)

    @width.setter
    def width(self, width) -> None:
        self._width = Geometry.validation_numerical_above_zero(width)
    
    def area(self):
        return self.length*self.breadth
    
    def circumference(self):
        return ((self.length*2)+(self.breadth*2)) 

    def is_inside(self, x_value, y_value):
        _ = Geometry.validation_numerical(x_value)
        _ = Geometry.validation_numerical(y_value)
        if (self.x_coordinate-self.length/2) <= x_value <= (self.x_coordinate+self.length/2) and (self.y_coordinate-self.width/2) <= y_value <= (self.y_coordinate+self.width/2):
            return True
        else:
            return False
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
            
        if self.length == other.length and self.width == other.width:
            return True
        else:
            return False
    

    

    



