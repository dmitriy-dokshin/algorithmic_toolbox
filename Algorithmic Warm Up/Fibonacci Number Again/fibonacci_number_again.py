# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def pisano_period(m):
    first = 1
    second = 1
    n = 1
    while not (first == 0 and second == 1):
        first, second = second, (first + second) % m
        n += 1

    return n


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    p = pisano_period(m)
    n %= p

    if n == 0:
        return 0
    elif n == 1:
        return 1

    first = 0
    second = 1
    i = 1
    while i != n:
        first, second = second, (first + second) % m
        i += 1

    return second


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
