actual_word = "waterbottle"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

print("Hello! Welcome to the GuessMyWord game")
print(f"You have {guess_limit} attempts to guess the word I am thinking of.")
print("Well then let's get started!")

while not guess == actual_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter in your guess: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Sorry, you ran out of attempts!")
else:
    print("You guessed it right!")