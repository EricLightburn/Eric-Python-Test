from random import randint
guess = 0
tries = 0
number = randint(1,100)
while (guess!=number):
    try:
        guess = int(input("Choose a number between 1 and 100: ")) 
        if (guess>=number):
            print("lower")
        if (guess<=number):
            print("higher")
        tries = tries + 1 
    except ValueError:
        print("pick a number")
print("It took you ", tries, " tries to guess the")
