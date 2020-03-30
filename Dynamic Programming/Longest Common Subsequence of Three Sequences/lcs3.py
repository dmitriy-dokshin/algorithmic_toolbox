# python3


class MultiDimensionalArray:
    def __init__(self, sizes):
        array_size = 1
        for size in reversed(sizes):
            self.Sizes.append(array_size)
            array_size *= size

        self.Sizes.reverse()
        self.Array = [0] * array_size

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


def iterate(sizes, index, f, d=0):
    for i in range(0, sizes[d]):
        index[d] = i
        if d < len(sizes) - 1:
            iterate(sizes, index, f, d + 1)
        else:
            f(index)


def equal_at(sequences, index):
    for i in range(1, len(sequences)):
        if sequences[i][index[i]] != sequences[i - 1][index[i - 1]]:
            return False
    return True


def f(res, sequences, index):
    if equal_at(sequences, index):
        i = 0
        while i < len(index) and index[i] > 0:
            index[i] -= 1
            i += 1
        x = res[index] if i == len(index) else 0
        while i > 0:
            index[i - 1] += 1
            i -= 1
        res[index] = x + 1
    else:
        x = 0
        for i in range(0, len(index)):
            if index[i] > 0:
                index[i] -= 1
                x = max(x, res[index])
                index[i] += 1
        res[index] = x


def lcs_n(sequences):
    sizes = [len(x) for x in sequences]

    res = MultiDimensionalArray(sizes)

    index = [0] * len(sequences)
    iterate(sizes, index, lambda index: f(res, sequences, index))

    return res[[len(x) - 1 for x in sequences]]


def lcs3_fast(first_sequence, second_sequence, third_sequence):
    com_len = []
    for i in range(0, len(first_sequence)):
        x = []
        for j in range(0, len(second_sequence)):
            x.append([0] * (len(third_sequence)))
        com_len.append(x)

    for i in range(0, len(first_sequence)):
        for j in range(0, len(second_sequence)):
            for k in range(0, len(third_sequence)):
                if first_sequence[i] == second_sequence[j] and first_sequence[i] == third_sequence[k]:
                    com_len[i][j][k] = (com_len[i - 1][j - 1][k - 1] if i > 0 and j > 0 and k > 0 else 0) + 1
                else:
                    com_len[i][j][k] = max(com_len[i - 1][j][k] if i > 0 else 0,
                                           com_len[i][j - 1][k] if j > 0 else 0,
                                           com_len[i][j][k - 1] if k > 0 else 0)

    return com_len[len(first_sequence) - 1][len(second_sequence) - 1][len(third_sequence) - 1]


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    return lcs_n([first_sequence, second_sequence, third_sequence])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
