# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search_impl(keys, q, begin, end):
    while begin < end:
        mid = begin + (end - begin) // 2
        if keys[mid] < q:
            begin = mid + 1
        else:
            end = mid
    return begin


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4
    i = binary_search_impl(keys, query, 0, len(keys))
    return i if i < len(keys) and keys[i] == query else -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
