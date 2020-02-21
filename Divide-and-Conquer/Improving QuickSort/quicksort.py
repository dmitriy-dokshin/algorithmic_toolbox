# python3

from random import randint


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition3(array, left, right):
    val = array[randint(left, right)]
    i = 0
    while left + i <= right:
        if array[left + i] < val:
            swap(array, left, left + i)
            left += 1
        elif array[left + i] > val:
            swap(array, right, left + i)
            right -= 1
        else:
            i += 1
    return left - 1, right + 1


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    res = partition3(array, left, right)
    randomized_quick_sort(array, left, res[0])
    randomized_quick_sort(array, res[1], right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
