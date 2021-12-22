# Exercise 7 (and Solution)
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

'''
	Several ways to solve this exercise
	The simpliest way with 2 lines of code (which could be one line of code by adding the list to the comprehension line)
'''
# my initial solution
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(([num for num in a if num % 2 == 0]))

# the single line solution
print(([num for num in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] if num % 2 == 0]))

# solution using a for loop
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = []
for num in a:
    if num % 2 == 0:
        even_list.append(num)
print(even_list)
