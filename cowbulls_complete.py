import random

def compare_numbers(number, user_guess):
    ## your code here

    cows = 0  #  cows start from 0
    bulls = 0  #  bulls start from 0

    # compare digits
    for i in range(len(number)):

        if user_guess[i] == number[i]:  # correct position
            bulls += 1

        elif user_guess[i] in number:  # correct number wrong place
            cows += 1

    cowbull = [cows, bulls]  # return list
    return cowbull

playing = True #if playing  the game
number = str(random.randint(1000,9999)) #random 4 digit number  # fixed to ensure 4 digits
guesses = 0
print(number)  # fixed print

print("Let's play a game of Cowbull!") # intro message with rules along
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")  # fixed raw_input

    if user_guess == "exit":
        break

    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1
    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))

        break # exit

    else:
        print("Your guess isn't quite right, try again.")