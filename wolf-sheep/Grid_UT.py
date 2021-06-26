import unittest
from Grid import Grid
import numpy as np
from Animal import Vector

class GridTestCase(unittest.TestCase):
    def test_nearby_0(self):
        grid = Grid(1, 4)
        pts = np.array([[0.4, 0.4], [0.4, 0.6], [0.6, 0.6], [0.6, 0.4]])
        grid.update_pos(pts)

        expected_close = [0, 1, 5, 4]
        expected_nearyby = [{0, 1, 3, 4, 5, 7, 12, 13, 15},
                            {0, 1, 2, 4, 5, 6, 12, 13, 14},
                            {0, 1, 2, 4, 5, 6, 8, 9, 10},
                            {0, 1, 4, 5, 8, 9, 3, 7, 11}]
        for idx, p in enumerate(pts):
            close, nearby = grid.get_closest_and_nearby(Vector(p[0], p[1]), idx)
            self.assertEqual(expected_close[idx], close)
            self.assertEqual(expected_nearyby[idx], nearby)


if __name__ == '__main__':
    unittest.main()
