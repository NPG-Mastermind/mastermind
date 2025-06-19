def show_main_menu():
	print("=============================")
	print("       GRA MASTERMIND        ")
	print("=============================")
	print("1 - Gra z komputerem")
	print("2 - Komputer zgaduje")
	print("3 - Tryb dwóch graczy")
	print("4 - Wczytaj grę")


def show_feedback(black, white, tries_left):
    	show_pegs(black, white)
    	print("Czarne (trafione miejsce i liczba):", black)
    	print("Białe (trafiona liczba, złe miejsce):", white)
    	print("Pozostało prób:", tries_left)
    	print("------------------------")

def show_pegs(black, white):
    	print("Wskazówki:", "○" * black + "●" * white)
