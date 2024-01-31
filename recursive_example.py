# Fibonacci's sequence
def fibonacci_sequence(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibonacci_sequence(num - 1) + fibonacci_sequence(num - 2)


# Factorial
def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)


# Pyramid Printing
def print_pyramid(rows, spaces=0):
    if rows > 1:
        print_pyramid(rows - 1, spaces + 1)
    print(spaces * " " + " *" * rows)
