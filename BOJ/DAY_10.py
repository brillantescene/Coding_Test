# 210201 MON
# 10808
import sys
word = input()
alpha = {i: -1 for i in 'abcdefghijklmnopqrstuvwxyz'}
for i in range(len(word)):
    if alpha[word[i]] == -1:
        alpha[word[i]] = i
for i in alpha.keys():
    print(alpha[i], end=' ')

# 10820
for word in sys.stdin.read().splitlines():
    report = [0, 0, 0, 0]
    for i in word:
        if i.islower():
            report[0] += 1
        elif i.isupper():
            report[1] += 1
        elif i.isdigit():
            report[2] += 1
        else:
            report[3] += 1
    print(' '.join(map(str, report)))

# 2743
print(len(input()))

# 11655
lower = [i for i in 'abcdefghijklmnopqrstuvwxyz']
upper = [i for i in 'abcdefghijklmnopqrstuvwxyz'.upper()]
plain = input()
cipher = []
for i in range(len(plain)):
    if plain[i].isupper():
        j = upper.index(plain[i])+13 if upper.index(plain[i]) + \
            13 < 26 else upper.index(plain[i])+13 - 26
        cipher.append(upper[j])
    elif plain[i].islower():
        j = lower.index(plain[i])+13 if lower.index(plain[i]) + \
            13 < 26 else lower.index(plain[i])+13 - 26
        cipher.append(lower[j])
    else:
        cipher.append(plain[i])
print(''.join(map(str, cipher)))
# 다른 사람들꺼 보니까 아스키 썼음 호오

# 10824
a, b, c, d = map(int, input().split())
print(int(str(a)+str(b))+int(str(c)+str(d)))

a, b, c, d = input().split()
print(int(a+b)+int(c+d))
# 이 두 개 중에 위에꺼가 더 빨리됨. 뭐지 ?

# 11656
word = input()
dic = []
for i in range(len(word)):
    dic.append(word[i:])
print('\n'.join(map(str, sorted(dic))))
