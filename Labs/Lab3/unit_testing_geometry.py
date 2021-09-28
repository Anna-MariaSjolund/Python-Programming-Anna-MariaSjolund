from geometry import Geometry
import unittest

class TestGeometry(unittest.TestCase):
    def setUp(self) -> None:
        self.x_coordinate, self.y_coordinate = 3, -3
    
    def create_geometry_object(self) -> "Geometry":
        return Geometry(self.x_coordinate, self.y_coordinate)

    def test_create_geometry_object(self):
        geo = self.create_geometry_object()
        self.assertEqual((geo.x_coordinate, geo.y_coordinate), (self.x_coordinate, self.y_coordinate))

    def test_validation_numerical(self):
        with self.assertRaises(TypeError):
            variable = Geometry.validation_numerical("3")
    
    def test_validation_numerical_above_zero(self):
        with self.assertRaises(TypeError):
            variable = Geometry.validation_numerical_above_zero("3")
        with self.assertRaises(ValueError):
            variable = Geometry.validation_numerical_above_zero(-3)

    def test_invalid_string_in_parameter(self):
        with self.assertRaises(TypeError):
            geo = Geometry("3", "-3")
    
    def test_translate(self):
        geo = self.create_geometry_object()
        geo.translate(4, -2)
        self.assertEqual((geo.x_coordinate, geo.y_coordinate), (4, -2))
    
    def test_translate_x_is_numerical(self):
        geo = self.create_geometry_object()        
        with self.assertRaises(TypeError):
            geo.translate("4", 2)
    
    def test_translate_y_is_numerical(self):
        geo = self.create_geometry_object()
        with self.assertRaises(TypeError):
            geo.translate(2, "4")

if __name__ == "__main__":
    unittest.main() 