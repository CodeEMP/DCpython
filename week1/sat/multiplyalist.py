numbers = [0, 2, 3, 6, 20]
factor = 3
numbers2 = []
for num in numbers:
    num *= factor
    numbers2.append(num)
print(numbers2)
numbers3 = [2, 3, 4, 8, 15]
numbers4= []
i = 0
for num in numbers:
    numbers4.append(num * numbers3[i])
    i += 1
print(numbers4)