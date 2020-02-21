# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    wp = []
    for i, w in enumerate(weights):
        wp.append((w, prices[i] / w))

    wp.sort(key=lambda x: x[1], reverse=True)

    total_weight = 0
    total_value = 0
    i = 0
    while total_weight < capacity and i < len(wp):
        weight = min(capacity - total_weight, wp[i][0])
        price = wp[i][1]
        total_weight += weight
        total_value += weight * price
        i += 1

    return total_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
