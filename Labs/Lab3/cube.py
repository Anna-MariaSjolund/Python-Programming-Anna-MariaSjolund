from rectangle import Rectangle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


class Cube(Rectangle):
    """
    A class used for representing cubes in a coordinate system.
    
    Attributes
    ----------
    side : float
        The length of the side of the cube.
    x_coordinate : float
        The x-coordinate at the centre of a cube (default 0).
    y_coordinate : float
        The y-coordinate at the centre of a cube (default 0).
    z_coordinate : float
        The z-coordinate at the centre of a cube (default 0).
    
    Methods
    -------
    area() -> float
        Calculates the surface area of a cube.
    volume() -> float:
        Calculates the volume of a cube.
    is_inside(x_value : float, y_value : float, z_value : float) -> bool
        Checks if a point (x, y, z) is inside a cube.
    __repr__() -> str
        Returns information about the size and position of a cube.
    """
    def __init__(self, side : float, x_coordinate:float=0, y_coordinate:float=0, z_coordinate:float=0) -> None: 
        """
        Parameters
        ----------
        side : float
            The length of the side of the cube.
        x_coordinate : float
            The x-coordinate at the centre of a sphere (default 0).
        y_coordinate : float
            The y-coordinate at the centre of a sphere (default 0).
        z_coordinate : float
            The z_coordinate at the centre of a sphere (default 0).
        """

        super().__init__(side, side, x_coordinate, y_coordinate) #https://www.pythonlikeyoumeanit.com/Module4_OOP/Inheritance.html
        self.side = side
        self.z_coordinate = z_coordinate


    #METHODS

    def translate(self, x_new_value, y_new_value, z_new_value) -> float:
        """
        Sets the x, y and z-coordinates to new values.

        Parameters
        ----------
        x_new_value : float
            The new value for the x-coordinate.
        y_new_value : float
            The new value for the y-coordinate.
        z_new_value : float
            The new value for the z-coordinate.

        Raises
        ------
        TypeError
            If value is not int or float.       

        Returns
        -------
        None
        """

        super().translate(x_new_value, y_new_value)
        self._z_coordinate = Rectangle.validation_numerical(z_new_value)
        
    def area(self) -> float:
        """Calculates the surface area of a cube."""

        return 6*(self.side**2)

    def volume(self) -> float:
        """Calculates the volume of a cube."""

        return self.side**3

    def is_inside(self, x_value:float, y_value:float, z_value:float) -> bool:
        """
        Checks if a point (x, y, z) is inside a cube.

        Parameters
        ----------
        x_value : float
            The x-value of the point.
        y_value : float
            The y-value of the point.
        z_value : float
            The z-value of the point.
        
        Raises
        ------
        TypeError
            If value is not int or float.
        
        Returns
        -------
        True
            If point is in the cube.
        False
            If point is not in the cube.
        """

        super().is_inside(x_value, y_value)
        _ = Rectangle.validation_numerical(z_value)
        
        if ((self.x_coordinate-self.side/2) <= x_value <= (self.x_coordinate+self.side/2) 
            and (self.y_coordinate-self.side/2) <= y_value <= (self.y_coordinate+self.side/2) 
            and (self.z_coordinate-self.side/2) <= z_value <= (self.z_coordinate+self.side/2)):
            return True
        else:
            return False

    def plot_figure(self, fixed_scale10=False):
        """Plot a cube in 3D."""
        def cuboid_data(coordinates, size):
            # code taken from
            # https://stackoverflow.com/a/35978146/4124317
            # suppose axis direction: x: to left; y: to inside; z: to upper
            # get the length, width, and height
            l, w, h = size, size, size
            x = [[coordinates[0], coordinates[0] + l, coordinates[0] + l, coordinates[0], coordinates[0]],  
                [coordinates[0], coordinates[0] + l, coordinates[0] + l, coordinates[0], coordinates[0]],  
                [coordinates[0], coordinates[0] + l, coordinates[0] + l, coordinates[0], coordinates[0]],  
                [coordinates[0], coordinates[0] + l, coordinates[0] + l, coordinates[0], coordinates[0]]]  
            y = [[coordinates[1], coordinates[1], coordinates[1] + w, coordinates[1] + w, coordinates[1]],  
                [coordinates[1], coordinates[1], coordinates[1] + w, coordinates[1] + w, coordinates[1]],  
                [coordinates[1], coordinates[1], coordinates[1], coordinates[1], coordinates[1]],          
                [coordinates[1] + w, coordinates[1] + w, coordinates[1] + w, coordinates[1] + w, coordinates[1] + w]]   
            z = [[coordinates[2], coordinates[2], coordinates[2], coordinates[2], coordinates[2]],                       
                [coordinates[2] + h, coordinates[2] + h, coordinates[2] + h, coordinates[2] + h, coordinates[2] + h],   
                [coordinates[2], coordinates[2], coordinates[2] + h, coordinates[2] + h, coordinates[2]],               
                [coordinates[2], coordinates[2], coordinates[2] + h, coordinates[2] + h, coordinates[2]]]               
            return np.array(x), np.array(y), np.array(z)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_aspect('auto')

        X, Y, Z = cuboid_data((self.x_coordinate-self.side/2, self.y_coordinate-self.side/2, self.z_coordinate-self.side/2), self.side)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1)

        lowest_x = self.x_coordinate-self.side/2
        highest_x = self.x_coordinate+self.side/2
        lowest_y = self.y_coordinate-self.side/2
        highest_y = self.y_coordinate+self.side/2
        lowest_z = self.z_coordinate-self.side/2
        highest_z = self.z_coordinate+self.side/2

        if fixed_scale10 == True and lowest_x >= -10 and lowest_y >= -10 and lowest_z >= -10 and highest_x <= 10 and highest_y <= 10 and highest_z <= 10:
            ax.set(xlim=(-10, 10), ylim=(-10, 10), zlim=(-10, 10))
            ticks_list=[-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10]
            ax.set(xticks=ticks_list, yticks=ticks_list, zticks=ticks_list)

        ax.set(xlabel='x', ylabel='y', zlabel='z')
        ax.set_title("Cube")

        plt.show()

    def __repr__(self):
        """Returns information about the size and position of a cube."""

        return f"The cube has a side of {self.side} length units. The geometric center is: ({self.x_coordinate}, {self.y_coordinate}, {self.z_coordinate})."


    #GETTERS AND SETTERS

    @property
    def side(self) -> float:
        """A getter method, returning the private side."""

        return self._side

    @property
    def z_coordinate(self) -> float:
        """A getter method, returning the private z_coordinate."""

        return self._z_coordinate
    
    @side.setter
    def side(self, side) -> None:
        """
        Validates that the side is numerical and above zero, and assigns it to a private variable.
        
        Parameters
        ----------
        side : float
            The length of the side of the cube.
        
        Raises
        ------
        TypeError
            If side is not int or float.
        ValueError
            If side is 0 or below.

        Returns
        -------
        None
        """

        self._side = Rectangle.validation_numerical_above_zero(side)

    @z_coordinate.setter
    def z_coordinate(self, z_coordinate:float) -> None:
        """
        Validates that the z-coordinate is numerical, and assigns it to a private variable.
        
        Parameters
        ----------
        z_coordinate : float
            The z-coordinate of a cube.
        
        Raises
        ------
        TypeError
            If z-coordinate is not int or float.

        Returns
        -------
        None
        """

        self._z_coordinate = Rectangle.validation_numerical(z_coordinate)
