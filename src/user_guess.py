import time
from game_logic import GenerateCode, CheckGuess, SetLength, SetMaxNumberOfAttempts, NumberOfColors, NUMBERS, LENGTH
from text_interface import show_feedback, show_win, show_loss
from stats import update_stats
from save import save_game, generate_new_save_filename


def player_guesses_code(loaded_state=None):
    if loaded_state:
        length = len(loaded_state["code"])
        tries = loaded_state["max_attempts"]
        secret_code = [str(num) for num in loaded_state["code"]]
        guesses = [[str(num) for num in guess] for guess in loaded_state["guesses"]]
        current_try = len(guesses)
        available_colors = NUMBERS[:8]
        print(f"\nWczytano grę. Pozostało prób: {tries - current_try}")
    else:
        length = SetLength()
        tries = SetMaxNumberOfAttempts()
        color_count = NumberOfColors()
        available_colors = NUMBERS[:color_count]
        secret_code = GenerateCode()
        guesses = []
        current_try = 0

        print(f"\nUżywanych będzie {length} liczb z listy:")
        print(', '.join(available_colors))
        print("Podawaj liczby oddzielone spacją, np.: 3 7 2 1")
        print("Aby zapisać grę, wpisz 'zapisz' zamiast kodu")
        print("Rozpoczynasz grę! Komputer ustawił tajny kod z liczb.")

    for i in range(current_try, tries):
        while True:
            guess_input = input(f"Próba {i + 1}/{tries}: ").strip().lower()

            if guess_input == "zapisz":
                save_filename = generate_new_save_filename()
                save_game({
                    "code": [int(num) for num in secret_code],
                    "guesses": [[int(num) for num in guess] for guess in guesses],
                    "max_attempts": tries
                }, save_filename)
                print(f"Gra została zapisana jako {save_filename}.")
                return

            guess_parts = guess_input.split()

            if len(guess_parts) != length:
                print(f"Musisz podać dokładnie {length} liczb.")
                continue

            if not all(part in available_colors for part in guess_parts):
                print(f"Niepoprawne liczby! Dostępne: {', '.join(available_colors)}")
                continue

            try:
                guess = [int(num) for num in guess_parts]
                break
            except ValueError:
                print("Wprowadź tylko liczby oddzielone spacjami lub 'zapisz'")

        guesses.append([str(num) for num in guess])
        black, white = CheckGuess(secret_code, [str(num) for num in guess])
        show_feedback(black, white, tries - (i + 1))

        if black == length:
            update_stats(True, i + 1)
            show_win()
            time.sleep(5)
            return
        else:
            update_stats(False, tries)
            show_loss(secret_code)
            time.sleep(5)