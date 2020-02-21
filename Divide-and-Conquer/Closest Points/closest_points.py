# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
from sys import float_info

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared_impl(points, ypoints, begin, end):
    if end - begin < 2:
        return float_info.max
    elif end - begin == 2:
        return distance_squared(points[begin], points[begin + 1])

    mid = begin + (end - begin) // 2
    xmid = points[mid].x

    lypoints = []
    rypoints = []
    for p in ypoints:
        if p.x < xmid:
            lypoints.append(p)
        else:
            rypoints.append(p)

    dl = minimum_distance_squared_impl(points, lypoints, begin, mid)
    dr = minimum_distance_squared_impl(points, rypoints, mid, end)
    d = min(dl, dr)

    xmin = points[mid].x - sqrt(d)
    xmax = points[mid].x + sqrt(d)

    ypoints = [p for p in ypoints if xmin <= p.x <= xmax]

    for pi, p in enumerate(ypoints):
        ymin = p.y - sqrt(d)
        ymax = p.y + sqrt(d)

        i = pi
        while i > 0 and ypoints[i - 1].y >= ymin:
            d = min(d, distance_squared(p, ypoints[i - 1]))
            i -= 1

        j = pi + 1
        while j < len(ypoints) and ypoints[j].y <= ymax:
            d = min(d, distance_squared(p, ypoints[j]))
            j += 1

    return d


def minimum_distance_squared(points):
    points.sort(key=lambda p: p.x)
    ypoints = sorted(points, key=lambda p: p.y)
    return minimum_distance_squared_impl(points, ypoints, 0, len(points))


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
