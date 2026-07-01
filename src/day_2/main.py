import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("=== Number Guessing Game ===")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.")

    elif guess > secret_number:
        print("Too High! Try again.")

    else:
        print("\nCongratulations!")
        print(f"You guessed the correct number: {secret_number}")
        print(f"You took {attempts} attempts.")
        break