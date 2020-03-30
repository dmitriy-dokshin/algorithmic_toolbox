# python3


def edit_distance(first_string, second_string):
    dist = [[0] * (len(second_string) + 1) for x in range(len(first_string) + 1)]

    i = 1
    while i <= len(first_string):
        dist[i][0] = i
        i += 1

    j = 1
    while j <= len(second_string):
        dist[0][j] = j
        j += 1

    i = 1
    while i <= len(first_string):
        j = 1
        while j <= len(second_string):
            if first_string[i - 1] == second_string[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min(dist[i - 1][j], dist[i][j - 1], dist[i - 1][j - 1]) + 1
            j += 1
        i += 1

    return dist[len(first_string)][len(second_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
