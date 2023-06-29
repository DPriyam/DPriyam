from functions import function1, function2, function3
import unittest

class IntegralTest(unittest.TestCase):

    def test_integral(self):
        val= input("Enter the value to test ")
        val=int(val)
        result = function1(val)
        result = function2(result)
        result = function3(result)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()
