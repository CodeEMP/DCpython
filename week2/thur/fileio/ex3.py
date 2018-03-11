fh = input('Enter file name: ')
file_handle = open(fh, 'r')
content = file_handle.read() + ' '
print(content)
letter_histogram = {}
for i in content:
    count = letter_histogram.get(i, 0)
    letter_histogram[i] = count + 1
for key in letter_histogram.items():
    print(key)
word_histogram = {}
word = ''
for i in content:
    if i != ' ':
        word += i
    else:
        count = word_histogram.get(word, 0)
        word_histogram[word] = count + 1
        word = ''
for key in word_histogram.items():
    print(key)