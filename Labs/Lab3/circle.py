from geometry import Geometry
import math
import matplotlib.pyplot as plt

class Circle(Geometry):
    """
    A class used for representing circles in a coordinate system.
    
    Attributes
    ----------
    radius : float
        The radius of a circle.
    x_coordinate : float
        The x-coordinate at the centre of a circle (default 0).
    y_coordinate : float
        The y-coordinate at the centre of a circle (default 0).
    
    Methods
    -------
    area() -> float
        Calculates the area of a circle.
    circumference() -> float
        Calculates the circumference of a circle.
    is_inside(x_value : float, y_value : float) -> bool
        Checks if a point (x, y) is inside a circle.
    __eq__(self, other : Circle) -> bool
        Checks if two circles are congruent.
    __repr__() -> str
        Returns information about the size and position of a circle.
    """

    def __init__(self, radius:float, x_coordinate:float=0, y_coordinate:float=0) -> None:
        """
        Parameters
        ----------
        radius : float
            The radius of a circle.
        x_coordinate : float
            The x-coordinate at the centre of a circle (default 0).
        y_coordinate : float
            The y-coordinate at the centre of a circle (default 0).
        """

        super().__init__(x_coordinate, y_coordinate)
        self.radius = radius

     
    #METHODS

    def area(self) -> float:
        """Calculates the area of a circle."""

        return (math.pi*(self.radius**2))
    
    def circumference(self) -> float:
        """Calculates the circumference of a circle."""

        return 2*math.pi*self.radius
    
    def is_inside(self, x_value:float, y_value:float) -> bool:
        """
        Checks if a point (x, y) is inside a circle.

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
            If point is in the circle.
        False
            If point is not in the circle.
        """
        _ = Geometry.validation_numerical(x_value)
        _ = Geometry.validation_numerical(y_value)
        eucl_distance = math.sqrt((self.x_coordinate - x_value)**2 + (self.y_coordinate - y_value)**2)
        if eucl_distance <= self.radius:
            return True
        else: 
            return False

    def plot_figure(self, fixed_scale10:bool = False) -> None: #https://www.geeksforgeeks.org/matplotlib-patches-rectangle-in-python/
        """
        Plots a Circle object in a coordinate system.
        
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

        lowest_x = self.x_coordinate-self.radius
        highest_x = self.x_coordinate+self.radius
        lowest_y = self.y_coordinate-self.radius
        highest_y = self.y_coordinate+self.radius

        circle_figure = plt.Circle((self.x_coordinate, self.y_coordinate), self.radius, facecolor="cornflowerblue", edgecolor="black")
        ax.add_patch(circle_figure)
        ax.set_aspect('equal', adjustable='box') #Reference: https://www.delftstack.com/howto/matplotlib/how-to-make-a-square-plot-with-equal-axes-in-matplotlib/

        if fixed_scale10 == True and lowest_x >= -10 and lowest_y >= -10 and highest_x <= 10 and highest_y <= 10:
            ax.set(xlim=(-10, 10), ylim=(-10, 10), xticks=[-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
        else:
            ax.set(xlim=(lowest_x-self.radius, highest_x+self.radius), ylim=(lowest_y-self.radius, highest_y+self.radius))

        ax.set(title=(f"Circle Plotted in a Coordinate System"), xlabel=("x"), ylabel=("y"))

    def __eq__(self, other) -> bool:
        """
        Checks if two objects are congruent.

        Parameters
        ----------
        self
            A Circle object
        other
            An object for comparison.
        
        Returns
        -------
        True
            If the radius of two Circle objects are of the same size.
        False
            If the other object is not a Circle.
            If the radius of two Circle objects are not of the same size.
        """
        if type(self) != type(other):
            return False

        if self.radius == other.radius:
            return True
        else:
            return False
    
    def __repr__(self):
        """Returns information about the size and position of a circle."""

        return f"The radius of the circle is: {self.radius} length units. The geometric center is: ({self.x_coordinate}, {self.y_coordinate})."


    #GETTERS AND SETTERS
    
    @property
    def radius(self) -> float:
        """A getter method, returning the private radius."""
        return self._radius
   
    @radius.setter
    def radius(self, radius:float) -> None:
        """
        Validates that the radius is numerical and above zero, and assigns it to a private variable.
        
        Parameters
        ----------
        radius : float
            The radius of a circle.
        
        Raises
        ------
        TypeError
            If radius is not int or float.
        ValueError
            If radius is 0 or below.

        Returns
        -------
        None
        """
        
        self._radius = Geometry.validation_numerical_above_zero(radius)