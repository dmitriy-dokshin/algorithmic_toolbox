# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    com_len = [[0] * (len(second_sequence)) for x in range(len(first_sequence))]

    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return 0

    if first_sequence[0] == second_sequence[0]:
        com_len[0][0] = 1

    i = 1
    while i < len(first_sequence):
        if first_sequence[i] == second_sequence[0]:
            com_len[i][0] = 1
        else:
            com_len[i][0] = com_len[i - 1][0]
        i += 1

    j = 1
    while j < len(second_sequence):
        if first_sequence[0] == second_sequence[j]:
            com_len[0][j] = 1
        else:
            com_len[0][j] = com_len[0][j - 1]
        j += 1

    i = 1
    while i < len(first_sequence):
        j = 1
        while j < len(second_sequence):
            if first_sequence[i] == second_sequence[j]:
                com_len[i][j] = com_len[i - 1][j - 1] + 1
            else:
                com_len[i][j] = max(com_len[i - 1][j], com_len[i][j - 1])
            j += 1
        i += 1

    return com_len[len(first_sequence) - 1][len(second_sequence) - 1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
