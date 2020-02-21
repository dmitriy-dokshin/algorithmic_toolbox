# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key=lambda x: x.start)

    result = []

    max_start = segments[0].start
    min_end = segments[0].end
    i = 1
    while i < len(segments):
        x = segments[i]
        if x.start > min_end:
            result.append(max_start)
            min_end = x.end
        elif x.end < min_end:
            min_end = x.end
        max_start = x.start
        i += 1

    result.append(max_start)

    return result


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
