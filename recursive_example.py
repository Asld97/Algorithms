# # Fibonacci's sequence
# def fibonacci_sequence(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1

#     return fibonacci_sequence(num - 1) + fibonacci_sequence(num - 2)


# # Factorial
# def factorial(num):
#     if num == 0:
#         return 1

#     return num * factorial(num - 1)


# # Pyramid Printing
# def print_pyramid(rows, spaces=0):
#     if rows > 1:
#         print_pyramid(rows - 1, spaces + 1)
#     print(spaces * " " + " *" * rows)


# Simple Recrusive Adding Loop


def recursive_adding(arr):
    if arr == []:
        return 0
    return arr[0] + recursive_adding(arr[1:])


arr = [5]
print(f"Value of sum: {recursive_adding(arr)}")


def recursive_counting(arr, count=0):
    if arr == []:
        return 0

    return 1 + recursive_counting(arr[1:])


print(f"Number of list's elements: {recursive_counting(arr)} ")


arr = [5, 2, 5, 11, 1, 2]


def recursive_biggest_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    temp_max = recursive_biggest_num(arr[1:])

    return arr[0] if arr[0] > temp_max else temp_max


print(f"The biggest number in an array: {recursive_biggest_num(arr)}")
