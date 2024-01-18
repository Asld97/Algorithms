"""
Binary search has O = log2 (n)
This is the max number of operation to find the index. Sometimes we need to make extra check if the number is correct or is none. 
(log2 8 = 3 so the number between 4-7 need at max 3 guesses, but 8 will need the extra one to final check; 8-15 at max 4 guesses;
Hint: log2 1 = 0, but we still need to check wheter the number is the looking one or it is not)
"""


def binary_search(input, wanted):
    low = 0
    high = len(input) - 1
    step = 0
    while low <= high:
        mid = (low + high) // 2

        guess = input[mid]
        step += 1
        print(
            f"Step finshed: {step}; min: {low}; max: {high}; mid: {mid}; guess: {guess}"
        )
        if guess == wanted:
            return mid
        elif guess > wanted:
            high = mid - 1

        else:
            low = mid + 1


input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 16, 21, 24, 45]
wanted = 45

print(f"The index of wanted number: {binary_search(input, wanted)}")
