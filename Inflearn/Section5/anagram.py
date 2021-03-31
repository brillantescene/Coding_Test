import sys
sys.stdin = open('Inflearn/in5.txt', 'r')
'''
word = [input() for _ in range(2)]
dic = {}
for i in range(2):
    dic[i] = {x: 0 for x in word[i]}
    for x in word[i]:
        dic[i][x] += 1
for x in word[0]:
    dic[1][x] -= 1
for v in dic[1].values():
    if v:
        print("NO")
        break
else:
    print("YES")
'''
a = input()
b = input()
dic = {}
for x in a:
    dic[x] = dic.get(x, 0) + 1
for x in b:
    dic[x] = dic.get(x, 0) - 1
for x in a:
    if dic[x]:
        print("NO")
        break
else:
    print("YES")
