import time
from text_interface import show_main_menu
from user_guess import player_guesses_code
from save import load_game
from save import delete_save
from statistics import show_stats
from two_players import player_vs_player

def main():
    while True:
        show_main_menu()
        print()
        choice = input("Wybierz tryb gry (1-6 lub q aby zakończyć): ").strip()

        if choice == "1":
            print("\n[Tryb 1: Gra z komputerem]\n")
            player_guesses_code()
        elif choice == "2":
            print("\n[Tryb 2: Komputer zgaduje]\n")

            #dodać komputer zgaduje

        elif choice == "3":
            print("\n[Tryb 3: Tryb dwóch graczy]\n")
            player_vs_player()

        elif choice == "4":
            print("\n[Tryb 4: Wczytywanie gry]\n")
            file_name = input("Podaj nazwe zapisu (np. save1.csv):")
            load_game(file_name)

        elif choice == "5":
            show_stats()

        elif choice == "6":
            file_name_to_delet = input("Podaj nazwe zapisu do usuniecia (np. save1.csv):")
            delete_save(file_name_to_delet)

        elif choice.lower() == "q":
            print("Zamykanie gry. Do zobaczenia!")

            time.sleep(5)
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

if __name__ == "__main__":
    main()