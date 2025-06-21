import random

Colors = ['Red', 'Green', 'White', 'Yellow', 'Orange', 'Pink', 'Purple', 'Blue']


def GetLength(n):
    while True:
        try:
            length = int(input("Podaj długośc kodu: "))
            if length > 0 and length <7:
                return length
            else:
                print("Podaj właściwą długość kodu: ")
        except ValueError:
            print("Zła wartość")

#placeholder wyboru dlugosci kodu
Length = 4

def MaxNumberOfAttempts(n):
    while True:
        try:
            attempts = int(input("Podaj maksymalna ilość prób: "))
            if attempts > 0:
                return attempts
            else:
                print("Zła wartość, podaj liczbe większa od zera: ")
        except ValueError:
            print("Zła wartość, podaj liczbę: ")

#placeholder wyboru mozliwych prob
MaxAttempts = 4

def NumberOfColors(n):
    while True:
        try:
            count = int(input("Wybierz liczbe kolorów od 6 do 8: "))
            if count in [6, 7, 8]:
                return count
            else:
                print("Wybierz liczbe od 6 do 8: ")
        except ValueError:
            print("Zła wartośc, wpisz liczbę: ")
#W implementacji(main) trzeba pzyciąć słownik o wybraną ilość kolorów 
def GenerateCode():
    return [random.choice(Colors) for _ in range(Length)]

def CheckGuess(secret, guess):
    black_pegs = 0
    white_pegs = 0
    SecretCopy= secret[:]
    GuessCopy = guess[:]
    for i in range(Length):
        if guess[i] == secret[i]:
            black_pegs += 1
            SecretCopy[i] = None
            GuessCopy[i] = None
    for i in range(Length):
        if GuessCopy[i] and GuessCopy[i] in SecretCopy:
            white_pegs += 1
            SecretCopy[SecretCopy.index(GuessCopy[i])] = None

    return black_pegs, white_pegs    

def Validate(guess):
    if len(guess) != Length:
        return False
    return all(color in Colors for color in guess)
