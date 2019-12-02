
import random

class main():
    """
    THIS IS A ROCK, PAPER, SCISSORS GAME.
    It will a user an input from the predefined choices.
    If the user, get it right or ran out of options, the program will stop.
    """
    name = input("WELCOME TO ROCK, PAPER, SCISSORS GAME!\nWhat is your name: \n")
    tries = int(input("Welcome {}! How many tries will this be? ".format(name.title())))
    while tries>0:
        choices = ['rock', 'paper', 'scissors']
        answer = input("Choose your weapon: ROCK, PAPER, SCISSORS ")
        rand_ans = random.choice(choices)
        if answer.lower() == rand_ans:
            print("It's a draw!")
            tries -= 1
        elif (answer.lower() == 'rock'):
            if (rand_ans == choices[1]):
                print("You lose! The computer's hand is " + rand_ans)
                tries -= 1
            else:
                print("Congrats! You win!")
                break
        elif (answer.lower() == 'paper'):
            if (rand_ans == choices[0]):
                print("Congrats! You win!")
                break
            else:
                print("You lose! The computer's hand is " + rand_ans)
                tries -= 1
        else:
            if (rand_ans == choices[0]):
                print("You lose! The computer's hand is " + rand_ans)
                tries -= 1
            else:
                print("Congrats! You win!")
                break



if __name__ == "__main__":
    main()