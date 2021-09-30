from geometry import Geometry
from math import sqrt

class Rectangle(Geometry):
    """
    A class used for representing rectangles in a coordinate system.
    
    Attributes
    ----------
    length : float
        The length of a rectangle (along the x-axis.)
    width : float
        The width of a rectangle (along the y-axis.)
    x_coordinate : float
        The x-coordinate at the centre of a rectangle (default 0).
    y_coordinate : float
        The y-coordinate at the centre of a rectangle (default 0).
    
    Methods
    -------
    area() -> float
        Calculates the area of a rectangle.
    circumference() -> float
        Calculates the circumference of a rectangle.
    is_inside() -> bool
        Checks if a point (x, y) is inside a rectangle.
    __eq__() -> bool
        Checks if two rectangles are congruent.
    __repr__() -> str
        Returns information about the size and position of a rectangle.
    """
    def __init__(self, length:float, width:float, x_coordinate:float=0, y_coordinate:float=0) -> None:
        """
        Parameters
        ----------
        length : float
            The length of a rectangle (along the x-axis.)
        width : float
            The width of a rectangle (along the y-axis.)
        x_coordinate : float
            The x-coordinate at the centre of a rectangle (default 0).
        y_coordinate : float
            The y-coordinate at the centre of a rectangle (default 0).
        """
        
        super().__init__(x_coordinate, y_coordinate)
        self.length = length
        self.width = width
    

    #METHODS

    def area(self):
        """Calculates the area of a rectangle."""

        return self.length*self.breadth
    
    def circumference(self):
        """Calculates the circumference of a rectangle."""

        return ((self.length*2)+(self.breadth*2)) 

    def is_inside(self, x_value, y_value):
        """
        Checks if a point (x, y) is inside a rectangle.

        Parameters
        ----------
        x_value : float
            The x-value of the point.
        y_value : float
            The y-value of the point.
        
        Raises
        ------
        TypeError
            If value is not int or float.
        
        Returns
        -------
        True
            If point is in the rectangle.
        False
            If point is not in the rectangle.
        """

        _ = Geometry.validation_numerical(x_value)
        _ = Geometry.validation_numerical(y_value)

        if ((self.x_coordinate-self.length/2) <= x_value <= (self.x_coordinate+self.length/2) 
            and (self.y_coordinate-self.width/2) <= y_value <= (self.y_coordinate+self.width/2)):
            return True
        else:
            return False
    
    def __eq__(self, other):
        """
        Checks if two objects are congruent.

        Parameters
        ----------
        self
            A Rectangle object
        other
            An object for comparison.
        
        Returns
        -------
        True
            If the radius of two Rectangle objects are of the same size.
        False
            If the other object is not a Rectangle.
            If the radius of two Rectangle objects are not of the same size.
        """

        if type(self) != type(other):
            return False

        if self.length == other.length and self.width == other.width:
            return True
        else:
            return False

    def __repr__(self):
        """Returns information about the size and position of a rectangle."""

        return f"The length of the rectangle is {self.length}, and the width is {self.width} length units. The geometric center is: ({self.x_coordinate}, {self.y_coordinate})."
    

    #GETTERS AND SETTERS

    @property
    def length(self) -> float:
        """A getter method, returning the private length."""
        return self._length
    
    @property
    def width(self) -> float:
        """A getter method, returning the private width."""
        return self._width
   
    @length.setter
    def length(self, length:float) -> None:
        """
        Validates that the length is numerical and above zero, and assigns it to a private variable.
        
        Parameters
        ----------
        length : float
            The length of a rectangle.
        
        Raises
        ------
        TypeError
            If length is not int or float.
        ValueError
            If length is 0 or below.

        Returns
        -------
        None
        """

        self._length = Geometry.validation_numerical_above_zero(length)

    @width.setter
    def width(self, width:float) -> None:
        """
        Validates that the width is numerical and above zero, and assigns it to a private variable.
        
        Parameters
        ----------
        width : float
            The width of a rectangle.
        
        Raises
        ------
        TypeError
            If width is not int or float.
        ValueError
            If width is 0 or below.

        Returns
        -------
        None
        """
        
        self._width = Geometry.validation_numerical_above_zero(width)
    

    

    



