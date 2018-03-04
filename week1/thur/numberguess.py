import random
number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")
guesses = 5
while guesses != 0:
    print("You have {} guesses left.".format(guesses))
    choice = int(input("What's the number? "))
    if choice < 1 or choice > 10:
        print("That's not even an option.")
    elif choice > number:
        print("Too high.")
        guesses -= 1
    elif choice < number:
        print("Too low.")
        guesses -= 1
    elif choice == number:
        print("You did it!")
        choice = input("Play again? ").lower()
        if 'yes' in choice:
            guesses = 5
            number = random.randint(1, 10)
            continue
        else:
            print("Thanks for playing!")
            break
if guesses == 0:
    print("You ran out of guesses!")
else:
    pass
