# python3

from functools import cmp_to_key
from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = [str(x) for x in numbers]

    numbers.sort(key=cmp_to_key(lambda x, y: 1 if x + y > y + x else -1), reverse=True)

    return int("".join(numbers))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
