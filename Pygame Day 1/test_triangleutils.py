import unittest
from math import pi as PI
from triangleutils import *


class TestRotateTriangleUtilMethods(unittest.TestCase):
    """
    This is a unit test class to test the functions in the traiangle_utils module.
    See https://docs.python.org/2/library/unittest.html
    """

    def test_degrees_to_radians(self):
        self.assertEqual(degrees_to_radians(180), PI)


    def test_triangle_polygon(self):
        triangle = create_triangle(0, 0)

        # Is the size of the polygon correct?
        self.assertEqual(len(triangle), 3)

        # Are the dimensions correct?
        self.assertEqual(triangle[0][0], 0)
        self.assertEqual(triangle[0][1], 50)

        self.assertEqual(triangle[1][0], 20)
        self.assertEqual(triangle[1][1], -10)

        self.assertEqual(triangle[2][0], -20)
        self.assertEqual(triangle[2][1], -10)


    def test_rotate_point(self):
        x, y = rotate_a_point((0, 60), 90, 0, 0)

        # We use the "almost equal" to account for rounding errors in conversion 
        # to integers to floating point numbers
        self.assertAlmostEqual(x, -60)
        self.assertAlmostEqual(y, 0)


if __name__ == '__main__':
    unittest.main()
