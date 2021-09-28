from geometry import Geometry

class Rectangle(Geometry):
    def __init__(self, length:float, breadth:float, x_coordinate:float=0, y_coordinate:float=0) -> None:
        super().__init__(x_coordinate, y_coordinate)
        self.length = length
        self.breadth = breadth
        self.breadth = breadth

    @property
    def length(self) -> float:
        return self._length
    
    @property
    def breadth(self) -> float:
        return self._breadth
   
    @length.setter
    def length(self, length) -> None:
        Geometry.validation_above_zero(length)
        #FIX THIS; DOES NOT TAKE THE VALIDATION NUMERICAL
        Geometry.validation_numerical(length)
        self._length = length
        return self._length

    @breadth.setter
    def breadth(self, breadth) -> None:
        Geometry.validation_above_zero(breadth)
        Geometry.validation_numerical(breadth)
        self._breadth = breadth
        return self._breadth
    
    def area(self):
        return self.length*self.breadth
    
    def circumference(self):
        return ((self.length*2)+(self.breadth*2)) 
    

    

    



