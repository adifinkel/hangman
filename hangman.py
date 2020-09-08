import random
from termcolor import colored
import os

MAX_TRIES = 6


def start_gui():
    """
    Prints gui to the console, used when the user starts a new game
    """
    print(colored(r"""
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""+"\n\n", "magenta"))


def print_by_level(state):
    """
    Gets the number of levels left for the player,
     the func prints the hang man state accordingly
    :parameter state: integer of the number of levels left for the player
    """
    state_dict = {
        0: lambda: print(
            """
            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |
            """),
        1: lambda: print(
            """
            x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |
            """),

        2: lambda: print(
            """
            x-------x
            |       |
            |       0
            |      /|\\
            |
            |
            """),

        3: lambda: print(
            """
            x-------x
            |       |
            |       0
            |       |
            |
            |
            """),

        4: lambda: print(
            """
            x-------x
            |       |
            |       0
            |
            |
            |
            """),

        5: lambda: print(
            """
            x-------x
            |       
            |       
            |
            |
            |
            """),

        6: lambda: print("x-------x")
    }
    os.system('cls' if os.name == 'nt' else 'clear')
    state_dict.get(state, state_dict[6])()
    if state > 0:
        print(f"you can try {state} times")


def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word: string of the answer
    :param old_letters_guessed: string of the guesses so far
    :return:string of _ where the missing letters are
     and letters where the right guesses are
    """
    word_by_guess = ' '.join([letter if letter in old_letters_guessed else '_'
                              for letter in secret_word.lower()])
    return word_by_guess


def check_win(guesses, answer):
    """
    Gets the guesses and the answer, and check if th user won
    :param guesses: string of guesses. all the letters the user have tried yet
    :param answer: string of the answer
    :return: True if there is a win, False otherwise
    """
    return all(guesses.count(letter) for letter in answer)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Gets a new guess and string of old guesses and
    return False if the player already guessed that letter
    or if his guess is not valid. otherwise, return True
    :param letter_guessed: string of the guess
    :param old_letters_guessed: string of previous guesses
    :return: True or False
    """
    flag = True

    if len(letter_guessed) > 1:
        print(colored("ERROR. More then one letter", "red"))
        flag = False

    if not letter_guessed.isalpha():
        print(colored("ERROR. Not a letter", "red"))
        flag = False

    if letter_guessed in old_letters_guessed:
        print(colored("Heyo! You already guessed that one!", "yellow"))
        flag = False

    return flag


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """isalpha
    gets a guess and old guesses, if the guess is valid,
     the func adds it to the guesses.
    if the guess is not valid, the func prints the upper case of the guess
     and string of the lower case past guesses
    :param letter_guessed: string of the guess of the user
    :param old_letters_guessed: string of the user guesses so far
    :return: True if the guess is valid, False otherwise
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        return True
    else:
        print(letter_guessed.upper())
        old_letters_guessed = sorted(list(old_letters_guessed))
        old_letters_guessed = " -> ".join(old_letters_guessed)
        print(old_letters_guessed)
        return False


def turn(guesses, answer):
    """
    Run a turn in the "hangman" game.
    :param guesses: string of past guesses
    :param answer: string of the answer
    :return: new guesses string
    """
    while not check_win(guesses, answer):

        guess = input("Guess a letter:\n").lower()

        if not try_update_letter_guessed(guess, guesses):
            continue

        elif guess in answer:
            guesses += guess
            print("Nice one!")
            print(show_hidden_word(answer, guesses))

        else:
            guesses += guess
            print("Maybe next time\n")
            break

    return guesses


def choose_word(file_path, index):
    """
    param: file_path: string of route for text file.
    param: index: integer for index of word in the file
    return: tuple. 1 var of the number of different words in the file.
     The 2 var is the word in the given index
    """
    with open(file_path, "r") as source:
        words = source.read()
    words = words.split()
    words = [word.lower() for word in words]
    without_dup = list(set(words))
    pick_index = (index - 1) % len(words)
    return len(without_dup), words[pick_index]


def main():
    """
    The function run the hangman game, and let the user know if he won
    """
    route = input("insert a route to a file\n")
    with open(route, "w") as hoard:
        hoard.write("adult advice productive attempt August advice happy smart"
                    " america USA romance gift")
    index_of_word = int(input("insert a number"))
    answer = choose_word(route, index_of_word)[1]
    guesses = ""
    max_tries = random.randint(2, MAX_TRIES)
    start_gui()

    for state in range(max_tries)[:0:-1]:
        print_by_level(state)
        guesses = turn(guesses, answer)
        if check_win(guesses, answer):
            print(colored("YOU WON", "white", "on_green"))
            return
    print_by_level(0)
    print(colored("YOU LOST", "white", "on_red"))


if __name__ == '__main__':
    main()
