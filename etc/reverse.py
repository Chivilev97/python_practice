arr = [11, 22, 33, 44, 55]


def reverse(arr):
    result = []
    for index in range(len(arr) - 1, -1, -1):
        result.append(arr[index])
    return result


print(reverse(arr))
