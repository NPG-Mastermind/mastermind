import random
import itertools

def get_user_feedback(guess):
    while True:
        try:
            print(f"Zgadywana kombinacja przez komputer: {guess}")
            black = int(input("Podaj liczbę czarnych pinów (trafienia na właściwej pozycji): "))
            white = int(input("Podaj liczbę białych pinów (trafienia, ale na złej pozycji): "))
            if 0 <= black <= 4 and 0 <= white <= 4 and black + white <= 4:
                return black, white
            else:
                print("Nieprawidłowe wartości. Suma pinów nie może przekraczać 4.")
        except ValueError:
            print("Wprowadź poprawne liczby całkowite.")

def computer_guessing_game():
    length = 4
    colors = 6
    max_attempts = 10
    all_possibilities = list(itertools.product(range(1, colors + 1), repeat=length))
    attempts = 0

    print("\n--- ODWRÓCONY MASTERMIND ---")
    print("Wymyśl tajną kombinację 4 cyfr od 1 do 6 (np. 1234).")
    print("Po każdej próbie wpisz liczbę czarnych i białych pinów.")
    print("Czarne: poprawna cyfra i pozycja. Białe: poprawna cyfra, zła pozycja.\n")

    while attempts < max_attempts and all_possibilities:
        guess = random.choice(all_possibilities)
        attempts += 1

        print(f"\n🔁 Próba #{attempts}")
        black, white = get_user_feedback(guess)

        if black == length:
            print(f"\n Komputer odgadł kombinację w {attempts} próbach: {guess}")
            return
        else:
            all_possibilities = [
                p for p in all_possibilities if simulate_feedback(p, guess) == (black, white)
            ]

    print("\n Komputer nie odgadł kombinacji w 10 próbach lub nie ma już możliwych kombinacji.")


def simulate_feedback(secret, guess):
    black = sum(s == g for s, g in zip(secret, guess))
    white = sum(min(secret.count(n), guess.count(n)) for n in set(guess)) - black
    return black, white

#if __name__ == "__main__":
    #computer_guessing_game()
