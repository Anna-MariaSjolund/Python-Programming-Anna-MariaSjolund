from abc import ABC, abstractmethod

class Geometry(ABC):
    """
    An abstract class, used for representing geometrical figures in a coordinate system.
    
    Attributes
    ----------
    x_coordinate : float
        The x-coordinate at the centre of a geometrical figure (default 0).
    y_coordinate : float
        The y-coordinate at the centre of a geometrical figure (default 0).
    
    Instance Methods
    ----------------
    translate(x_new_value:float, y_new_value:float) -> None
        Sets the x-coordinate and the y-coordinate to new values.
    
    Abstract Methods
    ----------------
    area() -> float
        Calculates the area of a geometrical figure.
    circumference() -> float
        Calculates the circumference of a geometrical figure.
    is_inside() -> bool
        Checks if a point (x, y) is inside a geometrical figure.
    plot_figure()
        Plots a geometrical figure in a coordinate system. 
    __eq__() -> bool
        Checks if two geometrical figures are congruent.
    __repr__() -> str
        Returns information about the size and position of a geometrical figure.
    
    Static Methods
    --------------
    validation_numerical(value:float) -> float
        Validates that a value is numerical.
    validation_numerical_above_zero(value:float) -> float
        Validates that a value is numerical and above zero.
    """

    def __init__(self, x_coordinate:float=0, y_coordinate:float=0) -> None:
        """
        Parameters
        ----------
        x_coordinate:float
            The x-coordinate at the centre of a geometrical figure (default 0).
        y_coordinate:float
            The y-coordinate at the centre of a geometrical figure (default 0).
        """

        self.x_coordinate = x_coordinate
        self.y_coordinate  = y_coordinate


    #INSTANCE METHODS

    def translate(self, x_new_value:float, y_new_value:float) -> None:
        """
        Sets the x-coordinate and the y-coordinate to new values.

        Parameters
        ----------
        x_new_value : float
            The new value for the x-coordinate.
        y_new_value : float
            The new value for the y-coordinate.

        Raises
        ------
        TypeError
            If value is not int or float.       

        Returns
        -------
        None
        """

        self._x_coordinate = Geometry.validation_numerical(x_new_value)
        self._y_coordinate = Geometry.validation_numerical(y_new_value)


    #ABSTRACT METHODS

    @abstractmethod
    def area(self) -> float:
        """Calculates the area of a geometrical figure."""

        pass

    @abstractmethod
    def circumference(self) -> float:
        """Calculates the circumference of a geometrical figure."""

        pass

    @abstractmethod
    def is_inside(self) -> bool:
        """Checks if a point (x, y) is inside a geometrical figure."""

        pass

    def plot_figure(self):
        "Plots a geometrical figure in a coordinate system."

        pass

    @abstractmethod
    def __eq__(self) -> bool:
        """Checks if two geometrical figures are congruent."""

        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Returns information about the size and position of a geometrical figure."""

        pass


    #STATIC METHODS

    @staticmethod
    def validation_numerical(value:float) -> float:
        """
        Validates that a value is numerical.
        
        Parameters
        -----------
        value : float
            The value to validate. Expected to be int or float.
             
        Raises
        ------
        TypeError
            If value is not int or float.

        Returns
        -------
        value : float
            If no error has occured, the value is returned.
        """

        if not isinstance(value, (int, float)):
            raise TypeError(f"Please enter an int or a float, not a {type(value)}.")
        else: 
            return value
    
    @staticmethod
    def validation_numerical_above_zero(value) -> float:
        """
        Validates that a value is numerical and above 0.
        
        Parameters
        -----------
        value : float
            The value to validate. Expected to be int or float.
        
        Raises
        ------
        TypeError
            If value is not int or float.
        ValueError
            If value is 0 or below.

        Returns
        -------
        value : float
            If no error has occured, the value is returned.
        """

        if not isinstance(value, (int, float)):
            raise TypeError(f"Please enter an int or a float, not a {type(value)}.")
        elif value <= 0:
            raise ValueError("The value has to be above 0.")
        else:
            return value    


    #GETTERS AND SETTERS

    @property
    def x_coordinate(self) -> float:
        """A getter method, returning the private x-coordinate."""

        return self._x_coordinate

    @property
    def y_coordinate(self) -> float:
        """A getter method, returning the private y-coordinate."""

        return self._y_coordinate
    
    @x_coordinate.setter
    def x_coordinate(self, x_coordinate:float) -> None:
        """
        Validates that the x-coordinate is numerical, and assigns it to a private variable.
        
        Parameters
        ----------
        x_coordinate : float
            The x-coordinate at the centre of a geometrical figure (default 0).
        
        Raises
        ------
        TypeError
            If x-coordinate is not int or float.

        Returns
        -------
        None
        """

        self._x_coordinate = Geometry.validation_numerical(x_coordinate)
    
    @y_coordinate.setter
    def y_coordinate(self, y_coordinate:float) -> None:
        """Validates that the y-coordinate is numerical, and assigns it to a private variable.
        
        Parameters
        ----------
        y_coordinate : float
            The y-coordinate at the centre of a geometrical figure (default 0).
        
        Raises
        ------
        TypeError
            If y-coordinate is not int or float.

        Returns
        -------
        None
        """

        self._y_coordinate = Geometry.validation_numerical(y_coordinate)