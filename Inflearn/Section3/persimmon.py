import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
yard = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(int(input())):
    a, b, c = map(int, input().split())

    if b:
        for _ in range(c):
            yard[a-1].insert(0, yard[a-1].pop())
    else:
        for _ in range(c):
            yard[a-1].append(yard[a-1].pop(0))

# 모래시계 계산 방법 1
x = -1
for i in range(n):
    y = 0
    if i <= n // 2:
        x += 1
        y = n-i
    else:
        x -= 1
        y = i+1
    for j in range(x, y):
        res += yard[i][j]
print(res)

# 모래시계 계산 방법 2
s, e = 0, n
for i in range(n):
    for j in range(s, e):
        res += yard[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
