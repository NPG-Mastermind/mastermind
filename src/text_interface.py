def show_main_menu():
	print("=============================")
	print("       GRA MASTERMIND        ")
	print("=============================")
	print("1 - Gracz zgaduje")
	print("2 - Komputer zgaduje")
	print("3 - Tryb dla dwóch graczy")
	print("4 - Wczytaj grę")


def show_feedback(black, white, tries_left):
    	show_pegs(black, white)
    	print("Czarne (trafione miejsce i liczba):", black)
    	print("Białe (trafiony liczba, złe miejsce):", white)
    	print("Pozostało prób:", tries_left)
    	print("------------------------")

def show_pegs(black, white):
    	print("Wskazówki:", "○" * black + "●" * white)

def show_win():
	print("Gratulacje! Odgadłeś kod!")

def show_loss(code):
	print("Przegrałeś. Prawidłowy kod to:",''.join(str(x) for x in code))