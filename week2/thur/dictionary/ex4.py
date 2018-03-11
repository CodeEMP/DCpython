paragraph = input('Type a paragraph. ').upper() + ' '
word_histogram = {}
word = ''
for i in paragraph:
    if i != ' ':
        word += i
    else:
        count = word_histogram.get(word, 0)
        word_histogram[word] = count + 1
        word = ''
for key in word_histogram.items():
    print(key)