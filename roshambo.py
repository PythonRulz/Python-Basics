# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
#
# While it specifically states this game is for 2 players, i found it better to have computer vs player.

import random

#function simply to randomly make a selection of Rock, Paper or Scissors
def get_computer_choice(comp_choice):
    return random.choice(comp_choice)

# function to get the user choice
# i did not code for bad user input here, but a simple loop would fix this
def get_user_choice(rps):
    user_choice = int(input("Choose: 1. Rock  2. Paper  3. Scissors: "))
    return (rps[user_choice - 1])

# i'm not a fan of all these conditional statements to determine the winner
# any suggestions would be appreciated
# while i did consider the use of AND/OR conditional statements, I couldn't figure it out
# after looking at some other solutions, I did find it.  While it's still noisy, it is a bit simplified

'''
    if (user == 'Rock' and computer == 'Paper') or (user == 'Scissors' and computer == 'Rock') or (user == 'Paper' and computer == 'Scissors'):
        print(f"{computer} beats {user} Computer Wins!")
    elif (computer == 'Rock' and user == 'Paper') or (computer == 'Scissors' and user == 'Rock') or (computer == 'Paper' and user == 'Scissors'):
        print(f"{user} beats {computer} User Wins!") 
    else:
        print("It's a tie")
'''
def who_wins(user, computer):
    if user == 'Rock' and computer == 'Paper':
        print("Paper beats Rock, Computer Wins!")
    elif user == 'Paper' and computer == 'Scissors':
        print("Scissors beats Paper, Computer Wins!")
    elif user == 'Scissors' and computer == 'Rock':
        print("Rock beats Scissors, Computer Wins!")
    elif computer == 'Rock' and user == 'Paper':
        print("Paper beats Rock, You Win!")
    elif computer == 'Paper' and user == 'Scissors':
        print("Scissors beats Paper, You Win!")
    elif computer == 'Scissors' and user == 'Rock':
        print("Rock beats Scissors, You Win!")
    else:
        print("It's a tie!")
    
# here in the main function we simply place the code in a while loop
# and call the other functions to run the program
def main():
    again = 'Y'
    while again == 'Y':
        rps_list = ['Rock', 'Paper', 'Scissors']
        user = get_user_choice(rps_list)
        computer = get_computer_choice(rps_list)
        print()
        print(f"The computer has chosen {computer}")
        print(f"You have chosen {user}")
        print()
        who_wins(user, computer)
        print()
        again = input("Type Y to play again or anything else to quit: ").upper()
        

main()
    
    

