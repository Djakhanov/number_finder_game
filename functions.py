"""
25/02/2025

Python
"Number finder" Game

Author: Mansur Djakhanov

Web sahifa: https://www.linkedin.com/in/mansur-djakhanov-a44bb3108/
"""

import random


def find_number(x=10):
    random_number = random.randint(1, x)
    print(f"I thought of a number from 1 to {x}. Can you find it?", end="")
    guesses = 0
    while True:
        guesses += 1
        guess = int(input(">>>"))
        if guess < random_number:
            print("Error. The number I thought of is larger than this. Try again:", end="")
        elif guess > random_number:
            print("Error. The number I thought of is smaller than this. Try again:", end="")
        else:
            break

    print(f"Congratulations. You found it in {guesses} guesses!")
    return guesses


def find_number_pc(x=10):
    input(f"Think of a number from 1 to {x} and press any button. I will find it.")
    low_er = 1
    up_per = x
    guesses = 0
    while True:
        guesses += 1
        if low_er != up_per:
            guess = random.randint(low_er, up_per)
        else:
            guess = low_er
        javob = input(f"You guessed the number {guess}: correct (t),"
                      f"The number I thought of was greater (+), or smaller (-)".lower())
        if javob == "-":
            up_per = guess - 1
        elif javob == "+":
            low_er = guess + 1
        else:
            break
    print(f"I found it with {guesses}guess!")
    return guesses


def play(x=10):
    more = True
    while more:
        user_guesses = find_number(x)
        pc_guesses = find_number_pc(x)

        if user_guesses > pc_guesses:
            print(f"I found it with {pc_guesses} guess and won!")
        elif user_guesses < pc_guesses:
            print(f"You guessed it with {user_guesses} guess and won!")
        else:
            print("A draw!")
        more = int(input("Shall we play again? Yes(1)/No(0):"))


play()