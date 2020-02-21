# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n == 0:
        return 0
    if n == 1:
        return 1

    first = 0
    second = 1
    i = 2
    while i != n:
        current = first + second
        first = second
        second = current
        i += 1

    return first + second


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
