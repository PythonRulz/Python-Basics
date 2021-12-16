# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def determine_if_divisor(num):
    divisor = [x for x in range (1, num+1) if num % x == 0]
    '''for x in range (1, num):
        if num % x == 0:
            divisor.append(x)'''
    return divisor

def main():
    num = int(input("Enter a number: "))
    result = determine_if_divisor(num)
    print(f"Here is a list of divisors of {num}")
    print(result)

main()
