# Exercise 5 (and Solution)
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

def create_list():
    rand_list = []
    list_size = random.randint(10, 20)
    for num in range (list_size + 1):
        rand_list.append(random.randint(1,100))
    return rand_list

def main():
    a = create_list()
    b = create_list()
    print(f"List A: {a}")
    print(f"List B: {b}")
    result = determine_common_items(a, b)
    print()
    if result:
        print(f"Common numbers between List A and List B is: {result}")
        print(result)
    else:
        print("There are no common numbers between the lists.")
    
main()
            
