input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 16, 21, 24, 45]
wanted = 5


def binary_search(input, wanted):
    low = 0
    high = len(input) - 1
    n = 1
    while low <= high:
        mid = -(-(low + high) // 2)
        print(mid)
        check = input[mid]
        if check < wanted:
            low = mid + 1
        elif check > wanted:
            high = mid - 1
        else:
            print(n)
            return mid
        n += 1
    return -1


print(binary_search(input, wanted))
