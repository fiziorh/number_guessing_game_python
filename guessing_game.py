"""
Python Web Development Techdegree
Project 1 - number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def lines():
    print("-"*10)


highscore = []


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    lines()
    print(
        "Hello my friend, this is a number guessing game. You have to guess the right number in order for you to win the game !")
    answer = input("Do you want to play now ? [Y/N]  ")
    lines()

    while answer.lower() == "y":
        count = 1
        num = random.randint(1, 10)
        lines()
        print(
            f"WELCOME TO THE GAME\nYou have to pick a number between 1-10\nYour current HIGHSCORE {min(highscore)}")
        try:
            number = int(input("What is your guess ?   "))
            while number != num:
                if number > 10 or number < 1:
                    print("It's outside the range, pick between 1-10")
                    count += 1
                elif num > number:
                    print("It's higher !!")
                    count += 1
                else:
                    print("It's lower !!")
                    count += 1
                number = int(input("What's the number ?   "))
        except ValueError:
            print("Oh no, you're not inputing a number, please input a number !!")
        else:
            lines()
            highscore.append(count)
            print("Congrats, you guessed the correct number !!")
            print(f"You have guessed {count} times !!")
            answer = input("Do you want to play again ?  ")
            lines()
    print("Thanks for your time, you can play the game whenever you're ready!!")


# Kick off the program by calling the start_game function.
start_game()
