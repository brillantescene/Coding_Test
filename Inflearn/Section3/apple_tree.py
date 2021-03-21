import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
# 방법 1

trees = [[]]*n
apples = 0

x = n // 2 + 1
for i in range(n):
    trees[i] = list(map(int, input().split()))
    if n//2 >= i:
        x -= 1
    else:
        x += 1
    y = n - x
    for j in range(x, y):
        apples += trees[i][j]
print(apples)


# 방법 2
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
