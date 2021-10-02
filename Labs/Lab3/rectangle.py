from matplotlib import colors
from geometry import Geometry
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as plt_rect

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

        return self.length*self.width
    
    def circumference(self):
        """Calculates the circumference of a rectangle."""

        return ((self.length*2)+(self.width*2)) 

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
    
    def plot_figure(self, fixed_scale10:bool = False) -> None: #https://www.geeksforgeeks.org/matplotlib-patches-rectangle-in-python/
        """
        Plots a Rectangle object in a coordinate system.
        
        Arguments
        ---------
        fixed_scale10 : bool
            If True and if the edges of the rectangles are between -10 and 10 on the x and y-axis,
                the method will show the object in a coordinate system scaled between -10 and 10.
            If False or if the edges of the rectangles are not between -10 and 10 on the x and y-axis, 
                the method will zoom in on the figure.

        Returns 
        -------
        None
        """

        fig = plt.figure(dpi=100)
        ax = fig.add_subplot()

        lowest_x = self.x_coordinate-self.length/2
        highest_x = self.x_coordinate+self.length/2 
        lowest_y = self.y_coordinate-self.width/2
        highest_y = self.y_coordinate+self.width/2

        rectangle_figure = plt_rect((lowest_x, lowest_y), self.length, self.width, facecolor="forestgreen", edgecolor="black")
        ax.add_patch(rectangle_figure)
        ax.set_aspect("equal", adjustable="box") #https://www.delftstack.com/howto/matplotlib/how-to-make-a-square-plot-with-equal-axes-in-matplotlib/

        if fixed_scale10 == True and lowest_x >= -10 and lowest_y >= -10 and highest_x <= 10 and highest_y <= 10:
            ax.set(xlim=(-10, 10), ylim=(-10, 10), xticks=[-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
        else:
            ax.set(xlim=(lowest_x-self.length, highest_x+self.length), ylim=(lowest_y-self.width, highest_y+self.width))

        ax.set(title=(f"Rectangle Plotted in a Coordinate System"), xlabel=("x"), ylabel=("y"))
        
        
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
    

    

    



