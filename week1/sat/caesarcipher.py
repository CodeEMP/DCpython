l2i = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
i2l = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
key = 13
text = input("What to Cipher? ")
cipher = ""
for c in text.upper():
    if c.isalpha():
        cipher += i2l[(l2i[c] + key)%26]
    else:
        cipher += c
text2 = ""
for c in cipher:
    if c.isalpha():
        text2 += i2l[(l2i[c] - key)%26]
    else:
        text2 += c
print(text)
print(cipher)
print(text2)