import unittest
from Animal import Vector


class MyTestCase(unittest.TestCase):
    def test_distance_in_periodic_map(self):
        self.assertEqual(5, Vector(0, 3).distance(Vector(4, 0)))
        v1 = Vector(1, 1)
        v2 = Vector(MAX_SCOPE - 2, MAX_SCOPE - 3)
        self.assertEqual(5, v1.distance(v2))

        # w1 = Animal("wolf", 1, pos= Vector(10,10), speed = Vector(3,1))
        # assert( w1.pos.x == 10 and w1.pos.y == 10)
        # w1.move(1)
        # assert( w1.pos.x == 13 and w1.pos.y == 11) given alignment effect, it's not


if __name__ == '__main__':
    unittest.main()
