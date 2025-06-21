from Main import GenerateCode, CheckGuess, Length
from text_interface import show_feedback, show_win, show_loss

def player_guesses_code():
    print("Rozpoczynasz grę! Komputer ustawił tajny kod z kolorów.")
    print("Dostępne kolory: Red, Green, White, Yellow, Orange, Pink, Purple, Blue")
    print("Podawaj kolory oddzielone spacją, np.: Red Green Blue Yellow")

    secret_code = GenerateCode()
    tries = 10

    for i in range(tries):
        guess_input = input(f"Próba {i+1}/{tries}: ")
        guess = guess_input.strip().split()

        if len(guess) != Length:
            print(f"Musisz podać dokładnie {Length} kolorów.")
            continue

        black, white = CheckGuess(secret_code, guess)
        show_feedback(black, white, tries - (i + 1))

        if black == Length:
            show_win()
            break

    else:
        show_loss(secret_code)