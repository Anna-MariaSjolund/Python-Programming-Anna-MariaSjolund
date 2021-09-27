from geometry import Geometry
import math

class Circle(Geometry):
    def __init__(self, radius:float, x_coordinate:float=0, y_coordinate:float=0) -> None:
        super().__init__(x_coordinate, y_coordinate)
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius
   
    @radius.setter
    def radius(self, radius) -> None:
        Geometry.validation_above_zero(radius)
        Geometry.validation_numerical(radius)
        self._radius = radius
        return self._radius
    
    def area(self):
        return (math.pi*(self.radius**2))
    
    def circumference(self):
        return 2*math.pi*self.radius
    
    #Felhantering för x-value, y-value
    def is_inside(self, x_value, y_value):
        eucl_distance = math.sqrt((self.x_coordinate - x_value)**2 + (self.y_coordinate-y_value)**2)
        print(eucl_distance)
        print(self.radius)
        if eucl_distance < self.radius:
            return True
        else: 
            return False
