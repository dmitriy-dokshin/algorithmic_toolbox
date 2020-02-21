# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    if len(elements) == 0:
        return 0

    elements.sort()

    last_x = elements[0]
    n = 0
    for x in elements:
        if x == last_x:
            n += 1
        else:
            last_x = x
            n = 1
        if n > len(elements) // 2:
            return 1

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
