def playagain():
    while True:
        choice = input("Do you want to play again?(Y/N) ").upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print("Invalid input")
boo = playagain()
print(boo)