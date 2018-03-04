coins = 0
while True:
    print("You have {} coins.".format(coins))
    choice = input("Do you want a coin? ").lower()
    if 'yes' in choice:
        coins += 1
    elif 'no' in choice:
        print('Bye')
        break
    else:
        print("It's a yes ot no question.")