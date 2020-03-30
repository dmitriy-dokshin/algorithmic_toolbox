# python3
from enum import Enum


class OperationType(Enum):
    Default = 0
    Add1 = 1
    MultiplyBy2 = 2
    MultiplyBy3 = 3


class Result:
    def __init__(self, minOps=0, opType=OperationType.Default):
        self.MinOps = minOps
        self.OpType = opType

    MinOps = 0
    OpType = OperationType.Default


def compute_operations(n):
    assert 1 <= n <= 10 ** 6

    res = [Result()] * (n + 1)
    val = 2
    while val <= n:
        res[val] = Result(res[val - 1].MinOps + 1, OperationType.Add1)
        if val % 3 == 0 and res[val // 3].MinOps + 1 < res[val].MinOps:
            res[val] = Result(res[val // 3].MinOps + 1, OperationType.MultiplyBy3)
        if val % 2 == 0 and res[val // 2].MinOps + 1 < res[val].MinOps:
            res[val] = Result(res[val // 2].MinOps + 1, OperationType.MultiplyBy2)
        val += 1

    seq = [n]
    val = n
    while res[val].OpType != OperationType.Default:
        if res[val].OpType == OperationType.Add1:
            val -= 1
        elif res[val].OpType == OperationType.MultiplyBy2:
            val //= 2
        else:
            val //= 3
        seq.append(val)
    seq.reverse()
    return seq


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
