import random

def numberguessgame():
    x = str(random.randint(1, 10))
    y = x
    while y == x:
        qs = input("Guess a number 1-10 to see if it's my number!")
        if qs == x:
            print("you got it right!")
            y = "hi"
        else:
            print("Incorrect!")

numberguessgame()