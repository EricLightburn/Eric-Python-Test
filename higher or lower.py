from random import randint
guess = 0
tries = 0
number = randint(1,100)
while (guess!=number):
    guess = int(input("Choose a number between 1 and 100: ")) 
    if (guess>number):
            print("lower")
    elif (guess<number):
            print("higher")
    tries = tries + 1 

print("It took you ", tries, " tries to guess the")
