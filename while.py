secret = 22
guess = None

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
    else:
        print(f"Sorry, your guess is not correct... The secret number is not {guess}")