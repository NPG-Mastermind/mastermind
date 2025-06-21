import time
from text_interface import show_main_menu
from user_guess import player_guesses_code
from two_players import player_vs_player
from komputer_zgaduje import computer_guessing_game


def main():
    while True:
        show_main_menu()
        print()
        choice = input("Wybierz tryb gry (1-4 lub q aby zakończyć): ").strip()

        if choice == "1":
            print("\n[Tryb 1: Gra z komputerem]\n")
            player_guesses_code()
        elif choice == "2":
            print("\n[Tryb 2: Komputer zgaduje]\n")
            computer_guessing_game()

        elif choice == "3":
            print("\n[Tryb 3: Tryb dwóch graczy]\n")
            player_vs_player()

        elif choice == "4":
            print("\n[Tryb 4: Wczytywanie gry]\n")

            #dodać wczytywanie

        elif choice.lower() == "q":
            print("Zamykanie gry. Do zobaczenia!")
            time.sleep(5)
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

if __name__ == "__main__":
    main()