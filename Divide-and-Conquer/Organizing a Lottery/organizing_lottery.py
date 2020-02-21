# python3
from enum import Enum
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


class PointType(Enum):
    Start = 1
    Point = 2
    End = 3

    def __lt__(self, other):
        return self.value < other.value


def points_cover(starts, ends, points):
    all_points = []

    for x in starts:
        all_points.append((PointType.Start, x))

    for x in ends:
        all_points.append((PointType.End, x))

    for (i, x) in enumerate(points):
        all_points.append((PointType.Point, x, i))

    all_points.sort(key=lambda x: (x[1], x[0]))

    counts = [0] * len(points)
    count = 0
    for x in all_points:
        if x[0] == PointType.Start:
            count += 1
        elif x[0] == PointType.End:
            count -= 1
        else:
            counts[x[2]] = count
    return counts


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
