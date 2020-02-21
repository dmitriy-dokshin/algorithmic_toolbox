# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def pisano_period(m):
    first = 1
    second = 1
    n = 1
    while not (first == 0 and second == 1):
        first, second = second, (first + second) % m
        n += 1

    return n


def last_digit_of_the_sum_of_fibonacci_numbers_(n, m):
    p = pisano_period(m)
    n %= p

    if n == 0:
        return 0
    elif n == 1:
        return 1

    first = 0
    second = 1
    i = 1
    sum = 1
    while i != n:
        first, second = second, (first + second) % m
        sum = (sum + second) % m
        i += 1

    return sum

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    return last_digit_of_the_sum_of_fibonacci_numbers_(n, 10)


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
