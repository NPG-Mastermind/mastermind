import random
import itertools

# komputer_zgaduje.py
import random
import itertools
from game_logic import LENGTH, COUNT, NUMBERS


def get_user_feedback(guess):
    while True:
        try:
            print(f"Zgadywana kombinacja przez komputer: {guess}")
            black = int(input("Podaj liczbę czarnych pinów (trafienia na właściwej pozycji): "))
            white = int(input("Podaj liczbę białych pinów (trafienia, ale na złej pozycji): "))
            if 0 <= black <= LENGTH and 0 <= white <= LENGTH and black + white <= LENGTH:
                return black, white
            else:
                print(f"Nieprawidłowe wartości. Suma pinów nie może przekraczać {LENGTH}.")
        except ValueError:
            print("Wprowadź poprawne liczby całkowite.")


def computer_guessing_game():
    length = LENGTH
    colors = COUNT
    max_attempts = 10
    all_possibilities = list(itertools.product(NUMBERS[:colors], repeat=length))
    attempts = 0

    print(f"\n--- ODWRÓCONY MASTERMIND ---")
    print(f"Wymyśl tajną kombinację {length} cyfr od 1 do {colors} (np. {' '.join(NUMBERS[:length])}).")
    print("Po każdej próbie wpisz liczbę czarnych i białych pinów.")
    print("Czarne: poprawna cyfra i pozycja. Białe: poprawna cyfra, zła pozycja.\n")

    while attempts < max_attempts and all_possibilities:
        guess = random.choice(all_possibilities)
        attempts += 1

        print(f"\n🔁 Próba #{attempts}")
        black, white = get_user_feedback(guess)

        if black == length:
            print(f"\nKomputer odgadł kombinację w {attempts} próbach: {' '.join(guess)}")
            return
        else:
            all_possibilities = [
                p for p in all_possibilities if simulate_feedback(p, guess) == (black, white)
            ]

    print("\nKomputer nie odgadł kombinacji w 10 próbach lub nie ma już możliwych kombinacji.")


def simulate_feedback(secret, guess):
    black = sum(s == g for s, g in zip(secret, guess))
    white = sum(min(secret.count(n), guess.count(n)) for n in set(guess)) - black
    return black, white

if __name__ == "__main__":
    computer_guessing_game()
