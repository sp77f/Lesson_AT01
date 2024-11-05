import unittest
from hw_at01 import div_rem

class Test(unittest.TestCase):
    def test_div_rem(self):
        self.assertEqual(div_rem(6, 3), 0)
        self.assertEqual(div_rem(70, 3), 1)
        self.assertRaises(ValueError, div_rem, 6, 0)


if __name__ == '__main__':
    unittest.main()
