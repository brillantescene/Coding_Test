import sys
from collections import deque

sys.stdin = open('Inflearn/in5.txt', 'r')

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

dq = deque()

n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if island[i][j] == 1:
            island[i][j] == 0
            dq.append((i, j))
            while dq:
                tmp = dq.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and island[x][y] == 1:
                        dq.append((x, y))
                        island[x][y] = 0
            cnt += 1
print(cnt)
