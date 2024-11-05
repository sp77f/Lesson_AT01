import unittest
from main import add, sub, mul, div, check

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertNotEqual(add(1,2), 2)

    def test_sub(self):
        self.assertEqual(sub(2,3), -1)
        self.assertNotEqual(sub(4,2), 1)

    def test_mul(self):
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(1,2), 2)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, div, 6, 0)

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(not check(3))
if __name__ == '__main__':
    unittest.main()