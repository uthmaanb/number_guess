import random

number = random.randint(1, 100)
tries = 0

uname = input("enter your name: ")
uname = uname.strip()

print("Hello " + uname)
print("Would you like to play a game")
print("1) yes")
print("2) no")

option = input("select your option ")
option = int(option)

if option == 1:
    pass
elif option == 2:
    print("Thanks")
else:
    print("No man pick 1 or 2")

if option == 1:
    print("I\'m thinking of a number between 1 and 100")
    print(" you have three tries")

    guess = input("Guess a number: ")
    guess = int(guess)
    tries += 1

    if guess > number:
        print("unlucky. Maybe go lower")
    if guess < number:
        print("a bit higher?")

    while guess != number and tries < 3:
        guess = input("try again: ")
        guess = int(guess)
        tries += 1

        if guess > number:
            print("unlucky. Maybe go lower")
        if guess < number:
            print("a bit higher?")

    if guess == number:
        print("WOW you're actually clever")
        print(f"number of tries: {tries}")
    else:
        print("too bad you lost")
elif option == 2:
    print("Thanks")
else:
    print("just follow the instructions")
