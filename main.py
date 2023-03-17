import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
easyNo = 10

hardNo = 5


def check_ans(guess, choosenNo, turns):
    if guess > choosenNo:
        print("Your Guess is Too High!")
        return turns - 1
    elif guess < choosenNo:
        print("Your Guess is too low!")
        return turns - 1
    else:
        print(f"You Win!, the answer is {choosenNo}")


def difficulty():
    level = input("enter the difficulty level easy or hard! : ")
    if level == "easy":
        return easyNo
    else:
        return hardNo


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choosenNo = random.randint(1, 100)
    turns = difficulty()
    guess = 0
    while guess != choosenNo:
        print(f"You have {turns} attempts left! ")
        guess = int(input("Make a Guess! : "))
        turns = check_ans(guess, choosenNo, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != choosenNo:
            print("Guess again.")


game()
