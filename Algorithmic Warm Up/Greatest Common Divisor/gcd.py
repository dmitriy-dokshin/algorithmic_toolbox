# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    # if a > b then a / b = (x * b + a') / b
    # d divides a without a remainder if and only if it divides a'
    # so, gcd(a, b) = gcd(a', b) = gcd(b, a')

    a, b = max(a, b), min(a, b)
    rem = a % b
    while rem != 0:
        a, b = b, rem
        rem = a % b

    return b


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
