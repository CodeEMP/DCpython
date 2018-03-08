list1 = [1, 2, 'steve', 2, 'rich', 'rich', 3, 'steve']
new = []
[new.append(item) for item in list1 if item not in new]
print(new)