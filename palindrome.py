# Exercise:
#		prompt the user for a string and determine if the entered string is a palindrome
#
#
#

# Index the string and append it to a list
# Then reverse the list and compare 

def is_palindrome(string):
    string_list = []
    for letter in string:
        string_list.append(letter)
    reverse_list = string_list[::-1]
    return string_list == reverse_list #return a True/False boolean to the result variable
        

def main():
    the_string = input("Enter a string: ")
    result = is_palindrome(the_string)
    
    print(
        f"The string {the_string} is a palindrome") if result else print(
            f"The string {the_string} is not a palindrome")
    

main()

# simplify by eliminating the need for lists
# example:
#       the_string[::-1]
