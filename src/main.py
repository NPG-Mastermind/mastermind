from text_interface import show_main_menu
from user_guess import player_guesses_code

def main():
    while True:
        show_main_menu()
        print()
        choice = input("Wybierz tryb gry (1-4 lub q aby zakończyć): ").strip()

        if choice == "1":
            print("\n[Tryb 1: Gra z komputerem]\n")
            player_guesses_code()
        elif choice == "2":
            print("\n[Tryb 2: Tryb dwóch graczy]\n")
        elif choice == "3":
            print("\n[Tryb 3: Komputer zgaduje]\n")
        elif choice == "4":
            print("\n[Tryb 4: Wczytywanie gry]\n")
        elif choice.lower() == "q":
            print("Zamykanie gry. Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

if __name__ == "__main__":
    main()