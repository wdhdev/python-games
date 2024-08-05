import random, sys, time

def type(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10 / 2500)
    print()

while True:
    type("Welcome to the number guessing game...\nIn this game you need to correctly guess a specific number to win.\n")
    type("There are 4 modes:\n")
    type("1. Easy: a number between 1-25 with 5 guesses")
    type("2. Medium: a number between 1-50 with 5 guesses")
    type("3. Hard: a number between 1-100 with 5 guesses")
    type("4. Custom: a custom range with a custom amount of guesses\n")

    def get_input(prompt, valid_options = None, validation_fn = None, error_message = "Invalid input. Please try again."):
        while True:
            user_input = input(f"{prompt} ")

            if valid_options and user_input in valid_options:
                return user_input
            elif validation_fn and validation_fn(user_input):
                return user_input
            elif not valid_options and not validation_fn:
                return user_input
            else:
                print(error_message)

    mode = get_input("Which mode do you want to play? (easy/medium/hard/custom)", ["easy", "medium", "hard", "custom"])

    hints = get_input("Do you want hints to be enabled? (yes/no)", ["yes", "no", "y", "n"])

    if hints == "yes" or hints == "y":
        hints = True
    else:
        hints = False

    type(f"\nYou have selected {mode} mode with hints {"enabled" if hints else "disabled"}.\n")

    def generate_number(x, y):
        x = int(x)
        y = int(y)

        if x > y:
            raise ValueError("min cannot be greater than max")
        elif x == y:
            raise ValueError("min cannot equal max")

        return random.randint(x, y)

    def guess(min_number, max_number, guesses):
        type("Let's begin the game...\n")
        random_number = generate_number(min_number, max_number)
        guessed = False

        while guesses > 0:
            guesses = guesses - 1
            guess = int(get_input(f"Please guess a number between {min_number}-{max_number}:", None, lambda x: x.isdigit() and int(x) >= min_number and int(x) <= max_number))

            if guess == random_number:
                type(f"\nYou guessed the correct number with {guesses} guesses left!\nYou won the game, congratulations!")
                guessed = True
                break
            else:
                type(f"Incorrect guess. You have {guesses} guess{"" if guesses == 1 else "es"} left.")

                if hints and guesses != 0:
                    type(f"The random number is {"lower" if guess > random_number else "higher"}.\n")
                else:
                    print()

        if guesses == 0 and guessed == False:
            type(f"The random number was {random_number}.")
            type("You lost, game over!")

    if mode == "easy":
        guess(1, 25, 5)
    elif mode == "medium":
        guess(1, 50, 5)
    elif mode == "hard":
        guess(1, 100, 5)
    elif mode == "custom":
        min_number = int(get_input("What do you want the minimum number to be? (min: 1)", None, lambda x: x.isdigit() and int(x) >= 1 and int(x) <= 99998))
        max_number = int(get_input(f"What do you want the maximum number to be? (min: {min_number + 2})", None, lambda x: x.isdigit() and int(x) >= min_number + 2 and int(x) <= 10000))
        guesses = int(get_input(f"How many guesses do you want? (min: 1, max: {max_number - min_number - 1})", None, lambda x: x.isdigit() and int(x) >= 1 and int(x) <= max_number - 1))

        type(f"\nMin number: {min_number}\nMax number: {max_number}\nGuesses: {guesses}\n")

        guess(min_number, max_number, guesses)

    play_again = get_input("\nDo you want to play again? (yes/no)", ["yes", "no", "y", "n"])

    if play_again == "no" or play_again == "n":
        type("\nThanks for playing the number guessing game! Goodbye.")
        break
    else:
        print()
