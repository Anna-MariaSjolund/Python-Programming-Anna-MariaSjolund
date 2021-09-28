from abc import ABC, abstractmethod

class Geometry:
    def __init__(self, x_coordinate:float=0, y_coordinate:float=0) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate  = y_coordinate

    @property
    def x_coordinate(self) -> float:
        return self._x_coordinate

    @property
    def y_coordinate(self) -> float:
        return self._y_coordinate
    
    @x_coordinate.setter
    def x_coordinate(self, x_coordinate:float) -> None:
        self._x_coordinate = Geometry.validation_numerical(x_coordinate)
    
    @y_coordinate.setter
    def y_coordinate(self, y_coordinate:float) -> None:
        self._y_coordinate = Geometry.validation_numerical(y_coordinate)
    
    @staticmethod
    def validation_numerical(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Please enter an int or a float, not a {type(value)}.")
        else: 
            return value
    
    @staticmethod
    def validation_numerical_above_zero(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Please enter an int or a float, not a {type(value)}.")
        elif value <= 0:
            raise ValueError("The value has to be above 0.")
        else:
            return value

    def translate(self, x_value, y_value):
        self._x_coordinate = Geometry.validation_numerical(x_value)
        self._y_coordinate = Geometry.validation_numerical(y_value)
        
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

    @abstractmethod
    def is_inside(self):
        pass