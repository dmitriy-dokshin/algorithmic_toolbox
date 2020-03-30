# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money, coins=[1, 3, 4]):
    result = [0] * (money + 1)
    m = 1
    while m <= money:
        for coin in coins:
            if coin <= m:
                count = result[m - coin] + 1
                result[m] = min(count, result[m]) if result[m] > 0 else count
        m += 1
    return result[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
