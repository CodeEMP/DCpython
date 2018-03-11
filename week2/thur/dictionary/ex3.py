word = input('What word? ')
letter_histogram = {}
for i in word:
    count = letter_histogram.get(i, 0)
    letter_histogram[i] = count + 1
print(letter_histogram)