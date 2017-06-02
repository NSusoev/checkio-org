
def checkio(data):
    small_data = False

    if len(data) <= 100:
        data.sort()
        small_data = True

    if len(data) % 2 == 0:
        if not small_data:
            data = sort_k_elems(data, round(len(data) / 2) + 1)
        return (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
    else:
        if not small_data:
            data = sort_k_elems(data, round(len(data) / 2))
        return data[len(data) // 2]

def sort_k_elems(data, k):
    left, right = 0, len(data) - 1

    while left < right:
        i, j, divider = left, right, data[k]
        while True:
            while data[i] < divider:
                i += 1
            while data[j] > divider:
                j -= 1
            if i <= j:
                data[i], data[j] = data[j], data[i]
                i += 1
                j -= 1
            if i > j:
                break
        if j < k:
            left = i
        if i > k:
            right = j
    return data


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")