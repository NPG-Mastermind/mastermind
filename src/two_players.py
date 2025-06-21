import random
from game_logic import *
from text_interface import show_feedback

def player_vs_player():
    print("Mastermind - wersja dla dwóch graczy")
    
    len = SetLength()
    atts = SetMaxNumberOfAttempts()
    
    print("Gracz 1 tworzy kod, Gracz 2 zgaduje.")
    print(f"Dostępne liczby: {NUMBERS}")
    
    # gracz 1 tworzy kod
    print("\nGracz 1 - tworzenie kodu:")
    secret_code = []
    for i in range(len):
        while True:
            number = input(f"Wybierz liczbę {i+1}/{len} z dostępnych {NUMBERS}: ").capitalize()
            if number in NUMBERS:
                secret_code.append(number)
                break
            else:
                print("Nieprawidłowa liczba. Spróbuj ponownie.")
    
    print("\n" * 50)  # czyszczenie ekranu
    
    # gracz 2 zgaduje
    print("Gracz 2 - zgadywanie kodu:")
    print(f"Dostępne liczby: {NUMBERS}")
    print(f"Masz {atts} prób, aby odgadnąć kod o długości {len}.")
    
    for attempt in range(1, atts + 1):
        print(f"\nPróba {attempt}/{atts}")
        while True:
            guess = input("Podaj swój kod (liczby oddzielone spacją): ").title().split()
            if Validate(guess):
                break
            print("Nieprawidłowy kod. Sprawdź długość i dostępne liczby.")
        
        black, white = CheckGuess(secret_code, guess)
        show_feedback(black, white, atts-attempt)
        
        if black == len:
            print(f"\nGratulacje! Gracz 2 odgadł kod w {attempt} próbach!")
            return
    
    print(f"\nKoniec prób! Sekretny kod to: {' '.join(secret_code)}")

if __name__ == "__main__":
    player_vs_player()
