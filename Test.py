import unittest
from Factorial import factorial
class Testfactorial(unittest.TestCase):
    def test_fact1(self):
        result = factorial(5)
        self.assertEqual(result,120)
    def test_fact2(self):
        result = factorial(6)
        self.assertEqual(result,720)
    def test_fact3(self):
        result = factorial(7)
        self.assertEqual(result,5040)
    def test_fact4(self):
        result = factorial(4)
        self.assertEqual(result,23)
    def test_fact5(self):
        result = factorial(3)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
