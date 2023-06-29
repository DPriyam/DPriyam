import unittest
 
# code to be tested
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def get_perimeter(self):
    	return 2*(self.width + self.height)
    	
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height
        
    def sum_area_perimeter(self):
    	return self.get_area() + self.get_perimeter()
 
# The test based on unittest module
class TestGetDimensionsRectangle(unittest.TestCase):
    def test(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.sum_area_perimeter(), 16, "incorrect sum")
 
    
# run the test
if __name__ == '__main__':
	print("Integration Test Started")
	unittest.main()
