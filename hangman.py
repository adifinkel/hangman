import random


def start_gui():
    print("""  _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |                      
                         |___/        \n\n""")


def print_by_level(state):
    # the function gets the number of levels left for the player, the func prints the hang man state
    if state == 0:
        print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")
    elif state == 1:
        print("""
            x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
        """)
    elif state == 2:
        print("""
      x-------x
    |       |
    |       0
    |      /|\\
    |
    |
        """)
    elif state == 3:
        print("""
    x-------x
    |       |
    |       0
    |       |
    |
    |
        """)
    elif state == 4:
        print("""
    x-------x
    |       |
    |       0
    |
    |
    |
        """)
    elif state == 5:
        print("""
    x-------x
    |       
    |       
    |
    |
    |
        """)
    else:
        print("x-------x")
    if state > 0:
        print(f"player 2, you can try {state} times")


def has_win(guesses, answer):
    return all(guesses.count(letter) for letter in answer)


def turn(guesses, answer):
    while not has_win(guesses, answer):
        guess = input("guess a letter:\n")
        if guesses.count(guess):
            print("You already guessed that one!\n")

        elif guess in answer:
            guesses += guess
            print("Nice one!")
            print(' '.join([letter if (letter in guesses)
                            else '_' for letter in answer]))

        else:
            guesses += guess
            print("Maybe next time\n")
            break

    return guesses


def game(answer):
    guesses = ""
    max_tries = random.randint(5, 10)
    start_gui()
    for i in range(max_tries)[::-1]:
        print_by_level(i)
        guesses = turn(guesses, answer)
        if has_win(guesses, answer):
            print("you win\n")
            return

    print_by_level(0)
    print("you lose\n")


if __name__ == '__main__':
    game("love")
