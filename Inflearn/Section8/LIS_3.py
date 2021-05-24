# 가장 높은 탑 쌓기
import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
bricks = [list(map(int, input().split())) for _ in range(n)]
bricks.sort(reverse=True)
dy = [0]*n
dy[0] = bricks[0][1]
res = bricks[0][1]

for i in range(1, n):
    max_h = 0
    for j in range(i-1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = max_h + bricks[i][1]
    res = max(res, dy[i])
print(res)
