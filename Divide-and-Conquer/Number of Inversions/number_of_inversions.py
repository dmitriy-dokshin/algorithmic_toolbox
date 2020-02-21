# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions_impl(a, begin, end):
    if begin == end:
        return [], 0
    elif begin + 1 == end:
        return [a[begin]], 0
    else:
        mid = begin + (end - begin) // 2
        left, left_inversions = compute_inversions_impl(a, begin, mid)
        right, right_inversions = compute_inversions_impl(a, mid, end)
        res = []
        inversions = left_inversions + right_inversions
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                inversions += len(left) - i
                j += 1

        while i < len(left):
            res.append(left[i])
            i += 1

        while j < len(right):
            res.append(right[j])
            j += 1

        return res, inversions


def compute_inversions(a):
    return compute_inversions_impl(a, 0, len(a))[1]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
