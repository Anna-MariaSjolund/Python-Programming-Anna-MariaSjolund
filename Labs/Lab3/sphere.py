from circle import Circle
import math
import matplotlib.pyplot as plt
import numpy as np

class Sphere(Circle):
    """
    A class used for representing spheres in a coordinate system.
    
    Attributes
    ----------
    radius : float
        The radius of a sphere.
    x_coordinate : float
        The x-coordinate at the centre of a sphere (default 0).
    y_coordinate : float
        The y-coordinate at the centre of a sphere (default 0).
    z_coordinate : float
        The z_coordinate at the centre of a sphere (default 0).
    
    Methods
    -------
    translate(x_new_value : float, y_new_value : float, z_new_value : float) -> None:
        Sets the x, y and z-coordinates to new values.
    area() -> float
        Calculates the surface area of a sphere.
    volume() -> float:
        Calculates the volume of a sphere.
    is_inside(x_value : float, y_value : float, z_value : float) -> bool
        Checks if a point (x, y, z) is inside a sphere.
    __repr__() -> str
        Returns information about the size and position of a sphere.
    """

    def __init__(self, radius:float, x_coordinate:float=0, y_coordinate:float=0, z_coordinate:float=0) -> None:
        """
        Parameters
        ----------
        radius : float
            The radius of a circle.
        x_coordinate : float
            The x-coordinate at the centre of a sphere (default 0).
        y_coordinate : float
            The y-coordinate at the centre of a sphere (default 0).
        z_coordinate : float
            The z_coordinate at the centre of a sphere (default 0).
        """

        super().__init__(radius, x_coordinate, y_coordinate)
        self.z_coordinate = z_coordinate


    #METHODS

    def translate(self, x_new_value, y_new_value, z_new_value) -> None:
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
        self._z_coordinate = Circle.validation_numerical(z_new_value)

    def area(self) -> float:
        """Calculates the surface area of a sphere."""

        return 4*math.pi*(self.radius**2)

    def volume(self) -> float:
        """Calculates the volume of a sphere."""

        return 4/3*math.pi*(self.radius**3)

    def is_inside(self, x_value:float=0, y_value:float=0, z_value:float=0) -> bool:
        """
        Checks if a point (x, y, z) is inside a sphere.

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
            If point is in the sphere.
        False
            If point is not in the sphere.
        """      
        
        super().is_inside(x_value, y_value)
        _ = Circle.validation_numerical(z_value)

        eucl_distance = math.sqrt((self.x_coordinate - x_value)**2 + (self.y_coordinate - y_value)**2 + (self.z_coordinate - z_value)**2)
        if eucl_distance <= self.radius:
            return True
        else: 
            return False

    def plot_figure(self, fixed_scale10=False): #Reference: https://stackoverflow.com/questions/40460960/how-to-plot-a-sphere-when-we-are-given-a-central-point-and-a-radius-size
        """Create a plot of the sphere in 3D."""

        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
        x = self.x_coordinate + self.radius * np.cos(u) * np.sin(v)
        y = self.y_coordinate + self.radius * np.sin(u) * np.sin(v)
        z = self.z_coordinate + self.radius * np.cos(v)

        ax.plot_surface(x, y, z, cmap="Blues")

        lowest_x = self.x_coordinate-self.radius
        highest_x = self.x_coordinate+self.radius
        lowest_y = self.y_coordinate-self.radius
        highest_y = self.y_coordinate+self.radius
        lowest_z = self.z_coordinate-self.radius
        highest_z = self.z_coordinate+self.radius

        if fixed_scale10 == True and lowest_x >= -10 and lowest_y >= -10 and lowest_z >= -10 and highest_x <= 10 and highest_y <= 10 and highest_z <= 10:
            ax.set(xlim=(-10, 10), ylim=(-10, 10), zlim=(-10, 10))
            ticks_list=[-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10]
            ax.set(xticks=ticks_list, yticks=ticks_list, zticks=ticks_list)
        
        ax.set(xlabel='x', ylabel='y', zlabel='z')
        ax.set_title("Sphere")

        plt.show()

    def __repr__(self) -> str:
        """Returns information about the size and position of a circle."""

        return f"The radius of the sphere is: {self.radius} length units. The center is: ({self.x_coordinate}, {self.y_coordinate}, {self.z_coordinate})."


    #GETTERS AND SETTERS

    @property
    def z_coordinate(self):
        """A getter method, returning the private z_coordinate."""

        return self._z_coordinate

    @z_coordinate.setter
    def z_coordinate(self, z_coordinate:float) -> None:
        """
        Validates that the z-coordinate is numerical, and assigns it to a private variable.
        
        Parameters
        ----------
        z_coordinate : float
            The z-coordinate of a sphere.
        
        Raises
        ------
        TypeError
            If z-coordinate is not int or float.

        Returns
        -------
        None
        """

        self._z_coordinate = Circle.validation_numerical(z_coordinate)