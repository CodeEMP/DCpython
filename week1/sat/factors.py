num = int(input('What number to factor? '))
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
    else:
        pass
