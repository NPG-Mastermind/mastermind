import random

# ZMIENNE GLOBALNE
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8']
LENGTH = 4
ATTEMPTS = 4
COUNT = 6

def SetLength():
    global LENGTH
    while True:
        try:
            length = int(input("Podaj długośc kodu: "))
            if length > 0 and length <7:
                LENGTH = length
                return length
            else:
                print("Podaj właściwą długość kodu: ")
        except ValueError:
            print("Zła wartość")
            

def SetMaxNumberOfAttempts():
    global ATTEMPTS
    while True:
        try:
            attempts = int(input("Podaj maksymalna ilość prób: "))
            if attempts > 0:
                ATTEMPTS = attempts
                return attempts
            else:
                print("Zła wartość, podaj liczbe większa od zera: ")
        except ValueError:
            print("Zła wartość, podaj liczbę: ")
            

def NumberOfColors():
    global COUNT
    while True:
        try:
            count = int(input("Wybierz liczbe dostępnych liczb (6 lub 8): "))
            if count in [6, 8]:
                COUNT = count
                return count
            else:
                print("Wybierz 6 lub 8: ")
        except ValueError:
            print("Zła wartość, wpisz liczbę: ")
# W implementacji(main) trzeba pzyciąć słownik o wybraną ilość liczb
# Wcale nie 
def GenerateCode():
    numbers = NUMBERS[:COUNT]
    return [random.choice(numbers) for _ in range(LENGTH)]

def CheckGuess(secret, guess):
    black_pegs = 0
    white_pegs = 0
    SecretCopy= secret[:]
    GuessCopy = guess[:]
    for i in range(LENGTH):
        if guess[i] == secret[i]:
            black_pegs += 1
            SecretCopy[i] = None
            GuessCopy[i] = None
    for i in range(LENGTH):
        if GuessCopy[i] and GuessCopy[i] in SecretCopy:
            white_pegs += 1
            SecretCopy[SecretCopy.index(GuessCopy[i])] = None

    return black_pegs, white_pegs    

def Validate(guess):
    if len(guess) != LENGTH:
        return False
    return all(number in NUMBERS for number in guess)
