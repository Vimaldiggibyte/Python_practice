import random
from utils import check_guess


def start_game():
    secret_number = random.randint(1, 100)

    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        result = check_guess(guess, secret_number)

        if result == "low":
            print("Too Low!")

        elif result == "high":
            print("Too High!")

        else:
            print("\nCongratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break