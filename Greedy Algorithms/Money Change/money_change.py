# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    n = 0
    coins = [10, 5, 1]
    for x in coins:
        n += money // x
        money %= x

    return n


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
