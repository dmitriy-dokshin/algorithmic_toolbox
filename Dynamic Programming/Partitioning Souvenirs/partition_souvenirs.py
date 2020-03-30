# python3

from itertools import product
from sys import stdin


class MultiDimensionalArray:
    def __init__(self, sizes, value):
        array_size = 1
        for size in reversed(sizes):
            self.Sizes.append(array_size)
            array_size *= size

        self.Sizes.reverse()
        self.Array = [value] * array_size

    def __array_index(self, index):
        array_index = 0
        for i in range(0, len(index)):
            array_index += index[i] * self.Sizes[i]
        return array_index

    def __getitem__(self, index):
        return self.Array[self.__array_index(index)]

    def __setitem__(self, index, value):
        self.Array[self.__array_index(index)] = value

    Sizes = []
    Array = []


def iterate(start, sizes, index, f, d=0):
    for i in range(start[d], sizes[d]):
        index[d] = i
        if d < len(sizes) - 1:
            iterate(start, sizes, index, f, d + 1)
        else:
            f(index)


def equal(values):
    for i in range(1, len(values)):
        if values[i] != values[i - 1]:
            return False
    return True


def convert(value, base, n):
    result = [0] * n
    while n > 0:
        div = base ** (n - 1)
        result[n - 1] = value // div
        value -= result[n - 1] * div
        n -= 1
    return result


def partition_n_naive(values, n):
    for x in range(0, n ** len(values)):
        shuffle = convert(x, n, len(values))
        sums = [0] * n
        for i in range(0, len(values)):
            sums[shuffle[i]] += values[i]
        if equal(sums):
            return True
    return False


def partition_n_recursive_impl(values, n, sums):
    if n == 0:
        return all(x == 0 for x in sums)

    for i in range(0, len(sums)):
        if sums[i] >= values[n - 1]:
            sums[i] -= values[n - 1]
            if partition_n_recursive_impl(values, n - 1, sums):
                return True
            else:
                sums[i] += values[n - 1]

    return partition_n_recursive_impl(values, n - 1, sums)


def partition_n_recursive(values, n):
    total_sum = sum(values)
    if total_sum % n != 0:
        return False

    target_sum = total_sum // n
    sums = [target_sum] * (n - 1)
    return partition_n_recursive_impl(values, len(values), sums)


def f(index, res, values):
    val = values[index[0] - 1]
    for i in range(1, len(index)):
        if index[i] >= val:
            index[0] -= 1
            index[i] -= val
            res_flag = res[index]
            index[0] += 1
            index[i] += val
            res[index] = res_flag
            if res_flag:
                return

    index[0] -= 1
    res_flag = res[index]
    index[0] += 1
    res[index] = res_flag


def partition_n(values, n):
    total_sum = sum(values)
    if total_sum % n != 0:
        return False

    target_sum = total_sum // n

    sizes = [len(values) + 1] + [target_sum + 1] * (n - 1)
    res = MultiDimensionalArray(sizes, False)
    index = [0] * n
    res[index] = True
    iterate([1] + [0] * n, sizes, index, f=lambda index: f(index, res, values))
    return res[index]


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    return 1 if partition_n(values, 3) else 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
