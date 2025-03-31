# Using unittest
import unittest
from mymodule import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)

if __name__ == '__main__':
    unittest.main()
