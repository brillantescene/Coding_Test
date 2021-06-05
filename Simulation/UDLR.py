n = int(input())
plan = list(map(str, input().split()))
board = [[0]*n for _ in range(n)]

d = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
x = y = 1

for p in plan:
    if 0 < x + d[p][0] <= n:
        x += d[p][0]
    if 0 < y + d[p][1] <= n:
        y += d[p][1]
    print(x, y)

print(x, y)
