import time
from game_logic import GenerateCode, CheckGuess, SetLength, SetMaxNumberOfAttempts, NumberOfColors, NUMBERS, LENGTH
from text_interface import show_feedback, show_win, show_loss

def player_guesses_code():
    length = SetLength()
    tries = SetMaxNumberOfAttempts()
    color_count = NumberOfColors()
    available_colors = NUMBERS[:color_count]

    print(f"\nUżywanych będzie {length} liczb z listy:")
    print(', '.join(available_colors))
    print("Podawaj liczby oddzielone spacją, np.: 3 7 2 1")

    globals()['LENGTH'] = length

    secret_code = GenerateCode()
    
    print("Rozpoczynasz grę! Komputer ustawił tajny kod z liczb.")

    for i in range(tries):
        guess_input = input(f"Próba {i+1}/{tries}: ")
        guess = guess_input.strip().split()

        if len(guess) != LENGTH:
            print(f"Musisz podać dokładnie {LENGTH} liczb.")
            continue

        if not all(number in available_colors for number in guess):
            print("Niepoprawne liczby! Spróbuj ponownie.")
            continue

        black, white = CheckGuess(secret_code, guess)
        show_feedback(black, white, tries - (i + 1))

        if black == LENGTH:
            show_win()
            time.sleep(5)
            break

    else:
        show_loss(secret_code)
        time.sleep(5)
