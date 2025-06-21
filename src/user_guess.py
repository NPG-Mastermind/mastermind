import time
from game_logic import GenerateCode, CheckGuess, GetLength, MaxNumberOfAttempts, NumberOfColors, Colors, Length
from text_interface import show_feedback, show_win, show_loss

def player_guesses_code():
    print("Rozpoczynasz grę! Komputer ustawił tajny kod z kolorów.")

    length = GetLength(None)
    tries = MaxNumberOfAttempts(None)
    color_count = NumberOfColors(None)
    available_colors = Colors[:color_count]

    print(f"\nUżywanych będzie {length} kolorów z listy:")
    print(', '.join(available_colors))
    print("Podawaj kolory oddzielone spacją, np.: Red Green Blue Yellow")

    globals()['Length'] = length

    secret_code = GenerateCode()

    for i in range(tries):
        guess_input = input(f"Próba {i+1}/{tries}: ")
        guess = guess_input.strip().split()

        if len(guess) != Length:
            print(f"Musisz podać dokładnie {Length} kolorów.")
            continue

        if not all(color in available_colors for color in guess):
            print("Niepoprawne kolory! Spróbuj ponownie.")
            continue

        black, white = CheckGuess(secret_code, guess)
        show_feedback(black, white, tries - (i + 1))

        if black == Length:
            show_win()
            time.sleep(5)
            break

    else:
        show_loss(secret_code)
        time.sleep(5)