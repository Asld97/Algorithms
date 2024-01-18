"""
Selection Sort steps
1. Select the lowest number in array
2. Add at the end of the table
3. Delete used number form the table
"""

data = [4, 7, 3, 23, 4, 56, 2]


def find_smallest(data):
    smallest_value = data[0]
    smallest_index = 0
    for i in range(0, len(data)):
        if data[i] < smallest_value:
            smallest_value = data[i]
            smallest_index = i

    return smallest_index


def selection_sort_asc(data):
    sorted_array = []
    while data:
        smallest_index = find_smallest(data)
        sorted_array.append(data.pop(smallest_index))

    return sorted_array


print(selection_sort_asc(data))

data = [4, 7, 3, 23, 4, 56, 2]


def find_largest(data):
    largest_value = data[0]
    largest_index = 0
    for i in range(0, len(data)):
        if data[i] > largest_value:
            largest_value = data[i]
            largest_index = i

    return largest_index


def selection_sort_desc(data):
    sorted_array = []
    while data:
        largest_index = find_largest(data)
        sorted_array.append(data.pop(largest_index))

    return sorted_array


print(selection_sort_desc(data))
