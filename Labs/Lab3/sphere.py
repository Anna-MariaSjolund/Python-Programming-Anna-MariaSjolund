from circle import Circle
import math

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