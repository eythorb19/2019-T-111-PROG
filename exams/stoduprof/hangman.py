import random

# Constants to be used in the implementation
WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'

def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def get_secret_word():
    secret_word = random.choice(WORD_LIST)
    return secret_word

def initialize_guess_word(secret_word):
    guess_word = [CHAR_PLACEHOLDER]*len(secret_word)
    return guess_word

def print_current_guess_word(guess_word):
    print("Word to guess: {}".format(" ".join(guess_word)))

def print_instructions(guess_word):
    print("The word you need to guess has", len(guess_word), "characters")
    print_current_guess_word(guess_word)

def process_guess(guess, num_guesses, secret_word, guess_word, letter_storage):
    if guess in letter_storage:
        print("You have already guessed that letter!")
    else:
        letter_storage.add(guess)
        num_guesses += 1
        if guess in secret_word:
            print("You guessed correctly!")
            for i in range(0, len(secret_word)):
                if secret_word[i] == guess:
                    guess_word[i] = guess
        else:
            print("The letter is not in the word!")
    return num_guesses

def play(secret_word, guess_word):
    letter_storage = set()
    num_guesses = 0
    while num_guesses < MAX_GUESS:
        guess = input("Choose a letter: ").lower()
        num_guesses = process_guess(guess, num_guesses, secret_word, guess_word, letter_storage)
        if not CHAR_PLACEHOLDER in guess_word:
            print("You won!")
            print_current_guess_word(guess_word)
            break
        else:
            print("You are on guess {}/{}".format(num_guesses, MAX_GUESS))
            print_current_guess_word(guess_word)
    else:   
        print("You lost! The secret word was {}".format(secret_word))


# Main program starts here
random_seed()
secret_word = get_secret_word()
guess_word = initialize_guess_word(secret_word)
print_instructions(guess_word)
play(secret_word, guess_word)
