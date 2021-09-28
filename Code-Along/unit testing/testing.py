from vector import Vector
import unittest

#v1 = Vector(1,1)
#print(v1)

class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2

    def create_2D_vector(self) -> "Vector":
        return Vector(self.x, self.y)

    #Testing starts here - all tests must start with the word test_

    #Tests creating vectors
    def test_create_2D_vector(self) -> None:
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))
    
    def test_create_5D_vector(self):
        v = Vector(1, 2, 3, 4, 5)
        self.assertEqual(v.numbers, (1, 2, 3, 4, 5))
    
    def test_empty_vector(self): 
        #With the following the code will not crash, but 
        with self.assertRaises(ValueError): #We except it to throw a ValueError, and if it does we have passed the test
            v = Vector()
    
    def test_create_invalid_vector(self):
        with self.assertRaises(TypeError):
            v = Vector("1", "Two")
    
    #test __eq__ ==
    def test_2_vector_equal(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1, 2)
        self.assertEqual(v1, v2)
    
    def test2_vector_equal(self):
        v1 = self.create_2D_vector()
        v2 = Vector(-1, 2)
        self.assertNotEqual(v1, v2)
    
    def test_2_vecs_equal_diff_dim(self): #If two vectors are not equal, because they have not the same number of dimension
        v1 = self.create_2D_vector()
        v2 = Vector(1, 2, 3)
        with self.assertRaises(TypeError):
            v1 == v2
    
    def test_get_item(self):
        v = self.create_2D_vector()
        self.assertEqual(self.x, v[0])
    
    def test_get_item_5D_vector(self):
        v = Vector(1, 2, 3, 4, 5)
        #We should not test several things in one test, because we then do not know what failed
        #However the following is okay, since it is the same test we test several times
        for i in range(5): #
            self.assertEqual(i+1, v[i])

    def test_multiply_vector_scalar(self):
        v = self.create_2D_vector()
        v2 = v*5 #We create a new Vector by multiplying the old vector (1, 2) with 5 and checks if it is equal to (5, 10)
        self.assertEqual(v2, (Vector(5,10)))
    
    def test_multiply_scalar_vector(self):
        v = self.create_2D_vector()
        v2 = 5*v
        self.assertEqual(v2, Vector(5, 10))   
    

#If this is true, run unittest.main()
#We can run Python code as a stand alone script (it will get the value __main__)
if __name__ == "__main__":
    unittest.main() #Then all of the tests will be run