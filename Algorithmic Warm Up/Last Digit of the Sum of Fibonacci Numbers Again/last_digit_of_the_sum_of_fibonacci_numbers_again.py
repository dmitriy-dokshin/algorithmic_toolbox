# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def pisano_period(m):
    first = 1
    second = 1
    n = 1
    while not (first == 0 and second == 1):
        first, second = second, (first + second) % m
        n += 1

    return n


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    m = 10
    p = pisano_period(m)

    f1 = min(from_index - from_index % p + p, to_index)
    f2 = max(to_index - to_index % p, from_index)
    x = 0
    if f1 < f2:
        x = (f2 - f1) // p

    from_index %= p
    to_index %= p

    first = 0
    second = 1
    i = 1
    sum = 0
    while True:
        if i <= to_index:
            sum = (sum + second) % m

        if i >= from_index:
            sum = (sum + second) % m

        sum = (sum + second * x) % m

        first, second = second, (first + second) % m

        i += 1
        if i == p:
            break

    return sum


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
