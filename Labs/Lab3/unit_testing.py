from geometry import Geometry
from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube
import unittest


#TESTS ABSTRACT BASE CLASS GEOMETRY

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


#TESTS CIRCLE SUBCLASS (AND TRANSLATE METHOD INHERITED FROM THE GEOMETRY CLASS)

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

    def test_create_circle_object_without_x_y(self):
        """Tests if a Circle object has been set up correctly, when not entering the x and y-coordinates."""

        circ = Circle(2)
        self.assertEqual((circ.radius, circ.x_coordinate, circ.y_coordinate), (2, 0, 0))

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


#TESTS RECTANGLE SUBCLASS

class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class."""

    #CREATION OF RECTANGLE OBJECT

    def setUp(self) -> None:
        """Initialises values to use for the length, width, x-coordinate and y-coordinate."""

        self.length, self.width, self.x_coordinate, self.y_coordinate = 4, 3, 3, -3
    
    def create_rectangle_object(self) -> "Rectangle":
        """Returns a Rectangle object, using the values from the setUp function."""

        return Rectangle(self.length, self.width, self.x_coordinate, self.y_coordinate)

    #TESTS CREATION OF RECTANGLE OBJECT

    def test_create_rectangle_object(self):
        """Tests if a Rectangle object has been set up with the correct values."""

        rect = self.create_rectangle_object()
        self.assertEqual((rect.length, rect.width, rect.x_coordinate, rect.y_coordinate), (self.length, self.width, self.x_coordinate, self.y_coordinate))

    def test_create_rectangle_object_without_x_y(self):
        """Tests if a Rectangle object has been set up correctly, when not entering the x and y-coordinates."""

        rect = Rectangle(2, 3)
        self.assertEqual((rect.length, rect.width, rect.x_coordinate, rect.y_coordinate), (2, 3, 0, 0))

    def test_invalid_string_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameters."""

        with self.assertRaises(TypeError):
            Rectangle("3", 3, -3, 3)
        with self.assertRaises(TypeError):
            Rectangle(3, "3", -3, 3)
        with self.assertRaises(TypeError):
            Rectangle(3, 3, "-3", 3)
        with self.assertRaises(TypeError):
            Rectangle(3, 3, -3, "3")
    
    def test_length_zero_or_below(self):
        """Tests if a ValueError is raised when trying to set the length to a value below 0."""

        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4)

    def test_width_zero_or_below(self):
        """Tests if a ValueError is raised when trying to set the width to a value below 0."""

        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4)
    
    #TESTS RECTANGLE METHODS

    def test_area(self):
        """Tests that the area is correctly calculated."""

        rect = self.create_rectangle_object()
        self.assertEqual(rect.area(), 12)
    
    def test_circumference(self):
        """Tests that the circumference is correctly calculated."""

        rect = self.create_rectangle_object()
        self.assertEqual(rect.circumference(), 14)
    
    def test_is_inside_true(self):
        """Tests if points that should be inside/on the boarder of the rectangle are correctly classified."""

        rect = self.create_rectangle_object()
        self.assertEqual(rect.is_inside(2, -2), True)
        self.assertEqual(rect.is_inside(5, -4.5), True)
    
    def test_is_inside_false(self):
        """Tests if points that should not be inside/on the boarder of the rectangle are correctly classified."""

        rect = self.create_rectangle_object()
        self.assertEqual(rect.is_inside(5, -4.6), False)

    def test_is_inside_str_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameter."""

        rect = self.create_rectangle_object()
        with self.assertRaises(TypeError):
            rect.is_inside("2", 3)
        with self.assertRaises(TypeError):
            rect.is_inside(2, "3")

    def test_equality_true(self):
        """Tests the overloaded equality operator, using two Rectangles with same length and width."""

        rect1 = Rectangle(4, 3, 1, 1)
        rect2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rect1 == rect2, True)

    def test_equality_false(self):
        """Tests the overloaded equality operator, using two Rectangle with different length and width."""  

        rect1 = Rectangle(5, 4, 2, 1)
        rect2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rect1 == rect2, False)

    def test_equality_not_same_type(self):
        """Tests the overloaded equality operator, using two different geometrical figures.""" 

        rect = Rectangle(4, 3, -2, 3)
        circ = Circle(3, -2, 3)
        self.assertEqual(rect == circ, False)


#TESTS SPHERE SUBCLASS

class TestSphere(unittest.TestCase):
    """Tests the Sphere class."""

    #CREATION OF SPHERE OBJECT

    def setUp(self) -> None:
        """Initialises values to use for the radius, x, y and z-coordinate."""

        self.radius, self.x_coordinate, self.y_coordinate, self.z_coordinate = 3, 3, -3, 3
    
    def create_sphere_object(self) -> "Sphere":
        """Returns a Sphere object, using the values from the setUp function."""

        return Sphere(self.radius, self.x_coordinate, self.y_coordinate, self.z_coordinate)

    
    #TESTS CREATION OF SPHERE OBJECT

    def test_create_sphere_object(self):
        """Tests if a Sphere object has been set up with the correct values."""

        sph = self.create_sphere_object()
        self.assertEqual((sph.radius, sph.x_coordinate, sph.y_coordinate, sph.z_coordinate), (self.radius, self.x_coordinate, self.y_coordinate, self.z_coordinate))

    def test_create_sphere_object_without_x_y_z(self):
        """Tests if a Sphere object has been set up correctly, when not entering the x, y and z-coordinates."""

        sph = Sphere(2)
        self.assertEqual((sph.radius, sph.x_coordinate, sph.y_coordinate, sph.z_coordinate), (2, 0, 0, 0))

    def test_invalid_string_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameters."""

        with self.assertRaises(TypeError):
            Sphere("3", 3, -3, 3)
        with self.assertRaises(TypeError):
            Sphere(3, "3", -3, 3)
        with self.assertRaises(TypeError):
            Sphere(3, 3, "-3", 3)
        with self.assertRaises(TypeError):
            Sphere(3, 3, -3, "3")
    
    def test_radius_zero_or_below(self):
        """Tests if a ValueError is raised when trying to set the radius to a value below 0."""

        with self.assertRaises(ValueError):
            Sphere(-1, 2, 3, 4)

    #TESTS SPHERE METHODS

    def test_translate(self):
        """Tests if the x, y and z-coordinates are changed correctly."""

        sph = self.create_sphere_object()
        sph.translate(4, -3, -2)
        self.assertEqual((sph.x_coordinate, sph.y_coordinate, sph.z_coordinate), (4, -3, -2))
    
    def test_translate_str_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameter."""

        sph = self.create_sphere_object()        
        with self.assertRaises(TypeError):
            sph.translate("4", 3, 2)
        with self.assertRaises(TypeError):
            sph.translate(4, "3", 2)
        with self.assertRaises(TypeError):
            sph.translate(4, 3, "2")
    
    def test_area(self):
        """Tests that the area is correctly calculated."""

        sph = self.create_sphere_object()
        self.assertAlmostEqual(sph.area(), 113.097, places=3)
    
    def test_circumference(self):
        """Tests that the circumference is correctly calculated."""

        sph = self.create_sphere_object()
        self.assertAlmostEqual(sph.circumference(), 18.850, places=3)
    
    def test_volume(self):
        """Tests that the volume is correctly calculated."""

        sph = self.create_sphere_object()
        self.assertAlmostEqual(sph.volume(), 113.097, places=3)
    
    def test_is_inside_true(self):
        """Tests if points that should be inside/on the boarder of the sphere are correctly classified."""

        sph = self.create_sphere_object()
        self.assertEqual(sph.is_inside(4, -3.5, 4), True)
        self.assertEqual(sph.is_inside(6, -3, 3), True)
    
    def test_is_inside_false(self):
        """Tests if points that should not be inside/on the boarder of the sphere are correctly classified."""

        sph = self.create_sphere_object()
        self.assertEqual(sph.is_inside(6, -3.1, 3), False)

    def test_is_inside_str_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameter."""

        sph = self.create_sphere_object()
        with self.assertRaises(TypeError):
            sph.is_inside("2", 3, 4)
        with self.assertRaises(TypeError):
            sph.is_inside(2, "3", 4)
        with self.assertRaises(TypeError):
            sph.is_inside(2, 3, "4")

    def test_equality_true(self):
        """Tests the overloaded equality operator, using two Spheres with same sized radiuses."""

        sph1 = Sphere(3, -2, 3, 4)
        sph2 = Sphere(3, 3, -2, 4)
        self.assertEqual(sph1 == sph2, True)

    def test_equality_false(self):
        """Tests the overloaded equality operator, using two Spheres with different radiuses."""        

        sph1 = Sphere(3, -2, 3, 4)
        sph2 = Sphere(4, -2, 3, 4)
        self.assertEqual(sph1 == sph2, False)

    def test_equality_not_same_type(self):
        """Tests the overloaded equality operator, using two different geometrical figures."""        

        sph = Sphere(3, -2, 3, 4)
        circ = Circle(3, -2, 3)
        self.assertEqual(sph == circ, False)


#TESTS CUBE SUBCLASS

class TestCube(unittest.TestCase):
    """Tests the Cube class."""

    #CREATION OF CUBE OBJECT

    def setUp(self) -> None:
        """Initialises values to use for the side, x, y and z-coordinate."""

        self.side, self.x_coordinate, self.y_coordinate, self.z_coordinate = 3, 3, -3, 3
    
    def create_cube_object(self) -> "Cube":
        """Returns a Cube object, using the values from the setUp function."""

        return Cube(self.side, self.x_coordinate, self.y_coordinate, self.z_coordinate)

    
    #TESTS CREATION OF CUBE OBJECT

    def test_create_cube_object(self):
        """Tests if a Cube object has been set up with the correct values."""

        cub = self.create_cube_object()
        self.assertEqual((cub.side, cub.x_coordinate, cub.y_coordinate, cub.z_coordinate), (self.side, self.x_coordinate, self.y_coordinate, self.z_coordinate))

    def test_create_cube_object_without_x_y_z(self):
        """Tests if a Cube object has been set up correctly, when not entering the x, y and z-coordinates."""

        cub = Cube(2)
        self.assertEqual((cub.side, cub.x_coordinate, cub.y_coordinate, cub.z_coordinate), (2, 0, 0, 0))

    def test_invalid_string_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameters."""

        with self.assertRaises(TypeError):
            Cube("3", 3, -3, 3)
        with self.assertRaises(TypeError):
            Cube(3, "3", -3, 3)
        with self.assertRaises(TypeError):
            Cube(3, 3, "-3", 3)
        with self.assertRaises(TypeError):
            Cube(3, 3, -3, "3")
    
    def test_radius_zero_or_below(self):
        """Tests if a ValueError is raised when trying to set the side to a value below 0."""

        with self.assertRaises(ValueError):
            Cube(-1, 2, 3, 4)

    #TESTS CUBE METHODS

    def test_translate(self):
        """Tests if the x, y and z-coordinates are changed correctly."""

        cub = self.create_cube_object()
        cub.translate(4, -3, -2)
        self.assertEqual((cub.x_coordinate, cub.y_coordinate, cub.z_coordinate), (4, -3, -2))
    
    def test_translate_str_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameter."""

        cub = self.create_cube_object()        
        with self.assertRaises(TypeError):
            cub.translate("4", 3, 2)
        with self.assertRaises(TypeError):
            cub.translate(4, "3", 2)
        with self.assertRaises(TypeError):
            cub.translate(4, 3, "2")
    
    def test_area(self):
        """Tests that the area is correctly calculated."""

        cub = self.create_cube_object()
        self.assertEqual(cub.area(), 54)
    
    def test_circumference(self):
        """Tests that the circumference is correctly calculated."""

        cub = self.create_cube_object()
        self.assertEqual(cub.circumference(), 12)
    
    def test_volume(self):
        """Tests that the volume is correctly calculated."""

        cub = self.create_cube_object()
        self.assertEqual(cub.volume(), 27)
    
    def test_is_inside_true(self):
        """Tests if points that should be inside/on the boarder of the cube are correctly classified."""

        cub = self.create_cube_object()
        self.assertEqual(cub.is_inside(4, -3.5, 4), True)
        self.assertEqual(cub.is_inside(4.5, -4.5, 4.5), True)
    
    def test_is_inside_false(self):
        """Tests if points that should not be inside/on the boarder of the cube are correctly classified."""

        cub = self.create_cube_object()
        self.assertEqual(cub.is_inside(4.6, -4.5, 4.5), False)

    def test_is_inside_str_in_parameter(self):
        """Tests if a TypeError is raised when entering a str in the parameter."""

        cub = self.create_cube_object()
        with self.assertRaises(TypeError):
            cub.is_inside("2", 3, 4)
        with self.assertRaises(TypeError):
            cub.is_inside(2, "3", 4)
        with self.assertRaises(TypeError):
            cub.is_inside(2, 3, "4")

    def test_equality_true(self):
        """Tests the overloaded equality operator, using two Cubes with same sized sides."""

        cub1 = Cube(3, -2, 3, 4)
        cub2 = Cube(3, 3, -2, 4)
        self.assertEqual(cub1 == cub2, True)

    def test_equality_false(self):
        """Tests the overloaded equality operator, using two Cubes with different sides."""        

        cub1 = Cube(3, -2, 3, 4)
        cub2 = Cube(4, -2, 3, 4)
        self.assertEqual(cub1 == cub2, False)

    def test_equality_not_same_type(self):
        """Tests the overloaded equality operator, using two different geometrical figures."""        

        cub = Cube(3, -2, 3, 4)
        sph = Sphere(3, -2, 3, 4)
        self.assertEqual(cub == sph, False)

if __name__ == "__main__":
    unittest.main() 