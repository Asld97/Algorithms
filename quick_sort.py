from random import randint


def quick_sort(arr):

    if len(arr) < 2:

        return arr

    # First element of array as pivot - possible worst-cases O(n^2) for sorted or almost sorted arrays
    pivot = arr[0]
    smaller = [num for num in arr[1:] if pivot >= num]
    greater = [num for num in arr[1:] if pivot < num]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

    # Version II - Randomly selected pivot - most cases invulnerable for worst-case. Generates medium-case - O(nlogn)
    # pivot = arr[randint(0, len(arr) - 1)]
    # smaller = [num for num in arr if pivot > num]
    # greater = [num for num in arr if pivot < num]
    # same = [num for num in arr if pivot == num]

    # return quick_sort(smaller) + same + quick_sort(greater)


num = [10, 4, 11, 2, 3, 2, 1, 5, 11]
print(f"Input array: {num}\nSorted array: {quick_sort(num)}")
