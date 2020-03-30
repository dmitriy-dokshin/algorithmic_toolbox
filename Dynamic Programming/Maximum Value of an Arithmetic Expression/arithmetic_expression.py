# python3
import sys
from enum import Enum


class EOperationType(Enum):
    Add = 0
    Subtract = 1
    Multiply = 2


def try_parse_op(c):
    op = None
    if c == '+':
        op = EOperationType.Add
    elif c == '-':
        op = EOperationType.Subtract
    elif c == '*':
        op = EOperationType.Multiply
    return op


class TMinMax:
    def __init__(self, min=None, max=None):
        self.Min = min
        self.Max = max

    Min = None
    Max = None


def calculate_min_max(x, y, op):
    if op == EOperationType.Add:
        return TMinMax(x.Min + y.Min, x.Max + y.Max)
    elif op == EOperationType.Subtract:
        return TMinMax(x.Min - y.Max, x.Max - y.Min)
    elif op == EOperationType.Multiply:
        return TMinMax(
            min(x.Min * y.Min, x.Min * y.Max, x.Max * y.Min, x.Max * y.Max),
            max(x.Min * y.Min, x.Min * y.Max, x.Max * y.Min, x.Max * y.Max)
        )
    else:
        raise Exception("Unknown operation type")


class TUpperTriangularMatrix:
    def __init__(self, size):
        self.Size = size
        self.Data = [TMinMax()] * (size * (size + 1) // 2)

    def __getitem__(self, key):
        return self.Data[self.__data_index__(key)]

    def __setitem__(self, key, value):
        self.Data[self.__data_index__(key)] = value

    def __data_index__(self, key):
        i, j = key
        shift = i * (2 * self.Size - i + 1) // 2  # n*(n + 1)/2 - (n - i)*(n - i + 1)/2
        j -= i
        return shift + j

    Size = 0
    Data = []


def max_value_of_arithmetic_expression(values, ops):
    res = TUpperTriangularMatrix(len(values))
    d = 0
    while d < len(values):
        i = 0
        j = d
        while j < len(values):
            if d == 0:
                res[i, j] = TMinMax(values[i], values[i])
            elif d == 1:
                res[i, j] = calculate_min_max(res[i, i], res[j, j], ops[i])
            else:
                mid = i
                while mid < j:
                    x = calculate_min_max(res[i, mid], res[mid + 1, j], ops[mid])
                    res[i, j] = TMinMax(
                        x.Min if res[i, j].Min is None else min(res[i, j].Min, x.Min),
                        x.Max if res[i, j].Max is None else max(res[i, j].Max, x.Max)
                    )
                    mid += 1
            i += 1
            j += 1
        d += 1

    return res[0, len(values) - 1].Max


def read(sin, values, ops):
    s = ""
    for c in sin:
        if '0' <= c <= '9':
            s += c
        else:
            op = try_parse_op(c)
            if op is not None:
                values.append(int(s))
                ops.append(op)
                s = ""
    values.append(int(s))


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    values = []
    ops = []
    read(dataset, values, ops)

    return max_value_of_arithmetic_expression(values, ops)


if __name__ == "__main__":
    print(find_maximum_value(input()))
