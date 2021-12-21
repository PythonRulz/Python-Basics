# Exercise 5 (and Solution)
# Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this


import random

def determine_common_items(lista, listb):
    c = []

    for num in lista:
        if num in listb:
            if num in c:
                continue
            c.append(num)
    return c

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = determine_common_items(a, b)
    print(result)

main()
