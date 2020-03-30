# python3

from sys import stdin


def knapsack_with_repetitions(capacity, weights, values):
    res = [0] * (capacity + 1)
    for w in range(0, len(res)):
        res[w] = max(iter(res[w - weights[i]] + values[i] for i in range(0, len(weights)) if weights[i] <= w),
                     default=0)
    return res[capacity]


def knapsack_without_repetitions(capacity, weights, values):
    res = []
    for w in range(0, capacity + 1):
        res.append([0] * (len(weights) + 1))
    for w in range(1, capacity + 1):
        for n in range(1, len(weights) + 1):
            res[w][n] = res[w][n - 1]
            if weights[n - 1] <= w:
                res[w][n] = max(res[w][n], res[w - weights[n - 1]][n - 1] + values[n - 1])
    return res[capacity][len(weights)]


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    return knapsack_without_repetitions(capacity, weights, values=weights)


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
