import unittest

def array_sum(arr):
    return sum(arr)

def array_max(arr):
    return max(arr)

def array_min(arr):
    return min(arr)

class TestStringMethods(unittest.TestCase):
  
    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual(array_sum([1,2,3]),6,"Practice Maths")
    def test_strings_b(self):
        self.assertEqual(array_min([1,2,3]),1,"Check Eye Power!!")
    def test_strings_c(self):
        self.assertEqual(array_max([1,2,3]),3,"Check Eye Power!!")
        
    # Returns True if the string is in upper case.
    
  
if __name__ == '__main__':
    unittest.main()