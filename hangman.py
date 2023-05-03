import random

HANGMAN_ASCII_ART = ("""Welcome to the game Hangman
       _    _
      | |  | |
      | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
      |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
      | |  | | (_| | | | | (_| | | | | | | (_| | | | |
      |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                           __/ |
                          |___/\n""")

MAX_TRIES = 6
OPEN_GUESSES_TEXT = "You have " + str(MAX_TRIES) + " guesses to try guess the full word\nlets get started!!"

STAGE0 = " x-------x\n"
STAGE1 = " x-------x\n |\n |\n |\n |\n |\n"
STAGE2 = " x-------x\n |       |\n |       0\n |\n |\n |\n"
STAGE3 = " x-------x\n |       |\n |       0\n |       |\n |\n |\n"
STAGE4 = " x-------x\n |       |\n |       0\n |      /|\ \n |\n |\n"
STAGE5 = " x-------x\n |       |\n |       0\n |      /|\ \n |      /\n |\n"
STAGE6 = " x-------x\n |       |\n |       0\n |      /|\ \n |      / \ \n |\n"
HANGMAN_PHOTOS = {0: STAGE0, 1: STAGE1, 2: STAGE2, 3: STAGE3, 4: STAGE4, 5: STAGE5, 6: STAGE6}


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def check_valid_input(letter_guessed, old_letters_guessed):
    return letter_guessed.isalpha() and 0 < len(letter_guessed) < 2 and \
           letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(old_letters_guessed))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    guess_progress = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            guess_progress += letter + " "
        else:
            guess_progress += "_ "

    return guess_progress


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def choose_word(file_path, index):
    fp = open(file_path)
    words = []
    for line in fp:
        for word in line.split():
            words.append(word)
    num_of_words_in_file = len(words)
    random.shuffle(words)
    return words[(index % num_of_words_in_file) - 1]


def game():
    # each ran of this function is a one game session
    print(HANGMAN_ASCII_ART, OPEN_GUESSES_TEXT)
    num_of_tries = 0
    old_letters_guessed = []
    while True:
        index = input("Enter a number to choose a word from our storage: ")
        if index.isdigit():
            break
        print("This is not a valid number!")

    secret_word = choose_word("words", int(index))
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries != MAX_TRIES:
        while True:
            guess = input("\nGuess a letter: ").lower()
            if try_update_letter_guessed(guess, old_letters_guessed):
                if guess not in secret_word:
                    num_of_tries += 1
                break

        print(guess.lower())
        if guess not in secret_word:
            print(":(")
            print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            quit()

    print("LOSE")
    print("The word was " + secret_word)


def main():
    while True:
        game()
        if input("\n\nDo you want to play another game (Y/N)? ").lower() != "y":
            break


if __name__ == '__main__':
    main()
