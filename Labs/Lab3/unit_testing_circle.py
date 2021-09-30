from geometry import Geometry
from circle import Circle
from rectangle import Rectangle
import unittest

class TestGeometry(unittest.TestCase):
    """Tests the static methods in the Geometry class."""

    def test_validation_numerical(self):
        """Tests if a TypeError is generated when entering a str."""

        with self.assertRaises(TypeError):
            Geometry.validation_numerical("3")
    
    def test_validation_numerical_above_zero_Type_Error(self):
        """Tests if a TypeError is raised when entering a str."""

        with self.assertRaises(TypeError):
            Geometry.validation_numerical_above_zero("3")

    def test_validation_numerical_above_zero_Value_Error(self):
        """Tests if a ValueError is generated when entering a value of 0 and below."""
        
        with self.assertRaises(ValueError):
            Geometry.validation_numerical_above_zero(0)
        with self.assertRaises(ValueError):
            Geometry.validation_numerical_above_zero(-3)

class TestCircle(unittest.TestCase):
    """Tests the Circle class."""


    #CREATION OF CIRCLE OBJECT

    def setUp(self) -> None:
        """Initialises values to use for the radius, x-coordinate and y-coordinate."""

        self.radius, self.x_coordinate, self.y_coordinate = 2.5, 3, -3
    
    def create_circle_object(self) -> "Circle":
        """Returns a Circle object, using the values from the setUp function."""

        return Circle(self.radius, self.x_coordinate, self.y_coordinate)

    
    #TESTS CREATION OF CIRCLE OBJECT

    def test_create_circle_object(self):
        """Tests if a Circle object has been set up with the correct values."""

        circ = self.create_circle_object()
        self.assertEqual((circ.radius, circ.x_coordinate, circ.y_coordinate), (self.radius, self.x_coordinate, self.y_coordinate))

    def test_invalid_string_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameters."""

        with self.assertRaises(TypeError):
            Circle("3", 3, -3)
        with self.assertRaises(TypeError):
            Circle(3, "3", -3)
        with self.assertRaises(TypeError):
            Circle(3, 3, "-3")
    
    def test_radius_zero_or_below(self):
        """Tests if a ValueError is raised when trying to set the radius to a value below 0."""

        with self.assertRaises(ValueError):
            Circle(-1, 2, 3)
    

    #TESTS METHOD INHERITED FROM THE GEOMETRY CLASS

    def test_translate(self):
        """Tests if the x and y-coordinates are changed correctly."""

        circ = self.create_circle_object()
        circ.translate(4, -2)
        self.assertEqual((circ.x_coordinate, circ.y_coordinate), (4, -2))
    
    def test_translate_str_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameter."""

        circ = self.create_circle_object()        
        with self.assertRaises(TypeError):
            circ.translate("4", 2)
        with self.assertRaises(TypeError):
            circ.translate(4, "2")
    
    #TESTS CIRCLE METHODS

    def test_area(self):
        """Tests that the area is correctly calculated."""

        circ = self.create_circle_object()
        self.assertAlmostEqual(circ.area(), 19.63, places=2)
    
    def test_circumference(self):
        """Tests that the circumference is correctly calculated."""

        circ = self.create_circle_object()
        self.assertAlmostEqual(circ.circumference(), 15.71, places=2)
    
    def test_is_inside_true(self):
        """Tests if points that should be inside/on the boarder of the circle are correctly classified."""

        circ = self.create_circle_object()
        self.assertEqual(circ.is_inside(2, -2), True)
        self.assertEqual(circ.is_inside(3, -5.5), True)
    
    def test_is_inside_false(self):
        """Tests if points that should not be inside/on the boarder of the circle are correctly classified."""

        circ = self.create_circle_object()
        self.assertEqual(circ.is_inside(3, -5.6), False)

    def test_is_inside_str_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameter."""

        circ = self.create_circle_object()
        with self.assertRaises(TypeError):
            circ.is_inside("2", 3)
        with self.assertRaises(TypeError):
            circ.is_inside(2, "3")

    def test_equality_true(self):
        """Tests the overloaded equality operator, using two Circles with same sized radiuses."""

        circ1 = Circle(3, -2, 3)
        circ2 = Circle(3, 3, -2)
        self.assertEqual(circ1 == circ2, True)

    def test_equality_false(self):
        """Tests the overloaded equality operator, using two Circles with different radiuses."""        

        circ1 = Circle(3, -2, 3)
        circ2 = Circle(4, -2, 3)
        self.assertEqual(circ1 == circ2, False)

    def test_equality_not_same_type(self):
        """Tests the overloaded equality operator, using two different geometrical figures."""        

        circ = Circle(3, -2, 3)
        rectang = Rectangle(4, 3, -2, 3)
        self.assertEqual(circ == rectang, False)

if __name__ == "__main__":
    unittest.main() 