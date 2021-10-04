from rectangle import Rectangle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

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
    plot_figure(fixed_scale10 : bool, point : tuple) -> None
        Creates a Cube object in 3D, in a coordinate system.
    Creates a Sphere object in 3D, in a coordinate system.
    __repr__() -> str
        Returns information about the size and position of a cube.
    """

    def __init__(self, side:float, x_coordinate:float=0, y_coordinate:float=0, z_coordinate:float=0) -> None: 
        """
        Parameters
        ----------
        side : float
            The length of the side of the cube.
        x_coordinate : float
            The x-coordinate at the centre of a cube (default 0).
        y_coordinate : float
            The y-coordinate at the centre of a cube (default 0).
        z_coordinate : float
            The z-coordinate at the centre of a cube (default 0).
        """

        super().__init__(side, side, x_coordinate, y_coordinate) #The side (length) will be passed in as both width and height - inherited from the Rectangle class. Reference: https://www.pythonlikeyoumeanit.com/Module4_OOP/Inheritance.html
        self.side = side
        self.z_coordinate = z_coordinate


    #METHODS

    def translate(self, x_new_value:float, y_new_value:float, z_new_value:float) -> float:
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

        super().translate(x_new_value, y_new_value) #Inherits the translate-method from the Rectangle class  - validates and sets the x and y-coordinates. Reference: https://www.geeksforgeeks.org/python-call-parent-class-method/
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
        Rectangle.validation_numerical(z_value)
        
        if ((self.x_coordinate-self.side/2) <= x_value <= (self.x_coordinate+self.side/2) 
            and (self.y_coordinate-self.side/2) <= y_value <= (self.y_coordinate+self.side/2) 
            and (self.z_coordinate-self.side/2) <= z_value <= (self.z_coordinate+self.side/2)):
            return True
        else:
            return False

    def plot_figure(self, fixed_scale10:bool=False, point:tuple=None) -> None: #Reference: https://stackoverflow.com/questions/33540109/plot-surfaces-on-a-cube/33542678
        """
        Creates a Cube object in 3D, in a coordinate system. 
        
        Arguments
        ---------
        fixed_scale10 : bool
            If True and if the edges of the cube are located between -10 and 10 on the x, y and z-axis,
                the cube will be shown in a coordinate system scaled between -10 and 10.
            If False or if the edges of the cube are not located between -10 and 10 on the x, y and z-axis, 
                the plot will zoom in on the cube.
            (default False)
        point : tuple
            Plots a point (x, y, z) in the coordinate system (default None).

        Returns 
        -------
        None
        """

        #Sets up the figure and axes
        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(projection="3d")

        #Returns three arrays of spherical coordinates, for the X, Y and Z-axis
        phi = np.arange(1, 10, 2) * np.pi / 4
        Phi, Theta = np.meshgrid(phi, phi)
        X = (np.cos(Phi) * np.sin(Theta)) * self.side + self.x_coordinate
        Y = (np.sin(Phi) * np.sin(Theta)) * self.side + self.y_coordinate
        Z = (np.cos(Theta) / np.sqrt(2)) * self.side + self.z_coordinate

        #Plots the surface of the cube
        ax.plot_surface(X, Y, Z, cmap="Greens", alpha=0.3)

        #Plots a point at the specified coordinates 
        if point != None:
            ax.plot(point[0], point[1], point[2], "ko")
        
        #Creates variables for the edges of the cube
        lowest_x = self.x_coordinate-self.side/2
        highest_x = self.x_coordinate+self.side/2
        lowest_y = self.y_coordinate-self.side/2
        highest_y = self.y_coordinate+self.side/2
        lowest_z = self.z_coordinate-self.side/2
        highest_z = self.z_coordinate+self.side/2

        #Sets the scale, depending on the values of the cube and if fixed_scale10 is set to True
        if fixed_scale10 == True and lowest_x >= -10 and lowest_y >= -10 and lowest_z >= -10 and highest_x <= 10 and highest_y <= 10 and highest_z <= 10:
            ax.set(xlim=(-10, 10), ylim=(-10, 10), zlim=(-10, 10))

        #Sets title and labels
        ax.set(title=f"Side Length: {self.side}, Center: ({self.x_coordinate}, {self.y_coordinate}, {self.z_coordinate})", xlabel="x", ylabel="y", zlabel="z")

        plt.show()

    def __repr__(self):
        """Returns information about the size and position of a cube."""

        return f"The cube has a side of {self.side} length units. The geometric center is: ({self.x_coordinate}, {self.y_coordinate}, {self.z_coordinate})."


    #GETTERS AND SETTERS

    @property
    def side(self) -> float:
        """Returns the side, as a private variable.."""

        return self._side

    @property
    def z_coordinate(self) -> float:
        """Returns the z-coordinate, as a private variable."""

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