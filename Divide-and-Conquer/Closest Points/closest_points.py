# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
from sys import float_info

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def distance(first_point, second_point):
    return sqrt(distance_squared(first_point, second_point))


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def lower_bound(items, x, comp, begin, end):
    while begin < end:
        mid = begin + (end - begin) // 2
        if comp(items[mid], x):
            begin = mid + 1
        else:
            end = mid
    return begin


def minimum_distance(points, begin, end):
    if end - begin < 2:
        return float_info.max
    elif end - begin == 2:
        return distance(points[begin], points[begin + 1])

    mid = begin + (end - begin) // 2
    dl = minimum_distance(points, begin, mid)
    dr = minimum_distance(points, mid, end)
    d = min(dl, dr)

    xless = lambda p, x: p.x < x
    xless_or_eq = lambda p, x: p.x <= x
    xmin = points[mid].x - d
    xmax = points[mid].x + d
    xbegin = lower_bound(points, xmin, xless, begin, mid)
    xend = lower_bound(points, xmax, xless_or_eq, mid, end)

    lpoints = []
    i = xbegin
    while i < mid:
        lpoints.append(points[i])
        i += 1

    rpoints = []
    while i < xend:
        rpoints.append(points[i])
        i += 1

    rpoints.sort(key=lambda p: p.y)

    yless = lambda p, y: p.y < y
    yless_or_eq = lambda p, y: p.y <= y
    for pi, p in enumerate(lpoints):
        ymin = p.y - d
        ymax = p.y + d
        ybegin = lower_bound(rpoints, ymin, yless, 0, len(rpoints))
        yend = lower_bound(rpoints, ymax, yless_or_eq, 0, len(rpoints))
        i = ybegin
        while i < yend:
            if i != pi:
                d = min(d, distance(p, rpoints[i]))
            i += 1

    return d


def minimum_distance_squared(points):
    points.sort(key=lambda p: p.x)
    return minimum_distance(points, 0, len(points)) ** 2


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
