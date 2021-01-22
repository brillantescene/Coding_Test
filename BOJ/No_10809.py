word = input()
alphabet = [[al, -1] for al in "abcdefghijklmnopqrstuvwxyz"]

for i in range(len(word)):
    for al in alphabet:
        if al[0] == word[i]:
            if al[1] != -1:
                continue
            else:
                al[1] = i


for al in alphabet:
    print(al[1], end=" ")