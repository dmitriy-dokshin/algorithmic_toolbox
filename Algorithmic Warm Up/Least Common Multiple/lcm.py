# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    rem = a % b
    while rem != 0:
        a, b = b, rem
        rem = a % b

    return b


def lcm(a, b):
    # For invalid test case: 10000000 0
    if a == 0 or b == 0:
        return 0

    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    # let c be lcm(a, b)
    # let d be gcd(a, b)
    # a = a' * d; b = b' * d
    # c = a' * b' * d, so c is divisible by a and b
    # or c = (a / d) * (b / d) * d = a * b / d

    d = gcd(a, b)
    return a * b // d


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
