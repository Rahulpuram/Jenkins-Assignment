import unittest
from Factorial import factorial
class Testfactorial(unittest.TestCase):
    def test_fact1(self):
        result = factorial(5)
        self.assertEqual(result,120)
    def test_fact2(self):
        result = factorial(6)
        self.assertEqual(result,720)

if __name__ == '__main__':
    unittest.main()
