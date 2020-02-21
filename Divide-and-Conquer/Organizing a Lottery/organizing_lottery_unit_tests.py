import unittest
from random import randint

from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, 6], [3, 10], list(range(10)))
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self, n=1000, m=1000):
        min = 0
        max = 1000

        starts = []
        ends = []
        i = 0
        while i < n:
            start = randint(min, max)
            starts.append(starts)
            end = randint(start, max)
            ends.append(end)
            i += 1

        points = []
        i = 0
        while i < m:
            points.append(randint(min, max))
            i += 1

    def test_large(self):
        self.test_random(50000, 50000)


if __name__ == '__main__':
    unittest.main()
