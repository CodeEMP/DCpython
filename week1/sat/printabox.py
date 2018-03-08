width = int(input("Width? "))
height = int(input("Height? "))
for i in range(1, height + 1):
    if i == 1 or i == height:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')