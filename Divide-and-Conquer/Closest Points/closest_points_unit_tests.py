import unittest
from closest_points import minimum_distance_squared, minimum_distance_squared_naive, Point
from random import randint


class ClosestPoints(unittest.TestCase):
    def test_small(self):
        for points in (
                [Point(1, 0), Point(1, 1)],
                [Point(1, 0), Point(1, 1), Point(1, 2), Point(3, 0), Point(3, 1), Point(3, 2)]
        ):
            self.assertAlmostEqual(minimum_distance_squared(points),
                                   minimum_distance_squared_naive(points),
                                   delta=1e-03)

    def test_random(self, n=100, max_value=1000):
        points = []
        for _ in range(n):
            x = randint(-max_value, max_value)
            y = randint(-max_value, max_value)
            points.append(Point(x, y))

        self.assertAlmostEqual(
            minimum_distance_squared(points),
            minimum_distance_squared_naive(points),
            delta=1e-03)

    def test_large(self):
        self.test_random(10 ** 4)


if __name__ == '__main__':
    unittest.main()
