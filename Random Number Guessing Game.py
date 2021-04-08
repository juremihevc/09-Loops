import random

min = 1
max = 1000

secret = random.randint(min , max)
guess = 0

while guess != secret:
    guess = int(input(f"Guess the secret number (between {min} and {max}): "))

    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {secret}.")
        break

    elif guess > secret:
        print("Aim lower!")

    else:
        print("Aim higher!")

