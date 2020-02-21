# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    dt = lambda i: 0 if i < 0 else stops[i]

    stops_count = 0
    i = -1
    while dt(i) + m < d:
        j = i
        while j + 1 < len(stops) and stops[j + 1] <= dt(i) + m:
            j += 1

        if i == j:
            return -1

        i = j
        stops_count += 1

    return stops_count


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
