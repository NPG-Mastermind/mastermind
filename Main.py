import random

Colors = ['Red', 'Green', 'White', 'Yellow', 'Orange', 'Pink']


# def JakaDlugosc(n):
#    ...

#placeholder wyboru dlugosci kodu
Length = 4

# def IleProbZgadywania(n):
#    ...

#placeholder wyboru mozliwych prob
MaxAttempts = 4

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
