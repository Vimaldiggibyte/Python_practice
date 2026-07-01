def check_guess(guess, secret_number):

    if guess < secret_number:
        return "low"

    elif guess > secret_number:
        return "high"

    else:
        return "correct"