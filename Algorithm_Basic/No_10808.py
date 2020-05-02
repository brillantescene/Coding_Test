word = input()
alphabet = [[al, 0] for al in "abcdefghijklmnopqrstuvwxyz"]

for al in alphabet:
    for char in word:
        if char == al[0]:
            al[1] += 1

for al in alphabet:
    print(al[1], end=" ")