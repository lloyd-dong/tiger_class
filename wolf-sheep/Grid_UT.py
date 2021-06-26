import unittest
from Grid import Grid
import numpy as np

class GridTestCase(unittest.TestCase):
    def test_nearby(self):
        grid = Grid(5, 20)
        pts = np.array([[0,0], [2.1, 2.9]])

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
