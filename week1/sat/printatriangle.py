height = int(input("How tall is the triangle?"))
for i in range(0, height):
    space = height - i - 1
    star = i * 2 + 1
    print(' ' * space + '*' * star)
    